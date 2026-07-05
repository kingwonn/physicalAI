## 内存容量 / 并发调度 / 量产标定 (Memory, Concurrency & Bring-Up)

The on-device brain is a **fixed-capacity, mixed-criticality resource-allocation problem**: a multi-GB VLM (S2, slow 慢系统), a small action expert (S1, fast 快系统), VSLAM, ASR/TTS, and safety/watchdog code must all co-reside in one RAM pool and share one (or two) GPUs *without the 5-10Hz reasoning loop ever starving the 200Hz control loop*. This section budgets the RAM, picks a concurrency mechanism, and lists the量产 (bring-up/量产标定) taxes that early sizing routinely underestimates.

### 1. The silicon envelope (128GB Thor vs 64GB IQ10)

| Platform | Unified RAM | Mem BW / bus | AI compute | CPU | Power | Packaging | Src |
|---|---|---|---|---|---|---|---|
| **Jetson Thor** (T5000) | 128GB LPDDR5X | 273 GB/s / 256-bit | 2070 TFLOPS sparse FP4 · 1035 dense FP4 · 517 dense FP8; 2560 CUDA / 96 Tensor cores (Blackwell) | 14-core Arm Neoverse-V3AE @2.6GHz | 40–130W | bare SoM | (primary) |
| **Qualcomm Dragonwing IQ10** | 64GB LPDDR5x, ECC ("16×16 ECC-hardened controllers" *(unverified)*) | n/a published | 700 TOPS | 18-core Oryon (12×V3 large @5.0GHz + 6×V3 medium @3.6GHz) | -40–70°C, 12/24V in | **forced-air-cooled enclosed module**; ~176×125×75mm *(unverified — single-source)*; HW security island *(unverified — not in Qualcomm brief)*; ≤12× GMSL2 cam, 8K@120fps codec | (primary) |

- **Unified memory is the load-bearing Thor property** (primary): CPU-side perception pre-processing and GPU-side transformer inference share one address space, so there is **no PCIe copy tax at each S2/S1 handoff** — the tensor-transfer cost that a discrete-GPU design pays every tick.
- IQ10 ships **as a pre-integrated, forced-air-cooled enclosed module, not a bare SoC** (primary — Qualcomm confirms integrated forced-air cooling, -40–70°C, 12/24V), reportedly with a **hardware security island** *(unverified — the security-island framing appears only in single-source COMPUTEX coverage, not the Qualcomm product brief)* so safety/watchdog isolation is physical, not scheduled — a different answer to the same mixed-criticality problem Thor solves in software (§3).

### 2. RAM carve-up: what actually fits

The concurrency budget = **nominal capacity − firmware/kernel carveouts − Σ per-model footprint**, with **quantization** and **visual-token compression** as the two first-order levers before buying bigger silicon.

**S2 VLM footprint is the dominant term** (everything else is rounding error at 64–128GB):

| Model | Params | Inference mem | Fine-tune mem | Note | Src |
|---|---|---|---|---|---|
| **pi0** (Physical Intelligence) | ~3.3B (2.29B PaliGemma VLM + 315M flow-matching action expert) | **>8GB** floor (RTX 4090); ~14GB bf16 typical | LoRA >22.5GB; full >70GB (A100-80/H100); 40GB peak train @bs16 on A100-40 | canonical heavy S2 | (primary) |
| **SmolVLA** (smallest) | SmolLM2 135M/360M/1.7B + SigLIP-B/16 93M | **<1–5GB** (~2GB) | — | ~5–10× lighter than pi0 | (secondary) |

- The **pi0 ~14GB vs SmolVLA ~2GB** gap **is** the capacity-budgeting decision: choosing SmolVLA for S2 changes the whole RAM carve-up math by **5–10×** (secondary).
- **Worked concurrency example (NVIDIA's own, 8GB scale)** (primary): a 4-bit VLM (2.2GB) + ASR + TTS occupies **4.5 of 7.6GB usable (~60%)**. Methodology scales directly to 64–128GB. Quantization savings: Qwen3-8B FP16→W4A16 saves ~10GB; Qwen3-4B BF16→INT4 saves ~5.6GB.
- **Peripheral models are cheap** (secondary): neural-SLAM maps run **~75–290MB** on Orin NX 16GB; cuVSLAM hits **~143Hz (0.007s/frame)** with 0.94% translation / 0.0019°·m⁻¹ error (KITTI) on Xavier-class HW. The capacity fight is VLM/action-model-dominated, **not** mapping-dominated.

### 3. Concurrency: spatial partition (MIG) beats time-share (MPS)

The core failure mode: naively time-multiplexing S2 and S1 on one GPU lets the VLM's mid-flight kernel make the 200Hz loop miss deadlines.

| Mechanism | Behavior | Verdict for a robot brain |
|---|---|---|
| **NVIDIA MPS** | merges GPU contexts of sharing processes into one; **no priority-based preemption** (only a non-binding priority *hint*), default FIFO device queue → a low-prio job blocks a high-prio one for its full kernel duration (**priority inversion**); high-prio job-completion-time "several times higher than that of running exclusively" | **unsafe** for mixed-criticality (secondary, FIKIT arXiv 2311.10359) |
| **MIG (spatial)** | physical SM partition | **preferred** — control code cannot be starved (primary) |

- **JetPack 7.2 MIG on Thor** (primary): a **2-way fixed split**, not 7 arbitrary slices — a larger **AI/graphics slice (12 SMs / 1536 CUDA cores)** for VLM/render/general CUDA, and a smaller **isolated compute slice (8 SMs / 1024 CUDA cores)** reserved for robotics/control/perception/safety, so a runaway VLM job **physically cannot** starve the safety partition. Paired with a **Preemptible RT kernel** for deterministic mixed-criticality scheduling.
- **Figure Helix's answer: don't share at all** (primary): S2 (**7B VLM @7–9Hz**, async background process) and S1 (**80M cross-attention transformer @200Hz**, real-time process) run on **two separate physical embedded GPUs** — sidesteps contention entirely at the cost of 2× GPU silicon.

### 4. Reconciling the timescales: chunking is the pressure valve

Systems don't make the VLM faster; they **amortize one slow forward pass across many control ticks** via action chunking.

| System | S2 (slow) | S1 (fast) | Lever | Src |
|---|---|---|---|---|
| Figure Helix | 7B VLM @7–9Hz | 80M @200Hz | dual-GPU, async S2 | (primary) |
| DualVLN | 7B VLM @2Hz | diffusion policy @30Hz | — | (secondary) |
| FiS-VLA | — | **21.9Hz no-chunk → 117.7Hz with 8-step chunk** | action chunking | (secondary) |

- **A third, faster timescale exists** (secondary): tactile sensing for slip/vibration commonly samples at **1000Hz** (e.g. Robotiq fingertips) — **10× the S1 loop, 100–200× the S2 loop**. Raw tactile streams must be **decimated/compressed** before any transformer (TacMamba's "tactile history compression adapter", arXiv 2603.01700) — feeding raw high-rate tokens into a VLA backbone is bottlenecked by the backbone's inference speed.

### 5. Tokenization cost — vision dominates, and it's quadratic

- **Resolution → token count (SigLIP/PaliGemma patch-14)** (primary): 224px²→**256 tok**, 448px²→**1024 tok**, 896px²→**4096 tok**. Self-attention is quadratic in tokens, so 224→896px is a **16× token / much-larger-compute** jump. Each additional camera (humanoids carry stereo head + wrist cams) adds this **linearly per stream**.
- **Dual vision encoders double the cost** (secondary): OpenVLA runs **DINOv2 + SigLIP** (fused) before any LM compute — a common 2024-26 pattern that ~2× the visual-encode tax.
- **Token compression is a first-order lever, not just quantization** (secondary): "Think Twice, Act Once" (arXiv 2505.21200) shows visual tokens dominate VLA inference cost and cuts token count up to **50%** + action-reuse for **~40% speedup** with maintained success — available to OEMs *before* buying bigger silicon.
- **Recognized-open-problem check** (primary): **VLA-Perf** (NVIDIA, arXiv 2602.18397; github.com/NVlabs/vla-perf) is a dedicated 2026 analytical performance-model for exactly the on-device vs edge-server vs cloud VLA placement decision — its existence confirms this is an active gap, not a solved problem (full numeric tables were image-rendered, not text-extractable — treat specifics as unverified).

### 6. Bring-up / 量产标定 taxes (frequently underestimated)

- **Firmware/kernel carveouts are real fixed taxes** (primary): on 8GB Orin Nano only **~7.6GB is usable** (~400MB lost). Display carveouts ≤68MB (DCE 32MB, DISP_EARLY_BOOT_FB 34MB, DCE_TSEC/TSEC_DCE 1MB each); camera carveouts ≤33MB (CAMERA_TASKLIST 32MB, RCE 1MB). **Disabling the graphical desktop alone frees up to 865MB.** Proportionally smaller at 64–128GB but **non-zero** — budget them at sizing time.
- Multi-camera GMSL2 ingest (≤12× on IQ10) and 8K codec are fixed per-frame bandwidth/latency costs to standardize during 标定.
- ECC-hardened controllers (IQ10) trade a little capacity/latency for bit-error safety — a量产-reliability, not a benchmark, decision.

来源:
- developer.nvidia.com/blog/introducing-nvidia-jetson-thor-the-ultimate-platform-for-physical-ai
- developer.nvidia.com/blog/deploy-agentic-ready-ai-at-the-edge-with-memory-efficiency-in-nvidia-jetpack-7-2
- developer.nvidia.com/blog/maximizing-memory-efficiency-to-run-bigger-models-on-nvidia-jetson
- finance.sina.com.cn (COMPUTEX 2026 Qualcomm Dragonwing IQ10 coverage)
- github.com/Physical-Intelligence/openpi ; blog.phospho.ai (pi0 architecture)
- emergentmind.com/topics/smolvla ; arxiv.org/html/2504.05299 (SmolVLM)
- arxiv.org/html/2311.10359v5 (FIKIT — MPS context-merge / no-preemption / FIFO "several times higher than running exclusively") ; arxiv.org/pdf/2406.05221 (GCAPS — Tegra preemptive GPU scheduling; does NOT itself discuss MPS)
- figure.ai/news/helix
- openreview.net (FiS-VLA) ; arxiv.org/pdf/2512.20188 (Async Fast-Slow VLA survey)
- arxiv.org/abs/2602.18397 ; github.com/NVlabs/vla-perf (VLA-Perf)
- github.com/NVIDIA-ISAAC-ROS/isaac_ros_visual_slam
- arxiv.org/html/2412.03555v1 (PaliGemma 2) ; emergentmind.com/topics/openvla
- arxiv.org/pdf/2505.21200 (Think Twice, Act Once)
- blog.robotiq.com/robotiq-brings-the-sense-of-touch-to-physical-ai ; arxiv.org/pdf/2603.01700 (TacMamba)
