---
title: "Company Deep Dive: Agility Robotics"
slug: company-agility
updated: 2026-07-05
confidence: verified
---
> Agility Robotics (founded 2015, HQ Salem, OR; spun out of Jonathan Hurst's Dynamic Robotics Lab at Oregon State via the ATRIAS→Cassie lineage) is the anti-hype humanoid company: bipedal-locomotion science first, "boring" warehouse work first, safety certification first — and now set to become **the only US-listed pure-play humanoid company** (official framing; media billed it as the first US humanoid maker to go public — Chinese peers like UBTech listed earlier in Hong Kong), via a **$2.5B pre-money SPAC merger with Churchill Capital Corp XI announced 2026-06-24** (>$620M expected gross proceeds: $420M trust + ~$200M PIPE led by Foxconn; ticker **AGLT**; expected to close in 2026). Its moat is a deployment record no rival matches: Digit has logged **65,000+ operating hours across 9 customer facilities** (GXO — the industry's first humanoid RaaS contract, 2024-06; Schaeffler; Toyota Motor Manufacturing Canada; Mercado Libre), **>100,000 totes moved** at a single GXO site, the **first OSHA-recognized NRTL field certification** of a humanoid (2025-11, company-claimed first), and **>$300M in contracted multi-year Digit v5 orders** (milestone-contingent). The skeptic case: opex of ~$111M in 2025 against small undisclosed revenue, a deliberately narrow tote-and-kitting use case, a DoF-limited platform next to dexterous rivals, and a SPAC structure with a poor sector track record. Context: [Humanoids](humanoid-robots.md), [Landscape: USA](landscape-usa.md), [Investment](investment.md), [Safety & regulation](safety-regulation.md).

## Company at a glance (as of 2026-07)

| Field | Detail |
|---|---|
| Founded | 2015, spun out of Oregon State University Dynamic Robotics Lab |
| Founders | **Jonathan Hurst** (Chief Robot Officer), **Damion Shelton** (CEO until 2024-03), **Mikhail Jones** |
| CEO | **Peggy Johnson** (since 2024-03; ex-Magic Leap CEO, 6 yrs Microsoft EVP BD under Nadella, 24 yrs Qualcomm) |
| CTO | Pras Velagapudi (Melonee Wise was CTO 2023→CPO 2024-05, left 2025-08 for KUKA) |
| HQ / footprint | Salem, OR (RoboFab factory + HQ); offices incl. Pittsburgh, Bay Area |
| Product | **Digit** biped (v4 in field; **v5** unveiled 2026-06-24, broader availability early 2027) |
| Business model | RaaS (robot + Agility Arc cloud + service subscription); some direct sales |
| Deployment record | 65,000+ hours, 9 customer facilities, >100k totes at GXO Flowery Branch (2025-11) |
| Customers | GXO Logistics, Schaeffler, Toyota Motor Manufacturing Canada, Mercado Libre; Amazon trials; >30-customer pipeline (company-reported) |
| Order book | >$300M multi-year Digit v5 orders, milestone-contingent (company-reported, 2026-06) |
| Private funding | ~$150M Series B (2022, DCVC/Playground, Amazon Industrial Innovation Fund); ~$400M Series C at ~$2.1B (2025, WP Global Partners; SoftBank, Amazon, Schaeffler) — see [Investment](investment.md) |
| Going public | SPAC w/ Churchill Capital Corp XI (Michael Klein): $2.5B pre-money, $420M trust + ~$200M Foxconn-led PIPE at $10/sh, >$620M gross, ticker AGLT, 180-day lockup, expected to close in 2026; exchange "a major North American exchange", not yet named (Churchill XI trades on Nasdaq as CCXI) |
| Financials | FY2025 opex ~$111M (vs ~$71M 2024), ~$100M cash burn (preliminary/unaudited, per filings via GeekWire); revenue undisclosed pending S-4 |
| Manufacturing | RoboFab, Salem OR: 70,000 sq ft, first purpose-built humanoid factory (2023), ~10,000 units/yr design capacity, ~75% US-sourced parts (company-reported) |

## Tech route & architecture

**Locomotion science → purpose-built logistics machine → learned whole-body control → safety-certified autonomy.** Agility's stack is the inverse of the Figure/Tesla "generalist VLA + five-finger hands" bet:

- **Spring-mass lineage, not humanoid mimicry.** Hurst's academic program (CMU PhD → OSU) built ATRIAS (DARPA-funded, first machine to mechanically embody the spring-mass model of running) and **Cassie** (2017) — the bird-legged biped later famous for a Guinness 100m bipedal-robot record. Digit's "backwards" knees, leaf-spring legs and low-inertia limbs come from animal-locomotion physics, not from copying human anatomy. See [Locomotion](locomotion.md).
- **Learned whole-body control foundation model** ("software motor cortex", per NVIDIA case study): digital twin in Isaac Sim (OpenUSD), millions of parallel RL episodes in Isaac Lab, cross-validation in containerized MuJoCo before hardware deployment. CTO Pras Velagapudi: "Isaac Sim running on NVIDIA GPUs lets us simulate years of real-world learning for Digit in just hours." See [Simulation](simulation.md).
- **Task autonomy over open-ended generality.** Digit runs structured warehouse workflows (tote handling, machine tending, sequencing) orchestrated by **Agility Arc**, Agility's cloud fleet-management platform (task assignment, WMS integration, monitoring). No public bet on an in-house generalist VLA; Agility is a Google DeepMind Gemini Robotics trusted tester and deep NVIDIA partner rather than a frontier-model lab (see [Landscape: USA](landscape-usa.md), [Company: NVIDIA](company-nvidia.md)).
- **Deliberately DoF-limited manipulation.** Digit v4 uses simple gripper end-effectors (~4-DoF arms; aggregator spec sheets disagree on exact counts — treat DoF figures as unverified); v5 adds **swappable hands/end-effectors** instead of a dexterous five-finger hand. Thesis: tote-and-case logistics doesn't need 20-DoF hands, and fewer DoF = cheaper, more reliable, easier to certify. The cost is a ceiling on task breadth vs [Figure](company-figure.md) 03's tactile hands or [Boston Dynamics](company-bostondynamics.md) Atlas. See [Tactile & hands](tactile-hands.md).
- **Safety as the differentiating layer.** Digit v5 is pitched as the first **"cooperatively safe"** AI-enabled humanoid — able to share unfenced space with people — built on a dedicated safety processor that can halt the robot independently of its AI stack, **NVIDIA IGX Thor** compute, **Halos OS**, and external facility cameras for around-corner perception. Agility is the first Halos partner — NVIDIA: **"Agility is the first company to team with NVIDIA to incorporate elements of Halos for Robotics into its proprietary safety system"** (Halos for Robotics announced 2026-06-22 at Automate); NVIDIA's ANAB-accredited **Halos AI Systems Inspection Lab** evaluates systems against IEC 61508, ISO 13849 and ISO/IEC TR 5469 in preparation for third-party certification (whether Digit formally goes through the lab is not yet disclosed — unverified). Agility's Kevin Reese (Distinguished Robotics Safety Engineer) is project leader of ISO 25785-1 in ISO/TC 299 WG 12, the first safety standard dedicated to dynamically stable mobile robots incl. humanoids — the company is literally co-writing the rules it plans to be first to pass. See [Safety & regulation](safety-regulation.md).

## The bet / vision

- Hurst's founder thesis is augmentation of scarce labor on dull work, not robot generality for its own sake: robots should take the **"dull, dirty, dangerous"** repetitive tasks (his recurring framing) while people keep the creative, varied, social work; the stated mission is **"to enable humans to be more human."** He pitches Digit as lightweight automation that can walk into an existing facility and start work without retrofitting (podcast/interview statements, paraphrased).
- On the SPAC: Hurst — **"We believe cooperative safety is the critical unlock for scaled humanoid adoption, and our next generation Digit represents an important milestone toward a future where robots become trusted partners in the workplace"** (official release). The v5 pitch is that removing fences/exclusion zones is worth more to customers than adding finger dexterity.
- Peggy Johnson's framing since 2024-03 has been explicitly anti-moonshot: **"focused on the here and now"** (TechCrunch, 2024-03) — ship revenue-generating warehouse robots now, expand scope later; "walking before backflipping." At the SPAC announcement she said **"Humanoid robots are a critical driver of American technology leadership and the future of global industry"** and sized the US manufacturing/distribution/logistics opportunity at "approximately $1 trillion" — explicitly "estimated by management" (official release).
- Strategic contrast: where Figure and Tesla sell a general-purpose future (home robots, $20K price points), Agility sells a **near-term labor product with a paying-customer record** — and is using the public markets, not private mega-rounds, to fund the scale-up. The wager is that boring, certified, unit-economic deployment compounds faster than capability demos.

## Products & deployments

### Platform generations

| Generation | Date | Key facts |
|---|---|---|
| ATRIAS | 2010s (OSU/DARPA) | Academic spring-mass biped; precursor |
| Cassie | 2017 | Legs-only biped sold to research labs (Michigan, Berkeley, et al.); Guinness 100m record (2022, OSU) |
| Digit v1–v3 | 2019–2022 | Torso + arms on Cassie legs; Ford last-mile delivery partnership (2019–20, first customer) — later abandoned in pivot to warehouse logistics |
| Digit v4 | 2023 | ~175 cm, ~65 kg, ~16 kg (35 lb) payload, gripper hands, ~8h battery w/ autonomous dock charging (aggregator specs, unverified); the fleet now in the field |
| **Digit v5** | unveiled 2026-06-24 | **50 lb (~22.7 kg) payload (+40% vs v4), up to 22 h/day operation, ~7.2 ft (2.1 m) reach, swappable hands, NVIDIA IGX Thor + Halos safety stack, "cooperatively safe" design**; broader availability early 2027 (company-reported) |

### Deployment record (the industry's most documented, as of 2026-06)

- **GXO Logistics** — industry-first multi-year humanoid **RaaS agreement (2024-06)**; Digit moves totes at the Spanx facility in Flowery Branch, GA; **>100,000 totes** by 2025-11; Agility also earned what it calls the **first OSHA-recognized NRTL field certification** of a humanoid at a live customer fulfillment site (2025-11, vs ANSI/RIA R15.08, ISO 13849, ISO 12100 — site-specific; the audited site is widely assumed to be the GXO facility but is not officially named — unverified).
- **Schaeffler** — strategic investor (2024-11) + customer; Digit loads/unloads components at the Cheraw, SC plant; Schaeffler has discussed use across its global plant network by 2030 (company statements).
- **Toyota Motor Manufacturing Canada** — commercial agreement 2026-02-19; RAV4 plant in Woodstock, Ontario; trials expanded from 3 toward 10 units, ~7 under the 2026 commercial rollout (reports differ on 7 vs 10 — treat exact count as unsettled).
- **Mercado Libre** — commercial agreement announced 2025-12-10; Digit deployed at Mercado Libre's San Antonio, TX fulfillment center, with LatAm expansion under exploration (2025-12→).
- **Amazon** — tested Digit at a Seattle-area facility (2023→); Amazon Industrial Innovation Fund is an investor; no scaled deployment announced (as of 2026-06).
- Aggregate: **65,000+ hours across 9 customer facilities** (release wording: "Through deployment commitments across nine customer facilities, Digit has accumulated more than 65,000 hours of operation" — i.e., the nine are deployment *commitments*); Agility is the only humanoid maker publishing fleet-hours at all (see [Evaluation](evaluation.md)). All figures company-reported but partially corroborated by customers (GXO, Schaeffler, TMMC announcements).

## Business model & unit economics

- **RaaS is the core model**: Agility retains ownership; customer pays subscription/usage covering robot, Agility Arc software, updates and maintenance. Widely reported company/Johnson framing benchmarks pricing at **~$30/robot-hour against fully loaded human labor cost**, with a stated target of **customer ROI < 2 years** (company-reported via press coverage; in her Atoms & Bits interview Johnson gives only "several $1,000 a month" for RaaS — treat the exact $30/hr figure as company-reported, not filing-verified).
- Aggregator estimates put RaaS at roughly **$10–15K/month/robot** and outright purchase near **$250K/unit** (both unverified; Agility doesn't publish pricing). One analyst estimate puts Digit's current operating cost at ~$10–12/robot-hour with a scaling path to $2–3 (single-source, unverified).
- Economics logic: at ~$30/hr × 20+ h/day duty cycle (v5 target 22 h), one robot ≈ 2–3 human shift-equivalents on tote work; margin expands with fleet software attach and falling unit BOM (see [Hardware](hardware.md) for sector BOM curves).
- **Order book**: >$300M multi-year Digit v5 contracts, explicitly **subject to contractual milestones** (i.e., contingent on v5 delivering); pipeline >30 customers (company-reported, 2026-06).
- **Cost reality**: FY2025 opex ~$111M, cash burn ~$100M (preliminary/unaudited); revenue undisclosed until the S-4 — sector-wide, revenue is $30M-scale at best against multi-billion valuations (see [Investment](investment.md)). SPAC proceeds (>$620M if redemptions are low) are the bridge to volume production.

## Strengths / weaknesses vs peers

| | Agility's position |
|---|---|
| **Strengths** | Longest real customer-site record in the industry (65k+ hrs, 9 sites, 100k+ totes); first-mover on RaaS contracts (GXO 2024) and safety certification (NRTL 2025, Halos partnership 2026, ISO 25785-1 pen-holder); public-market currency + >$620M expected cash while rivals depend on private mega-rounds; own factory (RoboFab) plus Foxconn as investor/scale partner; revenue-linked order book ($300M) rather than pure narrative |
| **Weaknesses** | Narrow use case: tote/case handling ≈ the whole proven business — Melonee Wise (Agility's own ex-CPO, now KUKA): **"I don't think anyone has found an application for humanoids that would require several thousand robots per facility"** (IEEE Spectrum, 2025-09); DoF-limited platform vs Figure 03 / Atlas dexterity — if generalist manipulation arrives, Digit's hardware ceiling shows; heavy losses (~$100M/yr burn) with small revenue; SPAC route carries adverse selection stigma (Churchill franchise: Lucid, MultiPlan — both traded far below merger prices) and redemption risk to the $420M trust; $300M orders are milestone-contingent, not booked revenue; "cooperative safety by early 2027" has already slipped once — Johnson in late 2024 (Web Summit) put commercialized cooperative safety "within the next 18-24 months", i.e. by ~mid/late 2026 |
| **Skeptic case** | A biped must beat cheaper fixed automation and AMRs on the same tote workflows; humanoid demand at scale is still hypothetical (IEEE Spectrum's "Reality Is Ruining the Humanoid Robot Hype"); if warehouse tote-moving commoditizes (Unitree-class pricing, see [Company: Unitree](company-unitree.md)), Agility's premium US-built machine competes on safety certification and uptime alone |
| **Bull case** | Only player whose claims are largely customer-corroborated; safety-certification moat is slow for rivals to replicate; public listing forces audited disclosure — a credibility weapon against self-reported rivals ([Figure](company-figure.md), [Optimus](company-optimus.md)) |

## Manufacturing & supply-chain posture

The section most relevant to ODM/EMS readers:

- **In-house first**: **RoboFab** (Salem, OR) — 70,000 sq ft, announced 2023-09 as the world's first purpose-built humanoid factory; hundreds of units/yr initially, **~10,000 units/yr design capacity**, 500+ jobs at full scale. Mass production of v4 was slated to start by end-2024 (Salem Reporter, 2024-09).
- **~75% of Digit parts sourced domestically in the US** (company-reported, SPAC materials) — a deliberate reshoring/geopolitics pitch ("American technology leadership") that contrasts with China-centric humanoid BOMs (see [Landscape: China](landscape-china.md)).
- **Foxconn is the ODM-shaped escape valve**: the world's largest EMS led the ~$200M PIPE and was already an investor. Coverage around the deal positions Foxconn as the natural contract manufacturer **if v5 demand exceeds RoboFab capacity** (reported framing, not a disclosed manufacturing agreement — unverified). Strategic read: Foxconn gets a hedged entry into humanoid assembly (it is separately deploying humanoids with NVIDIA in its Houston AI-server plant), Agility gets credible scale-up capacity without capex. Watch the S-4 for any formalized Foxconn manufacturing terms.
- **Schaeffler's dual role**: investor + customer, and as a precision motion-components maker (bearings, actuator components) a plausible supplier into Digit's drivetrain — supplier relationship suggested in coverage but not formally disclosed (unverified).
- **NVIDIA dependency**: IGX Thor + Halos OS are now load-bearing in the v5 safety architecture, alongside Isaac Sim/Lab in training — deep leverage, but a single-vendor concentration shared with much of the industry (see [Company: NVIDIA](company-nvidia.md)).
- Net posture: **vertically integrated final assembly + US-heavy supply chain + EMS giant on the cap table** — closest peer analogue is Figure's BotQ (fully in-house, no EMS partner) and Apptronik's Jabil partnership (EMS-first). Agility sits between: it owns the factory but pre-positioned the contract-manufacturing relationship before volume demand exists.

## Sources

- https://www.agilityrobotics.com/content/agility-robotics-to-go-public-through-merger-with-churchill-capital-corp-xi — official SPAC release: $2.5B pre-money, $420M trust + ~$200M Foxconn-led PIPE, >$620M, AGLT, 180-day lockup, $300M v5 orders, 65k+ hrs, 9 facilities, RoboFab 10k/yr, ~75% US parts, Johnson & Hurst quotes
- https://www.businesswire.com/news/home/20260624555633/en/Agility-Robotics-to-Go-Public-Through-$2.5-Billion-Merger-with-Churchill-Capital-Corp-XI — deal terms wire copy (2026-06-24)
- https://www.therobotreport.com/humanoid-maker-agility-robotics-go-public-through-spac-merger/ — independent confirmation of SPAC terms and deployment stats
- https://www.geekwire.com/2026/digit-maker-agility-robotics-to-go-public-in-2-5b-deal-heres-what-the-filings-say-about-its-finances/ — FY2025 opex ~$111M vs ~$71M 2024, ~$100M cash burn (preliminary/unaudited, per SPAC filings); Amazon testing
- https://www.sec.gov/Archives/edgar/data/0002074973/000121390026071287/ea029548401ex99-1.htm — Churchill Capital Corp XI 8-K exhibit (2026-06): deal press release as filed with the SEC
- https://www.forbes.com/sites/johnkoetsier/2026/06/24/first-humanoid-robot-maker-goes-public-in-us-25-billion-deal-new-robot-300-million-in-pre-orders/ — first-US-humanoid-to-list framing; v5 unveil same day
- https://www.techtimes.com/articles/319099/20260625/humanoid-robot-ipo-agility-robotics-signs-spac-deal-us-nasdaq-debut.htm — Digit v5: 50 lb payload, 22 h/day, swappable hands, Halos integration, early-2027 availability
- https://nvidianews.nvidia.com/news/nvidia-announces-halos-for-robotics-the-industrys-first-full-stack-safety-system-for-physical-ai — NVIDIA Halos for Robotics launch (2026-06-22, Automate): IGX Thor, Halos OS, ANAB-accredited inspection lab; "Agility is the first company to team with NVIDIA to incorporate elements of Halos for Robotics into its proprietary safety system"; IEC 61508 / ISO 13849 / ISO/IEC TR 5469
- https://www.nvidia.com/en-us/case-studies/agility-robotics-digit-humanoid-robot/ — whole-body control foundation model: Isaac Sim digital twin, Isaac Lab RL, MuJoCo validation; Velagapudi quote
- https://www.agilityrobotics.com/content/gxo-signs-industry-first-multi-year-agreement-with-agility-robotics — first commercial humanoid RaaS agreement (2024-06, official)
- https://www.agilityrobotics.com/content/digit-moves-over-100k-totes — >100,000 totes at GXO Flowery Branch (official, 2025-11-20; does not itself mention the NRTL certification)
- https://www.humanoidsdaily.com/news/agility-robotics-secures-osha-recognized-safety-approval-widening-the-gap-between-demo-and-deployment — OSHA-recognized NRTL field-inspection approval (2025-11): site-specific, vs ANSI/RIA R15.08, ISO 13849, ISO 12100; customer site not named
- https://www.agilityrobotics.com/content/agility-robotics-announces-strategic-investment-and-agreement-with-motion-technology-company-schaeffler-group — Schaeffler investment + deployment agreement (2024-11, official)
- https://www.therobotreport.com/schaeffler-plans-global-use-agility-robotics-digit-humanoid/ — Schaeffler Cheraw SC use and global rollout plans
- https://www.agilityrobotics.com/content/agility-robotics-announces-commercial-agreement-with-toyota-motor-manufacturing-canada — TMMC agreement (2026-02, official)
- https://techcrunch.com/2026/02/19/toyota-hires-seven-agility-humanoid-robots-for-canadian-factory/ — 7 Digits at Woodstock RAV4 plant
- https://www.therobotreport.com/toyota-motor-manufacturing-canada-deploys-agility-robotics-digit-humanoids/ — TMMC trial expansion 3→10 units
- https://www.agilityrobotics.com/content/opening-robofab-worlds-first-factory-for-humanoid-robots — RoboFab: 70k sq ft, hundreds year one, 10k/yr capacity, 500+ jobs (official, 2023-09)
- https://www.salemreporter.com/2024/09/03/salem-factory-will-start-mass-producing-humanoid-robots-by-the-end-of-the-year/ — RoboFab production start timing
- https://www.axios.com/2023/12/05/humanoid-robot-factory-agility-bipedal-amazon — Amazon testing Digit near Seattle
- https://techcrunch.com/2024/03/05/agility-robotics-new-ceo-is-focused-on-the-here-and-now/ — Johnson appointment, "here and now" positioning
- https://www.agilityrobotics.com/content/agility-robotics-appoints-peggy-johnson-as-chief-executive-officer — Johnson background (official, 2024-03)
- https://www.agilityrobotics.com/content/agility-welcomes-robotics-pioneer-melonee-wise-as-new-cto-establishes-new-chief-robot-officer-role-and-celebrates-year-of-outstanding-leadership-growth — Wise joins as CTO, Hurst → Chief Robot Officer (official, 2023)
- https://www.therobotreport.com/melonee-wise-leads-kuka-new-software-ai-organization/ — Wise departure (2025-08) to KUKA
- https://spectrum.ieee.org/humanoid-robot-scaling — IEEE Spectrum "Reality Is Ruining the Humanoid Robot Hype" (2025-09-11, Ackerman); Wise verbatim: "I don't think anyone has found an application for humanoids that would require several thousand robots per facility"
- https://techinformed.com/web-summit-2024-humanoid-robots-has-the-hardware-caught-up-with-the-software/ — Johnson at Web Summit 2024: cooperative safety commercialized "within the next 18-24 months" (the timeline that later slipped to early 2027)
- https://www.agilityrobotics.com/content/mercado-libre-and-agility-robotics-announce-commercial-agreement — Mercado Libre commercial agreement, San Antonio TX (official, 2025-12-10)
- https://spectrum.ieee.org/agility-robotics-introduces-cassie-a-dynamic-and-talented-robot-delivery-ostrich — Cassie introduction (2017), spring-mass lineage
- https://oregonbusiness.com/17736-i-robot/ — founding story: Hurst, Shelton, Jones; OSU spin-out; ATRIAS/DARPA
- https://atomsbitsnewsletter.substack.com/p/qa8-peggy-johnson-ceo-of-agility — Johnson on RaaS economics ("several $1,000 a month"), anti-backflip positioning
- https://robots4therestofus.substack.com/p/jonathan-hurst-of-agility-robotics — Hurst philosophy podcast (episode page; augmentation framing — no public transcript, quotes paraphrased)
- https://tsginvest.com/agility-robotics/ — $30/robot-hr RaaS benchmark + <2yr ROI target, operating-cost estimates (aggregator; figures company-reported, unverified against filings)
- https://blog.robozaps.com/b/agility-robotics-digit-review — Digit v4 aggregator specs (~175 cm, 65 kg, 16 kg payload — unverified)
- https://robotsandstartups.substack.com/p/why-a-spac-for-agility-makes-sense — Andra Keay's steel-man of the SPAC choice
- https://www.thescenarionist.com/p/the-humanoid-spac-test-deep-tech — SPAC-structure skeptic case
