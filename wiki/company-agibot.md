---
title: "Company Deep Dive: AgiBot (智元机器人)"
slug: company-agibot
updated: 2026-07-05
confidence: verified
---
> AgiBot (Zhiyuan Robotics / 智元机器人, Shanghai, founded 2023-02 by ex-Huawei VP Deng Taihua and ex-Huawei "Genius Youth" maker-celebrity Peng Zhihui "稚晖君") is the volume-and-data champion of Chinese Physical AI: fastest company to 10,000 cumulative general-purpose robots (2026-03, ~3 years from founding), 15,000th unit by 2026-06-28, and Omdia's 2025 shipment #1 (5,168 humanoids, 39% share — a crown Unitree's own prospectus disputes with >5,500). Its differentiated bet is a **full-stack open ecosystem**: the largest open real-robot manipulation dataset (AgiBot World, >1M trajectories from 100 robots in a 4,000 m² Lingang facility), open foundation models (GO-1 2025-03 → GO-2 2026-04, Genie Envisioner world models), a three-line product matrix (远征 Expedition A-series, 灵犀 Lingxi X-series, 精灵 Genie G-series), and a deliberately partner-heavy manufacturing posture that pulls China's consumer-electronics ODM/EMS chain (Lens Technology, Joyson/Pusmart, Longcheer) into humanoids. Capital story is equally aggressive: ~10+ venture rounds (Tencent, HongShan, BYD, JD, Hillhouse, LG) to a ~RMB 15B (~$2.1B) private mark, control of STAR-listed Swancor (~63.6%, ~RMB 2.1B, 2025-07 — "backdoor listing" denied), and a reported HK$40–50B HK IPO ambition (unverified). Skeptic case: revenue (~RMB 1B 2025, company-reported) trails Unitree's ~RMB 1.7B on similar volumes, profitability is undisclosed, overseas presence is nascent, and reliability/revenue-quality questions persist. Context: [Landscape: China](landscape-china.md), [Unitree](company-unitree.md), [Data](data.md), [Data foundry](data-foundry.md), [VLA models](vla-models.md), [Investment](investment.md).

## Company at a glance (as of 2026-07)

| Field | Value |
|---|---|
| Founded | 2023-02, Shanghai (智元机器人; legal entity AGIBOT Innovation (Shanghai) Technology Co., Ltd. / 智元创新(上海)科技股份有限公司 — converted from LLC to joint-stock company 2025-11, a standard pre-IPO step) |
| Founders | **Deng Taihua** (邓泰华, chairman & CEO; ~20-yr Huawei veteran, ex-VP who built the Kunpeng/Ascend compute lines) + **Peng Zhihui** (彭志辉 "稚晖君", co-founder, president & CTO; ex-Huawei "Genius Youth," Bilibili maker celebrity) |
| Private valuation | ~RMB 15B (~$2.1B) (as of 2025-08 rounds; PitchBook $2.07B as of 2026-03) |
| Key investors | Tencent (led 2025-03 round), HongShan/Sequoia China, Hillhouse, BYD, JD.com (0.75%), SAIC, BAIC, TCL, CICC, LG Electronics + Mirae Asset (strategic, 2025-08); total raised >$725M (secondary aggregate, unverified) |
| 2025 shipments | **5,168 humanoids** (Omdia #1, 39% global share); IDC ~5,200, also #1; Unitree disputes with >5,500 (methodology conflict) |
| Cumulative units | 1,000th (2025-01-06) → 5,000th (2025-12-08) → **10,000th (rolled off 2026-03-28, announced 2026-03-30; an Expedition A3)** → **15,000th (2026-06-28, a Genie G2)** |
| 2025 revenue | >RMB 1B (~$140M) (company-reported; chairman's guidance "超10亿元" — no audited figures public) |
| Profitability | Undisclosed; presumed loss-making (no public data) (unverified) |
| Product lines | 远征 Expedition A1/A2/A2-W/A2-Max/A3 (full-size biped); 灵犀 Lingxi X1 (open-source)/X1-W/X2 (compact); 精灵 Genie G1/G2 (wheeled dual-arm industrial); OmniHand dexterous hand (spun off 2026); C5 cleaning robot |
| Models / data | GO-1 (2025-03, open), GO-2 (2026-04-09); Genie Envisioner 1.0 (2025-08) / 2.0 (2026-04-10) world models; Genie Sim; AgiBot World dataset (>1M trajectories, open); 灵渠 Lingqu OS (2025-07) |
| Listed vehicle | **Swancor Advanced Materials / 上纬新材 (STAR 688585)**: ~63.6% control acquired for ~RMB 2.1B (~$290M) 2025-07; Peng Zhihui installed as chairman after 2025-11 board overhaul |
| IPO status | Reported HK IPO plan for 2026 at HK$40–50B (~$5.1–6.4B) target with CICC/CITIC as lead banks + Morgan Stanley (Reuters exclusive 2025-10: prospectus filing planned early 2026, listing by Q3 2026, 15–25% float); **company denied concrete plans in 2025 statements and declined comment to Reuters**; no filing visible as of 2026-07 |
| Manufacturing | Own Lingang/Fengxian (Shanghai) plant (volume production from late 2024, ~300 units/month by 2025-01) **plus** contract/JV manufacturing with Lens Technology, Joyson's Pusmart, and a supplier-equity web (15 startups invested, 17 JVs — reported) |

## 技术路线 — tech route & architecture

AgiBot's stack bet is **"data + open ecosystem" first, hardware as the carrier** — the closest thing in Physical AI to an "Android play," and the mirror image of [Unitree's](company-unitree.md) hardware-cost-down-first route and [Figure's](company-figure.md) closed single-embodiment stack.

- **Layer 1 — bodies (multi-form-factor, not one robot)**: three parallel lines matched to scenario economics — full-size biped Expedition A-series (service/interactive + industrial), compact Lingxi X-series (education/consumer-adjacent; X1 fully open-sourced incl. hardware designs), wheeled dual-arm Genie G-series (industrial tasks + data collection; the workhorse of AgiBot World). Rationale: wheeled bases and task-specific forms deploy and earn *now*, while bipeds mature — a contrarian position vs. biped-purists.
- **Layer 2 — data as strategic asset**: the **AgiBot World** program (with Shanghai AI Lab/OpenDriveLab) collected **>1M trajectories / 2,976 h / 217 tasks / 3,000+ objects on 100 homogeneous dual-arm robots** in a purpose-built **4,000 m² Lingang facility** simulating home/retail/industrial/restaurant/office domains, ~30–50k episodes/day via VR teleoperation (company figures) — then **open-sourced it** (CC BY-NC-SA 4.0), explicitly claiming it bigger and better-curated than Google's OXE; pretraining on it beat OXE-pretraining by ~30% (single-team claim; IROS 2025 Best Paper finalist). Follow-up **AgiBot World 2026** release + **AgiBot World Challenge** (ICRA 2026: 526 teams, 27 countries, real-robot final scoring). Proprietary firehose stays internal; a data-ops arm (觅蜂) targets 10M hours of data production by end-2026 (executive statement, unverified). See [Data](data.md), [Data foundry](data-foundry.md), [Evaluation](evaluation.md).
- **Layer 3 — models**: **GO-1** (Genie Operator-1, 2025-03; arXiv:2503.06669) — ViLLA architecture (InternVL2.5-2B VLM + latent-action planner + diffusion action expert), >60% success on complex tasks, +32% vs RDT; weights open on Hugging Face. **GO-2** (2026-04-09, at "AgiBot AI Week" 2026-04-07–14): unified reasoning + action in one architecture ("bridging the semantic–actuation gap"); CVPR/ACL 2026 papers. **Genie Envisioner** world models (1.0 open-sourced 2025-08; **GE 2.0 / GE-Sim 2026-04-10** turns the world model into an interactive "world simulator" with action-driven dynamics, minute-level stability, built-in reward modeling — used for evaluation, RL, and in-model teleoperation) plus **Genie Sim 3.0** simulation platform (open on GitHub). See [VLA models](vla-models.md), [World models](world-models.md), [Simulation](simulation.md).
- **Layer 4 — OS and deployment tooling**: 灵渠 **Lingqu OS** open robot operating system (2025-07); **Genie Studio** dev platform and **Genie Studio Agent** (2026) — zero-code, node-based task assembly (grasping, navigation, VLA decision nodes) aimed at making integrators, not roboticists, the deployment workforce; **LinkCraft** zero-code choreography tool (2025-10).
- **Layer 5 — components**: self-developed **PowerFlow** joint actuators (flagship: ~350 N·m peak at 1.6 kg, quasi-direct-drive, dual encoders, liquid cooling; modular R86/R52 variants in X1) and **OmniHand** tactile dexterous hands (RMB 9,800–14,800 — cheapest credible tactile hand; spun off 2026 as a standalone component supplier). See [Hardware](hardware.md), [Tactile & hands](tactile-hands.md).
- **Why this differs from rivals**: Unitree vertically integrates components to win on price and margin; Figure/Tesla close the whole stack to own the flywheel; AgiBot **gives away data, models, sim, OS, and even one robot's hardware design** to become the ecosystem default, monetizing via volume hardware, solutions, and (eventually) the platform — while using JVs/equity to lock in the supply chain rather than build everything in-house. The open-data strategy doubles as a state-alignment play (China's answer to closed US corpora — see [Landscape: China](landscape-china.md)).

## The bet / vision

- **Deng Taihua (CEO)**: "2026 年是部署态元年，具身智能正式从'能动'走向'会干'" — *2026 is Year One of the "deployment state": embodied AI moves from "can move" to "can do work."* (AgiBot Partner Conference / APC 2026, Shanghai Zhangjiang, 2026-04-17)
- **Peng Zhihui (CTO)**: "行业正在从'卖机器人'转向'交付结果'" — *the industry is shifting from selling robots to delivering outcomes* — and, on openness: "整个具身智能行业目前还在共同探索，没有任何一家企业能独自给出正确答案。我们需要协力攻破瓶颈，在正确的时间做正确的事" — *no single company can find the right answer alone; we must jointly break the bottlenecks and do the right things at the right time.*
- **Yao Maoqing (姚卯青, senior VP, embodied intelligence)**: internal calibration that the field's "GPT-3 progress bar" sat at ~5–10% through early 2026 and should reach **20–30% by end-2026** — i.e., leadership publicly frames current humanoids as pre-GPT-3, with deployment data as the accelerant.
- The founder-level thesis, assembled: **scale real-world deployment first** (even in unglamorous scenarios — reception, performance, inspection, education), because deployed fleets generate the data that trains the models that unlock the real labor market; open-source the commodity layers so the ecosystem standardizes on AgiBot's formats. Peng's celebrity (millions of Bilibili followers; 2026 China Youth May Fourth Medal; Xinhua profile 2026-05) gives the company a consumer-facing charisma no other Chinese robotics firm has; Deng supplies Huawei-style organizational execution and the capital network (both are UESTC alumni; Deng recruited Peng out of Huawei in 2022) — Chinese tech media reads AgiBot as "a Huawei-system company wearing a maker-celebrity's face."

## Products & deployments — real numbers

| Line | Models (launch) | Positioning | Numbers |
|---|---|---|---|
| 远征 Expedition | A1 (2023-08), A2 / A2-W / A2-Max (2024), A3 (2026-02) | Full-size biped; interactive service, reception, entertainment; A2-W wheeled industrial | A2 ~$100K class (reported); A2 Guinness record 106.286 km walk Suzhou→Shanghai (2025-11); A3: 173 cm / 55 kg, 10-h endurance, aerial martial-arts demos, ~$45K (reseller-reported, unverified); 1,742 A-series cumulative by 2025-12 |
| 灵犀 Lingxi | X1 (2024, open-source), X1-W, X2 (2025-03-11) | Compact (~1.3 m) low-cost; education, research, light interaction | 1,846 X-series cumulative by 2025-12 (largest line by units); 5,000th-unit ceremony robot was an X2 delivered to actor Huang Xiaoming's studio (2025-12) |
| 精灵 Genie | G1 (2024), G2 (2025) | Wheeled dual-arm "embodied task robot"; industrial ops + data collection; the AgiBot World embodiment | 1,412 G-series cumulative by 2025-12; 15,000th robot (2026-06) was a G2 delivered to ODM Longcheer |
| Components | OmniHand / OmniHand Pro; PowerFlow joints | Sold/spun off as supplier layer | OmniHand RMB 9,800–14,800; hand unit spun off 2026 |

- **Cumulative production curve**: ~2 years to first 1,000 (2025-01) → ~1 year to 5,000 (2025-12) → **3 months to 10,000 (2026-03)** — a >4x rate acceleration (company-reported) → 15,000 (2026-06-28). 2026 guidance: "数万台" (tens of thousands) (company statement via CLS, 2025-12).
- **Flagship industrial proof point (2026-06)**: six-day **global livestream at Longcheer's Nanchang tablet factory** — a G2 fleet ran 64+ hours on a live mass-production line, completing **64,828 tasks across four QC workflows (multimedia-interface, audio, radiated-spurious-emission, coupling tests) at a company-reported 99.99% success rate**, contributing to 17,625 tablets (company-run demo; better than lab demos but partner is also an investor-adjacent customer). Earlier: four humanoids ran a livestreamed 8-hour factory shift (2026-04).
- **Scenario mix** (per IDC, 2025): #1 in shipments across five mainstream scenarios; deployments span reception/guide, entertainment & commercial performance, industrial handling/3C loading, logistics sorting, security inspection, data collection, research & education — i.e., today's volume is mostly *not* factory labor (same structural caveat as Unitree's 74% research/education mix).
- **Overseas (early)**: certifications for China/US/EU markets (2025-05); Malaysia AI-robot experience center (2026-01, i-City Shah Alam — AgiBot's first overseas experience center); Singtel operator partnership in Singapore (2026-03); Germany launch in Munich with auto-parts maker Minth as partner (2026-02-24); APC partner conferences in Thailand, Indonesia, UK (2026); **UK Robot-as-a-Service launch + European A3 debut (2026-07-02)**; A3 rentals from ~EUR 899/day via local partners (reseller-reported). Target: overseas ~30% of 2026 revenue, trending toward 50%+ (executive statement, unverified).
- High-protocol demos: Lee Hsien Loong (2024-11); Xi Jinping viewed AgiBot robots during a Shanghai visit (2025-04) — state-visibility markers few private startups get.

## Business model & unit economics

- **Revenue trajectory (company-reported, unaudited)**: RMB ~0.3M (2023) → ~RMB 60M+ (2024) → **>RMB 1B (2025)** — vs Unitree's audited RMB 1.69–1.71B (2025). Implied blended ASP if 2025 revenue were all robot sales: ~RMB 200K/unit on 5,168 units (inference — mix includes hands, solutions, data services; treat as order-of-magnitude only).
- **Revenue streams**: (1) hardware sales across three lines; (2) **solutions** — "seven productivity solutions" in three directions: industrial manufacturing (3C part loading, palletizing, logistics sorting), commercial services (retail guide, chain F&B, service stations), special operations (security inspection, industrial cleaning); (3) **rental/RaaS** — domestic 擎天租 rental platform (China robot-rental market est. >RMB 1B in 2025) and the UK RaaS model (2026-07); (4) education/research bundles (X1, G-series); (5) components (OmniHand, PowerFlow — now partly via spin-off); (6) data/platform services (Genie Studio; data collection as a product).
- **Ecosystem-equity model**: in roughly a year AgiBot invested in ~15 startups and formed ~17 joint ventures (Chinese media tally, unverified) — using its valuation as currency to bind suppliers, integrators, and channel partners; more like a mini-Huawei/automotive-Tier-1 network than a typical startup.
- **Profitability**: never disclosed; the Swancor vehicle and IPO ambitions suggest continued external funding needs. Contrast: Unitree is GAAP-profitable (~RMB 288M net, 2025). No public gross-margin data (unverified).
- **Revenue-quality skeptic file**: Caijing cover story (2025-11) reportedly described a ~1,000-unit order where ~30% of robots were faulty and payment was never collected (single source, unverified; the original Caijing link was dead as of 2026-07 and the claim could not be re-verified elsewhere — treat as unconfirmed); the sector-wide commercial-performance rental crash is independently documented — e.g., Unitree G1 day-rates fell from ~RMB 15K (2025-02) to ~RMB 5–8K by mid-2025, and by 2026 older models rented for ~RMB 4–5K/day on AgiBot's own 擎天租 platform — the entertainment/rental demand pool AgiBot partly sells into is bubble-prone; several flagship "customers" (Longcheer, JV partners) are also ecosystem/capital partners — arm's-length demand is hard to isolate until audited filings appear.

## Capital access: Swancor and the IPO path

- **2025-07**: AgiBot-affiliated vehicles (智元恒岳, 智元新创) agreed to acquire **~63.62% of Swancor Advanced Materials (上纬新材, STAR 688585)** — a wind-blade-resin/composites maker — for **~RMB 2.1B (~$290M)** at RMB 7.78/share via negotiated transfer + tender offer; first deal of its kind by a humanoid startup.
- AgiBot **denied "backdoor listing"** (does not meet CSRC major-asset-restructuring definitions, it argued; also stated no major asset restructuring planned within 12 months) and denied concrete HK IPO plans (2025 statements; it declined comment on the 2025-10 Reuters report). Market voted otherwise: Swancor's stock ran up as much as ~20x — Securities Times' "20倍大牛股" characterization (2025) — and a **2025-11-25 board overhaul installed AgiBot founders — Peng Zhihui became Swancor chairman** (with 智元恒岳 as controlling shareholder and Deng Taihua as actual controller).
- **Reported HK IPO** (Reuters exclusive 2025-10 + Chinese media): 2026 listing targeting **HK$40–50B (~$5.1–6.4B)** valuation, CICC/CITIC Securities/Morgan Stanley as sponsors — no visible filing as of 2026-07 (unverified). The 2025-11 joint-stock conversion is consistent with either an HK listing or an eventual A-share route.
- Net effect: AgiBot holds **three capital channels** — private mega-rounds, a controlled listed A-share vehicle, and a prospective HK listing — the deepest capital optionality of any Chinese humanoid startup (see [Investment](investment.md)). Watch whether Swancor becomes an asset-injection vehicle despite denials.

## Strengths / weaknesses vs peers

**Strengths**
- **Volume + production ramp**: fastest to 10,000/15,000 cumulative units; 2025 shipment #1 per Omdia and IDC; three product lines de-risk any single form factor.
- **Data assets nobody matches openly**: AgiBot World is the largest open real-robot manipulation corpus; the Lingang collection facility + deployed-fleet flywheel is a structural moat *if* data-scaling laws hold (see [Data](data.md)).
- **Capital access & state alignment**: Tencent/BYD/JD/SAIC/BAIC cap table, Swancor listed vehicle, Shanghai/Lingang government cooperation, named candidate supplier in State Grid's reported RMB 6.8B 2026 embodied-robot plan ([Landscape: China](landscape-china.md)).
- **Founder pairing**: Peng's public charisma (recruiting, brand, retail-investor pull) + Deng's Huawei-scale operational playbook.
- **Ecosystem gravity**: open models/data/sim/OS + ICRA challenge + NVIDIA GR00T using AgiBot embodiments make it the default Chinese research/ecosystem platform alongside Unitree.

**Weaknesses / skeptic case**
- **Revenue lags volume**: ~RMB 1B (company-reported, unaudited) vs Unitree's audited RMB 1.7B with profits; no disclosed margins; heavier reliance on rental/performance/education demand of uncertain durability.
- **Related-party demand blur**: JV partners and investees double as customers and demo hosts (Longcheer); until an IPO prospectus forces audited disclosure, unit-economics claims are unverifiable.
- **Reliability questions**: the Caijing 30%-defect order report (unverified) and the sector-wide performance-rental price crash cut against the "deployment leader" narrative.
- **Thin overseas base**: exports just starting (experience centers, partner conferences, one RaaS launch) vs Unitree's years of >35–55% overseas revenue; the 30%-overseas 2026 target is aggressive.
- **US/allied scrutiny risk**: not yet on the Pentagon 1260H list (unlike Unitree, 2026-06) or named in the GUARD Act, but any Chinese humanoid at scale is in the blast radius of pending US import/procurement legislation; deep state-linked cap table raises the odds ([Safety & regulation](safety-regulation.md)).
- **Shipment-crown ambiguity**: Omdia's 5,168 vs Unitree's >5,500 prospectus claim — AgiBot's #1 is methodology-dependent; it markets the ranking harder than the data supports (see reconciliation in [Humanoids](humanoid-robots.md)).
- **Open-ecosystem paradox**: giving away data/models subsidizes rivals too (GO-1/AgiBot World are in competitors' training mixes); the moat depends on staying ahead of the corpus it publishes.

## Manufacturing & supply-chain posture

The section that most distinguishes AgiBot for ODM/EMS watchers: it is the humanoid maker most deliberately **importing China's consumer-electronics contract-manufacturing model** into robotics.

- **Dual-track production**: own **Lingang (Fengxian, Shanghai) plant** — established early 2024, volume production from ~H2 2024 (company accounts variously date the start to 2024-08 or 2024-10), 962 units by 2024-12-15, ~300 units/month by 2025-01 — *plus* external manufacturing partners ("自有工厂 + 代工" hybrid). Strategic cooperation with Lingang Group (Shanghai state-owned developer) anchors land/policy support (reported).
- **Lens Technology (蓝思科技, Apple-chain glass/precision giant)**: co-developed Lingxi X1 — supplying joint modules, dexterous hands, torso shells, structural parts **and whole-unit assembly**; announced it would take on "AgiBot's full series of humanoid models" in 2026 (company statements); JV 智启未来 (Zhiqi Future) to build precision humanoid production lines. This is the clearest humanoid-EMS relationship in the industry (as of 2026-07).
- **Joyson Electronic / Pusmart (均普智能)**: JV 宁波普智未来 (Ningbo, 2025-04) for co-R&D, production and sales of humanoid bodies; first-phase 2,000 m² line rated ~1,000 robots/yr (~200 units actually targeted off the line in 2025, expanding toward ~2,000/yr in 2026), plus a planned ~RMB 200M (2亿+) Ningbo embodied-intelligence innovation center (reported).
- **Longcheer (龙旗科技, top-3 smartphone/tablet ODM)**: customer + deployment showcase (Nanchang factory G2 fleet; recipient of the 15,000th robot) — the template for selling robots *into* EMS plants as labor, closing the loop between ODM partners and demand.
- **Component strategy**: in-house where data/performance-critical — PowerFlow actuators, OmniHand (both now partly externalized: hand business spun off as a standalone supplier, 2026, mirroring automotive Tier-1 formation — see [Tactile & hands](tactile-hands.md)); external via equity-linked suppliers — e.g., Fulin Precision (富临精工) for precision reducers and smart electric joints (reported). Contrast Unitree: purchased components only ~14–18% of cost, near-total vertical integration; AgiBot instead **buys ecosystem lock-in with equity and JVs**, trading margin for speed and capital efficiency.
- **Why it matters**: if humanoids follow the smartphone cost curve, the winners of AgiBot's route are the ODM/EMS partners who learn robot assembly early (Lens, Pusmart, Longcheer) — AgiBot is effectively bootstrapping a humanoid Tier-1/EMS layer that any brand (including foreign ones) could later use. Watch whether Lens becomes to AgiBot what Foxconn was to Apple, and whether AgiBot's own Lingang capacity stays R&D/NPI-focused while partners take volume.
- **Supply-chain geography**: Yangtze Delta cluster (Shanghai base; suppliers across Jiangsu/Zhejiang/Hunan/Jiangxi via partners); >90%-domestic sourcing typical for Chinese humanoid BOMs (sector figure — see [Hardware](hardware.md), [Landscape: China](landscape-china.md)).

## What to watch (as of 2026-07)

- HK IPO filing (or Swancor asset injection) — either forces audited unit economics into public record; sponsor mandates already reported.
- Whether 2026 shipments hit "tens of thousands" and how much lands overseas (30% revenue target).
- Lens Technology's humanoid assembly ramp — the first real test of EMS-model humanoid manufacturing at scale.
- GO-2/GE-2.0 adoption outside AgiBot hardware; whether AgiBot World 2026 keeps the open-data lead as proprietary corpora (Generalist, Tesla, Figure) pull away.
- US legislative action (GUARD Act et al.) spillover onto AgiBot specifically.

## Sources

- https://en.wikipedia.org/wiki/AgiBot — founding (2023-02), founders, product-line taxonomy, production timeline (962 units 2024-12, 1,000th 2025-01), Lingqu OS, certifications, Guinness A2 record, Xi Jinping/Lee Hsien Loong demos
- https://news.qq.com/rain/a/20250923A082NR00 — Tencent News deep-dive: Deng Taihua's Huawei background (Kunpeng/Ascend), UESTC ties with Peng, "Huawei-system" framing, role split (Deng chairman/CEO; Peng president/CTO)
- https://www.therobotreport.com/agibot-rolls-out-10000th-humanoid-robot/ — 10,000-unit coverage (2026-03-31); ramp acceleration (1,000→5,000 in ~1 yr; 5,000→10,000 in 3 months)
- https://www.stcn.com/article/detail/3710561.html — Securities Times: 10,000th unit rolled off 2026-03-28 (1,000th 2025-01-06, 5,000th 2025-12-08); "全球最快" mass-production-record framing; A3 milestone unit per accompanying coverage
- https://www.agibot.com/article/231/detail/53.html — company announcement of 10,000-unit milestone; overseas deployment claims (company-reported)
- https://www.prnewswire.com/apac/news-releases/agibots-15-000th-robot-rolls-off-the-production-line-marking-a-new-milestone-in-embodied-ai-deployment-302812695.html — 15,000th robot (2026-06-28), a Genie G2 delivered to Longcheer
- https://www.prnewswire.com/news-releases/omdia-ranks-agibot-no1-worldwide-in-humanoid-robot-shipments-in-2025-302656788.html — Omdia: 5,168 units 2025, 39% share, #1
- https://www.caixinglobal.com/2026-01-24/unitree-defends-robot-sales-as-rival-claims-market-crown-102407436.html — Unitree–AgiBot shipment-crown dispute
- https://huacheng.gz-cmc.com/pages/2026/01/24/dc13913b1e7d436d8cfba1c64561dc92.html — IDC: AgiBot #1 across five mainstream deployment scenarios (2025)
- https://technode.com/2025/07/10/agibot-denies-backdoor-listing-via-swancor-advanced-materials-acquisition/ — Swancor ~63.62% for ~RMB 2.1B; backdoor-listing denial
- https://www.scmp.com/tech/big-tech/article/3317741/robot-maker-agibot-seeks-stake-shanghai-listed-firm-potential-back-door-listing-move — deal structure (智元恒岳/智元新创, RMB 7.78/share, transfer + tender)
- https://www.stcn.com/article/detail/3511830.html — Securities Times: Peng Zhihui takes the helm (chairman) of Swancor after board overhaul; stock's bull run
- https://chinabizinsider.com/agibot-completes-corporate-restructuring-signaling-imminent-ipo-push/ — LLC→joint-stock conversion (2025-11); Swancor board seats for AgiBot founders
- https://finance.yahoo.com/news/exclusive-chinese-robot-maker-agibot-092020928.html — Reuters exclusive: HK IPO planned for 2026; CICC/CITIC/Morgan Stanley sponsors
- https://news.futunn.com/en/post/63128069/backed-by-tencent-and-sequoia-china-agibot-a-chinese-unicorn — HK$40–50B target valuation reports; company dismissal
- https://m.bjnews.com.cn/detail/1742817864168874.html — Tencent-led round (2025-03), ~RMB 15B valuation context
- https://www.scmp.com/tech/tech-trends/article/3312455/chinese-robotics-star-agibot-adds-jdcom-investor-joining-tencent-big-tech-backer — JD.com 0.75% stake; investor roster incl. SAIC, BAIC, TCL
- https://roboticsandautomationnews.com/2025/08/04/agibot-secures-strategic-investment-from-lg-electronics-and-mirae-asset/93485/ — LG Electronics + Mirae Asset strategic investment (2025-08)
- https://capital.com/en-int/learn/ipo/agibot-ipo — aggregate >$725M raised across rounds (secondary, unverified)
- https://arxiv.org/abs/2503.06669 — AgiBot World Colosseo paper: >1M trajectories, 2,976 h, 217 tasks, 100 robots, 4,000 m² facility, +30% vs OXE, GO-1 ViLLA
- https://agibot-world.com/blog/go1 — GO-1 model card/blog (company primary)
- https://github.com/OpenDriveLab/AgiBot-World — open dataset/code (CC BY-NC-SA 4.0); IROS 2025 Best Paper finalist
- https://www.therobotreport.com/agibot-releases-go-2-foundation-model-embodied-ai/ — GO-2 release (2026-04-09), AI Week (2026-04-07–14), unified reasoning+action
- https://www.therobotreport.com/agibot-unveils-genie-envisioner-2-0-advance-world-models-scalable-simulators-embodied-ai/ — Genie Envisioner 2.0 (2026-04-10): interactive world simulator, reward modeling
- https://www.humanoidsdaily.com/news/modularizing-the-last-mile-agibot-unveils-genie-studio-agent-to-scale-robot-deployment — Genie Studio Agent zero-code deployment platform
- https://www.tmtpost.com/7957537.html — Deng "部署态元年" quote; Peng "卖机器人→交付结果" quote; Yao Maoqing GPT-3-progress-bar 20–30% by end-2026; overseas 30%→50% target; 觅蜂 10M-hour data goal
- https://m.chinaagv.com/news/detail/202603/35368.html — Peng at HEIS annual meeting: "共同探索…没有任何一家企业能独自给出正确答案" quote; 2026 deployment-era framing
- https://www.chnfund.com/article/ARb69ae31c-86bd-1241-8952-3a1e5ac3fc22 — chairman's 2025 sales guidance >RMB 1B; core data disclosure
- https://zhuanlan.zhihu.com/p/1967553187411100303 — revenue trajectory RMB 0.3M (2023) → 60M+ (2024) → >1B (2025) (secondary, company-derived)
- https://www.zhiyuan-robot.com/article/188/detail/101.html — 5,000th unit (2025-12-08); line breakdown A-series 1,742 / X-series 1,846 / G-series 1,412; X2 to Huang Xiaoming studio
- https://m.cls.cn/detail/2122481 — 2026 guidance "数万台" (tens of thousands); listed supply-chain partners
- https://interestingengineering.com/ai-robotics/china-agibot-robots-hit-99-percent-success-during-six-day-live-factory-demo — Longcheer Nanchang six-day livestream: 64,828 tasks, 99.99% success (company-reported), 17,625 tablets
- https://www.agibot.com/article/231/detail/83.html — company account of the six-day factory livestream
- https://pandaily.com/agi-bot-unveils-expedition-a3-humanoid-capable-of-high-difficulty-aerial-moves — A3 unveiling (2026-02), martial-arts capability
- https://humanoid.press/database/humanoid-press-database-agibot-a3/ — A3 specs: 173 cm / 55 kg / 10-h endurance; ~$45K price (secondary, unverified)
- https://m.thepaper.cn/newsDetail_forward_31296583 — Lens Technology: taking on AgiBot full-series humanoid business in 2026 (assembly + components)
- https://zhuanlan.zhihu.com/p/1931286524881799133 — Guojin Securities note: Lens X1 co-development/assembly, Fulin Precision reducers/joints, Joyson/Pusmart JV, dual-track production, Lingang plant ~300 units/month
- https://www.tmtpost.com/7526278.html — TMTPost: 宁波普智未来 JV founding (2025-04), first-phase line ~1,000 units/yr, ~RMB 200M (超2亿) Ningbo innovation-center investment
- https://zhuanlan.zhihu.com/p/1968431938021885173 — "capital sprawl": ~15 startup investments, ~17 JVs in a year (secondary tally, unverified)
- http://yuanchuang.caijing.com.cn/2025/1109/5124211.shtml — Caijing cover story: 1,000-unit order ~30% defect / unpaid claim (single source; link dead / 404 as of 2026-07 and claim not corroborated elsewhere — unverified)
- https://finance.sina.com.cn/roll/2025-07-08/doc-infeumnf5080280.shtml — Sina Finance: humanoid rental-rate collapse (G1 ~RMB 15K → 5–8K/day by mid-2025), second-hand dumping, commercialization squeeze
- https://www.humanoidsdaily.com/news/the-10-000-unit-threshold-agibot-accelerates-production-in-bid-for-global-dominance — 10,000th milestone unit identified as an Expedition A3; Peng quote on scaling
- https://www.chinadaily.com.cn/a/202508/01/WS688c1eb5a310c26fd717cec5.html — overseas foray strategy (2025-08)
- https://roboticsandautomationnews.com/2026/07/02/agibot-debuts-a3-humanoid-robot-in-europe-and-launches-uk-robot-as-a-service-model/103018/ — A3 Europe debut + UK RaaS (2026-07-02); Munich/Germany entry, Minth partnership; EUR 899/day rental
- https://www.bastillepost.com/global/article/5676393-agibot-signs-strategic-cooperation-agreement-with-singtel-enterprise — Singtel operator partnership, Singapore (2026-03)
- https://www.trendforce.com/presscenter/news/20260409-13007.html — 2026 forecast: China output +94%, Unitree+AgiBot ~80% of shipments
- https://chinaselectcommittee.house.gov/media/press-releases/moolenaar-obernolte-mcclellan-introduce-legislation-to-ban-dangerous-chinese-robots — GUARD Act: US legislative risk backdrop for Chinese humanoids
- https://english.news.cn/20260503/3616ad8aae584ea6a5501dbb0fd78111/c.html — Xinhua profile of Peng Zhihui; May Fourth Medal; deployment milestones (state media)
- https://autonews.gasgoo.com/articles/news/zhiyuan-robot-spins-off-dexterous-hand-business-humanoid-robots-trigger-a-division-of-labor-revolution-2013868661754662912 — OmniHand business spin-off (2026)
