---
title: "ODM Opportunity Map: Where Contract Manufacturers Fit in Physical AI"
slug: odm-opportunity
updated: 2026-07-05
confidence: verified
---
> Where does an electronics ODM/EMS actually fit in Physical AI? As of 2026-07 the honest answer is: the manufacturing revenue pool is still tiny (~50,000 humanoids forecast globally for 2026 ≈ ~$2B of hardware at blended ASPs — less than one mid-size phone program), but the **design-win window is open and closing**: Apptronik named Jabil its worldwide manufacturing partner (2025-02), AgiBot handed Lens Technology a JV plus assembly of its full 2025 lineup, Foxconn is leading the ~$200M PIPE in Agility's $2.5B SPAC (2026-06) while preparing GR00T-powered humanoid deployment in its own Houston AI-server plant, Boston Dynamics designed electric Atlas "for compatibility with automotive supply chains" and sourced actuators to Hyundai Mobis — while the two largest planned ramps (Tesla, Figure) stay defiantly in-house. The opportunity splits into final assembly (small pool, high strategic value), components (bigger pool, brutal China price deflation), and picks-and-shovels (test rigs, battery-swap, teleop/data hardware — sells regardless of which robot brand survives). Demand signals for 2026–27 are real but institutional, not consumer: State Grid's ~¥6.8B phased robot procurement, the MIIT/SASAC "real-scene training" special action, IPO capital hitting robot makers' balance sheets. Sibling context: [Investment](investment.md), [Humanoid robots](humanoid-robots.md), [Hardware](hardware.md), [Landscape: China](landscape-china.md).

Scope note: written for an ODM-industry analyst building an executive investment case; the client's specific capability profile is unknown, so §5 judgments are phrased conditionally. Facts below were adversarially re-checked where flagged; one widely repeated claim (Luxshare's China Mobile order) failed verification and is marked accordingly.

## 1. Market size, honestly bounded (as of 2026-07)

Two different quantities get conflated in every humanoid pitch deck: **units × hardware ASP** (what a manufacturer can address) and **wages displaced** (what Jensen Huang's $40–50T is). An ODM's revenue scales with the first, never the second.

### Shipped-units reality

| Metric | Number | Tracker / source | Note |
|---|---|---|---|
| 2025 global humanoid shipments | **13,317** | Omdia (2026-01) | AgiBot 5,168 #1, Unitree 4,200, UBTech 1,000; Tesla/Figure/Agility ~150 each |
| 2025 global humanoid shipments | **~18,000** (+508% YoY) | IDC (2026-01) | Wider form-factor scope; the figure carried by Chinese state media |
| 2025 deployed (external sales only) | **>16,000**, China >80% | Morgan Stanley (2026-06) | Excludes prototypes/trial/internal units |
| 2026 forecast, China only | **50,000** | Morgan Stanley — raised 14K → 28K → 50K during H1 2026 | The most-quoted 2026 number; China-only |
| 2026 forecast, global | **>50,000** (+~700%) | TrendForce (2025-11-26) | Note baseline inconsistency vs 13–18K 2025 trackers |
| Largest disclosed pure-play revenue, 2025 | Unitree **¥1.69B (~$235M)** | IPO prospectus | Humanoids 51.5% of it; the whole segment's revenue reality check |

Wiki convention (from [State of the art](state-of-the-art.md)): quote 2025 shipments as "~13,000–18,000 depending on tracker," treat all #1 claims as disputed.

### The forecast ladder — label the rhetoric class

| Figure | Source, date | Horizon | Class (per [Visions](visions.md)) |
|---|---|---|---|
| $6–10B humanoid market | MarketsandMarkets et al. | 2030 | Analyst, conservative band |
| **$38B TAM, ~1.4M units** | Goldman Sachs (2024-02 revision) | 2035 | Analyst forecast |
| **$5T "humanoid ecosystem"** | Morgan Stanley (2025); a $7.5T update circulates (unverified) | 2050 | Analyst forecast, ecosystem-inflated scope |
| $40–50T labor automation | Jensen Huang (GTC Paris 2025-06, secondary); Figure's "$42T/yr" Master Plan | open-ended | **Investor-pitch rhetoric** — wages, not hardware |

- The 2030-vs-2050 spread is ~500×; every trillion-dollar figure assumes solved [manipulation](manipulation.md) and reliability that remain [open problems](open-problems.md).
- **ODM arithmetic (illustrative, this wiki's own calculation)**: 2026's ~50K units at a ~$40K blended ASP ≈ **~$2B total hardware revenue globally** — cross-checked: Morgan Stanley itself sizes China's 2026 humanoid market at ~$2B (2026-06, CNBC), and IDC put 2025 global market revenue at only ~$440M. Final-assembly value-add at typical EMS economics (~6–10% of product value) ≈ **$120–200M worldwide, split among all contract manufacturers**. Even Goldman's 2035 case ($38B) implies an assembly pool of roughly $2–4B and a components pool of ~$13–15B (actuators ~35–40% of BOM per [Humanoid robots](humanoid-robots.md), industry estimate).
- BOM anchor: Morgan Stanley models ~**$46K/unit on Chinese supply chains vs ~$131K without** (Optimus Gen 2-class); Chinese component costs deflating ~15–20%/yr (reported estimate) — whoever manufactures, margin pressure arrives with volume. See [Hardware](hardware.md).

## 2. Value-chain opening map for ODMs/EMS

Openings ranked by evidence of outsourcing appetite. The macro signal: Boston Dynamics states electric Atlas "significantly reduces the amount of unique parts" and **"every component has been designed for compatibility with automotive supply chains"** (official blog, 2024), and its Atlas GM frames the Hyundai Mobis actuator deal as access to "the well-established cost structures and scale potential of the automotive industry" — i.e., at least one top-tier OEM is *designing for* external supply chains. The counter-signal: Tesla (Fremont line, ~10,000 unique parts) and Figure (BotQ, 12K/yr capacity) build in-house as doctrine.

| Subsystem | ~BOM share | Incumbents (as of 2026-07) | Outsourcing-appetite evidence | ODM entry difficulty |
|---|---|---|---|---|
| **Final assembly & integration** | — (fee-based) | Mostly in-house: Tesla Fremont, Figure BotQ, Unitree, AgiBot, Agility RoboFab (10K/yr, ~75% US parts) | Apptronik→Jabil worldwide manufacturing partner (2025-02); AgiBot→Lens full-lineup assembly (2025-08); UBTech↔Foxconn's Yunzhihui coop (2025–27); China Mobile's 2025 tender was literally titled a "代工 (contract-manufacturing) services" procurement | **Medium** — trivially within phone/server ODM capability; barrier is trust + tiny volumes, not process |
| **Actuator modules & reducers** | ~35–40% (actuators; reducers ~15%, roller screws ~18% per circulated split, unverified) | Harmonic Drive Systems, Nabtesco (high-end); Green Harmonic, FORE (mid); PRS: Rollvis, GSA, Ewellix, NSK + Chinese entrants Beite, Wuzhou New Spring; assembly: Top Group, Sanhua | Tesla reportedly outsources actuator assembly/components — Sanhua ~$685M order (single source, unverified, denied comment); BD→Hyundai Mobis actuator supply (official) | **High** — precision thread-grinding machine tools are the moat; Beite's ¥1.85B plant targets 2.6M PRS sets/yr in 2026 |
| **Dexterous hands** | ~5–10% (est.) | Inspire (~10K hands 2025), LinkerBot, Unitree Dex5-1, Shadow, Wonik; Tesla/Figure in-house | AgiBot spun off its hand unit as a standalone supplier (2026); >30K hands shipped 2025 (derived, single source); Luxshare claims self-developed tendon hand near industry-leading (company-reported) | **Medium** — micro-motor + tendon assembly maps to phone-haptics/camera DNA; wear parts (gels, tendons, skins degrade in 2–4K cycles) = recurring revenue. See [Tactile & hands](tactile-hands.md) |
| **Harnesses & high-flex cabling** | low single-digit % | Automotive harness majors are the obvious adjacency (inference); no humanoid-specific incumbent identified | None public (absence of evidence, as of 2026-07); hands' signal-wire fatigue (snapping at 4.5–7K cycles in ORCA study) suggests unsolved need | **Low** — commodity capability, small pool |
| **Sensors & cameras** | ~20% incl. "other" (unverified split) | Camera modules: phone-supply-chain players; tactile: GelSight, Meta/Wonik Digit 360; F/T: ATI, Schunk + Hypersen, Kunwei, Keli scaling | Figure 03 ships palm cameras + fingertip arrays (in-house design, outsourceable class of part); Goertek explicitly positions its speakers/sensors/optics for humanoids while disclaiming assembly (2026-06, company statement) | **Low–Medium** — most direct reuse of optics/acoustics ODM capability |
| **Battery packs & power** | ~15–20% | Cells: CATL-class; packs in-house (Figure 2.3 kWh custom BMS; UBTech dual-pack swap) | UN38.3 certification became a marketed feature (2025); UBTech's 3-min autonomous swap is a productized subsystem others may buy rather than build | **Medium** — pack + BMS assembly is standard EMS work; swap infrastructure is a fresh niche |
| **Thermal management** | small % | In-house; driver is Jetson Thor's 40–130 W envelope + actuator heat | Indirect: server-ODM liquid-cooling DNA (Foxconn, Quanta GB300 lines) transfers | **Low–Medium** |
| **Test / calibration rigs & EOL lines** | capex, not BOM | None established — each OEM improvises (1X's 2.86M-cycle hand rigs; Figure's BotQ line) | Flex↔Teradyne: 20-yr test-equipment manufacturing lineage extended to robotics (2026-04-22); Luxshare's "Manufacturing 2.0" full component-to-assembly automation line (early 2026, company-reported) | **Medium** — picks-and-shovels: sells to every brand, survives any shakeout |
| **Teleop & data-collection hardware** | opex, not BOM | VR-rig assemblies, mocap suits; Neura×Bosch put sensor suits on Bosch production workers to capture motion/workflow data (partnership announced 2026-01); 1X runs paid operator stations as a data channel | The [data-foundry](data-foundry.md) buildout (AgiBot World-style data factories) needs fitted-out capture facilities and rigs at scale | **Low** — consumer-electronics DNA maps directly; small but growing with every data thesis in [Data](data.md) |

- **Where the moats are NOT**: final assembly of a ~$20–40K robot is less demanding than a modern smartphone (fewer microns, more torque). The scarce assets are (a) precision reduction-gear machining, (b) an OEM's trust at design-freeze time, (c) test/reliability engineering nobody has standardized yet ([Open problems](open-problems.md) §4).
- **Where the poison is**: any component tier China already owns — ~70% of even Optimus's components reportedly trace to Chinese suppliers (single Chinese source, unverified — see [Hardware](hardware.md)); China holds ~40% of precision bearings, ~35% of motors, ~90% of rare-earth magnet processing (McKinsey, as of 2025). Competing there means competing with 15–20%/yr deflation.

## 3. Competitor (友商) scoreboard

Ranked by commitment level: **JV / production line > investment (PIPE/equity) > internal pilot > components-only > nothing**. All entries dated; sourced in [Sources](#sources).

| # | Company | Tier | The move (dated) | Caveats |
|---|---|---|---|---|
| 1 | **Jabil** (US) | Production partnership | Named **worldwide manufacturing partner for Apptronik Apollo** (2025-02-25, joint release; program active through 2026); new-built Apollos validated on Jabil's own floors (inspection, kitting, lineside delivery) before shipping to customers — "Apollo building Apollo" | Anchor risk = Apptronik execution; commercial Apollo delivery from 2027 |
| 2 | **Lens Technology 蓝思科技** (CN) | JV + production | JV with AgiBot, **Hunan Zhiqi Future Technology (湖南智启未来科技)**, registered 2025-04, RMB 10M capital, Changsha (stakes undisclosed); disclosed taking on **manufacturing/assembly across AgiBot's full 2025 humanoid lineup** (2025-08); strategic stake in AgiBot's cleaning-robot subsidiary Zhiding | RMB 10M registration is an option, not a factory; no capacity/unit figures disclosed |
| 3 | **Luxshare Precision 立讯精密** (CN) | Own line + components (beyond ODM) | Guided **~3,000 humanoid units shipped 2025, all to external customers** (company-reported, 2025-11); "Manufacturing 2.0" flexible line early 2026; targets ~80% self-developed core components (reducers, tendon-driven hand) by mid-2026 + general-purpose robot prototype (company-reported). **Verification flag**: the circulated "~¥124M China Mobile order to Luxshare" (2025-07) is contested — primary tender coverage shows the ¥124.05M China Mobile contract-manufacturing procurement was won by **AgiBot (¥78M) and Unitree (¥46.05M)**; secondary coverage (leaderobot.com, syndicated to other Chinese industry sites) credits Luxshare with a same-sized same-month "complete-unit + joint-module" order. Treat as unverified/likely conflation | Whose 3,000 units? Customer names undisclosed; all figures company-side |
| 4 | **Foxconn / Hon Hai** (TW) | Deploy + invest (no own brand) | (a) Deploying NVIDIA Isaac GR00T-powered humanoids on its **Houston GB300 AI-server line**, target start Q1 2026 (announced at NVIDIA GTC Washington DC, 2025-10; Reuters had reported the plan earlier in 2025); (b) **leading the ~$200M+ PIPE** in Agility Robotics' $2.5B SPAC (2026-06-24) — financial/strategic stake, *not* a manufacturing JV; (c) Foxconn-affiliated Yunzhihui (云智汇) × UBTech global strategic cooperation signed 2025-09-21 (2025–27: Yunzhihui handles worldwide sales/marketing/after-sales of UBTech humanoids; deployment across Foxconn-ecosystem factories); (d) co-developing service humanoids with Nvidia in Kaohsiung (first announced by chairman Liu Young-way 2025-01, reiterated 2026-01/02) | No self-branded general-purpose humanoid as of 2026-07; the PIPE buys information rights, not build rights |
| 5 | **Quanta 广达** (TW) | Own robot via subsidiary | Quanta-group subsidiary **Techman Robot** unveiled "TM Xplore I" — a **wheeled-base humanoid** (upper body on mobile base), billed as the first humanoid developed and manufactured in Taiwan — prototype shown 2025-08, formally launched at NVIDIA GTC 2026 (2026-03-18) with Quanta Cloud Technology + Nvidia (Jetson Thor onboard); launch targeted 2026 (company + multi-outlet coverage); Quanta also a named GB300 server ODM in the "humanoids assembling servers" supply-chain story (Chinese-language industry press, 2025-07, unverified) | Cobot-maker heritage; humanoid is pre-production |
| 6 | **Pegatron 和硕** (TW) | Internal BU / components-first | Robotics business unit on a 5-year buildout, components first; showcased "Aria" service robot + robot dog (COMPUTEX/investor events, 2025–26); chairman Tung Tzu-hsien says Nvidia names Pegatron among humanoid supply-chain beneficiaries | No mass-production humanoid, no named external OEM customer (as of 2026-07) |
| 7 | **Flex** (US) | Adjacent (cobot/AMR), no humanoid | Expanded 20-yr Teradyne partnership (2026-04-22): deploys Universal Robots cobots + MiR AMRs in Flex factories **and manufactures key UR components** | Explicitly not a humanoid program |
| 8 | **Inventec 英业达** (TW) | Adjacent infrastructure | COMPUTEX 2026: "Atlas Edge" AI server on NVIDIA IGX Thor, dual-arm cobot iTwin, inspection UGV; Omniverse/Isaac sim-to-real tooling (company materials) | No humanoid build/assembly move found |
| 9 | **Goertek 歌尔股份** (CN) | Components only | Investor Q&A (2026-06): "some layout in robot-related business"; speakers/sensors/optics/precision structural parts usable across humanoid hardware; **explicitly has not disclosed entering final assembly or a named OEM partner** (2024 statement: "not yet engaged in humanoid robot-related business") | Market treats it as a theme beneficiary, not an assembler |
| 10 | **BYD Electronics 比亚迪电子** (CN) | Beneficiary framing only | Humanoid program (incl. reported target of 20,000 robots on BYD lines by 2026, unverified aspiration) sits at **BYD Group level, not the listed BYDE entity**; BYDE's own disclosures describe only "some business layout" touching the theme; UBTech Walker S1 pilots in BYD car plants are a customer relationship, not BYDE manufacturing | No external humanoid manufacturing contract disclosed (as of 2026-06) |
| 11 | **Wistron Corp 纬创资通** (TW) | No public move | Nothing found as of 2026-07. **Entity warning**: reports conflate Wistron with 上纬新材 (Shangwei New Material / Swancor, STAR 688585) — the listed materials company AgiBot's Peng Zhihui took control of in 2025 as a listing vehicle (see [Investment](investment.md)), which launched the 0.8 m mini humanoid **"Qiyuan Q1" (启元Q1, brand 上纬启元) on 2025-12-31** and showed it at CES 2026. That is not the PC/server ODM Wistron | The fact base circulating in industry channels contains this mislabel; check entities before benchmarking |

Pattern read: **US EMS engages via named partnerships (Jabil), Taiwan ODMs via subsidiaries/own robots + Nvidia ecosystem alignment, Chinese A-share "ODMs" via JV-plus-assembly for domestic humanoid champions** — three different risk postures on the same question.

## 4. Timing: is 2026–27 the entry window?

### Demand signals (the bull case)

- **Order books hardening (as of 2026-07)**: Agility **$300M contracted Digit v5 orders** (SPAC filings); UBTech Walker cumulative orders **>¥800M**; Hyundai plans **25,000+ Atlas** in US plants from 2028 plus a 30K/yr robot factory; Figure BotQ ramped to ~1 robot/hour (>350 built, company-reported). See [Humanoid robots](humanoid-robots.md).
- **State procurement, China**: State Grid's 2026 embodied-robot program totals **~¥6.8B (~$950M)** — 500 humanoid live-line robots (¥2.5B), 3,000 dual-arm inspection robots (¥1.8B), 5,000 quadrupeds (¥1.5B) — phased through 2026: Q1 pilot, Q3 scale procurement, Q4 supplementary (breakdown from Chinese industry reporting via 36kr, echoed by multiple Western secondary outlets; SCMP independently corroborates the billions-scale plan; the quarterly phasing remains single-source, unverified). Morgan Stanley cites the State Grid order as a key driver of its 2026-06 forecast raise. The China Mobile ¥124M biped tender (2025-07) was the template.
- **Policy demand, China**: MIIT + SASAC launched the **2026 Humanoid Robot & Embodied Intelligence "Real-Scene Training" Special Action** (2026-06-09, primary MIIT notice): 100+ high-value application scenarios by end-2026 and "ten-thousand-unit-scale" (万台级) deployment capability across manufacturing, logistics, inspection, healthcare, emergency response. This is a state-side demand commitment mechanism, not just rhetoric. Korea's chaebol-coordinated physical-AI axis is the parallel signal ([Investment](investment.md)).
- **IPO/SPAC capital arriving at robot makers**: Unitree ~$618M STAR IPO (registration approved 2026-07-02), Agility ~$620M gross via SPAC (close expected by end-2026, Foxconn-led PIPE), AgiBot's listing maneuver — freshly capitalized OEMs must convert cash into capacity in 2026–27, and capacity decisions are exactly where make-vs-buy gets settled.
- **Design-win cadence accelerating** (§6 ledger): six materially new ODM/EMS-relevant commitments in the 12 months to 2026-06 (Lens full-lineup assembly, Yunzhihui×UBTech, Foxconn Houston, Luxshare's 3K guidance, Flex×Teradyne, Foxconn-Agility PIPE) vs three in the prior 12 (Jabil×Apptronik, Lens JV, Foxconn's Kaohsiung announcement) — a doubling.

### The skeptic case (why 2026–27 may be early)

- **Reliability is unsolved**: the flagship western pilot (Figure 02 at BMW Spartanburg) ended 2025-11 after ~11 months of a single task (~1,250 operating hours; robots retired visibly worn, not scaled into a fleet) — BMW has since confirmed a new Figure 03 use case at Spartanburg (2026-06) but gave its first German pilot to Hexagon's AEON, not Figure; only ~40% of pilots reach production within 24 months (unverified market research); MTBF numbers are essentially unpublished industry-wide ([Open problems](open-problems.md) §4). Manufacturing capacity built for demand that pilots don't confirm is stranded capex.
- **Form-factor risk**: Rodney Brooks's on-record prediction — winning machines get wheels, task-specific grippers, non-human sensors within ~15 years; dexterity "pathetic compared to human hands beyond 2036." If he's right, humanoid-specific assembly lines are the wrong asset — though most of the component map above (actuators, sensors, batteries, test) survives a form-factor pivot. Hedge accordingly ([Open problems](open-problems.md) §7).
- **The biggest ramps don't outsource**: Tesla (Fremont, ~1M/yr aspiration) and Figure (BotQ) are vertically integrated by doctrine; Unitree hits ~60% gross margin *because* of extreme vertical integration. Outsourcing appetite concentrates in capital-constrained startups — precisely the counterparties most likely to die in the shakeout China's own NDRC warned about (2025-11: >150 near-identical programs). Counterparty selection matters more than TAM.
- **Volume math**: even a perfect 2026 (~50K units globally) is a rounding error against ODM scale — utilization risk on any dedicated line. Musk's own guidance: "Optimus production will be extremely slow at first, as everything is new. This is not like making a car." (X post, 2026-07-01).
- **Timeline slippage is the sector norm**: every major Optimus target since 2021 missed; Agility's SPAC filings show heavy losses; treat all 2026 ramp dates as aspirational.

### Net read

2026–27 is not the *volume* window — it is the **anchor-account window**. The manufacturing relationships that will serve the 2028–30 ramp (if it comes) are being assigned now, at low cost of entry (Jabil's deal, Lens's RMB 10M JV, Foxconn's PIPE are all cheap relative to ODM balance sheets). The rational posture is small, capability-matched commitments that buy design-in position and information, sized so that a Brooks-style outcome hurts nothing.

## 5. Strategic options for a generic ODM (build / partner / invest / wait)

Client capability profile unknown; judgments conditional.

| Option | Named precedent | Capital | Key risk | Fits if… |
|---|---|---|---|---|
| **Build own-brand robot** | Luxshare (3K units guided 2025, company-reported); Quanta/Techman TM Xplore I | High | Channel conflict — you become a competitor to every prospective assembly customer; and the moat is software you don't have ([VLA models](vla-models.md)) | …you already own core components + distribution and accept that assembly-for-others is foreclosed |
| **Anchor CM partnership** | Jabil↔Apptronik (2025-02) | Low–Med | Anchor mortality (startup counterparty); volumes may stay pilot-scale for years | …you want learning-by-building with bounded capex and can pick a well-capitalized anchor (Apptronik-class: >$935M raised, Google/Mercedes backing) |
| **Manufacturing JV with a robot OEM** | Lens↔AgiBot (2025-04) | Medium | Governance/IP leakage; small registered JVs are options, not commitments — don't over-read them (RMB 10M) | …a volume-credible OEM (AgiBot shipped 5K+ in 2025) wants co-located capacity and you want shared upside |
| **Strategic investment / PIPE** | Foxconn→Agility ~$200M PIPE lead (2026-06) | Med (financial) | Capital without manufacturing rights — Foxconn's PIPE is explicitly not a build contract; mark-to-market on frothy valuations ([Investment](investment.md) bubble watch) | …you want board-level information and optionality before committing plant, and can tolerate venture-style marks |
| **Component wedge** | Goertek (sensors/acoustics posture); Hyundai Mobis (Atlas actuators); Sanhua (Optimus actuator components, reported/unverified) | Medium | Chinese price deflation 15–20%/yr; commodity margins in any tier China owns | …you have differentiated precision-mechanics, optics, acoustics, or battery-pack DNA that maps to §2's Low/Medium-difficulty rows |
| **Picks-and-shovels: test rigs, EOL lines, swap/charging, teleop & data-capture hardware** | Flex↔Teradyne (2026-04); nobody owns humanoid EOL test yet | Low | Small near-term pool | …you want exposure that survives *both* the shakeout and the form-factor debate — every surviving brand needs test and data infrastructure ([Data foundry](data-foundry.md)) |
| **Wait** | Wistron Corp, Inventec (de facto) | None | Lockout from anchor accounts for the 2028–30 ramp; automotive-style design-win stickiness means late entry buys leftovers | …you weight Brooks/reliability skepticism heavily or your capacity is fully monetized by AI-server demand anyway (a real opportunity cost as of 2026: GB300 lines earn today) |

- Cross-cutting judgment: the **portfolio answer beats the single bet** — e.g., one anchor CM relationship + one component wedge + picks-and-shovels, totaling low-hundreds-of-$M exposure, replicates most of the upside of Foxconn's posture without an own-brand program.
- The Nvidia ecosystem is the de-facto coordination layer (GR00T/Isaac/Thor across Foxconn, Quanta/Techman, Pegatron, Agility, Boston Dynamics — see [Company: NVIDIA](company-nvidia.md)); alignment with it is near-free optionality for any ODM already in Nvidia's server supply chain.

## 6. What would make this urgent (FOMO evidence, honestly framed)

### The dated-commitment ledger

| Date | Peer move |
|---|---|
| 2025-01 | Foxconn chairman announces Nvidia service-humanoid co-development in Kaohsiung (reiterated 2026-01/02) |
| 2025-02-25 | Jabil named Apptronik's worldwide manufacturing partner; Apollo deployed in Jabil ops |
| 2025-04 | Lens×AgiBot JV (Hunan Zhiqi Future) registered, Changsha |
| 2025-08 | Lens discloses assembly across AgiBot's full 2025 lineup |
| 2025-09-21 | Yunzhihui (Foxconn-affiliated) × UBTech global strategic cooperation signed (2025–27) |
| 2025-10 | Foxconn announces humanoids on Houston GB300 line at NVIDIA GTC DC (target start Q1 2026) |
| 2025-11 | Luxshare guides 3,000 humanoid shipments for 2025 (company-reported) |
| 2026-04-22 | Flex×Teradyne expansion (cobots/AMRs + UR component manufacturing) |
| 2026-06-09 | MIIT/SASAC special action launches (100+ scenarios, 万台级 capability by end-2026) |
| 2026-06-24 | Agility SPAC announced with Foxconn-led ~$200M+ PIPE |

Cadence is accelerating, and each move makes the next cheaper to justify — classic design-win-race dynamics.

### Capacity and slots being locked (as of 2026-07)

- **Assembly slots**: Jabil holds the Apollo franchise; Lens holds AgiBot's; Hyundai's 30K/yr robot plant + Mobis actuator supply internalize the Atlas chain; Figure and Tesla are closed shops. Of the credible US platforms, the unassigned manufacturing slots are already few.
- **Component capacity**: Beite's Kunshan plant (2.6M roller-screw sets/yr, mass production 2026); Xynova hand plant (10K/yr, Q2 2026); AgiBot's hand spin-off; LinkerBot targeting 50–100K hands in 2026 (company statements, unverified). PRS grinding remains the most-cited physical bottleneck ([Hardware](hardware.md)) — scarce capacity is being claimed now.
- **Design-win stickiness**: humanoid BOMs are still fluid (Figure 03 vs 02 changed actuators, hands, charging; Atlas redesigned for automotive parts). Whoever co-develops DFM at this stage shapes the product toward their own processes — the same mechanism that made early iPhone and EV suppliers durable incumbents.

### Honest counterweights

- Every deal in the ledger is denominated in **tens to low hundreds of $M** — no humanoid manufacturing contract yet approaches a single phone-program's value. The FOMO is about *position*, not present revenue.
- The two largest planned manufacturing programs on Earth (Tesla, Figure) are explicitly not available to win.
- Several ledger entries are options dressed as commitments (RMB 10M JV; a PIPE; a chairman's forum remark). Grade peers by steel-in-the-ground, and by that metric only Jabil, Lens, and Luxshare have actually done manufacturing-adjacent things with humanoids — Foxconn's Houston deployment was slated to start Q1 2026, but its live status is unconfirmed as of 2026-07.
- If the 2026 forecasts slip the way every prior humanoid timeline has, "urgent" converts to "early" at zero notice. The urgency case rests on the cost asymmetry — entry stakes are cheap relative to ODM balance sheets, lockout for the real ramp is not — rather than on near-term P&L.

## Sources

- https://investors.jabil.com/news/news-details/2025/Apptronik-and-Jabil-Collaborate-to-Scale-Production-of-Apollo-Humanoid-Robots-and-Deploy-in-Manufacturing-Operations/default.aspx — Jabil×Apptronik primary release (2025-02-25): worldwide manufacturing partner, Apollo deployed in Jabil operations.
- https://www.therobotreport.com/apptronik-collaborates-with-jabil-to-produce-apollo-humanoid-robots/ — independent coverage of the Jabil-Apptronik scale-up and "Apollo building Apollo" framing.
- https://www.businesswire.com/news/home/20250225753929/en/Apptronik-and-Jabil-Collaborate-to-Scale-Production-of-Apollo-Humanoid-Robots-and-Deploy-in-Manufacturing-Operations — same announcement, wire version.
- https://stcn.com/article/detail/1636518.html — Lens×AgiBot JV (Hunan Zhiqi Future Technology 湖南智启未来科技) registration, RMB 10M, Changsha, shareholder list.
- https://www.thepaper.cn/newsDetail_forward_31296583 — JV scope: humanoid R&D + precision-manufacturing line.
- https://www.nbd.com.cn/articles/2025-08-04/4000682.html — Lens disclosure (2025-08): manufacturing/assembly across AgiBot's full 2025 humanoid lineup; Zhiding investment.
- https://www.leaderobot.com/news/6770 — Luxshare: 3,000-unit 2025 guidance, Manufacturing 2.0 line, self-developed reducers/tendon hand (company-reported); **also the single source attributing the ¥124M China Mobile order to Luxshare — contested, see next**.
- https://www.guancha.cn/economy/2025_07_12_782708.shtml — primary tender coverage (2025-07): China Mobile's ¥124.05M humanoid biped contract-manufacturing procurement won by AgiBot (¥78M) + Unitree (¥46.05M) — contradicts the Luxshare attribution.
- https://finance.sina.com.cn/tech/roll/2025-11-27/doc-infyvtha0077094.shtml — Luxshare humanoid guidance and three-pillar strategy (2025-11, company statements).
- https://m.ofweek.com/im/2025-11/ART-201900-8100-30674854.html — Luxshare ~80% self-developed core-component target by mid-2026; prototype reveal plan (company-reported).
- https://www.assemblymag.com/articles/99628-foxconn-to-deploy-humanoid-robots-on-production-line-at-houston-ai-server-plant — Foxconn Houston GB300 plant humanoid deployment, Q1 2026 target, Isaac GR00T/Jetson Thor stack.
- https://www.therobotreport.com/humanoid-maker-agility-robotics-go-public-through-spac-merger/ — Agility $2.5B SPAC terms; $300M contracted Digit v5 orders; PIPE structure.
- https://www.techtimes.com/articles/319099/20260625/humanoid-robot-ipo-agility-robotics-signs-spac-deal-us-nasdaq-debut.htm — Foxconn leading the >$200M PIPE (2026-06-24/25 coverage).
- https://www.agilityrobotics.com/content/agility-robotics-to-go-public-through-merger-with-churchill-capital-corp-xi — Agility primary release: >$620M gross proceeds, investor list incl. Foxconn.
- https://www.geekwire.com/2026/digit-maker-agility-robotics-to-go-public-in-2-5b-deal-heres-what-the-filings-say-about-its-finances/ — Agility SPAC-filing financials (heavy losses; order-book context).
- https://www.stcn.com/article/detail/3349413.html — UBTech × Yunzhihui global strategic cooperation agreement signed 2025-09-21 (Securities Times): 2025–27 scope, Yunzhihui responsible for global sales/marketing/after-sales.
- https://caifuhao.eastmoney.com/news/20251118194548969453820 — follow-up coverage of the Yunzhihui × UBTech 2025–2027 industrial-humanoid cooperation (2025-11).
- https://www.cna.com.tw/news/afe/202501030226.aspx — CNA (2025-01-03): Liu Young-way first announces Foxconn×Nvidia service-humanoid plan for Kaohsiung.
- https://www.21jingji.com/article/20260210/herald/c7e320646a87f919e869c3f343841278.html — Liu Young-way reiteration (2026-01/02): Foxconn co-developing service humanoids with Nvidia in Kaohsiung.
- https://www.tm-robot.com/en/company/news/Techman-Robot-at-GTC-2026_Unveils-New-AI-Strategy-and-Humanoid-Robot-TM-Xplore-I — Techman primary: TM Xplore I launch at NVIDIA GTC 2026 (2026-03-18) with Quanta Cloud Technology; wheeled-base humanoid, Jetson Thor.
- https://roboticsandautomationnews.com/2025/08/27/techman-robot-unveils-humanoid-prototype-aims-for-2026-launch/93937/ — TM Xplore I prototype unveiling (2025-08-27), 2026 launch target.
- https://money.udn.com/money/story/11162/8952450 — Techman Robot (Quanta group) "TM Xplore I" humanoid with Nvidia, production targeted 2026 (Taiwanese press).
- https://www.ctee.com.tw/news/20250726700012-430502 — GB300 NVL72 Taiwan supply chain reportedly introducing humanoid-assisted assembly (2025-07, Chinese-language industry press, unverified).
- https://www.technice.com.tw/issues/ai/158236/ — Pegatron robotics BU, components-first 5-year plan, Tung Tzu-hsien framing.
- https://udn.com/news/story/7240/8470291 — Pegatron "Aria" service robot showcase details.
- https://news.cnyes.com/news/id/4329179 — Tung: Nvidia names Taiwanese supply-chain players incl. Pegatron as humanoid beneficiaries.
- https://ai.inventec.com/%E8%8B%B1%E6%A5%AD%E9%81%94%E6%96%BCcomputex-2026%E5%B1%95%E7%8F%BEai%E8%90%BD%E5%9C%B0%E5%AF%A6%E5%8A%9B/ — Inventec COMPUTEX 2026: Atlas Edge AI server (IGX Thor), iTwin cobot, iUGV (company materials).
- https://investors.flex.com/news/news-details/2026/Flex-and-Teradyne-Robotics-Expand-Partnership-to-Scale-Intelligent-Automation-Across-Global-Manufacturing/default.aspx — Flex×Teradyne expansion (2026-04-22): deploy UR/MiR + manufacture key UR components (primary).
- https://www.therobotreport.com/flex-teradyne-expand-partnership-scale-physical-ai/ — independent confirmation of the Flex-Teradyne physical-AI framing.
- https://finance.sina.com.cn/stock/bxjj/2026-06-23/doc-iniekqut6549406.shtml — Goertek investor Q&A (2026-06): robot-related layout, components positioning, no final-assembly disclosure.
- https://view.inews.qq.com/a/20260623A06YPI00 — Goertek: same statement, secondary confirmation.
- https://www.stcn.com/article/detail/1353689.html — BYD Electronics investor-facing smart-product/humanoid framing (listed-entity scope).
- https://www.qbitai.com/2024/12/238878.html — BYD Group-level humanoid program and 20,000-robot 2026 deployment target (reported, unverified aspiration).
- https://finance.sina.com.cn/stock/t/2026-06-03/doc-iniactaq0858417.shtml — "short-term phone/auto, long-term AI" market framing of BYDE (2026-06).
- https://www.stcn.com/article/detail/3568326.html — Securities Times (2025-12-31): Peng Zhihui's open letter as Shangwei/Swancor chairman launching the force-controlled mini humanoid 启元Q1 (Qiyuan Q1, brand 上纬启元).
- https://techorange.com/2026/01/02/china-primebot-q1-humanoid-robot/ — Shangwei/上纬 "Qiyuan Q1" mini humanoid launch coverage — the entity behind the Wistron name-collision warning.
- https://bostondynamics.com/blog/boston-dynamics-unveils-new-atlas-robot-to-revolutionize-industry/ — electric Atlas: fewer unique parts, "designed for compatibility with automotive supply chains" (official).
- https://www.hyundai.com/worldwide/en/newsroom/detail/hyundai-motor-group-announces-ai-robotics-strategy-to-lead-human-centered-robotics-era-at-ces-2026-0000001100 — Hyundai CES 2026: Mobis actuator supply for Atlas, 30K/yr robot plant, Metaplant deployment from 2028 (official).
- https://eu.36kr.com/en/p/3780742359243776 — State Grid ~¥6.8B embodied-robot procurement: 500 humanoids (¥2.5B) / 3,000 dual-arm (¥1.8B) / 5,000 quadrupeds (¥1.5B); 2026 Q1-pilot/Q3-scale/Q4-supplementary phasing (origin source for the breakdown; phasing unverified).
- https://interestingengineering.com/ai-robotics/china-8500-robots-power-grid — Western secondary echo of the 8,500-unit/¥6.8B State Grid breakdown.
- https://www.scmp.com/economy/china-economy/article/3351323/china-plans-invest-billions-robot-army-run-its-power-grid — SCMP corroboration of the billions-scale State Grid robot program.
- https://www.miit.gov.cn/zwgk/zcwj/wjfb/tz/art/2026/art_f291ccd3da4c47ce95741de63cc088e6.html — MIIT/SASAC joint notice (primary): 2026 Humanoid Robot & Embodied Intelligence Real-Scene Training Special Action.
- https://www.news.cn/tech/20260612/a069b3a9948b4e0aaaa94cf3d618e545/c.html — Xinhua (2026-06-12): special-action launch; 100+ high-value scenarios, 万台级 deployment-capability goal by end-2026.
- https://technode.com/2026/01/09/chinas-agibot-leads-global-humanoid-robot-shipments-in-2025-omdia-says/ — Omdia 2025: 13,317 global shipments, vendor table.
- https://www.globaltimes.cn/page/202601/1354054.shtml — IDC 2025: ~18,000 units, +508% YoY.
- https://www.scmp.com/tech/article/3358210/morgan-stanley-raises-china-humanoid-robot-shipment-forecast-50000-units — Morgan Stanley 2026 China forecast raised to 50K (2026-06-24).
- https://www.cnbc.com/2026/06/24/morgan-stanley-china-humanoid-robot-market-forecast.html — Morgan Stanley forecast ladder (14K → 28K → 50K during 2026), ~$2B China humanoid market in 2026, State Grid order cited as driver.
- https://www.prnewswire.com/news-releases/ai-to-reshape-the-global-technology-landscape-in-2026-says-trendforce-302626789.html — TrendForce (2025-11-26): 2026 global humanoid shipments to surpass 50,000 units (+~700%).
- https://m.jiemian.com/article/13925066.html — IDC: ~18,000 units and ~$440M global humanoid market revenue in 2025.
- https://www.press.bmwgroup.com/global/article/detail/T0455864EN/bmw-group-to-deploy-humanoid-robots-in-production-in-germany-for-the-first-time?language=en — BMW primary (2026-02-27): Figure 02 Spartanburg pilot completed (~1,250 h, 30,000+ X3s); first German pilot (Leipzig) goes to Hexagon AEON, not Figure; Figure 03 use cases under evaluation.
- https://www.press.bmwgroup.com/global/article/detail/T0458778EN/bmw-group-advances-the-use-of-physical-ai-in-production-with-figure-03-project-in-spartanburg?language=en — BMW primary (2026-06-25): Figure 03 sequencing-logistics project at Spartanburg — the relationship continued past the 02 retirement.
- https://interestingengineering.com/ai-robotics/figure-humanoid-robots-retires-bmw — Figure 02 robots retired visibly worn after the 11-month BMW deployment (2025-11).
- https://neura-robotics.com/neura-robotics-bosch-partnership/ — Neura×Bosch partnership (announced 2026-01): Bosch production workers wear sensor suits to generate motion/workflow training data.
- https://electrek.co/2026/07/02/musk-shuts-down-optimus-4d-chess-theory/ — Musk X post (2026-07-01): "Optimus production will be extremely slow at first… This is not like making a car."
- https://www.goldmansachs.com/insights/articles/the-global-market-for-robots-could-reach-38-billion-by-2035 — Goldman $38B / 1.4M units by 2035.
- https://www.morganstanley.com/insights/articles/humanoid-robot-market-5-trillion-by-2050 — Morgan Stanley $5T-by-2050 ecosystem forecast.
- https://www.scmp.com/tech/article/3337151/china-packs-patent-punch-race-build-humanoid-robots — Morgan Stanley BOM: $46K with Chinese supply chain vs $131K without.
- https://eu.36kr.com/en/p/3780414717129481 — Optimus BOM split, Chinese supplier map, reported Sanhua ~$685M actuator order (single-source, unverified).
- https://www.mckinsey.com/industries/industrials/our-insights/turning-humanoid-supply-chain-constraints-into-billion-dollar-wins — China component shares (bearings ~40%, motors ~35%, magnet processing ~90%).
- https://autonews.gasgoo.com/articles/news/from-prototypes-to-production-dexterous-hands-kick-off-a-mass-production-race-2016425582734970881 — dexterous-hand volume race: >30K hands 2025 (derived), Inspire ~10K, Xynova plant, capacity build-out.
