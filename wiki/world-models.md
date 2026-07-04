---
title: World Models for Robotics
slug: world-models
updated: 2026-07-04
confidence: verified
---
> World models are neural networks that predict how an environment evolves — in pixels, latents, or full interactive 3D — given actions, text, or prior frames. Between early 2025 and mid-2026 they moved from research curiosity to core infrastructure for Physical AI: NVIDIA's Cosmos line (culminating in the omnimodal Cosmos 3, June 2026) serves as an open synthetic-data and policy backbone; Google DeepMind's Genie 3 (Aug 2025) generates real-time interactive worlds that now train SIMA 2 agents and underpin the Waymo World Model; 1X uses an action-conditioned video model to evaluate and teach its NEO humanoid; Meta's V-JEPA 2 plans in latent space with zero-shot robot manipulation; and Tesla runs a "neural world simulator" trained on fleet video to close the loop on both FSD and Optimus. World models now fill four roles in robot training — learned simulator, planner, policy evaluator, and data engine — but hallucination, compounding rollout error, weak action-conditioning fidelity, and compute cost remain the binding constraints.

## Why world models matter for robotics

- Robotics' core bottleneck is data and evaluation, not compute: real-robot trials are slow, expensive, and unrepeatable. See [Data for robot learning](data.md) and [Simulation](simulation.md).
- A world model replaces (or augments) hand-built physics simulators with a *learned* simulator trained on video — sidestepping asset creation and some of the sim-to-real gap, at the cost of physical guarantees.
- Four distinct roles have crystallized (taxonomy follows the May-2026 survey "World Model for Robot Learning," arXiv:2605.00080):
  1. **Simulator / evaluator** — roll out a policy inside the model instead of on hardware (1X World Model, Tesla neural simulator, WorldEval).
  2. **Planner** — imagine outcomes of candidate actions and pick the best (V-JEPA 2-AC, 1X NEO's video-prediction-plus-inverse-dynamics loop).
  3. **Data engine** — generate synthetic trajectories to train policies (NVIDIA DreamGen "neural trajectories," Cosmos Transfer domain augmentation).
  4. **Policy backbone** — pre-train on world prediction, fine-tune into an action model ("World Action Models" on Cosmos 3; WMPO-style world-model RL for [VLA models](vla-models.md)).
- Two architectural camps: **generative pixel-space** models (Cosmos, Genie, 1XWM, Tesla — photorealistic, human-inspectable, expensive) vs **latent-space predictive** models (V-JEPA 2 — no pixels, cheaper planning, harder to inspect). Interactive-3D generators (Genie 3, World Labs Marble) form a third branch closer to game engines.

## Landscape comparison

| Model / line | Org | Key release | Type | Action-conditioned? | Primary robotics role |
|---|---|---|---|---|---|
| Cosmos 1 → Cosmos 3 | NVIDIA | Jan 2025 (CES) → Jun 2026 | Pixel video WFM; Cosmos 3 omnimodal (text/image/video/sound/action) | Yes (Cosmos 3 emits joint angles, gripper poses, trajectories) | Synthetic data engine, policy backbone (open weights) |
| Genie 1/2/3 | Google DeepMind | Genie 3: Aug 2025 | Interactive real-time world generation (24 fps, 720p) | Navigation/agent actions; promptable world events | Agent training environments (SIMA 2); AV sim via Waymo World Model |
| 1X World Model (1XWM / Redwood) | 1X Technologies | Paper Jun 2025; product Jan 2026 | Action-conditioned video prediction for a full humanoid | Yes (exact robot trajectories) | Offline policy evaluation; task learning from video for NEO |
| V-JEPA 2 / V-JEPA 2-AC | Meta FAIR | Jun 2025 | Latent-space predictive (JEPA), no pixel generation | AC variant: yes (arm actions/poses) | Zero-shot planning for manipulation; representation backbone |
| Neural world simulator | Tesla | Shown ICCV Oct 2025 | Pixel video, fleet-video-trained, closed-loop | Yes (responds to driving/robot actions) | Closed-loop eval, adversarial scenario synthesis, large-scale RL for FSD + Optimus |
| Waymo World Model | Waymo (on Genie 3) | Feb 2026 | Generative driving sim, camera + lidar output | Yes (driving inputs, language, scene layout) | Long-tail AV scenario simulation |
| Marble | World Labs | Nov 2025 | 3D scene generation (Gaussian splats/meshes) from text/image/video | No (static scenes) | Simulation asset/environment creation |

## The 2026 world-model funding wave

- Capital validated the category in early 2026: three ~$1B+ world-model rounds **closed** within three weeks of each other (round-by-round sourced rows live in [Investment](investment.md)):
  - **World Labs** (Fei-Fei Li, spatial intelligence / Marble): **$1B growth round closed 2026-02-18**, led by Autodesk ($200M), with AMD, Nvidia, Fidelity, Emerson Collective and Sea; total raised $1.23B. The widely quoted **~$5.4B post-money valuation is per Forbes and was never company-confirmed** (Bloomberg had reported ~$5B during talks).
  - **Wayve** (UK, driving world models / embodied AI): **$1.2B Series D closed 2026-02-25 at $8.6B post-money**, plus **$300M in milestone-based capital from Uber** ($1.5B total secured); Eclipse, Balderton and SoftBank Vision Fund 2 co-led.
  - **AMI Labs** (Paris, Yann LeCun's post-Meta world-model lab): **$1.03B seed closed 2026-03-09 at a $3.5B pre-money valuation** — the largest European seed round on record; Nvidia, Samsung, Temasek and Toyota Ventures among backers.
- Read-through: world models are now a funded category independent of robot hardware — spanning spatial intelligence (World Labs), autonomous driving (Wayve), and LeCun's anti-generative JEPA research program (AMI Labs; see the V-JEPA section below). Combined, these rounds (~$3.2B) drove much of H1 2026's record physical-AI funding totals.

## NVIDIA Cosmos: the open world-model platform

- **Cosmos 1 (CES, 2025-01-06):** platform of open-weight "world foundation models" (WFMs) — diffusion and autoregressive video models plus tokenizers, guardrails, and a curation pipeline. Trained on ~9,000 trillion tokens including **20 million hours** of driving/robotics/related video (as of 2025-01). Early adopters included 1X, Agility, Figure AI, Fourier, Galbot, Skild AI, Waabi, XPENG, and Uber. Paper: arXiv:2501.03575; permissive open license.
- **Cosmos Reason (GTC, 2025-03):** physical-AI reasoning VLM added to the family; used for data curation/captioning and as a critic for physical plausibility.
- **Cosmos Predict 2.5 / Transfer 2.5 (2025-10-06):** Predict 2.5 is a flow-based model unifying Text2World / Image2World / Video2World with Cosmos-Reason1 as its text encoder, generating coherent rollouts **up to 30 s**. Transfer 2.5 does controllable sim-to-real style transfer conditioned on spatial control inputs (depth, segmentation, edges) — the main tool for multiplying one demonstration into many photorealistic variants.
- **Cosmos 3 (GTC Taipei at COMPUTEX, 2026-06-01, as of 2026-06):** billed as the first "fully open omnimodel" — native understanding + generation across text, image, video, ambient sound, and **action** (joint angles, gripper positions, trajectory points). Mixture-of-transformers pairs a reasoning transformer with an expert generation transformer. Variants: Super (physics accuracy), Nano (fast inference), Edge (announced, real-time on-device). NVIDIA claims first place among open models on Physics-IQ, PAI-Bench, R-Bench, RoboArena and other leaderboards (vendor claim, as of 2026-06). Launched with a "Cosmos Coalition" (Agile Robots, Black Forest Labs, Generalist, LTX, Runway, Skild AI).
- **Cosmos Policy (paper 2026-01-22, arXiv:2601.16163):** post-trains Cosmos Predict-2 into a unified control model that encodes robot actions, future states, and expected returns as "frames" in one diffusion process — one model does visuomotor control, observation prediction, and return estimation. Reported **98.5% average success on LIBERO** (beating prior diffusion policies and VLAs such as CogVLA 97.4% and OpenVLA-OFT 97.1%) and 67.1% on RoboCasa with 50 demos/task; +12.5% average task completion on two real-world bimanual (ALOHA) manipulation tasks when planning with the model. Positions Cosmos as a backbone for "World Action Models" (WAMs) — pre-trained to imagine, fine-tuned to act.
- Strategic read: Cosmos is NVIDIA's bid to become the "Android of Physical AI" — open weights that seed demand for its simulation and compute stack. See [Organizations](organizations.md) and [Landscape: USA](landscape-usa.md).

## DeepMind's Genie line and its offspring

- **Genie 1 (2024-02):** foundation world model trained on 2D-platformer video; learned latent actions without action labels. **Genie 2 (2024-12):** 3D embodied worlds from a single image, but only ~10–20 s of consistency.
- **Genie 3 (2025-08-05):** text-prompted interactive worlds at **24 fps, 720p**, navigable in real time, consistent for a few minutes with visual memory reaching back ~1 minute; supports "promptable world events" (inject weather, objects, characters mid-rollout). Released as a limited research preview; a public-facing "Project Genie" demo followed in late Jan 2026 (as of 2026-01).
- **Robotics relevance:** DeepMind pairs Genie 3 with its generalist agent **SIMA 2** (2025-11) — agents practice multi-step tasks inside generated worlds and reportedly improve without new human demonstrations, an existence proof for world-models-as-infinite-training-grounds (unverified beyond DeepMind's own reporting).
- **Waymo World Model (2026-02):** frontier generative driving simulator built *on* Genie 3, producing multi-sensor (camera + lidar) rollouts; simulates never-observed long-tail events (tornadoes, animals on road) controllable via language, driving inputs, and scene layouts. The clearest production deployment of the Genie line.
- Acknowledged Genie 3 limits: restricted agent action spaces, weak multi-agent interaction, inaccurate real-world geography, poor text rendering, and interaction horizons of minutes, not hours.

## 1X World Model: evaluation-first for humanoids

- Paper "1X World Model: Evaluating Bits, not Atoms" (2025-06-16): an action-conditioned video model that forecasts high-fidelity, contact-rich futures for a **full-body humanoid** (NEO) — steered by exact robot trajectories, not language, unlike text-to-video models. See [Humanoid robots](humanoid-robots.md).
- Core use is **offline policy evaluation**: predict task-success rates for candidate policy checkpoints without touching hardware. 1X reports high correlation with real-world evals; a world model that is only ~70% accurate still picks the better of two policies ~90% of the time when their real success rates differ by 15 points.
- Scaling result: prediction accuracy improves monotonically with training compute and real NEO data; multi-task training data (shelf + arcade) beats single-task. Known failure: held-out object categories.
- **Product release (2026-01-12):** 1X shipped the world model into NEO — a voice/text prompt makes NEO generate video of future actions, and a built-in **inverse dynamics model** translates predicted frames into motor commands, letting NEO attempt tasks it was never demonstrated (air-fryer baskets, toasters). CEO Bernt Børnich framed it as "the starting point of NEO's ability to teach itself"; press coverage notes real capability remains limited to simple tasks (as of 2026-01). 1X has also stood up a dedicated World Model Lab.

## V-JEPA 2: the latent-space alternative

- Meta FAIR release (2025-06-11), open-source (commercial use permitted): a **1.2B-parameter** self-supervised joint-embedding predictive architecture pre-trained on **1M+ hours** of internet video plus 1M images; predicts in representation space rather than pixels (Yann LeCun's anti-generative thesis — see [Key people](key-people.md)).
- **V-JEPA 2-AC:** action-conditioned variant post-trained on **<62 hours** of unlabeled DROID robot video; enables **zero-shot** pick-and-place via model-predictive control toward image goals on Franka arms in two labs — no environment-specific data, task training, or reward engineering — at **65–80% success** in unfamiliar settings.
- Shipped with three new physical-reasoning benchmarks: **IntPhys 2** (physics-plausibility detection), **MVPBench** (shortcut-controlled video QA), **CausalVQA** (cause-and-effect) — all show humans near-ceiling and models far below, quantifying the physics-understanding gap.
- Benchmarks (as of 2025-06): 77.3% top-1 on Something-Something v2 (motion understanding), 39.7 recall@5 on Epic-Kitchens-100 action anticipation; 84.0 PerceptionTest / 76.9 TempCompass when aligned with an 8B LLM.
- Meta claims planning with V-JEPA 2-AC is ~30× faster than pixel-generative alternatives such as Cosmos (vendor comparison, contested methodology) (unverified).
- Trade-off: latent models are cheap and fast for planning/plausibility checks but produce no video, so they cannot serve as synthetic-data engines or human-inspectable simulators.

## Tesla: one neural simulator for cars and humanoids

- At ICCV (2025-10) Ashok Elluswamy (VP of AI Software, also heading Optimus) detailed a **neural world simulator** trained on Tesla's fleet-video firehose: it synthesizes multi-camera video in response to the AI's actions — a learned closed-loop simulator, not hand-coded physics.
- Uses: closed-loop evaluation of new FSD builds (Elluswamy: open-loop prediction loss "might not correlate to great performance in the real-world"), replay against historical data, synthetic adversarial corner-case generation, and large-scale RL.
- The same simulator generates video of **Optimus** acting (walking, turning in factory settings), supporting Tesla's claim that FSD-derived world modeling "seamlessly transfers" to the humanoid — a single foundation-model strategy across car and robot. At CVPR 2026 (June, Denver) Elluswamy reportedly showed a 36 Hz end-to-end model and reiterated the unified FSD-Optimus vision (secondary sources only) (unverified).
- Tesla's approach is closed and vertically integrated — no papers, weights, or benchmarks — so external validation is impossible; claims should be weighted accordingly. Cross-reference [Landscape: USA](landscape-usa.md).

## World models as data engines: the DreamGen recipe

- NVIDIA GEAR's **DreamGen** (2025) is the canonical pipeline for turning a video world model into a robot-data factory, four stages: (1) fine-tune a video WFM (Cosmos-Predict2) on the target embodiment; (2) prompt with initial frame + language instruction to generate synthetic robot videos; (3) recover **pseudo-actions** via latent-action or inverse-dynamics models; (4) train visuomotor policies on the resulting "neural trajectories."
- Headline result: from teleop data of a **single pick-and-place task in one environment**, DreamGen enabled a GR1 humanoid to perform **22 new behaviors across 10 new environments** — zero-shot behavior and environment generalization. Also validated on Franka and the $100 SO-100 arm and in RoboCasa.
- Scaling: log-linear relationship between number of neural trajectories (tested to 240k) and downstream policy performance.
- Works for contact-rich and deformable tasks (folding, hammering) where classical simulators struggle — the pitch is "real-to-real" data generation that bypasses the sim-to-real gap of [Simulation](simulation.md).
- Related 2026 threads: WMPO (world-model-based policy optimization for VLAs, arXiv:2511.09515), interactive world simulators for policy training/evaluation (arXiv:2603.08546), and iterative co-improvement of VLA + world model (VLAW, arXiv:2602.12063). This is now the main coupling point between world models and [VLA models](vla-models.md).

## Strengths and limits

| Role | What works (as of 2026-07) | What breaks |
|---|---|---|
| Simulator/evaluator | Policy ranking correlates with reality (1XWM, WorldEval arXiv:2505.19017); no asset authoring needed | Hallucinations corrupt the eval signal itself — artifacts (arm ghosting, object teleportation) worsen precisely when evaluating bad policies (MiraBench) |
| Planner | Zero-shot manipulation via latent planning (V-JEPA 2-AC); interpretable visual futures (1X NEO) | Vicious cycle: hallucination → bad action → further out-of-distribution → worse hallucination; long-horizon error compounds |
| Data engine | Log-linear policy gains from neural trajectories (DreamGen); photorealistic domain randomization (Cosmos Transfer) | Pseudo-action extraction is noisy; generated physics can be subtly wrong, teaching policies false dynamics |
| Policy backbone | Video pre-training transfers to action (Cosmos 3 WAMs, GR00T line) | Unproven at scale vs. plain VLA training; heavy compute for pixel-space models |

- **Physics fidelity is the crux:** video models optimize visual plausibility, not dynamics correctness — benchmarks like Physics-IQ and MiraBench (arXiv:2605.29360) exist because the two diverge. A position paper (arXiv:2606.15032) argues world models should be evaluated by decision-making utility, not video quality.
- **Horizon limits:** even Genie 3 holds consistency only for minutes; most robot-relevant rollouts remain ≤30 s (Cosmos Predict 2.5).
- **Action-space poverty:** interactive models expose narrow action interfaces (navigation, simple events) vs. the full contact-rich action space of manipulation — see [Manipulation](manipulation.md) and [Open problems](open-problems.md).
- **Compute cost:** pixel-space rollouts are orders of magnitude more expensive than classical sim; latent models (V-JEPA) trade inspectability for speed.
- **Convergence signal:** by mid-2026 essentially every major Physical-AI player — NVIDIA, DeepMind/Waymo, Tesla, 1X, Meta, World Labs, plus Chinese labs shipping open video-world models — treats world models as a primary pillar, alongside VLAs, of the [tech tree](tech-tree.md). The open question is whether they become the *policy* (WAMs) or stay the *factory* (data/eval infrastructure).

## Sources

- https://nvidianews.nvidia.com/news/nvidia-launches-cosmos-world-foundation-model-platform-to-accelerate-physical-ai-development — Cosmos CES 2025 launch (2025-01-06), open model license, adopter list
- https://blogs.nvidia.com/blog/cosmos-world-foundation-models/ — training scale: 9,000T tokens from 20M hours of real-world/robotics/driving video
- https://arxiv.org/abs/2501.03575 — Cosmos WFM platform paper (components, open license)
- https://huggingface.co/blog/nvidia/cosmos-predict-and-transfer2-5 — Cosmos Predict 2.5 / Transfer 2.5 details (flow-based unification, 30 s rollouts, Oct 2025)
- https://nvidianews.nvidia.com/news/nvidia-launches-cosmos-3-the-open-frontier-foundation-model-for-physical-ai — Cosmos 3 launch (date, omnimodal claims, variants, Coalition, leaderboards)
- https://blogs.nvidia.com/blog/cosmos-3-physical-ai-open-world-foundation-model/ — Cosmos 3 architecture (mixture-of-transformers), native action generation, WAM framing
- https://arxiv.org/abs/2601.16163 — Cosmos Policy paper (submitted 2026-01-22; LIBERO 98.5% / RoboCasa 67.1%)
- https://www.therobotreport.com/nvidia-adds-cosmos-policy-world-foundation-models/ — Cosmos Policy coverage (2026-02-19): 50-demo RoboCasa detail, +12.5% real-world ALOHA planning gain, baseline comparisons
- https://deepmind.google/blog/genie-3-a-new-frontier-for-world-models/ — Genie 3 capabilities, limits, availability (Aug 2025)
- https://en.wikipedia.org/wiki/Genie_(world_model) — Genie lineage, Genie 2 horizon, SIMA 2 + Project Genie timeline
- https://www.techtimes.com/articles/317932/20260606/deepmind-world-models-train-robots-imagined-worlds-sima-practices-inside-genie-3-model.htm — SIMA 2 self-improvement inside Genie 3 worlds (secondary)
- https://waymo.com/blog/2026/02/the-waymo-world-model-a-new-frontier-for-autonomous-driving-simulation/ — Waymo World Model built on Genie 3, camera+lidar, long-tail simulation
- https://www.1x.tech/1x-world-model.pdf — 1XWM paper "Evaluating Bits, not Atoms"
- https://www.1x.tech/discover/redwood-ai-world-model — 1XWM policy-evaluation results, scaling, limitations
- https://www.1x.tech/discover/world-model-self-learning — 1X announcement post (2026-01-12): video prediction + inverse dynamics model shipped into NEO
- https://techcrunch.com/2026/01/13/neo-humanoid-maker-1x-releases-world-model-to-help-bots-learn-what-they-see/ — press coverage of the 1X release (Børnich quote, capability caveats)
- https://arxiv.org/abs/2506.09985 — V-JEPA 2 paper (training scale, V-JEPA 2-AC, benchmarks, zero-shot manipulation)
- https://ai.meta.com/blog/v-jepa-2-world-model-benchmarks/ — V-JEPA 2 official post: 1.2B params, 62 h DROID post-training, 65–80% pick-and-place success, IntPhys 2 / MVPBench / CausalVQA benchmarks
- https://www.marktechpost.com/2025/06/12/meta-ai-releases-v-jepa-2-open-source-self-supervised-world-models-for-understanding-prediction-and-planning/ — V-JEPA 2 release context, 30× planning-speed claim vs Cosmos
- https://www.humanoidsdaily.com/news/tesla-ai-chief-details-unified-world-simulator-for-fsd-and-optimus — Tesla neural world simulator (ICCV talk, uses, FSD-Optimus unification)
- https://research.nvidia.com/labs/gear/dreamgen/ — DreamGen pipeline, 22-behavior result, scaling to 240k neural trajectories
- https://arxiv.org/abs/2605.00080 — comprehensive survey: world models for robot learning (roles taxonomy)
- https://arxiv.org/pdf/2505.19017 — WorldEval: world models as robot-policy evaluators
- https://arxiv.org/pdf/2605.29360 — MiraBench: action-conditioned reliability, hallucination artifacts in robotic world models
- https://arxiv.org/pdf/2511.09515 — WMPO: world-model-based policy optimization for VLA models
- https://techcrunch.com/2025/11/12/fei-fei-lis-world-labs-speeds-up-the-world-model-race-with-marble-its-first-commercial-product/ — World Labs Marble launch (Nov 2025)
- https://finance.yahoo.com/news/ai-pioneer-fei-fei-lis-192214332.html — World Labs $1B round closed 2026-02-18 (Reuters): Autodesk $200M lead; AMD, Nvidia, Emerson Collective, Fidelity, Sea; company declined to confirm valuation
- https://www.forbes.com/sites/josipamajic/2026/06/30/world-model-startups-raise-3-billion-vcs-bet-beyond-llms/ — World Labs ~$5.4B post-money (Forbes figure, not company-confirmed), $1.23B total raised; >$3B into world-model startups in H1 2026
- https://wayve.ai/press/series-d/ — Wayve Series D close (primary, 2026-02-25): $1.2B at $8.6B post-money; +$300M milestone-based Uber capital = $1.5B total secured
- https://techcrunch.com/2026/03/09/yann-lecuns-ami-labs-raises-1-03-billion-to-build-world-models/ — AMI Labs $1.03B seed closed at $3.5B pre-money (2026-03-09); investor syndicate
