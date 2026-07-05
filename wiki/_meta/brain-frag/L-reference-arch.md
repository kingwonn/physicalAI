## 参考架构 & 模组厂视角 (Reference Architecture & the Module-Maker Read)

> Stepping back from the dual-system model (see [Architecture](#)) and the SoC menu (see [SoC landscape](#)), the field has converged on a **3-tier control hierarchy** that any on-device brain must physically instantiate: an **S2 deliberative VLM** (7–10 Hz), an **S1 reactive visuomotor policy** (100–200 Hz), and an **S0 hard-real-time motor/reflex loop** (500 Hz–1 kHz). S2/S1 live on the AI SoC; S0 lives on a deterministic MCU / co-processor / Safety Island, decoupled from the Linux clock domain. For a module-maker (模组厂) the load-bearing insight is that the **hard part is not the TOPS number** — it is stitching this heterogeneous, jitter-partitioned, non-portable stack into one shippable module with connectivity and functional safety built in.

### The converged 3-tier reference stack

| Tier | Role | Rate | Silicon / clock domain | OS / runtime | Latency budget |
|---|---|---|---|---|---|
| **S2** deliberative | scene/language understanding, planning | **7–10 Hz** | AI SoC GPU (Jetson) or NPU+CPU | Ubuntu + PREEMPT_RT; TensorRT/QNN/BPU | ~100–140 ms/step OK; cloud-offloadable |
| **S1** reactive | VLA/visuomotor policy → continuous action chunks | **100–200 Hz** | AI SoC GPU/NPU | same SoC, soft-RT (ROS2) | **8.3 ms @ 120 Hz** — must stay local |
| **S0** hard-real-time | joint/torque/servo loop, reflex, safe-stop | **500 Hz–1 kHz+** | deterministic **MCU / RTOS / Safety Island** | bare-metal / RTOS | **sub-ms**, zero OS jitter tolerated |

- **Figure Helix (primary)**: S2 = 7B internet-pretrained VLM @ 7–9 Hz; S1 = 80M cross-attn enc-dec transformer @ 200 Hz; S2 emits a **single continuous latent vector** into S1's token space; both run **entirely onboard on dual low-power embedded GPUs**. [figure.ai/news/helix]
- **NVIDIA GR00T N1 (primary)**: S2 (Eagle-2 VLM) @ **10 Hz** (paper benchmarks this on an NVIDIA L40); S1 (diffusion-transformer, flow-matching action head) @ **120 Hz**; the two modules are **jointly trained end-to-end**. Public GR00T-N1-2B = 2.2B params total (1.34B in the VLM). Below both sits a whole-body torque loop ~1000 Hz (GR1-class) offloaded to MCU/RTOS. [arXiv 2503.14734]
- The S0 tier is exactly the layer that **cannot tolerate software/OS jitter** — hence its physical exile to a separate deterministic co-processor. This is the same "split-brain" boundary the China single-die SoCs (D-Robotics RDK S100: 6× A78AE + BPU + **4× Cortex-R52+ lockstep**) try to collapse onto one package while keeping the R52 cores in a **separate hard-RT island** on-die (secondary). [F-soc-landscape.md]

### S0 fieldbus: how the reflex tier talks to actuators

- The S0 loop runs over **EtherCAT and/or CAN-FD** fieldbus, **decoupled from the Linux/AI-SoC clock domain** (secondary):
  - EtherCAT humanoid control architectures reach **1 kHz update, control rates >2 kHz, I/O latency <1 ms**; EtherCAT slaves verified error-free across **1 kHz–9 kHz** (secondary — researchgate/mediatum humanoid papers).
  - **CAN-FD** is described as ideal for synchronized multi-axis robotic systems needing deterministic timing (secondary — TI slla659a).
  - Dexterous-hand datapoint: **BrainCo Revo 2** supports max comms frequency **1 kHz across RS-485, CAN-FD, and EtherCAT alike** (secondary).
- Module-maker read: the flagship compute SoCs now bake these buses in — **Qualcomm Dragonwing IQ10** ships **EtherCAT (4× 1G Base-T)** + **8× CAN-FD (4× native + 4× external via SPI)** + TSN-ready Ethernet + a segmented **2.5G Base-T safety-domain (SAIL) link**; the fieldbus is no longer a bolt-on FPGA (primary — docs.qualcomm.com IQ10 product brief 87-A0789-1 Rev. A).

### The high-end silicon choice for S1/S2 (see also [SoC landscape])

| SoC | Peak AI | Memory / BW | Power | Price | S0 story |
|---|---|---|---|---|---|
| **Jetson AGX Thor (T5000)** | 2,070 FP4-sparse TFLOPS; Blackwell (2,560 CUDA+96 Tensor); 14-core Neoverse-V3AE | 128 GB LPDDR5X @ **273 GB/s** | 40–130 W | $3,499 dev kit; GA 2025-08-25 | separate MCU (implicit) |
| **Jetson T4000** | 1,200 FP4 TFLOPS | 64 GB LPDDR5X | 40–70 W | ~$1,999 @1k; CES 2026 | separate MCU |
| **Qualcomm Dragonwing IQ10** | ~700 TOPS sparse (18 Oryon CPU + NPU + GPU) | 64 GB LPDDR5x | 12/24 V | early-access June 2026; GA Sept 2026 | **on-die Safety Island (SAIL)** |

- Thor claims **7.5× AI compute / 3.5× energy efficiency vs Orin**; carries 1 TB NVMe + 100GbE; NVIDIA's own **Isaac GR00T Reference Humanoid** = Unitree H2 Plus + Sharpa Wave hands + Thor onboard + Isaac GR00T SW (primary).
- **IQ10's SAIL is the architectural tell**: a hardware-isolated Safety Island keeps braking/obstacle-avoidance executing **even if the primary OS throws a software exception** (secondary — Qualcomm launch press; the product brief itself states only "safety island + domain separation supports functional-safety architectures") — i.e., the S0 deterministic co-processor is **built into the compute-tier silicon**, not a discrete MCU. I/O per the brief: **2× 10G Base-T (main domain) + 1× 2.5G Base-T (SAIL safety domain)**, **8× CAN-FD (4× native + 4× external via SPI)**, **EtherCAT 4× 1G Base-T**, TSN-ready Ethernet, up to **12 GMSL2 cameras** (3× MAX96724 — secondary) + LiDAR/ToF/IMU, **Wi-Fi 7 + BT; 5G modem optional add-on**. Early-access units seeded to enterprise customers **June 2026** (Thundercomm confirmed via TurboX IRB10; "10 partners / NEURA" *unverified*).

### The two binding constraints (why the tiers exist at all)

- **Memory bandwidth, not TOPS, is the wall (secondary).** VLA action-expert inference is **memory-bound, not compute-bound** on edge accelerators (arXiv 2604.24447). Spec-sheet TOPS does **not** predict achievable Hz:
  - **LiteVLA-Edge**: fully on-device at only **150.5 ms/step (~6.6 Hz)** on Jetson AGX Orin (4-bit SmolVLM-256M, all 42 layers GPU-offloaded) — far under the >100 Hz–1 kHz target despite Orin's 275 INT8 TOPS (secondary, arXiv 2603.03380).
  - Fixed-function NPUs (Qualcomm NPU, Horizon BPU) map MACs but **not attention/softmax/layernorm**, forcing CPU/DSP fallback on VLA transformer layers — a structural argument for **GPU-class silicon over pure-NPU** at the high end (secondary).
- **Real Thor VLA numbers quantify why heavy reasoning gets exiled to S2/cloud (primary, arXiv 2602.18397 VLA-Perf):**

  | Model | On-device rate (Jetson Thor) | Notes |
  |---|---|---|
  | π0 baseline | **19.0 Hz** (52.57 ms/step) | vision enc 6.06 + VLM 20.30 + action expert 26.20 ms |
  | π0-L (9.1B) | 3.9 Hz | larger backbone degrades sharply |
  | π0-XL (16.7B) | 2.1 Hz | — |
  | π0 + 1K-timestep context | 1.3 Hz (768.3 ms) | long context kills it |
  | π0 baseline on **H100** | **162.5 Hz** | ~100×+ edge-vs-datacenter gap |
  | π0 baseline on **B100** | **314.4 Hz** | — |

  Diffusion-based action decoding is **102.4× faster** than vanilla autoregressive with chunking (primary) — the mechanism that lets a not-real-time stack still hit S1 rates.

### Hybrid edge-cloud is sound for S2 only

- Network latency (tens of ms on 5G/WiFi, >100 ms on poor LTE) **categorically exceeds** the S1 budget (**8.3 ms @ 120 Hz**), so only the S2/deliberative tier is cloud-offloadable — and it works there because S2 output can be **buffered/decoupled from RTT** (primary).
  - **"Speculative Policy Orchestration"** (arXiv 2603.19418): streams pre-computed waypoints from a cloud world-model into a local edge buffer, ε-tube verifier + Adaptive Horizon Scaling; **60% less network-induced idle time**, ~60% fewer discarded cloud predictions vs static caching (primary).
  - Async inference over 5G + datacenter B100 yields **5.99× throughput** vs synchronous cloud (35.9 Hz sync → 215.3 Hz async; VLA-Perf Table 8); async speedup peaks at **13.79×** under 4G + slow-cloud (3.7 → 50.5 Hz) — the worse the link, the more decoupling buys (primary, VLA-Perf).
- **Location alone is not the lever — model size/quantization is (primary, arXiv 2601.14921):** on a Unitree G1-EDU + NVIDIA L4 24GB edge node, LLaMA-3.2-11B-Vision (4-bit) ran **1600 ms edge vs 1685 ms cloud — only ~5% faster**; Qwen2-VL-2B ran **sub-second**. Text generation dominates >85% of latency regardless of location. **Right-size + quantize; don't just relocate a big model to the edge.**
- **MEC/5G** infrastructure can hit **5–10 ms end-to-end** vs >50 ms traditional cloud *(unverified — web synthesis, not pinned to one paper)* — the basis for treating cellular connectivity (a module-maker's core competency) as **infrastructurally load-bearing** for the S2 cloud-assist tier, not a nice-to-have.

### The software stack has also converged (and it's non-portable)

- De-facto pattern (primary): **Ubuntu 22.04 + PREEMPT_RT** (or vendor RTOS) on the AI SoC for perception/planning/VLA, glued via **ROS2** (soft-RT middleware), with **per-vendor non-portable inference runtimes** (TensorRT / QNN / BPU toolchain), plus a **separate bare-metal MCU/RTOS** owning the S0 loop.
  - PREEMPT_RT merged to mainline only in **kernel 6.12 (Sept 2024)**, ending ~20 years out-of-tree — but remains **soft real-time only**, which is *why* the dedicated S0 MCU is universal. ROS2's RT story is still "probabilistic/soft, not hard" as of 2025–26 (primary; arXiv 2601.10722 et al.).
- **Runtimes are genuinely non-portable — this is the module-maker moat (primary):** NVIDIA's own docs state *"an engine built on RTX 4090 will not work on H100."* A D-Robotics BPU model won't run on Jetson; a Qualcomm QNN graph runs on neither. D-Robotics ships a dedicated **rdk_LeRobot_tools** porting layer (PyTorch→ONNX→Horizon→.hbm), currently verified **for ACT policies only** on RDK S100 — the same open policy code needs **N separate vendor stitch-jobs** to deploy. "Middleware support" is a real differentiator, not a commodity.

### Functional safety maps onto the S0 layer

- Humanoid FuSa practice requires an **independent hardware watchdog/interlock enforcing safe-motion bounds that survives OTA-updated software failing**, targeting **IEC 61508 SIL-2/SIL-3** (secondary, automate.org/QNX). Guidance ties this explicitly to OTA: use independent interlocks/watchdogs *because* higher-level software is remotely updated.
- A cited hazard-detection/intervention system reports **>99% reliability** framed as SIL-2 risk reduction (secondary, arXiv 2603.22703). A separately-reported RISC-V safety-watchdog core claims an **18 µs fail-safe shutdown** targeting SIL-3 *(single-source, unverified)*.
- This requirement lands **directly on the deterministic MCU / Safety Island** tier — and is another reason IQ10's on-die SAIL is a strategic bet: the safety co-processor becomes part of the sold silicon.

### The module-maker (模组厂) read

- **The wedge is integration, not compute.** The reference stack is a heterogeneous, jitter-partitioned mess — big-SoC (S2/S1) + deterministic MCU/island (S0) + fieldbus (EtherCAT/CAN-FD) + connectivity (5G/Wi-Fi for the S2 cloud-assist tier) + a non-portable per-vendor runtime + a FuSa watchdog. A module-maker that ships this **pre-integrated, with the porting layer and cellular stack done**, sells the scarce thing.
- **Connectivity is load-bearing, not peripheral** — because MEC/5G is the enabling substrate for the only cloud-offloadable tier (S2). This is precisely where a cellular-module vendor's core competency slots in.
- **Concrete shipping instance — Quectel SH602HA-AP (partial; single-source on module SKU details):** a module-maker's on-device-brain module built on **D-Robotics Sunrise5 (X5M)** (up to **10 TOPS BPU**), Ubuntu OS, **4 GB LP4/LP4x RAM + 64 GB storage** default (40.5×40.5×2.9 mm; launched CES 2026), pairs with Quectel's own **LTE Cat1/Cat4/5G/Wi-Fi6/GNSS** modules for connectivity, and supports VSLAM / binocular depth / 3D point cloud / Transformer-BEV-Occupancy models + LiDAR. It sits at the **low end (10 TOPS, S1-lite/perception tier)**, not the Thor/IQ10 flagship — but it is a real, shipping proof that the "arms-dealer" module play (compute die + connectivity + OS pre-integrated) exists today. [F-soc-landscape.md, Quectel product page]

来源:
- https://www.figure.ai/news/helix
- https://arxiv.org/abs/2503.14734
- https://arxiv.org/abs/2602.18397 — VLA-Perf: π0 on Jetson Thor 19.0 Hz; π0-L 3.9 Hz; π0-XL 2.1 Hz; H100 162.5 Hz / B100 314.4 Hz; diffusion 102.4× vs autoregressive
- https://arxiv.org/abs/2603.19418 — Speculative Policy Orchestration: 60% less network-idle time; ε-tube verifier + Adaptive Horizon Scaling
- https://arxiv.org/abs/2601.14921 — VLMs on the Edge: 11B-Vision 1600 ms edge vs 1685 ms cloud (~5%); Qwen2-VL-2B sub-second; text-gen >85% of latency
- https://arxiv.org/abs/2604.24447 — Characterizing VLA across XPUs: memory-bound not compute-bound
- https://arxiv.org/abs/2603.03380 — LiteVLA-Edge: 150.5 ms/step (~6.6 Hz) on Jetson AGX Orin, 4-bit SmolVLM-256M
- https://docs.qualcomm.com/doc/87-A0789-1/87-A0789-1_REV_A_Qualcomm_Dragonwing_IQ10_Robotics_Reference_Design_Product_Brief.pdf — IQ10 RRD: up to 700 TOPS sparse, 18× Oryon CPU + NPU + GPU, 64 GB LPDDR5x, Safety Island (SAIL 2.5G Base-T domain), 8× CAN-FD (4 native + 4 external via SPI), EtherCAT 4× 1G Base-T, 2× 10G Base-T main domain, up to 12 GMSL2 cameras, Wi-Fi 7 + BT, 5G optional; GA Sept 2026
- https://developer.nvidia.com/blog/introducing-nvidia-jetson-thor-the-ultimate-platform-for-physical-ai/ — Thor 2,070 FP4 TFLOPS, 128 GB @ 273 GB/s, 7.5×/3.5× vs Orin
- https://nvidianews.nvidia.com/news/nvidia-open-humanoid-robot-reference-design — Isaac GR00T Reference Humanoid (Unitree H2 Plus + Sharpa + Thor)
- https://en.wikipedia.org/wiki/PREEMPT_RT — mainline in kernel 6.12 (Sept 2024), soft-RT only
- https://www.ti.com/lit/an/slla659a — CAN-FD for deterministic multi-axis robotics
- https://automate.org/ — QNX/robot functional-safety: independent watchdog/interlock, IEC 61508 SIL-2/3, OTA rationale
- https://arxiv.org/abs/2603.22703 — Learning Safe-Stoppability Monitors for Humanoid Robots
