---
title: Dexterous Manipulation
slug: manipulation
updated: 2026-07-03
confidence: verified
---
> Dexterous manipulation — using end-effectors to grasp, reorient, and control objects, including deformables and tools — is the central bottleneck of Physical AI: locomotion is largely solved, manipulation is not. The field's dominant recipe shifted (2023–2026) from task-specific control to large-scale imitation learning (ALOHA/ACT, Diffusion Policy, UMI) absorbed into [VLA foundation models](vla-models.md), with real-world RL fine-tuning (π*0.6/RECAP, 2025-11) re-emerging to push reliability. Hardware is bifurcated: cheap parallel-jaw grippers still power most deployed systems and most training data, while multi-fingered hands (20+ DoF, tactile skins) entered mass production in China in 2025 (30k+ units shipped). Flagship capabilities as of 2026-07 — laundry folding, box assembly, dishwasher loading, all-day espresso making — remain slow and error-prone versus humans; in-hand reorientation of arbitrary objects, forceful tool use, and standardized evaluation remain open.

## Why manipulation is the hard part

- Moravec's paradox in practice: contact-rich physics (friction, compliance, intermittent contact) is far harder to model, simulate, and learn than free-space motion or [locomotion](locomotion.md).
- Contact dynamics are discontinuous and chaotic — tiny pose errors flip grasp outcomes; simulators handle rigid-body contact poorly and deformables (cloth, cables, food) worse, limiting the sim-to-real route that solved walking (see [Simulation](simulation.md)).
- Perception is occluded exactly where it matters: the hand covers the object at the moment of contact, motivating tactile sensing.
- Data scarcity: there is no manipulation-scale internet corpus; every paradigm below is ultimately a strategy for acquiring action-labeled contact data cheaply (see [Data](data.md)).
- Long-horizon compounding: household/industrial tasks chain dozens of contact events; per-step success rates of 95% still yield frequent task failures, which is why throughput (successes/hour) is replacing single-attempt success rate as the metric that matters (π0.6 model card, 2025-11).

## End-effectors: grippers vs dexterous hands

| Type | DoF (typ.) | Cost (typ., as of 2026) | Strengths | Weaknesses | Examples |
|---|---|---|---|---|---|
| Parallel-jaw gripper | 1 | $100s–$5k | Cheap, robust, easy to model, dominant in datasets | No in-hand reorientation; weak on small/flat/deformable-precise tasks | Robotiq 2F-85, WSG-50, UMI gripper, Franka hand |
| Suction / hybrid | 1–2 | $100s–$5k | Flat surfaces, logistics picking | Porous/irregular objects fail; no dexterity | Warehouse pickers (see [State of the art](state-of-the-art.md)) |
| Underactuated 2–3 finger | 3–11 | $5k–$20k | Adaptive power grasps, tolerant to error | Limited precision manipulation | Robotiq 3F, Shadow DEX-EE (3-finger, DeepMind collab) |
| Anthropomorphic multi-finger | 16–24+ | ~$3k (China volume) to $100k+ (Shadow) | In-hand reorientation, tool use, human-tool compatibility, teleop-friendly | Fragile, expensive at high end, control/data hungry | Shadow Hand (24 joints), Tesla Optimus Gen-3 (22 DoF), Unitree Dex5-1 (20 DoF), Inspire RH56, DexRobot DexHand021 |

- The pragmatist case (bimanual parallel jaws suffice for most tasks; human tools can be power-grasped without five fingers) is argued explicitly in "The Case Against Human Hands" and reflected in practice: ALOHA, UMI, π0's laundry demos, and most warehouse deployments use simple grippers.
- The maximalist case: pinch grasps on small objects, in-hand regrasping, assembly, and handwriting-class precision need multi-finger hands; every major [humanoid program](humanoid-robots.md) (Tesla, Figure, Sanctuary, Apptronik, Chinese OEMs) is now betting on them.
- Tesla Optimus Gen-3 hand: 22 DoF hand + 3 DoF wrist, tendon-driven from forearm-housed actuators (patent-based analyses count ~25 actuators per forearm rather than full per-DoF actuation (secondary sources, unverified)), tactile fingertips; shown playing catch and handling eggs in 2025 demos — several flagged by press as teleoperated.
- Shadow Hand remains the DoF reference (24 joints, ~20 actuated, tendon-driven, used in OpenAI's Dactyl 2018–2019 in-hand cube/Rubik's work); its DEX-EE 3-finger hand (2023, with Google DeepMind) traded anthropomorphism for robustness under RL-scale wear.
- China mass-production wave (per Gasgoo industry reporting, single source): known dexterous-hand shipments >30,000 units in 2025 — a figure Gasgoo derives by assuming two hands per robot shipped; Inspire Robots delivered ~10,000 hands in 2025 (vs ~2,000 in 2024); Unitree's humanoid-robot shipments topped 5,500 units but hand-only figures are not broken out; LinkerBot targets 50,000–100,000 units in 2026 (unverified). See [Landscape: China](landscape-china.md).
- DexRobot DexHand021 Pro (shown at CES 2026-01; full hand series + DexTele teleop system unveiled at Automate 2026-06): 22 DoF (wrist-hand integrated, dual-tendon drive), 50 N payload, full-palm multi-modal sensing, >300k durability cycles, ~$14k–28k — claimed ~1/5 the cost of comparable hands (company PR, unverified).
- TESOLLO DG-5F (Korea): 20 DoF five-finger hand aimed at the humanoid market (as of 2025).
- Cross-embodiment problem: policies trained on one hand transfer poorly to another; grippers vs hands also splits the data ecosystem (most open datasets are parallel-jaw). See [Open problems](open-problems.md).

## Tactile sensing

- Why touch: resolves occlusion at contact, enables slip detection, force-limited grasping (eggs, glass), texture/material ID, and contact-rich insertion that vision alone misses.
- Vision-based tactile (camera watches deformable gel): the GelSight family dominates research — micron-level surface resolution; 2024–2025 variants include GelBelt (large surfaces), ThinTact (lensless), DTactive (active surface), and modularized open designs (Yuan lab, IJRR 2025).
- Meta AI × GelSight Digit 360 (announced 2024-10): fingertip-shaped sensor, ~8.3M taxels, omnidirectional touch, detects forces down to ~1 mN, 18+ sensing modalities, on-device processing; positioned as the open research standard.
- Magnetic/piezo array skins are winning on hands because they are thin and cheap: Unitree Dex5-1 ships 94 touch points per hand (as of 2025); Tesla added fingertip force sensing in Optimus Gen-3.
- Tacta (CES 2026, company claims, unverified): 361 sensels/cm² at 1 kHz in a 4.5 mm module; first full-hand coverage demo with 1,956 sensels across fingertips, pads, and palm.
- Policy integration is early but accelerating: tactile-conditioned diffusion policies (PolyTouch, 2025), tactile-language-action models (TLA, 2025), VLA-Touch (dual-level tactile feedback for VLAs, 2025), AnyTouch (unified representation across visuo-tactile sensors, 2025). No frontier VLA yet ships with tactile input as a first-class modality (as of 2026-07) — a gap repeatedly cited because tactile data is absent from human video and most teleop datasets.

## Imitation learning lineage: ALOHA/ACT → Diffusion Policy → UMI → VLAs

The 2023–2024 imitation-learning wave is the direct ancestor of today's [VLA models](vla-models.md); see also [History](history.md).

| Year | System | Contribution |
|---|---|---|
| 2023-04 | **ALOHA + ACT** (Zhao, Finn et al., Stanford) | ~$20k open-source bimanual teleop rig; Action Chunking with Transformers (CVAE, predicts action sequences not single steps) hits 80–90% on fine tasks from ~50 demos |
| 2023 (RSS) | **Diffusion Policy** (Chi, Song et al., Columbia/TRI) | Denoising diffusion over action trajectories; handles multimodal demonstrations; ~47% average improvement over prior BC baselines; became the default policy class |
| 2024-01 | **Mobile ALOHA** (Fu, Zhao, Finn) | Whole-body bimanual mobile teleop (~$32k); co-training with static ALOHA data boosts ACT/Diffusion/VINN — early cross-task data-pooling evidence |
| 2024-02 | **UMI** (Chi, Song et al.) | Hand-held gripper with GoPro + fisheye + mirrors: in-the-wild human data collection without robots; policies transfer to arms for dynamic and bimanual tasks |
| 2024 | **ALOHA 2** (DeepMind) | Ruggedized, more capable ALOHA platform (plus MuJoCo sim model); became DeepMind's bimanual data-collection workhorse |
| 2024-10 | **ALOHA Unleashed** (DeepMind) | "Simple recipe" — >26,000 teleop demos across 5 tasks + diffusion policy — masters shirt hanging, shoe-lace tying, gear insertion; showed dexterity is data-bound, not algorithm-bound |
| 2024-10 | **π0** (Physical Intelligence) | Flow-matching VLA; absorbed the IL lineage into a foundation model; laundry folding, table bussing across embodiments |
| 2025 | **UMI derivatives** | FastUMI (FastUMI-100K: >100k episodes, 54 tasks), DexUMI (CoRL 2025: hand exoskeleton + robot-hand inpainting → 86% avg success on XHand/Inspire), ActiveUMI, UMI-on-Legs/Air |
| 2025-11 | **π*0.6 / RECAP** (Physical Intelligence) | RL from real-world experience on top of IL: advantage-conditioned policies + teleop corrections; ~2× throughput, ~½ failure rate on hardest tasks |

- Key conceptual moves: (1) action chunking beats per-step prediction for smooth contact-rich control; (2) generative policies (diffusion/flow) capture multimodal human demonstrations; (3) data collection interfaces (ALOHA teleop, UMI handhelds, exoskeletons) matter as much as architectures; (4) human video and handheld devices decouple data from expensive robots.
- The lineage converged into VLAs: Gemini Robotics (2025-03, Gemini 2.0-based) does origami folds and Ziploc packing on ALOHA 2 rigs, transferring to Franka bi-arm and Apptronik Apollo; Figure's Helix runs the same trunk for logistics and laundry. See [VLA models](vla-models.md), [Key people](key-people.md) (Zhao, Chi, Song, Finn, Levine, Hausman).
- RL's return: after OpenAI's Dactyl (2018–19, sim-to-real in-hand cube RL) the field went quiet on real-world RL; 2025 revived it — π*0.6/RECAP, Honda RL-for-dexterity patent filings (2025-02), and mixture-of-experts in-hand reorientation (DexReMoE) plus tactile sim-to-real distillation (PTLD, 2026) (single-source each).

## Bimanual systems

- Two arms are the practical floor for household tasks: cloth flattening, box assembly, and tool-plus-workpiece tasks all require a stabilizing hand plus an acting hand (research line: VoxAct-B, EquiBim, one-shot bimanual from video).
- Research platforms: ALOHA 2 (ViperX arms), bimanual Franka FR3, UR5e pairs (π0), SO-ARM101 (low-cost, used in LeHome 2026 challenge).
- Humanoid milestones (as of 2026-07): Figure Helix folded laundry autonomously with multi-fingered hands (2025-08, first claimed end-to-end neural humanoid laundry folding); Figure's Helix 02 completed a ~4-minute, 61-action dishwasher load/unload with no resets or teleop, integrating walking + manipulation (unedited video released 2026-01-28; Figure claims longest-horizon autonomous humanoid task to date); Apptronik Apollo runs Gemini Robotics checkpoints. See [Humanoid robots](humanoid-robots.md).
- π*0.6 deployments (2025-11, company-reported): espresso machine operation 5:30am–11:30pm runs; folding 50 distinct novel garments in a new environment; assembling + labeling 59 chocolate boxes in a factory setting.
- Data note: bimanual + multi-finger data is the scarcest tier of the [data pyramid](data.md); teleop cost scales with DoF, which is why UMI-style handhelds and exoskeletons (DexUMI, DexTele) are proliferating.

## Capability frontier and benchmarks (as of 2026-07)

**Demonstrated (reliably, in at least one lab/company setting):**
- Laundry/garment folding from a basket — π0.6 does this out-of-the-box (no task fine-tuning), ~60%+ success with ~19 successes/hour (model card, 2025-11); Helix on towels/laundry.
- Table bussing, dish loading, shirt hanging, shoe-lace tying, gear insertion, box assembly (π0.6 out-of-box box assembly only ~20% success — fine-tuning still needed for hard tasks).
- In-hand reorientation of varied rigid objects in lab settings (RL, e.g. DexReMoE mixture-of-experts, sim-to-real).
- Multi-hour unattended operation with RL-tuned VLAs (π*0.6 espresso), at throughput well below human baseline.

**Benchmarks and their problems:**

| Benchmark | Type | Status |
|---|---|---|
| LIBERO (+ LIBERO-Plus) | Sim, 4 generalization suites | De-facto VLA standard; near-saturated, LIBERO-Plus adds 7-factor perturbations to restore headroom |
| SIMPLER | Real-to-sim eval of real-robot policies | Standard for RT/π-class policy comparison |
| RobotArena ∞ / RoboArena | Real-to-sim + human preferences | Largest cross-lab VLA comparison to date (2025–26) |
| ICRA Cloth Competition (2024) | Real, cloth unfolding grasp selection | Deformable-object reference dataset |
| LeHome Challenge (2026) | Sim, bimanual garment folding on SO-ARM101 | Community deformables benchmark |

- Evaluation crisis: real-world results are mostly self-reported company demos with non-comparable setups; success-rate-per-attempt hides speed and recovery, hence the shift to throughput (successes/hour) and long-run autonomy metrics. Independent replication (e.g., Penn "π0 in the wild" study) finds generalist policies markedly weaker outside their training distributions.

## What remains hard, and why

- **In-hand manipulation of arbitrary objects**: regrasping, finger-gaiting, and tool reorientation generalize poorly beyond trained object sets; contact simulation error and tactile data scarcity are the binding constraints.
- **Forceful + delicate tool use**: tasks coupling high force with precision (peeling, cutting, fastening, connector insertion at scale) sit outside current demo classes.
- **Deformables beyond flat folding**: cable routing, dressing assistance, food manipulation — state estimation for high-DoF deformables remains unsolved.
- **Reliability, not existence proofs**: frontier demos succeed at 60–90% per attempt and run 3–10× slower than humans; industrial adoption needs 99%+ with graceful recovery. RL-from-experience (RECAP) is the current best lever.
- **Tactile-policy integration**: sensors exist (Digit 360, gel skins) but frontier VLAs are still vision-proprioception only; no large tactile-labeled dataset exists (as of 2026-07).
- **Cross-embodiment transfer to hands**: gripper-centric datasets (Open X-Embodiment, DROID) don't transfer to 20-DoF hands; exoskeleton/inpainting pipelines (DexUMI) are early workarounds.
- **Hand hardware economics**: high-DoF hands remain the least durable, most expensive subsystem of a humanoid; Chinese volume manufacturing (2025–26) is compressing cost but durability under continuous contact (>300k-cycle claims) is largely unaudited (unverified). See [Hardware](hardware.md), [Investment](investment.md).
- **Sim-to-real for contact**: [world models](world-models.md) and GPU simulators still mis-model friction, compliance, and deformables; most manipulation progress since 2023 came from real data, not sim — the reverse of locomotion.

## Sources

- https://arxiv.org/abs/2410.13126 — ALOHA Unleashed: scale + diffusion recipe, 5 dexterous bimanual tasks (DeepMind, 2024-10).
- https://mobile-aloha.github.io/resources/mobile-aloha.pdf — Mobile ALOHA paper: whole-body teleop, co-training gains for ACT/Diffusion/VINN.
- https://arxiv.org/abs/2402.10329 — Universal Manipulation Interface (UMI): in-the-wild handheld-gripper data collection.
- https://dex-umi.github.io/ — DexUMI (CoRL 2025): hand exoskeleton + inpainting, 86% avg success on XHand/Inspire hands.
- https://arxiv.org/html/2606.04708 — VISTA: UMI-data adaptation for VLA training; surveys FastUMI-100K (>100k episodes, 54 tasks) and UMI variant ecosystem.
- https://website.pi-asset.com/pi06star/PI06_model_card.pdf — π0.6 model card (2025-11-17): architecture, out-of-box laundry/box-assembly results, throughput metrics.
- https://www.pi.website/blog/pistar06 and https://arxiv.org/abs/2511.14759 — π*0.6/RECAP: RL from experience, espresso/laundry/box-factory runs, 2× throughput claim.
- https://deepmind.google/blog/gemini-robotics-brings-ai-into-the-physical-world/ — Gemini Robotics (2025-03): origami-class dexterity, ALOHA 2 → Apollo transfer.
- https://www.figure.ai/news/helix-learns-to-fold-laundry — Figure Helix laundry folding with multi-fingered hands (2025-08-12).
- https://www.figure.ai/news/helix-loads-the-dishwasher — Figure primary post: Helix 02 dishwasher load/unload, 61 actions, no resets (2026-01).
- https://the-decoder.com/figure-ai-shows-robot-that-really-puts-its-hip-into-dishwasher-duty/ — independent coverage confirming the ~4-minute unedited Helix 02 dishwasher video.
- https://www.basenor.com/blogs/news/tesla-optimus-gen-3-hands-22-dof-50-actuators-explained — Optimus Gen-3 hand: 22 DoF + 3 wrist, tendon-driven, fingertip tactile (secondary source).
- https://www.teslarati.com/tesla-optimus-v3-hand-arm-details-revealed-new-patents/ — Optimus V3 hand/arm patents: forearm-housed actuators, tendon drive (secondary source).
- https://vedder.io/misc/the_case_against_human_hands.html — the gripper-suffices argument in the hands-vs-grippers debate.
- https://www.therobotreport.com/tesollo-unveils-dexterous-robot-hand-for-humanoids/ — TESOLLO DG-5F 20-DoF hand.
- https://www.prnewswire.com/news-releases/dexrobot-unveils-full-dexterous-hand-series-and-new-dextele-teleoperation-system-at-automate-2026-302808579.html — DexHand021 Pro specs (22 DoF, 50 N, 300k cycles) and DexTele teleop (company PR).
- https://autonews.gasgoo.com/articles/news/from-prototypes-to-production-dexterous-hands-kick-off-a-mass-production-race-2016425582734970881 — China dexterous-hand shipments 2025 (>30k units derived at two hands/robot; Inspire ~10k vs ~2k in 2024; LinkerBot 2026 targets; Unitree figure in the article is humanoid units, not hands).
- https://www.unitree.com/mobile/Dex5-1/ — Unitree Dex5-1: 20 DoF (16 active), 94 tactile points.
- https://www.businesswire.com/news/home/20241031980322/en/GelSight-and-Meta-AI-Introduce-Digit-360-Tactile-Sensor — Digit 360: ~8.3M taxels, ~1 mN sensitivity, 18+ sensing features.
- https://finance.yahoo.com/news/fingertips-full-body-coverage-ensuring-090900110.html — Tacta full-hand tactile coverage at CES 2026 (company claims).
- https://github.com/linchangyi1/Awesome-Touch — curated index of tactile sensors and tactile-policy papers (PolyTouch, TLA, AnyTouch, VLA-Touch).
- https://arxiv.org/pdf/2508.01695 — DexReMoE: mixture-of-experts RL for general in-hand reorientation.
- https://arxiv.org/abs/1808.00177 — OpenAI Dactyl: RL in-hand cube reorientation lineage.
- https://openreview.net/attachment?id=OutljIofvS&name=pdf — RobotArena ∞: scalable real-to-sim VLA benchmarking.
- https://arxiv.org/pdf/2508.16749 — ICRA 2024 Cloth Competition dataset/benchmark for cloth unfolding.
- https://arxiv.org/pdf/2606.27163 — LeHome Challenge 2026: bimanual garment folding benchmark on SO-ARM101.
- https://penn-pal-lab.github.io/Pi0-Experiment-in-the-Wild/ — independent evaluation of π0 generalization gaps.
