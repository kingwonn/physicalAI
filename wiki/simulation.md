---
title: Simulation & Sim2Real
slug: simulation
updated: 2026-07-03
confidence: verified
---
> Simulation is the primary lever for scaling robot learning data beyond what real hardware can produce: GPU-parallel physics engines (Isaac Sim/Lab, MuJoCo Warp/MJX, Genesis, ManiSkill3/SAPIEN) run thousands of environments per GPU, turning locomotion training from weeks into minutes, while domain randomization, system identification, and real2sim pipelines shrink the sim2real gap. In 2025–26 the field consolidated around two GPU physics stacks — NVIDIA's Newton (co-developed with Google DeepMind and Disney Research, Linux Foundation-governed since 2025-09, 1.0 GA at GTC 2026) and MuJoCo Warp — and simulation's role expanded from RL training ground to industrial-scale synthetic-data factory (MimicGen/SkillGen trajectory multiplication, Cosmos/GR00T-Dreams neural world-model data), increasingly blurring into [world models](world-models.md) as a "neural simulation" tier of the [data strategy](data.md).

## Why simulation matters for Physical AI

- Real-robot data is the binding constraint on robot foundation models: teleoperation collects on the order of hours per robot per day, while a single GPU can simulate years of experience per day. See [Data](data.md) for the full data-pyramid picture (web data → synthetic/sim → real teleop).
- Simulation is effectively **solved infrastructure for locomotion**: massively parallel RL + domain randomization yields zero-shot transferable walking/running controllers — the training recipe behind essentially every modern [humanoid](humanoid-robots.md) and quadruped gait (see [Locomotion](locomotion.md)). Rudin et al. (2021) showed ANYmal locomotion policies trained in ~20 minutes with 4,096 parallel Isaac Gym environments on one workstation GPU.
- **Manipulation remains real-data-heavy**: contact dynamics, deformables, and perception gaps mean most [VLA models](vla-models.md) (π0, Helix, RT-2 lineage) train predominantly on real teleop, with sim used for augmentation, evaluation, and pre-training. Closing this asymmetry is a headline [open problem](open-problems.md).
- Simulation also serves as **evaluation harness** (reproducible benchmarks such as ManiSkill, RoboCasa, LIBERO, Isaac Lab Arena) — increasingly important as VLA claims outpace standardized testing (see [State of the art](state-of-the-art.md)).

## Major platforms (as of 2026-07)

| Platform | Steward | Physics / rendering | Distinguishing traits | Status |
|---|---|---|---|---|
| **Isaac Sim 5.0 + Isaac Lab** | NVIDIA | PhysX 5 → migrating to Newton; RTX ray-traced sensors | Full-stack robotics sim on Omniverse/OpenUSD; SDG pipelines; neural (NuRec) rendering; open-sourced on GitHub at SIGGRAPH 2025 | GA; Isaac Lab 2.3 (2025-09) added ADR, PBT, dexterous teleop |
| **MuJoCo / MJX / MuJoCo Warp** | Google DeepMind | MuJoCo contacts; MJX (JAX), MJWarp (NVIDIA Warp) | Research standard for contact-rich RL; MJWarp is joint DeepMind–NVIDIA, feeds Newton | MuJoCo mature; MJWarp ships as a Newton 1.0 solver ("MuJoCo 3.5", 2026-03); throughput-optimized (per docs, single-step latency worse than CPU MuJoCo) |
| **Newton** | Linux Foundation (NVIDIA + Google DeepMind + Disney Research) | Multi-solver (MJWarp, Warp solvers, MPM), differentiable, OpenUSD | Intended common GPU physics substrate; Isaac Lab backend; adopters incl. ETH RSL, TUM, Peking U., Lightwheel, Style3D | Beta 2025-09-29; 1.0 GA at GTC 2026 (2026-03) w/ VBD + iMPM deformables, Disney Kamino solver |
| **Genesis** | Genesis AI + ~20-lab academic consortium | Custom GPU physics (rigid, MPM, SPH, FEM) + generative scene engine | Pure-Python; headline 43M FPS on RTX 4090 (simple scene); speed claims disputed (see below) | Open source since 2024-12 |
| **SAPIEN / ManiSkill3** | UCSD Hao Su lab / Hillbot | PhysX-based GPU sim + parallel rendering | Manipulation-centric benchmark suite (12 domains); 10–1000x faster visual-data collection than peers, ~30k+ FPS with rendering; RSS 2025 paper | Active |
| **Habitat 3.0** | Meta FAIR | Kinematic/abstracted physics, fast CPU rendering | Human-robot collaboration (avatars), social navigation/rearrangement; navigation-era flagship | Maintained; less central since field shifted to GPU physics + manipulation |
| **Genie Sim 3.0** | AgiBot (Zhiyuan) | — | Open-sourced full-stack eval toolchain with AgiBot World datasets; used in AGIBOT World Challenge 2026 at ICRA (526 teams, 27 countries) | Active; see [China landscape](landscape-china.md) |

- Other notable entries: Gazebo/ROS 2 (classical robotics), Webots, CoppeliaSim (legacy); Unreal/Unity-based photoreal sims (AirSim descendants, UnrealZoo); mjlab (2026-01, Kevin Zakka et al.) — Isaac Lab's manager-based API on MuJoCo Warp physics, positioned as a lightweight alternative; MuJoCo Playground (DeepMind, 2025-01) — batteries-included MJX/Warp sim2real suite used for quadruped and humanoid transfer.

## The GPU-parallel RL paradigm

- **Core recipe** (established by Isaac Gym 2021, now standard): thousands of vectorized environments on one GPU, PPO-family on-policy RL, rewards/observations computed as batched tensors without CPU round-trips; end-to-end policy training in minutes-to-hours on consumer hardware.
- Throughput benchmarks (vendor-reported, as of 2025-09 to 2026-06):
  - MuJoCo Warp: >70x humanoid and ~100x in-hand-manipulation speedup vs. prior MuJoCo baselines at Newton's GTC 2025 unveiling; the Newton 1.0 GA release (GTC 2026, 2026-03) reports 252x (locomotion) and 475x (manipulation) vs. MJX on RTX PRO 6000 Blackwell (vendor numbers, no independent replication).
  - ManiSkill3: 30,000+ FPS including rendering; 10–1000x faster and 2–3x less GPU memory than comparable platforms (paper claim).
  - Genesis: claimed 43M FPS / 430,000x real time for a Franka arm on an RTX 4090. Independent analysis (Stone Tao, SAPIEN/ManiSkill author) showed headline numbers came from near-empty scenes; with typical contact-rich setups other GPU sims match or beat it. Treat headline FPS marketing across all vendors as scene-dependent.
- **Trend — physics/framework decoupling**: Isaac Lab API is becoming a de-facto interface standard (adopted by mjlab over MuJoCo Warp), while Newton aims to be a solver-pluggable substrate; expect training code portable across physics backends.
- **Trend — RL at scale returns**: Isaac Lab 2.3 shipped built-in Automatic Domain Randomization (ADR) and Population Based Training (PBT) with runs up to 40,960 parallel envs for dexterous manipulation, echoing OpenAI's 2019 ADR recipe at commodity cost.

## Sim2real: the gap and the toolkit

Gap sources: rigid-contact approximation, actuator/transmission dynamics, sensing noise and latency, visual appearance, and unmodeled physics (cables, deformables, friction variability).

| Technique | Idea | Canonical examples |
|---|---|---|
| Domain randomization (DR) | Randomize visuals/dynamics so reality is one sample of the training distribution | Tobin et al. 2017 (vision); Peng et al. 2018 (dynamics) |
| Automatic DR / curricula | Auto-widen randomization ranges as policy improves | OpenAI Rubik's Cube 2019; Isaac Lab 2.3 ADR (2025) |
| System identification | Fit sim parameters (esp. actuators) to real logs; learned actuator nets | Hwangbo et al. 2019 (ANYmal) |
| Teacher-student distillation | Privileged-state teacher in sim → observation-only student deployed | Lee et al. 2020; standard in humanoid whole-body control |
| LLM-guided reward + DR design | LLM writes reward functions and DR configs | Eureka (2023), DrEureka (2024) |
| Multi-simulator randomization | Train across heterogeneous simulators to cancel per-engine bias | PolySim (2025-10) — zero-shot transfer to Unitree G1 |
| Real2sim / digital twins | Reconstruct real scenes (photogrammetry, 3D Gaussian splatting, neural rendering) as sim assets | Isaac Sim 5.0 NuRec; digital-twin factory workflows |
| Residual / online correction | Fine-tune or correct sim policy with small real datasets or human interventions | TRANSIC (2024); simDP (2026-06) aligning action/observation spaces |
| Hardware-in-the-loop & co-training | Mix sim and real batches when training one policy | Common in VLA training (sim-and-real co-training reports) |

- Consensus as of 2026: the gap is an engineering budget, not a wall — for locomotion it is routinely crossed zero-shot; for contact-rich manipulation it still costs real-world fine-tuning. A 2025 Annual Reviews survey ("The Reality Gap in Robotics") frames best practice as combining fidelity, randomization, and adaptation rather than betting on any single fix.

## Synthetic data generation (SDG) pipelines

- **Trajectory multiplication**: MimicGen (2023) generated ~50k demonstrations from ~200 human demos by re-composing object-centric segments; successor SkillGen (Isaac Lab 2.3) adds collision-free motion planning; DexMimicGen extends to bimanual/dexterous setups. This is the workhorse for scaling imitation data cheaply.
- **Perception SDG**: Isaac Sim/Omniverse Replicator renders ray-traced RGB, depth, lidar, radar with randomized scenes for detector/segmenter training — mature, widely used in industrial vision.
- **Neural / world-model SDG** (the 2025–26 shift): NVIDIA Cosmos world foundation models generate photoreal robot video conditioned on an image + language; **GR00T-Dreams** (based on DreamGen research) extracts pseudo-action trajectories from these "dreams" to train GR00T-N humanoid models on tasks with zero task-specific teleop. NVIDIA reports development time falling "from months to hours" (vendor claim). Cosmos WFMs passed 3M downloads and the NVIDIA Physical AI Dataset 4.8M downloads as of 2025-09. This tier overlaps heavily with [World models](world-models.md).
- **Cosmos Transfer** style models do sim2real appearance translation — rendering a sim rollout into diverse photoreal variants, attacking the visual gap from the generative side (Cosmos Transfer 2.5 is 3.5x smaller than its predecessor, as of 2025-09).
- **Data-strategy positioning**: NVIDIA's public "data pyramid" = web-scale video/text (bulk) → synthetic sim + neural data (middle) → real teleop (scarce apex). Genesis AI's pitch inverts the usual skepticism: a proprietary physics engine as the primary data source for a universal robot foundation model. Tesla/Figure emphasize real fleet/teleop data instead; the sim-vs-real data mix is an open strategic bet across [organizations](organizations.md) — see [Data](data.md) and [Investment](investment.md).

## Ecosystem and commercial layer (as of 2026-07)

- **NVIDIA** is the gravitational center: Isaac Sim/Lab open-sourced (SIGGRAPH 2025), Newton beta (2025-09) → 1.0 GA (GTC 2026) under Linux Foundation governance — GA adopters include Skild AI (GPU-rack assembly RL) and Samsung/Lightwheel (deformable cable simulation) — plus GR00T models + Cosmos WFMs + OSMO orchestration as an integrated "three computers" pitch (train / simulate / deploy). The Isaac GR00T reference humanoid (announced 2026-06-01 at GTC Taipei/COMPUTEX) pairs a Unitree H2 Plus body, Sharpa Wave tactile hands, and Jetson Thor T5000 with the open Isaac GR00T stack, aimed at academic labs (Ai2, ETH Zurich, Stanford, UCSD); availability slated for 2026-10.
- **Google DeepMind** keeps MuJoCo free/open and co-develops MuJoCo Warp; MuJoCo Playground + mjlab form the lightweight research-first stack.
- **Genesis AI**: $105M seed co-led by Eclipse and Khosla (2025-07, one of the largest robotics seeds on record; backers incl. Eric Schmidt, Bpifrance, HSG); founded by Zhou Xian (CMU) and Théophile Gervet (ex-Mistral); ~60 staff split US/Europe (as of 2025-07). Went "full stack" with GENE-26.5 (2026-05): dexterous-manipulation demos (egg-cracking, slicing, Rubik's Cube, piano) on humanoid hands co-designed with Wuji Tech; vendor demos only, no third-party evaluation yet.
- **Lightwheel** (sim-asset/eval startup) co-develops Isaac Lab Arena policy-evaluation framework with NVIDIA; **Hillbot** commercializes the SAPIEN/ManiSkill line; **Antioch** (founded 2025-05) raised an $8.5M seed at a $60M valuation (2026-04, A* + Category Ventures) pitching itself as "Cursor for physical AI" — cloud sim instances wired to a robot's real software stack.
- **China**: AgiBot's Genie Sim 3.0 + AgiBot World datasets anchor an open sim2real toolchain; the AGIBOT World Challenge 2026 (ICRA, Vienna, 2026-06; 526 teams from 27 countries in the 2026-05 online round, vivo's PrismBot won the Reasoning-to-Action track) moved final scoring from simulation benchmarks to closed-loop real-robot testing — a notable evaluation-culture shift. See [China landscape](landscape-china.md).

## Timeline highlights, 2024-12 → 2026-06

| Date | Event |
|---|---|
| 2024-12 | Genesis open-sourced; viral 430,000x-real-time claim and ensuing benchmark-methodology dispute |
| 2025-01 | MuJoCo Playground released (GPU sim2real suite on MJX) |
| 2025-03 (GTC) | MuJoCo Warp announced; Newton (NVIDIA + DeepMind + Disney) unveiled |
| 2025-06 | Isaac Sim 5.0 / Isaac Lab 2.2 early developer preview on GitHub |
| 2025-07 | Genesis AI emerges from stealth with $105M seed |
| 2025-08 (SIGGRAPH) | Isaac Sim 5.0 + Isaac Lab 2.2 GA, open-sourced |
| 2025-09 | Newton beta under Linux Foundation; Isaac Lab 2.3 (ADR, PBT, Arena w/ Lightwheel); GR00T N1.6 + Cosmos Reason |
| 2025-10 | PolySim multi-simulator randomization → zero-shot Unitree G1 transfer |
| 2026-01 | mjlab preprint (Isaac Lab API on MuJoCo Warp) |
| 2026-03 (GTC) | Newton 1.0 GA — MJWarp ("MuJoCo 3.5") 252x/475x vs MJX vendor claims; VBD + iMPM deformable solvers; Disney Kamino rigid solver; SDF collisions, hydroelastic contact |
| 2026-04 | Antioch $8.5M seed ("Cursor for physical AI") |
| 2026-05 | Genesis AI full-stack demo (GENE-26.5) |
| 2026-06 | AGIBOT World Challenge @ ICRA moves to real-robot closed-loop eval; Genie Sim 3.0 open toolchain; NVIDIA Isaac GR00T reference humanoid (2026-06-01); Cosmos 3 omnimodal WFM release (2026-06) |

## Open questions

- **Can manipulation follow locomotion's sim-first path?** Contact-rich, deformable, and tool-use tasks still lack trustworthy sim physics; Newton's multi-solver (MPM + rigid) coupling is the main bet.
- **Classical sim vs. neural world models**: whether learned video/world models displace physics engines for data generation, or settle into a hybrid (physics for dynamics ground truth, generative models for appearance/diversity) — see [World models](world-models.md).
- **Benchmark integrity**: vendor FPS numbers are scene-dependent and marketing-prone (Genesis episode); policy-level evaluation (Isaac Lab Arena, real-robot challenges like AgiBot's) is displacing raw throughput as the metric that matters.
- **Fragmentation vs. consolidation**: Newton/MJWarp convergence suggests a shared GPU physics substrate, but Genesis, SAPIEN, and proprietary in-house sims (Tesla, Figure, Boston Dynamics) keep the landscape plural.

## Sources
- https://developer.nvidia.com/blog/announcing-newton-an-open-source-physics-engine-for-robotics-simulation/ — Newton architecture, Warp/OpenUSD basis, MJWarp 70x/100x speedups
- https://nvidianews.nvidia.com/news/nvidia-accelerates-robotics-research-and-development-with-new-open-models-and-simulation-libraries — Newton beta + Linux Foundation (2025-09), GR00T N1.6, Cosmos download counts, adopter list
- https://www.linuxfoundation.org/press/linux-foundation-announces-contribution-of-newton-by-disney-research-google-deepmind-and-nvidia-to-accelerate-open-robot-learning — Newton governance
- https://developer.nvidia.com/blog/streamline-robot-learning-with-whole-body-control-and-enhanced-teleoperation-in-nvidia-isaac-lab-2-3/ — Isaac Lab 2.3 (2025-09): ADR, PBT, SkillGen, Arena/Lightwheel, 40,960-env runs
- https://developer.nvidia.com/blog/isaac-sim-and-isaac-lab-are-now-available-for-early-developer-preview/ — Isaac Sim 5.0 / Isaac Lab 2.2 GitHub release, GA at SIGGRAPH 2025
- https://developer.nvidia.com/blog/newton-adds-contact-rich-manipulation-and-locomotion-capabilities-for-industrial-robotics/ — Newton 1.0 GA (GTC 2026, 2026-03-16): MJWarp 252x/475x vs MJX on Blackwell, VBD/iMPM deformables, Kamino solver, Skild AI + Samsung/Lightwheel adopters
- https://mujoco.readthedocs.io/en/latest/mjwarp/ — MJWarp status, features, MJX scaling comparison, Isaac Lab/mjlab integration
- https://github.com/google-deepmind/mujoco_warp — MJWarp repo (NVIDIA + DeepMind joint effort)
- https://github.com/google-deepmind/mujoco_playground — MuJoCo Playground sim2real suite
- https://arxiv.org/abs/2601.22074 — mjlab: Isaac Lab manager-based API on MuJoCo Warp (2026-01)
- https://arxiv.org/abs/2410.00425 — ManiSkill3: GPU-parallel sim+rendering, 30k+ FPS, RSS 2025
- https://arxiv.org/abs/2310.13724 — Habitat 3.0: humans, avatars, robots co-habitat
- https://stoneztao.substack.com/p/the-new-hyped-genesis-simulator-is — independent critique of Genesis speed benchmarks
- https://techcrunch.com/2025/07/01/genesis-ai-launches-with-105m-seed-funding-from-eclipse-khosla-to-build-ai-models-for-robots/ — Genesis AI $105M seed, founders, headcount
- https://techcrunch.com/2026/05/06/khosla-backed-robotics-startup-genesis-ai-has-gone-full-stack-demo-shows/ — Genesis AI full-stack demo (2026-05)
- https://developer.nvidia.com/blog/enhance-robot-learning-with-synthetic-trajectory-data-generated-by-world-foundation-models/ — GR00T-Dreams / DreamGen WFM trajectory generation
- https://developer.nvidia.com/blog/scale-synthetic-data-and-physical-ai-reasoning-with-nvidia-cosmos-world-foundation-models/ — Cosmos WFM SDG role
- https://arxiv.org/abs/2510.01708 — PolySim multi-simulator dynamics randomization, Unitree G1 zero-shot
- https://arxiv.org/abs/2606.03551 — Isaac Sim survey (2026-06): architecture, SDG, usage patterns
- https://arxiv.org/abs/2511.04831 — Isaac Lab framework paper (2025-11)
- https://www.annualreviews.org/content/journals/10.1146/annurev-control-031924-100130 — "The Reality Gap in Robotics" survey: gap taxonomy and best practices
- https://arxiv.org/abs/2109.11978 — Rudin et al.: massively parallel RL, minutes-scale locomotion training
- https://arxiv.org/abs/1703.06907 — Tobin et al. 2017: domain randomization origin
- https://arxiv.org/abs/1910.07113 — OpenAI 2019: automatic domain randomization (Rubik's Cube)
- https://arxiv.org/abs/2310.17596 — MimicGen: 200 demos → 50k synthetic demonstrations
- https://techcrunch.com/2026/04/16/this-simulation-startup-wants-to-be-the-cursor-for-physical-ai/ — Antioch $8.5M seed at $60M valuation (2026-04)
- https://www.tradingview.com/news/eqs:09f22872d094b:0-agibot-world-challenge-2026-advances-embodied-ai-competition-from-simulation-to-real-robot-testing-at-icra-2026/ — AGIBOT World Challenge 2026, Genie Sim 3.0, real-robot eval shift
- https://www.globenewswire.com/news-release/2026/05/13/3293715/0/en/Global-Showdown-526-Teams-from-27-Countries-Compete-in-the-AGIBOT-WORLD-CHALLENGE-ICRA-2026-Online-Round.html — 526 teams / 27 countries in the 2026-05 online round
- https://nvidianews.nvidia.com/news/nvidia-open-humanoid-robot-reference-design — Isaac GR00T reference humanoid (Unitree H2 Plus + Sharpa Wave hands + Jetson Thor T5000, 2026-06-01, availability 2026-10)
- https://www.prnewswire.com/news-releases/genesis-ai-unveils-gene-26-5--the-first-ai-brain-to-enable-robots-with-human-level-physical-manipulation-capabilities-302763638.html — GENE-26.5 launch details, Wuji Tech hand partnership
- https://nvidianews.nvidia.com/news/nvidia-launches-cosmos-3-the-open-frontier-foundation-model-for-physical-ai — Cosmos 3 omnimodal WFM release (2026-06)
