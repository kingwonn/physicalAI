---
title: "Company Deep Dive: Skild AI"
slug: company-skild
updated: 2026-07-05
confidence: verified
---
> Skild AI (Pittsburgh, founded 2023-05 by CMU professors Deepak Pathak and Abhinav Gupta) is the most highly valued independent robot-brain lab: a $1.4B Series C at >$14B post-money (announced 2026-01-14, SoftBank lead; NVentures, Bezos Expeditions, Macquarie) — roughly triple its mid-2025 mark in ~7 months. Its bet is the "omni-bodied" **Skild Brain**: one foundation model claimed to control any body — quadrupeds, humanoids, tabletop arms, mobile manipulators — trained sim-first ("a universe with 100,000 different robots") plus internet human video, with real-robot data only for post-training. Unlike deliberately pre-revenue [Physical Intelligence](company-pi.md), Skild is revenue-first: it claims 0 → ~$30M revenue during 2025 (company-reported) from security/inspection, construction, delivery, data-center, warehouse, and manufacturing deployments, and in 2026 moved aggressively down-stack — Foxconn Blackwell-line deployment (2026-03), ABB/Universal Robots partnerships, and acquisition of Zebra's robotics (Fetch) AMR business (2026-04). The catch: near-total technical opacity — no papers, no open weights, no external benchmarks, unnamed customers, and funding filings that trackers cannot reconcile. Context: [Landscape: USA](landscape-usa.md), [Investment](investment.md), [Evaluation](evaluation.md), [Key people](key-people.md).

## Company at a glance

| Field | Status (as of 2026-07) |
|---|---|
| Founded | 2023-05; emerged from stealth 2024-07-09 |
| HQ / offices | Pittsburgh, PA (CMU orbit); SF Bay Area office (early 2025); Bengaluru, India |
| Founders | Deepak Pathak (CEO; CMU faculty, ex-FAIR, Berkeley PhD — curiosity-driven RL, rapid motor adaptation) and Abhinav Gupta (President; CMU RI professor since 2009, ex-FAIR founding member, 75k+ citations) — both dual-hat CMU ([Academic labs](academic-labs.md)) |
| Product | **Skild Brain** — "the industry's first unified robotics foundation model" (company framing); closed weights, no papers |
| Thesis | "Omni-bodied": one brain for any body — quadruped, humanoid, arm, AMR — vs per-embodiment models |
| Valuation | **>$14B post** (Series C, 2026-01-14) — highest of any robot-brain lab; ~2.5x PI's closed $5.6B mark |
| Disclosed raised | ~$1.83B tracked (A $300M + B ~$100–135M + C $1.4B; Crunchbase: >$1.83B); Pathak says ">$2B" (via Bloomberg/TechCrunch) — records don't reconcile (see skeptic case) |
| Key investors | SoftBank (led B + C), Lightspeed, Coatue, Sequoia, Felicis, NVentures (NVIDIA), Bezos Expeditions, Amazon (Industrial Innovation Fund + Alexa Fund), Macquarie, 1789 Capital, IQT (In-Q-Tel), CMU; strategics LG, Schneider Electric, CommonSpirit, Salesforce Ventures (Samsung joined the 2025 round, ~$10M — absent from the company's own Series C list) |
| Revenue | 0 → ~$30M during 2025 (company-reported, no named customers); "growing rapidly" |
| Deployment sectors | Security & facility inspection, construction, last-mile/point-to-point delivery, data centers, warehouses, factory assembly (company list) |
| Named partners / M&A | Foxconn (NVIDIA Blackwell lines, Houston), ABB Robotics, Universal Robots (both GTC 2026-03); acquired Zebra Technologies' robotics unit (ex-Fetch Robotics) 2026-04-15 |
| Headcount | Not disclosed; 24 (2024-11), 25+ (2025-07) — extreme valuation-per-employee even by robot-brain-lab standards |

## 技术路线 Tech route & architecture

What is public (no papers, no model cards — everything below is company blogs, the NVIDIA case study, and press):

- **Hierarchical two-tier policy stack**: (1) a high-level policy issuing low-frequency manipulation/navigation/task-intent commands; (2) a low-level policy translating them into high-frequency joint angles and motor torques for whatever body is attached. No parameter counts, backbone identity, or action-decoding scheme disclosed — vs [PI](company-pi.md)'s fully published flow-matching VLA lineage ([VLA models](vla-models.md)).
- **Sim-first pre-training at morphology scale**: "We created a universe with 100,000 different robots and trained our AI to control them all"; "[a]fter a millenia of simulated time" (sic) a resilient omni-bodied brain emerged (company blog, 2025-09). Thousands of robot instances across humanoids/quadrupeds/arms with randomized morphologies — the claim is that morphology diversity *forces* in-context adaptation instead of memorizing one body's controller. Direct descendant of Pathak's CMU rapid-motor-adaptation line ([Locomotion](locomotion.md)).
- **Internet human video as pre-training** — humans treated as "biological robots" whose internet videos serve as demonstration data (Pathak's framing); real-robot data used only for targeted post-training and deployment refinement. Pathak's stated position (Davos interview, 2026-01): the industry approaches data wrong; teleop-heavy fleets and even "Tesla's self-driving dataset won't help Optimus generalize."
- **Claimed emergent adaptation** (company demos, zero-shot on robots excluded from training): recovers from limb loss (effective locomotion after ~7–8 s of in-context adaptation) and a broken leg (walks again within ~2–3 s), detects jammed wheels and switches to a legged gait, walks on stilts (company blog, 2025-09); handles payloads up to 1.5x body weight and reaches "60%–80% task performance within hours of data collection" (NVIDIA case-study figures — vendor-published, unverified).
- **NVIDIA-stack native**: trains with Isaac Lab (RL), Cosmos Transfer (text-prompted environment augmentation), NVIDIA compute; Cosmos Coalition member and Newton 1.0 GA adopter (GPU-rack assembly RL) — see [Simulation](simulation.md), [NVIDIA](company-nvidia.md). Witt (New Yorker, 2026-07) found every robot at Skild ran NVIDIA silicon and trained in NVIDIA sim.
- **How the route differs from rivals**: vs PI — sim+video-first instead of teleop-first, locomotion+manipulation breadth instead of manipulation depth, closed instead of open, revenue instead of research purity. vs NVIDIA GR00T — Skild sells the brain as product; NVIDIA gives models away to sell the platform (and is Skild's investor + infrastructure vendor simultaneously). vs [Figure](company-figure.md)/[Tesla](company-optimus.md) — no body of its own (until the Fetch AMR acquisition), embodiment breadth as the moat.
- Company claimed at launch it trains on "at least 1,000 times more data points than competing models" (2024, company claim, unverifiable — no dataset disclosure).

## The bet / vision

- **Omni-bodied is the product, not a training trick**: "The Skild Brain can control robots it has never trained on, adapting in real time to extreme changes in form or environments" (Pathak, Series C). "The model is forced to adapt rather than memorize — much like intelligence in nature" (Pathak). Gupta: robots must "operate dynamically in complex environments, without requiring preprogrammed instructions."
- **Physical intelligence as the path to AGI**: Pathak argues physical intelligence — not language — is the real foundation of AGI (Davos, 2026-01); "Learning by experience, and not pre-programming, is the step change that has happened in robotics" (NVIDIA case study).
- **Anti-humanoid-hype, pro-any-body**: Pathak refuses to keep a humanoid in his own home — "People are using appearance as a way to misguide the public. If you make a robot humanlike, you expect it to have humanlike capabilities. But technology is far behind that" (New Yorker, 2026-07). The omni-bodied bet is an explicit hedge on form factor ([Visions](visions.md), [Humanoids](humanoid-robots.md)).
- **Same "one brain, any body" church as PI, different liturgy**: PI treats commercialization as a distraction and publishes everything; Skild treats deployment as the data engine ("shifting from programming tasks to building systems that continuously learn and improve, even during deployment" — Pathak on Foxconn) and publishes nothing. Investor framing from the Series A: "A GPT-3 moment is coming to the world of robotics" (Stephanie Zhan, Sequoia).
- Enterprise first, consumer homes later (company stated priority, Series C).

## Products & deployments (real numbers where they exist)

| Deployment / product | Date | What's claimed (and what's verifiable) |
|---|---|---|
| Skild Brain public unveil | 2025-07-29 | Stair-climbing under adversarial conditions, fine-grained assembly, dishwashing demos; "safe to use around humans" claim (trained to apply low force — technical.ly relaying company); no benchmarks, no third-party evals |
| Revenue-generating deployments: security & facility inspection, construction, delivery, data centers, warehouses, factory assembly | during 2025 | **0 → ~$30M revenue in "a few months" of 2025** (company-reported); deployments "including security and facility inspection, last-mile and point-to-point delivery, warehouses, manufacturing, data centers, and construction tasks" (Crunchbase News, echoing the company list); zero named customers; technical.ly additionally reported the company "became profitable" in 2025 (single-source, unverified — implausible against frontier-model compute burn without qualification) |
| **Foxconn: NVIDIA Blackwell GPU-server assembly lines, Houston** | announced GTC 2026-03-16 | Skild Brain on Foxconn's robotic lines (dual-arm manipulators, high-precision assembly); "the first public mass-deployment" of Skild's model after years of testing (technical.ly's characterization); explicit data-flywheel framing; robot counts and line scope undisclosed |
| ABB Robotics + Universal Robots partnerships | GTC 2026-03-16 | Embedding Skild's "shared intelligence layer" into widely deployed industrial and cobot fleets — retrofit route into existing installed bases; commercial terms undisclosed |
| **Acquisition: Zebra Technologies' robotics automation unit (ex-Fetch Robotics) + Symmetry Fulfillment orchestration** | 2026-04-15 | Terms undisclosed; Zebra says it received cash plus an equity stake in Skild; Zebra had paid $290M in 2021 for the 95% of Fetch it didn't own (deal valued Fetch at ~$305M). Gives Skild an AMR product line, a warehouse orchestration platform, and a real customer base; pitch: humanoids pick, quadrupeds inspect, arms pack, AMRs haul — one brain orchestrating all |
| Demo bodies | ongoing | Unitree quadrupeds/humanoids and commodity arms in press demos (per New Yorker and demo footage) (unverified as to full fleet mix); Pittsburgh street/park/fire-escape navigation, desk cleanup, AirPod-case insertion |

- Independent ground truth is thin and mixed: Witt's firsthand New Yorker demo (2026-07 issue) — a Skild-driven Unitree handled an upright cup but **flailed when the cup was laid on its side** — the perturbation-fragility pattern documented across the field in [Evaluation](evaluation.md).
- The $30M figure, if real, would be the largest disclosed revenue of any robot-brain lab (PI: $0 by choice; [Unitree](company-unitree.md), a hardware maker, books ~$235M for calibration). No filing, audit, or customer list backs it (as of 2026-07).

## Business model & unit economics

- **Model**: license the brain, let others own the body — API access / per-usage licensing, fine-tuning services, and OEM integration licensing (per Contrary Research's breakdown, pre-revenue era), plus full-stack solutions where Skild delivers the whole deployment (its security/inspection offering; and now Fetch AMRs + Symmetry orchestration post-acquisition). Revenue-first stance is the explicit anti-PI position ([Company: PI](company-pi.md) — Groom refuses commercialization talk; Pathak reports revenue in every funding release).
- **Deployment = data**: every paying deployment feeds the flywheel; customers effectively subsidize training-data collection ([Data](data.md), [Data foundry](data-foundry.md)).
- **Claimed unit economics** (NVIDIA case study, vendor-published): Skild-driven commodity robots at "$4,000–$15,000 per system vs $250,000+ conventional automation," ~10x total-cost-of-ownership reduction — the pitch that cheap Chinese-made bodies + licensed brain undercut bespoke integrators. No customer-verified TCO data public.
- **Revenue mix opacity**: nothing public separates recurring brain-licensing from one-off integration/pilot revenue in the ~$30M; post-Zebra, AMR hardware and orchestration-software revenue will further blur the "pure brain licensor" story (watch item).
- **Capital position**: ~$1.84B tracked raised; Series C alone ($1.4B) exceeds every US robot-brain rival's total except Figure-class hardware players ([Investment](investment.md)). Burn undisclosed.

## Strengths / weaknesses vs peers

**Strengths**
- **Only robot-brain lab with a revenue narrative** (~$30M claimed 2025) — de-risks the "brains never monetize" objection that hangs over PI; SoftBank/NVIDIA/Bezos all doubled in on it.
- **Embodiment breadth is real differentiation**: locomotion + manipulation + navigation across quadrupeds/humanoids/arms/AMRs, rooted in Pathak/Gupta's decade of sim2real and adaptation research — PI is arm/manipulation-centric; Figure/Tesla are single-body.
- **Capital + strategic web**: most-funded pure brain lab; SoftBank (which is also buying ABB Robotics for $5.375B — a captive future distribution channel, see [Visions](visions.md)), NVIDIA (compute + GR00T-ecosystem seat), Amazon (warehouse channel), Korean chaebol cluster (LG, Samsung, Mirae, KIC — consumer-robot adjacency), In-Q-Tel (security/government demand signal), Schneider (industrial distribution), CommonSpirit (healthcare).
- **Installed-base strategy**: ABB/UR retrofits + Fetch AMR fleet + Foxconn lines monetize robots that already exist, rather than waiting for humanoids to work ([Open problems](open-problems.md)).

**Weaknesses / skeptic case**
- **Opacity is total**: no papers, no open weights, no model cards, no external benchmarks, no named customers, no audited revenue. Every capability number traces to company blogs or its vendor-investor NVIDIA. PI publishes and open-sources; NVIDIA publishes; Skild asks for trust ([Evaluation](evaluation.md)).
- **Funding record doesn't reconcile**: press reported a ~$500M Series B at $4.5–4.7B (2025-04/05); trackers record only ~$100–135M closed (Crunchbase $135M; Robot Report's 2025-07 running total of "$435M across two rounds" corroborates); the only Skild Form D found by technical.ly was ~$1M via an SPV (filed under "cgf2021-llc"; PitchBook's total was then ~$814M); disclosed rounds sum to ~$1.83B while Pathak says ">$2B." None of this is fraud evidence — but for a $14B company it is unusually murky (as of 2026-07).
- **Valuation-to-proof gap**: >$14B on ~$30M company-reported revenue is ~470x forward-unclear sales, priced 7 months after a $4.5B mark — repricing velocity the [Investment](investment.md) page flags as bubble-pattern.
- **Independent demo evidence cuts against robustness**: the New Yorker cup failure is the only firsthand third-party test on record, and Skild failed it.
- **Channel conflicts ahead**: owning Fetch AMRs puts Skild in competition with the AMR makers it wants as licensees; NVIDIA is simultaneously investor, supplier, and competitor (GR00T); SoftBank's ABB could privilege — or absorb — Skild.
- **Same thin talent pool** as every rival: the bet concentrates on two dual-hat professors; CMU lineage is deep but the deployed-fleet engineering muscle (vs research pedigree) is unproven at scale ([Key people](key-people.md)).
- Steel-man: revenue-first discipline generates exactly the messy real-world data the sim-first route lacks; if the omni-bodied claims are even half-true, Skild owns the widest embodiment coverage in the industry and the only brain-lab P&L that survives a funding winter.

## Manufacturing & supply-chain posture (ODM/EMS lens)

- **Builds no robot bodies by design** (pre-2026): pure software/model company; demo and deployment fleets ride on third-party commodity hardware — Unitree-class quadrupeds/humanoids, commodity cobot arms (partially unverified fleet mix). The brain-licensing thesis makes hardware partners — OEMs, ODMs, EMS — the body suppliers by construction: Skild's TCO pitch explicitly depends on $4–15k commodity robots, i.e., on Chinese-cost hardware supply chains ([Hardware](hardware.md), [Landscape: China](landscape-china.md)).
- **Foxconn is the marquee EMS relationship** (as of 2026-03): Skild brains run Foxconn's dual-arm assembly robots building NVIDIA Blackwell GPU racks in Houston. Dual significance for ODM readers: (a) EMS lines themselves are the customer — "AI-driven manufacturing" sold to contract manufacturers; (b) Foxconn has its own robot-building ambitions, making it a potential high-volume body channel for Skild brains. Newton-based GPU-rack-assembly RL work (per NVIDIA, [Simulation](simulation.md)) suggests sim-trained cells moving onto real EMS lines.
- **Retrofit-first go-to-market**: ABB Robotics and Universal Robots partnerships target the existing installed base of industrial arms and cobots — no new manufacturing capacity required, revenue from software attach. SoftBank's pending ABB Robotics acquisition (closing ~mid-late 2026) could turn this into a captive OEM channel under common ownership.
- **Post-Zebra, Skild owns hardware products for the first time**: the ex-Fetch AMR portfolio plus Symmetry Fulfillment orchestration. Fetch AMRs have historically been contract-manufactured/US-assembled at modest volumes (unverified current arrangement); nothing public suggests Skild wants factories — the acquisition reads as buying a fleet, an orchestration layer, and warehouse data, not a manufacturing operation.
- **Compute supply chain**: single-vendor NVIDIA — training (Isaac Lab, Cosmos, DGX-class infra) and, per Witt's reporting, onboard inference silicon too. NVentures equity aligns but also concentrates dependency ([NVIDIA](company-nvidia.md)).
- **What ODMs should take away** (as of 2026-07): Skild is the clearest "Android licensor" analog in Physical AI — it needs body partners at every form factor, has capital to fund integrations, and (except in warehouse AMRs, post-Fetch) does not compete with hardware makers. The open questions for a body partner: no published integration SDK/API spec, no certification program, and no disclosed per-robot licensing economics.

## Sources

- https://www.skild.ai/blogs/series-c — primary Series C announcement (2026-01-14): $1.4B, >$14B, full investor list (no Samsung), $30M revenue claim, deployment sectors
- https://techcrunch.com/2026/01/14/robotic-software-maker-skild-ai-hits-14b-valuation/ — Series C corroboration; Pathak ">$2B raised" via Bloomberg; prior $4.5B mark
- https://www.bloomberg.com/news/articles/2026-01-14/robotics-startup-skild-valued-above-14-billion-after-softbank-led-funding-round — SoftBank-led round, >$14B valuation
- https://www.therobotreport.com/skild-ai-raises-1-4b-building-omni-bodied-robot-skild-brain/ — extended investor list (incl. IQT, KIC, Mirae), offices (Pittsburgh/SF/Bengaluru), Pathak/Gupta quotes, deployment sectors
- https://news.crunchbase.com/venture/robotics-startup-skild-ai-triples-valuation/ — valuation tripling in ~7 months; total-raised >$1.83B; Series B recorded at $135M/$4.5B; deployment-environment list
- https://www.businesswire.com/news/home/20240709306400/en/Skild-AI-Raises-%24300M-Series-A-To-Build-A-Scalable-AI-Foundation-Model-For-Robotics — Series A (2024-07-09): $300M at $1.5B; Lightspeed/Coatue/SoftBank/Bezos leads; Amazon, CMU, Sequoia participation
- https://techcrunch.com/2025/12/08/softbank-and-nvidia-reportedly-in-talks-to-fund-skildai-at-14b-nearly-tripling-its-value/ — pre-C talks; "$4.7B in May" when it raised the reported $500M; LG Technology Ventures/Samsung/NVIDIA in B
- https://finance.yahoo.com/news/nvidia-samsung-back-4-5b-203049332.html — NVIDIA ~$25M + Samsung ~$10M into the ~$4.5B 2025 round
- https://www.therobotreport.com/skild-ai-is-giving-robots-a-brain/ — Skild Brain unveil (2025-07-30); "$435M across two rounds" running total; 25+ employees; Pathak stair-climbing/assembly quote
- https://technical.ly/entrepreneurship/skild-brain-unveiled-ai-human-robot/ — SEC Form D investigation: only ~$1M SPV filing found vs $814M PitchBook total; hiring footprint
- https://technical.ly/entrepreneurship/skild-ai-1-4-billion-raise/ — "became profitable, ~$30M in 2025" phrasing (single source); Form D absence flag
- https://www.skild.ai/blogs/omni-bodied — omni-bodied thesis primary: 100,000-robot simulation universe, limb-loss/gait-switch/stilts zero-shot claims
- https://www.skild.ai/blogs/building-the-general-purpose-robotic-brain — data pyramid (sim + internet video pre-train, real-world post-train); two-tier high/low-level policy architecture
- https://www.nvidia.com/en-us/case-studies/skild-ai/ — NVIDIA case study: Isaac Lab + Cosmos Transfer usage, "millennium of experience within days," 60–80%-within-hours, $4–15k vs $250k+ TCO claims, Pathak quote
- https://nvidianews.nvidia.com/news/nvidia-and-global-robotics-leaders-take-physical-ai-to-the-real-world — GTC 2026-03-16: Skild x ABB Robotics, Universal Robots, Foxconn Blackwell-line partnerships
- https://technical.ly/entrepreneurship/pittsburgh-skild-ai-nvidia-foxconn-robotics-deployment/ — Foxconn Houston deployment detail: "first public mass-deployment," data-flywheel framing, Pathak quote (2026-03-18)
- https://www.skild.ai/blogs/skild-zebra — primary Zebra robotics acquisition post (2026-04-15): Fetch lineage, Symmetry Fulfillment, end-to-end warehouse pitch
- https://www.therobotreport.com/skild-acquires-fetch-robotics-assets-from-zebra-automation/ — Zebra's Fetch purchase price (2021); Skild's plans for the Fetch installed base
- https://www.dcvelocity.com/material-handling/robotics/zebra-sells-off-its-fetch-amr-division — deal consideration: "in addition to receiving cash consideration, it also took on an equity stake in Skild AI" (Zebra statement); corroborates Zebra press release
- https://www.zebra.com/us/en/about-zebra/newsroom/press-releases/2021/zebra-technologies-to-acquire-fetch-robotics.html — Zebra's 2021 Fetch acquisition: $290M cash for the remaining 95%, ~$305M implied value
- https://research.contrary.com/company/skild-ai — founding story, founder bios, Series A detail, 24 headcount (2024-11), projected licensing/API business model, "1,000x more data" claim
- https://sources.news/p/skild-ai-ceo-robotics-brain-davos — Pathak Davos interview (2026-01): data-strategy critique, Tesla/Optimus skepticism, physical-intelligence-as-AGI thesis
- https://www.newyorker.com/magazine/2026/07/06/are-humanoid-robots-ready-to-be-deployed — Witt firsthand: Skild-driven Unitree cup failure; Pathak anti-humanoid quotes; NVIDIA silicon ubiquity at Skild (paywalled; existence/title/thrust corroborated via secondary links, but quote wording not independently re-checkable by open search as of 2026-07-05)
- https://lsvp.com/stories/skild-is-bringing-generative-ai-to-the-real-world/ — Lightspeed investment memo framing (Series A lead)
