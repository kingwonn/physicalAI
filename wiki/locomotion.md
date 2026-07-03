---
title: Legged Locomotion
slug: locomotion
updated: 2026-07-03
confidence: verified
---
> Legged locomotion went through a paradigm shift roughly between 2018 and 2022: from model-based control (ZMP walking, whole-body MPC) to reinforcement-learning policies trained in massively-parallel GPU simulation and transferred zero-shot to hardware. The now-standard recipe — PPO with thousands of parallel environments (Isaac Gym/Lab lineage), terrain curricula, domain randomization, and teacher–student distillation of privileged observations — first made quadrupeds robust in the wild (ANYmal hiking mountains, DARPA SubT), then agile (parkour from egocentric vision, 2023–24), and by 2024–26 carried humanoids from lab walking to parkour, 10 m/s sprints, and general whole-body motion tracking. As of 2026-07, essentially every serious quadruped and humanoid program, including Boston Dynamics, uses learned locomotion; the frontier has moved to perceptive whole-body agility and unifying locomotion with [manipulation](manipulation.md).

## Why locomotion is the solved-enough layer of Physical AI

- Locomotion is the first robot capability where sim-to-real RL became the *default* industrial method, not a research curiosity — years ahead of [manipulation](manipulation.md), where contact-rich dynamics and perception diversity are harder to simulate.
- Reasons it cracked first: low-dimensional action space (12–29 joints), dynamics dominated by rigid-body physics + contacts (simulable), self-supervised reward (velocity tracking), and cheap resets in sim.
- Locomotion policies are the "spinal cord" layer under [VLA models](vla-models.md) and whole-body controllers in modern [humanoid](humanoid-robots.md) stacks: a high-level model emits velocity or pose targets; a learned low-level policy at ~50 Hz keeps the robot upright.
- See [history](history.md) for the broader field timeline and [state-of-the-art](state-of-the-art.md) for the current overall snapshot.

## Era 1 — Model-based control: ZMP to MPC (1968–~2019)

- **ZMP (Zero Moment Point)**: criterion introduced by Miomir Vukobratović (1968–72). Stability = keep the point where net inertial+gravity moments vanish inside the support polygon. Enabled Honda P2 (1996) and **ASIMO** (2000, walking 1.6 km/h at debut) and a generation of flat-floor, quasi-static walkers.
- **Preview control / capture point**: Kajita's ZMP preview control (2003) and capture-point / divergent-component-of-motion methods made walking dynamic rather than quasi-static.
- **Raibert dynamics**: MIT Leg Lab hoppers (1980s) showed dynamic balance via simple heuristics — the intellectual root of Boston Dynamics (BigDog 2005, Spot, hydraulic Atlas).
- **Convex MPC era (~2013–2021)**: whole-body MPC + trajectory optimization gave the DRC-era humanoids and MIT Cheetah 3 / Mini Cheetah their gaits; Boston Dynamics' famous Atlas parkour and backflip videos (2017–2021) were model-based (offline-optimized behavior libraries + online MPC), *not* RL.
- Structural weaknesses that RL later exploited: hand-modeled contact schedules, fragility to unmodeled terrain (mud, vegetation, rubble), heavy per-behavior engineering, and poor recovery from large disturbances.

## Era 2 — The RL turn (2018–2021)

- **Hwangbo et al., Science Robotics 2019** (ETH Zurich): RL policies trained in RaiSim with a learned **actuator network** (models real series-elastic actuator dynamics) transferred zero-shot to ANYmal — faster locomotion than prior model-based controllers plus fall recovery. Established that the sim-to-real gap is largely an *actuator/contact modeling* problem.
- **Lee et al., Science Robotics 2020** ("Learning quadrupedal locomotion over challenging terrain"): blind (proprioception-only) ANYmal controller; introduced the **privileged teacher–student** paradigm to locomotion — teacher trains with ground-truth terrain/contact info in sim, student distills to a policy using only deployable sensor history. Zero-shot robustness on mud, snow, rubble, vegetation never seen in training.
- **RMA (Kumar, Fu, Pathak, Malik — RSS 2021)**: rapid motor adaptation; an adaptation module estimates environment latents online from proprioceptive history — the low-cost-quadruped (Unitree A1) counterpart to teacher–student.
- **Siekmann et al. 2021** (Oregon State): blind bipedal stair traversal on Cassie via sim-to-real RL — first convincing biped robustness result from the same toolbox.
- **DARPA SubT Final 2021**: team CERBERUS (consortium led by the University of Nevada Reno / NTNU, with ETH Zurich supplying the robots and controllers) won using four ANYmal C quadrupeds running learned locomotion controllers in mines/caves/urban rubble — first high-stakes field validation of RL locomotion.

## Era 3 — Massively-parallel simulation (2021–)

- **Isaac Gym (NVIDIA, 2021, arXiv:2108.10470)**: end-to-end GPU physics + RL, thousands of environments on one GPU, eliminating the CPU-sim bottleneck.
- **"Learning to Walk in Minutes" (Rudin et al., CoRL 2021, arXiv:2109.11978)**: the recipe paper. 4096 parallel ANYmal environments, PPO, game-inspired terrain curriculum; flat-terrain policy in **under 4 minutes**, rough-terrain in ~20 minutes on a single GPU — orders of magnitude faster than prior work. Open-sourced as `legged_gym` + `rsl_rl`, which became the de-facto community standard (extended to A1/Go1/Go2, G1, H1, Cassie, Digit, Spot, ANYmal-B/C/D and more; RSL-RL library paper arXiv:2509.10771, 2025).
- Simulator landscape as of 2026-07 (details on [simulation](simulation.md)):

| Stack | Origin | Notes |
|---|---|---|
| Isaac Gym → Orbit → **Isaac Lab** | NVIDIA | Dominant lineage for locomotion RL; Isaac Lab is the maintained successor (framework paper arXiv:2511.04831) |
| **MuJoCo MJX / MuJoCo Playground** | Google DeepMind | GPU MuJoCo; Playground (2025) trains locomotion policies in minutes on one GPU |
| **Genesis** | open-source consortium | generative/universal physics engine, Dec 2024 |
| **Newton** | NVIDIA + Google DeepMind + Disney Research | open-source, Warp+OpenUSD based, beta since 2025-09, Linux Foundation governance; interoperates with Isaac Lab and MuJoCo Playground; NVIDIA reports MuJoCo-Warp up to ~152x faster than MJX on locomotion workloads (RTX 4090, vendor benchmark, unverified) |

## The standard training recipe (as of 2026)

The community-consensus pipeline, stable since ~2022 with incremental upgrades:

1. **Algorithm**: PPO, ~4096 parallel envs, minutes-to-hours wall clock on one GPU.
2. **Observations**: proprioceptive history (joint pos/vel, IMU, last actions); optionally height-map scan or depth for perceptive policies.
3. **Actions**: target joint positions to a PD controller at 50 Hz (torque policies exist but transfer is harder).
4. **Reward**: velocity-command tracking + survival, minus penalties (torque, action rate, slip, orientation); optionally style terms.
5. **Terrain curriculum**: procedurally generated slopes/stairs/gaps/rubble, difficulty promoted per-robot on success ("game-inspired curriculum").
6. **Domain randomization**: friction, link masses, motor strength/latency, push perturbations, sensor noise — the core sim-to-real tool.
7. **Actuator modeling**: learned actuator nets or identified motor models close the remaining dynamics gap.
8. **Teacher–student / asymmetric actor-critic**: teacher (or critic) sees privileged sim state (true heights, contacts, frictions); deployable student distilled via DAgger-style supervision on observation history, or depth-vision student distilled from scandots teacher.
9. **Style priors when naturalness matters**: Adversarial Motion Priors (AMP, Peng et al. 2021) or motion-tracking objectives from human/animal mocap.
10. **Deployment**: ONNX/TensorRT policy on embedded compute, running under a safety layer; zero-shot, no on-robot fine-tuning in the standard recipe.

Failure modes still handled by engineering: reward hacking (foot skating, unnatural gaits), sim-unmodeled compliance (soft ground handled via specialized granular-media models), and camera-latency mismatch for vision policies.

## Parkour and agility milestones

| Year | System | Result |
|---|---|---|
| 2021 | Atlas parkour (Boston Dynamics) | model-based behavior library + MPC; not learned |
| 2022 | Mini Cheetah rapid locomotion (MIT, Margolis et al., RSS 2022) | RL controller sustaining sprints up to 3.9 m/s on grass, ice, gravel |
| 2022-09 | **Cassie 100 m Guinness record** (Oregon State) | 24.73 s, RL controller, standing start/finish |
| 2023 | Robot Parkour Learning (Zhuang et al., CoRL 2023) + **Extreme Parkour** (CMU, arXiv:2309.14341) | low-cost quadruped, single depth camera, end-to-end: long-jumps 2x body length, high-jumps 2x body height, handstand walking |
| 2024-03 | **ANYmal Parkour** (Hoeller et al., Science Robotics) | perception + skill catalog + navigation modules; jumping, climbing, crouching at up to 2 m/s through obstacle courses |
| 2024 | **Humanoid Parkour Learning** (Zhuang et al., CoRL 2024) | end-to-end vision whole-body policy, no motion priors: jumps onto 0.42 m platforms, leaps 0.8 m gaps, runs 1.8 m/s outdoors |
| 2024-04 | DeepMind 1v1 robot soccer (Science Robotics) | RL on mini OP3 humanoids: kicking, falling-and-recovering, dynamic play |
| 2025 | ASAP (LeCAR Lab, RSS 2025) | real-to-sim delta-action model alignment for agile G1 whole-body skills |
| 2026-01 | **Deep Whole-Body Parkour** (Zhuang et al., arXiv:2601.07701) | exteroception fused into whole-body motion tracking: vaulting and dive-rolling over uneven terrain with a single policy |

## Bipeds and humanoids: from Cassie to whole-body control

- **Cassie/Digit line**: Xie et al. (2019) first RL walking on Cassie; blind stairs 2021; 100 m Guinness record 2022. Agility's Digit uses learned locomotion in warehouse deployments (see [humanoid robots](humanoid-robots.md)).
- **Radosavovic et al., Science Robotics 2024** ("Real-world humanoid locomotion with reinforcement learning", Berkeley): causal-transformer policy trained in sim, zero-shot outdoor walking on Digit — evidence that locomotion policies scale with the same sequence-model machinery as [VLAs](vla-models.md).
- **Whole-body motion tracking became the dominant humanoid framing (2024–2026)**: rather than a walking controller, train one policy to track retargeted human motion (locomotion falls out as a special case). Lineage: H2O/OmniH2O and Expressive Whole-Body Control (2024) → **ASAP** (RSS 2025; aligns sim physics to real via learned delta-action models) → **HOVER** (NVIDIA, ICRA 2025; one neural controller multiplexing command modes) → BeyondMimic / GMT / UniTracker (2025) → **SONIC** (NVIDIA, arXiv:2511.07820, 2025-11; motion tracking "supersized" — reports 100% success over 50 diverse real-world trajectories on a Unitree G1, real-time onboard).
- **Unitree demo cadence** (see [landscape-china](landscape-china.md)): H1 standing backflip without hydraulics (2024, claimed first); G1 kung-fu/side-flip demos through 2025; Spring Festival Gala 2026-02 routine — autonomous kung-fu, 3 m trampoline somersaults, 7.5-rotation airflare, wall-assisted backflips — watched by ~679M viewers (Unitree PR figures, unverified).
- **Speed records** (as of 2026-04): Unitree H1 sprinted **10 m/s (~22.4 mph)** on an outdoor track on 2026-04-11, matching the 10 m/s mark set by MirrorMe's "Bolt" earlier in 2026 (both single-source company videos, unverified); H1's own prior record was 3.3 m/s (2024-03). Software/control gains, not new hardware, credited.
- **Boston Dynamics converted**: partnered with the Robotics & AI Institute (2025-02, press release) on a shared RL training pipeline for electric Atlas; RAI's open Spot pipeline (Isaac Lab, ICRA 2025) hit **5.2 m/s zero-shot — ~3x Spot's default top speed** — using distribution-matching (Wasserstein/MMD + CMA-ES) to tune sim parameters. Fifth-gen electric Atlas (unveiled 2026-07) continues the sim+RL pipeline with "order of magnitude" simpler hardware (Forbes, as of 2026-07).

## Robustness in the wild

- **Miki et al., Science Robotics 2022** ("robust perceptive locomotion in the wild"): attention-based recurrent fusion of proprioception + uncertain elevation maps; ANYmal hiked Mount Etzel (2.2 km, 120 m elevation): summit in 31 min vs ~35 min human sign-posted time, zero falls — the canonical field-robustness result.
- Blind policies (Lee 2020) survive terrain classes never simulated: mud, snow, gushing water, dense vegetation — robustness emerges from randomized-dynamics training, not terrain realism.
- Deformable/granular terrain: dedicated granular-media modeling in sim extended robustness to sand and soft ground (Choi et al., Science Robotics 2023).
- Commercial proof: thousands of Spot and ANYmal units run learned or hybrid controllers in industrial inspection; Unitree shipped 5,500+ humanoids in 2025 with RL locomotion as standard firmware (as of 2026, see [investment](investment.md) and [organizations](organizations.md)).
- Surveys consolidating the field: Ha, Lee, van de Panne, Xie, Yu, Khadiv — "Learning-based legged locomotion: state of the art and future perspectives" (IJRR 2025, arXiv:2406.01152); MDPI systematic DRL-locomotion review (2025, 27 studies 2018–2025).

## Open problems (as of 2026-07)

- **Perceptive whole-body generality**: parkour-grade agility + motion tracking + manipulation in one policy is just emerging (Deep Whole-Body Parkour, 2026-01); no system yet handles arbitrary terrain + arbitrary tasks.
- **Torque-level and hardware-limit-aware policies**: most policies still ride on PD position control; direct torque policies transfer poorly.
- **Long-horizon autonomy**: locomotion is robust for minutes-to-hours, but falls remain costly for 50+ kg humanoids; fall-recovery and fall-avoidance under payload is active work.
- **Energy efficiency**: learned gaits typically burn more energy than optimized model-based gaits; cost-of-transport rarely reported.
- **Benchmark opacity**: agility claims are company-video-driven (speed records, gala demos) with no standardized evaluation — see [open problems](open-problems.md).

## Sources

- https://arxiv.org/abs/2109.11978 — Rudin et al., "Learning to Walk in Minutes": 4096 envs, <4 min flat / ~20 min rough terrain, terrain curriculum, legged_gym.
- https://ar5iv.labs.arxiv.org/html/2108.10470 — Isaac Gym paper: GPU-based massively parallel physics for RL.
- https://www.science.org/doi/10.1126/scirobotics.abc5986 — Lee et al. 2020: blind quadrupedal locomotion, privileged teacher–student, zero-shot mud/snow/rubble robustness.
- https://www.science.org/doi/10.1126/scirobotics.abk2822 — Miki et al. 2022: perceptive locomotion in the wild; Mount Etzel hike numbers.
- https://ethz.ch/en/news-and-events/eth-news/news/2022/01/how-robots-learn-to-hike.html — ETH news: Etzel hike 31 min to summit vs 35 min human estimate.
- https://www.science.org/doi/10.1126/scirobotics.adi7566 — Hoeller et al., ANYmal Parkour (Science Robotics 2024): perception/locomotion/navigation modules, up to 2 m/s.
- https://arxiv.org/pdf/2309.14341 — Cheng et al., Extreme Parkour with Legged Robots: 2x-length jumps, 2x-height climbs, handstand, single depth camera.
- https://humanoid4parkour.github.io/ — Zhuang et al., Humanoid Parkour Learning (CoRL 2024): 0.42 m platform, 0.8 m gaps, 1.8 m/s, no motion priors.
- https://arxiv.org/abs/2601.07701 — Deep Whole-Body Parkour (2026-01): perceptive general motion control, vaulting and dive-rolling.
- https://news.oregonstate.edu/news/bipedal-robot-developed-oregon-state-achieves-guinness-world-record-100-meters — Cassie 100 m Guinness record, 24.73 s (2022).
- https://www.guinnessworldrecords.com/world-records/629600-fastest-100-m-by-a-bipedal-robot — Guinness official listing: fastest 100 m by a bipedal robot.
- https://arxiv.org/abs/2205.02824 — Margolis et al., Rapid Locomotion via RL (RSS 2022): Mini Cheetah sustained speeds up to 3.9 m/s.
- https://global.honda/en/newsroom/news/2000/c001120b-eng.html — Honda ASIMO debut announcement (2000): 1.6 km/h walking speed.
- https://www.science.org/doi/full/10.1126/scirobotics.adi9579 — Radosavovic et al.: transformer RL humanoid locomotion on Digit (Science Robotics 2024).
- https://github.com/LeCAR-Lab/ASAP — ASAP (RSS 2025): sim/real physics alignment via delta-action models, Unitree G1.
- https://arxiv.org/pdf/2511.07820 — SONIC (NVIDIA, 2025): large-scale humanoid motion tracking, 100% success on 50 real G1 trajectories.
- https://rai-inst.com/resources/press-release/boston-dynamics-atlas-partnership/ — BD + RAI Institute RL partnership for Atlas (2025-02).
- https://rai-inst.com/resources/papers/high-performance-reinforcement-learning-on-spot/ — RAI Institute: Spot RL at 5.2 m/s, sim-param optimization via distributional measures (ICRA 2025).
- https://www.humanoidsdaily.com/news/unitree-h1-reclaims-speed-record-with-blistering-10-m-s-sprint — Unitree H1 10 m/s sprint (2026-04-11); prior 3.3 m/s record; MirrorMe Bolt context.
- https://www.prnewswire.com/news-releases/kung-fu-meets-spring--unitree-spring-festival-gala-robots-present-cyber-real-kung-fu-in-the-year-of-the-horse-302689291.html — Unitree Spring Festival Gala 2026 demo claims (airflare, trampoline somersaults, viewership).
- https://developer.nvidia.com/blog/announcing-newton-an-open-source-physics-engine-for-robotics-simulation/ — Newton physics engine: NVIDIA+DeepMind+Disney, Warp/OpenUSD, Isaac Lab + MuJoCo Playground interop.
- https://www.linuxfoundation.org/press/linux-foundation-announces-contribution-of-newton-by-disney-research-google-deepmind-and-nvidia-to-accelerate-open-robot-learning — Linux Foundation press release (2025-09-29): Newton contribution, beta status, vendor-neutral governance.
- https://spectrum.ieee.org/ai-institute — IEEE Spectrum: independent confirmation RAI's RL tripled Spot's running speed (1.7 to 5.2 m/s).
- https://arxiv.org/abs/2207.04914 — Team CERBERUS SubT technical overview: UNR/NTNU-led consortium, four ANYmal C robots at the Final Event.
- https://arxiv.org/pdf/2511.04831 — Isaac Lab framework paper (2025): GPU-accelerated multi-modal robot learning; morphology coverage of the legged-gym lineage.
- https://arxiv.org/abs/2406.01152 — Ha et al., learning-based legged locomotion survey (IJRR 2025): field state-of-the-art and perspectives.
- https://www.mdpi.com/2410-390X/10/1/8 — systematic DRL legged-locomotion review (2025): 27 studies, DR/reward-shaping findings.
- https://arxiv.org/html/2509.10771v1 — RSL-RL library paper (2025): standard PPO tooling for locomotion research.
- https://www.forbes.com/sites/johnkoetsier/2026/07/02/boston-dynamics-new-atlas-humanoid-robot-order-of-magnitude-simpler/ — fifth-gen electric Atlas simplification (2026-07).
