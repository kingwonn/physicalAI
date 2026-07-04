---
title: "Company Deep Dive: NVIDIA Robotics Stack"
slug: company-nvidia
updated: 2026-07-04
confidence: verified
---
> NVIDIA is the platform vendor of Physical AI — the "sell picks and shovels to every robot maker" play, executed as a **three-computer thesis**: train on DGX, simulate on Omniverse/Cosmos (OVX/RTX PRO servers), act on Jetson. Around that skeleton it has built the deepest stack in the field: Isaac Sim/Lab simulation (open-sourced 2025), the Newton physics engine (Linux Foundation, 1.0 GA at GTC 2026), the open GR00T robot-foundation-model line (N1 2025-03 → N1.7 early access 2026-04 → N2/DreamZero GA slated late 2026), the Cosmos world-model family (1 → 3, 2025-01 → 2026-06), Jetson Thor onboard compute (GA 2025-08), and the Halos safety platform extended from AVs to humanoids (2026-06). It invests in its own customers (Figure, Skild, Neura), and CEO Jensen Huang frames humanoids as a ~$40T labor-automation TAM. The tension: NVIDIA's disclosed automotive-and-robotics revenue was ~$2.3B of a $215.9B FY2026 (~1%), robotics-specific revenue is not broken out at all, and its largest robot-making customers (Tesla, Figure) are actively developing non-NVIDIA onboard silicon. Context: [Simulation](simulation.md), [World models](world-models.md), [Hardware](hardware.md), [VLA models](vla-models.md), [Landscape: USA](landscape-usa.md), [Investment](investment.md).

## The platform thesis: three computers, picks and shovels

- **Three-computer architecture** (NVIDIA's own framing, canonical since late 2024): (1) **DGX/HGX** AI supercomputers to *train* robot foundation models; (2) **Omniverse + Cosmos on OVX / RTX PRO servers** to *simulate, test, and generate synthetic data* (Isaac Sim, Isaac Lab, digital twins); (3) **Jetson AGX Thor** (robots) / DRIVE AGX Thor (vehicles) to *act* — on-robot inference. All three run Blackwell-generation silicon, so every layer of a customer's robotics program monetizes NVIDIA hardware.
- Strategic logic: NVIDIA does not sell robots; it aims to be the **"CUDA of robotics"** — the substrate every robot maker standardizes on, capturing value regardless of which robot company wins. Press shorthand: the "Android of generalist robotics" (TechCrunch, 2026-01) — open(-ish) models seeding demand for closed, high-margin compute.
- The model layer is deliberately **open-weight** (GR00T under NVIDIA Open Model License, Cosmos permissively licensed) while the money layer (GPUs, Jetson) is proprietary — the inverse of vertically integrated players like [Figure](company-figure.md) (closed model, own robot) or Tesla.
- Supporting glue: **OSMO** (workflow orchestration across the three computers), **Metropolis** (vision AI for factories), **Mega** Omniverse Blueprint (factory-scale digital twins with Siemens), **Isaac ROS** (GPU-accelerated ROS 2 packages).
- Scale claims (NVIDIA, GTC 2026-03): **~2M robotics developers** on its platforms; 40,000+ Inception startups; Hugging Face partnership connecting to 13M AI builders — robotics is the fastest-growing category on Hugging Face, with NVIDIA models leading downloads (as of 2026-01).
- **Independent field corroboration of the moat (as of 2026-07)**: Stephen Witt, after touring 1X, Skild, Caltech and others for the New Yorker (2026-07-06 issue): "Every single robot I encountered while reporting this article ran on an Nvidia microchip, and every single one had trained in an Nvidia digital gym." Same piece relays a former employee's characterization that NVIDIA deliberately built "vender lock" — making robot makers dependent on its stack — the strongest third-party (non-vendor) statement of NVIDIA ubiquity on record, though scoped to the robots one reporter happened to see.

## Simulation layer: Isaac Sim, Isaac Lab, Newton, Arena

Detailed treatment in [Simulation](simulation.md); the NVIDIA-specific spine:

- **Isaac Sim 5.0 + Isaac Lab 2.2** open-sourced on GitHub (GA at SIGGRAPH 2025-08) — full robotics sim on Omniverse/OpenUSD with RTX sensor simulation and synthetic-data pipelines (Replicator, MimicGen→SkillGen trajectory multiplication).
- **Isaac Lab 2.3** (2025-09): automatic domain randomization, population-based training (runs to 40,960 parallel envs), dexterous teleop; **Isaac Lab Arena** policy-evaluation framework co-developed with Lightwheel. **Isaac Lab 3.0** early access at GTC 2026-03 — pitched as large-scale robot learning on DGX infrastructure.
- **Newton physics engine**: co-developed with Google DeepMind and Disney Research, contributed to the Linux Foundation (2025-09), **1.0 GA at GTC 2026-03** with MuJoCo-Warp solver, deformables, and Disney's Kamino solver (used to train Disney's BDX droids). Governance concession that mitigates the lock-in critique at the physics layer.
- **GR00T Blueprint / GR00T-Dreams**: synthetic-data generation — NVIDIA claims 780,000 trajectories (≈9 months of human demonstration) generated in 11 hours at N1 launch (vendor claim, 2025-03); DreamGen "neural trajectories" bridge into the [world-model](world-models.md) data engine.

## Model layer: the GR00T line

Full lineage and architecture in [VLA models](vla-models.md). "Project GR00T" was announced at GTC 2024-03 alongside the Jetson Thor announcement; status as of 2026-07:

| Model | Date | Status | Key point |
|---|---|---|---|
| GR00T N1 | 2025-03-18 (GTC) | open weights | Billed as first open humanoid foundation model; ~2B params, dual-system (Eagle-2 VLM + DiT action head); early partners 1X, Agility, Boston Dynamics, Mentee, NEURA |
| GR00T N1.5 | 2025-05 | open weights | Frozen Eagle 2.5 VLM; FLARE learning from human video; targets Jetson Thor |
| GR00T N1.6 | announced CoRL 2025-09-29, shipped CES 2026-01 | open weights | Cosmos Reason as reasoning brain; full-body loco-manipulation; LeRobot distribution |
| GR00T N1.7 | 2026-04-17 | **early access**, open weights (NVIDIA Open Model License) | 3B; Cosmos-Reason2-2B backbone; EgoScale 20,854 h egocentric human video; claimed "first scaling law for robot dexterity" (vendor claim) |
| GR00T N2 | previewed GTC 2026-03-16 | **preview; GA slated late 2026** (as of 2026-07 not GA) | Built on **DreamZero** world-action model; claimed ~2x success rate of leading VLAs on new tasks/environments, #1 on MolmoSpaces & RoboArena (vendor claims) |

- The GR00T bet mirrors the field's architecture convergence: dual-system VLA → reasoning VLA → world-action model (VLA and world-model threads merging).
- **Isaac GR00T reference humanoid** (announced GTC Taipei/COMPUTEX, 2026-05-31): open reference design — Unitree H2 Plus body + Sharpa Wave tactile hands + Jetson Thor T5000 + Isaac GR00T stack — for academic labs (Ai2, ETH Zurich, Stanford Robotics Center, UCSD); available from Unitree in late 2026 (per NVIDIA release; no month given). Notable: NVIDIA's US reference platform rides a Chinese robot body ([Unitree](company-unitree.md)).

## World-model layer: Cosmos

Full treatment in [World models](world-models.md); the platform-strategy view:

- **Cosmos 1** (CES 2025-01-06): open world foundation models trained on ~9,000T tokens / 20M hours of video; launch adopters included 1X, Agility, Figure, Fourier, Galbot, Skild, Waabi, XPENG, Uber. **Cosmos Reason** (GTC 2025-03) added physical-reasoning VLM — now the backbone of GR00T N1.6/N1.7. **Predict 2.5 / Transfer 2.5** (2025-10): 30 s rollouts; sim2real style transfer. **Cosmos 3** (unveiled GTC 2026-03; full open release GTC Taipei 2026-05-31): "first fully open omnimodel" — text/image/video/sound/**action** generation; Super/Nano/Edge variants; launched with a "Cosmos Coalition" (Agile Robots, Black Forest Labs, Generalist, LTX, Runway, Skild AI). A **Cosmos-H** variant is used by CMR Surgical for surgical-system validation (per GTC 2026 release).
- **Cosmos Policy** (2026-01): post-trains Cosmos into a control model — 98.5% LIBERO (reported) — positioning world models as *policy backbones*, not just data engines.
- Downloads: Cosmos WFMs passed **3M downloads** and the open NVIDIA Physical AI Dataset **4.8M+ downloads** (as of 2025-09, NVIDIA figures per the CoRL 2025-09-29 release).
- Strategy: Cosmos converts robotics' data scarcity into GPU demand — NVIDIA's GTC 2026 framing was literally to "swap the data problem for a compute problem."

## Act layer: Jetson, and the Halos safety platform

Details in [Hardware](hardware.md). Jetson lineage: TK1 (2014) → TX1/TX2 → AGX Xavier (2018) → AGX Orin (2022, 275 TOPS, the 2023–25 humanoid workhorse) → **Thor**:

| Module | AI compute | Memory | Price | Status |
|---|---|---|---|---|
| Jetson AGX Thor (T5000) | 2,070 TFLOPS (FP4 sparse) | 128 GB | $3,499 dev kit | **GA 2025-08-25**; 7.5× Orin compute |
| Jetson T4000 | 1,200 TFLOPS (FP4 sparse) | 64 GB | $1,999 @1k units | announced CES 2026-01 (mid-tier) |

- Thor's 128 GB fits multi-billion-parameter VLAs onboard; early adopters: Agility, Amazon Robotics, Boston Dynamics, Figure, Caterpillar, Meta; 1X NEO ships on Thor; OpenAI and Physical Intelligence evaluating (as of 2025-08, NVIDIA list).
- **Power cost of onboard NVIDIA compute**: per Witt's New Yorker reporting (2026-07-06 issue), an NVIDIA edge chip "can drain as much as sixty per cent of a robot's electricity supply" — vs ~20% of body energy for the human brain; Apptronik CEO Jeff Cardenas, in the same piece: "It's not the motors that take up most of the battery. It's actually the compute." A concrete number behind the price/power-sensitivity risk flagged below and in [Hardware](hardware.md).
- **Halos**: introduced at GTC 2025-03 as an AV full-stack safety system; **Halos for Robotics announced 2026-06-22 (Automate 2026)** — billed as the industry's first full-stack safety system for Physical AI. Four layers: **IGX Thor** industrial-grade compute, **Holoscan Sensor Bridge**, **Halos OS** safety software, and the **Halos AI Systems Inspection Lab** (certification prep against IEC 61508, ISO 13849, ISO/IEC TR 5469). NVIDIA claims it transfers 18,600+ engineering-years of AV safety work to robots (vendor framing). **Agility Robotics is first adopter** for Digit — safety becoming a platform-sold feature is new for the field; see [Safety & regulation](safety-regulation.md).

## Verticals

- **Isaac for Healthcare** (introduced GTC 2025-03): medical-robotics dev platform (digital twins, SDG, edge deployment on IGX/Holoscan). As of GTC 2026: **Johnson & Johnson MedTech** training its Monarch platform (urology launch in US slated 2026) with Isaac Sim + Cosmos; **Medtronic** exploring IGX Thor for surgical systems; **CMR Surgical** validating Versius with Cosmos-H.
- **Isaac for AMR / industrial**: Isaac Perceptor/Nova sensor stacks; Isaac AMR path planning + Metropolis vision agents deployed in Foxconn's Houston plant; virtual commissioning integrations with **FANUC, ABB, KUKA, Yaskawa** (combined 2M+ robot install base) announced at GTC 2026 — the wedge from humanoids into the installed industrial-arm base.
- **Factories as customers and showcases**: Foxconn's 242,287 sq ft Houston AI-server plant designed in Omniverse and slated to be among the first lines running **GR00T-powered humanoid robots** (announced 2025-10; deployment targeted Q1 2026 alongside GB300 server production; independent confirmation that humanoids are running in production had not surfaced as of 2026-07 — treat as in-progress). TSMC (Phoenix fab), Toyota (Georgetown), Caterpillar, Lucid, Wistron, Belden all named Omniverse/Isaac users (GTC DC, 2025-10-28).

## Partnership and investment graph (as of 2026-07)

| Relationship | Who | Substance |
|---|---|---|
| Equity investments | [Figure](company-figure.md) (Series B 2024-02 + Series C 2025-09), Skild AI (NVentures, 2025 + Series C 2026-01), Neura Robotics (2026-06 round) | NVIDIA funds its own future platform customers — "kingmaker" dynamic (see [Investment](investment.md)) |
| Model/infra customers | Figure ("using NVIDIA accelerated computing" to build Helix + Isaac for sim/training, per NVIDIA PR 2025-10-28), Skild, Boston Dynamics, Agility, 1X (NEO on Thor), AGIBOT, Hexagon | Even labs with in-house models train on NVIDIA GPUs; Figure's Helix is closed but NVIDIA-trained |
| GR00T ecosystem | 1X, Agility, Boston Dynamics, Mentee, NEURA (N1 launch); Fourier, Franka, AGIBOT, Unitree (reference humanoid) later | Open-model distribution channel; validation breadth varies (many are pilots/evals) |
| Manufacturing | Foxconn (Houston humanoids + AI-server capacity in TX/WI/CA; also led Agility's SPAC PIPE), TSMC, Toyota, BMW (Omniverse factory digital twins since 2021–23), Mercedes, Hyundai (AV + robotics via Boston Dynamics parent) | Factory digital twins as beachhead; BMW's humanoid supplier is Figure, not NVIDIA directly |
| Sim/physics allies | Google DeepMind + Disney Research (Newton), Lightwheel (Arena), Hugging Face/LeRobot | Coopetition: DeepMind is a model-layer rival but physics-layer partner |
| Cloud | Microsoft Azure (Physical AI Data Factory blueprint), CoreWeave (Isaac Lab pipelines), Alibaba Cloud (full stack) | Three computers rentable, not just buyable |

## Robotics revenue vs. rhetoric

The gulf between narrative and disclosed numbers is the core skeptic exhibit:

| Metric (as of 2026-05 reporting) | Value |
|---|---|
| FY2026 total revenue (year ended 2026-01-25) | **$215.9B** |
| FY2026 Data Center | $193.7B (~90%) |
| FY2026 Automotive line (incl. robotics; DRIVE + Jetson) | **$2.3B (~1.1%)**; Q4 FY26: $604M vs Data Center's $62.3B |
| Q1 FY2027 (ended 2026-04-26, reported 2026-05-20) | Total $81.6B; **new segmentation**: Data Center $75.2B; **Edge Computing $6.4B** (+29% YoY) |
| Robotics-specific revenue | **never separately disclosed** |

- From Q1 FY2027 NVIDIA collapsed reporting into two segments — Data Center and **Edge Computing**, where robotics sits mixed with **PCs, game consoles, workstations, AI-RAN, and automotive** — making robotics revenue *less* visible just as the rhetoric peaks.
- The honest bull case: robotics' revenue contribution today is mostly *indirect* — every robot lab's training cluster is Data Center revenue (Figure, Skild, PI, OpenAI all train on NVIDIA), so the robotics stack functions as demand insurance for the core business.
- **Jensen Huang's TAM rhetoric**: "The ChatGPT moment for general robotics is just around the corner" (CES 2025); "The age of generalist robotics is here" (GTC 2025-03); "Physical AI has arrived — every industrial company will become a robotics company" (GTC 2026-03). Financial press (2026-05) reports him repeatedly framing humanoid robots as a **~$40T labor-automation TAM** (secondary attribution; he and Musk have also floated ~$50T "physical AI" figures) — a number ~4 orders of magnitude above any disclosed robotics revenue in the industry.

## Competitive position

| Challenger | Play | Status (as of 2026-07) |
|---|---|---|
| **Qualcomm** | Full robotics suite at CES 2026-01: Dragonwing IQ10 (18-core premium SoC for humanoids/AMRs), Dragonwing Robotics Development Platform explicitly pitched against Jetson on power/cost; Arduino acquisition (2025-10, 33M-user community; Uno Q / Ventuno Q boards) | Ecosystem partners include Advantech, Booster, KUKA, VinMotion — and **Figure**, which is "collaborating to define the next generation of compute architecture" with Qualcomm (Qualcomm PR) — a direct crack in NVIDIA's flagship-customer story |
| **Tesla (in-house)** | AI5 custom silicon taped out 2026-04-15 (Samsung + TSMC), volume mid-to-late 2027, aimed at Optimus + inference clusters | The vertical-integration escape route: still trains on NVIDIA today, plans not to need Jetson ever |
| **Huawei** | CloudRobo embodied-AI platform (cloud-heavy "end-edge-cloud" architecture) + Ascend silicon; explicitly modeled on NVIDIA's playbook (Digitimes) | Default option for Chinese makers as US export controls bite; no dominant humanoid design win confirmed as of mid-2026 (see [Landscape: China](landscape-china.md)) |
| **Google DeepMind** | Gemini Robotics model line (closed) competes with GR00T at the policy layer | Simultaneously NVIDIA's Newton/MuJoCo-Warp partner — coopetition |
| **Chinese edge chips** | Horizon Robotics, Black Sesame | Positioned as domestic Jetson alternatives; no widely adopted humanoid win reported as of mid-2026 (unverified absence) |

- NVIDIA's structural advantages: CUDA developer gravity (4M+ registered CUDA developers), the Isaac Lab API becoming a de-facto training-framework standard (even MuJoCo-based mjlab adopts it), and the only end-to-end train/simulate/act offer.
- Structural risks: China market access (export controls push the largest robot-manufacturing nation toward domestic stacks); onboard-inference price/power sensitivity (a $3,499 dev-kit-class computer in a ~$20k robot is a real BOM line — see [Hardware](hardware.md)); and the biggest robot fleets (Tesla, possibly Figure) verticalizing away.

## Skeptic case

- **Announcement density ≠ adoption**: partner lists recycle across press releases (the same ~15 names appear at CES, GTC, CoRL, Automate); many entries are pilots, evaluations, or "exploring." Deployment-grade, independently confirmed uses of the *full* stack are rarer than the graph above suggests. Vendor benchmark claims (N2's "2x over leading VLAs," the N1.7 "dexterity scaling law," Newton's 252x/475x speedups) lack third-party replication — see [Evaluation](evaluation.md).
- **Open-washing critique**: GR00T weights ship under NVIDIA's own license (not Apache/MIT), Cosmos/Isaac are optimized for — and effectively assume — NVIDIA hardware; the "open Android" is a funnel into closed silicon. Counterpoint: Newton's Linux Foundation governance and genuine Isaac Sim open-sourcing are more than most rivals offer.
- **Ecosystem lock-in worries are voiced by builders**: VLA-era workloads are heterogeneous (vision, language, action, world-model inference), and an all-NVIDIA assumption prevents mixing best-per-workload accelerators — an argument that robotics could *dilute* rather than extend the CUDA moat (investor/analyst commentary, 2026).
- **Customer concentration irony**: the best-funded US humanoid programs are precisely the ones with means to leave — Tesla (AI5), Figure (Qualcomm collaboration despite NVIDIA's equity stakes). NVIDIA investing in its own customers also muddies "adoption" as an organic signal.
- **Revenue opacity**: folding robotics into a gaming-dominated Edge Computing segment (2026-05) means the market cannot track whether the robotics business is actually growing — the $40T story is unfalsifiable from NVIDIA's own disclosures.
- Steel-man: none of the skeptic points touch the core asymmetry — NVIDIA profits from robot-AI *training* regardless of whose robot or whose onboard chip wins, and no competitor offers the integrated three-computer pipeline. Picks-and-shovels positioning is robust to individual robot-maker failures; it is exposed mainly to the sector-wide [bubble scenario](investment.md).

## Sources

- https://blogs.nvidia.com/blog/three-computers-robotics/ — three-computer thesis (DGX train / Omniverse+Cosmos simulate / Jetson act), official framing
- https://nvidianews.nvidia.com/news/nvidia-isaac-gr00t-n1-open-humanoid-robot-foundation-model-simulation-frameworks — GR00T N1 launch (2025-03-18), early partners (1X, Agility, Boston Dynamics, Mentee, NEURA), Blueprint 780k-trajectories claim, Newton announcement
- https://research.nvidia.com/labs/gear/gr00t-n1_5/ — GR00T N1.5 (Eagle 2.5, FLARE)
- https://nvidianews.nvidia.com/news/nvidia-releases-new-physical-ai-models-as-global-partners-unveil-next-generation-robots — N1.6 shipped with Cosmos Reason integration + LeRobot distribution (CES, 2026-01-05)
- https://nvidianews.nvidia.com/news/nvidia-accelerates-robotics-research-and-development-with-new-open-models-and-simulation-libraries — N1.6 announced (CoRL, 2025-09-29); Cosmos 3M / Cosmos Reason 1M / Physical AI Dataset 4.8M download counts
- https://huggingface.co/blog/nvidia/gr00t-n1-7 — GR00T N1.7 early access (2026-04-17): Cosmos-Reason2-2B backbone, EgoScale 20,854 h, licensing
- https://nvidianews.nvidia.com/news/nvidia-and-global-robotics-leaders-take-physical-ai-to-the-real-world — GTC 2026-03-16: GR00T N2/DreamZero preview + vendor claims, Isaac Lab 3.0, Newton 1.0, Cosmos 3 unveiling, full partner list, 2M robotics developers, Hugging Face partnership, Huang "every industrial company" quote
- https://nvidianews.nvidia.com/news/nvidia-launches-cosmos-world-foundation-model-platform-to-accelerate-physical-ai-development — Cosmos 1 launch (CES 2025-01-06), training scale, adopters
- https://nvidianews.nvidia.com/news/nvidia-launches-cosmos-3-the-open-frontier-foundation-model-for-physical-ai — Cosmos 3 open release (2026-06-01), omnimodel, variants, Coalition
- https://nvidianews.nvidia.com/news/nvidia-open-humanoid-robot-reference-design — Isaac GR00T reference humanoid (Unitree H2 Plus + Sharpa Wave + Thor T5000, 2026-06-01, academic launch users, Unitree availability 2026-10)
- https://nvidianews.nvidia.com/news/nvidia-blackwell-powered-jetson-thor-now-available-accelerating-the-age-of-general-robotics — Jetson Thor GA (2025-08-25), specs, $3,499 dev kit, adopter list
- https://developer.nvidia.com/blog/accelerate-ai-inference-for-edge-and-robotics-with-nvidia-jetson-t4000-and-nvidia-jetpack-7-1/ — Jetson T4000 specs and pricing (CES 2026-01)
- https://nvidianews.nvidia.com/news/nvidia-announces-halos-for-robotics-the-industrys-first-full-stack-safety-system-for-physical-ai — Halos for Robotics: four layers, Agility first adopter, standards targeted
- https://www.robotics247.com/article/automate-2026-nvidia-announces-halos-for-robotics — Halos for Robotics date/venue (Automate 2026, 2026-06-22), 18,600 engineering-years framing
- https://developer.nvidia.com/blog/introducing-nvidia-isaac-for-healthcare-an-ai-powered-medical-robotics-development-platform/ — Isaac for Healthcare platform intro (GTC 2025-03)
- https://www.jnj.com/media-center/press-releases/johnson-johnson-to-advance-robotics-development-with-nvidia-isaac-for-healthcare — J&J MedTech on Isaac for Healthcare; Monarch training
- https://nvidianews.nvidia.com/news/nvidia-us-manufacturing-robotics-physical-ai — GTC DC (2025-10-28): Figure building Helix on NVIDIA accelerated computing + Isaac; Foxconn Houston 242,287 sq ft; Amazon BlueJay; TSMC/Toyota/Caterpillar/Lucid digital twins; $1.2T US capacity framing
- https://www.investing.com/news/stock-market-news/foxconn-to-deploy-humanoid-robots-at-houston-ai-server-plant-4315135 — Reuters: Foxconn GR00T-powered humanoids at Houston GB300 plant, Q1 2026 deployment target
- https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-fourth-quarter-and-fiscal-2026 — FY2026 results: $215.9B total, $193.7B Data Center, $2.3B Automotive (Q4: $604M)
- https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-first-quarter-fiscal-2027 — Q1 FY27 (ended 2026-04-26): $81.6B total; new Data Center ($75.2B) / Edge Computing ($6.4B) segmentation; Edge includes robotics + automotive + PCs/consoles
- https://www.cnbc.com/2026/05/20/nvidia-nvda-earnings-report-q1-2027.html — Q1 FY27 reporting date and coverage
- https://techcrunch.com/2026/01/05/nvidia-wants-to-be-the-android-of-generalist-robotics/ — "Android of robotics" framing; robotics fastest-growing Hugging Face category
- https://247wallst.com/investing/2026/05/31/jensen-huang-just-called-humanoid-robots-a-40-trillion-market-heres-why-wall-street-is-loading-up-on-physical-ai-stocks/ — $40T humanoid TAM attribution to Huang (secondary; financial press)
- https://www.qualcomm.com/news/releases/2026/01/qualcomm-introduces-a-full-suite-of-robotics-technologies-power — Qualcomm robotics suite (CES 2026): Dragonwing IQ10, ecosystem incl. Figure compute-architecture collaboration
- https://www.automate.org/robotics/news/ces-2026-qualcomm-targets-nvidia-jetson-with-new-robotics-developer-platform — Qualcomm Dragonwing platform positioned against Jetson
- https://spectrum.ieee.org/qualcomm-arduino-acquisition-open-source — Qualcomm–Arduino acquisition (2025-10) and open-source-community debate
- https://electrek.co/2026/04/15/tesla-ai5-chip-taped-out-musk-ai6-dojo3/ — Tesla AI5 tape-out (2026-04-15), 2027 volume target, Optimus focus
- https://www.digitimes.com/news/a20250103PD214/huawei-nvidia-robotics-llm-robot.html — Huawei entering humanoid robotics on the NVIDIA platform model
- https://www.huaweicloud.com/intl/en-us/news/20250919133255709.html — Huawei CloudRobo embodied-AI platform description
- https://builtin.com/articles/nvidias-cuda-future-ai-infrastructure — CUDA lock-in critique; argument that heterogeneous robotics workloads weaken the moat
- https://www.newyorker.com/magazine/2026/07/06/are-humanoid-robots-ready-to-be-deployed — Witt: "every single robot… ran on an Nvidia microchip / trained in an Nvidia digital gym"; edge chips drain up to 60% of robot battery (Cardenas quote); "vender lock" ex-employee characterization (read via Wayback snapshot)
