---
title: Tactile Sensing & Dexterous Hands
slug: tactile-hands
updated: 2026-07-03
confidence: verified
---
> Dexterous hands and tactile sensing are the weakest hardware branch of Physical AI: every other subsystem (legs, actuators, compute, batteries) has a converged "standard stack," while hands remain the least durable, most expensive, most fragmented component — and touch is still missing from frontier robot policies entirely. As of 2026-07 the landscape spans a 100× price range (AgiBot OmniHand ~$1.4k entry to Shadow Hand ~$100–150k), two rival sensing philosophies (camera-on-gel vision-based tactile vs cheap taxel arrays), and a Chinese-led mass-production wave (>30k hands shipped worldwide 2025, Gasgoo-derived estimate) that is collapsing prices faster than durability or data pipelines improve. Tactile-first models (AnyTouch, TLA, VLA-Touch, OmniVTLA, FTP-1) and datasets (Touch100k, TacQuad, Daimon-Infinity) emerged 2025–26, but no frontier [VLA](vla-models.md) yet ships touch as a first-class input. This page covers hand hardware and touch sensing in depth; the policy/learning side lives in [Manipulation](manipulation.md), and actuators/compute in [Hardware](hardware.md).

## Why hands are the weakest branch

- Locomotion converged on sim-to-real RL and standard actuators; hands did not — contact physics simulates poorly, so hand hardware cannot be validated or trained cheaply in sim (see [Simulation](simulation.md)).
- A 20+ DoF hand concentrates the hardest engineering constraints in the smallest volume: actuation density, thermal limits, wiring, sensor real estate, and constant collision exposure.
- The subsystem carries a triple penalty: highest per-unit cost share after actuators, highest failure rate (fingers hit things), and lowest data availability (tactile signals are absent from human video and most teleop corpora — see [Data](data.md)).
- Design consensus emerging as of 2026: move actuators to the forearm, drive fingers by tendons (Tesla Optimus Gen-3, Figure 03, DexRobot) — freeing hand volume for sensing at the price of cable wear and friction/hysteresis in control.

## Hand landscape (as of 2026-07)

| Hand | Maker (origin) | DoF | Actuation | Tactile | Price (as of 2026) | Notes |
|---|---|---|---|---|---|---|
| Shadow Dexterous Hand | Shadow Robot (UK) | 24 joints, 20 actuated | Tendon (electric/pneumatic) | 129 sensors; BioTac/GelSight options | ~$100k–150k | Research DoF benchmark since OpenAI Dactyl; 2.8 kg |
| Optimus Gen-3/V3 hand | Tesla (US) | 22 hand + 3 wrist | Tendon, ~25 actuators per forearm (patent analyses, unverified) | Fingertip force sensing; broader coverage in development | Not sold | V3 production ramp targeted H2 2026 (secondary sources, unverified) |
| Figure 03 hand | Figure (US) | ~16 (F02 baseline) | Tendon, forearm-housed | Fingertip sensors detect ~3 g force; palm camera per hand | Not sold | In-house sensor built after existing options "could not withstand real-world use"; design principles: "extreme durability, long-term reliability, high-fidelity sensing" |
| SharpaWave | Sharpa (Singapore) | 22 | Motor-driven, human-scale (1.2 kg) | Visuo-tactile fingertips: >1,000 tactile pixels each, 0.005 N sensitivity over 0–30 N, 180 FPS | ~$50k (36kr figure, unverified) | >20 N fingertip; certified 1M grip cycles (company claim); shipping since 2025-10; in NVIDIA/Unitree H2 Plus reference design (2026-06) |
| Unitree Dex5-1 | Unitree (CN) | 20 (16 active + 4 passive) | Direct-drive, ~1 kg | Optional 94-point array @1 kHz | $25k–27k at US resellers; ~$6k–8k on gray-market/Alibaba listings; no official list price (unverified) | ~10 N fingertip, ~1 mm repeatability; fingers individually replaceable |
| Inspire RH56E2 / FTP | Inspire Robots (CN) | 6 active | Linkage | Up to 17 tactile pads, 0–30 N range | $8,900 (US retail, tactile config); basic DFX models cheaper | The volume workhorse: ~10k hands delivered 2025; 790 g, ~30 N fingertip |
| Linker Hand L20 | LinkerBot (CN) | 20 (16 active + 4 passive) | Motor | 72-cell (6×12) array @200 FPS; optional VBT/e-skin | RMB 49,900 (~$7k); L20 Lite <$5k | 100 N grip; >10k units delivered 2025; O7 (7 active DoF) budget line, L25/L30 higher tiers |
| DexHand021 | DexRobot (CN) | 22 (wrist-integrated) | Dual tendon | Full-palm multi-modal (Pro) | ~$9.5k retail; Pro ~$14k–28k | 50 N payload, >300k cycle claim (company PR, unverified) |
| OmniHand 2025 | AgiBot/Zhiyuan (CN) | 16 (10 active + 6 passive) | Motor, 500 g | 400+ force points, slip detection | RMB 9,800–14,800 (~$1.4k–2.1k) | Cheapest credible tactile hand; Pro: 19 DoF, 0.1 N resolution; hand business spun off as separate company (2026) |
| PaXini DexH13 | PaXini Tech (CN) | 13 | Motor | 1,140 multi-dimensional tactile units (15 sensed dimensions claimed) | n/a (quote) | "Tactile infrastructure" full-stack pitch at CES 2026 |
| Allegro Hand V5 | Wonik Robotics (KR) | 16 | Motor | Optional; Digit 360 integration partner | ~$15k–30k (secondary source) | Long-running research mid-tier; Wonik is Meta's hand partner for Digit 360 commercialization |
| DG-5F | Tesollo (KR) | 20 | Motor | Optional | n/a | Aimed at humanoid OEM market |
| F-TAC Hand | PKU + BIGAI (CN, research) | 15 (anthropomorphic kinematics) | Motor | 17 VBT sensors covering ~70% of palmar surface, 0.1 mm resolution | Not sold | Nature Machine Intelligence 2025-06; densest tactile coverage demonstrated on a hand |

- Market structure: a premium visuo-tactile tier (SharpaWave, Shadow), a $5k–10k Chinese high-DoF tier (LinkerBot L20, DexRobot, Inspire tactile configs — Unitree's Dex5-1 appears here only on gray-market listings; it runs $25k+ at Western resellers), and a sub-$2.5k entry tier (OmniHand at RMB 9,800, LinkerBot O6/O6 Lite at RMB 6,666/3,999, Inspire base) — the middle tier is where volume is concentrating.
- Humanoid OEMs (Tesla, Figure) build hands in-house and do not sell them; Chinese OEMs increasingly buy or spin off (Zhiyuan's hand spin-off signals a component-supplier layer forming, mirroring automotive Tier-1s).

## Vision-based tactile (VBT): the GelSight lineage

Camera watches a deformable, illuminated gel skin; photometric stereo recovers contact geometry at up to micron resolution.

- Lineage: retrographic sensing (Johnson & Adelson, MIT, 2009) → GelSight Inc spinout → GelSlim (MIT), DIGIT (Meta, 2021, low-cost open design manufactured by GelSight) → GelSight Mini (2022: $499 unit, $49 replacement gels — the price that made VBT a commodity research tool) → 2024–25 variants (GelBelt, ThinTact, DTactive; see [Manipulation](manipulation.md)).
- **Meta × GelSight Digit 360** (2024-10): fingertip-shaped, ~8.3M taxels, omnidirectional deformation capture, ~1 mN force sensitivity, 18+ sensing modalities (incl. vibration, heat, odor via gas sensor), on-device processing. Distributed free to selected researchers; commercialization via GelSight and Wonik Robotics; fully open-sourced designs/code.
- **F-TAC Hand** (PKU/BIGAI, Nature MI 2025-06): first hand where VBT is structural, not add-on — 17 sensors in 6 configurations double as load-bearing components, covering ~70% of the grasping surface at 0.1 mm resolution; outperformed non-tactile baselines across 600 real-world adversarial-grasp trials.
- **Daimon Robotics DM-Tac** (Shenzhen): claims 40,000 sensing units/cm² and 5M-press durability (company figures, unverified); ships on Daimon's own hands and feeds its VTLA model line — the most aggressive commercial VBT bet in China.
- **Sharpa DTA**: 180 FPS dynamic tactile array with sub-mm spatial resolution — the first VBT-class sensing in a mass-produced commercial hand (shipping 2025-10; "first" is company/press framing, unverified).
- VBT weaknesses that keep it out of most production hands: gel/skin wear (soft silicone fingertip skins degraded within ~2,000–4,000 grasp cycles in the ORCA hand study; GelSight-class gels are consumables), per-finger camera bulk and cost, frame-rate vs 1 kHz control loops, and calibration drift as gels deform permanently.

## Taxel arrays, force/torque, and emerging skins

**Taxel arrays** (piezoresistive/capacitive/magnetic pads) win on production hands because they are thin, cheap, and survive contact:

| System | Density / count | Rate | Status |
|---|---|---|---|
| Unitree Dex5-1 | 94 points/hand | 1 kHz | Shipping (optional) |
| Inspire FTP series | 17 pads/hand, 0–30 N | — | Shipping |
| LinkerBot L20 | 72 cells (6×12) | 200 FPS | Shipping |
| AgiBot OmniHand | 400+ points, 0.1 N resolution (Pro) | — | Shipping |
| PaXini ITPU | 1,140 units on DexH13; 15 dimensions claimed | — | Shipping (quote-based) |
| Tacta | 361 sensels/cm², 4.5 mm module; 1,956-sensel full-hand demo | 1 kHz | CES 2026 demo (company claims, unverified) |
| Figure 03 fingertips | ~3 g force detection threshold | — | In-house, production |

- Trade-off vs VBT: taxels give force distribution at kHz rates but no fine geometry; VBT gives geometry/texture but is fragile and slow. Hybrid hands (LinkerBot optional VBT modules, SharpaWave camera+taxel fingertips) hedge both ways.
- **Force/torque sensing** (covered in depth in [Hardware](hardware.md)): six-axis wrist F/T sensors plus joint-torque-from-current estimation; Chinese suppliers scaling fast. For hands specifically, fingertip 3-axis force + joint current is the common production recipe; full 6-axis per fingertip remains research-grade.
- **Emerging skins**: robot e-skin market estimated $266M (2025) → $795M (2034) (market research, unverified); PDMS substrates dominate with graphene-composite conductors emerging; neuromorphic e-skin with local "pain" reflexes and modular repair demonstrated (PNAS, 2026); EIT-based stretchable skins and capacitive large-area skins (CushSense) target whole-arm/body coverage rather than fingertips. None are in production humanoids as of 2026-07.

## Tactile datasets and tactile-first models

The binding constraint is data: touch cannot be scraped from the internet, teleop rigs rarely record it, and every sensor speaks a different "language" (resolution, gel optics, force calibration).

**Datasets (as of 2026-07):**
- **Touch100k** — first touch-language-vision dataset at 100k-sample scale; enables GelSight-style representation pretraining (TLV-Link).
- **TacQuad** — aligned multi-sensor data across GelSight Mini, DIGIT, DuraGel, Tac3D; built to attack cross-sensor transfer.
- **Daimon-Infinity** (2026-04): tactile-inclusive multimodal embodied dataset; 10,000 hours open-sourced on Alibaba ModelScope, ~1B data points claimed, company projects "millions of hours" by end-2026 (company claims, unverified) — the largest open tactile-labeled corpus if claims hold.
- **RobOmni** (Daimon × Galbot, 2026): benchmark isolating how much tactile sensing improves manipulation — an early answer to the field's tactile-evaluation gap (see [Evaluation](evaluation.md)).

**Models:**
- **AnyTouch** (ICLR 2025) and AnyTouch 2 (2026): unified static+dynamic representations across heterogeneous visuo-tactile sensors — the "sensor Babel" workaround.
- **TLA** (2025): tactile-language-action model for contact-intensive tasks (e.g., peg insertion) via cross-modal language grounding.
- **VLA-Touch** (2025): bolts dual-level tactile feedback onto existing VLAs without retraining the trunk.
- **OmniVTLA** (2025-08) and **TacVLA** (2026): vision-tactile-language-action architectures with semantically aligned tactile encoders.
- **FTP-1** (2026): a generalist "foundation tactile policy" trained across tactile sensors for contact-rich manipulation — first explicit foundation-model framing for touch.
- Status check: these are all research-scale; no frontier VLA (π-series, Helix, Gemini Robotics, GR00T) ships tactile input as a documented first-class modality as of 2026-07 (Figure 03 ships tactile fingertips and says they enable slip-aware grasping, but Figure has not published Helix consuming tactile as a model input). Daimon's VTLA line is the closest commercial attempt (single vendor, unverified performance).

## China's hand mass-production economics

- Known dexterous-hand shipments exceeded 30,000 units worldwide in 2025 (Gasgoo estimate derived from >15k global humanoid shipments at two hands per robot; Chinese vendors dominate; single source); Inspire ~10k (5× its 2024 volume of 2,000), LinkerBot shipped its 10,000th hand 2025-12 (peak month >4,000 units; company PR) with 50k–100k targeted for 2026 (company statements, unverified).
- Capacity build-out (as of 2026): Xynova plant slated for Q2 2026 commissioning at 10k hands/yr (>10k hands already on order); ENCOS declared full mass production; Zhiyuan/AgiBot spun off its hand unit as a standalone supplier (Shanghai "Critical Point", 2026) — the market is verticalizing into a component tier (see [Landscape: China](landscape-china.md)).
- Price collapse mechanics mirror the EV/G1 playbook: domestic motor/reducer/sensor supply chains, shared humanoid demand pull, and aggressive entry pricing (OmniHand's RMB 9,800 launch discount). A 20-DoF tactile hand cost ~$100k+ (Shadow-class) in 2020; ~$7k (LinkerBot L20-class) in 2025; ~$1.4k–2.1k entry (OmniHand, launched 2025-08).
- What the low price buys is unclear: durability cycles, force accuracy under sustained load, and tactile calibration stability are not independently audited at any tier (as of 2026-07); buyers report wide quality variance (anecdotal, unverified).
- Western/Korean positioning: premium sensing (Sharpa at ~$50k, Digit 360 research ecosystem) or vertical integration (Tesla, Figure in-house). No US/EU vendor competes in the $5k–10k volume tier (as of 2026-07).

## Why dexterity remains the gap

- **Durability**: fingers live in collision. Tendon/cable wear, soft-skin degradation (~2,000–4,000 grasp cycles in the ORCA study, with signal-wire snapping at 4,500–7,000 cycles), and connector fatigue make hands the highest-maintenance subsystem; vendor durability claims (SharpaWave 1M grip cycles, DexRobot >300k, DM-Tac 5M presses) are company-certified, not independently audited.
- **Control degradation**: tendon transmissions suffer friction, hysteresis, and calibration drift that erode repeatability over deployment timescales — a 2026 review argues these are systematically underreported in hand evaluations.
- **Sensor drift**: piezoresistive taxels show initial-resistance drift from nanoparticle dispersion and microstructure variance; VBT gels deform permanently; both need recalibration loops no production stack yet automates (as of 2026-07).
- **Data scarcity**: tactile is missing from human video, most teleop rigs, and all web-scale corpora; datasets above are 3–5 orders of magnitude smaller than vision-language pretraining data.
- **Sensor fragmentation**: no standard tactile "format" — cross-sensor transfer (AnyTouch, TacQuad, FTP-1) is an active research field rather than a solved plumbing problem.
- **Simulation gap**: gel optics, soft contact, and taxel response are harder to simulate than rigid-body contact, blocking the sim-to-real path that solved [locomotion](locomotion.md).
- **Economics vs need**: most deployed tasks (logistics picking) still monetize with parallel-jaw grippers, so hands lack the deployment-driven data flywheel that improves everything else (the gripper-suffices argument is covered in [Manipulation](manipulation.md); broader unsolved issues in [Open problems](open-problems.md)).

## Watch items

- Does a frontier VLA ship tactile as a first-class input in 2026 (candidates: π-series successor, Daimon VTLA, FTP-1 scaling)?
- Daimon-Infinity's "millions of hours by end-2026" claim — would be the first internet-scale tactile corpus if real.
- Independent durability audits of the $5k–10k Chinese hand tier; whether LinkerBot hits 50k–100k units.
- VBT-in-production trajectory: SharpaWave field reliability vs Figure's explicit anti-gel durability bet.
- Whether Tesla's V3 hand ramp (H2 2026 target) validates forearm-tendon architecture at automotive volume.

## Sources

- https://www.robotwale.com/article/dexterous-hands-shadow-allegro-inspire-race-to-5-finger-dexterity — Shadow ~$100k–150k, Allegro ~$15k–30k price bands.
- https://www.shadowrobot.com/wp-content/uploads/2022/03/shadow_dexterous_hand_e_technical_specification.pdf — Shadow Hand: 24 joints/20 actuated, 129 sensors, 2.8 kg.
- https://www.sharpa.com/pages/wave — SharpaWave: 22 DoF, >1,000 tactile pixels/fingertip, 0.005 N sensitivity, >20 N fingertip, 1M-cycle certification.
- https://www.cnx-software.com/2026/06/02/sharpa-wave-high-end-dexterous-robotic-hand-with-22-dof-high-sensitivity-dynamic-tactile-array/ — SharpaWave DTA: 180 FPS, sub-mm resolution, 1.2 kg.
- https://www.humanoidsdaily.com/news/sharpa-robotics-begins-shipping-sharpawave-dexterous-hand — SharpaWave shipping from 2025-10.
- https://roboticsandautomationnews.com/2026/06/09/sharpa-brings-dexterous-robot-hands-to-nvidia-and-unitree-humanoid-reference-design/102424/ — Sharpa in NVIDIA/Unitree H2 Plus reference design; ~$50k price mention (secondary).
- https://www.unitree.com/mobile/Dex5-1/ — Dex5-1: 20 DoF, 94 tactile points, 1 kHz, replaceable fingers.
- https://robostore.com/products/unitree-dex5-1 — Dex5-1 US reseller pre-order at $25,000 (not yet shipping).
- https://www.usrobotstore.com/products/unitree-5-finger-dexterous-hand-20-dof-dex5-1-dex5-1p-compatible-with-unitree-h2 — Dex5-1/Dex5-1P at $27,000 (US reseller); Alibaba gray-market listings run ~$7k–8k (unverified).
- https://www.usrobotstore.com/products/inspire-robots-5-finger-robotic-dexterous-hand-rh56e2 — Inspire RH56E2: $8,900, 6 DoF, 17 tactile pads, 790 g, ~30 N fingertip.
- https://aifitlab.com/products/linkerbot-linker-hand-l20 — Linker Hand L20: 20 DoF, 72-cell array, 100 N grip, RMB 49,900.
- https://kr-asia.com/linkerbot-raises-new-funding-to-build-a-full-stack-platform-for-robot-dexterity — LinkerBot funding, full-stack platform, O6/O6 Lite/L6/L30 pricing (RMB 3,999–99,900).
- https://www.prnewswire.com/news-releases/10-000-dexterous-hands-shipped-150-million-raised-linkerbot-leads-the-market-302645409.html — LinkerBot 10,000th hand shipped (2025-12-18), peak month >4,000 units, $150M raised (company PR).
- https://www.prnewswire.com/news-releases/dexrobot-unveils-full-dexterous-hand-series-and-new-dextele-teleoperation-system-at-automate-2026-302808579.html — DexHand021 series specs (company PR).
- https://news.futunn.com/en/flash/19251630/zhiyuan-robotics-has-released-the-omnihand-2025-dexterous-hand-with — OmniHand 2025 pricing (RMB 9,800 launch / 14,800 tactile).
- https://store.agibot.com/products/omnihand-pro-2025 — OmniHand Pro: 19 DoF, 750 g, 0.1 N resolution.
- https://humanoid.guide/product/dexh13/ — PaXini DexH13: 1,140 tactile units.
- https://www.koreaherald.com/article/10651060 — PaXini "tactile infrastructure" full-stack matrix at CES 2026.
- https://www.therobotreport.com/tesollo-unveils-dexterous-robot-hand-for-humanoids/ — Tesollo DG-5F 20 DoF.
- https://www.teslarati.com/tesla-optimus-v3-hand-arm-details-revealed-new-patents/ — Optimus V3 hand patents: 22 DoF, forearm tendon drive (secondary).
- https://www.figure.ai/news/introducing-figure-03 — Figure 03: ~3 g fingertip detection, palm cameras, durability-driven sensor design.
- https://www.nature.com/articles/s42256-025-01053-3 — F-TAC Hand (Nature MI 2025-06): 17 VBT sensors, ~70% coverage, 0.1 mm resolution, 600 trials.
- https://arxiv.org/abs/2412.14482 — F-TAC Hand preprint with design detail.
- https://www.businesswire.com/news/home/20241031980322/en/GelSight-and-Meta-AI-Introduce-Digit-360-Tactile-Sensor — Digit 360: 8.3M taxels, ~1 mN, 18+ modalities.
- https://ai.meta.com/blog/fair-robotics-open-source/ — Digit 360 open-source release; GelSight + Wonik commercialization partnership.
- https://www.gelsight.com/gelsightmini/ — GelSight Mini $499 / $49 gels.
- https://autonews.gasgoo.com/articles/news/daimon-robotics-releases-embodied-dataset-daimon-infinity-2044748516201508865 — Daimon-Infinity: 2026-04, 10k hours open, ~1B data points, DM-Tac 40k units/cm² and 5M-press claims.
- https://spectrum.ieee.org/daimon-robotics-physical-ai — DAIMON Robotics VBT + VTLA profile.
- https://www.therobotreport.com/daimon-robotics-and-galbot-jointly-launches-robomni-for-benchmarking-tactile-perception-and-dexterous-manipulation/ — RobOmni tactile-manipulation benchmark.
- https://arxiv.org/html/2406.03813v1 — Touch100k dataset.
- https://arxiv.org/pdf/2502.12191 — AnyTouch (ICLR 2025) + TacQuad multi-sensor dataset.
- https://arxiv.org/pdf/2602.09617 — AnyTouch 2: dynamic tactile representation learning.
- https://arxiv.org/html/2508.08706v1 — OmniVTLA: vision-tactile-language-action with semantic-aligned tactile.
- https://arxiv.org/pdf/2603.12665 — TacVLA: contact-aware tactile fusion for VLAs.
- https://arxiv.org/pdf/2606.13102 — FTP-1: generalist foundation tactile policy across sensors.
- https://github.com/linchangyi1/Awesome-Touch — curated tactile sensing/policy index (TLA, VLA-Touch, PolyTouch).
- https://autonews.gasgoo.com/articles/news/from-prototypes-to-production-dexterous-hands-kick-off-a-mass-production-race-2016425582734970881 — China 2025 shipments >30k (derived), Inspire ~10k, LinkerBot targets, Xynova plant.
- https://autonews.gasgoo.com/articles/news/zhiyuan-robot-spins-off-dexterous-hand-business-humanoid-robots-trigger-a-division-of-labor-revolution-2013868661754662912 — Zhiyuan hand-business spin-off.
- https://autonews.gasgoo.com/articles/news/encos-dexterous-hand-enters-full-mass-production-2008795632859136001 — ENCOS mass production.
- https://arxiv.org/html/2404.19448v1 — piezoresistive soft-skin hand: sensor drift <0.3% over 5,000 cycles; skin ruptures during mounting (does NOT contain the 2k-cycle figure; see ORCA below).
- https://link.springer.com/article/10.1007/s44245-026-00275-y — 2026 review: tendon friction/hysteresis/calibration drift underreported in hand evaluations.
- https://pmc.ncbi.nlm.nih.gov/articles/PMC11677542/ — piezoresistive taxel initial-resistance drift and repeatability fixes.
- https://www.pnas.org/doi/10.1073/pnas.2520922122 — neuromorphic e-skin with pain/injury perception and modular repair.
- https://www.intelmarketresearch.com/robot-electronic-skin-market-27486 — e-skin market $266M (2025) → $795M (2034) (market research, unverified).
- https://arxiv.org/html/2504.04259v2 — ORCA hand: silicone-skin degradation in ~2,000–4,000 grasp cycles, signal-wire snapping in ~4,500–7,000 cycles; reliability/cost framing for uninterrupted dexterous learning.
