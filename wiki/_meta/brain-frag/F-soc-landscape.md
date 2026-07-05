## SoC / 硬件版图 (On-Device Brain SoC Landscape)

> The on-device "brain" for embodied AI is not one chip but a **tiered market** stratified by TOPS and price, and increasingly by a **brain-cerebellum (大脑-小脑) integration** question: whether cognition (VLA perception/policy) and hard-real-time motor control live on one die or two. As of 2026-07, NVIDIA Jetson Thor anchors the high end, Qualcomm Dragonwing IQ10 is the credible ~700 TOPS challenger, and a dense Chinese tier (Horizon/D-Robotics, Black Sesame, Rockchip, Ascend) undercuts on price. Critically, the binding constraint on large VLA policies at real-time rates is **memory bandwidth, not raw TOPS** — a spec-sheet TOPS number does not predict usable control-loop frequency.

### High-end: the humanoid-brain reference class

| SoC / Module | Peak AI compute | Memory / BW | Power | Price | Status (as of 2026-07) |
|---|---|---|---|---|---|
| **NVIDIA Jetson AGX Thor (T5000)** | 2,070 FP4 sparse TFLOPS; Blackwell GPU (2,560 CUDA + 96 Tensor cores); 14-core Neoverse-V3AE | 128 GB LPDDR5X @ **273 GB/s** | 40–130 W | $3,499 dev kit | GA 2025-08-25; de-facto high-end standard (primary) |
| **NVIDIA Jetson T4000** | 1,200 FP4 sparse TFLOPS | 64 GB LPDDR5X | 40–70 W | $1,999 @1k | Announced CES 2026-01; cost-tier Thor (primary) |
| **Qualcomm Dragonwing IQ10** | 700 TOPS (18 Oryon cores + NPU + GPU) | 64 GB LPDDR5x ECC / 512 GB UFS 4.0 | 12V/24V, −40→70 °C | — | Unveiled Computex 2026-06; GA Sept 2026 (primary) |
| **Tesla AI5** (custom) | ~2,500 INT8 TOPS/board *(unverified — no TOPS figure in primary tape-out coverage; ~8–10× compute vs AI4 is the cited metric)*; Musk claims ~H100-class single-chip <150 W | 192 GB LPDDR5X (~9× capacity / ~5× BW vs AI4, relative) | <150 W (claim) | captive | Taped out 2026-04-15 (TSMC AZ + Samsung TX, **3 nm**); volume mid–late 2027; Optimus + Cybercab/supercluster first (secondary) |

- NVIDIA states Thor delivers **7.5× AI compute** and **3.5× energy efficiency** vs Jetson AGX Orin (primary).
- Thor T5000 also carries 1 TB NVMe + 100GbE — a full data-center-in-a-torso spec, not a microcontroller (primary).
- Dragonwing IQ10 is engineered to drop into Thor's socket-class role: natively **12 GMSL2 cameras** (3× MAX96724) + LiDAR/ToF/IMU, 2×10GBase-T + 2.5G + 4×1G EtherCAT, **8 CAN-FD**, Wi-Fi 7 + 5G. 10 early-access partners (incl. NEURA Robotics, Thundercomm) got units June 2026 (primary).

### Incumbent / legacy workhorse

- **Jetson AGX Orin** — 275 INT8 TOPS, 64 GB, 15–60 W, ~$1,999 dev kit — is still the production incumbent in shipping robots as of mid-2026 (secondary). Unitree **G1** standard configs ship on Orin, **not** Thor; Unitree **H1-2** spec lists up to 3× Jetson Orin NX alongside an Intel Core i5/i7 (secondary).
- Migration to Thor is beginning, not done: NVIDIA's **Isaac GR00T Reference Humanoid** (Unitree co-design: H2 Plus + Sharpa Wave + Thor T5000) reaches academic users first, general Unitree availability slated **2026-10** (primary).
- First Thor-in-a-humanoid design win: **Galbot G1 Premium**, claiming the full 7.5×/3.5× jump; Galbot G1 robots run autonomously in **10+ Beijing pharmacies**, targeting **100+ nationwide by end-2026** (secondary).

### Chinese domestic tier (price-led, brain-cerebellum fusion)

| Chip / board | AI compute | Notable trait | Named designs |
|---|---|---|---|
| **D-Robotics RDK S100 / S100P** (Horizon Robotics subsidiary; Nash BPU) | 80 / 128 TOPS (INT8) | **Brain+cerebellum on one die** ("CPU+BPU+MCU"): 6× Cortex-A78AE + Nash BPU + 4× Cortex-R52+ (1× DCLS lockstep + 1× Split-Lock) for hard-real-time control; ¥2,799 (~$390) at launch 2025-06-11 | pitched at "~half NVIDIA price, same compute" (secondary) |
| **D-Robotics Sunrise5/X5** | ~10 TOPS BPU | octa-A55 @1.5 GHz, dual 4-lane MIPI CSI-2, CAN FD, PoE; low-end China BPU standard | RDK X5 board; Quectel SH602HA-AP module (primary) |
| **Black Sesame Huashan A2000 + Wudang C1236** | A2000 claimed ≈ 4× Orin-X | **Two-chip** brain (A2000, "Jiushuo" NPU) + cerebellum (C1236) | Wuhan Univ. "Tianwen" humanoid; CES 2026-01 (secondary) |
| **Rockchip RK3588/S** | 6 TOPS NPU | 8-core (4×A76+4×A55), INT4/8/16+FP16; entry tier | AgiBot Lingxi X2, LimX Oli, Gaoqing Pi/Pi+ (secondary) |
| **Huawei Ascend 310 family** | up to 176 TOPS/chip; 352 TOPS dual | Orange Pi AI Studio Pro (2×310, 192 GB RAM) — **dev-kit packaging, not a confirmed in-robot design win** | domestic Thor-tier alt (secondary) |

- The **split-brain collapse** is the defining China architecture bet: D-Robotics' RDK S100 (Horizon Robotics' robotics arm) fuses cognitive AI and Lock-Step motion control onto one SoC; Black Sesame keeps them as two purpose-built chips. Both attack NVIDIA's implicit "big GPU SoC + separate MCU" pattern (secondary).
- China-vs-NVIDIA price gap is explicit vendor marketing: D-Robotics prices RDK S100 (80–128 TOPS) at "roughly half of an NVIDIA equivalent-TOPS solution" — note the TOPS metrics differ (Horizon Nash-BPU INT8 TOPS vs NVIDIA FP4-sparse TFLOPS), so this is a marketing claim, not an apples-to-apples benchmark (secondary).

### Qualcomm mid-tier (module ecosystem)

- **QCS8550/QCM8550** — 48 INT8 TOPS / 12 FP16 TOPS; Kryo 8-core (1×X3 @3.2 GHz + A710/A715), Adreno 740, 8th-gen AI Engine with INT4/FP16 + transformer "micro-tile inferencing" (primary).
- Packaged by **Quectel** (SG885G) and **MeiG Smart** (SNM970). MeiG's **dual-SNM970** design (~100 TOPS combined) powers the **通天晓 / Ultra Magnus** humanoid — claimed first fully Qualcomm-SoC on-device-AI humanoid (partner AidLux/阿加犀, CES 2025) (secondary).
- **Thundercomm TurboX IRB10** packages Dragonwing IQ10 into a humanoid-named SoM: peak 700 TOPS, 20 concurrent cameras (Embedded World 2026) — the "peak-compute threat" to the ~48–100 TOPS module tier (Quectel/MeiG) (primary).

### The real constraint: memory-bandwidth wall, not TOPS

- For a **7B-parameter VLA** (LLaMA-2-7B-scale) at <1 ms/token (needed for >1 kHz control responsiveness), a back-of-envelope estimate puts required memory bandwidth at **~13.67 TB/s** *(unverified — a derived figure, not stated in the cited XPU-characterization paper; magnitude is precision-dependent: a 7B model in FP16 reads ~14 GB/token ⇒ ~14 TB/s at 1 ms, ~4 TB/s if 4-bit)* — roughly **50× Jetson Thor's 273 GB/s**. The cited work does confirm the qualitative claim: VLA action-expert inference is **memory-bound, not compute-bound** on edge accelerators (secondary).
- Fixed-function NPUs (Qualcomm NPU, Horizon BPU) map MACs well but **not attention/softmax/layernorm**, forcing CPU/DSP fallback on VLA transformer layers — a structural argument for **GPU-class (Jetson)** over pure-NPU at the high end (secondary).
- Concrete gap: **LiteVLA-Edge** reports fully on-device multimodal control at **150.5 ms/step (~6.6 Hz)** on Jetson AGX Orin — using a 4-bit (Q4_K_M) SmolVLM-256M backbone on the llama.cpp CUDA runtime, all 42 layers GPU-offloaded — far below the >100 Hz–1 kHz whole-body-control target. Note this is a small (256M) VLM, so even a well-under-billion-param policy already caps at ~6.6 Hz on Orin. This is exactly **why perception/policy and low-level joint control are split** across separate compute (the split-brain pattern) (secondary).
- Sensor firehose motivating on-device inference: a 12-camera + 3D-LiDAR humanoid reportedly generates **~4.7 GB/s** raw sensor data; a separate **RISC-V safety watchdog** core is cited hitting **18 µs fail-safe shutdown** to meet IEC 61508 **SIL-3** — *(unverified, single-source)*.

### Takeaways

- **Tiering, not a winner**: Thor ($3.5k, 2,070 TFLOPS) → IQ10/T4000 (~700–1,200) → Qualcomm modules (~48–100 TOPS) → Horizon/Black Sesame (China mid) → Rockchip (6 TOPS entry). Pick by price × real-time bandwidth budget, not headline TOPS.
- **Spec TOPS ≠ control Hz**: a 275-TOPS Orin yields only ~6.6 Hz even on a sub-billion-param VLA (LiteVLA-Edge, 256M, 4-bit); always validate against the actual policy's bandwidth and op-mix, not headline TOPS.
- **Architecture divergence**: NVIDIA/Qualcomm sell big-SoC-plus-MCU; China (Horizon RDK S100) bets on single-die brain-cerebellum fusion — a genuine fork worth tracking.

来源:
- https://developer.nvidia.com/blog/introducing-nvidia-jetson-thor-the-ultimate-platform-for-physical-ai/
- https://nvidianews.nvidia.com/news/nvidia-blackwell-powered-jetson-thor-now-available-accelerating-the-age-of-general-robotics
- https://developer.nvidia.com/blog/accelerate-ai-inference-for-edge-and-robotics-with-nvidia-jetson-t4000-and-nvidia-jetpack-7-1/
- https://www.nvidia.com/en-us/autonomous-machines/embedded-systems/jetson-thor/
- https://nvidianews.nvidia.com/news/nvidia-open-humanoid-robot-reference-design
- https://roboticsandautomationnews.com/2025/08/26/galbot-becomes-first-company-in-the-world-to-integrate-nvidia-jetson-thor-into-a-humanoid-robot/93911/
- https://www.engineering.com/galbot-adopts-nvidia-jetson-thor-for-robotics/
- https://www.semiaccurate.com/2026/06/01/qualcomm-releases-the-dragonwing-iq10-rrd-robotics-platform/
- https://docs.qualcomm.com/doc/87-A0789-1/87-A0789-1_REV_A_Qualcomm_Dragonwing_IQ10_Robotics_Reference_Design_Product_Brief.pdf
- https://www.qualcomm.com/internet-of-things/products/q8-series/qcs8550
- https://www.meigsmart.com/articledetail/496.html
- https://www.thundercomm.com/turbox-irb10-launches-at-embedded-world-2026/
- https://www.cnx-software.com/2025/06/30/d-robotics-rdk-x5-development-board-features-sunrise-x5-octa-core-soc-with-10-tops-bpu-for-ros-projects/
- https://www.hackster.io/news/d-robotics-launches-the-10-tops-edge-ai-rdk-x5-and-teases-the-96-tops-rdk-ultra-c88714dab9d5
- https://eu.36kr.com/en/p/3473485924538759
- https://www.equalocean.com/news/2026010821715
- https://www.cnx-software.com/2025/09/30/orange-pi-ai-studio-pro-huawei-ascend-310-ai-mini-pc-with-up-to-352-tops-192gb-ram/
- https://www.tomshardware.com/tech-industry/artificial-intelligence/orange-pi-ai-studio-pro-mini-pc-debuts-with-huawei-ascend-310-and-352-tops-of-ai-performance-also-features-up-to-192gb-of-memory-but-relies-on-a-single-usb-c-port
- https://www.orientdeck.com/tech-trend/ai-robotics/8895.html
- https://electrek.co/2026/04/15/tesla-ai5-chip-taped-out-musk-ai6-dojo3/
- https://www.notebookcheck.net/Tesla-AI5-FSD-computer-to-run-inference-10x-cheaper-than-Nvidia-AI-chips.1145221.0.html
- https://arxiv.org/pdf/2604.24447 — "Characterizing VLA Models across XPUs": VLA action-expert inference is memory-bound not compute-bound; cites Jetson Thor 273 GB/s (13.67 TB/s figure is a derived estimate, not from this paper)
- https://arxiv.org/pdf/2603.03380 — LiteVLA-Edge: 150.5 ms/step (~6.6 Hz) on Jetson AGX Orin, 4-bit Q4_K_M SmolVLM-256M, llama.cpp CUDA, 42 layers GPU-offloaded
- https://www.spheron.network/blog/ai-memory-wall-inference-latency-guide-2026/
