---
title: The Robot Data Problem
slug: data
updated: 2026-07-04
confidence: verified
---
> Robotics has no internet-scale corpus: LLMs train on trillions of web tokens, but robot actions must be manufactured — via teleoperation, handheld capture rigs, egocentric human video, or simulation. As of 2026-07 the field's largest open real-robot datasets sit at ~1–2M episodes (Open X-Embodiment, AgiBot World) while the largest disclosed proprietary corpus is Generalist AI's 270,000+ hours (growing ~10k h/week as of 2025-11). 2025–2026 produced the first credible scaling-law evidence for robot data — power laws in environment/object diversity (ICLR 2025), in raw pretraining hours (GEN-0), and in egocentric human video (NVIDIA EgoScale) — which triggered a capital race to build "data factories": Figure×Brookfield, Apptronik's Robot Park, Scale AI's Physical AI Data Engine, and 40+ state-backed collection centers in China.

## Why data is the bottleneck

- Language and vision models bootstrap from a free, passively accumulated internet corpus; there is no equivalent "internet of robot actions." Robot trajectories (synchronized video + proprioception + actions) must be deliberately produced, at marginal cost per hour.
- ~4M industrial robots are in operation worldwide (IFR stock estimate), yet almost none log training-usable data — the hardware exists, the data does not.
- The consensus framing (popularized by NVIDIA's GR00T "data pyramid") is a three-layer mix: **web & human video** (huge, actionless) → **synthetic/simulation data** (cheap, sim-to-real gap) → **real robot teleoperation** (gold-standard action labels, expensive and slow). Frontier labs now co-train on all three; see [VLA models](vla-models.md) and [World models](world-models.md).
- Cost anchor: high-quality teleoperation data reportedly fell from ~$340/hour (early 2024) to ~$136/hour (Q4 2025) as rigs and pipelines matured (unverified, single industry-report source).
- Data strategy is now a primary competitive axis between labs — arguably more than architecture; see [State of the art](state-of-the-art.md) and [Investment](investment.md).

## Collection method trade-offs

| Method | Action labels | Throughput / cost | Weakness | Exemplars |
|---|---|---|---|---|
| Robot teleoperation (leader-follower, VR) | Exact robot actions | ~35 demos/h per operator; rigs $20–30k (ALOHA-class) | Slow, operator-bound, embodiment-locked | ALOHA/ALOHA 2, Mobile ALOHA, DROID (Quest 2), AgiBot World |
| Handheld/portable capture | End-effector pose + gripper (SLAM-recovered) | ~111 demos/h (~3× teleop, UMI) | No force sensing; retargeting to arm needed | UMI, FastUMI, DexUMI, ActiveUMI |
| Egocentric human video (instrumented) | Hand pose only (retargeted) | Passive, wearable; scales with workforce | Embodiment gap (hands ≠ grippers), no action labels | EgoDex (Vision Pro), EgoMimic (Aria), Tesla camera rigs, Figure Go-Big |
| Web/human video (uninstrumented) | None (pseudo-labeled) | Effectively free, internet-scale | Weakest supervision; viewpoint/embodiment mismatch | Ego4D, YouTube pretraining in GR00T/Helix pipelines |
| Simulation / synthetic | Perfect ground truth | 780k trajectories in 11 h (DexMimicGen on Isaac) | Sim-to-real gap, asset/scene diversity limits | MimicGen, DexMimicGen, Isaac Lab; see [Simulation](simulation.md) |
| Neural-generated ("dreams") | Pseudo-actions from video models | GPU-bound, no physics rig at all | Hallucinated physics, needs filtering | NVIDIA DreamGen, GigaBrain-0; see [World models](world-models.md) |

## Teleoperation and handheld capture

- **ALOHA / ALOHA 2 / Mobile ALOHA** (Stanford/Google DeepMind, 2023–2024): open-source bimanual leader-follower rigs at roughly $20–30k per station; became the de-facto academic standard and the template for Chinese data-center rigs. Mobile ALOHA showed co-training mobile-manipulation data with static ALOHA datasets lifts task success by up to ~90 points on some tasks (paper claim).
- **UMI (Universal Manipulation Interface)** (Stanford/Columbia, 2024): handheld gripper + wrist GoPro fisheye; SLAM recovers end-effector trajectories, so no robot is needed at collection time. ~30 s/demonstration (~111 demos/h vs ~35/h for teleop); policies transferred zero-shot across UR5e and Franka arms. Spawned a large follow-up family (FastUMI, DexUMI for dexterous hands, ActiveUMI) through 2025–2026.
- **VR teleoperation** is standard for whole-body humanoids: Quest/Vision Pro headsets plus motion retargeting (used by DROID, AgiBot, Chinese training centers, and most [humanoid](humanoid-robots.md) companies). Apple Vision Pro's on-device hand tracking also powers EgoDex-style human-only capture.
- Ergonomics/economics rule of thumb (as of 2026): one skilled teleoperator produces roughly 20–50 usable episodes/hour; national-scale efforts therefore employ hundreds of full-time "data collectors" repeating tasks hundreds of times per day (documented in Chinese centers; Rest of World, 2026).
- **The AV precedent — teleop as training data**: Waymo used **500,000+ hours of real-world driving data** in its 2025 scaling-law study (Waymo's own blog, 2025-06; Witt's New Yorker piece cites the same "at least half a million hours" powering its driving model), and its remote human "pilots" (teleoperators working from the Philippines) double as a training-data source. 1X runs the identical flywheel in homes: teleop "Expert Mode" sessions feed model training — "It's also useful data for us" (CEO Bernt Børnich, per Witt) — see [Data foundry](data-foundry.md) and [Open problems](open-problems.md).

## Egocentric human video

- Thesis: humans are the cheapest "robots" — record first-person video of people doing tasks, then bridge the embodiment gap with retargeting or co-training. 2025–2026 moved this from research idea to primary strategy at several labs.
- **EgoDex** (Apple, 2025-05): 829 hours of Vision Pro egocentric video with paired 3D hand/finger joint tracking, 194 tabletop tasks — the largest dexterous manipulation dataset at release (paper claim).
- **Ego4D** (Meta): ~3,670 hours of general egocentric daily activity; a perception backbone staple but not manipulation-labeled. **EgoMimic** (Georgia Tech, 2024) used Project Aria glasses to co-train human + robot data, reporting 34–228% task-performance gains over robot-only data.
- **NVIDIA EgoScale / GR00T N1.7** (early access 2026-04): pretrained on 20,854 hours of egocentric human video across 20+ task categories; NVIDIA reports a log-linear scaling law for dexterity — scaling 1k→20k hours more than doubles average task completion — with dexterous-hand tasks (syringe handling, card sorting, shirt folding) learned primarily from human video, no robot in the loop (company claim).
- **Figure "Project Go-Big"** (announced 2025-09): partnership with Brookfield (100,000+ residential units, 500M sq ft offices, 160M sq ft logistics) to passively collect egocentric human video in real homes; Figure reported Helix navigated cluttered homes from language commands after training on 100% egocentric human video — zero-shot human-to-robot transfer (company claim); see [Humanoid robots](humanoid-robots.md).
- **Tesla Optimus** pivoted mid-2025 from mocap suits/teleoperation to a vision-only strategy: workers wear helmet-and-backpack rigs with five cameras recording everyday tasks, mirroring the FSD camera-first playbook (reported after Ashok Elluswamy took over the program, 2025-06).
- **Neura Robotics (Germany)** runs the mocap-suit variant at industrial scale: **1,000+ industrial workers in motion-capture suits** generating humanoid training data (per Witt, New Yorker 2026-07-06 issue; company program, scale not independently verified). CEO David Reger frames it as data collection, not job replacement: "We're getting, like, a lot of data." Witt's ceiling estimate for the whole approach: "Even if the entire population of Earth donned motion-capture suits, it would take decades to generate the amount of data that was used to train ChatGPT" — whole-population mocap still doesn't reach LLM-corpus scale, which is why labs stack it with video and simulation.
- Open question: human video lacks robot action labels and force signals; competing bridges include latent-action models (GO-1, GR00T), hand-to-gripper retargeting, and co-training. One reported result: 1 hour of Aria human data contributed more than 1 extra hour of teleop data in a co-training setup (unverified, single source).

## Simulation and neural-generated data

- **MimicGen / DexMimicGen** (NVIDIA): automatically expand a handful of human demos into large sim datasets; DexMimicGen generated 780,000 trajectories (~6,500 h human-equivalent) in 11 hours on Isaac Sim for GR00T N1 training.
- **DreamGen / GR00T-Dreams** (2025): video world models generate "neural trajectories" — photorealistic rollouts of tasks the robot never performed — then pseudo-label actions; NVIDIA reports ~40% performance improvement when mixed with real data (unverified company/blog claim). See [World models](world-models.md).
- Sim data dominates [locomotion](locomotion.md) (RL in Isaac Gym–class simulators needs no demonstrations) but remains a co-training supplement, not a replacement, for contact-rich manipulation — the sim-to-real gap is covered in [Simulation](simulation.md) and [Open problems](open-problems.md).

## Open datasets

| Dataset | Scale | Embodiments | Notes |
|---|---|---|---|
| **Open X-Embodiment (OXE)** (2023, growing) | 1M+ real trajectories, 500+ skills, 160k+ task variants | 22 robot types | Pooled from 60 prior datasets by a 21-institution collaboration; RLDS format; the default VLA pretraining corpus but quality/format is highly heterogeneous |
| **DROID** (2024) | 76k teleop trajectories, 350 h, 564 scenes, 86 tasks | Franka Panda (single standardized rig) | 13 institutions, 50 collectors, 12 months; calibrated stereo, 1,417 viewpoints; diversity-per-episode benchmark |
| **AgiBot World** (2024-12 α, 2025 β) | >1M trajectories, 2,976.4 h, 217 tasks, 3,000+ objects | 100 homogeneous dual-arm AgiBot G1 humanoid robots | Collected at AgiBot's ~4,000 m² Lingang (Shanghai) facility (figures per arXiv:2503.06669 + Hugging Face dataset card); paper reports policies pretrained on it beat OXE-pretrained by ~30% in- and out-of-distribution; basis of GO-1 latent-action model; IROS 2025 Best Paper finalist |
| **RoboMIND** (2024-12) | 107k trajectories, 479 tasks, 96 object classes | 4 embodiments incl. Tien Kung humanoid | Beijing X-Humanoid center; unified platform, includes failure trajectories |
| **RoboMIND 2.0** (2025-12) | 310k dual-arm trajectories, 1,000+ h, 12k tactile-enriched, 20k mobile-manipulation | 6 heterogeneous embodiments | Adds tactile and mobile-manipulation modalities (paper claim) |
| **EgoDex** (Apple, 2025-05) | 829 h egocentric video + 3D hand tracking, 194 tasks | Human hands (Vision Pro) | Largest dexterous human-manipulation set at release |
| **AIRoA release** (Japan, announced 2026-02) | ~10,000 h real-robot multimodal data (RGB-D, F/T, language) | Mobile manipulators (Toyota HSR evaluation) | Released in LeRobot format with a global VLA-pipeline competition at ICRA 2026-06 |
- Hugging Face **LeRobot** has become the community-standard data format/tooling layer (as of 2026); NVIDIA's Physical AI Open Datasets on HF report 4.8M+ downloads (unverified).
- China's ecosystem (AgiBot World, RoboMIND, Kylin training-ground outputs) now rivals or exceeds US open releases in raw episode count — see [Landscape: China](landscape-china.md).

## Commercial data factories

- **Generalist AI** (as of 2025-11): 270,000+ hours of real-world manipulation data, growing ~10,000 h/week via multiple contracted "data foundry" partners across thousands of homes/warehouses; raised $400M at a ~$2B valuation (announced 2026-06; Radical Ventures-led, total raised >$500M) to scale its GEN-0 models and data engine; see [Organizations](organizations.md).
- **Scale AI Physical AI Data Engine** (expanded 2025-09): 100,000+ production hours logged at its San Francisco robotics lab plus global contributors; named clients include Physical Intelligence, Generalist AI, and Cobot; 2026-03 partnership (announced at GTC) embeds the engine in Universal Robots' UR AI Trainer leader-follower kit (100k+ installed industrial arms as a collection fleet).
- **Apptronik Robot Park** (announced 2026-06-30): 90,000 sq ft humanoid data factory in Austin — Apollo 2 fleets doing logistics/manufacturing/retail work under mixed teleoperation + autonomy, feeding Google DeepMind's Gemini Robotics models; satellite collection sites at Mercedes-Benz and GXO.
- **Figure × Brookfield** (2025-09): real-estate-portfolio-as-dataset — passive egocentric human video capture across 100k+ residential units (see above).
- **China's state-backed centers**: 40+ government-linked data collection centers announced by 2025-12, ~two dozen operational by early 2026 (Rest of World). Flagships: Shanghai's Kylin training ground (National-Local Co-built Humanoid Robotics Innovation Center + Zhangjiang Group; ~4,600–5,000 m² per state media, 100+ heterogeneous humanoid robots training simultaneously, opened 2025-01) and Beijing Shijingshan (10,000+ m², co-built with Leju Robotics; 16 staged scenarios across 4 categories). UBTech sold ¥566M (~$80M) of humanoids to three provincial data centers (as of 2025); workers repeat single actions up to ~600×/day.
- **Tesla**: fully in-house; camera-rig human-video capture at scale plus Optimus fleet data (as of 2025-06 strategy shift).
- Contrast in philosophy: US labs increasingly bet on human video + customer-site fleet data; China bets on subsidized centralized teleoperation halls. Both are converging on hybrid pyramids.

## Cross-embodiment transfer

- **RT-X** (2023) was the proof of concept: training one model on OXE's 22 embodiments produced positive transfer — RT-1-X beat specialist models by ~50% on underrepresented-lab benchmarks and RT-2-X roughly tripled success on emergent-skill evaluations vs RT-2 (paper claims).
- **π0 / π0.5** (Physical Intelligence): π0.5's mixture combines ~400 h of mobile-manipulation demos with multi-environment static-robot data, diverse cross-embodiment lab data, high-level language subtask data, and web VQA/captioning — an explicit "curriculum" for open-world generalization in unseen homes (as of 2025-04). See [VLA models](vla-models.md).
- **GR00T N1/N1.5/N1.7** and **GEN-0** train across heterogeneous embodiments (GEN-0 evaluated on 6-DoF, 7-DoF, and 16+DoF semi-humanoid platforms).
- Caveats: naive pooling can produce negative transfer — OXE's inconsistent viewpoints, action spaces, and quality are a known drag, and AgiBot's ~30% advantage over OXE pretraining is evidence that curated homogeneous data can beat larger heterogeneous corpora (single-team claim). Action-space unification (latent actions, end-effector canonicalization, augmentation efforts like OXE-AugE) is an active 2026 research front.

## Scaling-law evidence

| Study | Axis scaled | Reported law | Caveat |
|---|---|---|---|
| **Data Scaling Laws in Imitation Learning** (Tsinghua et al., ICLR 2025 oral; 40k+ demos, 15k+ rollouts) | # environments & objects | Power law in environment/object diversity; demos-per-environment saturate (~threshold, then flat); ~90% success on novel-environment tasks from 1 afternoon × 4 collectors | Single-task policies, 2 robots, manipulation only |
| **GEN-0** (Generalist AI, 2025-11) | Pretraining hours (270k h) | L(D) = (D_c/D)^α power law on downstream error; "ossification" below ~7B params — bigger models absorb data better | Company technical blog, not peer-reviewed |
| **NVIDIA EgoScale / GR00T N1.7** (2026-04) | Egocentric human-video hours (20,854 h) | Log-linear dexterity scaling; 1k→20k h more than doubles avg task completion | Company claim, early-access model |
| **Mobile ALOHA co-training** (2024) | Cross-task co-training | Up to +90 pts success from co-training with existing static data | Small-scale, task-specific |
- Interpretation (as of 2026-07): evidence now supports "more and more-diverse data predictably helps," with **diversity of environments/objects mattering more than raw episode count** at small scale, and raw hours mattering at foundation-model scale. There is still no agreed compute-optimal "Chinchilla for robotics" — data mixture ratios (real : human-video : sim) remain empirical lab lore; see [Open problems](open-problems.md).

## Open questions

- What ratio of real teleop : human video : synthetic data is compute/dollar-optimal? Every lab reports a different mixture; none publish full ablations.
- Do egocentric-video scaling laws (EgoScale, Go-Big) hold through contact-rich, force-dependent tasks where video carries no haptic signal? Tactile-enriched sets (RoboMIND 2.0) are an early response.
- Will open corpora keep pace? The proprietary–open gap widened in 2025–2026: Generalist's 270k h dwarfs all open datasets combined; open releases (AgiBot World, AIRoA) are the counterweight.
- Evaluation lags collection: most dataset papers self-report success rates on in-house tasks; standardized cross-lab benchmarks remain thin (see [State of the art](state-of-the-art.md)).

## Sources
- https://arxiv.org/abs/2410.18647 — Data Scaling Laws in Imitation Learning (ICLR 2025 oral): power law in environments/objects, 40k demos, ~90% novel-environment success.
- https://generalistai.com/blog/nov-04-2025-GEN-0 — GEN-0: 270k+ h corpus, +10k h/week, L(D) power law, 7B ossification threshold, data foundry partners.
- https://www.therobotreport.com/generalist-raises-400m-to-scale-its-general-purpose-ai-models/ — Generalist $400M raise (announced 2026-06).
- https://www.bloomberg.com/news/articles/2026-06-04/nvidia-backed-robotics-startup-generalist-ai-valued-at-2-billion — Generalist $400M round at ~$2B valuation, 2026-06-04, Radical Ventures-led, total >$500M.
- https://iclr.cc/virtual/2025/oral/31769 — ICLR 2025 oral listing for Data Scaling Laws in Imitation Learning (confirms oral status).
- https://umi-gripper.github.io/ — UMI: handheld gripper, ~30 s/demo (~111 demos/h vs 35/h teleop), cross-platform zero-shot deployment.
- https://proceedings.mlr.press/v270/fu25b — Mobile ALOHA: whole-body teleop rig, co-training gains up to 90 pts.
- https://droid-dataset.github.io/ — DROID: 76k trajectories, 350 h, 564 scenes, 86 tasks, 13 institutions, Franka Panda + Quest 2.
- https://arxiv.org/html/2503.06669v4 — AgiBot World Colosseo: >1M trajectories, 217 tasks, 100 dual-arm humanoid robots, ~4,000 m² Lingang facility, +30% vs OXE pretraining, GO-1.
- https://huggingface.co/datasets/agibot-world/AgiBotWorld-Beta — AgiBot World Beta dataset card: 2,976.4 hours, >1M trajectories.
- https://arxiv.org/abs/2412.13877 — RoboMIND: 107k trajectories, 479 tasks, 96 object classes, multi-embodiment teleop benchmark.
- https://arxiv.org/abs/2512.24653 — RoboMIND 2.0: 310k dual-arm trajectories, 6 embodiments, 1,000+ h, tactile + mobile manipulation.
- https://machinelearning.apple.com/research/egodex-learning-dexterous-manipulation — EgoDex: 829 h Vision Pro egocentric video, 194 tasks.
- https://ai.meta.com/blog/egomimic-project-aria-georgia-tech-ego4d-robotics-embodied-ai/ — EgoMimic/Project Aria human-robot co-training; Ego4D context.
- https://www.figure.ai/news/project-go-big — Project Go-Big: Brookfield partnership scale (100k+ homes), Helix zero-shot navigation from 100% human video (2025-09).
- https://huggingface.co/blog/nvidia/gr00t-n1-7 — GR00T N1.7: 20,854 h egocentric pretraining (EgoScale), log-linear dexterity scaling, 1k→20k h doubles completion (2026-04).
- https://arxiv.org/pdf/2503.14734 — GR00T N1: data-pyramid training corpus, MimicGen/DexMimicGen synthetic data, neural trajectories.
- https://developer.nvidia.com/blog/building-a-synthetic-motion-generation-pipeline-for-humanoid-robot-learning/ — Isaac/DexMimicGen: 780k sim trajectories (~6,500 h equivalent) in 11 h.
- https://www.eweek.com/news/tesla-optimus-robot-training/ — Tesla 2025 pivot to vision-only camera-rig human data collection; Optimus leadership change.
- https://scale.com/blog/physical-ai — Scale AI Physical AI Data Engine: 100k+ production hours, collection + annotation stack.
- https://www.universal-robots.com/news-and-media/news-center/universal-robots-scale-ai-launch-imitation-learning-system-accelerate-ai-training-lab-to-factory/ — Scale × Universal Robots UR AI Trainer partnership.
- https://www.forbes.com/sites/johnkoetsier/2026/06/30/apptronik-announces-robot-park-a-90000-square-foot-humanoid-data-factory-teases-new-robot/ — Apptronik Robot Park: 90,000 sq ft Austin data factory, Apollo 3 (2027), DeepMind/Mercedes/GXO sites.
- https://restofworld.org/2026/china-robots-training-centers-workers/ — China: 40+ announced state data centers, ~two dozen operational, worker practices, UBTech ¥566M sales.
- https://www.chinadaily.com.cn/a/202501/23/WS67919d43a310a2ab06ea8c2e.html — Shanghai Kylin humanoid training ground opening (2025-01), 4,600 m², 100+ robots training simultaneously.
- https://english.news.cn/20250122/8da44371af8342ca84ee505914fd5fa6/c.html — Xinhua on Kylin: 5,000+ m², 100+ humanoid robots in initial phase, launched 2025-01-21.
- https://english.beijing.gov.cn/latest/news/202510/t20251009_4216190.html — Beijing Shijingshan center: 10,000+ m², largest in China, 16 scenarios in 4 categories, co-built with Leju Robotics.
- https://www.airoa.org/updates/20260210/208/ — AIRoA ~10,000 h mobile-manipulator data release (RGB-D, F/T, language; LeRobot format) + ICRA 2026 VLA-pipeline competition, Toyota HSR evaluation.
- https://www.pi.website/blog/pi05 — π0.5 training mixture: ~400 h mobile manipulation + multi-environment + cross-embodiment + web data.
- https://robotics-transformer-x.github.io/ — Open X-Embodiment/RT-X: 1M+ trajectories, 22 embodiments, positive-transfer results.
- https://www.roboticscenter.ai/state-of-robotics-2026 — industry-report figures: teleop cost decline ($340→$136/h), LeRobot/NVIDIA dataset adoption (secondary source; marked unverified where used).
- https://www.newyorker.com/magazine/2026/07/06/are-humanoid-robots-ready-to-be-deployed — Witt: Neura's 1,000+ mocap-suited workers (Reger quotes), whole-population-mocap ceiling framing, Waymo teleop pilots as data source, 1X Expert-Mode-as-data quote (read via Wayback snapshot).
- https://waymo.com/blog/2025/06/scaling-laws-in-autonomous-driving/ — Waymo scaling-law study on 500,000 h of real-world driving data (primary; corroborates Witt's "half a million hours").
