## 功耗 / 散热 / 成本工程 (Power, Thermal & Cost)

The on-device brain is not free silicon on a shelf — it is a heat source inside a sealed, moving robot on a battery budget. Three constraints bind together: **perf-per-watt** (每瓦性能) beats peak TOPS, **thermal design** (散热) sets the true sustained ceiling, and **cost tiering** (成本分层) means most robots should *not* buy the biggest brain. The engineering thesis: reduce precision (量化) to convert the same watts into more usable inference, then design the thermal path so those watts actually flush out before the SoC trips.

### 芯片级功耗与能效 (Chip-level power & efficiency)

Jetson AGX Thor is the reference "big-brain" module already cited in [hardware.md](../hardware.md)'s compute table; the numbers below are the design envelope it exposes.

| Metric | Jetson AGX Orin | Jetson AGX Thor (T5000) | Source |
|---|---|---|---|
| Power envelope | 15–60 W | **40–130 W** | NVIDIA blog (primary) |
| Peak AI compute | 275 TOPS INT8 | **2,070 TFLOPS FP4 sparse** / 1,035 dense FP4 / 517 dense FP8 | NVIDIA blog (primary) |
| CPU | 12-core A78AE | 14-core Neoverse-V3AE @ 2.6 GHz | NVIDIA blog (primary) |
| Memory | 64 GB | 128 GB LPDDR5X | NVIDIA blog (primary) |
| Gen-over-gen claim | baseline | **7.5× AI compute, only 3.5× energy efficiency** vs Orin | NVIDIA blog (primary) |

- The load-bearing observation is the **7.5× vs 3.5× gap** (primary): raw compute scaled roughly **2.1× faster than efficiency** across the Orin→Thor generation. Bigger VLA models want *more than proportionally* more power — unless software (quantization) closes the gap. Silicon alone does not give you a free perf-per-watt win.
- Practically, this is why the 40–130 W envelope is so wide: the same module is a 40 W part running a small policy or a 130 W part running a multi-billion-parameter [VLA](../vla-models.md) — and, as the thermal section shows, those two operating points need physically different cooling hardware.

### 量化换算功耗:软件才是每瓦性能的杠杆 (Quantization as the perf-per-watt lever)

The usable speedup at a **fixed power envelope** comes mostly from precision reduction, not new silicon:

| Technique | Speedup | Efficiency / latency | Task quality retained | Source |
|---|---|---|---|---|
| FP4 quant + Eagle speculative decoding (Qwen2.5-VL-7B, Thor vs Orin W4A16) | **up to 3.5×** faster inference | — | — | NVIDIA dev blog (primary claim, secondary aggregation) |
| Thor vs Orin, generative AI (LLM/VLM/VLA) overall | **up to 5×** faster | — | — | NVIDIA dev blog (primary claim, secondary aggregation) |
| INT8 vs BF16 (VLA / imitation-learning policy, Jetson-class GPU) | **~1.6×** | **~1.7×** energy efficiency | **~97%** of FP pick-and-place success | arXiv 2412.01034 / 2505.15304 (secondary) |
| INT4 vs BF16 (same) | **~2.5×** | **~2.5×** energy efficiency | (degrades further; use saliency-aware quant) | arXiv 2412.01034 / 2505.15304 (secondary) |
| GR00T N1 Compressed Action Tokens + parallel decoding | **up to 2.5×** faster policy inference | **<5 ms** per-step latency | — | NVIDIA Isaac GR00T materials (secondary) |

- **"TOPS/W beats peak TOPS" is measurable at the model level, not just the chip level** (secondary): INT8 keeps ~97% of full-precision task success while cutting energy ~1.7× — the concrete quantitative case that quantization is the real lever. INT4 doubles the win but needs saliency-aware quantization to protect task quality.
- **Real-time gap** (secondary): a humanoid joint controller wants **~1 kHz** hard-real-time cycles (the "split-brain" MCU/x86 loop in [hardware.md](../hardware.md)), while the VLA "brain" runs far slower. GR00T N1's compressed-action-token + parallel decoding pushes per-step VLA latency **below 5 ms**, closing that gap *on the same power budget* — an architectural trick, not more watts.
- **Distinct axis, other silicon** (primary/secondary): perf-per-watt is a real design axis independent of peak TOPS — EnCharge AI EN100 claims ~**40 TOPS/W** @ 200 TOPS INT8; Hailo-8 delivers **26 TOPS at 2.5–3 W** (~9–10 TOPS/W). These sit in the "small-brain" tier below Thor, where efficiency, not headline TOPS, is the buy criterion.

### 散热:真正的持续性能天花板 (Thermal — the true sustained ceiling)

Peak TOPS is a datasheet number; the sustained number is whatever the heat path allows before throttle or trip.

- **Hard trip, not soft throttle** (primary): per NVIDIA's Jetson Thor Thermal Design Guide (TDG12271001), the Thor SoC is rated to a junction temperature **not to exceed 118 °C**, enforced by **hardware thermal-trip that automatically performs a system reset** when exceeded. On a sealed humanoid this is a stronger failure mode than frequency throttling — an unmanaged thermal design risks an outright **reboot mid-task**, not just slowdown.
- **Cooling mass scales with TDP** (secondary; Advanced Thermal Solutions SOM heatsinks, corroborated across DigiKey + Power Systems Design):

| Solution | Rated TDP @ 50 °C ambient | Airflow | Size / mass | Source |
|---|---|---|---|---|
| Passive aluminum heatsink | up to **100 W** | needs **500 LFM** system airflow | 87×100.8×20 mm, **168 g** | ATS via DigiKey / PSD (secondary) |
| Active frameless-fan (fan-in-fin) | **95 W** | self-provided | 87×100.8×20 mm, **104 g** | ATS (secondary) |
| Active blower heatsink | **175 W** | self-provided | 92×100.8×28.6 mm, **174 g** | ATS (secondary) |

  A module labeled "40–130 W" needs meaningfully heavier/costlier cooling depending on where in that range it is driven — real **BOM and integration weight**, not free. Note the passive 100 W part assumes 500 LFM of forced airflow that a sealed enclosure may not have.
- **Sealed-enclosure reality** (unverified, informed-analyst framing): sealed / aesthetic-skin humanoids trap heat; one analysis estimates internal temp can exceed **70 °C within 30 min** of full load on a 35 °C day, with thermal-protection throttling cutting **max actuator torque by 40%+** — a payload/manipulation hit *separate from* compute throttling. Treat the exact figures as directional; the qualitative push toward **hybrid active-liquid + passive** designs is the takeaway.
- **Industry signal** (unverified, single-source, paywalled): DIGITIMES (2026-05-27) frames thermal management as a "**critical bottleneck**" for humanoid mass production — cramped joint architectures, limited dissipation space. Directional only; no extractable numbers.

### 功耗预算与"大脑占比"辨析 (Power budget & the "brain share" question)

A recurring claim (via the Witt / New Yorker piece already cited in [data.md](../data.md)) is that compute takes **~60%** of a robot's electricity vs **~20%** for a human brain of body energy. That framing is **load-state-dependent and mostly wrong for a working robot**:

| System state | Whole-system draw | Thor share (@130 W max) | Source |
|---|---|---|---|
| Idle / standing | 250–500 W | **~26–52%** | Longsing Tech (secondary) |
| Normal walking | 700–1,500 W | **~9–19%** | Longsing Tech (secondary) |
| Peak (lift / stairs / recovery, 5–10 s) | 2,000–4,000 W | **~3–6%** | Longsing Tech (secondary) |

- Reference pack: ~**1.99 kWh** (51.8 V, 38.4 Ah NMC) — consistent with the ~2 kWh class in [hardware.md](../hardware.md). Compute is only a large share of draw when the robot is **nearly stationary**; during locomotion, **locomotion dominates** (>70% by one aggregator estimate that puts compute/"agentic autonomy" at ~**20–25%** during active operation — unverified precise attribution, but consistent with the ~9–19% walking-state figure above). At the peak-load band a 130 W Thor is only **~3–6%** of draw, not <5% flat — at the 2,000 W low end the share is ~6.5%, so "<5%" holds only above ~2,600 W.
- **The human-brain benchmark** (secondary): brain ≈ **20 W continuous**, ~20% of the body's ~100 W basal metabolic rate. The Witt comparison invokes a robot brain drawing a *higher share* than that — but whether it actually exceeds 20% (let alone reaches 60%) depends entirely on activity state.
- **Verification note (unverified, single-source, could not re-confirm exact wording)**: the specific New Yorker "~60%" figure could **not** be independently re-verified this pass (paywalled; direct + Wayback fetches failed; no secondary source repeats the exact figure). Recommend the wiki state it as a single-source claim and use the load-dependent Longsing numbers + the 20–25% bracket as the honest contextualization, not "~60% of the battery goes to the chip."

### 成本分层:大多数机器人不该买最大的大脑 (Cost tiering — don't over-buy the brain)

The "small-brain tier" exists because AMRs/service robots need enough TOPS for nav/perception but cannot justify Thor-class watts, cooling, or price.

| Tier | Example | Compute | Power / price | Source |
|---|---|---|---|---|
| Big-brain (humanoid VLA) | Jetson AGX Thor T5000 | 2,070 TFLOPS FP4 | 40–130 W / **$3,499** dev kit | NVIDIA (primary) |
| Mid Thor | Jetson T4000 | 1,200 TFLOPS FP4 | 40–70 W / $1,999 @1k | NVIDIA (primary) |
| Small-brain (AMR/service) | Qualcomm RB5 (2020) → RB6 | **15 TOPS → 70–200 TOPS** | far lower W/$ | Qualcomm (primary + secondary) |
| Ultra-low-power accel | Hailo-8 | 26 TOPS | **2.5–3 W** | vendor (secondary) |

- Qualcomm's lineage (primary/secondary) shows the small-brain tier scaling **15 TOPS (RB5) → 70–200 TOPS (RB6)** — an order of magnitude below Thor's 2,070 FP4 TFLOPS, at correspondingly lower power and price. An inventory/cleaning/delivery robot whose *whole* power and cost budget is a fraction of a humanoid's has no reason to carry a 130 W, $3,499 brain.
- **Design rule of thumb**: (1) size the compute tier to the *smallest* model that hits your control-loop and task-success targets after quantization; (2) budget the thermal path for the *sustained*, not peak, operating point (respect the 118 °C hard trip); (3) recognize the brain is a **single-digit-to-~20% slice** of a working robot's power — locomotion and actuation, not compute, dominate the battery.

来源:
- https://developer.nvidia.com/blog/introducing-nvidia-jetson-thor-the-ultimate-platform-for-physical-ai/ (primary — Thor 40–130 W envelope, 2,070 TFLOPS FP4, 7.5×/3.5× gen claim, FP4+spec-decode 3.5×/5× speedups)
- https://developer.nvidia.com/downloads/assets/embedded/secure/jetson/thor/docs/jetson_thor_thermal_dg_tdg12271001.pdf (primary — 118 °C junction hard thermal-trip / system reset)
- https://arxiv.org/abs/2412.01034 (secondary — Quantization-Aware Imitation Learning: INT8 ~1.6×/~1.7×, ~97% success; INT4 ~2.5×)
- https://arxiv.org/abs/2505.15304 (secondary — Saliency-Aware Quantized Imitation Learning)
- https://github.com/NVIDIA/Isaac-GR00T (secondary — GR00T N1 Compressed Action Tokens, up to 2.5×, <5 ms per-step)
- https://www.longsingtech.com/humanoid-robot-power-system/ (secondary — whole-system draw 250–500 W idle / 700–1,500 W walk / 2,000–4,000 W peak; ~1.99 kWh pack)
- https://www.digitimes.com/news/a20260527PD226/robot-cooling-production-efficiency-management.html (unverified, single-source, paywalled — thermal "critical bottleneck" framing)
- https://www.qualcomm.com/developer/hardware/robotics-rb5-development-kit (primary — RB5 15 TOPS; RB6 70–200 TOPS via secondary 5G Americas/ActuIA coverage)
- https://www.newyorker.com/magazine/2026/07/06/are-humanoid-robots-ready-to-be-deployed (unverified re the "~60%" compute-share figure; already cited in data.md)
- ATS thermal solutions via DigiKey / Power Systems Design (secondary — passive 100 W, active-fan 95 W/104 g, blower 175 W/174 g); airobotseidos.com / rigidchill.com (unverified — sealed-enclosure 70 °C/30 min, 40%+ torque derate); neuroscience-popularization sources (secondary — human brain ~20 W ≈ ~20% of ~100 W BMR)
