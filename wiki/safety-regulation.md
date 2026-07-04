---
title: Safety & Regulation
slug: safety-regulation
updated: 2026-07-04
confidence: verified
---
> As of mid-2026, safety standards are the acknowledged bottleneck between humanoid demos and volume deployment. The dedicated standard for balance-controlled robots — ISO 25785-1, developed in ISO/TC 299 WG 12 with US-delegation project leadership from Agility Robotics, Boston Dynamics and A3 — reached committee draft (CD) stage on 2026-05-12, with publication expected 2027-ish; until then humanoids are certified piecemeal against ISO 10218:2025 (which absorbed the collaborative-robot TS 15066), ANSI/RIA R15.08 (mobile robots), ISO 12100/13849 risk assessment, and UL 3300 for consumer/service robots (added to OSHA's NRTL test-standard list 2025-12-31). The EU stacks the Machinery Regulation 2023/1230 (applies 2027-01-20) on top of the AI Act, whose high-risk deadlines slipped to late-2027/2028 in the 2026 "Digital Omnibus". China moved fastest on paper: MIIT stood up a national humanoid standards committee (2025-12-26, with Unitree and AgiBot founders as vice-chairs) and published HEIS 2026, the first national standard system for humanoids and embodied AI (52 initial standards). Agility's Digit obtained the first OSHA-recognized NRTL field certification of a humanoid in a live fulfillment center (2025-11); genuinely fenceless "cooperatively safe" operation and certified home deployment (1X NEO ships late 2026) remain ahead of the standards, not behind them.

## The standards stack (as of 2026-07)

| Instrument | Scope | Status | Why it matters for humanoids |
|---|---|---|---|
| ISO 10218-1/-2:2025 | Industrial robots + robot applications/cells | Published 2025 (first revision since 2011) | Baseline for any factory humanoid; now includes collaborative-application requirements, functional safety, cybersecurity |
| ISO/TS 15066:2016 | Collaborative robot operation (power/force limits, body-region thresholds) | Largely absorbed into ISO 10218-2:2025 | The four collaborative modes carried over verbatim; "collaborative robot" as a term retired in favor of "collaborative application" |
| ANSI/A3 R15.06-2025 | US national adoption of ISO 10218 (3 parts) | Published 2025-09 after ~8 years of work | US legal reference for industrial robot safety; adds user-facing Part 3 |
| ANSI/RIA R15.08 | Industrial mobile robots (AMRs) | In force; Part 3 covers users | Basis of Digit's 2025 NRTL field inspection; nearest fit for wheeled-base mobile manipulators |
| **ISO 25785-1** | **Dynamically stable industrial mobile robots (legged/wheeled/other)** | **Committee draft (CD) registered 2026-05-12 (ISO/TC 299 WG 12)** | First standard written *for* robots that need active balance — bipeds, quadrupeds, wheeled balancers |
| ISO 13482:2014 | Personal care / service robots | Published 2014, widely seen as dated for dynamically stable humanoids (unverified characterization) | Only existing ISO safety standard aimed at robots around untrained people |
| ANSI/CAN/UL 3300:2024 | SCIEE robots (service, communication, info, education, entertainment) incl. humanoids | First edition published 2024-05; ANSI/SCC-approved version 2025-04-16; added to OSHA NRTL "appropriate test standards" list 2025-12-31 | The likeliest certification path for consumer/home and commercial-service humanoids in North America |
| ISO 12100 / ISO 13849 | Machinery risk assessment / safety-related control systems | Long-established | The horizontal standards every humanoid deployment is actually assessed against today |
| EU Machinery Regulation 2023/1230 | All machinery incl. self-evolving ML safety functions | Applies 2027-01-20 | Makes ML-based safety behavior a mandatory third-party conformity route in the EU |
| EU AI Act | AI systems incl. safety components of products | Full applicability 2026-08-02; high-risk deadlines deferred (see below) | Embodied-AI stacks can be "high-risk AI" on top of machinery compliance |
| China HEIS 2026 | National standard *system* for humanoids + embodied intelligence | Released 2026-02-28; 52 initial standards | The first comprehensive national framework; feeds China positions into ISO/IEC |

## ISO 25785-1 — the humanoid-shaped gap gets a standard

- Full title: *Robotics — Safety requirements for dynamically stable industrial mobile robots (legged, wheeled, or other forms of locomotion) — Part 1: Robots*. A **Type C** (machine-specific) safety standard under **ISO/TC 299 (Robotics), Working Group 12**.
- Covers robots that must actively balance to stay upright — bipeds/humanoids, quadrupeds, three-legged forms, and wheeled self-balancers. Existing standards (10218, R15.08) implicitly assume statically stable machines; loss-of-balance, fall behavior, and safe stop while balancing are the new hazard classes.
- Timeline: working-group session in Barcelona 2025-10; **CD (committee draft) registered 2026-05-12** (ISO catalogue lists it as ISO/CD 25785-1); publication widely expected 2027 (some coverage says late 2026, optimistic) — CD → DIS → FDIS stages remain.
- US delegation leadership: **Kevin Reese (Agility Robotics, project leader), Federico Vicentini (Boston Dynamics, head of safety), Carole Franklin (A3, director of robotics standards development)**.
- Complementary track: the **IEEE Humanoid Study Group** (led by Aaron Prather, ASTM) published *A Pathway Study for Future Humanoid Standards* (2025) mapping needed work in three areas — classification, stability, human-robot interaction — and coordinating across SDOs; Prather estimated 18–36 months to ratified standards and said volume humanoid deployment realistically waits for ~2027. See [Open problems](open-problems.md).

## ISO 10218:2025 and the end of the "collaborative robot"

- The 2025 revision (first since 2011) is the biggest industrial-robot safety overhaul in over a decade. Key changes: clarified **functional safety** requirements, new **cybersecurity** requirements (to the extent they affect safety), updated robot classifications, end-effector and manual load/unload content, and — most consequentially — **absorption of most of ISO/TS 15066** into Part 2.
- Terminology shift: no more "collaborative robot" / "collaborative operation" — only **"collaborative applications"**, because safety can only be designed and verified at the application level (robot + end-effector + workpiece + cell), not the robot alone. The four TS 15066 collaborative modes (incl. power- and force-limiting with body-region thresholds) carry over.
- US adoption: **ANSI/A3 R15.06-2025** published 2025-09 (Parts 1–3; Part 3 is new user-focused guidance). A3 positions it as the roadmap for "safety in the era of intelligent automation".

## US consumer/service path: UL 3300

- **ANSI/CAN/UL 3300** (Standard for Service, Communication, Information, Education and Entertainment — SCIEE — Robots) explicitly lists humanoids, household robots, companion robots, delivery robots, exoskeletons and mobile service robots in scope; it prioritizes safe operation around ordinary people, including users with disabilities.
- On **2025-12-31 OSHA added UL 3300 to the NRTL program's List of Appropriate Test Standards**, making it usable for certification of SCIEE robots deployed in US commercial/enterprise settings.
- UL Solutions opened its first dedicated service-robot testing lab; UL 3300 covers multidirectional mobility, fire/shock, external manipulation, user classes and use surroundings.

## EU: two-layer regime (machinery + AI)

- **Machinery Regulation (EU) 2023/1230** replaces the Machinery Directive and **applies from 2027-01-20**. Machinery with "fully or partially self-evolving behaviour using machine learning" in **safety functions** is on the high-risk list → mandatory (third-party) conformity assessment. Any humanoid whose learned policy performs a safety function falls squarely in scope.
- **EU AI Act**: in force 2024-08-01; GPAI obligations from 2025-08; general applicability **2026-08-02**. The **Digital Omnibus on AI** (proposed 2025-11-19; provisional trilogue agreement 2026-05-07, COREPER-confirmed 2026-05-13; Parliament endorsed 2026-06-16; Council final approval 2026-06-29) deferred the high-risk regime: stand-alone (Annex III) high-risk systems apply **at latest 2027-12-02**, high-risk AI **embedded in products** (the humanoid case) **at latest 2028-08-02**.
- The omnibus also moved the Machinery Regulation to **Section B of Annex I**, meaning AI Act Chapter III obligations no longer apply directly to machinery-embedded AI; instead the Commission must fold AI-specific health/safety requirements into the Machinery Regulation via delegated acts **by 2028-08-02**, and AI used purely for convenience/optimization (not safety) is excluded from "safety component" status. Net effect: one merged machinery-centric compliance route for EU humanoids, arriving ~2027–28.

## China: HEIS 2026 and the standards race

- MIIT formally constituted the **Humanoid Robot and Embodied Intelligence Standardization Technical Committee (MIIT/TC08)** on **2025-12-26**. Vice-chairs include **Wang Xingxing (Unitree founder)** and **Peng Zhihui (AgiBot co-founder/CTO)** — manufacturers sit at the head of the table. See [Landscape: China](landscape-china.md) and [Key people](key-people.md).
- On **2026-02-28** in Beijing Yizhuang, MIIT released the **Humanoid Robot and Embodied Intelligence Standard System (2026 edition, "HEIS 2026")** — the world's first comprehensive national standard system for humanoids/embodied AI. Six pillars: foundational & common; brain-inspired intelligence & intelligent computing; limbs & components; complete systems & integration; applications; **safety & ethics running through the entire lifecycle**. An initial roster of **52 standards** was published, drafted by **120+** institutes/enterprises with CESI structural support.
- The system is explicitly aimed at feeding Chinese positions into **ISO/IEC** — a deliberate play for first-mover influence over international humanoid rules while ISO 25785-1 is still in CD stage. Western coverage frames this as a "standards race"; note HEIS 2026 is a framework/roadmap, not yet a certification regime (distinction often lost in coverage).

## Certification gates in practice

**Fenceless factory work**
- Today's deployments (Figure at BMW, Digit at GXO, Apollo at Mercedes — see [Humanoids](humanoid-robots.md)) run in **restricted or segregated zones**; no humanoid is certified for free-roaming collaborative operation around unprotected workers.
- **Agility Robotics** announced (2025-11-25) the first **OSHA-recognized NRTL field inspection** of a humanoid in a live e-commerce fulfillment center — evaluated against **ANSI/RIA R15.08, ISO 13849, ISO 12100** for tote-handling workflows. The approval is **site-specific** (that configuration, that facility) but establishes the template. Agility's safety team also lists ANSI B11.0/B11.19 and ISO 10218 among its foundational compliances; a claimed TÜV Rheinland validation of its ISO 12100 risk assessments could not be independently confirmed (unverified).
- Agility pitches Digit v5 as the first "cooperatively safe" humanoid (built on NVIDIA Halos); the CEO's target for cooperative safety has slipped from "within 18 months" (late 2024) to **early 2027** (unverified single-source timeline). Until ISO 25785-1 publishes, "fenceless" claims have no dedicated standard to certify against.

**Home deployment**
- **1X NEO** (US home deliveries targeted late 2026, $20K or $499/mo; Hayward factory opened 2026-05-01, first production units going to internal testers) leads with safety-by-design arguments: ~30 kg tendon-driven body, soft 3D-lattice polymer skin, covered pinch-proof joints, low-force actuation — plus human teleoperation ("Expert Mode") for hard tasks, which shifts part of the safety question to operator vetting and privacy. 1X has published **no specific third-party safety certification** for NEO (as of 2026-07, unverified absence).
- UL 3300 is the natural North-American certification route for home humanoids; the EU route (Machinery Regulation + AI Act) hardens 2027–28. Legal commentary flags home humanoids as a products-liability minefield until then.
- **Guardrail-jailbreak risk (as of 2026-07)**: home humanoids inherit the LLM jailbreak problem with physical consequences. Witt's illustrative scenario (New Yorker, 2026-07-06 issue): a persistent, creative child coaxing NEO past its AI guardrails into a harmful command (e.g. bashing its head on a table) — "research shows that such guardrails can be circumvented." Notably, 1X's own CEO agrees NEO "should not be used around small children" (per Witt), yet no standard above tests LLM-guardrail robustness as a safety function.
- **In-home teleoperation privacy**: 1X's "Expert Mode" means human operators can see inside customers' homes through NEO's eye cameras; mitigations are disclosure-based — operators sit next to the AI team at 1X's campus, and NEO's earpiece light rings change color during remote operation (per Witt). Børnich confirms sessions double as training data ("It's also useful data for us"), tying home privacy to the unresolved consent questions in [Data foundry](data-foundry.md); no certification or statute yet governs in-home robot teleop (as of 2026-07).

## Incidents, liability, insurance

- **Unitree H1 "flailing" incident (2025-05, viral)**: a crane-suspended H1 in a factory test thrashed violently near workers, dragging its stand; handler attributed it to running a full-body control policy while the feet weren't load-bearing. No serious injury; became the canonical clip in humanoid-safety debates.
- **Unitree G1 kicked a child** during a public demo in China (video shared 2026-06-04; widely covered — a wig-wearing G1's roundhouse kick struck a child in the stomach; Chinese media reported no serious injury).
- **Unitree G1 Bluetooth "robot botnet" vulnerability**: security researchers Andreas Makris & Kevin Finisterre disclosed (2025-09) a BLE flaw letting attackers take control of G1 fleets, "creating a robot botnet that spreads without user intervention" — resurfaced for a mainstream audience by Witt's New Yorker piece (2026-07-06 issue). Full technical detail (UniPwn, CVE-2025-60017/-60250/-60251, disclosure timeline) in the [Unitree deep dive](company-unitree.md); relevant here because ISO 10218:2025 now makes cybersecurity a safety-standard requirement, and a wormable exploit on the world's most-deployed research humanoid is the concrete case for it.
- **Tesla Fremont robot-arm lawsuit**: a robotics technician disassembling a FANUC industrial arm at Tesla's Fremont plant (2023-07-22) was knocked unconscious and pinned when the arm unexpectedly released and its ~8,000 lb counterbalance came down on him; his ~$51M suit against Tesla and FANUC (filed 2025, ~$1M medical costs incurred + ~$6M projected) is what coverage calls the first major robot-workplace-injury lawsuit. Frequently miscited as a humanoid incident — it was a classic industrial arm.
- Warehouse-automation context: reporting has claimed Amazon's robotic facilities show ~54% higher injury rates than non-robotic ones (contested, single investigative source, unverified).
- **Liability** is unsettled: workers' comp covers employees but not pain-and-suffering; third-party product-liability suits against robot makers are the expected pressure valve; negligent-deployment theories against integrators/operators are untested for humanoids. Teleoperated home robots add a novel operator-liability layer.
- **Insurance** is emerging fastest in China: policies for two 60 kg humanoids were written at ~RMB 5,000 (~$707) premium per robot for up to RMB 500,000 coverage over one year (Hubei's first embodied-AI policy, bought by a HUST incubator, 2025-11); China Pacific launched China's first dedicated commercial-humanoid insurance product 2025-09, with PICC and Ping An following. US brokers report general-liability premiums rising 10–20% where robots operate (secondary source, unverified). Expect insurers to become de-facto regulators — pricing certified vs uncertified deployments — before statutes catch up.

## Who sits at the key tables (as of 2026-07)

| Body | Key names / composition |
|---|---|
| ISO/TC 299 WG 12 (ISO 25785-1) | Kevin Reese (Agility, project leader); Federico Vicentini (Boston Dynamics); Carole Franklin (A3) lead the US delegation |
| A3 (ANSI/A3 R15.06, R15.08) | Carole Franklin, director of robotics standards development |
| IEEE Humanoid Study Group | Aaron Prather (ASTM), lead; cross-SDO coordination role |
| MIIT/TC08 (China) | Vice-chairs incl. Wang Xingxing (Unitree), Peng Zhihui (AgiBot); CESI secretariat support; 120+ drafting organizations |
| UL Standards & Engagement | UL 3300 technical committee (consumer/service robots incl. accessibility input) |

Pattern worth noting: in both the US-led ISO track and China's national committee, **the manufacturers themselves hold the pens** — Agility, Boston Dynamics, Unitree, AgiBot. Fast, informed — and a structural conflict of interest that critics of self-set safety bars point to. See [Organizations](organizations.md) and [Open problems](open-problems.md).

## Sources

- https://www.iso.org/standard/91469.html — ISO/CD 25785-1 title and CD stage (2026-05-12), ISO/TC 299
- https://www.techbriefs.com/component/content/article/53111-safety-in-motion-setting-the-standard-for-humanoid-robots — ISO 25785-1 Type C scope, US delegation leadership (Reese/Vicentini/Franklin)
- https://www.fortrobotics.com/news/shaping-the-robot-safety-standards-of-the-future — TC 299 WG 12 scope, Barcelona 2025-10 session
- https://www.automate.org/robotics/blogs/updated-iso-10218-faq — ISO 10218:2025 changes, "collaborative application" terminology, TS 15066 absorption
- https://www.therobotreport.com/iso-10218-industrial-robot-safety-standard-receives-major-overhaul/ — 10218:2025 overhaul details (functional safety, cybersecurity)
- https://www.businesswire.com/news/home/20250910605228/en/New-ANSIA3-R15.06-2025-American-National-Standard-for-Industrial-Robot-Safety-Now-Available-for-Purchase — ANSI/A3 R15.06-2025 publication, Franklin quote
- https://www.ul.com/news/ul-3300-outline-investigation-helps-advance-safety-consumer-service-and-education-robots — UL 3300 scope incl. humanoids
- https://www.federalregister.gov/documents/2025/12/31/2025-24076/ul-llc-grant-of-expansion-of-recognition-and-modification-to-the-nrtl-programs-list-of-appropriate — Federal Register notice adding UL 3300 to the NRTL appropriate-test-standards list, effective 2025-12-31 (primary)
- https://webstore.ansi.org/standards/ul/ansiul33002024 — ANSI/CAN/UL 3300:2024 designation; ANSI-approved edition published 2025-04-16 (first edition 2024-05)
- https://www.humanoidsdaily.com/feed/agility-robotics-secures-osha-recognized-safety-approval-widening-the-gap-between-demo-and-deployment — Digit NRTL field inspection (2025-11-25), R15.08/13849/12100, site-specific
- https://inkog.io/labs/eu-machinery-regulation-ai-agents — Machinery Regulation 2023/1230 applicability date, self-evolving ML safety functions
- https://www.gibsondunn.com/eu-ai-act-omnibus-agreement-postponed-high-risk-deadlines-and-other-key-changes/ — Digital Omnibus deferred high-risk deadlines (2027-12-02 / 2028-08-02)
- https://www.insideglobaltech.com/2026/05/28/eu-ai-act-update-timeline-relief-targeted-simplification-and-new-prohibitions/ — Machinery Regulation moved to Annex I Section B; delegated acts by 2028-08
- https://www.consilium.europa.eu/en/press/press-releases/2026/06/29/artificial-intelligence-council-gives-final-green-light-to-simplify-and-streamline-rules/ — Council final approval of the AI omnibus, 2026-06-29 (primary)
- https://www.consilium.europa.eu/en/press/press-releases/2026/05/07/artificial-intelligence-council-and-parliament-agree-to-simplify-and-streamline-rules/ — provisional trilogue agreement, 2026-05-07 (primary)
- https://www.addleshawgoddard.com/en/insights/insights-briefings/2026/technology/ai-omnibus-provisional-agreement-changes-eu-ai-act-delayed-deadlines/ — omnibus agreement timeline (May–June 2026 approvals)
- https://sesec.eu/2026/04/01/chinas-first-standards-system-for-humanoid-robots-and-embodied-intelligence/ — HEIS 2026 release (2026-02-28), six pillars, 52 standards, MIIT/TC08, CESI
- https://robottoday.com/article/china-s-humanoid-robot-and-embodied-intelligence-standard-system-heis-2026 — MIIT/TC08 constitution 2025-12-26, vice-chairs Wang Xingxing and Peng Zhihui, ISO/IEC engagement
- https://www.globaltimes.cn/page/202512/1351625.shtml — MIIT standardization committee establishment (2025-12), 65 members, global-competitiveness framing
- https://www.therobotreport.com/ieee-study-group-publishes-framework-for-humanoid-standards/ — IEEE Humanoid Study Group framework, Aaron Prather, 18–36-month timeline
- https://www.therobotreport.com/1x-announces-pre-order-launch-neo-humanoid-robot/ — NEO pre-orders, 2026 US home deliveries, safety-by-design features
- https://roboticsandautomationnews.com/2025/05/08/ai-robot-attacks-worker-viral-video-shows-unitree-humanoid-going-berserk/90524/ — Unitree H1 factory incident and cause
- https://interestingengineering.com/ai-robotics/viral-humanoid-robot-kicks-child-in-stomach — Unitree G1 child-kick incident (2026-06)
- https://www.chinadaily.com.cn/a/202512/12/WS693b6d05a310d6866eb2e404.html — China humanoid insurance policy terms (premium, coverage)
- https://www.automotivedive.com/news/former-factory-worker-sues-tesla-fanuc-robotic-arm-unconscious-51-million/761146/ — Tesla Fremont FANUC-arm lawsuit details ($51M, 2023-07-22 incident, counterbalance release during disassembly)
- https://humanoidliability.com/industries/humanoid-robots/ — liability framing, insurance premium trends
- https://www.travteks.com/blog/1x-neo-home-delivery/ — 1X Hayward factory opening 2026-05-01, first units to internal team, customer deliveries targeted late 2026
- https://www.agilityrobotics.com/content/beyond-the-hype — Agility's own account of NRTL approval and compliance standards list
- https://www.newyorker.com/magazine/2026/07/06/are-humanoid-robots-ready-to-be-deployed — Witt: G1 Bluetooth botnet vulnerability (Makris/Finisterre), child-jailbreak scenario, 1X teleop privacy/disclosure model (read via Wayback snapshot)
- https://spectrum.ieee.org/unitree-robot-exploit — UniPwn technical detail and disclosure timeline (primary technical coverage; full treatment in company-unitree)
