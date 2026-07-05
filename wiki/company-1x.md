---
title: "Company Deep Dive: 1X Technologies"
slug: company-1x
updated: 2026-07-05
confidence: verified
---
> 1X Technologies (founded May 2014 as Halodi Robotics in Moss, Norway by Bernt Børnich; HQ Palo Alto, CA since ~2025) is the only major humanoid maker betting **home-first**: its ~30 kg, 22 dB, tendon-driven NEO opened consumer pre-orders 2025-10-28 at **$20K or $499/mo** and booked 10,000+ deposits in five days (company-reported), with US home deliveries promised before end-2026. The stack is safety-first hardware (low-inertia tendon drives, soft lattice-polymer body, HIC <250) + a small onboard VLA (**Redwood**, 160M params) + the **1X World Model**, with human teleoperation ("Expert Mode") backstopping autonomy — which is both the data flywheel and the privacy controversy. Manufacturing is radically in-house: the 58,000 sq ft Hayward, CA factory (opened 2026-04/05) builds its own motors, batteries, tendons and structures, targeting 10K/yr now and 100K+/yr by end-2027 (company targets). Counterweights: a reported ~$1B raise at ~$10B has not been confirmed closed (as of 2026-07), disclosed funding is only ~$136.5M through Series B, the fluent demos are teleoperated (Witt, New Yorker), and industrial traction is thin next to [Figure](company-figure.md) and Agility. Context: [Humanoids](humanoid-robots.md), [World models](world-models.md), [Open problems](open-problems.md), [Safety & regulation](safety-regulation.md).

## Company at a glance (as of 2026-07)

| Field | Value |
|---|---|
| Founded | May 2014 as **Halodi Robotics**, Moss, Norway; rebranded **1X Technologies** 2023-03 |
| Founder / CEO | **Bernt Øivind Børnich** (decided at age 11 to build humanoids; robotics/nano-electronics, U. Oslo); co-founders Phuong Nguyen (former CTO), Jørgen Sundell, Pål Løken |
| HQ / footprint | Palo Alto, CA (consolidated 2025-07); factory Hayward, CA; second site San Carlos, CA coming online (2026); legacy engineering/manufacturing Moss, Norway |
| Headcount | 663 (2025-09, Contrary Research); ~800 observed at Bay Area HQ+factory complex (Witt reporter observation, 2026-07) |
| Products | EVE (wheeled humanoid, 2018) → NEO Beta (2024-08-30) → NEO Gamma (2025-02-21) → **NEO consumer launch (2025-10-28)** |
| AI stack | Redwood VLA (160M params, ~5 Hz, onboard Jetson Thor) + 1X World Model + off-board LLM voice; teleop "Expert Mode" backstop |
| Pricing | **$20,000** purchase (Early Access, priority 2026 delivery) or **$499/mo** subscription (ships later); $200 refundable deposit |
| Order book | 10,000+ deposits in first 5 days; first-year capacity "sold out" (company-reported); ~20,000 pre-orders slated to ship in 2026 (per Forbes, 2026-06) |
| Industrial channel | EQT partnership (2025-12-11): shared intent, up to 10,000 NEOs across EQT portfolio companies 2026–2030 |
| Disclosed funding | ~$136.5M through Series B ($23.5M A2 led by OpenAI Startup Fund 2023-03; $100M B led by EQT Ventures 2024-01) |
| Valuation | ~$820M (2024-01, reported); **seeking up to $1B at ~$10B+ since 2025-09 — no close announced (as of 2026-07, unverified)** |
| Key backers | OpenAI Startup Fund, EQT Ventures, Tiger Global, Samsung NEXT, ADT (strategic, 2021), Sandwater, Alliance Ventures, Skagerak Capital, Nistad |

## Tech route & architecture

**Hardware thesis: safety is the binding constraint for homes, so design for low mechanical impedance — not industrial payload.**

- **Tendon-driven actuation**: joints driven through tendon transmissions rather than direct high-ratio gearing — Halodi's original innovation (**Revo1** high-torque-density servo + cable-driven transmission, rejecting harmonic gears; developed **2018** per 1X's own timeline, on safe-actuator R&D running since the 2014 founding), now **Revo2** motors + "low inertia tendon drives" in NEO. High torque-density motors at low gear ratios → backdrivable, low reflected inertia, compliant on contact.
- **Result on the spec sheet** (official, as of 2026-07): **~1.68 m (5'6"), 30 kg (66 lb)** — vs ~57 kg Tesla Optimus, 61 kg Figure 03 — **22 dB** locomotion noise ("leaves rustling"; verified hands-on by Witt), lifts 70 kg (154 lb), carries 25 kg (55 lb), 18 lb arm payload; 22-DoF hands ×2, 7-DoF arms; 842 Wh battery, ~4 h runtime, 5G/WiFi; soft **3D-lattice polymer body** with knit textile cover, no external pinch points, **HIC rating <250** (head-injury criterion, company-published).
- **Onboard compute**: "NEO Cortex" = NVIDIA Jetson Thor, up to 2,070 FP4 TFLOPS ([Landscape: USA](landscape-usa.md)); dual 8.85MP 90 Hz stereo fisheye cameras, 4 beamforming mics.
- **Redwood** (announced 2025-06-10): a deliberately **small** VLA — **160M parameters at ~5 Hz**; fuses pretrained language embeddings + ViT vision tokens + proprioception (joint positions *and* applied forces), decodes through a diffusion policy into whole-body NEO/EVE actions; trained on teleop + autonomous data from the EVE and NEO fleets; runs entirely onboard. Conversation is handled by an off-board LLM. Contrast: Figure Helix 02 is a 3-tier 7B/80M/10M hierarchy at up to 1 kHz — see [VLA models](vla-models.md).
- **1X World Model (1XWM)** (paper 2025-06-16; shipped into NEO 2026-01-12): action-conditioned video prediction used for **offline policy evaluation** and, in-product, video-prediction + inverse-dynamics so NEO attempts undemonstrated tasks; Børnich: "this marks the starting point of Neo's ability to teach itself to master nearly anything you could think to ask" (launch PR — a claim 1X's own spokesperson promptly softened to "attempt anything", per TechCrunch). A dedicated **1X World Model Lab** followed 2026-06-04 (led by Sam Sinha, ex-Luma AI). Full treatment in [World models](world-models.md).
- **Teleop as an architectural layer, not a bug**: "Expert Mode" — 1X operators (seated beside the AI team; earpiece ring changes color during remote control) pilot NEO through tasks autonomy can't do; sessions feed model training ("It's also useful data for us" — Børnich, per Witt). The Waymo-style flywheel applied to homes — see [Data](data.md), [Data foundry](data-foundry.md).
- **How it differs from rivals**: Figure/Optimus/Chinese vendors optimize industrial rigidity, payload, and cycle time, then hope to descale into homes; 1X inverted the order — mass, force, noise and skin-softness were the primary design variables from the Halodi era, and capability is expected to arrive later via fleet data. The cost is exactly what industrial buyers want: payload, speed, precision.

## The bet / vision

- **Home-first, in the founder's words**: "The home and consumer has to happen first before we go into all of these other markets" (Børnich, per Contrary Research) — the direct inverse of Figure/Agility/Boston Dynamics sequencing.
- **Why homes**: (1) the **data flywheel** — homes offer the diverse, long-tail manipulation data industrial cells never produce, and paying customers subsidize collection; Børnich touts fleet-level learning ("whatever one robot learns, every robot learns" framing) — a network effect Witt infers "may account for" 1X's rush to ship ([Open problems](open-problems.md)); (2) the consumer market is where a 30 kg safe robot has a structural advantage no industrial player can match by de-rating a 60–90 kg machine.
- **Tolerance for imperfection**: Børnich is explicitly testing whether consumers accept "**robotics slop**" — slow, occasionally failing, teleop-backstopped service — while autonomy improves (Børnich's own coinage at launch, per Gizmodo 2025-10-29; also reported by Witt, New Yorker, 2026-07-06 issue).
- **Teleop framed as a feature**: Børnich defends Expert Mode as "a better, more secure service" than letting a human cleaner into your home (on NYT's *Hard Fork* podcast, 2025-11, per Humanoids Daily) — disclosure lights, face-blurring, app-set no-go rooms, operator access only with owner permission (company-described mitigations).
- **The promise**: 2026 US home deliveries — "a promise we've made to the world, and a promise we've gotta keep" (product head Dar Sleeper, on the record to Witt, 2026-07).
- **AI candor**: Børnich has acknowledged "all our current AIs completely fail at most reasoning tasks" — the vision explicitly leans on hardware safety + teleop to bridge the autonomy gap, not on near-term AGI. Ex-VP of AI Eric Jang's framing: "all roads lead to robots" ([Key people](key-people.md)).

## Products & deployments — real numbers

| Platform | Debut | Form / cost | Deployment record |
|---|---|---|---|
| **EVE** | Prototype 2017-07; released 2018 | Wheeled humanoid, ~$100K production cost, leased ~$50K/yr (Contrary) | **140-unit agreement with ADT Commercial (2022-03, ~NOK 70M ≈ $7M/yr)** for security patrol; pilots: Sunnaas Hospital (NO), Altopack (IT, packaging), Strongpoint (retail logistics), I-Mens (BE, elder care); "EVE Industrial" variant existed; platform de-emphasized after NEO pivot |
| **NEO Beta** | 2024-08-30 | Bipedal, soft-bodied | In-home testing (limited, teleop-heavy) |
| **NEO Gamma** | 2025-02-21 | Improved iteration | Home alpha testing; NVIDIA GTC 2025 demos (teleoperated) |
| **NEO (consumer)** | Pre-orders 2025-10-28 | $20K / $499-mo, 3 colors | **10,000+ deposits in first 5 days; first-year capacity (>10K units) sold out** (company-reported); ~20,000 pre-orders by 2026-06 (per Forbes); **no confirmed third-party customer home deliveries as of 2026-07** — first Hayward production units went to internal testing/validation and R&D (2026-05) |

- **EQT industrial deal (2025-12-11)**: strategic partnership with EQT (its Series B lead's parent, >300 portfolio companies) — "shared intent" to roll out **up to 10,000 NEOs 2026–2030** in manufacturing, warehousing, logistics, facility ops, healthcare; US pilots 2026, then Europe/Asia. Note: intent-based, not booked orders; it is also a tacit hedge on the home-first thesis (TechCrunch framing: sending "home" humanoids to factories).
- **Autonomy reality check (as of 2026-07)**: Witt's site visit found the fluid NEO kitchen demo was **VR-teleoperated** ("a marionette") and 1X **declined to demo autonomy**; at the 2025-10-28 launch, the complex tasks in the launch-window press demo were fully teleoperated — "100% of its actions are tele-operated" (MKBHD on the WSJ hands-on; Tom's Guide and others on Expert Mode reliance). 1XWM-driven autonomous tasks remain simple (air-fryer baskets, toast into toasters, high-fives — TechCrunch and press consensus, 2026-01; 1X itself walked back Børnich's "any prompt" framing to "attempt anything", capability "limited to basic tasks"). See [Evaluation](evaluation.md).
- Hand durability rig observed at 2.86M finger-flex cycles; NEO confirmed ~66 lb by bridal-carry test (Witt, 2026-07).

## Business model & unit economics

- **Consumer dual-track**: $20K outright ("Early Access", priority 2026 delivery, includes charger/lint roller/carrying case) or **$499/mo subscription** shipping later; $200 refundable deposit. 10,000 × $200 ≈ only ~$2M of deposit float — the order book is an option book, not revenue (deposits refundable; mix of $20K vs $499/mo buyers undisclosed).
- **Revenue potential**: 10K first-year units ≈ $200M if all were $20K purchases (upper bound; actual mix unknown). At $499/mo, price parity with $20K takes ~40 months — subscription is a reliability/obsolescence hedge for consumers and a recurring-revenue story for 1X.
- **Hidden COGS: teleoperation labor.** Every Expert Mode hour is human labor + data acquisition; 1X discloses no teleop-hours-per-robot or staffing ratio (industry-wide gap — see [Evaluation](evaluation.md)). Jim Fan: "Babysitting these robots demands an entire operation team."
- **BOM/cost**: NEO manufacturing cost said to "mirror mid-range autonomous-vehicle expenses" (Contrary, vague); no published BOM. Compare commercial-grade humanoid BOM ~$46K on Chinese supply chains vs ~$130K Western ([Humanoids](humanoid-robots.md)) — $20K retail implies either thin/negative early margins or aggressive cost engineering via in-house motors (unverified).
- **Halodi-era RaaS precedent**: EVE leased at ~$50K/yr against ~$100K production cost — ~2-yr payback; that business (~$7M/yr ADT run-rate) was the company's only meaningful revenue history (as of last disclosure; current revenue undisclosed).
- **Funding gap is the skeptic's anchor**: ~$136.5M disclosed through 2024 vs Figure's ~$1.9B; scaling to 100K units/yr on that base requires the reported **~$1B at ~$10B** round — **still unconfirmed as closed (as of 2026-07)**; a >12x markup over the $820M (2024-01, reported) mark in ~20 months — see [Investment](investment.md) on repricing velocity.

## Strengths / weaknesses vs peers

| | Assessment |
|---|---|
| **Strengths** | Sole credible **home-category leader** (Figure's home push trails; Optimus unshipped); genuinely differentiated **safety hardware** (30 kg/22 dB/HIC<250 is not retrofittable by rivals); lowest Western price point ($20K/$499-mo); deep vertical integration incl. in-house motors; OpenAI/EQT/Samsung cap table; decade-long actuation head start (safe-actuator R&D since the 2014 founding; Revo1 2018); EQT channel de-risks consumer bet; home data flywheel if deliveries land |
| **Weaknesses** | **Teleop dependence** — headline capability is human-powered; autonomy demos withheld (Witt); **delivery risk** on the end-2026 promise (no customer units confirmed shipped as of 2026-07); **thin industrial traction** vs Agility (65K+ customer-site hours) and Figure (BMW-confirmed); ~$136.5M disclosed capital vs $1B+ peers, round unclosed; 4 h runtime/842 Wh; 25 kg carry limit; privacy objections may cap mainstream adoption; AI-leadership churn (Eric Jang exited 2026-01, succeeded by Mohi Khansari) |
| **Opportunities** | First-mover consumer brand + installed-base network effects; EQT's 300+ portfolio companies; "Made in USA" positioning amid tariff politics; subscription LTV |
| **Threats** | Tesla/Figure entering homes with 10-100x capital; Chinese sub-$10K platforms ([Unitree](company-unitree.md)); a single serious in-home injury or privacy scandal (Aaron Ames: "I don't know how 1X is actually going to get away with it" — legal exposure of home falls); UL 3300-type certification gaps — 1X has published **no third-party safety cert for NEO** (as of 2026-07, unverified absence — [Safety & regulation](safety-regulation.md)) |

- **Skeptic case, condensed**: 1X is shipping a $20K teleop terminal with an autonomy roadmap attached; order book is refundable deposits; the valuation ask (~$10B) prices in the flywheel working before any customer delivery exists. **Steel-man**: the hardware safety moat is real and verified by independent hands-on reporting; deposits-in-5-days showed real consumer demand no rival has demonstrated; and teleop-as-data is exactly how Waymo bootstrapped — the strategy is coherent even if the marketing overreached.

## Manufacturing & supply-chain posture

**Posture: maximal in-house vertical integration; no ODM/EMS contract-manufacturing relationships disclosed (as of 2026-07).**

- **Hayward, CA factory**: 58,000 sq ft, final permits 2026-01, opened 2026-04-30/05-01 ("America's first vertically integrated humanoid robot factory" — company framing), 200+ staff, initial capacity **~10,000 NEOs/yr**.
- **Made in-house**: motors, battery packs, structural parts, tendon transmissions, soft goods (lattice polymer + textile), and sensors, with dedicated lines for motors, hand assemblies, battery packs, and **tendon production** (proprietary precision braiding + post-processing).
- **Revo2 motor line**: fully automated — winds its own copper coils, fabricates stators from electrical steel on machines 1X designed itself; **17,000 motors produced** since Hayward production started (company-reported at the 2026-04-30 factory opening); motor lineage dates to Halodi-era Moss R&D (Revo1 developed 2018). In-house motors are the claimed enabler of NEO's torque-density-at-low-weight and of hitting $20K retail.
- **Outsourced components**: for parts not made in-house, 1X says it works "directly inside our suppliers' facilities" to enforce its own quality standards; supplier identities and component origins (chips aside: NVIDIA Jetson Thor) are undisclosed — no visibility on actuator-grade steel, magnets, or battery-cell sourcing (as of 2026-07).
- **Scale plan**: Hayward automation upgrades + a **second San Carlos, CA facility** coming online later 2026 → **100,000+ units/yr by end-2027** (company target); stated intent to use a hybrid of industrial automation and NEO robots themselves on the line. Historical roadmap (Contrary): thousands (2025) → tens of thousands (2026) → hundreds of thousands (2027) → millions (2028) — every prior humanoid maker has missed comparable curves.
- **Footprint history**: Moss, Norway (actuators + EVE/NEO assembly, co-located with engineering) → Montreal & Oakland expansion 2021 → HQ consolidation to Palo Alto 2025-07 → production center of gravity now California; Moss retained for engineering (role in volume production unclear, unverified).
- **Read for the ODM/EMS industry**: 1X is a **closed shop at assembly and actuation** — the opposite of an ODM opportunity at system level; openings are at the **component tier** (cells, magnets, precision steel, semiconductors, polymer lattice materials) under 1X-embedded quality regimes. Its US-assembly posture is both a tariff hedge and a marketing asset, and makes 1X the clearest test of whether Western in-house manufacturing can approach Chinese BOM economics (~$46K commercial-grade — [Landscape: China](landscape-china.md)) at 100K/yr scale. Compare [Figure's BotQ](company-figure.md) (same vertical-integration religion, industrial-first) and Agility (partner-heavier).

## Sources

- https://en.wikipedia.org/wiki/1X_Technologies — Halodi founding (2014-05, Moss), founders, EVE 2018, rebrand 2023, HQ Palo Alto
- https://research.contrary.com/company/1x — Contrary Research business breakdown: founder backstory, Revo1 transmission, ADT unit economics (~$100K cost / ~$50K-yr lease / ~$7M-yr), $210M post-A2 valuation, 663 headcount (2025-09), production roadmap, Børnich home-first and AI-limitations quotes
- https://ipvm.com/reports/halodi-robotics — ADT Commercial 140-EVE agreement analysis (2022)
- https://www.securitysystemsnews.com/article/adt-commercial-introduces-humanoid-robotics-to-security-industry — ADT-side EVE deployment confirmation
- https://www.1x.tech/discover/1x-rasies-23-5m-in-series-a2-funding-led-by-open-ai — Series A2 $23.5M, OpenAI Startup Fund lead, Tiger Global (official, 2023-03)
- https://www.1x.tech/discover/1x-secures-100m-in-series-b-funding — Series B $100M, EQT Ventures lead, Samsung NEXT (official, 2024-01)
- https://www.theinformation.com/articles/humanoid-robot-developer-1x-targets-1-billion-new-funding — reported ~$1B raise at $10B+ target (2025-09; close unconfirmed)
- https://www.humanoidsdaily.com/news/report-humanoid-robotics-firm-1x-seeking-up-to-dollar1b-at-a-valuation-of-dollar10b-or-more — prior $820M valuation (2024-01, reported); 12x markup context
- https://www.1x.tech/neo — official NEO spec sheet: 5'6"/66 lb, 22 dB, 154 lb lift/55 lb carry, 842 Wh/4 h, HIC<250, lattice polymer body, Jetson Thor Cortex, Expert Mode
- https://www.therobotreport.com/1x-announces-pre-order-launch-neo-humanoid-robot/ — pre-order launch terms (2025-10-28), $200 deposit, 2026 US / 2027 international
- https://www.forbes.com/sites/johnkoetsier/2026/04/30/1x-kicks-off-full-scale-production-of-humanoid-robot-neo/ — 10,000+ deposits in 5 days (company-reported), full-scale production start, Redwood on Jetson Thor
- https://www.globenewswire.com/news-release/2026/04/30/3285118/0/en/1x-opens-neo-factory-in-hayward-ca-america-s-first-vertically-integrated-humanoid-robot-factory-with-consumer-shipments-planned-for-2026.html — Hayward factory opening PR: 58K sq ft, 200+ staff, 10K/yr, 100K+ by end-2027 target
- https://www.1x.tech/discover/neo-factory — vertical-integration specifics: in-house motors/batteries/structures/tendons/soft goods/sensors, automated Revo2 line, 17,000 motors, supplier-embedded quality, San Carlos site
- https://thenextweb.com/news/1x-neo-humanoid-factory-hayward-10000-home-robots — first units off the line to internal R&D; San Carlos facility; 100K/yr-by-2027 automation plan
- https://www.travteks.com/blog/1x-neo-home-delivery/ — first production units to internal testers, customer deliveries targeted late 2026
- https://www.therobotreport.com/1xs-neo-humanoid-gains-autonomy-with-new-redwood-ai-model/ — Redwood announcement (2025-06-10), Eric Jang quotes, onboard-GPU deployment
- https://www.1x.tech/discover/redwood-ai — Redwood architecture: 160M params, ~5 Hz, vision+language+proprioception → diffusion policy (official)
- https://www.1x.tech/discover/world-model-self-learning — 1X World Model shipped into NEO (2026-01-12): video prediction + inverse dynamics
- https://www.globenewswire.com/news-release/2026/01/12/3217155/0/en/1x-unveils-paradigm-shift-in-humanoid-ai-neo-s-starting-to-learn-on-its-own.html — 1XWM product PR: Børnich "starting point of Neo's ability to teach itself" quote (2026-01-12)
- https://techcrunch.com/2026/01/13/neo-humanoid-maker-1x-releases-world-model-to-help-bots-learn-what-they-see/ — 1XWM release coverage: air-fryer/toaster/high-five task examples; 1X spokesperson walks back "any prompt" claim
- https://www.forbes.com/sites/johnkoetsier/2026/06/04/1x-launches-humanoid-robot-world-model-lab-you-cant-fine-tune-your-way-to-agi/ — 1X World Model Lab (2026-06-04, Sam Sinha); ~20,000 pre-orders slated to ship 2026
- https://www.1x.tech/about — official company timeline: founded 2014, Revo1 developed 2018, EVE industrial deployments 2022, NEO pivot 2023
- https://www.businesswire.com/news/home/20251211360340/en/1X-Announces-Strategic-Partnership-to-Make-up-to-10000-Humanoid-Robots-Available-to-EQTs-Global-Portfolio — EQT partnership PR: up to 10,000 humanoids, 2026–2030, portfolio use cases (official, 2025-12-11)
- https://techcrunch.com/2025/12/11/1x-struck-a-deal-to-send-its-home-humanoids-to-factories-and-warehouses/ — EQT deal framing as industrial pivot/hedge; US pilots 2026
- https://www.newyorker.com/magazine/2026/07/06/are-humanoid-robots-ready-to-be-deployed — Stephen Witt: VR-teleoperated kitchen demo, autonomy demo declined, ~800 staff observed, 66 lb/22 dB verified hands-on, 2.86M finger-cycle rig, Sleeper "promise" quote, Børnich "useful data" quote, Ames legal-exposure quote (read via Wayback snapshot; paywalled — sole source for the site-visit observations)
- https://www.humanoidsdaily.com/feed/1x-ceo-details-neo-s-two-modes-and-defends-teleoperation-as-more-secure-than-a-cleaner — Børnich teleop defense ("a better, more secure service") and two-modes explanation, made on NYT's Hard Fork podcast (2025-11)
- https://gizmodo.com/neo-wants-to-usher-in-the-era-of-robotics-slop-2000678755 — Børnich's "robotics slop" framing at launch (2025-10-29); WSJ hands-on found demo fully teleoperated
- https://www.tomsguide.com/home/smart-home/the-neo-home-robot-thats-breaking-the-internet-promises-to-change-the-world-but-theres-one-huge-problem — launch-video backlash over Expert Mode reliance; privacy mitigations (blurring, no-go zones)
- https://www.humanoidsdaily.com/news/1x-neo-launch-sparks-debate-on-autonomy-and-teleoperation — launch-window debate; MKBHD: "100% of its actions are tele-operated" (WSJ demo)
- https://www.therobotreport.com/teleop-not-autonomy-the-path-for-1x-neo-humanoid/ — analysis: teleop-first path, autonomy roadmap caveats
- https://www.humanoidsdaily.com/news/eric-jang-steps-down-as-vp-of-ai-at-1x-technologies — Jang departure (2026-01), Khansari succession
- https://evjang.com/2026/01/21/leaving-1x.html — Jang's own departure post (primary)
