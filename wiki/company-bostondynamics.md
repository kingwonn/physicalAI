---
title: "Company Deep Dive: Boston Dynamics"
slug: company-bostondynamics
updated: 2026-07-05
confidence: verified
---
> Boston Dynamics (founded 1992 by Marc Raibert as an MIT Leg Lab spin-off, HQ Waltham, MA, ~1,000 employees) is the oldest brand in legged robotics and, since 2026-06, a 100%-owned Hyundai Motor Group subsidiary — Hyundai bought SoftBank's residual 9.65% for $325M after paying ~$880M for 80% in 2020–21. Its 2026 story is the pivot from three decades of research theater to production: the electric Atlas production model launched at CES 2026-01-05 (56 DoF, 2.3 m reach, 50 kg lift), with the entire 2026 run committed to Hyundai's Robotics Metaplant Application Center and Google DeepMind, a 30,000-robots/yr factory targeted for 2028, and Hyundai planning 25,000+ Atlas units in its own US plants. The tech route is distinctive: world-best model-based-control hardware heritage, with the "brain" outsourced to partners (RAI Institute for RL, Toyota Research Institute LBMs, Google DeepMind Gemini Robotics) rather than an in-house VLA. Meanwhile Spot (~$75K quadruped, 3,000+ deployed) and Stretch (DHL MoU for 1,000+ more units) are the actual revenue businesses — but FY2025 revenue was only ~₩150B (~$110M) against a ~₩528B (~$385M) net loss, funded by Hyundai rights offerings. Context: [Humanoids](humanoid-robots.md), [Locomotion](locomotion.md), [Landscape: USA](landscape-usa.md), [Key people](key-people.md).

## Company at a glance (as of 2026-07)

| Field | Value |
|---|---|
| Founded | 1992, by **Marc Raibert** (MIT/CMU Leg Lab spin-off) |
| HQ | Waltham, Massachusetts; ~1,000 employees (Wikipedia, undated recent) |
| Ownership | **Hyundai Motor Group 100%** (SoftBank's remaining 9.65% bought for **$325M**, group approval reported for 2026-06-22); 2020–21 entry: ~$880M for 80% at a $1.1B valuation, with Chairman **Chung Eui-sun personally taking ~20%** of the buyer side (reported) |
| Leadership | Interim CEO **Amanda McMaster** (concurrently CFO) since 2026-02-27; Robert Playter (CEO 2019/2020–2026, 30-yr veteran) retired; permanent-CEO search ongoing |
| Products | **Spot** (quadruped, commercial since 2020-06, $74,500 base), **Stretch** (case-handling logistics robot, commercial 2022), **Atlas** (humanoid; production version CES 2026-01-05), **Orbit** (fleet software) |
| FY2025 financials | Revenue **₩150.1B (~$110M)**; **net loss ₩528.4B (~$385M)** (Korean-filings coverage) |
| Valuation | ~$3.4B implied by the SoftBank exit — but the put was struck on terms set in 2021, so not a market mark; circulating ~₩30T (~$20B) analyst figures (unverified) |
| Fleet | Spot 3,000+ deployed (aggregator, unverified); Stretch: DHL MoU for 1,000+ additional units; Atlas 2026 run fully committed (Hyundai RMAC + Google DeepMind) |
| Key partners | Hyundai Mobis (actuators), Google DeepMind (foundation models), RAI Institute (RL), Toyota Research Institute (LBMs), LG Energy Solution (batteries), NVIDIA (GR00T early partner, Thor adopter) |

## 30-year lineage: Leg Lab → hydraulics → electric production

| Era | Milestones |
|---|---|
| 1980s | Raibert's MIT/CMU **Leg Lab** hoppers prove dynamic balance via simple control heuristics — the intellectual root of the company (see [History](history.md)) |
| 1992 | Boston Dynamics founded as MIT spin-off; decades of DARPA/military funding |
| 2005–2013 | **BigDog** (2005, DARPA pack mule) puts dynamic legged locomotion on the map; PETMAN; **hydraulic Atlas** (2013) built for the DARPA Robotics Challenge |
| 2013–2017 | Owned by **Google X** (acquired 2013-12, price undisclosed); Google's robotics program dissolves, sold on |
| 2017–2020 | Owned by **SoftBank** (undisclosed sum); Spot productized; Playter becomes CEO |
| 2020–2021 | **Spot general commercial sale** (2020-06, $74,500); **Hyundai buys 80% for ~$880M** (announced 2020-12, closed 2021-06); Stretch announced 2021-03 |
| 2017–2021 | Viral parkour/backflip hydraulic-Atlas videos — offline-optimized behavior libraries + online MPC, **not RL** ([Locomotion](locomotion.md)) |
| 2024-04 | **Hydraulic Atlas retired**; all-electric Atlas unveiled |
| 2025 | RAI Institute RL partnership (2025-02); TRI **Large Behavior Model** drives Atlas (2025-08) |
| 2026 | **Production Atlas at CES (2026-01-05)** + Google DeepMind partnership; CNET "Best Robot" of CES; Playter exits (2026-02); Hyundai reaches 100% ownership (2026-06); $100M Massachusetts expansion (2026-06) |

## Tech route & architecture (技术路线)

**Hardware-first, brain-by-partnership** — the mirror image of [Figure's](company-figure.md) vertical-integration thesis.

- **Model-based-control heritage**: the 2017–2021 Atlas parkour era ran on hand-engineered trajectory optimization + MPC behavior libraries; Boston Dynamics was the last major holdout against learned locomotion and converted only in ~2025 ([Locomotion](locomotion.md)).
- **RL via the RAI Institute** (partnership announced 2025-02): Raibert's Hyundai-backed institute (founded 2022) co-develops sim-to-real locomotion and whole-body loco-manipulation policies for Atlas; prior joint work includes Spot's RL Researcher Kit (RAI's open pipeline hit 5.2 m/s on Spot, ~3× stock speed). RAI's framework produced Atlas's CES 2026 gymnastics and natural gait ([Key people](key-people.md)).
- **Manipulation via TRI**: the 2025-08 demo used Toyota Research Institute's **Large Behavior Model** — a single ~450M-param language-conditioned diffusion-transformer policy controlling the whole body, hands and feet alike ([Organizations](organizations.md)).
- **Cognition via Google DeepMind** (announced CES 2026-01-05): **Gemini Robotics foundation models as Atlas's high-level brain** — models "designed to allow robots of any shape and size to perceive, reason, use tools and interact with humans" (official); "embodied mind" is press framing, not the partners' own wording. Joint research "will be conducted at both companies," and DeepMind is one of the two recipients of the entire 2026 Atlas run. Fleet-learning pitch (BD spec sheet): "Once one Atlas learns a new skill, that task can easily be deployed across your entire Atlas fleet." A reunion of sorts — Google owned BD 2013–2017 ([VLA models](vla-models.md)).
- **What BD does NOT do**: train its own frontier VLA. Its stack is a partner sandwich — BD owns whole-body control, hardware, and the Orbit fleet layer (MES/WMS integration; autonomous, teleoperated, and tablet-steer modes); the high-level "brain" is DeepMind's. This trades speed for dependency (see SWOT below).
- **Production Atlas hardware** (official spec sheet, dated 2025-12): **56 DoF**, fully rotational joints, **2.3 m reach**, **50 kg instant / 30 kg sustained lift** (20 kg one-handed), **1.9 m / 90 kg**, 4 h battery life (2 h under heavy lifting) with **autonomous ~3-min battery self-swap**, −20 °C to 40 °C operation, **IP67**, tactile fingers and palm (press describes a four-fingered hand); dual swappable packs (press-reported). Fifth-generation design with "almost an order of magnitude reduction in complexity" vs the prior generation — "way, way less unique parts" (Alberto Rodriguez, Director of Robot Behavior for Atlas, Forbes 2026-07).

## The bet / vision

- **Playter at CES 2026**: *"This is the best robot we have ever built. Atlas is going to revolutionize the way industry works, and it marks the first step toward a long-term goal we have dreamed about since we were children — useful robots that can walk into our homes and help make our lives safer, more productive, and more fulfilling."*
- **Raibert's founder thesis** (now pursued from the RAI Institute): robots that can do what people and animals do — decades of "athletic intelligence" first, cognition later. The 2025–26 partnership structure effectively re-couples Raibert's research agenda to BD's product line.
- **Hyundai's thesis**: robots as the next vehicle. The group's CES 2026 "Physical AI" strategy makes BD the manufacturing arm of a chaebol-scale bet — $26B US investment envelope, a robot factory, and its own plants as the anchor customer. Hyundai says **industrial deployment comes before any home application** (KED, 2026-03).
- Strategy inversion worth noting: BD spent 30 years as the field's research showcase; the current bet is that **manufacturing discipline, not model supremacy, wins** — "every component has been designed for compatibility with automotive supply chains" (Zack Jackowski, GM of Atlas).

## Products & deployments (real numbers)

### Atlas (humanoid) — as of 2026-07
- **Entire 2026 production run committed** to two customers: **Hyundai's Robotics Metaplant Application Center (RMAC, Georgia, opening 2026)** and **Google DeepMind**; additional customers early 2027 (company-stated).
- **Hyundai deployment plan**: 25,000+ Atlas units across Hyundai/Kia plants — **Metaplant America (Savannah, GA) from 2028** (parts sequencing), Kia Georgia 2029, component assembly from ~2030. That absorbs ~83% of the planned 30,000/yr capacity (press calculation).
- Korea carve-out: Hyundai says Atlas will **not** be deployed at domestic (Korean) plants — North America first (Seoul Economic Daily, 2026-04) — after the Hyundai branch of the Korean Metal Workers' Union declared "not a single robot can enter the workplace without labor-management agreement" (2026-01-22).
- Production started at Boston HQ immediately after CES; mass production targeted **2028** at a 30,000/yr US factory (announced; site details thin as of 2026-07).

### Spot (quadruped) — the cash cow that isn't cash-flow-positive
- **3,000+ units deployed globally** (2026, third-party profile, unverified; company milestones passed 1,500 earlier); base price **$74,500** (launch 2020, roughly flat since).
- Verticals: industrial inspection (oil & gas, utilities, mining, construction monitoring), public safety, research; 35+ certified integrators in North America (market report, unverified). Europe ~28% of the market (market report, unverified).
- Third-party estimate: **>500 robots shipped in 2025 across Spot + Stretch, ~$130M revenue** (aggregator, unverified — directionally consistent with the ₩150.1B filing figure).

### Stretch (logistics case handling)
- **DHL**: partnership since 2018; commercial deployment from 2023 (North America, then UK/Europe); **2025-05-13 strategic MoU for 1,000+ additional Stretch units globally** — the largest publicly known commitment in the category, though an MoU rather than a firm purchase order (DHL Group primary).
- Other customers: **Gap** (beta at Fishkill NY → year-long Tennessee pilot → OH/TX/CA rollout), **H&M, Maersk/Performance Team, Otto Group**.
- Performance: up to **700 cases/hour** container unloading (company/DHL-reported).

## Business model & unit economics

- **Model**: direct product sales + integrator channel (Spot), large-account fleet deals (Stretch/DHL), and — for Atlas — **captive-first deployment** into the parent's factories with external sales from 2027. Orbit software is the recurring-revenue hook (fleet management, MES/WMS integration); no public ARR breakdown.
- **Atlas pricing signal**: below "the cost of employing two US manufacturing workers for two years," or about **$320K** (KED, 2026-01, per "sources briefed on the plan"; no public MSRP). BD reportedly briefed analysts at CES on an initial **$130–140K** sale price (Samsung Securities' Esther Yim, via Boston Globe 2026-03); the Hyundai union's internal estimate is ~₩200M (~$145K) (single source); prior-generation Atlas cost "historically upwards of $200,000" to build (Forbes). See [Hardware](hardware.md) price table.
- **Unit economics are unproven**: FY2025 revenue ₩150.1B (~$110M) vs net loss ₩528.4B (~$385M) — losses ~3.5× revenue, six years after Spot went on sale. Hyundai's three future-business affiliates (robotics, autonomy, AAM) accumulated **₩2.21T (~$1.5B) equity-method losses over five years** (Korean filings coverage, 2026-05: ₩2.2109T incl. HMG Global, Motional, Supernal).
- **Funding**: successive Hyundai-funded rights offerings — the 2025-08 round alone ~**$970M (~₩1.3T)**, larger than the prior three combined (₩982B total 2022–24; Korean coverage). SoftBank's stake diluted 20% → 9.65% before the $325M exit; the exact mechanics are unclear — Korean coverage reported SoftBank slated to participate pro-rata (~$121M) in the 2025-08 round (unverified). A NASDAQ IPO in 2027/2028 has been floated (single source, unverified).
- The 25,000-unit Hyundai commitment converts the humanoid program from a market bet into **related-party demand** — de-risked revenue, but not third-party market validation (contrast [Agility](company-agility.md)'s external customer orders, [Figure](company-figure.md)'s BMW deployment).

## Strengths / weaknesses vs peers

| Strengths | Weaknesses |
|---|---|
| 30-year hardware/controls pedigree; arguably the best whole-body mobility in the field (CES 2026 gymnastics) | **Late to learned software**: converted to RL ~2025, has no in-house VLA — the "brain" is DeepMind's, which also partners with Apptronik and others (no exclusivity evident) |
| **Hyundai captive demand** (25,000+ units) + $26B US investment envelope + automotive mass-production know-how (~7M vehicles/yr group capacity) | Losses ~3.5× revenue; repeated cash injections; valuation opaque |
| Strongest brand in robotics; CES 2026 "Best Robot"; recruiting magnet | **Cost/closed ecosystem**: <$320K signal vs [Unitree](company-unitree.md) G1 at ~$16K; no developer/open-model story vs [NVIDIA](company-nvidia.md) GR00T ecosystem |
| Spot/Stretch are real commercial businesses with blue-chip logos (DHL, Gap, H&M, Maersk) — rare in this field | Leadership vacuum: interim CEO since 2026-02; founder's research energy sits outside the company (RAI Institute) |
| Safety-standards pen-holder: BD's head of safety co-leads ISO 25785-1 drafting ([Safety & regulation](safety-regulation.md)) | Korean union has blocked domestic deployment; labor politics shadow the flagship customer |
| Chaebol supply chain: Mobis actuators, LG Energy batteries, RAI/TRI/DeepMind research triangle | Mass production is a **2028 promise** while Figure, Agility, and Chinese vendors ship at volume in 2026 ([Humanoids](humanoid-robots.md)) |

**Skeptic case**: BD has been the industry's demo king for 20 years with ~$110M revenue to show for it; the Atlas plan's anchor numbers (25K units, 30K/yr factory, 2028) are all forward-looking Hyundai commitments, not market orders; the DeepMind dependency means the hardest, most differentiating layer of the stack belongs to someone else; and if humanoid task economics disappoint, Hyundai's appetite for ₩0.5T/yr losses is the single point of failure. **Steel-man**: nobody else combines proven robot hardware at Spot/Stretch commercial maturity with an automaker's factory capacity and a frontier-lab AI partner — if humanoids become an automotive-grade manufacturing game (the bet), BD is structurally better positioned than software-first rivals.

## Manufacturing & supply-chain posture

- **In-house assembly, chaebol-integrated components** — neither Figure-style full vertical integration nor Agility-style contract manufacturing.
- **Current**: Atlas production began at the Boston-area HQ (2026-01); **$100M expansion of a robotics/AI center near Waltham** announced 2026-06 in preparation for 2028 mass production (KED).
- **Scale plan**: dedicated **30,000 robots/yr US factory by 2028** under Hyundai's $26B US investment program (site/details unconfirmed as of 2026-07).
- **Actuators — Hyundai Mobis** (announced CES 2026): first commercial customer of Mobis's robotics-components business; actuators ≈ **60% of humanoid material cost** (Korea Herald); the group plans a Mobis-operated **US plant with 350,000+ actuators/yr capacity from 2028** — sized to the full 30K-robot run (Seoul Economic Daily: "weighing" 2026-03 → "will establish" 2026-05) — and Mobis plans to expand into grippers, sensors, controllers, and battery packs.
- **Batteries — LG Energy Solution**: supply contracts covering the top-3 US humanoid programs (Tesla, Boston Dynamics, Figure); high-nickel ternary chemistry (KED, 2026-07).
- **Design-for-manufacture doctrine**: production Atlas delivers "almost an order of magnitude reduction in complexity" and "way, way less unique parts" vs the prior generation (Rodriguez); "every component has been designed for compatibility with automotive supply chains" (Jackowski). This is Hyundai's core value-add: treating the humanoid as a vehicle program, with Tier-1 suppliers (Mobis, LG) slotting into existing automotive qualification pipelines.
- For an ODM/EMS reader: BD is a **closed shop** — no known ODM/EMS outsourcing, no reference-design licensing, components sourced from group-affiliated Tier-1s. Opportunity surface is at the component tier (actuator subcomponents, reducers, sensors, battery packs feeding Mobis/LG), not at assembly.

## Sources

- https://bostondynamics.com/blog/boston-dynamics-unveils-new-atlas-robot-to-revolutionize-industry/ — production Atlas announcement (2026-01-05): 56 DoF, 2.3 m reach, 50 kg, battery swap, RMAC + DeepMind 2026 allocation, Playter/Jackowski quotes, Orbit modes (official)
- https://bostondynamics.com/blog/boston-dynamics-google-deepmind-form-new-ai-partnership/ — Google DeepMind partnership: Gemini Robotics as Atlas "embodied mind," joint research fleets (official)
- https://techcrunch.com/2026/01/05/boston-dynamicss-next-gen-humanoid-robot-will-have-google-deepmind-dna/ — DeepMind-on-Atlas coverage
- https://www.therobotreport.com/boston-dynamics-google-reunite-on-next-gen-atlas-humanoid/ — Google "reunion" framing, spec confirmation
- https://www.hyundainews.com/releases/4664 — Hyundai CES 2026 AI-robotics strategy: RMAC 2026, Metaplant 2028 → assembly 2030, 30K/yr capacity (official)
- https://interestingengineering.com/ai-robotics/hyundai-25000-atlas-humanoid-robots-us-plants — 25,000+ Atlas across Hyundai/Kia plants; Kia Georgia 2029
- https://www.techtimes.com/articles/317005/20260522/hyundai-commits-25000-atlas-robots-own-factories-union-blocks-deployment-without-labor-deal.htm — 25K = ~83% of 30K/yr capacity; union standoff
- https://en.sedaily.com/finance/2026/01/22/not-a-single-robot-without-agreement-hyundai-motor-union — union statement (2026-01-22), ₩200M unit-cost estimate
- https://en.sedaily.com/news/2026/04/05/hyundai-motor-to-break-ground-on-ulsan-plant-rebuild-next-20260405 — Hyundai rules out domestic Atlas deployment; overseas-first
- https://www.kedglobal.com/robotics/newsView/ked202601200007 — Atlas priced below ~2 years of two US manufacturing workers' payroll (~$320K ceiling); analyst $130–140K band
- https://www.kedglobal.com/robotics/newsView/ked202606210001 — Hyundai buys SoftBank's remaining 9.65% for $325M; 2021 put-option mechanics; approval 2026-06-22
- https://www.kedglobal.com/robotics/newsView/ked202606250011 — $100M Massachusetts robotics/AI center expansion; 2028 mass-production prep
- https://www.kedglobal.com/robotics/newsView/ked202603040003 — Hyundai: industrial use before home application
- https://www.kedglobal.com/batteries/newsView/ked202607020005 — LG Energy Solution battery supply to Tesla, Boston Dynamics, Figure (high-nickel ternary)
- https://www.koreaherald.com/article/10651569 — Hyundai Mobis actuator supply for Atlas; actuators ~60% of material cost; first robotics-components customer
- https://en.sedaily.com/finance/2026/03/06/hyundai-mobis-weighs-us-plant-for-atlas-robot-parts — Mobis weighing US plant, 350,000 actuators/yr from 2028 (single source)
- https://bostondynamics.com/news/hyundai-mobis-forms-strategic-collaboration-framework-with-boston-dynamics/ — Mobis–BD strategic collaboration framework (official)
- https://rai-inst.com/resources/press-release/boston-dynamics-atlas-partnership/ — RAI Institute RL partnership (2025-02): sim-to-real, whole-body loco-manipulation, Spot RL kit lineage (primary)
- https://bostondynamics.com/blog/large-behavior-models-atlas-find-new-footing/ — TRI LBM on Atlas: ~450M-param language-conditioned diffusion policy (official, 2025-08)
- https://group.dhl.com/en/media-relations/press-releases/2025/dhl-group-signs-mou-with-boston-dynamics-and-accelerates-cross-business-automation-strategy.html — DHL MoU for 1,000+ additional Stretch units, 700 cases/hr, partnership since 2018 (primary, 2025-05-13)
- https://wwd.com/sourcing-journal/logistics/boston-dynamics-stretch-robot-warehouses-gap-hm-dhl-supply-chain-1238793351/ — Stretch customers Gap/H&M/DHL; demand detail
- https://www.retailtouchpoints.com/features/retail-success-stories/why-gap-turned-to-robots-for-an-unpopular-fulfillment-task-unloading-boxes — Gap rollout path (Fishkill → TN → OH/TX/CA); 700 cases/hr
- https://venturebeat.com/ai/boston-dynamics-buy-spot-robot-74500 — Spot commercial launch price $74,500 (2020-06)
- https://www.roboticscenter.ai/companies/boston-dynamics — Spot 3,000+ deployed; >500 robots / ~$130M revenue in 2025 (aggregator, unverified)
- https://techcrunch.com/2026/02/10/boston-dynamics-ceo-robert-playter-steps-down-after-30-years-at-the-company/ — Playter departure (last day 2026-02-27); McMaster interim CEO
- https://en.wikipedia.org/wiki/Boston_Dynamics — founding 1992, MIT spin-off, ownership chain (Google 2013, SoftBank 2017, Hyundai $880M/80%), ~1,000 employees, product dates
- https://www.ilyo.co.kr/?ac=article_view&entry_id=471437 — FY2022–23 loss trend (revenue ₩78.2B→₩91B; net loss ₩255.1B→₩334.8B); Hyundai funding posture (Korean, 2024 — does NOT contain FY2025 figures)
- https://finance.biggo.com/news/t1MPBJ0BNZYCTTDvFwpX — FY2025 revenue ₩150.1B / net loss ₩528.4B; ~₩30T valuation framing; $880M-for-80% at $1.1B (aggregator of Korean coverage)
- https://www.asiatoday.co.kr/kn/view.php?key=20260528010008586 — ₩2.2109T five-year accumulated equity-method losses across robotics/autonomy/AAM affiliates (Korean, 2026-05-28)
- https://www.bloter.net/news/articleView.html?idxno=640915 — 2025-08 rights offering ~$970M (~₩1.3T), larger than prior three rounds combined (₩982B); participant breakdown incl. SoftBank pro-rata ~$121M (Korean)
- https://bostondynamics.com/wp-content/uploads/2026/01/atlas-spec-sheet.pdf — official Atlas spec sheet (12/2025): 1.9 m / 90 kg, 50 kg instant / 30 kg sustained / 20 kg one-hand lift, 4 h battery (2 h heavy lifting), 3-min autonomous battery swap, IP67, −20–40 °C, autonomous/VR-teleop/tablet modes, fleet skill sharing
- https://www.bostonglobe.com/2026/03/04/business/robots-hyundai-atlas-musk-optimus/ — Samsung Securities (Esther Yim): CES analyst briefing on initial $130–140K Atlas price
- https://en.sedaily.com/news/2026/05/20/hyundai-builds-robot-ecosystem-in-us-from-atlas-components — group to establish Mobis-operated US actuator plant (350K+/yr from 2028)
- https://www.newsspace.kr/news/article.html?no=13851 — SoftBank put-option deadline; NASDAQ listing decision framing (Korean, unverified)
- https://douglasresearch.substack.com/p/boston-dynamics-rights-offering-of — ~₩1.2–1.3T rights offering; potential NASDAQ IPO 2027/28 (single source, unverified)
- https://www.bloter.net/news/articleView.html?idxno=666151 — Hyundai buying at "2021 price tag": put exercised on 2021-agreed terms, not market valuation (Korean)
- https://www.forbes.com/sites/johnkoetsier/2026/07/02/boston-dynamics-new-atlas-humanoid-robot-order-of-magnitude-simpler/ — fifth-gen Atlas complexity reduction; Rodriguez quote; prior-gen >$200K build cost
- https://diginomica.com/ces-2026-can-boston-dynamics-atlas-robot-carry-humanoid-industry-its-shoulder — Playter full CES quote; skeptic case (Moravec's paradox, China cost headwind)
- https://www.automate.org/robotics/industry-insights/boston-dynamics-to-begin-production-on-redesigned-atlas-humanoid-in-2026 — 2026 allocations committed; external customers early 2027
- https://www.hyundaimotorgroup.com/en/news/CONT0000000000199186 — Atlas named "Best Robot," Best of CES 2026 (official Hyundai)
