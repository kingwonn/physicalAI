## 端侧 VLA 推理算力需求 (On-Device Compute Requirements)

How much silicon does an on-device embodied brain actually need? The honest answer from 2026 measurement work is: **less "peak TOPS" and more memory bandwidth than the marketing decks imply**. The load-bearing bottleneck in a modern VLA (视觉-语言-动作模型) is not the vision/language backbone — it is the diffusion **action expert (动作专家)**, which is memory-bandwidth-bound on every edge chip tested. This section quantifies the real compute envelope, the gap between spec-sheet TOPS and delivered Hz, and where current edge silicon actually lands.

### 1. Baseline: π0 (2.7B) latency across the hardware ladder

The single most useful reference is **VLA-Perf** (arXiv 2602.18397), which benchmarks the same π0 (2.7B params, BF16, 10 denoising steps, action chunk = 50) across a full ladder, decomposed into vision encoder / VLM backbone / diffusion action expert (primary):

| Hardware | Class | Vision | VLM backbone | Action expert | E2E | Throughput |
|---|---|---|---|---|---|---|
| B100 | datacenter | 0.40 ms | 1.87 ms | 0.91 ms | **3.18 ms** | **314.4 Hz** |
| H100 | datacenter | — | — | — | **6.15 ms** | **162.5 Hz** |
| A100 | datacenter | — | — | — | **16.20 ms** | **61.7 Hz** |
| RTX 4090 | consumer | 4.02 ms | 19.79 ms | 7.25 ms | **31.06 ms** | **32.2 Hz** |
| Jetson Thor | **edge** | 6.06 ms | 20.30 ms | 26.20 ms | **52.57 ms** | **19.0 Hz** |

All numbers primary (VLA-Perf Table 3, §4.2). The edge-to-datacenter gap is **~16.5x** (Thor vs B100) on the *same* model. Note Thor's action-expert dominates (26.2 ms of 52.6 ms, ~50%), whereas on B100/4090 the VLM backbone dominates — a hardware-dependent inversion explained in §3.

### 2. Model size collapses frequency roughly linearly

Scaling π0 up is punishing on-device — frequency falls approximately linearly with parameter count, and edge/consumer parts OOM well before datacenter parts (primary, VLA-Perf Table 5, §4.3):

| Variant | Params | Jetson Thor | RTX 4090 | B100 |
|---|---|---|---|---|
| π0 | 2.7B | 19.0 Hz | 32.2 Hz | 314.4 Hz |
| π0-L | 9.1B | 3.9 Hz | 8.0 Hz | 73.6 Hz |
| π0-XL | 16.7B | 2.1 Hz | **OOM** | 39.7 Hz |
| π0-XXL | 81.3B | **OOM** | **OOM** | 9.6 Hz |

Design consequence: an on-device brain is realistically capped at the **~2–3B backbone** tier if it must run fully local at usable rates; anything ≥9B is single-digit Hz on the best edge chip available.

### 3. Why TOPS lies: the action expert is memory-bandwidth-bound

This is the mechanistic core. VLA-Perf reports operator intensity (算术强度, FLOPs/Byte) per component vs each chip's roofline ridge point (primary, Table 4, §4.2, Takeaway 2):

| Component | Operator intensity | Behavior |
|---|---|---|
| Vision encoder | 321.4 FLOPs/Byte | compute-bound (except on Thor) |
| VLM backbone | 542.8 FLOPs/Byte | compute-bound (except on Thor) |
| **Diffusion action expert** | **54.0 FLOPs/Byte** | **memory-bound on ALL hardware** |

| Chip | Ridge point (balance) | Implication |
|---|---|---|
| RTX 4090 | 163.7 | vision/VLM compute-bound; action memory-bound |
| B100 | 218.8 | vision/VLM compute-bound; action memory-bound |
| **Jetson Thor** | **1481.5** | **all three components memory-bound** |

Thor's ridge point is **~9x** a 4090's because its FLOPs-to-bandwidth ratio is wildly skewed toward compute (huge FP4 TOPS, only 273 GB/s). Everything falls left of the ridge → memory-bound → the headline TOPS number is simply not the binding constraint. A second independent study (arXiv 2604.24447, secondary) corroborates: inside one inference call the VLM backbone runs **>90% SM utilization** while the diffusion action expert only hits **20–40%** — a ~3x efficiency gap that peak-TOPS ratings cannot reveal.

### 4. The marketing-vs-delivered gap, quantified twice

Two separate gaps compound:

- **Roofline vs real kernels**: even the *theoretical* roofline overpredicts. Optimized Triton code reaches only **73–83%** of roofline — 1 cam: 14.7 ms roofline vs 20.0 ms real (73.3%); 3 cam: 30.4 vs 36.8 ms (82.6%) (primary, VLA-Perf Table 1, §3). Un-optimized deployments land further below.
- **Precision basis (FP4 headline vs BF16 reality)**: Jetson Thor's "**2070 FP4-sparse TFLOPS**" headline collapses to **~258 BF16 TFLOPS** — an ~8x gap — and most VLA policies run BF16, not FP4 (secondary, arXiv 2604.24447). That paper's *plain-BF16* on-device π0 measurement is even worse than VLA-Perf's FP4-tuned figure: **246 ms uncompiled → 163 ms compiled (~6.1 Hz)** on Thor; RTX 4090 102.3 → 35.2 ms (28.4 Hz); Ascend 310P 818 → 350 ms (2.86 Hz).

Takeaway: **always ask "TOPS at what precision, dense or sparse, and does my policy actually use that datatype?"** before trusting a spec.

### 5. Levers that matter (and one that doesn't)

- **Denoising steps cost real wall-clock; chunk size is near-free.** On B100 (chunk 50), going 10→50 denoising steps = **5x** action-expert latency and **2.15x** overall latency; action chunk size has "negligible effect" (primary, VLA-Perf §4.5, Takeaways 6). So chunk more actions per call freely; add diffusion steps only when accuracy demands it.
- **Diffusion >> autoregressive for the action head.** Diffusion action decoding is **~102x faster** than vanilla autoregressive (B100, chunk 50: 3.2 ms / 312.5 Hz vs 327.6 ms / 3.0 Hz); AR-parallel is only competitive at chunk ≤10 (primary, §4.6, Takeaways 7–8).
- **Long context (KV-cache growth) kills edge throughput.** On B100: 1 step = 3.2 ms/314 Hz/0.01 GB KV; 100 steps = 11.3 ms/88 Hz/1.3 GB; 1K steps = 85.2 ms/11.7 Hz/13.2 GB; 10K steps = 823.7 ms/1.2 Hz/131.8 GB. Edge/consumer GPUs are limited to **~100 past timesteps** in real time; only datacenter GPUs sustain ~1K (primary, Table 6, §4.4, Takeaway 5).
- **Quantization is not a free lunch for VLA.** A 4-bit NF4 backbone + FP32 head reached ~9x speedup, but INT4 on full OpenVLA gave only 1.14x with **9% success-rate degradation** (secondary) — unlike pure-LLM quantization, VLA task success can degrade materially.

### 6. Where real edge silicon lands (the compute ladder)

Spec-sheet TOPS across the parts an on-device brain designer actually chooses (all figures with precision/sparsity basis called out — they are **not** cross-comparable without it):

| Tier | Part | Headline compute | Basis | Memory / BW |
|---|---|---|---|---|
| Module | Qualcomm QCS8550 | 48 TOPS | INT8 (HTP/NPU) | 8/16 GB LPDDR5X @4200 |
| Module | Qualcomm Dragonwing Q-8750 | 77 TOPS dense; up to 11B LLM | dense | (SD 8 Elite class) |
| Jetson | Orin Nano | 67 TOPS | INT8 sparse | 7–25 W |
| Jetson | Orin NX | 157 TOPS | INT8 sparse | 10–40 W |
| Jetson | AGX Orin | 275 TOPS | INT8 sparse | 15–60 W |
| High-end | Qualcomm Dragonwing IQ10 | 700 TOPS sparse (350 dense) | sparse | 18 Oryon CPU + NPU + GPU |
| High-end | **NVIDIA Jetson Thor** | **2070 TFLOPS** (~258 BF16) | **FP4 sparse** | 128 GB LPDDR5X, **273 GB/s**, 40–130 W |

All primary except the Thor BF16 figure (secondary). Thor claims 7.5x perf / 3.5x energy-efficiency vs AGX Orin (primary). The IQ10 (Thundercomm TurboX IRB10 reference design, up to 20 cameras) is the current "700-TOPS humanoid tier" (primary).

### 7. The bandwidth wall at servo rates

Compute headroom does not solve the highest-frequency loop. One aggregator estimate puts a π0/GR00T-class policy at **~1,750 GB/s** to sustain **500 Hz** servo-level control — **6.4x** Thor's actual 273 GB/s (unverified). Even if approximate, it confirms the structural gap: today's edge silicon is **bandwidth-starved** for the S1 (motor-servo) loop, independent of TOPS headroom. This is *why* the dual-system split (fast tiny local S1, slower VLM S2) exists — you cannot brute-force 500 Hz VLA inference on-device with 2026 edge memory subsystems.

### 8. Design targets and takeaways

VLA-Perf's explicit Hz bands: **10 Hz = "acceptable"** (near camera frame rate); **100 Hz = "high-performance"** (exceeds typical video ingest) (primary, §4.11).

- **On-device (Thor) already clears 10 Hz** with π0 (19 Hz), but reaching 100 Hz needs **~5x** more via compression/quantization (Takeaways 13, primary).
- **Server-side offload beats on-device on fast/medium links** — B100 server *total* latency (3.18 ms compute + network round-trip): **3.3 ms (Ethernet 10G) / 8.4 ms (WiFi7) / 27.8 ms (5G) / 73.0 ms (4G)** vs Thor on-device **52.57 ms**. So Ethernet/WiFi7/5G all beat local, but the **4G path (73.0 ms) is *slower* than Thor on-device** — offload is a win only where the link is decent (primary, §4.7, Table 8, Takeaway 9). Fully-local is a *policy/privacy/uptime* choice; latency-wise it only wins when the link degrades to 4G-class or worse.
- **Async S1/S2 overlap recovers throughput — most on fast links** (where S1 can run at high native frequency): B100 async speedup (S2 cap 10 Hz) **2.24x (Eth 10G) → 1.26x (WiFi7) → 1.05x (5G)**; dual-system gives **1.30x on Thor on-device** (10 Hz S2 cap). No 4G async row is reported (primary, Table 9).

**Bottom line for an on-device brain**: size the backbone at ~2–3B, run the diffusion action expert (bandwidth-bound — maximize memory BW, not TOPS), keep denoising steps low and chunks long, cap local context near ~100 timesteps, and budget the servo loop as a *separate* tiny reflex net because no 2026 edge chip has the bandwidth to run full VLA inference at servo rates.

来源:
- https://arxiv.org/abs/2602.18397 ; https://arxiv.org/html/2602.18397v1 — VLA-Perf: π0 latency ladder, roofline/memory-bound analysis, denoising/chunk/context sweeps, Hz targets (primary)
- https://arxiv.org/abs/2604.24447 — Characterizing VLA Models across XPUs: BF16 π0 latencies, SM-utilization gap, FP4-vs-BF16 spec gap (secondary)
- https://www.nvidia.com/en-us/autonomous-machines/embedded-systems/jetson-thor/ ; https://blogs.nvidia.com/blog/jetson-thor-physical-ai-edge/ — Thor spec (primary)
- https://www.nvidia.com/en-us/autonomous-machines/embedded-systems/ — Jetson Orin family TOPS ladder (primary)
- https://www.qualcomm.com/products/internet-of-things/industrial/industrial-processors/qcs8550 — QCS8550 48 TOPS INT8 (primary)
- https://www.qualcomm.com/products/technology/processors/dragonwing — Dragonwing Q-8750 (77 TOPS) & IQ10 (700 TOPS sparse) (primary)
- https://www.thundercomm.com/product/turbox-irb10/ — TurboX IRB10 / IQ10 reference design, 20-camera (primary)
