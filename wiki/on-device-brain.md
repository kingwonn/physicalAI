---
title: "如何在端侧做好具身智能大脑 (Building a Good On-Device Embodied-AI Brain)"
slug: on-device-brain
updated: 2026-07-05
confidence: verified
---
> 深度技术+战略调查:一个跑在机器人**机身上(on-device / edge)** 的具身智能"大脑"要怎么设计才算做好?本页由一个 6 轮研究循环(每个子课题经 Sonnet 采集 → Opus 写作 → Opus 对抗核查,数字全部对准 arXiv / 官方规格一手源)建成,覆盖架构、云边分工、算力需求、模型优化、实时控制切分、SoC 版图、功耗散热、软件栈、端侧模型、端侧学习、评价判据、参考架构。**四条收官结论**:(1) 架构已收敛为**双/三系统**——慢的深思 System 2(VLM,5–10 Hz)+ 快的反应 System 1(视觉运动策略,100–200 Hz)+ 硬实时 System 0(电机/反射环,500 Hz–1 kHz 在 MCU 上),跨"富 SoC + 确定性 MCU"切分。(2) 实时控制与安全环**必须在端侧**(Linux+GPU 栈给不出 µs–ms 确定性;断网机器人不能停),重推理可"云边混合"。(3) **算力已基本不是瓶颈**——Jetson Thor 2,070 FP4 TFLOPS、量化(INT4/FP4)、动作分块(action chunking)、小型 VLA 已把端侧推理压到可用频率;真正卡住的是**可靠性(9 个 9)与泛化**,不是 FLOPS。(4) 对模组厂(移远式)的读数:**端侧大脑(算力+连接模组)是可防御的军火商赛道**——机电 BOM([零部件供应链](component-supply-chain.md))十年护城河进不去,而真正的威胁是高通/NVIDIA 芯片原厂**越过模组商直供整机**([友商全景](odm-competitors.md))。

配套阅读:[VLA 模型](vla-models.md)、[硬件底座](hardware.md)、[NVIDIA 机器人栈](company-nvidia.md)、[零部件供应链](component-supply-chain.md)、[评测与基准](evaluation.md)、[开放问题](open-problems.md)、[移远 pitch](../pitch/quectel.md)、[ODM 机会图谱](odm-opportunity.md)。

方法与证据说明:本页每个 section 由独立研究+对抗核查产出;所有关键数字(Hz、TOPS、ms、参数量)在核查阶段逐条对准一手源(arXiv 论文、NVIDIA/高通/Figure/DeepMind 官方规格与博客);单源/未证实项在正文显式标注 `(unverified)`/`(secondary)`。一手源标 `(primary)`。构建循环日志见 [on-device-brain-plan](_meta/on-device-brain-plan.md) 与 [loop-log](_meta/loop-log.md) 的 `loop(brain-N)` 条目。

---

## 阅读导航 (Reading guide)

| # | Section | 一句话 |
|---|---|---|
| A | 架构基础与双系统 | S2 慢而通用 + S1 快而专;为何单一模型不能又聪明又快 |
| B | 云边分工 | 什么必须本地(实时/安全)、什么可上云;云边混合 |
| C | 端侧算力需求 | 跑一个 VLA 到可用频率要多少 TOPS + 内存带宽;VLA-Perf 实测阶梯 |
| D | 面向端侧的模型优化 | 量化/蒸馏/动作头选择;扩散比自回归快 ~100x;动作分块藏延迟 |
| E | 实时控制的切分 | AI 脑 + MCU 脊髓;确定性/安全为何必须分层 |
| F | SoC / 硬件版图 | Jetson Thor / 高通 / D-Robotics / Tesla AI5 分档 |
| G | 功耗/散热/成本 | ~2kWh 移动电源约束;TOPS/W 才是真指标 |
| H | 软件栈与运行时 | Ubuntu+PREEMPT_RT+ROS2+TensorRT/QNN;尚无标准"机器人脑 OS" |
| I | 为端侧而生的模型 | Gemini On-Device / GR00T N1.6 / Helix / SmolVLA / LiteVLA / BitVLA |
| J | 端侧学习与数据飞轮 | 云训练+端适配;车队数据飞轮;OTA;测试时算力 |
| K | "做好"的判据与评价 | 延迟/泛化/可靠性/功耗/成本/可更新的评分标尺 |
| L | 参考架构与模组厂视角 | 三层收官架构 + 模组规格清单 + 移远战略读数 |

---


## 大脑架构基础与双系统 (Architecture & Dual-System)

The on-device embodied "brain" is not one model. Across the four production-grade systems that define the 2025-26 state of the art — Figure Helix, NVIDIA GR00T N1/N1.5, Physical Intelligence π0/π0.5, and Google DeepMind Gemini Robotics — the field has converged on a **dual-system split**: a slow, internet-pretrained **System 2 (S2)** that does semantic scene/language understanding and planning, feeding a fast, lightweight **System 1 (S1)** that turns that intent into continuous motor commands. This is the concrete architecture any on-device brain must instantiate.

### Why split at all (the speed-vs-generality tradeoff)

- Figure's framing is the field's rationale (primary): *"VLM backbones are general, but not fast, and robot visuomotor policies are fast but not general. Helix resolves this tradeoff through two complementary systems, trained end-to-end to communicate."* [figure.ai/news/helix]
- A single monolithic VLM is semantically general but too slow for closed-loop control (large internet-pretrained transformers run at single-digit-to-~10 Hz); a small visuomotor policy is fast (100-200+ Hz) but does not generalize beyond its demo data. The split lets each layer run at its own clock and own scale. (primary)
- The pattern maps onto a neuroanatomical analogy widely used in the field: **S2 ≈ cerebral cortex** (symbolic/semantic deliberation), **S1 ≈ cerebellum** (fast motor control + environmental feedback); some literature adds a spinal-cord / reflex tier. (unverified — analogy, cross-cited but not from a single canonical primary source)

### The four reference architectures

| System | S2 (slow / "brain") | S2 rate | S1 (fast / "cerebellum") | S1 rate | Coupling | Deploy |
|---|---|---|---|---|---|---|
| **Figure Helix** | 7B open-weight VLM | 7-9 Hz | 80M cross-attn enc-dec transformer | 200 Hz | single continuous latent vector; async | dual low-power embedded GPUs, fully onboard |
| **NVIDIA GR00T N1** | Eagle-2 VLM (1.34B) | 10 Hz | Diffusion Transformer (flow-matching) | 120 Hz | cross-attention on VLM tokens; jointly trained | Jetson-class; 2.2B total |
| **NVIDIA GR00T N1.5** | Eagle 2.5 VLM (2.1B), **frozen** | (~10 Hz) | flow-matching DiT + FLARE aux | (~120 Hz) | LN'd MLP connector; joint flow-matching + world-model loss | ~3B total |
| **PI π0 / π0.5** | PaliGemma VLM (3B) | (chunk-triggered) | 300M flow-matching "action expert" | ~50 Hz | two streams, one jointly-trained model | 3.3B total; π0-small 470M variant |
| **Gemini Robotics** | Gemini Robotics-ER ("cognitive brain") | cloud/edge | Gemini Robotics VLA + local action decoder | 50 Hz local | ER emits per-step NL instruction; rolling-horizon chunks | cloud backbone + on-device decoder (or fully local) |

All figures (primary) except GR00T N1.5 S2/S1 rates in parentheses (inferred to match N1; the N1.5 page does not restate them — treat as (unverified) at the exact-Hz level).

### Figure Helix — the purest asynchronous dual-clock design

- **S2**: a 7B-parameter open-weight VLM, pretrained on internet-scale data, fine-tuned on 500+ hours of robot teleoperation; runs at **7-9 Hz**. (primary, verified vs figure.ai/news/helix)
- **S1**: an **80M-parameter** cross-attention encoder-decoder transformer (~90x smaller than S2), runs at **200 Hz** — a ~25-30x rate gap between the two systems. (primary, verified)
- **Communication is a single continuous latent vector**, not language tokens: S2 *"distills all semantic task-relevant information into a single continuous latent vector"* consumed by S1. During training, gradients backpropagate from S1 into S2 through this vector (full end-to-end differentiability); at deploy, S1 reads *"the most recent S2 latent vector"* from shared memory — this decoupling is exactly what lets the two systems run **asynchronously at their own clock rates**. (primary, verified)
- **Action space**: full upper-body **35-DoF** at 200 Hz — wrist poses, per-finger flexion + abduction, torso and head orientation targets — enabling dexterous bimanual manipulation. (primary, verified)
- **Deployment**: both S1 and S2 run **entirely onboard on dual low-power embedded GPUs**, splitting inference across two chips — a literal "brain-vs-cerebellum on separate silicon" instance and the single most relevant on-device precedent here. (primary, verified) See also [Figure](company-figure.md).

### NVIDIA GR00T N1 → N1.5 — jointly-trained VLM + Diffusion Transformer

- **N1** pairs an Eagle-2 VLM System-2 (1.34B params; Eagle-2 = SmolLM2 LLM + SigLIP-2 image encoder) with a **Diffusion-Transformer (flow-matching) System-1** that cross-attends to the VLM tokens. Both are **trained jointly end-to-end**, not as separate stages. Released checkpoint GR00T-N1-2B = **2.2B** total. (primary)
- **N1 throughput**: S1 samples a **16-action chunk in 63.9 ms** on an L40 GPU (bf16), with **K=4 flow-matching integration steps**; S2 updates conditioning at **10 Hz**, S1 sustains **120 Hz** closed-loop control. Chunking amortizes the slow VLM over many fast actions. (primary, verified vs arXiv 2503.14734 — "inference time for sampling a chunk of 16 actions is 63.9ms on an L40 GPU using bf16"; VLM "1.34B", total "2.2B", SmolLM2 LLM + SigLIP-2 encoder, S2 10Hz / S1 120Hz all confirmed verbatim)
- **N1.5** upgrades S2 to **Eagle 2.5 (2.1B)**, **freezes the VLM during pretraining and finetuning**, adds a layer-norm to the MLP connector, and co-trains flow-matching + **FLARE** (Future LAtent Representation Alignment — aligns to target future embeddings rather than generating future frames), letting it learn from human video too. Trained **250K steps on 1K H100 GPUs, global batch 16,384**. (primary, verified vs research.nvidia.com/labs/gear/gr00t-n1_5)
- **Payoff of a stronger, decoupled S2**: on a real Fourier GR-1 humanoid (pick a language-specified fruit → plate), **language-following 93.3% (N1.5) vs 46.6% (N1)**; overall success **83.0% vs 43.3%** — evidence that strengthening/freezing S2 sharply improves instruction-following without touching the control-rate S1. (primary, verified — all four figures 93.3/46.6 and 83.0/43.3 confirmed verbatim on research.nvidia.com/labs/gear/gr00t-n1_5) See also [NVIDIA](company-nvidia.md).

### Physical Intelligence π0 / π0.5 — two streams, flow-matching action expert

- **π0**: PaliGemma **3B** VLM backbone + a separate **300M flow-matching "action expert"** (init from scratch, handles proprioceptive state + action generation); **3.3B** total. Conceptually the same S2/S1 split as Helix, but implemented as **two streams inside one jointly-trained model** rather than two asynchronously-clocked systems. (primary, verified vs arXiv 2410.24164 — "300M parameters for the action expert…for a total of 3.3 billion parameters")
- **Chunking**: predicts a full **H=50 action chunk (1 s @ 50 Hz)** per forward pass via conditional flow matching, **10 integration steps** (δ=0.1); the chunk executes open-loop before regeneration. (primary, verified — "we use H=50", "10 integration steps (corresponding to δ=0.1)")
- **Rate**: ~**50 Hz** motor output; onboard inference latency **~73 ms (RTX 4090, bf16, 3 cameras)** — a new pass fires every ~0.5-0.8 s. This is how a not-real-time VLM+diffusion stack still sustains 50 Hz: chunking amortizes slow inference over many fast open-loop actions. (~73 ms figure secondary — not in 2410.24164 main text, corroborated by external benchmarks; the ~86 ms off-board/network figure could not be sourced and is dropped as (unverified))
- **π0-small (470M, no VLM pretraining)** makes the tradeoff explicit: dropping internet-scale pretraining shrinks the model ~7x but sacrifices generalization — why the field keeps a large pretrained VLM specifically for the S2 role. (primary, verified — "π0-small, has 470M parameters, does not use VLM initialization")
- **π0.5** makes the hierarchy explicit: the model first **verbalizes the next subtask in natural language** ("what to do next"), then the 300M action expert decodes it into a 50-step chunk — chain-of-thought-to-action (shared with PI's "Hi Robot"). Heterogeneous co-training (multi-robot + web/semantic + subtask annotations) yields open-world generalization: **10-15 min multi-stage mobile-manipulation** in entirely new kitchens/bedrooms unseen in training. (primary) See also [Physical Intelligence](company-pi.md).

### Google DeepMind Gemini Robotics — explicit cloud/edge two-model split

- **Two models**: **Gemini Robotics-ER** (the "cognitive brain" / embodied-reasoning model) does spatial understanding, task planning, and success detection; **Gemini Robotics (VLA)** turns each ER-emitted per-step NL instruction into low-level motor commands, with its own internal chain-of-thought and long-task decomposition. (primary)
- **Latency hiding**: a large VLA backbone runs in the **cloud**, sending compressed guidance to a **lightweight local action decoder** that predicts multiple short motion chunks at once to mask a backbone **query-to-response latency optimized to under 160 ms** behind a **50 Hz effective control frequency**, for ~**250 ms end-to-end** (raw observations → low-level action chunks) closed-loop latency. (primary, verified vs arXiv 2503.20020 — "optimized from seconds to under 160ms", "end-to-end latency…is approximately 250ms", "effective control frequency is 50Hz") A separately-released **fully on-device variant** (Gemini Robotics On-Device) runs the whole loop locally, but **no per-step ms figure is published** — DeepMind's on-device materials give no hard latency number, so the earlier "under 10 ms/step" claim is **(unverified)** and likely wrong (on-device control loops are documented only at ≥15-30 Hz, i.e. ~33-67 ms/cycle).
- **Cross-embodiment "Motion Transfer"**: skills trained only on ALOHA 2 transfer **zero-shot** to Apptronik Apollo and a bi-arm Franka — because the shared backbone learns embodiment-agnostic representations and only the lightweight local decoder needs per-robot adaptation. Splitting brain (backbone) from cerebellum (decoder) aids **cross-embodiment transfer, not just speed**. (primary)

### Takeaways for an on-device brain

- **Two clocks, two sizes**: budget for a big slow S2 (single-digit-to-~10 Hz, 1-7B params) and a small fast S1 (~50-200 Hz, 80-300M params). The rate gap is the whole point. (primary, cross-model)
- **Latent (not tokens) is the tightest coupling**: Helix's single continuous latent vector + shared memory is what makes true async on-device dual-GPU deployment work. (primary)
- **Chunking is the latency trick**: π0/GR00T show a slow non-real-time stack still hits 50-120 Hz by amortizing one inference over a 16-50-step chunk. Any on-device brain lives or dies on chunk-horizon vs regeneration-latency budgeting. (primary)
- **Freezing/strengthening S2 pays off** (GR00T N1.5's 46.6%→93.3% language-following, 43.3%→83.0% overall) — decoupling lets you upgrade the reasoning half independently of the control half. (primary)

来源:
- https://www.figure.ai/news/helix
- https://arxiv.org/abs/2503.14734
- https://research.nvidia.com/labs/gear/gr00t-n1_5/
- https://arxiv.org/abs/2410.24164
- https://www.pi.website/blog/pi0
- https://arxiv.org/abs/2504.16054
- https://www.pi.website/blog/pi05
- https://deepmind.google/blog/gemini-robotics-15-brings-ai-agents-into-the-physical-world/
- https://arxiv.org/abs/2503.20020

---

## 云边分工 (Cloud vs Edge / Split-Brain)

The central design decision for an on-device embodied brain is **what stays local and what may leave the robot**. The industry has converged on a *layered latency budget* and a *reflex/cognition split* (System 1 / System 2, or "小脑/大脑", cerebellum/brain). The real-time control loop must be local because network round-trips exceed its cycle budget by orders of magnitude; high-level reasoning is cloud-offloadable because it is intermittent and latency-tolerant.

### 1. The latency-budget hierarchy (why the control loop can never leave)

Control layers run at radically different frequencies, and the fastest ones categorically cannot absorb any network round-trip:

| Layer | Frequency | Cycle budget | Must be local? |
|---|---|---|---|
| Low-level joint/torque control | ~1000 Hz (GR1 whole-body torque) | ~1 ms | Yes — sub-ms |
| Whole-body QP / balance control | ~100–200 Hz (QP@100 Hz; REEM-C PC@200 Hz) | 5–10 ms | Yes |
| Inverse kinematics / motion planning | ~30–50 Hz (IK caps ~30 Hz) | 20–33 ms | Yes (reactive) |
| Perception / VLM scene understanding | ~7–9 Hz (Helix S2) | 100+ ms | Edge-preferred |
| Deliberative planning / multi-step reasoning | seconds | 100s ms–s | Cloud-offloadable |

- Anchor comparison: even a *well-optimized teleoperation* channel, **ExtremControl (2026)**, hits only ~**50 ms** end-to-end for direct extremity control over a network link (secondary) — that is already an order of magnitude worse than a local joint-control loop (sub-ms to a few ms), which is precisely why teleop is a *supervisory/fallback* mode, never the primary control loop.
- A general edge-cloud robotics survey frames edge devices for **sub-10 ms** response, with multi-robot edge-resident pipelines demonstrating **<1 ms** (0.001 s) average command-response for the edge portion **(unverified — specific sub-ms figure not reconfirmed in cited surveys)**; cloud is reserved for complex generation/reasoning offload (secondary).

### 2. The cost of pushing large VLAs fully on-device (VLA-Perf, π0 family)

Hard inference numbers show a **100x+** gap between datacenter and edge silicon — the load-bearing evidence that fully-local large VLAs are frequency-limited (primary, VLA-Perf arXiv 2602.18397v1):

| Model | Jetson Thor (edge) | RTX 4090 (consumer) | Datacenter |
|---|---|---|---|
| π0 baseline | 52.57 ms/step (19.0 Hz)* | 31.06 ms (32.2 Hz) | H100 6.15 ms (162.5 Hz); B100 3.18 ms (314.4 Hz); A100 16.20 ms (61.7 Hz) |
| π0-L (9.1B) | 3.9 Hz | 8.0 Hz | — |
| π0-XL (16.7B) | 2.1 Hz | — | — |
| π0-XXL (81.3B) | — | — | B100 9.6 Hz |
| long-context (1K timesteps) | 768.3 ms (1.3 Hz) | — | — |

\*π0 baseline breakdown on Thor: vision enc 6.06 ms + VLM backbone 20.30 ms + action expert 26.20 ms.

- Architecture matters as much as location: **diffusion-based action decoding is 102.4x faster** than vanilla autoregressive with chunking; raising denoising steps 10→50 increases end-to-end latency **2.15x** (primary).
- **Asynchronous inference over 5G + datacenter GPU (B100) yields 5.99x throughput** vs. synchronous cloud inference (primary) — quantifying the payoff of decoupling the async, cloud-offloadable perception/planning path from the synchronous, local action loop.

### 3. Location alone is not the win — model size is (edge-vs-cloud counter-point)

A controlled VLM benchmark on a **Unitree G1-EDU** humanoid (edge node = NVIDIA L4 24 GB, a realistic ORAN/MEC node) shows moving compute to the edge is *not* automatically a big win (primary, arXiv 2601.14921):

| Model | Edge (end-to-end) | Cloud baseline | Δ |
|---|---|---|---|
| LLaMA-3.2-11B-Vision (4-bit NF4) | 1600.03 ms | 1685.20 ms | only ~5% |
| Qwen2-VL-2B | "sub-second" | — | <½ of cloud baseline |

- Text generation dominates **>85%** of latency regardless of location — so a big model gains almost nothing from edge placement; the win comes from a **smaller, quantized** on-device model. Takeaway: pair the split-brain design with a *right-sized* local model, don't just relocate a large one.

### 4. Industry architectures on the cloud-vs-edge spectrum

| System | Split pattern | On-device compute | Cloud role | SQ |
|---|---|---|---|---|
| **Figure Helix** | S2 (7B VLM @7–9 Hz → latent vector) + S1 (80M cross-attn transformer @200 Hz, 35-DoF upper-body) | dual low-power embedded GPUs, model parallelism | **none** — fully onboard, removes "latency and uptime risk of cloud-dependent systems" | primary |
| **Gemini Robotics On-Device** | VLA foundation model run **entirely locally**; adapts w/ 50–100 demos | robot-local | flagship cloud Gemini Robotics kept for SOTA "without on-device limitations" — explicit capability/latency tradeoff | primary |
| **Quectel Robrain (移远 v2.0)** | 端云协同 (edge-cloud collaboration); detects network in real time, dynamically allocates compute; 以端侧为主、云端为辅 | edge-primary; sensitive data local | 云端迭代优化; plugs into Doubao (豆包)/DeepSeek + search when connected | primary (85%-offline figure: secondary) |
| **RoboOS** | "Brain" (cloud reasoning/planning) + "Cerebellum" (on-device reactive control); cross-embodiment, multi-agent | per-robot cerebellum | multi-step reasoning + cross-robot coordination | primary |
| **Tesla Optimus** | vision-only, cloud-independent inference; custom onboard chip (AI5-class for Gen 3, FSD lineage) | custom SoC | none for control loop | **unverified** (enthusiast press; chip name/specs unverified) |
| **1X Neo** | edge autonomy + **remote-human teleop fallback** ("Redwood"), ~60–70% autonomy at launch | onboard | *human operator*, not a bigger cloud model, is the fallback | **unverified** (secondary; outage-safety behavior undocumented) |

- **Robrain** claims **"断网环境下仍维持85%核心功能"** (maintains 85% core functionality when disconnected) (secondary); deployed on LimX Dynamics' TRON 1 bipedal robot. This is the concrete graceful-degradation target for an edge-primary design.
- **Helix data efficiency**: ~**500 hours** of training data — **<5% of the size of previously collected VLA datasets** (a **>95% reduction**), per Figure's own post (primary) — with no multi-embodiment collection or multi-stage training; evidence that the S1/S2 split (small reactive net conditioned by a pretrained VLM) is more data-efficient than a monolithic on-device giant, favoring hybrid over monolithic.
- **Gemini Robotics On-Device** outperforms the prior best on-device VLA on out-of-distribution tasks and multi-step instructions, running dexterous bimanual tasks (unzipping bags, folding clothes) fully local (primary) — the on-device capability gap is closing.

### 5. On-device compute anchor (2025–2026)

- **NVIDIA Jetson Thor (Blackwell)** — the reference platform many humanoid makers (Boston Dynamics Atlas, Agility Digit gen-6) are adopting: up to **2,070 FP4 TFLOPS**, **128 GB** memory, **40–130 W**, ~273 GB/s bandwidth; 2,560 CUDA cores, 96 5th-gen Tensor Cores, 14-core Arm Neoverse-V3AE (primary). That is **7.5x the AI perf and 3.5x the power efficiency** of AGX Orin — orders of magnitude below B100/H100, but enough to run a 7–9B VLM backbone at single-digit-to-tens of Hz **plus** a small action-expert net at 100–200 Hz. This is exactly the compute envelope Helix-style S1/S2 splits are engineered for.

### 6. The general CS trend

- Splitwise-style edge-cloud LLM collaborative-inference research frames the split at the **token/layer level** using Lyapunov-optimization-based RL to meet latency SLAs dynamically per network conditions (primary/secondary) — the non-robotics analog of Robrain's real-time network-aware compute allocation. Expect robot brains to adopt the same dynamic, SLA-driven splitting rather than a static edge/cloud boundary.

### Design takeaways

- **Never** route the ≥100 Hz reactive/balance loop through the network — reserve the edge for it unconditionally.
- Split at the **System 1 / System 2** boundary: fast local action net, latency-tolerant VLM/planner (local-preferred, cloud-offloadable).
- Right-size the local model (quantize, distill) — edge placement of a large model buys almost nothing (§3).
- Design an explicit **degradation ladder**: full cloud reasoning → local VLM → reflex-only autonomy → human teleop (1X pattern) → safe-stop.
- Target a concrete offline floor (Robrain's 85%) and treat cloud as *iterative optimization*, not a dependency.

来源:
- https://deepmind.google/blog/gemini-robotics-on-device-brings-ai-to-local-robotic-devices/
- https://www.figure.ai/news/helix
- https://www.quectel.com.cn/news-and-pr/robrain-v2-0
- https://www.quectel.com.cn/news-and-pr/%E5%90%AC%E5%BE%97%E8%A7%81%E3%80%81%E6%83%B3%E5%BE%97%E9%80%9A%E3%80%81%E5%81%9A%E5%BE%97%E5%88%B0%EF%BC%9A%E7%A7%BB%E8%BF%9C%E9%80%9A%E4%BF%A1%E6%90%BA%E6%89%8B%E9%80%90%E9%99%85%E5%8A%A8%E5%8A%9B
- https://arxiv.org/html/2602.18397v1
- https://arxiv.org/html/2601.14921
- https://arxiv.org/pdf/2505.03673
- https://arxiv.org/pdf/2507.16731
- https://extremcontrol.github.io/ ; https://arxiv.org/html/2602.11321v2
- https://www.nvidia.com/en-us/autonomous-machines/embedded-systems/jetson-thor/ ; https://blogs.nvidia.com/blog/jetson-thor-physical-ai-edge/
- https://aiweekly.co/alerts/figure-ai-helix-02-runs-200-hours-sorts-149K-packages
- https://robotwale.com/article/tesla-optimus-14 ; https://optimusk.blog/blog/what-is-tesla-optimus/ (secondary/enthusiast, unverified)
- https://www.humanoidsdaily.com/news/1x-neo-launch-sparks-debate-on-autonomy-and-teleoperation ; https://www.therobotreport.com/teleop-not-autonomy-the-path-for-1x-neo-humanoid/ (unverified)

---

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

---

## 面向端侧的模型优化 (Model Optimization for Edge)

端侧具身大脑的核心矛盾:VLA (Vision-Language-Action) 模型要在受限的算力/内存/功耗预算内跑到可用的控制频率。四条主线撑起全部优化空间——**动作头架构 (action-head architecture)**、**动作分块 (action chunking)**、**量化 (quantization)**、**异步/协同推理 (async / collaborative inference)**。以下数字大量来自 NVIDIA 的 VLA-Perf 基准 (arXiv 2602.18397),这是目前唯一横跨嵌入式→数据中心硬件的公开 VLA 延迟基准。

### 1. 动作头架构:扩散/流匹配 vs. 自回归 (Action Head: Diffusion/Flow vs. Autoregressive)

- 最大的单点杠杆。自回归 VLA 逐维生成动作 token(14-DoF × chunk 50 ≈ **700 个串行 decode 步**),扩散/流匹配一次性预测整个 chunk,只需固定的少量去噪 pass。
- VLA-Perf 在 NVIDIA B100 上:50-action chunk,标准扩散头 **3.2ms** 端到端 vs. 经典自回归 decode **327.6ms** → **102.4x 加速** (primary)。
- 去噪步数是**次要成本**:B100 上 10 步 = 3.2ms,步数从 10→50(×5)端到端延迟仅 ×2.15(≈6.9ms);transformer 前向传播才是主导项 (primary)。
- 因此**动作头类型 >> 去噪步数 >> chunk 大小**,这是端侧优化的优先级排序(综合 VLA-Perf 分项结论——chunk 影响可忽略、去噪步影响显著、头类型 102x——的推论,论文未直接给出此排序)。

### 2. 硬件层与模型大小的延迟曲线 (Hardware Tier & Model-Size Latency Curve)

π0 (2.7B) 同一模型跨硬件(VLA-Perf,均为短上下文,primary;注:VLA-Perf 将 π0 计为 2.7B = SigLIP-So 0.4B + Gemma-2B 2.0B + Act-M 0.3B,Physical Intelligence 原论文计为 ~3.3B,因把 PaliGemma 整体计为 ~3B——数字差异源于计数口径,非矛盾):

| 硬件 (Hardware) | 端到端延迟 | 频率 | 层级 |
|---|---|---|---|
| Jetson Thor | 52.57ms | 19.0 Hz | 嵌入式端侧 |
| RTX 4090 | 31.06ms | 32.2 Hz | 消费级 |
| A100 | 16.20ms | 61.7 Hz | 数据中心 |
| H100 | 6.15ms | 162.5 Hz | 数据中心 |
| B100 | 3.18ms | 314.4 Hz | 数据中心 |

嵌入式↔数据中心存在 **>16x** 差距。模型大小近似线性缩放频率(B100,同族,primary):

| 模型 | 参数 | 频率 (B100) |
|---|---|---|
| π0 | 2.7B | 314.4 Hz |
| π0-L | 9.1B | 73.6 Hz |
| π0-XL | 16.7B | 39.7 Hz |
| π0-XXL | 81.3B | 9.6 Hz |

- **KV-cache 才是长时程杀手** (primary):1,000 步累积上下文(13.2GB KV cache)时,Jetson Thor 从 19Hz 跌到 **768.3ms (1.3Hz)**,RTX 4090 跌到 900.6ms (1.1Hz),连 B100 也只剩 85.2ms (11.7Hz)。端侧在短上下文领先、长上下文崩溃——因为 Thor 的算力/带宽无法摊薄增长的 cache。端侧设计必须**限制上下文窗口 / 定期清 cache**,不能靠堆历史。

### 3. 动作分块:最省力的延迟隐藏 (Action Chunking)

- **predict-H, execute-open-loop** 是所有现代 VLA 共用的头号延迟隐藏手段 (primary)。chunk 成本**次线性**:VLA-Perf 测得 chunk 50→250(×5)端到端延迟仅 +11%——放大开环 chunk 是"廉价换吞吐"的旋钮(牺牲反应性换频率)。
- 各模型 H 取值差异巨大,反映不同的反应性/吞吐权衡:

| 模型 | H (chunk) | 去噪步数 K | 输出率 |
|---|---|---|---|
| π0 (3.3B) | 50 | 10 (δ=0.1) | 20Hz(臂)~50Hz(移动) |
| GR00T N1 (2.2B) | 16 | 4 (K) | 120Hz(System 1)/10Hz(System 2) |
| SmolVLA (~450M) | 显式 async chunk | flow-matching | 提升控制率 |

### 4. 端侧代表 VLA:小模型 + 扩散/流头 (Edge-Class VLAs)

- **π0 (Physical Intelligence, 3.3B)** (primary):PaliGemma VLM (~3B) + 从零训练的 action expert (~300M);流匹配用 linear-Gaussian 概率路径 + Beta 时间步采样,**仅 10 积分步** vs. 扩散常需数百步(流匹配学到更平滑的 ODE 向量场)。RTX 4090 板载分解:图像编码 14ms + observation 前向 32ms + 10× action 前向 27ms = **73ms**(离板含 WiFi 86ms)。
- **π0-small (470M)** (primary):DistilBERT + ViT + DiT,**无 VLM 初始化**的消融——π0 (VLM 初始化) 显著胜出,尤其细粒度语言跟随任务,证明互联网级 VLM 预训练能有效迁移到动作生成(不只是参数量)。
- **SmolVLA (HF LeRobot, ~450M)** (primary):SmolVLM-2 骨干 + flow-matching action expert (~100M);单 GPU 训练,交错 cross/self-attention,含 async 推理栈解耦感知/规划与执行。**~78.3% 真机平均成功率**,号称可比 10x 大的 VLA。可跑消费级 GPU 甚至 CPU。
- **TinyVLA (<1B backbone)** (primary):在小型高速多模态骨干上挂扩散 policy decoder,**跳过大规模机器人预训练**。MetaWorld sim +21.5%,真机比 OpenVLA (7B) 高 **25.7%**,且更快——小扩散头 VLA 在速度和精度上双杀更大的自回归模型。
- **GR00T N1 (NVIDIA, 2.2B)** (primary):Eagle-2 VLM = 1.34B(System 2,10Hz 推理)+ DiT flow-matching policy(System 1,120Hz);**仅 K=4 去噪步**、H=16。L40 GPU bf16 采样 16-action chunk = **63.9ms**(以上均经 arXiv 2503.14734 逐项核实)。扩散头额外去噪缓冲显存 **~4–6GB**(unverified)——GR00T N1 与 VLA-Perf 原文均未给出该 GB 区间,系推测数字。

### 5. 量化:从 INT8 到 1-bit (Quantization)

| 方案 | 显存 | 性能损失 | 备注 |
|---|---|---|---|
| OpenVLA-7B INT8 (secondary) | 14GB→~7GB | <5% | 自回归仍慢 |
| OpenVLA-7B INT4 (secondary) | →~3.5GB | 8–12% | 损失大于 OFT 变体 |
| OpenVLA bf16 vs INT4 (secondary) | — | — | ~500ms/action (A100) → INT4 仍 ~100–200ms |
| Llama-3.2-11B-Vision NF4 (primary) | 20GB→6.5GB | 近云端精度 | Unitree G1-EDU 边缘部署;VLM 非 VLA |
| **BitVLA 1-bit/ternary** (primary) | **11x↓** | 持平 4-bit OpenVLA-OFT | 4.4x 延迟↓,仅用 29.8% 显存 |

- 关键结论:**量化改善内存/精度,但改不了架构瓶颈** (secondary)。OpenVLA 即使 INT4 仍 ~100–200ms/action,远高于扩散/流 VLA 的个位数 ms——自回归逐 token decode 是结构性瓶颈,不是精度问题。
- **BitVLA** (primary) 是本轮研究最激进点:基于 BitNet b1.58 2B4T(权重∈{-1,0,1})+ "Quantize-then-Distill" 把视觉编码器压到 1.58-bit(全精度 teacher 对齐表征),**11.0x 显存↓ + 4.4x 端到端延迟↓** vs. 全精度 OpenVLA-OFT,精度持平 4-bit PTQ 基线而仅用其 29.8% 显存。

### 6. 异步与协同推理 (Async & Collaborative Inference)

- 独立 async(System-2 限 10Hz)在 **5G 网络**上(VLA-Perf Table 8,B100):**async 215.3Hz vs sync 35.9Hz = 5.99x** (primary)。异步解耦(慢规划 / 快执行)是端侧提频的正解。
- **但纯设备-服务器卸载是净亏损** (primary):服务端协同加速随网络递减——Ethernet 10G **2.24x**、WiFi 7 1.26x、5G 仅 1.05x(VLA-Perf Table 9,B100+10Hz cap);而 KV-cache 下载开销 Eth 10G 12.4ms / WiFi7 43.7ms / **5G 257.7ms**。原文结论:协同推理**总是慢于纯服务端推理**,且除快速有线网(Eth 10G)外通常也慢于纯设备推理。→ 端侧要么全本地异步,要么全云端,**"半卸载"往往最差**。

### 7. 端侧硬件的营销 vs. 实测 (Vendor Claims vs. Measured)

- **NVIDIA Jetson Thor** (secondary):Blackwell GPU,128GB LPDDR5X 统一内存,2070 FP4 TFLOPS,40–130W;NVIDIA 官方博客/产品页仅明确宣称"生成式 AI 较 Jetson Orin 提速最高 5x"(2070 TFLOPS、128GB、40–130W 均已核实)。**"120 action tokens/sec 用于 π0.5 类 VLA"这一具体营销值未能在 NVIDIA 官方博客或产品页找到 (unverified)**——引用需谨慎;AGX Orin 的"275 TOPS INT8 / 60W"来自 Orin spec sheet(该博客未给 Orin 绝对 TOPS)。无论如何,VLA-Perf 独立实测同级 π0 (2.7B) 在 Thor 上仅 **19Hz / 52.57ms**——独立端到端实测远低于任何峰值/token-rate 宣称,端侧选型别信 spec sheet 峰值。
- **Quectel SP895BD-AP 模组(CES 2026,2026-01-05 发布)** (unverified):Qualcomm Dragonwing Q-8750 SoC(3nm,8 核 Oryon),支持 INT4/INT8/INT16/FP16;NPU 口径不一——Qualcomm 官方称"最高 **77 TOPS** 密集 AI 算力",Quectel/CNX 报道则称"**80 TOPS** NPU"(约差 3 TOPS),声称"支持端侧运行最高 **110 亿参数** LLM"(此点两家一致)。**无任何 11B 实跑 accuracy/Hz**,非 VLA 专用基准——纯厂商声明,谨慎引用。

### 端侧优化决策清单 (Edge Optimization Checklist)

1. **先选扩散/流动作头**(~100x 杠杆),自回归只在必须逐 token 输出时用。
2. **动作头类型 > 去噪步数 > chunk 大小**:去噪步 10 通常够,chunk 可大(次线性成本)。
3. **限制上下文/清 KV-cache**:长时程 cache 是端侧真正的墙,不是模型大小。
4. **量化到内存预算**:BitVLA 1-bit 是激进上限;但别指望量化解决自回归慢。
5. **异步全本地,或全云端**;避开半卸载(传输开销吃掉收益)。
6. **选型看实测不看峰值 TOPS**:Thor 端到端实测仅 19Hz(52.57ms),远低于任何峰值 TFLOPS / token-rate 营销宣称。

来源:
- VLA-Perf: How Fast Can I Run My VLA? — arXiv 2602.18397 / github.com/NVlabs/vla-perf
- π0: A Vision-Language-Action Flow Model — arXiv 2410.24164 / pi.website/blog/pi0
- SmolVLA — arXiv 2506.01844 / huggingface.co/lerobot/smolvla_base
- TinyVLA — arXiv 2409.12514
- GR00T N1 — arXiv 2503.14734
- OpenVLA — arXiv 2406.09246
- BitVLA — arXiv 2506.07530
- Vision-Language Models on the Edge for Real-Time Robotic Perception — arXiv 2601.14921
- Quectel SP895BD-AP — quectel.com/product/sp895bd-ap-smart-module / iotbusinessnews.com (2026-01) / cnx-software.com (2026-01)
- NVIDIA Jetson Thor — NVIDIA 产品页 + developer blog "Introducing NVIDIA Jetson Thor"

---

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

---

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

---

## 功耗 / 散热 / 成本工程 (Power, Thermal & Cost)

The on-device brain is not free silicon on a shelf — it is a heat source inside a sealed, moving robot on a battery budget. Three constraints bind together: **perf-per-watt** (每瓦性能) beats peak TOPS, **thermal design** (散热) sets the true sustained ceiling, and **cost tiering** (成本分层) means most robots should *not* buy the biggest brain. The engineering thesis: reduce precision (量化) to convert the same watts into more usable inference, then design the thermal path so those watts actually flush out before the SoC trips.

### 芯片级功耗与能效 (Chip-level power & efficiency)

Jetson AGX Thor is the reference "big-brain" module already cited in [hardware.md](hardware.md)'s compute table; the numbers below are the design envelope it exposes.

| Metric | Jetson AGX Orin | Jetson AGX Thor (T5000) | Source |
|---|---|---|---|
| Power envelope | 15–60 W | **40–130 W** | NVIDIA blog (primary) |
| Peak AI compute | 275 TOPS INT8 | **2,070 TFLOPS FP4 sparse** / 1,035 dense FP4 / 517 dense FP8 | NVIDIA blog (primary) |
| CPU | 12-core A78AE | 14-core Neoverse-V3AE @ 2.6 GHz | NVIDIA blog (primary) |
| Memory | 64 GB | 128 GB LPDDR5X | NVIDIA blog (primary) |
| Gen-over-gen claim | baseline | **7.5× AI compute, only 3.5× energy efficiency** vs Orin | NVIDIA blog (primary) |

- The load-bearing observation is the **7.5× vs 3.5× gap** (primary): raw compute scaled roughly **2.1× faster than efficiency** across the Orin→Thor generation. Bigger VLA models want *more than proportionally* more power — unless software (quantization) closes the gap. Silicon alone does not give you a free perf-per-watt win.
- Practically, this is why the 40–130 W envelope is so wide: the same module is a 40 W part running a small policy or a 130 W part running a multi-billion-parameter [VLA](vla-models.md) — and, as the thermal section shows, those two operating points need physically different cooling hardware.

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
- **Real-time gap** (secondary): a humanoid joint controller wants **~1 kHz** hard-real-time cycles (the "split-brain" MCU/x86 loop in [hardware.md](hardware.md)), while the VLA "brain" runs far slower. GR00T N1's compressed-action-token + parallel decoding pushes per-step VLA latency **below 5 ms**, closing that gap *on the same power budget* — an architectural trick, not more watts.
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

A recurring claim (via the Witt / New Yorker piece already cited in [data.md](data.md)) is that compute takes **~60%** of a robot's electricity vs **~20%** for a human brain of body energy. That framing is **load-state-dependent and mostly wrong for a working robot**:

| System state | Whole-system draw | Thor share (@130 W max) | Source |
|---|---|---|---|
| Idle / standing | 250–500 W | **~26–52%** | Longsing Tech (secondary) |
| Normal walking | 700–1,500 W | **~9–19%** | Longsing Tech (secondary) |
| Peak (lift / stairs / recovery, 5–10 s) | 2,000–4,000 W | **~3–6%** | Longsing Tech (secondary) |

- Reference pack: ~**1.99 kWh** (51.8 V, 38.4 Ah NMC) — consistent with the ~2 kWh class in [hardware.md](hardware.md). Compute is only a large share of draw when the robot is **nearly stationary**; during locomotion, **locomotion dominates** (>70% by one aggregator estimate that puts compute/"agentic autonomy" at ~**20–25%** during active operation — unverified precise attribution, but consistent with the ~9–19% walking-state figure above). At the peak-load band a 130 W Thor is only **~3–6%** of draw, not <5% flat — at the 2,000 W low end the share is ~6.5%, so "<5%" holds only above ~2,600 W.
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

---

## 软件栈 & 运行时 (Software Stack & Runtime)

> There is **no standard "robot brain OS."** The de-facto stack is a two-tier split — a Linux+PREEMPT_RT (or vendor RTOS-augmented Linux) host running perception/planning/VLA inference, plus a bare-metal MCU/RTOS owning the hard-real-time motor loop — glued together by ROS 2 (soft-real-time middleware) and per-vendor accelerator runtimes (TensorRT / QNN / BPU toolchains) that are **not portable across silicon**. Every vendor stitches its own; portability is paid for in re-ports.

### OS 层:实时性 (Real-time OS layer)

- **PREEMPT_RT merged into mainline Linux only in kernel 6.12** (final enabling commit merged Sept 20 2024; 6.12 released Nov 2024), ending a ~20-year (rt-patch work from c.2004) out-of-tree existence; final printk PR presented to Linus Torvalds at Sept 2024 Open Source Summit Europe (Vienna); real-time support enabled first on x86 / x86_64, ARM64, RISC-V. (primary)
  - Consequence for robot brains: before 6.12, *every* "real-time Linux" stack (Jetson/Ubuntu included) needed a separately-applied out-of-tree patch series, versioned per kernel and often lagging vendor BSPs by months — a recurring integration tax. (primary)
- **PREEMPT_RT is still only *soft* real-time.** The dominant pattern splits work: Ubuntu (typically 22.04) on the AI SoC for perception/planning/VLA; a **dedicated MCU/RTOS** for the sub-millisecond torque/servo loop, because standard Linux cannot give *hard* guarantees at those rates. (secondary)
- **RT-kernel does measurably help ROS 2**: a controlled benchmark (CJME/Springer) found PREEMPT_RT-Linux-ROS2 yields substantially smaller and less-variable max latency across message payload sizes vs. a stock non-RT kernel — the standard justification for pairing ROS 2 with an RT kernel on robot SoCs. (secondary)

### 中间件:ROS 2 仍是软实时 (Middleware — ROS 2 remains soft-RT)

- ROS 2's real-time story is **fundamentally probabilistic/soft, not hard**. As of 2025–2026, academic work is still *characterizing* (not solving) executor/DDS worst-case latency: e.g. *A Survey of Real-Time Support… in ROS 2* (arXiv 2601.10722), *ReDAG-RT* multi-DAG scheduling (arXiv 2603.18238), *Probabilistic Latency Analysis of DDS in ROS 2* (arXiv 2508.10413). (primary)
- **Discovery scales poorly** with node count under default DDS/RTPS. `rmw_zenoh` (Zenoh-based) cuts discovery time by **up to 99.97%** vs. default DDS discovery — relevant to boot-time discovery on multi-node on-device brains; PX4 also supports `rmw_zenoh` as a uORB→ROS 2 bridge. (secondary)
- **Zero-copy for GPU-heavy pipelines — Isaac ROS NITROS**: passes GPU memory handles between nodes (type adaptation REP-2007 / negotiation REP-2009) instead of serializing full image/tensor payloads, avoiding CPU↔GPU copies. **Caveat (verified against docs): zero-copy holds only when all NITROS nodes run in the *same process*.** (primary)

### 推理运行时 & 硬件分层 (Inference runtime & hardware tiering)

Per-vendor runtimes are the robot-brain analog of a "CUDA moment" — and they do **not** interoperate (a Jetson engine ≠ a D-Robotics BPU model ≠ a Qualcomm QNN graph).

| Runtime | Silicon / role | Key facts | sq |
|---|---|---|---|
| **TensorRT** | NVIDIA Jetson/RTX/H100 | GPU-arch-specific engines (non-portable across archs) | primary |
| **TensorRT Edge-LLM** | Jetson Thor/Orin (JetPack 7.1, 2026) | Python-free C++ LLM/VLM runtime; EAGLE-3 spec-decode, NVFP4, chunked prefill; open-sourced (NVIDIA/TensorRT-Edge-LLM); demoed Cosmos-Reason2-8B (NVFP4, ~4× mem cut) on Thor, Qwen3-4B (INT4 AWQ, ~2GB) on Orin Nano; Bosch/ThunderSoft/MediaTek building on it (CES 2026) | primary |
| **QNN / AI Engine Direct** (QAIRT SDK) | Qualcomm Snapdragon 8 Gen2/3/8 Elite, X-laptops, auto/XR | Supersedes older SNPE; per-operator control across CPU/Adreno GPU/Hexagon NPU | secondary |
| **BPU toolchain** | D-Robotics RDK X5 | Proprietary, parallel to & non-interoperable with TensorRT | primary |

**SoC-vs-model-size tiering (sizing rule of thumb):** (primary)

| SoC | Target model class | Notes |
|---|---|---|
| Jetson AGX Thor 128GB | **20B–120B** (e.g. Llama 3.2 Vision 70B) | flagship humanoid brain |
| Jetson AGX Orin 64GB | **4B–20B** | mainstream |
| D-Robotics RDK X5 | small VLA / classic ROS 2 | Ubuntu 22.04, octa-core A55 "Sunrise 5", **10 TOPS BPU** + 32 GFLOPS GPU; ships "NodeHub" 200+ plug-and-play ROS 2 modules (primary) |
| Qualcomm Snapdragon 8-class | mobile/edge | ~**15 TOPS @ 5–8W** (unverified) |

### VLA 部署:System 1 / System 2 与异步分块 (VLA deployment — S1/S2 split & async chunking)

- **Dual-system is now concrete, not just a metaphor.** GR00T N1 (Mar 2025 paper): System 2 (VLM) at **10Hz** (as reported on an NVIDIA L40), System 1 (Diffusion-Transformer flow-matching action head) at **120Hz**, tightly coupled and jointly trained end-to-end. (secondary)
- **Only the DiT action head is TensorRT-compiled**; VLM backbone (vision encoder + language model) stays in PyTorch. Measured **GR00T-N1.6-3B** DiT speedups (NVIDIA deployment docs; the benchmark table is from the N1.6 release, not the original N1) — engines are GPU-arch-specific ("an engine built on RTX 4090 will not work on H100"): (primary)

| Device | PyTorch | TensorRT | Speedup |
|---|---|---|---|
| RTX 5090 | 58ms / 17.3Hz | 31ms / 32.1Hz | 1.86× |
| H100 | 77ms / 13.0Hz | 36ms / 27.9Hz | 2.14× |
| RTX 4090 | 82ms / 12.2Hz | 43ms / 23.3Hz | 1.92× |
| Jetson Thor | 117ms / 8.6Hz | 92ms / 10.9Hz | 1.27× |
| Jetson Orin | 300ms / 3.3Hz | 173ms / 5.8Hz | 1.73× |

- **Action chunking amortizes latency.** Physical Intelligence **π0** = ~3B PaliGemma VLM + 300M flow-matching "action expert"; runs at **50Hz**, emitting a 50-step chunk (≈1s of control) in one **~73ms** pass on a consumer RTX GPU. (primary)
- **Real-Time Chunking (RTC)** — training-free, any diffusion/flow VLA: predicts the next chunk *while the current one executes*, "freezing" already-committed actions and "inpainting" the rest, blending old/new to kill the "robot idles waiting for next chunk" stall. (primary)
- **LeRobot async-inference** (RobotClient ↔ PolicyServer) is the open reference S1/S2 pattern: knobs `actions_per_chunk` (default 50, typical 10–50) and `chunk_size_threshold` (docs-table default 0.7; 0.5–0.6 recommended — when queue is ≤ that fraction full, send fresh observation); overlaps merged via `aggregate_fn_name=weighted_average`. (primary)
- **Policy memory footprint gates hardware**: **π0 ≈ 14GB** at inference vs. **SmolVLA ≈ 2GB** — the first check when choosing on-device compute (Orin Nano vs AGX) and feasible control fps. (primary)

### 碎片化的证据 (Fragmentation, concretely)

- LeRobot — the "open reference stack" — still needs a **per-vendor porting layer** to run off NVIDIA/Qualcomm silicon: D-Robotics ships **`rdk_LeRobot_tools`**, a dedicated BPU adapter (PyTorch→ONNX→Horizon toolchain→`.hbm`; targets RDK X5 "bayes" and RDK S100 "nash"; **currently verified for ACT policies only**, on S100), and a NodeHub module is not portable to Jetson/Isaac ROS without a re-port. (primary) → Same policy code, N vendor stitch-jobs.

来源:
- https://www.hackster.io/news/linux-can-now-power-real-time-operating-systems-as-the-preempt-rt-patch-set-is-merged-into-mainline-dde8fe8c7308
- https://en.wikipedia.org/wiki/PREEMPT_RT
- https://developer.d-robotics.cc/en/rdkx5
- https://www.cnx-software.com/2025/06/30/d-robotics-rdk-x5-development-board-features-sunrise-x5-octa-core-soc-with-10-tops-bpu-for-ros-projects/
- https://arxiv.org/pdf/2601.10722 ; https://arxiv.org/pdf/2603.18238 ; https://arxiv.org/pdf/2508.10413
- https://cjme.springeropen.com/articles/10.1186/s10033-023-00976-5
- https://github.com/ros2/rmw_zenoh ; https://docs.px4.io/main/en/middleware/zenoh
- https://nvidia-isaac-ros.github.io/concepts/nitros/index.html ; https://developer.nvidia.com/blog/boosting-custom-ros-graphs-using-nvidia-isaac-transport-for-ros
- https://www.jetson-ai-lab.com/tutorials/tensorrt-edge-llm/ ; https://developer.nvidia.com/blog/accelerating-llm-and-vlm-inference-for-automotive-and-robotics-with-nvidia-tensorrt-edge-llm/
- https://developer.nvidia.com/blog/getting-started-with-edge-ai-on-nvidia-jetson-llms-vlms-and-foundation-models-for-robotics/
- https://nvidia-isaac-gr00t.mintlify.app/deployment/tensorrt
- https://arxiv.org/abs/2503.14734
- https://huggingface.co/blog/pi0 ; https://www.cloderic.com/content/2025-02-27-notes-on-pi0
- https://arxiv.org/pdf/2506.07339
- https://huggingface.co/docs/lerobot/async ; https://huggingface.co/papers/2506.01844
- https://docs.qualcomm.com/bundle/publicresource/topics/80-63442-2/setup.html

---

## 为端侧而生的模型 (Models Built for On-Device)

上一节讲优化手段;本节盘点**为端侧设计/部署的 VLA 模型本身**——谁真能在机器人自带的芯片上离线跑,跑到多少 Hz。核心分野:**端侧原生模型 (edge-native)**(Octo/SmolVLA/TinyVLA/LiteVLA-Edge/BitVLA、以及厂商随机部署的 Helix/GR00T/π0.5/GR-3)vs. **端侧勉强 (server-bound)** 模型(OpenVLA-7B、原生 π0——文献称量化后仍需一台协同服务器,而非真正跑在 Jetson 级边缘)(secondary,建议对照 OpenVLA/π0 原文核实)。

### 1. 参考硬件:Jetson Thor (Reference Edge SoC)

GR00T N1.5/N1.6/N1.7 与 π0.5 端侧部署的公开基准几乎都跑在同一颗芯片上,先立标尺 (primary):

- Blackwell 级 GPU,原生 **FP4** 量化 + Transformer Engine 动态 FP4/FP8 切换;峰值 **2070 FP4 TFLOPS**。
- **128GB** 统一 LPDDR5x 内存,带宽 **273GB/s**;14 核 Arm Neoverse-V3AE CPU;可配 **40–130W**。
- 对比上代 Jetson AGX Orin:**7.5x** AI 算力、**3.5x** 能效。NVIDIA 的 Isaac GR00T Reference Humanoid 用它配 Unitree H2 Plus 本体。

### 2. 端侧模型全景 (The On-Device Model Roster)

| 模型 (Model) | 参数 | 骨干/架构 | 目标芯片 | 最佳公开 Hz(芯片) | 源 |
|---|---|---|---|---|---|
| Figure **Helix S1** | 80M | visuomotor policy | 板载嵌入式双 GPU | **200Hz**(onboard) | primary |
| Figure **Helix S2** | 7B | 互联网预训练 VLM | 同上 | 7–9Hz(onboard) | primary |
| **GR00T-N1.6-3B** | 3B | VLM + DiT 动作头 | Jetson Thor | 10.9Hz(TensorRT 现货)/ 22–24Hz(手写 CUDA) | primary |
| **π0.5** | ~3B | PaliGemma 系 | Jetson Thor | ~10–11Hz(TensorRT+NVFP4)/ 23Hz(手写 CUDA) | primary |
| **π0** | ~3B | PaliGemma | Jetson Thor | 22Hz(手写 CUDA) | primary |
| **π0-small** | 470M | 跳过 VLM 初始化 | 轻/边缘定位 | 未公布板载 Hz | primary |
| **SmolVLA** | 450M | SmolVLM(层跳过)+ 异步 | 消费级 GPU/CPU/MacBook | 15–30Hz(RTX 4090,非嵌入式) | primary |
| **LiteVLA-Edge** | 256M | SmolVLM-256M,Q4_K_M 4-bit | Jetson AGX Orin | **6.6Hz**(150.5ms,全离线) | primary |
| **BitVLA** | ~2B | BitNet b1.58(三值 {-1,0,1}) | 通用(1-bit) | 未公布板载 Hz(见下) | primary |
| **TinyVLA(-H)** | 70M–1.4B | Pythia + 扩散 policy 解码 | 边缘定位 | 未公布板载 Hz | primary |
| **Octo** | 93M | — | Jetson AGX Orin | 唯一"无需额外优化即可舒适运行" | secondary |
| ByteDance **GR-3** | 4B | Qwen2.5-VL-3B + DiT(MoT,flow-matching) | 机器人自带 NUC(ByteMini) | 延迟/Hz **未公布** | primary |
| AgiBot **GO-1** | — | Genie Operator-1 | 未公布边缘芯片 | 30Hz(训练/评测率,非板载) | unverified |
| Gemini Robotics **On-Device** | 未披露 | DeepMind VLA | 机器人本体(离线) | 未公布 Hz(见下) | primary |

### 3. 三种"为端侧而生"的路线 (Three Design Routes)

**A. 厂商随机随芯片交付(硬件-模型捆绑)**

- **Figure Helix**(primary):整套双系统 VLA 全部**板载、零云依赖**、跑在嵌入式低功耗 GPU 上。S2(7B VLM)7–9Hz 做场景/语言理解与目标序列;S1(80M)**200Hz** 把 S2 的 latent 转成 35-DoF(含手指)连续关节指令。~500 小时遥操数据训练;是首个给人形上半身(含手指)全连续控制、且**同一份权重同时跑两台机器人**的 VLA,展示行为无需任务级微调。**200Hz 反射环 vs. 单位数~30Hz 的 VLM 推理环差一个数量级——这正是双系统 (System1/System2) 架构的核心工程理由。**
- **Gemini Robotics On-Device**(primary,2025-06-24):DeepMind 首个开放**本地微调**的 VLA,**完全离线跑在机器人硬件上、无网络依赖**(官方称对延迟敏感、间歇/零连接场景有用)。用 Gemini Robotics SDK(基于 MuJoCo)**仅需 50–100 条演示**即可微调;在 ALOHA(主训)、Franka FR3 双臂、Apptronik Apollo 人形上测试,官方声称在 7 项灵巧任务(拉拉链、发牌、装午餐盒等)分布外(OOD)基准上超越同类端侧模型。**注:官方博客未给出具体数值成功率(仅对比图)——"7 项任务 >60% 平均成功率" 无法在一手来源核实,标 (unverified)。参数量 Google 未披露**——横比时是空洞。
- **ByteDance GR-3**(primary):4B,Qwen2.5-VL-3B-Instruct 骨干 + 扩散-transformer 动作头(mixture-of-transformers,flow-matching);部署在**机器人自带 NUC**(ByteMini 平台)而非云。三类数据协同训练(视觉-语言 / 机器人轨迹 / 人类轨迹),强少样本适应与长时程灵巧任务声明。**推理延迟/Hz 技术报告未披露**——相对 GR00T/π0 已公布的 TensorRT 数字是明显缺口。
- **AgiBot GO-1**(unverified):以 AgiBot World 数据集的采集率 **30Hz** 原生训练/评测(本体感知、关节/末端位姿、图像均 30Hz 记录)。但**未公布专门的边缘芯片目标或板载 Hz/延迟**——GO-1 的 30Hz 是训练/评测控制频率,**不能等同真机板载性能**,应标 (unverified)。

**B. 端侧原生小模型(下探到 <500M 甚至 <100M)**

- **SmolVLA**(HF/LeRobot,450M)(primary):**纯社区数据**训练——Hugging Face 上 487 个 LeRobot 标注数据集共 **10M 帧**。VLM 骨干**层跳过 (layer-skipping)** + **异步推理**(当前动作块执行时预算下一块)带来响应快 30%、任务吞吐 2x。单张 RTX 4090 上 15–30Hz;小到能跑 CPU 甚至 MacBook,单张消费级 GPU 可训。
- **TinyVLA**(70M–1.4B,Pythia 骨干)(primary):**TinyVLA-H 成功率超 OpenVLA 25.7%、参数少 5.5x**。LoRA 微调(可训参仅占 5%),扩散 policy 解码器经线性投影挂到冻结的预训练多模态骨干上;定位快速、数据高效,低端 70M 远在 SmolVLA 的 450M 地板之下。
- **LiteVLA-Edge**(arXiv 2603.03380)(primary):**Jetson AGX Orin 上全离线**,256M SmolVLM 骨干经 **Q4_K_M 4-bit GGUF** 量化(llama.cpp CUDA 后端)。平均延迟 **150.5ms ≈ 6.6Hz**,在 ROS2 感知-推理-动作闭环里跑,输出 `geometry_msgs/Twist`。**明确定位为纯端侧(无云回退)**,以此对照它所说"OpenVLA/π0 边缘用需要一台服务器"。
- **Octo**(93M)(secondary):被引为"当前唯一无需额外优化即可在 Jetson AGX Orin 上舒适运行的基础模型",反衬 OpenVLA/π0(3B–7B)一代与真·端侧原生(Octo/SmolVLA/TinyVLA/LiteVLA-Edge/BitVLA)之间的体量鸿沟。

**C. 极致量化路线(1-bit 原生)**

- **BitVLA**(arXiv 2506.07530)(primary):**全原生 1-bit(三值 {-1,0,1})** VLA,建于 BitNet b1.58 2B4T。三段管线:(1) 多模态 1-bit 预训练 →(2) "Quantize-then-Distill" 把视觉编码器压到 1.58-bit 权重 →(3) 机器人适配训练。**~11x 显存↓、端到端 4.4x 加速**,而在 sim 基准与真机任务上**持平全精度 OpenVLA-OFT**;部分对比称可达 32x 模型压缩。代码/权重公开(CC-BY-4.0,GitHub ustcwhy/BitVLA)。**板载具体 Hz 未公布**,但它是本轮"内存下限"最激进的答案。

### 4. π0 家族的端侧成员 (The π0-Family Edge Members)

- **π0-small(470M)**(primary):**跳过 VLM 预训练/初始化**,是原 π0 论文里对照 ~3B 全 π0(建于 PaliGemma)的轻量/边缘定位消融成员。openpi 开源库在 JAX/Flax 与 PyTorch 上实现了 π0、π0-FAST、π0.5。
- **π0.5 于 Jetson AGX Thor**(primary):TensorRT + NVFP4 量化把 ~163ms(PyTorch BF16)降到 **~94ms 总 / ~90ms 纯模型**(TensorRT FP8+NVFP4),**1.73x** 加速 ≈ **10–11Hz** 端到端。而社区论坛用**手写 CUDA kernel**(非官方 TensorRT 路径)报到 **23Hz(44ms)**——官方与手搓路径存在巨大优化落差。
- **GR00T-N1.6-3B 的 TensorRT 分层真相**(primary):Jetson Thor 端到端 92ms / **10.9Hz**,对 PyTorch 仅 **1.27x**——是全表最差加速比(RTX 5090 1.86x、H100 2.14x、RTX 4090 1.92x、Orin 1.73x)。原因:**只有 DiT 动作头拿到 TensorRT 大头(Action Head 3.59x)**,视觉编码器/LLM 仍留在 PyTorch;TensorRT engine 还**绑 GPU 架构,换芯片必须重编**。绕开 TensorRT 的 Q/DQ 开销、用手写 CUDA kernel,Thor 才升到 **22–24Hz**。

### 端侧选型要点 (Selection Takeaways)

1. **先分"原生"还是"server-bound"**:OpenVLA-7B/原生 π0 即便量化,文献仍说需协同服务器;真上机器人自带芯片选 Octo/SmolVLA/TinyVLA/LiteVLA-Edge/BitVLA,或厂商捆绑的 Helix/GR00T/π0.5/GR-3。
2. **官方数字 ≠ 可达上限**:Thor 上 GR00T 10.9Hz(TensorRT)vs. 22–24Hz(手写 CUDA)、π0.5 10–11Hz vs. 23Hz——官方/手搓落差常达 2x,预算频率要给手工优化留空间。
3. **警惕"训练率冒充板载率"**:GO-1 的 30Hz、GR-3 未公布 Hz——训练/评测频率不是真机端到端性能。
4. **反射环与推理环分层**:Helix S1 200Hz vs. S2 7–9Hz 差一个量级,这是双系统架构存在的根本原因,单模型很难同时满足两端。

来源:
- Gemini Robotics On-Device — deepmind.google/blog/gemini-robotics-on-device-brings-ai-to-local-robotic-devices
- NVIDIA GR00T TensorRT 基准 — nvidia-isaac-gr00t.mintlify.app/deployment/tensorrt
- NVIDIA 开发者论坛(Thor/RTX 手写 CUDA)— forums.developer.nvidia.com/t/real-time-inference-on-thor-rtx-pi0-5-gr00t-n1-6-1-7-.../368788
- NVIDIA Jetson Thor — developer.nvidia.com/blog/introducing-nvidia-jetson-thor-the-ultimate-platform-for-physical-ai
- Figure Helix — figure.ai/news/helix
- π0 论文 — arxiv.org/html/2410.24164v1 ; openpi — github.com/Physical-Intelligence/openpi
- π0.5 on Thor — jetson-ai-lab.com/tutorials/openpi_on_thor
- SmolVLA — huggingface.co/blog/smolvla
- LiteVLA-Edge — arxiv.org/abs/2603.03380
- BitVLA — arxiv.org/abs/2506.07530
- TinyVLA — arxiv.org/abs/2409.12514
- Foundation Models for Robot Manipulation 2025(secondary 聚合)— roboticscenter.ai/research/foundation-models-robot-manipulation-2025
- ByteDance GR-3 — arxiv.org/html/2507.15493
- AgiBot World Colosseo / GO-1 — arxiv.org/abs/2503.06669

---

## 端侧学习 / 自适应 & 数据飞轮 (On-Device Learning & Data Flywheel)

An on-device brain that ships frozen is a dead brain. The economically decisive property is not peak inference quality on day one but **the rate at which the deployed fleet improves itself** — the loop from *deploy → collect experience → curate → fine-tune → redeploy*. This section separates three distinct regimes that are routinely conflated: (1) **cloud-scale training** (thousands of episodes to acquire a genuinely new skill), (2) **on-device few-shot adaptation** (tens of demos to calibrate/adapt an existing skill), and (3) **test-time compute** (spend more FLOPs *per action* at inference to buy accuracy, trading directly against control-loop Hz). All three feed a fleet-level **data flywheel**, whose real engineering content is curation, OTA safety, and privacy — not the model.

### The two data regimes — cloud-scale acquisition vs. on-device adaptation

The single most abused number in this space is "50 demos." It is real, but it applies only to *adaptation*, not *new-skill acquisition*. The Gemini Robotics technical report states both bounds explicitly:

| Regime | Data budget | What it buys | Where it runs | Source |
|---|---|---|---|---|
| On-device few-shot adaptation | **50–100 demonstrations** | task-specific calibration/adaptation of an *existing* skill; **"for 7 of 8 tasks, fine-tuning achieved success rate above 70% with at most 100 demonstrations"** (per-task breakdown in Fig. 26; no explicit cross-task average is reported *(unverified: ">60% avg" is an interpolation)*) | on-robot (Gemini Robotics On-Device) | arXiv:2503.20020 (primary) |
| Cloud-scale skill acquisition | **2,000–5,000 episodes / task** | genuinely new long-horizon / dexterous skills | cloud training | arXiv:2503.20020 (primary) |

**Gemini Robotics On-Device** (Google DeepMind, launched **2025-06-24**) is the first VLA in the Gemini Robotics family opened for fine-tuning, and it runs **inference fully locally on the robot's onboard computer, "independent of a data network"** (robust to intermittent/zero connectivity); developers fine-tune via the Gemini Robotics SDK (MuJoCo sim + "Trusted Tester" program) (primary). *(Note: DeepMind confirms network-independent **inference**; it does not explicitly state the **fine-tuning** step itself runs offline — "fully local training with no network" is (unverified).)* This is architecturally distinct from the **full cloud-hybrid Gemini Robotics** model, which is a **split fast/slow design**: a large cloud-hosted VLA backbone (distilled from Gemini Robotics-ER) paired with a **local low-level action decoder**. That hybrid reports **~250 ms** end-to-end observation→action-chunk latency, an **effective 50 Hz** control rate (each chunk = multiple actions), and a backbone query→response latency cut from "seconds" to **<160 ms** via distillation to the smaller on-robot decoder (primary). *Takeaway: "50 demos on-device" and "250 ms cloud-hybrid" describe two different products; do not merge them.*

### Continual learning — is catastrophic forgetting actually the enemy?

Two opposing findings, both worth carrying:

- **Explicit architectural insulation.** Physical Intelligence's **"Knowledge Insulation"** (introduced with **π0.5 + KI**; arXiv:2505.23705): the VLM backbone trains on π0-FAST discrete action tokens + web-data co-training targets, while a *separate action expert* produces continuous actions (flow/diffusion) and **its gradients are blocked ("Stop Gradient") from flowing back into the VLM backbone** — "gradients from the action expert do not flow into the VLM backbone." This is gradient isolation against semantic/language forgetting during action fine-tuning — not replay buffers, not EWC-style regularization (primary — pi.website/research/knowledge_insulation, arXiv:2505.23705). *(π0.6, Nov 2025, builds on the same PI recipe lineage; explicit "Knowledge Insulation" naming is documented for π0.5 — π0.6 attribution (unverified).)*
- **Counter-narrative: VLAs may not need heavy machinery.** A **2026** arXiv study (Liu et al.) found pretrained VLA models are **"surprisingly resistant to forgetting in continual learning"** vs. small-policy-from-scratch baselines. Its actual mechanism is **simple Experience Replay (ER) in supervised continual imitation learning** — *not* an anti-forgetting-machinery-free result and *not* on-policy RL. The load-bearing finding: **large-scale pretraining changes the dynamics** so that ER achieves near-zero forgetting with a **tiny replay buffer (~2% of data)**, where from-scratch models need **>20%**; "forgotten" skills also recover rapidly with minimal fine-tuning (secondary, single-source — arXiv:2603.03818). *Caveat: still contradicts classical RL/vision continual-learning results where forgetting is severe; treat as VLA-specific and provisional — and note it does still use a replay buffer.*

**Engineering read:** insulation (π-style) is the safe default when a *single* model must keep both language and motor competence; the "resistant to forgetting" result is promising but not yet load-bearing enough to design against.

### Fleet-scale RL and the closed loop ("Learning While Deploying")

- **LWD** closes deploy→shared-experience→improve→redeploy across a **fleet of 16 dual-arm robots** on **8 real-world manipulation tasks**, reaching **95% average success** (primary — arXiv:2605.00416). Mechanism: **DIVL** (Distributional Implicit Value Learning) for stable value estimation + **QAM** (Q-learning via Adjoint Matching) to extract policies from flow-based VLA models, fed by autonomous rollouts **plus human interventions** collected fleet-wide — i.e. **offline-to-online RL**, not imitation learning. The load-bearing point: *human interventions are a first-class data source*, not a fallback.

### The data flywheel, quantified (Scanford / "Robot-Powered Data Flywheels")

The clearest end-to-end flywheel measurement in the literature:

| Stage | Concrete number | Source |
|---|---|---|
| Deploy | Franka FR3 + TidyBot++ base, **10 days × 4 h/day = 40 h** scanning library shelves | arXiv:2511.19647 (primary) |
| Human cost | only **26 interventions total** (~2.6/day, each **<5 min**); est. **18.7 h manual labor saved** | " |
| Curation | **8,232** raw labeled images → **5,019** training images via string-similarity DB matching | " |
| In-domain gain | accuracy **32.4% → 71.8%** after **one** fine-tuning cycle | " |
| Domain-adjacent gain | OCR far weaker: EN **24.8%→46.6%**, ZH **30.8%→38.0%** | " |

**Lesson:** the flywheel's real engineering is **automated curation** (which filtered ~39% of raw images) and the **in-domain vs. domain-adjacent gap** — flywheels compound fast on the exact deployed distribution and *much* more slowly on adjacent capabilities.

### Test-time compute — buying accuracy against the Hz budget

The System-2-for-robots question is a resource-allocation problem: every extra sample/iteration spent reasoning is subtracted from control frequency. The quantified tradeoffs:

| Method | Compute spent | Accuracy gain | Latency / Hz cost | Source |
|---|---|---|---|---|
| **RoboMonkey** | sample **16 actions** + Gaussian-perturbation verifier | **+25 pts** OOD (60% vs 35% OpenVLA); power-law error↓ vs sample count across CogACT/Octo/OpenVLA/SpatialVLA | **+~650 ms** on 1×H100 (−41.3% vs naive); real-world **~1.5 Hz** | arXiv:2506.17811 (primary) |
| **E-TTS** | co-scale reasoning + action sampling, history-aware verify | **+150% relative** success (optimal config) | only **+46.6%** latency | arXiv:2606.27268 (secondary) |
| **Recurrent-Depth VLA** | latent iterative reasoning (not token CoT) | tasks at **0%@1-iter → >90%@4-iter**; simple tasks saturate fast | avoids token-CoT memory/latency; designed for on-device budget | arXiv:2602.07845 (secondary) |

**Key architectural answer** — the mainstream reconciliation is the **dual-system (System-1/System-2)** split: a large VLM "slow system" at **~1–9 Hz** for scene/language/planning, a lightweight (often diffusion) "fast system" for motor control (typically **20–50 Hz**, up to **200 Hz** at the extreme). Figure **Helix**: onboard VLM System-2 (7B) at **7–9 Hz**, paired with an **80M System-1 running at 200 Hz** (its fast side sits *well above* the 20–50 Hz band — do not lump Helix's fast loop into 20–50 Hz); HiRT / RoboDual / OpenHelix / FiS-VLA / UniFS follow the more typical **1–5 Hz slow / 20–50 Hz fast** split (secondary — figure.ai/news/helix, arXiv:2506.01953 + dual-system VLA literature). RoboMonkey's ~1.5 Hz shows why naive 16-sample verification is a *slow-system* technique — it cannot live in the fast loop.

**Budget ceiling:** all of the above must fit **NVIDIA Jetson Thor** if run locally rather than via a cloud backbone — up to **2,070 (sparse) FP4 TFLOPS** (1,035 dense), **128 GB** LPDDR5X, **40–130 W**; **up to 7.5× AI compute** and **3.5× energy efficiency** vs. Jetson AGX Orin, and **"up to 5× on generative AI models"** — but this 5× is the *max* across LLMs/VLMs/VLAs; the measured **VLA (GR00T N1.5) speedup is ~2.74×**, not 5× (primary — NVIDIA developer blog). RoboMonkey's 16-sample verifier is budgeted for an **H100**, not Thor; on-device test-time scaling must therefore favor *cheap* schemes (recurrent-depth latent iteration) over *sample-heavy* ones (16× verification).

### Fleet operations — flywheel plumbing (teleop, OTA, privacy)

- **Teleop-as-flywheel (1X NEO "Expert Mode").** Human operators remotely pilot the robot through not-yet-autonomous tasks; **every teleop session is recorded, labeled, and fed into the Redwood model** (CEO Børnich: "the first NEO will be less capable than the thousandth NEO"). Privacy mitigations disclosed: operators need owner permission, video can be blurred, owner-defined no-go zones, no takeover without approval — framed as a "social contract" (secondary — therobotreport / engadget).
- **Fleet OTA + cross-robot transfer (Figure).** Whole-fleet simultaneous behavior pushes via OTA, paired with **cross-robot policy transfer** (a policy trained on one robot applies across many without per-robot fine-tuning) — ties flywheel economics to production ramp: more robots → more fleet-hours → more failures → more Helix training data (secondary — figure.ai/news/helix).
- **OTA safety = staged canary.** Best practice: push to **~1%** of fleet first, monitor boot-success / heartbeat / sensor-data-quality; proceed to **10%+** only if nominal; per-device status chain (downloaded→verified→applied→booted→health-check-passed); **automatic rollback** on failed post-update health check without human intervention (secondary — roboticscenter.ai; arXiv:2605.28097 "ICAN-Deploy").
- **Privacy: federated learning (proposed).** The formal privacy mechanism for fleet learning is **federated learning** — raw sensor/interaction data never leaves the device; only model-weight updates are aggregated centrally (e.g. secure aggregation / differential-privacy noise) (secondary; *source text truncated in research — treat as directional, verify aggregation-scheme specifics before citing*).

### Takeaway

Design the brain to **learn after it ships**, and instrument the three regimes separately: (1) reserve cloud training for new-skill acquisition (**2,000–5,000 episodes**), (2) expose **on-device few-shot adaptation** (**50–100 demos**) for per-site calibration, (3) budget **test-time compute** as a *slow-system* resource (dual-system 1–9 Hz / 20–50 Hz), preferring latent-iteration over sample-heavy verification when local. The flywheel's engineering value lives in **automated curation** (Scanford filtered 8,232→5,019) and **fleet safety plumbing** (canary OTA + rollback), while **teleop interventions** are first-class training data and **federated learning** is the privacy story that makes home deployment socially acceptable.

来源:
- https://deepmind.google/blog/gemini-robotics-on-device-brings-ai-to-local-robotic-devices/
- https://arxiv.org/html/2503.20020v1 (Gemini Robotics technical report)
- https://www.pi.website/research/knowledge_insulation ; https://arxiv.org/pdf/2505.23705 (Knowledge Insulation — introduced with π0.5+KI; "Stop Gradient" isolates action-expert gradients from the VLM backbone) ; https://website.pi-asset.com/pi06star/PI06_model_card.pdf (π0.6 lineage)
- https://arxiv.org/pdf/2603.03818 (VLAs "resistant to forgetting", secondary/single-source)
- https://arxiv.org/abs/2605.00416 (Learning While Deploying, DIVL + QAM)
- https://arxiv.org/html/2511.19647v1 (Robot-Powered Data Flywheels / Scanford)
- https://arxiv.org/html/2506.17811 (RoboMonkey)
- https://arxiv.org/html/2606.27268v1 (E-TTS)
- https://arxiv.org/pdf/2602.07845 (Recurrent-Depth VLA)
- https://arxiv.org/html/2506.01953v1 (Fast-in-Slow) + dual-system VLA literature
- https://blogs.nvidia.com/blog/jetson-thor-physical-ai-edge/ ; https://developer.nvidia.com/blog/introducing-nvidia-jetson-thor-the-ultimate-platform-for-physical-ai
- https://www.therobotreport.com/teleop-not-autonomy-the-path-for-1x-neo-humanoid/ ; https://www.engadget.com/ai/1x-neo-is-a-20000-home-robot-that-will-learn-chores-via-teleoperation-040252200.html
- https://www.figure.ai/news/helix ; https://www.figure.ai/news/helix-logistics
- https://www.roboticscenter.ai/learn/remote-robot-fleet-management-guide ; https://arxiv.org/pdf/2605.28097 (ICAN-Deploy)

---

## "做好"的判据 & 评价 (What Makes an On-Device Brain Good)

Every prior section describes *how* to build the brain; this one defines *whether it is good* — and exposes that the field currently **cannot answer that question with public data**. The honest summary: there is a **benchmark crisis** (self-reported numbers, no apples-to-apples task set) stacked on top of an **evaluation crisis** (near-zero public MTBF/intervention-rate disclosure). A buyer's job is to convert marketing Hz/TOPS into a scorecard with a **hardware SKU attached to every number** and a **duty-cycle attached to every success rate**. This section gives that scorecard, its anchor numbers, and where the numbers are missing.

### The scorecard (七维判据)

Seven axes. Each cell pairs a *demandable metric* with the best public anchor and its source-quality tag. **Rule of thumb: reject any Hz/TOPS figure not bound to a named SoC SKU and a sustained (not burst) duty cycle.**

| 判据 (axis) | Demandable metric | Public anchor (best available) | Tag |
|---|---|---|---|
| **实时性 Real-time** | S1 control rate on the *shipping* module, not a desktop GPU | S1 200 Hz / S2 7–9 Hz (Figure Helix, but S1 = 80M params only); full 7B VLA = ~3 FPS on Jetson AGX Orin @INT4 | (primary) |
| **延迟 Latency** | end-to-end perception→action ms on the module SKU | LiteVLA-Edge 150.5 ms (~6.6 Hz) Jetson-class; LiteVLA-H 19.74 Hz outer / 6.08–6.67 Hz semantic on one AGX Orin (best edge dual-rate) | (primary) |
| **泛化 Generalization** | OOD instance/spatial/language success, per task class | π0: 87% Clean-Dish vs 67% Unzip-Bag (in-dist. spread); ACT 86%→~12% unseen dishes; pretrained Qwen-VLA out-generalizes π0.5 on OOD language, exact 32.0%/12.6% figures *(unverified)* | (primary) |
| **可靠性 Reliability** | MTBI / MTBF at 8h×5d duty; uptime % | AutoInspect MTBI **78 h** (non-humanoid); industrial target 95–99% uptime; humanoids today 30–90 min/charge; safety-critical bar = 99.999% | (primary anchor / secondary targets) |
| **功耗热 Power/thermal** | *sustained* W and TOPS/W under continuous load | Jetson AGX Thor 40–130 W, ≤2,070 FP4 TFLOPS, 128 GB, ~3.5× perf/W vs Orin; Hailo-8 ~26 TOPS @2.5–3 W (~10 TOPS/W, ASIC) | (primary / secondary) |
| **成本 Cost** | $/TOPS, brain as % of system BOM | Silicon ~8% of humanoid BOM 2025 → ~5% by 2035; ~$1,400 semi BOM/unit (UBS); ~$35k total BOM, actuators >30% (BofA) | (secondary) |
| **可更新 & 安全 Updatability/Safety** | OTA cadence, canary vs fleet-wide, certified fallback | SSE→MRC formal safe-stop (arXiv 2603.22703); ISO 10218:2025 ties stop-distance to latency+control-freq; Optimus overnight fleet OTA (vendor-claimed) | (primary / unverified) |

### Anchor 1 — the real-time / latency gap (延迟鸿沟)

The single most load-bearing evaluation fact: **full-size VLAs on real edge silicon run 5–30× too slow for smooth manipulation**, and the fast rates you see in papers are usually desktop-GPU rates.

- **Production dual-rate exists, but only by shrinking S1.** Figure Helix runs S2 (internet-pretrained VLM) at **7–9 Hz** and S1 (reactive visuomotor policy, **80M params**) at **200 Hz** across **35 DoF** of the upper body (primary, figure.ai/news/helix). Broader dual-system surveys quote Slow **1–5 Hz** / Fast **20–50 Hz** (primary, arXiv 2510.24795). Key caveat: the 200 Hz is achieved *at 80M params*, not with a full VLA.
- **Full VLA on edge is far below control rate.** OpenVLA (**7B**) hits only **~3 FPS on Jetson AGX Orin even at INT4** (primary). LiteVLA-Edge: **150.5 ms** mean end-to-end (~**6.6 Hz**) on a Jetson-class ROS2 pipeline; LiteVLA-H: **19.74 Hz** outer-loop action emission with **6.08–6.67 Hz** semantic perception on a single **AGX Orin** — the best-reported *edge* dual-rate result (primary, arXiv 2511.05642 / 2603.03380 / 2605.00884).
- **Beware GPU-class Hz.** Parallel/async decoding (PD-VLA) cuts VLA latency **~2.5×** (2.52× action-frequency speedup) and pushes toward **100–200 Hz** — but on **desktop-class GPUs**, not edge modules (primary, arXiv 2503.02310; surveyed in 2505.04769). This is why the scorecard rule is *demand the SKU*.

See §E (the real-time control split) for where these cuts land in silicon, and §I (edge-native models) for the model-shrinking that makes 200 Hz S1 possible.

### Anchor 2 — the generalization scorecard (泛化崩塌)

Success rate is **not one number**; the *same* policy swings 40+ points across task classes, and imitation baselines collapse under OOD shift.

| Policy | Metric | Number | Tag |
|---|---|---|---|
| π0 | in-dist. task spread | **87%** Clean-Dish vs **67%** Unzip-Bag vs **52%** Folding-Shorts (200 demos) | (primary) |
| ACT | standard → unseen-dishes (OOD instance) | **86% → ~12%** (−74 pts) | (primary) |
| Qwen-VLA vs π0.5 | avg OOD *language*-conditioned success | a pretrained Qwen-VLA out-generalizes π0.5 on OOD language; the exact **32.0% / 12.6%** pair is *(unverified — not found in cited source)* | (unverified) |
| GR-Dexter (cross-embodiment) | unseen objects / unseen instructions | **0.85 / 0.83** | (primary) |

Buyer checklist items that fall straight out of this: (1) demand success rates *per task class*, not a headline average; (2) ask whether the policy was **trained cross-embodiment** — GR-Dexter's 0.83–0.85 OOD vs single-embodiment baselines shows this is a measurable lever (primary, arXiv 2512.24210); (3) treat any single OOD number below ~30% language-following as the current *field* floor, not a vendor defect. Sources: arXiv 2511.11298 (π0/ACT). *Caveat: the specific "Qwen-VLA-Instruct 32.0% vs π0.5 12.6%" figures could not be located in arXiv 2505.15660 (which is X-ICM cross-task in-context imitation) or in the Qwen-VLA paper 2605.30280 (which reports Qwen-VLA-aloha 76.9% avg OOD vs π0.5 41.5%) — treat the 32.0/12.6 pair as (unverified).*

### Anchor 3 — the reliability data void (可靠性数据缺口)

This is the axis where the industry is **least honest**, because almost no one publishes MTBF.

- **The demo→24/7 gap is quantitative.** "Stage-walk vs eight hours a day, five days a week, without intervention" — a >90% curated demo success rate does **not** imply fleet reliability (secondary, therobotreport/mindstudio).
- **Duty-cycle reality.** Industrial buyers expect **95–99% uptime**; most humanoids today run **30–90 min** before recharge/intervention, with battery chemistry capping active use at **1–4 h** (secondary, awesomerobots.xyz / patentpc.com). Power/thermal and mechanical failure **compound** with AI-brain failure.
- **Near-zero public MTBF.** The cleanest dated public number is **MTBI = 78 h** from AutoInspect (long-term autonomous industrial *inspection*, non-humanoid but instructive) (primary, arXiv 2404.12785). Against a safety-critical **99.999% ("five nines")** aspirational bar (secondary, patentpc.com), humanoid/VLA vendor MTBF is **essentially unpublished** — this absence *is* the finding.

### Anchor 4 — how to actually benchmark (评测方法学)

Because self-reported numbers aren't comparable, the methodology itself is a criterion.

- **The reproducibility problem is structural.** Most VLA/policy results use lab-specific hardware, task defs, and success metrics; even shared object sets suffer camera/lighting/hardware variance — published rates are **not apples-to-apples** (secondary, arXiv 2510.04354 / 2508.11117).
- **The leading proposed fix: RoboArena.** Decentralized, **double-blind pairwise** real-robot evaluation across **7 institutions** on a shared **DROID** platform, aggregating **600+ pairwise episodes** over 7 generalist policies (**4,284** total eval episodes in the broader dataset) into an ELO-like ranking — the direct answer to "how do you benchmark generalist policies you can't fix a task list for" (primary, arXiv 2506.18123). A buyer should prefer vendors whose numbers come from **third-party pairwise** evaluation over self-run fixed-task demos.

See [evaluation](evaluation.md) and [open-problems](open-problems.md) for the field-wide benchmark discussion.

### Anchor 5 — cost, power, updatability & safety (成本 / 功耗 / 更新 / 安全)

- **The brain is not the cost lever.** Compute is **~8% of humanoid BOM (2025) → ~5% by 2035**; ~**$1,400** semi BOM/unit rising to ~$2,000 by 2050 (UBS); total BOM ~**$35k**, **actuators >30%** (>50% in simple configs) (secondary, UBS / BofA Apr 2025). Optimizing $/TOPS matters far less than actuation/mechanics — but power/thermal still gates duty cycle.
- **Power/thermal: demand sustained, not burst.** Jetson AGX Thor spans **40–130 W** for ≤**2,070 FP4 TFLOPS** / 128 GB, ~**3.5× perf/W** vs Orin — ask *where in that band* the workload sits under **continuous** load (primary, nvidia.com). Contrast Hailo-8 at ~**26 TOPS @2.5–3 W (~10 TOPS/W)** — dedicated ASICs win TOPS/W but can't host large VLA/VLM (secondary, hailo.ai). See §G (power & thermal).
- **Updatability = a fleet-learning loop, with a risk flag.** Tesla Optimus is described as pushing "validated model weight updates… to all Optimus units overnight" (Cortex 67k+ H100-equiv, 70k GPU-h/cycle, 10k+ synthetic variations/task) — but sourcing is a **fan/analyst blog**, so treat figures as **vendor-claimed (unverified)**. Demandable: OTA *cadence*, **canary/staged vs fleet-wide-simultaneous** (simultaneous rollout is riskier on regression), and whether any adaptation is on-device vs cloud-trained-then-pushed. See §J (edge learning).
- **Safety must be control-capable and latency-aware.** The formal anchor is a **Safe-Stoppable Envelope (SSE)**: a state-set from which a certified fallback controller reaches a dynamically-stable **Minimum Risk Condition (MRC)**, with monitors detecting envelope departure (primary, arXiv 2603.22703). **ISO 10218:2025** now makes functional-safety explicit and requires protective-separation-distance math to include **system latency and control-loop frequency** — directly tying the latency axis to certified safety, so a slow brain is *literally* a less-safe brain (primary/standard). See [safety-regulation](safety-regulation.md).

### Takeaway

A "good" on-device brain is **not** the one with the biggest headline TOPS or Hz. It is the one that (1) sustains its S1 control rate on the *shipping SoC* under continuous load (Figure's 200 Hz benchmark — but note that's 80M params, and full VLAs still crawl at 3–7 Hz on Jetson); (2) reports OOD success **per task class** and was trained **cross-embodiment**; (3) can show a **third-party pairwise** eval (RoboArena-style) rather than self-run demos; (4) publishes an **MTBF/intervention rate** at 8h×5d duty at all — which today almost none do; and (5) ships a **certified, control-capable safe-stop** whose stopping math already accounts for brain latency. The brain is only ~5–8% of BOM, so the return on getting these five right is disproportionate. Every number a vendor quotes should arrive with a **SKU and a duty cycle** — its absence is the answer.

来源:
- https://www.figure.ai/news/helix
- https://arxiv.org/pdf/2510.24795 (Survey on Efficient VLA Models)
- https://arxiv.org/pdf/2511.05642 (Lite VLA) ; https://arxiv.org/pdf/2603.03380 (LiteVLA-Edge) ; https://arxiv.org/html/2605.00884 (LiteVLA-H)
- https://arxiv.org/abs/2503.02310 (PD-VLA — parallel decoding, 2.52× action-frequency speedup, desktop-GPU) ; https://arxiv.org/html/2505.04769 (VLA Models survey — cites PD-VLA, GPU-class Hz caveat)
- https://arxiv.org/pdf/2511.11298 (Experiences from Benchmarking VLA Models — π0 in-dist. 87/67/52%, ACT 86%→12% OOD; verified against Table 3)
- https://arxiv.org/html/2505.15660 (Exploring the Limits of VLA Manipulations in Cross-task Generalization / X-ICM — does NOT contain the 32.0/12.6 Qwen figures) ; https://arxiv.org/abs/2605.30280 (Qwen-VLA — reports 76.9% avg OOD vs π0.5 41.5%, also not 32.0/12.6)
- https://arxiv.org/pdf/2512.24210 (GR-Dexter Technical Report — cross-embodiment 0.85/0.83)
- https://arxiv.org/pdf/2404.12785 (AutoInspect — MTBI 78 h)
- https://arxiv.org/abs/2506.18123 (RoboArena — distributed double-blind pairwise real-robot eval)
- https://arxiv.org/html/2510.04354 ; https://arxiv.org/html/2508.11117 (reproducibility / sim-to-real eval)
- https://www.therobotreport.com/ ; https://mindstudio.ai (humanoid deployment gap analysis — secondary)
- https://awesomerobots.xyz (Enterprise Humanoid Robots Guide 2026) ; https://patentpc.com (Robot Downtime Rates & Reliability Data)
- https://www.nvidia.com/en-us/autonomous-machines/embedded-systems/jetson-thor/ ; https://thinkrobotics.com (Jetson AGX Thor review)
- https://hailo.ai/blog/evaluating-edge-ai-processor-in-the-generative-ai-era
- UBS Humanoid Robots semiconductor analysis (via financialmodelingprep.com) ; https://institute.bankofamerica.com (Humanoid Robots 101, Apr 2025)
- https://optimusk.blog/blog/tesla-optimus-software-update (fan/analyst blog — vendor claims unverified)
- https://arxiv.org/pdf/2603.22703 (Learning Safe-Stoppability Monitors for Humanoid Robots — SSE/MRC)
- ISO 10218:2025 revision (functional-safety; stop-distance must include latency + control frequency)

---

## 参考架构 & 模组厂视角 (Reference Architecture & the Module-Maker Read)

> Stepping back from the dual-system model (see §A, Architecture) and the SoC menu (see §F, SoC landscape), the field has converged on a **3-tier control hierarchy** that any on-device brain must physically instantiate: an **S2 deliberative VLM** (7–10 Hz), an **S1 reactive visuomotor policy** (100–200 Hz), and an **S0 hard-real-time motor/reflex loop** (500 Hz–1 kHz). S2/S1 live on the AI SoC; S0 lives on a deterministic MCU / co-processor / Safety Island, decoupled from the Linux clock domain. For a module-maker (模组厂) the load-bearing insight is that the **hard part is not the TOPS number** — it is stitching this heterogeneous, jitter-partitioned, non-portable stack into one shippable module with connectivity and functional safety built in.

### The converged 3-tier reference stack

| Tier | Role | Rate | Silicon / clock domain | OS / runtime | Latency budget |
|---|---|---|---|---|---|
| **S2** deliberative | scene/language understanding, planning | **7–10 Hz** | AI SoC GPU (Jetson) or NPU+CPU | Ubuntu + PREEMPT_RT; TensorRT/QNN/BPU | ~100–140 ms/step OK; cloud-offloadable |
| **S1** reactive | VLA/visuomotor policy → continuous action chunks | **100–200 Hz** | AI SoC GPU/NPU | same SoC, soft-RT (ROS2) | **8.3 ms @ 120 Hz** — must stay local |
| **S0** hard-real-time | joint/torque/servo loop, reflex, safe-stop | **500 Hz–1 kHz+** | deterministic **MCU / RTOS / Safety Island** | bare-metal / RTOS | **sub-ms**, zero OS jitter tolerated |

- **Figure Helix (primary)**: S2 = 7B internet-pretrained VLM @ 7–9 Hz; S1 = 80M cross-attn enc-dec transformer @ 200 Hz; S2 emits a **single continuous latent vector** into S1's token space; both run **entirely onboard on dual low-power embedded GPUs**. [figure.ai/news/helix]
- **NVIDIA GR00T N1 (primary)**: S2 (Eagle-2 VLM) @ **10 Hz** (paper benchmarks this on an NVIDIA L40); S1 (diffusion-transformer, flow-matching action head) @ **120 Hz**; the two modules are **jointly trained end-to-end**. Public GR00T-N1-2B = 2.2B params total (1.34B in the VLM). Below both sits a whole-body torque loop ~1000 Hz (GR1-class) offloaded to MCU/RTOS. [arXiv 2503.14734]
- The S0 tier is exactly the layer that **cannot tolerate software/OS jitter** — hence its physical exile to a separate deterministic co-processor. This is the same "split-brain" boundary the China single-die SoCs (D-Robotics RDK S100: 6× A78AE + BPU + **4× Cortex-R52+ lockstep**) try to collapse onto one package while keeping the R52 cores in a **separate hard-RT island** on-die (secondary). (see §F, SoC landscape)

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
- **Concrete shipping instance — Quectel SH602HA-AP (partial; single-source on module SKU details):** a module-maker's on-device-brain module built on **D-Robotics Sunrise5 (X5M)** (up to **10 TOPS BPU**), Ubuntu OS, **4 GB LP4/LP4x RAM + 64 GB storage** default (40.5×40.5×2.9 mm; launched CES 2026), pairs with Quectel's own **LTE Cat1/Cat4/5G/Wi-Fi6/GNSS** modules for connectivity, and supports VSLAM / binocular depth / 3D point cloud / Transformer-BEV-Occupancy models + LiDAR. It sits at the **low end (10 TOPS, S1-lite/perception tier)**, not the Thor/IQ10 flagship — but it is a real, shipping proof that the "arms-dealer" module play (compute die + connectivity + OS pre-integrated) exists today. (see §F, SoC landscape; Quectel product page)

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

---
