---
title: Physical AI Tech Tree
slug: tech-tree
updated: 2026-07-04
confidence: verified
---
> Physical AI progresses as a layered dependency stack: **hardware** (actuators, hands, sensors, compute, batteries) enables **perception**, which feeds **control** (locomotion, whole-body, manipulation primitives), which is increasingly subsumed by **learning** (imitation + RL + sim-to-real), which at scale produces **foundation models** (VLAs, world models, embodied reasoners), which finally gate **deployment** (factories, logistics, eventually homes). As of mid-2026 the stack is unevenly mature: locomotion is largely solved via sim-to-real RL, VLA architectures are converging, and 50,000+ humanoid shipments are forecast this year (TrendForce) — but the binding constraints have shifted to (1) real-world manipulation data at scale, (2) dexterous hands with human-grade tactile sensing, (3) reliability/uptime economics (batteries, MTBF, safety standards), and (4) evaluation, where saturated sim benchmarks mask a large open-world generalization gap between closed frontier models and open-weight ones.

## How to read this tree

- Each layer **depends on** the layers below it and **unlocks** the layers above it.
- "Bottleneck" = the constraint that most limits progress on that branch as of 2026-06, not necessarily the hardest long-term problem.
- Sibling deep-dives: [Hardware](hardware.md), [Data](data.md), [VLA models](vla-models.md), [World models](world-models.md), [Simulation](simulation.md), [Manipulation](manipulation.md), [Locomotion](locomotion.md), [Humanoid robots](humanoid-robots.md), [Open problems](open-problems.md).

## Layer 0 — Hardware: the physical substrate

- **Actuators**: joint actuators are >30% of BOM in high-spec humanoids with five-fingered hands, >50% in basic configs (Interact Analysis, as of 2025). Rotary/linear actuators with harmonic or planetary-roller-screw drives; low production volume of high-precision screws is a named scaling bottleneck. Actuators now *exceed* human muscle in power density, speed, and endurance — raw strength is no longer the constraint.
- **Dexterous hands**: the weakest hardware branch, and the single largest cost component — ~31% of humanoid BOM (Bank of America Institute, as of 2025-04). Example frontier part: Sharpa Wave tactile five-finger hands, 22 DoF, chosen for NVIDIA's 2026 reference humanoid. Human hands remain far ahead in resolution, robustness, and cost.
- **Tactile sensing**: 2026 lab results (Cambridge graphene/liquid-metal skin, ~200 µm pyramid taxels, detects sand-grain-scale contact, normal + shear force + slip) improve sensitivity/size roughly 10x over prior flexible sensors (as of 2026-03, single-source, unverified). Commercial offerings (XELA, GelSight-style optical) exist but are fragile and expensive; almost no fleet robot ships with dense skin today.
- **Compute (edge)**: NVIDIA Jetson AGX Thor T5000 — Blackwell GPU, 2,070 FP4 TFLOPS, 128 GB unified memory, 40–130 W, 7.5x Jetson Orin compute — is the de-facto onboard inference standard for 2026 humanoids, enough to run multi-billion-parameter VLAs locally. GA 2025-08-25, dev kit from $3,499; adopters at launch included Agility Robotics, Amazon Robotics, Boston Dynamics, Figure, Hexagon, and Meta, with 1X, OpenAI, and Physical Intelligence evaluating (as of 2025-08).
- **Energy**: Li-ion packs at ~250–350 Wh/kg give 1–4 h of active humanoid runtime (many units realistically 30–90 min between charges); reference points: Unitree H1 carries a 0.864 kWh pack, Tesla Optimus Gen 2 ~2.3 kWh (high-nickel NMC) for roughly 2 h of dynamic operation (TrendForce/CnEVPost, 2026-01). Industrial customers expect 95–99% uptime, so hot-swap batteries (Agility Digit, Apptronik Apollo) and charging choreography are stopgaps. Solid-state cells are the awaited unlock for full-shift (8 h) operation; TrendForce projects 74 GWh of humanoid solid-state demand by 2035 (as of 2026-01).
- **Platforms/cost**: Unitree sells humanoids at roughly an order of magnitude below US competitors (entry models from ~$4,290–$16k class, as of 2026) and self-reports 5,500+ humanoids shipped in 2025 (Unitree prospectus figure; Omdia independently counts ~4,200); commodity hardware is arriving faster than the intelligence to use it.
- **Unlocks**: everything above. Cheap reliable platforms (Layer 0) are precisely what turned learning research (Layer 3) from simulation-only into fleet-scale.

## Layer 1 — Perception

- **Status: largely riding the VLM wave.** Modern stacks use pre-trained vision(-language) backbones instead of bespoke detection pipelines; multi-view RGB + depth + proprioception is standard, e.g. reference-design stereo head cameras (140° H / 102° V).
- **Embodied reasoning models** now provide perception-as-a-service above raw vision: Gemini Robotics-ER 1.5 (2025-09, preview via Gemini API) does pointing, affordance-grounded 2D outputs, and multi-step planning; ER 1.6 (2026-04-14) adds multi-camera understanding, success detection, and instrument reading (93% success with agentic vision), claiming SOTA on 15 embodied-reasoning benchmarks for the 1.5 generation.
- **Remaining gaps**: contact-rich perception (force, slip, texture — depends on Layer 0 tactile), reliable success detection for autonomous data collection, and long-horizon spatial memory (Physical Intelligence's MEM, 2026-03, targets >10-minute tasks).
- **Unlocks**: perception quality directly gates manipulation under occlusion/clutter (Layer 2/3) and autolabelling of unstructured video into training data (Layer 3).

## Layer 2 — Control

- **Locomotion: effectively a solved research problem.** Sim-to-real RL with massive domain randomization is the standard recipe; FastTD3/FastSAC-style off-policy RL now trains deployable humanoid walking in ~15 minutes on one RTX 4090 with thousands of parallel envs (arXiv 2512.01996, demonstrated on Unitree G1 and Booster T1, as of late 2025). See [Locomotion](locomotion.md).
- **Whole-body control (WBC)**: latent-command interfaces let high-level policies drive full 30–75 DoF bodies; LeVERB (2025) showed first zero-shot sim-to-real whole-body control from vision-language input. Multi-simulator dynamics randomization (PolySim) further narrows the sim-to-real gap.
- **Manipulation control**: grasping of rigid known objects works; dexterous in-hand manipulation, tool use, deformables, and recovery-from-slip remain research-grade — bottlenecked jointly by hands/tactile (Layer 0) and data (Layer 3). See [Manipulation](manipulation.md).
- **Unlocks**: solved locomotion + WBC freed humanoid makers to compete on manipulation and autonomy; it also makes mobile manipulation (π0.5-style "clean an unseen kitchen") possible at all.

## Layer 3 — Learning: data engines and algorithms

- **The consensus bottleneck of the whole tree is here: data, not compute.** Robot policies need paired observation–action streams that do not exist at internet scale.
- **Teleoperation** is the gold standard but yields only ~5–50 episodes per operator-hour; parallelized sites reach ~200–500 demos/day. Frontier labs (Physical Intelligence, NVIDIA GR00T, Google DeepMind) target million-demonstration scale, where the constraint shifts to logistics: calibration, format consistency, QA across dozens of stations (as of 2026).
- **Aggregated datasets**: Open X-Embodiment — 1M+ episodes, 22+ robot types, 33 institutions — proved cross-embodiment transfer beats single-robot training, but the community concedes much of OXE is low-quality demonstration data with no agreed quality metric. DROID ~76k trajectories; RH20T 110k+ contact-rich sequences.
- **Force multipliers emerging in 2026**: policy-assisted teleop (partially trained policy does easy sub-tasks, human does hard parts — claimed 5–10x fewer human demos per task), autonomous collection with robot-assisted reset, human-video retargeting, and synthetic data from world models (Layer 4 feeding back down).
- **Synthetic data leverage, concretely**: NVIDIA GR00T N1 (2025-03, arXiv 2503.14734) used only 88 h of in-house humanoid teleop data (Fourier GR-1) at the "peak" of its data pyramid — augmented ~10x to 827 h with neurally generated video — plus 780k DexMimicGen/Isaac-Sim simulation trajectories (~6,500 h) generated in 11 hours; external real datasets (Open X-Embodiment subsets, 140k AgiBot-Alpha trajectories) were also in the mix. NVIDIA reports combining synthetic with real data improved performance ~40% over real data alone. Recent consensus holds that sim-to-real success depends more on training-data diversity than on simulation physics accuracy (unverified).
- **RL on real robots is back**: π*0.6 + RECAP (2025-11-17, arXiv 2511.14759) trains VLAs with advantage-conditioned RL over demonstrations, teleoperated corrections, and autonomous rollouts — on the hardest tasks it more than doubles throughput and roughly halves failure rate, running multi-hour uninterrupted espresso service, folding laundry in unseen homes, and assembling factory boxes; π's "RL token" work (2026-03-19) extracts fast online-RL interfaces from VLAs; DexPIE and similar 2026 papers do stable dexterous policy improvement from real-world experience.
- **Position-paper critique** (arXiv 2606.06556, 2026): the field is "policy-scaling-centric" when it should be "grounding-centric" — the missing machinery is data engines that autolabel unstructured behavior (internet video, wearables, deployment failures) into robot supervision, task-preserving retargeting, physics-grounded world models, and self-improving deployment loops.
- **Unlocks**: every foundation-model capability in Layer 4 is downstream of this layer's throughput.

## Layer 4 — Foundation models

### VLAs (vision-language-action)

- Field growth: VLA submissions at ICLR went 1 (2024) → 9 (2025) → **164 (2026)** — an 18x year-over-year jump.
- **Model line examples**: π0 (2024-10) → π0.5 open-world generalization (2025-04) → π0.6 +RL (2025-11) → π0.7 "steerable foundation model, step-change in generalization" (2026-04-16). Google: Gemini Robotics 1.5 (VLA) + Robotics-ER 1.5/1.6 (reasoner) split the stack into thinker/actor. NVIDIA: Isaac GR00T open models + Cosmos 3 world models (2026-05-31). China: LingBot-VLA (Ant Group, 2026-01), RDT-1B, ABot-M0. See [VLA models](vla-models.md) and [State of the art](state-of-the-art.md).
- **Architecture trend (as of ICLR 2026)**: shift from autoregressive token decoding to **discrete diffusion** action generation (parallel decoding of long action chunks); embodied chain-of-thought (subtasks, boxes, trajectories) for interpretability; better action tokenizers (FAST, RVQ/B-spline successors like FASTer, OMNISAT).
- **Benchmark saturation problem**: LIBERO at 95–98%, CALVIN >4.0 standard — sim benchmarks no longer discriminate. Real gap: open-weight VLAs match closed models in sim but clearly trail Gemini Robotics / π0.5-class closed models on novel objects, unseen scenes, paraphrased instructions.

### World models

- Genie 3 (DeepMind, 2025-08): real-time interactive 3D world generation at 24 fps; primary robotics use is generating diverse egocentric training environments and edge cases; still limited research preview (as of early 2026). Waymo adapted it into a driving world model (2026-02) (unverified).
- NVIDIA Cosmos 3 (technical report 2026-06, arXiv 2606.02800): omnimodal mixture-of-transformers unifying language, image, video, audio, and action in one architecture; open weights/code/datasets; claimed best policy model on RoboArena at release. Positions video world models as both synthetic-data generators and policy backbones ("Cosmos policy" fine-tuning for visuomotor control). Cosmos WFMs passed 2M downloads by 2026-01, trained on ~20M hours of real-world video (NVIDIA, as of 2026-01).
- World-model-based policy optimization (WMPO and successors) trains/evaluates VLAs inside learned simulators — the intended escape hatch from the real-world data bottleneck, if physics fidelity (contact, forces) can be trusted. See [World models](world-models.md).
- **Unlocks**: cheap policy evaluation (real-world trials are the scarcest resource of all — frontier labs win partly on fleet access) and possibly unlimited synthetic experience.

## Layer 5 — Deployment

- NVIDIA's Jensen Huang declared the "ChatGPT moment for Physical AI" at CES 2026. Counterpoint Research estimates **~16,000 humanoids installed globally in 2025** (>80% in China) and forecasts a **100,000+ installed base by 2027**; TrendForce separately forecasts **50,000+ humanoid shipments in 2026** (>700% YoY) (as of 2026-01). Earlier aggregator claims of "Counterpoint: 50k in commercial operation in 2026" conflate the two.
- **Flagship deployments (as of 2026-06)**: Figure (02/03) + Helix at BMW Spartanburg since 2024; BMW reports the Spartanburg pilot moved 90,000+ components with millimeter precision across 1,250 operating hours in 2025, supporting production of 30,000+ BMW X3s (BMW press, 2026-02-27). BMW's first humanoid in Germany is Hexagon Robotics' AEON at Plant Leipzig — initial tests 2025-12, pilot phase from summer 2026 on high-voltage battery assembly — alongside a new BMW "Center of Competence for Physical AI in Production" (BMW press, 2026-02); reports that Figure itself expanded to Leipzig in 2026-03 conflict with BMW's own announcement (unverified). Agility Robotics signed a RaaS agreement with Toyota Motor Manufacturing Canada (2026-02) (unverified). Figure's BotQ factory reportedly producing one robot per ~90 minutes (as of 2026-04, unverified). Tesla Optimus: Musk conceded on the 2026-01 Q4 call that Optimus is "not in usage in our factories in a material way"; Gen 3 production launch targeted for summer 2026 at an eventual $20k–$30k price (projection, unverified).
- **Capital and platforms (as of 2026-06)**: Figure — $1B+ Series C at $39B post-money (2025-09). Unitree — filed 2026-03-20 for a Shanghai STAR IPO raising ¥4.2B (~$608–610M); listing approval cleared 2026-06-01 after a record 73-day fast-track, target valuation ~$6.2B (Caixin, as of 2026-05); 2025 revenue ¥1.7B with humanoids at 51.5% of revenue. Agility Robotics — going public via ~$2.5B SPAC with ~$300M in pre-orders (2026-06), first US-listed pure-play humanoid. AgiBot — planned HK IPO at ~$5–6.4B. See [Investment](investment.md), [Landscape: China](landscape-china.md), [Organizations](organizations.md).
- **Research platform standardization**: NVIDIA Isaac GR00T Reference Humanoid (announced 2026-05-31/06-01, GTC Taipei): Unitree H2 Plus chassis (31 DoF, ~6 ft, 150 lb) + Sharpa Wave hands (22 DoF, 75 DoF total) + Jetson Thor T5000 + full Isaac stack (Teleop, GR00T models, Sim/Lab, ROS); available from Unitree late 2026; partners include Ai2, ETH Zurich, Stanford, UCSD.
- **Deployment gates**: uptime economics (batteries, MTBF), safety certification — ISO 10218:2025 and ANSI/A3 R15.06-2025 apply, but no finished standard yet exists for dynamically balancing humanoids (ISO 25785-1 in development) — plus insurance, and proving $/task versus human labor.

## Dependency map: what unlocks what

- Cheap actuators + edge compute (L0) → affordable research humanoids → **fleet-scale data collection** (L3)
- Tactile skin + better hands (L0) → contact-rich perception (L1) → **dexterous manipulation policies** (L2/L3) — currently blocked
- GPU-parallel simulation (Isaac Lab) → 15-minute sim-to-real RL → **solved locomotion/WBC** (L2) → mobile manipulation (L4)
- VLM pretraining (adjacent tree) → VLA backbones + embodied reasoners (L4) → language-tasked robots (L5)
- Teleop data engines (L3) → generalist VLAs (L4) → policy-assisted teleop → **cheaper data** (L3, self-reinforcing loop)
- World models (L4) → synthetic data + offline evaluation → relaxes both the data and the real-world-trials bottlenecks (L3)
- Deployment fleets (L5) → failure/correction data → self-improving loops (L3) — the flywheel every lab is chasing; mostly aspirational as of 2026

## Bottleneck per branch (as of 2026-06)

| Branch | Status | Current bottleneck | Plausible unlock |
|---|---|---|---|
| Actuators | Mature, cost-driven | Precision screw/reducer production volume; >30% of BOM | China supply-chain scale; Unitree-style pricing |
| Hands & touch | **Weakest link** | Dense, durable, cheap tactile skin; hand robustness | Graphene/liquid-metal skins; optical taxels at scale |
| Energy | Constraining ops | 1–4 h runtime vs 8 h shifts; 250–350 Wh/kg Li-ion | Solid-state cells; hot-swap logistics |
| Edge compute | Not a bottleneck | — (Jetson Thor: 2,070 FP4 TFLOPS, 128 GB) | — |
| Perception | Strong via VLMs | Contact/force perception; success detection | Tactile hardware + ER-class reasoners |
| Locomotion/WBC | Largely solved | Long-tail terrain, robustness certification | Multi-sim randomization; on-robot adaptation |
| Manipulation | Research-grade | Dexterity under uncertainty; deformables; recovery | Tactile + RL-from-real + better hands |
| Data | **THE bottleneck** | Teleop throughput (5–50 eps/op-hr); no quality metrics | Policy-assisted teleop; autolabelling video; world-model synthesis |
| VLAs | Rapid convergence | Zero-shot generalization gap; benchmark saturation | Discrete diffusion; embodied CoT; real-world evals |
| World models | Promising, immature | Physics fidelity (contact/forces) vs visual plausibility | Physics-grounded WMs; interactive-trace training |
| Deployment | Early commercial | Uptime, safety standards (no humanoid ISO yet), $/task | ISO 25785-1; battery swap; fleet learning |
| Evaluation | Underrated blocker | Sim benchmarks saturated; real trials scarce & manual | Real-to-sim eval (PolaRiS-style); standardized fleets |

## Cross-layer wildcards

- **Closed vs open gap**: closed frontier models (Gemini Robotics, π0.x) lead on open-world generalization largely via proprietary data fleets — data access, not architecture, is the moat (ICLR 2026 analysis).
- **China cost curve**: Chinese makers dominated 2025 unit shipments and sell at ~10x lower price points; if intelligence commoditizes via open GR00T-style stacks, hardware cost leadership may decide the market. See [Landscape: China](landscape-china.md).
- **In-context learning for robots** is nearly absent from current VLA research despite being the mechanism that made LLMs generally useful — a conspicuous open branch (as of ICLR 2026).
- **Self-improving deployment loops** (deployment data → autolabel → retrain) would collapse the L3 bottleneck; every major lab claims to be building one, none has published a convincing closed loop at scale (as of 2026-06).

## Sources

- https://nvidianews.nvidia.com/news/nvidia-open-humanoid-robot-reference-design — Isaac GR00T Reference Humanoid specs (H2 Plus, Sharpa hands, Jetson Thor T5000, 2,070 FP4 TFLOPS), late-2026 availability, partners
- https://www.pi.website/blog — Physical Intelligence release timeline: π0 (2024-10), π0.5 (2025-04), π0.6 +RL (2025-11), π0.7 (2026-04-16), MEM memory (2026-03), FAST tokenizer
- https://mbreuss.github.io/blog_post_iclr_26_vla.html — ICLR 2026 VLA analysis: 164 submissions, discrete-diffusion trend, LIBERO 95–98% saturation, open/closed generalization gap, data-quality critique
- https://deepmind.google/blog/gemini-robotics-er-1-6/ — Gemini Robotics-ER 1.6 (2026-04-14): multi-view, success detection, instrument reading 93%
- https://www.infoq.com/news/2025/09/deepmind-gemini-robotics/ — Gemini Robotics-ER 1.5 release, SOTA on 15 embodied benchmarks, API availability
- https://arxiv.org/html/2606.06556v1 — "Robots Need More Than VLAs & World Models": grounding-centric critique; OXE 1M+/22 embodiments, DROID ~76k, RH20T 110k+
- https://arxiv.org/pdf/2512.01996 — FastTD3/FastSAC: sim-to-real humanoid locomotion trained in ~15 min on one RTX 4090 (Unitree G1, Booster T1)
- https://people.eecs.berkeley.edu/~sastry/pubs/Pdfs%20of%202025/XueLeVERB2025.pdf — LeVERB: first zero-shot sim-to-real vision-language whole-body control
- https://interactanalysis.com/insight/joint-actuators-the-fundamental-component-for-humanoid-robots-power-and-dexterity/ — actuators >30% (up to >50%) of humanoid BOM
- https://claru.ai/training-data/teleoperation — teleop throughput 5–50 episodes/operator-hour; million-demo targets; logistics bottleneck
- https://www.shaip.com/blog/robot-training-data-strategy/ — teleop vs sim vs human-video data strategy; policy-assisted teleop 5–10x claim
- https://techxplore.com/news/2026-03-graphene-based-artificial-skin-human.html — Cambridge graphene/liquid-metal tactile skin, ~10x sensitivity/size improvement (2026-03)
- https://www.labellerr.com/blog/genie-3-google-deepmind-world-model/ — Genie 3 (2025-08): interactive world model, egocentric robot-training data use case
- https://www.vaasblock.com/news/humanoid-robotics-figure-tesla-optimus-commercial-reality-2026/ — Figure 03/Helix at BMW Spartanburg; Optimus "not material" per 2026-01 earnings call (aggregator; its Figure-Leipzig and "Counterpoint 50k in operation 2026" claims are contradicted by BMW's and Counterpoint's own publications)
- https://counterpointresearch.com/en/insights/Global-Humanoid-Robot-Installations-Reach-16,000-Units-in-2025-as-Mass-Production-Picks-Pace — Counterpoint primary: ~16,000 humanoids installed in 2025 (>80% China), 100,000+ installed base forecast by 2027
- https://techmarketbriefs.com/pre-ipo/figure-ai/ — Figure $1B+ Series C at $39B post-money (2025-09); BotQ production rate
- https://restofworld.org/2026/unitree-china-humanoid-robot-shanghai-ipo/ — Unitree IPO filing 2026-03-20, ¥4.2B (~$610M) raise
- https://www.caixinglobal.com/2026-05-26/unitree-fast-tracks-shanghai-ipo-with-target-valuation-of-62-billion-102447449.html — Unitree fast-track approval, ~$6.2B target valuation, 5,500 humanoids shipped 2025, 2025 financials
- https://kraneshares.com/a-complete-guide-to-unitree-robotics-2026-ipo-why-it-matters-for-star-market-etf-kstr-humanoid-robotics-etf-koid/ — Unitree 5,500+ humanoids shipped 2025, valuation targets, China unit dominance
- https://autonews.gasgoo.com/articles/market-industry/annual-champion-changes-hands-unitree-announces-over-5500-humanoid-robot-shipments-2014711162140991489 — Unitree prospectus 5,500+ "pure humanoids" vs Omdia's ~4,200 count (AgiBot ~5,100); classification/methodology dispute
- https://www.forbes.com/sites/johnkoetsier/2026/06/24/first-humanoid-robot-maker-goes-public-in-us-25-billion-deal-new-robot-300-million-in-pre-orders/ — Agility Robotics $2.5B SPAC, $300M pre-orders (2026-06)
- https://techcrunch.com/2026/06/24/agility-robotics-plans-to-go-public-via-spac-in-a-2-5b-deal/ — Agility SPAC corroboration: Churchill Capital Corp XI, ~$620M proceeds, ticker AGLT
- https://theresarobotforthat.com/blog/humanoid-robot-safety-standards-2026/ — ISO 10218:2025, ANSI/A3 R15.06-2025, ISO 25785-1 in development for dynamically stable robots
- https://stdbattery.com/blog/detail/2026-humanoid-robot-market-status-outlook-lithium-battery-pack-core-specifications — Li-ion 250–350 Wh/kg, 1–4 h runtime constraints
- https://www.marktechpost.com/2026/01/29/ant-group-releases-lingbot-vla-a-vision-language-action-foundation-model-for-real-world-robot-manipulation/ — LingBot-VLA (Ant Group, 2026-01)
- https://www.buildfastwithai.com/blogs/nvidia-cosmos-3-isaac-groot-physical-ai-2026 — Cosmos 3 release timing (2026-05-31) alongside GR00T reference robot
- https://arxiv.org/abs/2511.14759 — π*0.6/RECAP paper: advantage-conditioned RL, >2x throughput and ~½ failure rate on hardest tasks, espresso/laundry/box-assembly results
- https://arxiv.org/abs/2606.02800 — Cosmos 3 technical report: omnimodal mixture-of-transformers, open release, RoboArena policy claim
- https://developer.nvidia.com/blog/scale-synthetic-data-and-physical-ai-reasoning-with-nvidia-cosmos-world-foundation-models/ — Cosmos WFM scale: 2M+ downloads, ~20M hours of training video (as of 2026-01)
- https://nvidianews.nvidia.com/news/nvidia-blackwell-powered-jetson-thor-now-available-accelerating-the-age-of-general-robotics — Jetson Thor GA 2025-08-25, $3,499 dev kit, 7.5x Orin, launch adopter list
- https://www.press.bmwgroup.com/global/article/detail/T0455864EN/bmw-group-to-deploy-humanoid-robots-in-production-in-germany-for-the-first-time?language=en — BMW primary source: Leipzig AEON (Hexagon) timeline, Spartanburg 90k+ components / 1,250 operating hours, Physical AI competence center
- https://arxiv.org/abs/2503.14734 — GR00T N1 paper: 88 h in-house GR-1 teleop data augmented ~10x to 827 h neural video; OXE subsets + 140k AgiBot-Alpha real trajectories also in training mix; 780k DexMimicGen sim trajectories
- https://nvidianews.nvidia.com/news/nvidia-isaac-gr00t-n1-open-humanoid-robot-foundation-model-simulation-frameworks — 780k synthetic trajectories (~6,500 h) generated in 11 h; +40% over real-only data
- https://blog.pebblous.ai/project/AgenticAI/isaac-groot/en/ — GR00T N1 data-mix explainer (secondary)
- https://institute.bankofamerica.com/content/dam/transformation/humanoid-robots.pdf — dexterous hands ~31% of humanoid BOM, largest single component
- https://www.trendforce.com/presscenter/news/20260128-12902.html — humanoid battery runtimes (<2 kWh, 2–4 h), 74 GWh solid-state demand forecast by 2035, 50k+ 2026 shipment forecast
- https://cnevpost.com/2026/01/28/demand-for-solid-state-batteries-humanoid-robots-74-gwh-2035/ — corroborates H1 0.864 kWh and Optimus Gen 2 2.3 kWh (~2 h dynamic) reference points
- https://arxiv.org/abs/2510.03342 — Gemini Robotics 1.5: thinker/actor split, embodied reasoning, motion transfer across embodiments
