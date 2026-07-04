---
title: Evaluation & Benchmarks
slug: evaluation
updated: 2026-07-04
confidence: verified
---
> Physical AI has no ImageNet: as of 2026-07 the field's headline results are mostly self-reported success rates on self-chosen tasks, run on different robots with 10–20 trials and no statistical testing, which makes [VLA models](vla-models.md) essentially incomparable across papers. The dominant sim benchmarks (LIBERO, CALVIN, SimplerEnv) are saturated — top models cluster at 97–99% while robustness probes like LIBERO-Plus show the same models collapsing below 30% under modest camera or pose perturbations. The 2025–26 response is a wave of shared real-robot evaluation infrastructure (RoboArena on DROID, RoboChallenge Table30, GM-100, AutoEval, VLA-REPLICA), harder sim suites (BEHAVIOR-1K, RoboCasa365, MolmoSpaces-Bench), embodied-reasoning exams (ERQA), and a state-backed Chinese benchmark (EIbench) — but no single standard has won, and industry meanwhile scores robots on throughput, intervention rate, and "nines" rather than benchmark success rates.

## The evaluation crisis in one page

- **Numbers don't transfer.** Real-robot evaluation is slow, hardware-specific, and unreproducible across labs: OpenVLA's headline was 29 tasks on a WidowX/BridgeData rig; π0's was a proprietary task suite on Physical Intelligence's own fleet; Figure's Helix has never appeared on any public benchmark. Different robots, cameras, object sets, task definitions, initial-state distributions, and random seeds mean cross-paper comparison is mostly meaningless (see [Open problems](open-problems.md) §6).
- **Small-n, no stats.** PhAIL's survey of 13 real-robot VLA papers (2023–2025) found the modal per-condition sample size is 10–20 trials, and **none of the 13 reported confidence intervals or paired significance tests** (as of 2026-05). The one rigorous exception it identifies — TRI's LBM study (N=50 real / 200 sim per condition, paired exact tests) — sits outside those 13 "standard-practice" papers.
- **Saturation masks stagnation.** The ICLR 2026 VLA-research survey (Reuss) finds LIBERO/SIMPLER/CALVIN dominate paper evals and are "basically solved" — "showing 99% vs 98% is not very helpful"; the interesting failures (zero-shot, open-world) occur precisely where papers rarely evaluate.
- **Scores hide broken behavior.** LIBERO-Plus (2025-10) showed SOTA VLAs dropping from ~95% to below 30% under modest perturbations, with strongest sensitivity to camera viewpoint and robot initial state — and found many models **ignore the language instruction entirely**, succeeding by trajectory memorization.
- **Even harnesses disagree.** The vla-eval audit (2026-03) found well-documented benchmarks leave critical details implicit — overloaded termination flags, hidden action-normalization statistics — each a source of silent score distortion between reimplementations (single paper).
- **Sim-vs-real correlation is partial.** SimplerEnv established (~1,500 eval episodes each in sim and real) that carefully "visually matched" sim scores correlate strongly with real performance on Google Robot and WidowX setups — but only for those setups; real-to-sim generalization benchmarks (RobotArena ∞, REALM) are trying to extend this.
- **The crisis has gone mainstream (as of 2026-07).** Stephen Witt's New Yorker piece ("Are Humanoid Robots Ready to Be Deployed?", 2026-07-06 issue) relays that industrial roboticists see "no standardized benchmarks for progress" and that videos of remarkable feats are "often culled from hundreds of takes." Witt's firsthand demos match: 1X's fluid Neo kitchen demo was VR-tele-operated ("a marionette"), 1X declined to show autonomous operation at all, and a Skild-driven Unitree that handled an upright cup flailed when the cup was laid on its side — success rates measured on demonstrator-chosen configurations say little about the perturbed case.

## Major benchmarks compared

| Benchmark | What it measures | Embodiment | Sim/real | Status (as of 2026-07) |
|---|---|---|---|---|
| **LIBERO** (UT Austin, 2023) | 130 tabletop manipulation tasks; standard eval = 4×10-task suites (Spatial/Object/Goal/Long) | Franka (sim) | Sim (robosuite/MuJoCo) | **Saturated**: OpenVLA-OFT 97.1% avg; π0.5-LIBERO ~near-ceiling; now a sanity check |
| **LIBERO-Plus** (OpenMOSS/Fudan, 2025-10) | Robustness: 7 perturbation dimensions (layout, camera, robot init, language, light, background, noise), 21 sub-factors | Franka (sim) | Sim | Active; best reported avg ~81% (VLA-GSE, 2026-05) vs ~95% on vanilla LIBERO |
| **CALVIN** (2022) | Language-conditioned long-horizon chains (ABCD→D) | Franka (sim) | Sim | Near-saturated (ICLR 2026 survey) |
| **SimplerEnv / SIMPLER** (UCSD Hao Su lab + Google, 2024) | Real-to-sim replicas of Google Robot & WidowX/Bridge evals; visual-matching + variant aggregation | Google Robot, WidowX | Sim (proxy for real) | Widely used; top models cluster high; valuable mainly as cheap regression test |
| **RoboCasa365** (UT Austin/NVIDIA, ICLR 2026; arXiv 2026-03) | 365 household tasks, 2,500 kitchens, 3,200+ objects; multi-task, pretraining, lifelong learning; 2,200+ h demos, 500k+ trajectories | Mobile manipulators (sim) | Sim (RoboCasa/robosuite) | New, far from saturated; LeRobot-integrated |
| **BEHAVIOR-1K** (Stanford SVL, 2024→) | 1,000 long-horizon household activities (avg 6.6 min), bimanual + mobile; BDDL goal predicates | Mobile bimanual (sim) | Sim (OmniGibson on Isaac Sim) | Hard: NeurIPS 2025 challenge (50 tasks, 10k demos, 18 teams) won at ~26% q-score; 2026 challenge scales to 100 tasks / 20k demos (results due 2026-11) |
| **MolmoSpaces-Bench** (Ai2, 2026-02) | Generalist-policy generalization under controlled single-factor variation; 230k+ scenes, 130k+ objects, 42M grasps; simulator-agnostic (MuJoCo/Isaac/ManiSkill) | Manipulators + navigation (sim) | Sim (+ real-world validation studies) | New; NVIDIA claims GR00T N2 #1 (2026-03, company claim) |
| **RoboArena** (DROID consortium, 2025-06) | Crowd-sourced double-blind pairwise A/B of generalist policies; evaluators pick tasks/scenes freely; preference-aggregated ranking | Franka (DROID rig) | **Real**, 7+ institutions | Live leaderboard; 600+ pairwise episodes in launch paper; the closest thing to a Chatbot-Arena for robots |
| **AutoEval** (UC Berkeley, 2025) | 24/7 autonomous real-robot eval: learned success classifiers + reset policies; public job queue | WidowX (Bridge setup) | **Real** | Live; few stations/tasks, but near-zero human labor |
| **RoboChallenge Table30** (Dexmal + Hugging Face et al., 2025-10) | 30 tabletop tasks (insertion, food prep, tool use) run on operator-hosted real robots | UR5, Franka, ARX5, ALOHA | **Real** (remote, centralized) | 80,000+ real executions, 20+ models ranked; Table30 retires 2026-05-27, Table30 v2 announced |
| **GM-100 / "Great March 100"** (RHOS: SJTU/SII + Ant Group, 2026-01) | 100 detail-oriented tasks from human-object-interaction primitives; SR + partial-success + action error; 130+ demos/task/platform | Agilex Cobot Magic, Dobot Xtrainer (more planned) | **Real** | Brutally hard: best avg success ~17% (LingBot-VLA, self-reported); antidote to demo videos |
| **VLA-REPLICA** (2026-05) | Low-cost physical benchmark from off-the-shelf parts, designed for cross-lab replication | Small arm kit | **Real** (replicable) | New (unverified adoption) |
| **ERQA** (Google DeepMind, 2025-03) | 400 multiple-choice VQA items: spatial/trajectory/action/task reasoning, state estimation, pointing, multi-view | None (VLM exam) | Neither (image+text) | Active standard for "embodied reasoning"; ERQA-Plus diagnostic follow-up 2026-06 |
| **EIbench "Qiusuo"** (CESI, 2025-11) | State-backed embodied-intelligence evaluation, folded into China's HEIS 2026 standards framework | Multiple | Mixed | v1 released; paired CAICT industry benchmarking standard effective 2026-06-01 |

## Sim benchmarks: saturation and the robustness correction

- **LIBERO** became the field's default scorecard because it is cheap, scripted, and comparable — exactly the properties real robotics lacks. By 2025 the recipe papers (OpenVLA-OFT: 76.5%→97.1% via decoding changes alone) showed LIBERO scores measure fine-tuning recipe more than capability; frontier labs still quote it (π0.5-LIBERO checkpoint) as a sanity check.
- **The robustness wave** (2025-10→): LIBERO-Plus, LIBERO-PRO, and LIBERO-Para (paraphrase robustness, 2026-03) all perturb the saturated benchmark and report large drops — establishing that aggregate success rate on fixed scenes is a misleading statistic, not just a coarse one.
- **Scaling difficulty instead**: RoboCasa365 (365 tasks/2,500 kitchens) and BEHAVIOR-1K (1,000 activities, ~26% winning q-score at NeurIPS 2025) reintroduce headroom via task count, horizon, and mobility; MolmoSpaces-Bench reintroduces it via controlled-variable generalization sweeps. The-decoder's framing of BEHAVIOR-1K as robotics' would-be ImageNet is aspiration, not fact — sim-only long-horizon scores still lack demonstrated real-world correlation (see [Simulation](simulation.md)).
- **Real-to-sim eval** is the compromise track: SimplerEnv (validated correlation for two rigs), RobotArena ∞ (translate real videos into sim for OOD tests, 2025-10), REALM (2025-12). The open question is whether correlation holds for contact-rich and long-horizon tasks, where sim physics is weakest.

## Real-robot evaluation: three competing models

- **Federated arena (RoboArena).** Distributed evaluators at 7+ academic institutions run double-blind pairwise comparisons on DROID Franka rigs, choosing tasks freely; preference aggregation yields rankings that the launch paper (CoRL 2025) shows are more accurate and manipulation-resistant than centralized single-lab evals. Weakness: single embodiment class, academic throughput.
- **Centralized eval-as-a-service (RoboChallenge).** Upload a policy, a staffed lab executes it on real UR5/Franka/ARX5/ALOHA hardware under a fixed protocol — 80,000+ executions since 2025-10. Produced a notable transparency event: Spirit AI's **Spirit v1.5** topped the leaderboard and open-sourced weights + eval code (2026-01-12) explicitly so results could be independently verified. Weakness: single-site trust, cost, benchmark retirement churn (Table30 → v2, 2026-05).
- **Autonomous eval stations (AutoEval).** Berkeley's answer to eval labor: foundation-model success classifiers plus learned reset policies keep WidowX stations evaluating around the clock; results closely match human-run ground truth (paper claim). Weakness: only works for resettable tabletop tasks.
- **Hard task batteries (GM-100).** RHOS (SJTU/SII with Ant Group's xbench team) curates 100 detail-oriented tasks with fixed demos and a controlled protocol (one deployment used 25 robots and ~22,500 trials); best 2026 generalist VLAs average ~17% success / ~35% partial success — the most-cited sobering number against demo-video inflation (self-reported by model vendors on a third-party protocol).
- **Competition as eval:** the AGIBOT World Challenge 2026 (ICRA, 526 teams from 27 countries) moved final scoring from simulation to closed-loop real-robot testing — a symbolically important culture shift (see [Landscape: China](landscape-china.md)).

## Embodied-reasoning benchmarks (no robot required)

- **ERQA** (released with Gemini Robotics, 2025-03): 400 interleaved image+text MCQs spanning spatial/trajectory/action/task reasoning, state estimation, pointing, multi-view — tests the VLM layer of the stack, not motor control. Gemini Robotics-ER 1.5 claims top aggregate across 15 embodied-reasoning benchmarks incl. ERQA, Point-Bench, RefSpatial (company-reported).
- **ERQA-Plus** (2026-06): diagnostic decomposition of embodied reasoning failures (single paper, unverified adoption).
- **RoboBench** (2025-10): evaluates multimodal LLMs "as embodied brain" — planning, affordances, failure diagnosis (single paper).
- Caveat: high embodied-reasoning scores demonstrably do not transfer to control — the same reports that tout ERQA wins acknowledge fine-grained manipulation remains unsolved; treat these as prerequisite exams, not capability certificates.

## Industry metrics: throughput, interventions, nines

Deployed-robot operators mostly ignore academic success rates and track:

- **Throughput**: picks/totes/packages per hour or cycle time. Figure reported per-package cycle time falling 6.84 s → 4.31 s with more training data in logistics (company, 2025); Agility's Digit passed **100,000 totes moved** in ~16 months at GXO Flowery Branch (2025-11) — the largest disclosed humanoid work volume. Vendors do not publish picks-per-hour vs. the ~human baseline; analysts estimate current humanoids run well below human throughput (unverified).
- **Intervention rate / autonomy**: interventions per hour (or per task) times human cost is the ROI killer — e.g. at a 5% intervention rate with 30 s per fix, a $30/h supervisor adds ~$1.50/h per robot before maintenance (analyst arithmetic, unverified). Physical Intelligence's π*0.6 evals leaned on this framing: multi-hour uninterrupted runs (espresso service 5:30am–11:30pm, ~18 h) with throughput and success tracked over wall-clock time rather than trial batches (company-reported).
- **Reliability "nines"**: lab benchmarks stop at 95–99%; customers price 99% as failure — unattended operation implicitly requires 99.9%+ (see [Open problems](open-problems.md) §4). No humanoid vendor publishes MTBF, uptime, or intervention-rate data as of 2026-06; uptime disclosures are limited to charging ratios (Digit ~2:1 operate:charge, target 4:1+).
- The gap between these operational metrics and academic benchmarks is itself part of the crisis: no public benchmark yet scores long-duration autonomy, interventions, or degradation over hours — the dimensions purchasers actually buy (RoboChallenge's long-horizon tasks and PI's marathon runs are the nearest approximations).
- **Tele-operation is the undisclosed intervention channel (as of 2026-07).** Witt's New Yorker reporting documents remote humans behind nominally autonomous systems across the industry — Waymo's professional "pilots" in the Philippines, VR tele-stocking in Japanese 7-Elevens, 1X seating tele-operators beside its AI team (Neo's earpiece rings change color to disclose remote control; 1X de-emphasized teleop in marketing after customer pushback without abandoning it). Jim Fan (NVIDIA, late 2025, quoted in the piece): "Babysitting these robots demands an entire operation team. Mistakes are irreversible and unforgiving." No vendor reports teleop hours per autonomous hour — a disclosure gap sitting on top of the missing MTBF/intervention-rate data above.

## Who runs what (as of 2026-07)

| Leaderboard / benchmark | Steward | Type |
|---|---|---|
| LIBERO (+ community variants) | UT Austin (orig.); LIBERO-Plus by OpenMOSS/Fudan | Academic, self-run per paper |
| SimplerEnv | UCSD (Hao Su lab) + Google collaborators | Academic, self-run |
| RoboCasa365 | UT Austin + NVIDIA (Yuke Zhu); Hugging Face LeRobot distribution | Academic/corporate hybrid |
| BEHAVIOR-1K + annual challenge | Stanford SVL (Li Fei-Fei, Jiajun Wu) | Academic, NeurIPS challenge |
| MolmoSpaces-Bench | Ai2 (Allen Institute) | Nonprofit lab, open ecosystem |
| RoboArena leaderboard | DROID academic consortium (Berkeley/Stanford-led, 7+ universities) | Federated academic, live site |
| AutoEval stations | UC Berkeley RAIL | Academic, public queue |
| RoboChallenge (Table30 → v2) | Dexmal + Hugging Face et al. | Startup + community, live site |
| GM-100 | RHOS (SJTU/SII) + Ant Group xbench | Academic + corporate (CN) |
| ERQA | Google DeepMind | Corporate, open GitHub |
| EIbench "Qiusuo" | CESI under MIIT (China) | State standards body |

## Will 2026 converge?

- **Forces for convergence:** RoboArena's federation is growing and vendor-cited (NVIDIA quoted RoboArena and MolmoSpaces ranks for GR00T N2, 2026-03 — the first time a frontier vendor marketed third-party robot-benchmark placement); Hugging Face is wiring LeRobot into RoboCasa365 and RoboChallenge, giving open models a default scoreboard; China is standardizing top-down (EIbench v1 2025-11; CAICT-led embodied-AI benchmarking industry standard, 40+ drafting institutions, effective 2026-06-01), which could make a state benchmark the de facto gate for the world's largest robot market (see [Safety & regulation](safety-regulation.md)).
- **Forces against:** embodiment fragmentation (a Franka-arena rank says little about a [humanoid](humanoid-robots.md)); frontier labs' best models are closed and absent from public leaderboards (Helix, Gemini Robotics VLA, π0.6/0.7 as of 2026-07); benchmark churn (Table30 retired after ~7 months); and the structural incentive to report the benchmark you win.
- **Realistic 2026 endstate:** a portfolio, not a standard — saturated sim suites as regression tests, one or two live real-robot arenas for generalist rankings, hard task batteries (GM-100, BEHAVIOR) for headroom, and operational metrics (throughput/interventions/nines) as the commercial ground truth. The "ImageNet moment" has not happened (drafted here as the consensus view; no primary source claims otherwise).

## Sources

- https://arxiv.org/abs/2510.13626 — LIBERO-Plus: 7 perturbation dimensions, 95%→<30% drops, language-ignoring finding
- https://mbreuss.github.io/blog_post_iclr_26_vla.html — ICLR 2026 VLA survey: LIBERO/SIMPLER/CALVIN dominance and saturation quotes
- https://openvla-oft.github.io/ — OpenVLA-OFT 76.5%→97.1% LIBERO; recipe-vs-capability evidence
- https://arxiv.org/pdf/2405.05941 — SIMPLER/SimplerEnv: ~1,500 eval episodes each in sim and real, visual-matching correlation
- https://arxiv.org/abs/2506.18123 — RoboArena paper (CoRL 2025): DROID, 7 institutions, 600+ double-blind pairwise episodes
- https://robo-arena.github.io/ — RoboArena live leaderboard site
- https://arxiv.org/abs/2503.24278 — AutoEval: autonomous 24/7 real-robot eval, WidowX stations, public queue
- https://arxiv.org/abs/2510.17950 — RoboChallenge tech report: Table30, UR5/Franka/ARX5/ALOHA, centralized real-robot eval
- https://robochallenge.ai/news — 80,000+ executions, 20+ models, Table30 retirement 2026-05-27, Table30 v2
- https://www.prnewswire.com/news-releases/robochallenges-top-ranked-embodied-ai-model-goes-open-source-challenging-clean-data-collection-paradigm-302658247.html — Spirit AI's Spirit v1.5 #1 on RoboChallenge, open-sourced 2026-01-12
- https://arxiv.org/html/2601.11421v1 — GM-100 paper: 100 tasks, RHOS/SJTU/SII/Ant Group, platforms, SR/PSR metrics
- https://www.rhos.ai/research/gm-100 — GM-100 site: 130+ demos per task, leaderboard, platform roadmap
- https://www.marktechpost.com/2026/01/29/ant-group-releases-lingbot-vla-a-vision-language-action-foundation-model-for-real-world-robot-manipulation/ — LingBot-VLA GM-100 scores (~17.30% SR / 35.41% PSR), 130 demos/task on each of 3 platforms
- https://arxiv.org/abs/2601.18692 — LingBot-VLA paper: 25 robots across 4 commercial platforms, 22,500-trial controlled protocol vs π0.5/GR00T N1.6/WALL-OSS
- https://arxiv.org/abs/2605.06175 — VLA-GSE: 81.2% avg zero-shot on LIBERO-Plus (best reported, 2026-05)
- https://arxiv.org/abs/2603.04356 — RoboCasa365 (ICLR 2026): 365 tasks, 2,500 kitchens, 2,200+ h demos
- https://arxiv.org/abs/2403.09227 — BEHAVIOR-1K: 1,000 activities, OmniGibson
- https://behavior.stanford.edu/challenge/index.html — BEHAVIOR Challenge page (now shows 2026 edition: 100 tasks, 20k demos; 2025 edition in archive)
- https://robot-learning-collective.github.io/winning-behavior-1k-challenge.html — winning solution ~26% q-score, 18 teams
- https://the-decoder.com/behavior-1k-is-set-to-become-for-robotics-what-imagenet-was-for-computer-vision/ — "ImageNet for robotics" framing (aspirational)
- https://allenai.org/blog/molmospaces — MolmoSpaces ecosystem: 230k scenes, 130k objects, 42M grasps, MolmoSpaces-Bench
- https://arxiv.org/html/2602.11337v2 — MolmoSpaces paper: simulator-agnostic bench, controlled variation
- https://github.com/embodiedreasoning/ERQA — ERQA: 400 MCQs, categories, DeepMind release
- https://arxiv.org/html/2606.17639v1 — ERQA-Plus diagnostic benchmark (2026-06)
- https://deepmind.google/blog/gemini-robotics-15-brings-ai-agents-into-the-physical-world/ — ER 1.5 claimed SOTA on 15 embodied-reasoning benchmarks
- https://arxiv.org/abs/2605.20774 — VLA-REPLICA: low-cost replicable real-world benchmark
- https://arxiv.org/pdf/2605.29710 — PhAIL: 13-paper survey (modal n=10–20, zero CIs), distributional methodology
- https://arxiv.org/html/2603.13966v1 — vla-eval harness: hidden normalization/termination pitfalls, config-pinned reproducibility
- https://arxiv.org/html/2510.23571v1 — RobotArena ∞: real-to-sim translation benchmarking
- https://nvidianews.nvidia.com/news/nvidia-and-global-robotics-leaders-take-physical-ai-to-the-real-world — NVIDIA GR00T N2 #1 claims on MolmoSpaces + RoboArena (2026-03, company claim)
- https://sesec.eu/2026/04/01/chinas-first-standards-system-for-humanoid-robots-and-embodied-intelligence/ — EIbench "Qiusuo" (CESI, 2025-11) within HEIS 2026 framework
- https://news.cgtn.com/news/2026-03-27/China-releases-first-industry-standard-for-embodied-intelligence-1LQAZmMXmtW/p.html — CAICT-led embodied-AI benchmarking industry standard, effective 2026-06-01
- https://roboticsandautomationnews.com/2025/11/24/agility-robotics-digit-humanoid-passes-100000-tote-milestone-in-live-gxo-implementation/96877/ — Digit 100,000-tote milestone at GXO (2025-11)
- https://www.figure.ai/news/scaling-helix-logistics — Figure logistics cycle-time metrics (6.84→4.31 s/package)
- https://blog.robozaps.com/b/roi-of-humanoid-robots — intervention-rate cost arithmetic, throughput-vs-human estimates (analyst, unverified)
- https://www.pi.website/blog/pistar06 — π*0.6 marathon-run evaluation style (multi-hour throughput/success tracking)
- https://www.globenewswire.com/news-release/2026/05/13/3293715/0/en/Global-Showdown-526-Teams-from-27-Countries-Compete-in-the-AGIBOT-WORLD-CHALLENGE-ICRA-2026-Online-Round.html — AGIBOT World Challenge scale; real-robot final scoring shift
- https://www.newyorker.com/magazine/2026/07/06/are-humanoid-robots-ready-to-be-deployed — Stephen Witt (2026-07-06 issue): "no standardized benchmarks" / hundreds-of-takes demo videos, tele-operated 1X Neo demo, teleop-behind-autonomy pattern, Jim Fan babysitting quote (paywalled; read in full via Wayback snapshot 2026-07-03)
