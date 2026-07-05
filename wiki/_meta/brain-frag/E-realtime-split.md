## 实时控制的切分 (The Real-Time Control Split)

The central architectural fact of an on-device embodied brain: **a single clock cannot serve the whole stack.** Semantic reasoning wants seconds; whole-body coordination wants milliseconds; the motor current loop wants microseconds. No one compute substrate is good at all three, so every serious humanoid stack splits control into a **frequency hierarchy**, mapping each tier onto the silicon whose determinism guarantee matches that tier's period. The engineering discipline is deciding *where each cut falls* and *what hardware each side runs on*.

### The frequency ladder (端侧控制频率阶梯)

The tiers are ordered by loop period. As frequency rises, the substrate shifts from Linux+GPU (non-deterministic, best-effort) toward dedicated MCUs / real-time cores (hard-deterministic).

| Tier | 典型频率 | What it computes | Substrate | Determinism |
|---|---|---|---|---|
| S2 语义推理 | slow / planning timescale | scene understanding, language, behavior sequencing | Linux + GPU (VLM) | none (best-effort) |
| S1 全身策略 | 30–200 Hz | perception → full-body joint targets | Linux + GPU (transformer policy) | soft / firm RT |
| S0 反射层 | ~1 kHz | balance, contact, coordination; joint actuator commands | RT core / MCU | hard RT |
| 电流/力矩环 (FOC) | 1–20 kHz | field-oriented current control, PWM | joint MCU firmware | hard RT (native) |

### Reference architectures — where vendors put the cuts

| System | Slow / semantic | Fast policy (S1) | Reflex / low-level (S0) | Source |
|---|---|---|---|---|
| Figure Helix 02 | S2, planning timescale | 200 Hz, transformer, all sensors→all actuators (**80M-param figure unverified — page states "transformer-based" only**) | **1 kHz, 10M-param NN**; trained on **1,000+ hr** retargeted human motion across **200,000+ parallel sim envs** | figure.ai/news/helix-02 (primary) |
| Figure Helix v1 | System 2 VLM, low freq | **200 Hz single motor policy, 35-DoF** action space (fingers, end-effectors, head gaze, torso) | *(no separate reflex tier — added in v02)* | figure.ai/news/helix (primary) |
| Boston Dynamics electric Atlas | large-behavior-model policy | **30 Hz** (images+proprio+language→actions) | underlying **MPC-based whole-body controller** (freq not disclosed) | bostondynamics.com (primary) |
| Academic WBC (survey) | centroidal MPC / learned policy **10–50 Hz** | task-space / whole-body controller **50–120 Hz** | *(dedicated joint firmware, below survey scope)* | hierarchical-WBC survey (secondary) |

**Key observation:** Helix v1 → v02 is the industry admitting one cut wasn't enough — the 200 Hz policy was too slow/non-deterministic for balance and contact, so a **1 kHz reflex layer (S0)** was carved out below it (primary). Atlas's learned "brain" runs even slower at **30 Hz** and *commands* a classical MPC controller underneath — same slow-policy → fast-classical-controller pattern, just with the policy layer noticeably slower than Helix's 200 Hz S1 (primary). Note that **none of the surveyed academic architectures reach the 500 Hz–1 kHz MCU tier directly** — that tier lives in dedicated joint firmware below the whole-body controller (secondary).

### Why Linux+GPU cannot own the fast loop (为什么大脑算力≠实时算力)

The quantitative case that the AI substrate is structurally disqualified from the ≥1 kHz tier:

- **Stock Linux tail latency is fatal to a 1 kHz loop.** ROS2 on a vanilla (non-RT-patched) kernel measured a **max scheduling latency of 6,243 µs (6.2 ms)** *(exact figure single-sourced to the paywalled paper's results table; the multi-ms native-Linux tail is corroborated by independent measurements of 1.5–13.4 ms worst-case)* — ~3 µs average, but the tail is what kills you. A 1 kHz loop has a **1 ms budget**; a 6.2 ms stall is a missed deadline (primary, *Chinese J. Mechanical Engineering*).
- **PREEMPT_RT is a mitigation, not a guarantee.** The same setup with the PREEMPT_RT patch bounded worst-case latency to **94 µs** under both no-load and full-load — adequate for kHz-class *soft/firm* RT, but it is a software patch generally used only **up to ~1 kHz**, not the 10–20 kHz current loop, and not a hardware guarantee (primary).
- **ros2_control shows the discipline required.** The `controller_manager` runs a fixed-rate loop (commonly **200 Hz–1000 Hz**), requests **SCHED_FIFO priority 50**, supports per-component async rates (e.g. IMU read at 1000 Hz while others run 500 Hz), and its docs *explicitly warn* that non-RT-safe calls (e.g. `get_lifecycle_state()`) must stay out of the RT path and recommend an RT/low-latency kernel (primary, control.ros.org).
- **GPU can accelerate the S1 tier but not make it hard-RT.** ReLU-QP (a QP solver reformulated as a weight-tied ReLU net on GPU) raised whole-body-MPC frequency for one-foot Atlas balancing from **~65 Hz (CPU QP) → 1,300+ Hz** — proof the whole-body tier is compute-bound and GPU can push it past 1 kHz, but this is **best-effort GPU compute, not a deterministic guarantee**, which is exactly why the innermost torque loop still needs a separate MCU (primary, arXiv:2311.18056, ICRA 2024).

**The architectural root cause:** the AI SoC's main **Cortex-A / GPU** complex has an **MMU** — TLB misses, page walks, cache and scheduler variability all inject jitter. Real-time/safety cores use **Cortex-R with an MPU** instead: deterministic address translation, no TLB misses, no page walks, typically in **dual-core lockstep** to catch single-event upsets by output comparison (secondary, Arm Newsroom). This is why silicon vendors *bolt on* a separate deterministic domain rather than time-share the Linux complex.

### The hardware boundary — what a compute module must expose

The cut isn't just software; it's silicon. Even inside the "rich SoC," there is a physically isolated real-time domain:

- **NVIDIA Jetson (Orin-class) Functional Safety Island (FSI):** **4× dual-core-lockstep Cortex-R52 (Armv8-R)**, independently power/voltage-isolated, rated **ASIL-D (systematic) / ASIL-D (random)** — the FSI is the *only* domain on the Orin SoC that reaches ASIL-D random (the rest of the SoC is lower), **~10K ASIL-D MIPS**, **512 KB TCM per R52 core** (ATCM 256 KB + BTCM 128 KB + CTCM 128 KB), **3 MB shared SRAM**. A Hardware Safety Manager (HSM) monitors faults and asserts a **`SOC_ERROR` GPIO** to an external MCU (primary, NVIDIA DRIVE OS 6.0.9/7.0.3 FSI docs). This is the clearest evidence for what a module must expose: a deterministic RT/safety domain **physically separate from the AI compute domain.**
- **EtherCAT as the deterministic fieldbus:** cycle times as low as **62.5–100 µs** for dozens of servo axes, **jitter <1 µs**; one study measured a **50 µs min cycle** on gigabit with 50 devices @100 B each; a real humanoid implementation reaches **250 µs** cycles (secondary — acontis/elmomc/ASIX). This µs-determinism lets a single master synchronously command dozens of drives within one ~1 kHz period.
- **acontis EC-Master on Jetson Orin/Thor:** the direct commercial instantiation of "rich SoC runs ROS2 over EtherCAT to distributed joint MCUs" — preserves **>99% of CPU availability** for AI inference/perception/navigation while handling the fieldbus in background, with **microsecond-level determinism** (primary — acontis.com, *note: page gives the >99% and µs-determinism claims but no explicit Jetson cycle-time number*).
- **Joint-level MCU tier (the "spinal cord"):** TI **C2000 TMS320F28P650DK** integrates a hardware **EtherCAT** controller **+ CAN-FD** on one **9×9 mm BGA**, **IEC 61508 SIL 2** certified, with FOC-capable PWM/ADC — one chip bridging deterministic bus + motor control + safety (primary, TI product page + AppBrief slla659a).
- **The bus below EtherCAT:** where full determinism isn't needed, **CAN-FD** raises data-phase rate from CAN 2.0's **1 Mbps → 5–8 Mbps** (some cite up to 10 Mbps), payload **8 → 64 B**; documented gain = joint-position feedback throughput **1 → 5 Mbps** (secondary — Dorleco/Grid Connect).
- **FOC current loop, the innermost tier:** runs **10–20 kHz**; common pattern is a **10 kHz current/torque loop nested in a 1 kHz speed loop** (NXP MCUXpresso SDK reference), PWM switching **10–20 kHz** (primary, NXP FOC user guides). This is *below* everything above and lives entirely in joint firmware.

### The humanoid twist — the safety layer must be control-capable (安全层不能只是急停)

A critical asymmetry vs. fixed-base industrial arms: **a humanoid E-stop cannot simply cut power.** IEC 61508 (applied alongside ISO 10218 / ISO/TS 15066) requires SIL targets, fault-containment regions and safe states; a joint torque-limit violation nominally triggers a **Cat 0 stop (IEC 60204-1)**. But an underactuated biped with unilateral ground contact will **fall/collide if power is abruptly removed** — so the deterministic safety layer must run a **predefined fallback controller** (preserve balance, regulate contacts, reach a safe terminal pose), i.e. it has to be **control-capable, not a kill switch** (secondary — kitecompliance.ai; arXiv 2603.22703 "Learning Safe-Stoppability Monitors"). This raises the bar on the deterministic tier: it is not merely a monitor but a real controller running on the isolated RT/safety core.

### Takeaway

Design the brain as **cuts, not a monolith.** Put S2/S1 (semantic + whole-body policy, 30–200 Hz) on Linux+GPU; accept it is best-effort. Put S0 (~1 kHz reflex/balance) and the safety fallback on an isolated deterministic core (Cortex-R FSI or dedicated MCU). Put the 1–20 kHz FOC loop in joint MCU firmware, reachable over EtherCAT (µs-determinism) or CAN-FD (5–8 Mbps). The compute module's non-negotiable exposed feature is **a real-time/safety domain electrically isolated from the AI domain** — Jetson Orin ships exactly this as the Cortex-R52 FSI.

来源:
- https://www.figure.ai/news/helix-02
- https://www.figure.ai/news/helix
- https://bostondynamics.com/blog/large-behavior-models-atlas-find-new-footing
- https://www.acontis.com/en/humanoid-robotics.html
- https://www.ti.com/ (C2000 TMS320F28P650DK real-time motor-control MCU product page; App Brief slla659a "Motor Control in Humanoid Robots")
- NXP MCUXpresso SDK FOC user guides (PMSMMC56F80000EVK, PMSMMKV31UG)
- https://doi.org/10.1186/s10033-023-00976-5 (Chinese J. Mechanical Engineering, "ROS2 Real-time Performance Optimization and Evaluation")
- https://control.ros.org (Controller Manager; "Different update rates for Hardware Components")
- https://arxiv.org/abs/2311.18056 (ReLU-QP, ICRA 2024)
- NVIDIA DRIVE OS 6.0.9 / 7.0.3 "Functional Safety Island (FSI)" developer docs
- Arm Newsroom, "Cortex-R and the Next-generation of Vehicles"
- Dorleco / Grid Connect (CAN 2.0 vs CAN-FD comparisons)
- kitecompliance.ai "A Primer on Humanoid Robot Compliance"; arXiv 2603.22703 "Learning Safe-Stoppability Monitors for Humanoid Robots"
