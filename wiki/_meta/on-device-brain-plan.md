# Deep-research loop: 如何在端侧做好具身智能大脑 (On-Device Embodied-AI Brain)

Started 2026-07-05. A sustained multi-iteration research loop; each iteration
researches sub-topics (Sonnet collect → Opus write → Opus verify), writes a
section fragment, commits. Final iteration assembles → completeness critic →
bilingual page `wiki/on-device-brain.md` + interactive HTML.

Deliverable question: **端侧(on-device / edge)的具身智能"大脑"应该怎么做才算做好?**
Audience: technical + strategic (Quectel-style on-device compute-module maker).

## Section plan (12 sub-topics → 6 research iterations + 1 synthesis)

- [x] **A. 大脑架构基础 & 双系统** — perception→cognition→action; System 1 (fast reactive) / System 2 (slow deliberative VLA) dual-system; what "brain" means; Helix / GR00T N1 / π0 architectures.
- [x] **B. 云边分工 (split-brain / 云边混合)** — latency/reliability/privacy case for on-device; what MUST be local vs cloud; bandwidth & latency budgets; the offline-capability argument.
- [x] **C. 端侧 VLA 推理算力需求** — TOPS/memory-bandwidth to run a VLA at N Hz; real numbers per model; the compute ladder (10/48/77/700/2070); INT8/FP4.
- [x] **D. 面向端侧的模型优化** — quantization (INT4/INT8/FP4), distillation, small-VLA, action-head choices (diffusion/flow-matching/autoregressive tokens) and their latency; on-device LLM.
- [x] **E. 实时控制的切分** — AI-module (perception/policy 7-50 Hz) + MCU (motor control ~1 kHz); determinism, safety, why the split; the two-brain hardware pattern.
- [x] **F. SoC / 硬件版图** — Jetson Thor (2,070 TFLOPS) vs Qualcomm QCS8550/Snapdragon vs Horizon/D-Robotics vs others; big-brain vs small-brain tiers; NPU/GPU; memory.
- [x] **G. 功耗 / 散热 / 成本工程** — battery budget, edge-chip power draw (the ~60% claim), thermal on a moving robot, cost-of-compute; the mobile-power constraint.
- [x] **H. 软件栈 & 运行时** — ROS2, on-device inference engines (TensorRT / Qualcomm AI stack / llama.cpp-class), OS (Ubuntu on edge modules), the VLA runtime & middleware.
- [x] **I. 为端侧而生的模型** — Gemini Robotics On-Device, NVIDIA GR00T N1 (Jetson-native), Figure Helix S1/S2, π0/π0.5 on-device, small open VLAs; who ships an edge brain.
- [x] **J. 端侧学习/自适应 & 数据飞轮** — on-device adaptation vs cloud training; the deployed-robot data flywheel; test-time compute.
- [x] **K. "做好"的判据 & 评价** — latency / generalization / reliability (9s) / power / cost / updatability; how to benchmark an on-device brain.
- [x] **L. 参考架构 & 模组厂视角** — the emerging best-practice on-device-brain architecture (recipe); what an on-device-brain MODULE should look like (Quectel Robrain-class); strategic read for a module maker.

## Iteration mapping
- iter1: A+B · iter2: C+D · iter3: E+F · iter4: G+H · iter5: I+J · iter6: K+L
- iter7 (synthesis): assemble fragments → adversarial completeness critic → summary/read → bilingual page + HTML + push.

## Loop mechanics
- Driven by workflow-completion notifications (each iteration's workflow completes → integrate its section → launch next). A ScheduleWakeup heartbeat as fallback.
- Model tiering: Sonnet for collection, Opus for write/verify/synthesis.
- Fragments in scratchpad/brain-sections/; final page wiki/on-device-brain.md (+ zh) + docs/on-device-brain.html.
- Every iteration = one commit `loop(brain-N): <section>`.
