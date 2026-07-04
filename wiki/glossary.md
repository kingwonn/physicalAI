---
title: Glossary
slug: glossary
updated: 2026-07-04
confidence: verified
---
> Definitional glossary of ~35 core Physical AI terms — models and architectures (VLA, world model, dual-system), learning methods (imitation vs RL, diffusion policy, flow matching), data machinery (teleoperation, UMI, data flywheel, Open X-Embodiment), hardware (QDD, harmonic drive, roller screw, tactile sensing), control theory (ZMP, MPC, whole-body control), and business shorthand (RaaS, BOM). Each entry is 1–3 sentences with a cross-link to the wiki page that covers it in depth. Alphabetical; letter-range sections.

## A–C

- **ACT (Action Chunking with Transformers)** — Imitation-learning policy (Zhao et al., 2023, arXiv:2304.13705) that trains a transformer as the decoder of a conditional VAE to predict *chunks* of future actions instead of single steps, cutting compounding error; with the ALOHA rig it reached 80–90% success on fine bimanual tasks from ~10 minutes of demonstrations. A foundational recipe behind modern [manipulation](manipulation.md) learning and most [VLA](vla-models.md) action heads.
- **Action tokenization** — Converting continuous robot actions into discrete tokens so a language-model backbone can emit them like text. Ranges from naive per-dimension binning (RT-2) to compression-based tokenizers such as Physical Intelligence's FAST, which applies a discrete cosine transform to action chunks and quantizes the coefficients, yielding far shorter sequences (~5× faster training, company-reported). See [VLA models](vla-models.md).
- **ALOHA** — "A Low-cost Open-source Hardware" bimanual teleoperation rig (~$20k, leader–follower arms; Zhao et al., 2023) that made high-quality two-handed demonstration collection affordable; successors include ALOHA 2 and Mobile ALOHA. The de facto academic standard teleop platform — see [manipulation](manipulation.md) and [data](data.md).
- **BOM (bill of materials)** — The summed cost of every component in a robot; the key input for arguing humanoid price floors and margins. Actuators (see QDD, harmonic drive, planetary roller screw below) and dexterous hands dominate humanoid BOMs; Chinese supply chains are the main force pushing them down — see [hardware](hardware.md) and [investment](investment.md).
- **Cost of transport (CoT)** — Dimensionless locomotion-efficiency metric: CoT = P / (m·g·v) (power over weight times speed); lower is better, and it lets robots be compared directly to animals and vehicles. Human walking is ≈0.2 — the canonical robotics reference value (Collins et al., Science 2005), with gross-metabolic estimates running closer to ≈0.3 — while ASIMO-era powered humanoids measured ≈3.2, an order of magnitude worse. Learned gaits have since undercut model-based control on efficiency: Hwangbo et al. (Science Robotics 2019) reported an RL-trained ANYmal policy using less mechanical power (78.1 vs 97.3 W) and 23–36% less torque than the model-based baseline at matched speeds, and a 2025 FITEE study reports a learned multigait quadruped policy averaging CoT ≈0.43 across feasible velocity commands — see [locomotion](locomotion.md) for details and the caveats on inconsistent CoT reporting.
- **Cross-embodiment** — Training a single policy on data from many different robot bodies (arms, bimanual rigs, quadrupeds, humanoids), and/or transferring skills across bodies. Landmark evidence: Open X-Embodiment's RT-1-X outperformed the per-robot specialist models on their own data by ~50% on average in smaller-data domains, and RT-2-X tripled RT-2's success on emergent-skill evaluations. See [VLA models](vla-models.md) and [data](data.md).

## D–F

- **Data flywheel** — The self-reinforcing loop where deployed robots generate interaction data → data improves the model → better model wins more deployment → more data. Popularized by Tesla's FSD program; now the explicit strategy of most humanoid and VLA companies. See [data](data.md).
- **Data foundry** — An organization or operation that produces robot training data as a product: teleoperation farms, staged real-world environments, egocentric human-video collection, and synthetic-data pipelines (vendors as of 2026 include Scale AI, micro1, and many Chinese collection centers; NVIDIA's "Physical AI Data Factory" blueprint is the simulation-heavy variant). See [data](data.md).
- **Dexterous hand DoF** — Degrees of freedom: the number of independent joints in a robot hand (the human hand has ~21+). Reference points as of 2026: Shadow Hand 24 joints (~20 actuated), Tesla Optimus Gen-3 hand 22 DoF, Chinese volume hands 16–22 DoF at ~$3k–$28k; note joint DoF ≠ actuated DoF — many hands are underactuated (tendon-coupled). See [manipulation](manipulation.md).
- **Diffusion policy** — Representing a visuomotor policy as a conditional denoising diffusion process over action sequences (Chi et al., RSS 2023): the model iteratively refines noise into an action trajectory conditioned on observations, gracefully capturing multimodal demonstrations. Widely used as the action head of VLAs — see [manipulation](manipulation.md) and [VLA models](vla-models.md).
- **Domain randomization** — Randomizing simulator parameters (textures, lighting, friction, masses, latencies) during training so the real world looks like just another sample from the training distribution (Tobin et al., 2017, arXiv:1703.06907). The standard cheap weapon against the sim2real gap — see [simulation](simulation.md).
- **Dual-system VLA (System 1 / System 2)** — VLA architecture splitting a slow, large vision-language reasoner ("System 2", ~7–10 Hz: scene understanding, task planning) from a fast, small visuomotor policy ("System 1", ~100–200 Hz: reactive motor control), borrowing Kahneman's fast/slow-thinking terminology. Canonical examples: Figure Helix (7–9 Hz VLM / 200 Hz policy) and NVIDIA GR00T N1 (10 Hz VLM / 120 Hz diffusion action head). See [VLA models](vla-models.md).
- **Embodied AI** — The older academic term (1990s embodied-cognition lineage) for intelligence that has and depends on a physical body; in current usage a near-synonym of Physical AI, with "embodied" the research framing and "Physical AI" the industry framing. See [history](history.md).
- **Embodied scaling laws** — The (partially demonstrated) hypothesis that robot-policy performance improves as a power law with training scale, where the axes that matter are environment/object *diversity* and number of *embodiments*, not just raw hours: data-scaling studies in imitation learning found near-power-law generalization gains (arXiv:2410.18647), and locomotion policies trained on ~1,000 procedurally generated bodies generalized to unseen ones (arXiv:2505.05753). Generalist's GEN-0 claims smooth scaling on 270k+ hours of manipulation data (company-reported, unverified). See [open problems](open-problems.md) and [data](data.md).
- **Flow matching** — A continuous-time generative-modeling technique (learning a velocity field that transports noise to data) used instead of diffusion for action generation; fewer integration steps make it fast enough for real-time control. π0's flow-matching "action expert" emits action chunks at up to 50 Hz. See [VLA models](vla-models.md).

## G–I

- **GPU-parallel simulation** — Running physics entirely on the GPU so thousands of environment instances step in parallel on one card (NVIDIA Isaac Gym 2021 → Isaac Lab; also MJX, Genesis), a 2–3 order-of-magnitude wall-clock speedup over CPU farms. This is what made massively parallel RL for legged locomotion routine — see [simulation](simulation.md).
- **Harmonic drive (strain-wave gear)** — Compact gear using a flexing "flexspline" to achieve very high reduction (commonly 30:1–320:1) in a single near-zero-backlash stage; the standard reducer in industrial-arm and humanoid rotary joints, but poorly backdrivable and torque must usually be sensed rather than inferred. Contrast QDD. See [hardware](hardware.md).
- **Imitation learning (IL)** — Learning a policy from demonstrations (simplest form: behavior cloning, i.e., supervised learning on observation→action pairs). Dominant recipe for manipulation since 2023 (ACT, diffusion policy, VLA pretraining); contrast reinforcement learning, which learns from reward instead of demonstrations. See [manipulation](manipulation.md).

## M–P

- **MPC (model predictive control)** — Control by repeatedly solving a finite-horizon optimal-control problem online at every timestep and executing only the first action ("receding horizon"). Workhorse of dynamic legged control (Boston Dynamics' parkour-era Atlas) and increasingly hybridized with learned policies. See [locomotion](locomotion.md).
- **Open X-Embodiment (OXE)** — The landmark cross-embodiment dataset and collaboration (a Google DeepMind–led effort spanning 21 institutions, 2023): 60 pooled datasets from 34 labs, 22 robot embodiments, 1M+ real trajectories in a common format, plus RT-X models demonstrating positive transfer across robots. The default pretraining corpus for open VLAs — see [data](data.md).
- **Physical AI** — Umbrella industry term for AI systems that perceive, understand, and act in the physical world through sensors and actuators — robots, autonomous vehicles, smart spaces; popularized by NVIDIA/Jensen Huang from 2024 onward as the "next wave" after generative AI. Effectively the commercial rebrand of embodied AI — see [history](history.md) and [state of the art](state-of-the-art.md).
- **Planetary roller screw** — Rotary-to-linear transmission in which threaded rollers orbit between a screw shaft and nut, spreading load over many contact lines; versus ball screws it gives ~2–3× the load capacity and far longer life in the same diameter. Tesla Optimus uses 14 of them (inverted layout) in its linear actuators, making roller screws a headline humanoid supply-chain and cost item as of 2026. See [hardware](hardware.md).

## Q–S

- **QDD (quasi-direct-drive) actuator** — A large-diameter, high-torque-density motor with a deliberately low gear ratio (~3:1–10:1), giving backdrivability, low reflected inertia, impact tolerance, and torque estimation straight from motor current ("proprioceptive actuation", MIT Cheetah lineage). Default choice for dynamic legged robots; contrast harmonic drive. See [hardware](hardware.md).
- **RaaS (Robots-as-a-Service)** — Business model where customers pay a subscription or per-task fee instead of buying the robot, shifting capex to opex and keeping fleet data + upgrades with the vendor; the prevailing commercial structure for humanoid and warehouse-robot pilots as of 2026. See [investment](investment.md).
- **Reinforcement learning (RL)** — Learning a policy by trial and error against a reward signal rather than from demonstrations. In Physical AI it dominates locomotion (massively parallel sim training + sim2real) and is re-emerging as real-world fine-tuning to push manipulation reliability (e.g., Physical Intelligence's RECAP/π*0.6). See [locomotion](locomotion.md) and [manipulation](manipulation.md).
- **Sim2real** — Transferring a policy trained in simulation onto physical hardware; the "sim-to-real gap" is the mismatch in dynamics, contact, sensing, and visuals that makes naive transfer fail. Attacked with domain randomization, better physics/rendering, and real-world adaptation. See [simulation](simulation.md).
- **System 1 / System 2** — See **Dual-system VLA** above.

## T–Z

- **Tactile sensing** — Giving robots a sense of touch. Two dominant families: *vision-based* sensors (GelSight and descendants: a camera images the deformation of an illuminated elastomer pad, yielding high-resolution contact geometry and force) and *taxel arrays* (grids of discrete pressure/magnetic sensing elements, the robot-skin approach used on fingertips and palms). See [hardware](hardware.md) and [manipulation](manipulation.md).
- **Taxel** — "Tactile pixel": one discrete sensing element in a tactile array; array resolution is quoted in taxels the way image resolution is quoted in pixels.
- **Teleoperation** — A human remotely controlling a robot in real time — via leader–follower arms (ALOHA), VR headsets, motion-capture suits, or exoskeletons. In Physical AI it is primarily a *data-collection* method: the main source of high-quality demonstrations for imitation learning, with cost scaling in operator hours. See [data](data.md).
- **UMI (Universal Manipulation Interface)** — A handheld, unpowered 3D-printed gripper with a GoPro as its only sensor (Chi et al., 2024, arXiv:2402.10329); humans collect "in-the-wild" demonstrations without any robot, gripper poses are recovered by monocular SLAM, and policies transfer to real arms. Spawned a large variant family (DexUMI, FastUMI, UMI-on-Legs). See [data](data.md).
- **VLA (vision-language-action model)** — A foundation model, usually initialized from a vision-language model, that maps camera images + language instructions directly to robot actions; the term was introduced with Google DeepMind's RT-2 (2023). The dominant architecture class of Physical AI as of 2026 (π0.x, Gemini Robotics, GR00T, Helix) — see [VLA models](vla-models.md).
- **Whole-body control (WBC)** — Control framework that coordinates *all* of a robot's joints simultaneously to satisfy a prioritized stack of tasks (e.g., keep balance ≻ track hand pose ≻ maintain posture), typically solved as a quadratic program each timestep; the classic enabler of humanoid loco-manipulation. See [locomotion](locomotion.md).
- **World model** — A learned model that predicts how an environment evolves — future observations or states conditioned on actions. Used three ways in Physical AI: as a neural simulator/training ground (Genie 3), as a synthetic-data engine (NVIDIA Cosmos), and increasingly as the policy backbone itself ("world-action models", e.g., GR00T N2). See [world models](world-models.md).
- **ZMP (zero moment point)** — The point on the ground where the net moment of gravity plus inertial forces has no horizontal component; keeping the ZMP inside the foot-support polygon is the classic criterion for dynamically stable walking (Vukobratović, late 1960s–70s). It underpinned ASIMO-era humanoids and survives as a stability check even as RL/MPC controllers took over. See [locomotion](locomotion.md).

## Sources
- https://www.nvidia.com/en-us/glossary/generative-physical-ai/ — NVIDIA's definition of Physical AI
- https://www.nvidia.com/en-us/glossary/embodied-ai/ — NVIDIA's definition of embodied AI; term contrast
- https://arxiv.org/abs/2304.13705 — ACT/ALOHA paper: action chunking, $20k rig, 80–90% success from 10-min demos
- https://arxiv.org/abs/2402.10329 — UMI paper: handheld GoPro gripper, SLAM-recovered trajectories
- https://diffusion-policy.cs.columbia.edu/ — Diffusion Policy (Chi et al., RSS 2023) definition
- https://www.pi.website/blog/pi0 — π0 flow-matching action expert, up-to-50 Hz control
- https://www.pi.website/research/fast — FAST action tokenizer (DCT-based compression)
- https://robotics-transformer-x.github.io/ — Open X-Embodiment: 1M+ trajectories, 22 embodiments, 60 datasets, RT-X transfer
- https://arxiv.org/abs/2108.10470 — Isaac Gym: GPU-parallel physics, 2–3 orders-of-magnitude speedup
- https://arxiv.org/abs/1703.06907 — Domain randomization (Tobin et al., 2017)
- https://arxiv.org/abs/2503.14734 — GR00T N1 whitepaper: dual-system architecture, 10 Hz VLM / 120 Hz diffusion action module
- https://www.figure.ai/news/helix — Figure Helix dual-system architecture: 7–9 Hz System 2 / 200 Hz System 1
- https://arxiv.org/abs/2307.15818 — RT-2 paper, coins the term "vision-language-action (VLA) models"
- https://en.wikipedia.org/wiki/Zero_moment_point — ZMP definition and Vukobratović attribution
- https://en.wikipedia.org/wiki/Cost_of_transport — dimensionless CoT formula P/(m·g·v); gives gross human-walking CoT ≈0.3
- https://www.science.org/doi/10.1126/science.1107799 — Collins et al. 2005: human walking CoT ≈0.2 reference value, ASIMO ≈3.2
- https://arxiv.org/abs/1901.08652 — Hwangbo et al. (Science Robotics 2019): learned ANYmal policy beats model-based baseline on power (78.1 vs 97.3 W) and torque
- https://doi.org/10.1631/FITEE.2401070 — Wang et al., FITEE 2025 26(9):1679–1691: learned multigait policy, average CoT 0.4306
- https://pmc.ncbi.nlm.nih.gov/articles/PMC5751610/ — GelSight vision-based tactile sensing mechanism
- https://www.fastcompany.com/91314612/this-tiny-screw-is-powering-the-humanoid-robot-revolution — planetary roller screws vs ball screws in humanoids
- https://www.kggfa.com/news/humanoid-robot-dexterous-hand-structure-to-high-load-bearing-development-the-number-of-roller-screws-may-be-doubled/ — Optimus's 14 inverted planetary roller screws (2 elbow, 4 wrist, 8 leg)
- https://arxiv.org/abs/2004.00467 — QDD definition: high-torque-density motor + low (<10:1) gear ratio for backdrivability/bandwidth
- https://en.wikipedia.org/wiki/Strain_wave_gearing — harmonic drive 30:1–320:1 single-stage ratios, no backlash
- https://arxiv.org/abs/2410.18647 — data scaling laws in imitation learning
- https://arxiv.org/abs/2505.05753 — embodiment scaling laws in locomotion
- https://generalistai.com/blog/nov-04-2025-GEN-0 — GEN-0 270k+ hours scaling claim (company-reported)
