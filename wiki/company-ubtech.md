---
title: "Company Deep Dive: UBTech (优必选)"
slug: company-ubtech
updated: 2026-07-05
confidence: verified
---
> UBTech Robotics (优必选, Shenzhen, founded 2012-03 by Zhou Jian 周剑) is the longest-running Chinese humanoid bet and the sector's first listed pure-play (HKEX 9880, 2023-12-29). Its arc runs from in-house servo actuators and Alpha toy robots (540 of them dancing at the 2016 CCTV Spring Festival Gala) through education/consumer robots to the Walker industrial humanoid line: Walker S2 entered mass production 2025-11, and UBTech delivered 1,079 full-size humanoids in 2025 — the first company past 1,000 *full-size* units in a year (AgiBot and Unitree shipped more units overall counting smaller models) — to BYD, Foxconn, Geely, FAW-VW, BAIC, SF Express and state data-collection centers, on >RMB 1.3B of 2025 Walker orders. On 2026-06-30 it pivoted a third leg into consumers: the UWORLD U1 "ultra-bionic" companion humanoid (from RMB 119,800; 13,361 launch orders, company-reported). The financial reality check: 2025 revenue RMB 2.0B (+53.3%) but a RMB 790M net loss (cumulative 2020–2025 losses ~RMB 5.8B), funded by ~HK$7.6B of post-IPO share placements plus a $1B Infini Capital facility. UBTech is the anti-[Unitree](company-unitree.md): loss-making but capital-rich, industrial-orders-first, and supply-chain-orchestrating ("chain master") rather than extreme vertical integration. See [Humanoids](humanoid-robots.md), [Landscape: China](landscape-china.md), [Investment](investment.md).

## Company at a glance (as of 2026-07)

| Field | Value |
|---|---|
| Founded | 2012-03, Shenzhen (R&D began 2008; Zhou Jian self-funded with ~RMB 20M of personal cash) |
| Founder/Chairman/CEO | Zhou Jian (周剑, Nanjing Forestry University materials class of '99); no controlling shareholder since acting-in-concert pact ended 2024-12-29 |
| Listing | HKEX 9880, listed 2023-12-29 at HK$90 (bottom of HK$86–116 range); raised ~HK$1.04B; day-one market cap ~HK$38B |
| Share price / cap | HK$108.90 close 2026-07-03 (+17.6% on the day; U1 orders + BofA target raise to HK$162); ~HK$54.7B (~$7.0B) market cap; 52-wk range HK$75.50–161; all-time peak HK$328 (2024-03, cap briefly >HK$140B) |
| 2025 revenue | RMB 2,001M (+53.3% YoY); humanoid segment RMB 820.6M (41.1% of revenue, +2,203.7% YoY) |
| 2025 profitability | Net loss RMB 789.8M (narrowed 31.9% from RMB 1,159.9M); gross margin 37.7% (+9 pp); still loss-making every year since founding disclosures began |
| 2025 volumes | 1,079 full-size humanoids delivered (first company >1,000 full-size/yr; company claims #1 globally in full-size revenue and volume); >6,000 units/yr annualized capacity claimed at end-2025 (company-reported) |
| Cash | ~RMB 4.89B cash & equivalents at end-2025 (single-source), after HK$3.06B net Dec-2025 placement; end-2024 was RMB 1.19B vs RMB 1.54B bank borrowings |
| Product lines | Walker S1/S2 industrial humanoids; Walker C commercial; UWORLD U1 consumer (2026-06); Tien Kung Xingzhe research humanoid (¥299K); Cruzr service robot; education (Alpha/Jimu/AlphaMini), logistics AMRs, consumer gadgets (mowers, pool robots, pet tech) |
| 2026 targets | ~5,000 humanoid deliveries (10× 2025's industrial base); Liuzhou+Shenzhen capacity 5K/yr → 10K by 2027; U1 output >10,000 units (company-reported) |

## Founding story — servos before humanoids

- **2008**: Zhou Jian, then a businessman, sees humanoid robots at a Japanese trade show and decides to build one; he later says he put "all the liquid cash in my bank account — RMB 20M" into the project and nearly went broke twice before launch (Chinese media profiles).
- **2012-03**: UBTech registered in Shenzhen after the team's core breakthrough — a **commercial servo actuator (伺服舵机) at ~1/10th the cost of imported Japanese/Korean/Swiss equivalents**, developed over ~4 years. Cheap in-house rotary actuation is the company's founding technology and remains its stated moat.
- **2012-H2**: first **Alpha 1** toy humanoid ships — 16 DoF, dances/boxes/kicks; becomes a trade-show staple.
- **2016-02**: **540 Alpha 1S robots dance in synchrony on the CCTV Spring Festival Gala** — the company's fame moment, nine years before Unitree's equivalent (see [Landscape: China](landscape-china.md)).
- **2015–2018 capital run**: Qiming-led ~$60M Series A (2015, iFlytek became a shareholder via transfer); by the 2018 Series C (~$820M, Tencent among leads) UBTech was reported at a ~$5B valuation — then the world's most valuable AI/robotics startup by some counts (single-source, unverified).
- **2023-12-29**: lists on HKEX main board as the **first humanoid-robot stock** ("Walker S struck the gong"); Tencent held ~6.3% pre-IPO. Over 760,000 robots (mostly education/consumer) sold cumulatively 2020–H1 2023 per prospectus.
- Zhou Jian is a co-founder of the state-backed Beijing Humanoid Robot Innovation Center (X-Humanoid, 2023-11, with Xiaomi Robotics and Beijing Jingcheng) — see [Organizations](organizations.md), [Key people](key-people.md).

## 技术路线 — tech route & architecture

- **Full-stack, actuator-up**: UBTech designs its own servo joints (from toy-grade to humanoid torque classes), dexterous hands (4th-gen, 11 DoF each on Walker S2), and motion control; it claims the world's largest portfolio of effective humanoid-robot patents (company claim, unverified).
- **Walker S2 platform** (unveiled 2025-07; mass production 2025-11): 1.76 m, 43–73 kg depending on configuration, **52 DoF**, 2 m/s walk, 15 kg lift, ±162° waist rotation for ground-level picking; split-brain compute — Intel i7-1185G7 for hard-real-time control + NVIDIA Jetson AGX Orin 64 GB (275 TOPS) for perception/policy (see [Hardware](hardware.md)).
- **Signature engineering bet: autonomous hot-swap batteries.** Dual 48 V packs (~2 h each); the robot swaps its own battery in ~3 min without powering down — designed for 24/7 factory shifts. This is UBTech's clearest hardware differentiation vs peers, whose humanoids dock or stop to charge.
- **Software bet: swarm over solo.** Where Figure bets on one end-to-end VLA (Helix) and Unitree on low-cost single-robot autonomy, UBTech's frame is **BrainNet 2.0** — a dual-loop framework in which a "super brain" does task-level reasoning/dispatch and "intelligent sub-brains" on each robot execute skills, letting fleets of Walker S2s (and wheeled Cruzr units) share maps and coordinate — plus **Co-Agent**, billed as the first agent framework purpose-built for humanoid production lines (intention understanding → task planning → tool use → autonomous error handling). First multi-humanoid collaborative-training demos ran at Zeekr's 5G factory (2025, company demo).
- Rationale: UBTech's customers buy *deployments* (dozens of robots + integration), not single units — so orchestration, battery logistics, and station-level integration matter more than benchmark-topping single-robot dexterity. The skeptic read: swarm framing also flatters robots that are individually "at most half" as productive as a human worker (Merics, 2026-03; UBTech targets 80% by 2027).
- Positioning vs rivals: heavier, costlier, more integrated than [Unitree](company-unitree.md)'s cost-down machines; more factory-embedded than US software-first labs; closest Western analogue in go-to-market is Agility's fleet-orchestration pitch ([Company: Agility](company-agility.md)).

## The bet — Zhou Jian's thesis

- Founder-level conviction is total: **"为了造出真正的人形机器人，我愿意赌上一切"** ("To build a true humanoid robot, I'm willing to bet everything") — the headline LatePost put on its ~7-hour two-session Zhou interview (conducted 2025-04 and 2025-12, published 2026-01-25; editorial headline rather than a verbatim in-text quote, but it condenses his account of staking his house, cars and savings on the company).
- **Three-step roadmap (三步走), stated consistently since listing**: industrial manufacturing first → commercial services second → family/home companionship third. As of 2025-12, verbatim: "人形机器人不是用来表演的，是要进工厂、干实事、被客户真金白银买单的" ("Humanoids are not for performing — they must go into factories, do real work, and be paid for by customers with real money"; the 21jingji interview ran under the headline "相比表演秀，人形机器人更要进工厂干实事") — an explicit jab at acrobatics-led rivals.
- Focus stations: **handling, sorting, quality inspection** — chosen for high labor turnover, repetitiveness, and semi-structured layouts.
- **The consumer turn (2026-06-30)**: with the UWORLD U1 launch UBTech declared a ten-year **"人机共生" (human–robot symbiosis)** strategy and Zhou reframed the timeline: the humanoid **"iPhone moment" will start with emotional companionship** — "情感陪伴已成为当下的刚需" ("emotional companionship has become a hard need of the moment") — "预计一到三年内，针对特定人群的'iPhone时刻'就会到来" (arriving within 1–3 years for specific groups: 失独 elderly who lost an only child, empty-nest youth, the autism community), while general home robots remain 5–10 years out. He now splits effort ~50% industrial/commercial, ~50% home (interview, 2026-07-01).
- Zhou's stated moats for U1: emotion-interaction models, ultra-realistic bionic manufacturing ("no precedent in manufacturing history" — custom faces/skin need new production lines), and an ecosystem/subscription layer on top of hardware.
- Skeptic note: UBTech has re-picked its "killer app" several times (education → retail service → industrial → companionship); each pivot tracked the era's funding narrative. The company would counter that all run on the same actuator/full-stack base.

## Products & deployments — with real numbers

### Product lineage

| Year | Product | Notes |
|---|---|---|
| 2012 | Alpha 1 | 16-DoF toy humanoid; first product on in-house servos |
| 2016 | Alpha 1S Gala swarm | 540 synchronized robots, CCTV Spring Festival Gala |
| 2016–19 | Jimu kits, Alpha Mini, Cruzr | STEM kits (sold in Apple Stores), desktop humanoid, wheeled service robot; Disney-licensed Stormtrooper toy robot |
| 2018–19 | Walker (CES debut, then full-body) | First Chinese full-size bipedal home-concept humanoid |
| 2021 | Walker X | 41 DoF service demo platform |
| 2023 | Walker S | Industrial pivot; factory pilots begin |
| 2024-10 | Walker S1 | Pilots at BYD, Foxconn, Zeekr; only **10 humanoids delivered in all of 2024** (RMB 35.6M revenue) |
| 2025-03 | Tien Kung Xingzhe (天工行者) | ¥299K (~$41K) full-size research/education humanoid with X-Humanoid; 1.7 m, 10 km/h; deliveries from Q2 2025 |
| 2025-07 | Walker S2 | 52 DoF, 3-min battery self-swap; mass production from 2025-11 |
| 2026-06-30 | UWORLD U1 series | Consumer "ultra-bionic" companions — see below |
| 2026 (planned) | Walker S3 | Next industrial gen; H2 2026 volume expected (analyst notes, unverified) |

### Industrial Walker deployments and order book

- **2025 deliveries: 1,079 full-size humanoids** (+35,866.7% YoY; includes Walker S line plus Tien Kung Xingzhe research units — note the official growth rate implies a 2024 *full-size* base of just 3 units, vs the 10 humanoids of all types media reported for 2024); UBTech's stated 2025 target of 500+ *industrial* units was met (company-reported); Omdia credits UBTech with ~1,000 units for 2025, #3 globally ([State of the art](state-of-the-art.md)).
- **2025 Walker-series orders >RMB 1.3B** (excluding Tien Kung Xingzhe and small AI Wukong units): includes RMB 250M single order (2025-09), RMB 159M Zigong data-collection center (early Nov), RMB 264M Fangchenggang data-collection/testing-center win (2025-11-21, then-cumulative ¥1.1B), RMB 143M Jiujiang data-collection/training-center win (2025-11-28), which pushed the tally past ¥1.3B (~$185M). The oft-quoted ">RMB 800M" was the mass-production-announcement tally (2025-11-17); the ¥1.3B mark was thus crossed by end-Nov, not just at year-end.
- **Customer roster** (auto-heavy): BYD, Foxconn, Geely/Zeekr, FAW-Volkswagen Qingdao, Audi FAW, BAIC New Energy, Dongfeng Liuzhou (20 units, ~RMB 50M contract 2025-04, brokered by the Liuzhou government), SF Express; 2026 agreements with **Airbus** (Walker S2 purchase for aircraft assembly — Airbus itself calls it an "early concept testing phase") and **Texas Instruments** (purchased Walker S2s for its semiconductor plants, scale undisclosed) per Merics — early-stage adoptions, not fleet deployments.
- **State demand matters**: four 2025 public-sector orders were ≥RMB 100M each (Liuzhou, Zigong, Fangchenggang, Jiujiang — mostly humanoid data-collection/training centers); UBTech had sold ~RMB 566M of humanoids to three provincial data centers (see [Data foundry](data-foundry.md)). Skeptics note much "industrial" revenue is actually government-adjacent training-center procurement, not factory labor.
- Efficiency reality: Walker S2 robots are **"at most half as efficient as human workers"** (Merics, 2026-03); UBTech targets 80% of human productivity by 2027.
- 2026 order book at year-start: ~RMB 1.0–1.2B in hand, ~2,500–3,000 units, ~70% S2 / 30% S3 (retail-analyst estimate, unverified).

### UWORLD U1 consumer launch (2026-06-30, Shenzhen)

- Three models: **U1 Lite** semi-torso (RMB 119,800), **U1 Pro** full-body (RMB 169,800), **U1 Ultra** high-dynamic full-body with lifelike silicone skin (RMB 990,000 male / 880,000 female presets); marketed for companionship, eldercare, reception — explicitly *not* chores ("won't do housework, will say it loves you," as Chinese tech media put it). Custom likeness/"replica" options are part of the long-term pitch (TechRadar).
- **13,361 cumulative orders claimed at launch** (company-reported, all channels since JD.com pre-orders opened 2026-06-02); TechNode independently reports ~11,000+ secured. First batch ships 2026-09-16; 2026 mass-production target >10,000 units, plus a 2027 target of **50,000-unit scale production capability** stated by Zhou at the launch event (company-reported) — though in his 2026-07-01 21jingji interview he declined to commit to a 2027 *delivery* target ("作为上市公司，现在我没法预测明年的目标").
- Strategic read: at RMB 119,800 the U1 undercuts nothing (Unitree R1 is ~RMB 30–40K) but sells emotion and realism, not locomotion — a deliberate category swerve away from the price war. Order-to-delivery conversion is unproven; treat launch tallies as refundable-deposit-grade until H1 2027 results.

### Legacy businesses (the revenue that kept the lights on)

- **Education robots & solutions**: Alpha/Jimu/AlphaMini + smart-campus curricula; the largest segment for most of company history (38.6% of H1 2025 revenue, ~RMB 240M).
- **Consumer robots & hardware**: 2024 revenue RMB 477M (+88.1%) — lawnmower M10, pool robot PC10, smart litter box C20, pet grooming vacuum, feeder F10, vacuum V10 — largely export-oriented catalog hardware (41.9% of H1 2025 revenue, RMB 260.1M).
- **Logistics robots** (wheeled AMRs/forklifts): ~9% of H1 2025 revenue (~RMB 56M).
- These lines fund and de-risk the humanoid program but are low-moat, competitive categories; the humanoid segment overtook them all only in 2025.

## Business model & unit economics

| Year | Revenue | Net loss | Notes |
|---|---|---|---|
| 2020 | ~RMB 740M | −RMB 707M | education-led |
| 2021 | RMB 817M | −RMB 918M | |
| 2022 | RMB 1,008M | −RMB 987M | |
| 2023 | RMB 1,056M | −RMB 1,265M | IPO year |
| 2024 | RMB 1,305M (+23.7%) | −RMB 1,160M | only 10 humanoids delivered |
| 2025 | RMB 2,001M (+53.3%) | −RMB 790M (−31.9%) | humanoids 41.1% of revenue; GM 37.7% |

- **Cumulative 2020–2025 net losses ~RMB 5.8B** — against ~RMB 7.1B revenue over the same span. Chinese financial media: "5 years, RMB 5B lost."
- **Humanoids are (gross-)profitable**: 2025 humanoid segment gross margin ~54.6% (~RMB 448M gross profit on RMB 820.6M, +1,568% YoY, per Chinese annual-report coverage; company total gross profit RMB 754M, +101.6%) — far above the legacy hardware lines; this is what lifted blended GM from 28.7% to 37.7%. Implied 2025 revenue per humanoid delivered ≈ RMB 760K (~$105K), blending six-figure-USD Walker S2 solutions with ¥299K research units.
- **Below the gross line the model still burns**: 2025 R&D RMB 508M (25.4% of revenue), heavy selling/admin costs; H1 2025 operating cash flow −RMB 370M. Revenue is extremely **Q4-back-loaded** — H1 2025 was only RMB 621M of the year's RMB 2,001M, with the humanoid ramp almost entirely in Nov–Dec — so annual "growth" leans on year-end recognition of state-linked orders (skeptic flag).
- **Cost-down plan**: manufacturing cost cuts of 20–30%/yr at scale; unit cost below $20K by 2030 (CBO Michael Tam, company-reported). 2026 output guided to ~5,000 units (~10× the 2025 industrial base).
- **Funding machine (the real business model to date)**: IPO HK$1.04B (2023-12) + **six placements in two years** (2024-08, 2024-10, 2024-11, 2025-02, 2025-07 net HK$2.41B, 2025-12 net HK$3.06B) ≈ **HK$7.6B cumulative**; plus a **$1B strategic financing facility from Infini Capital (2025-08-31**, deployable via placements/CBs/cash rights, tied to Middle East humanoid production plans). End-2025 cash ~RMB 4.89B (single-source). Listed-company access to capital is UBTech's structural answer to Unitree's profitability.
- **A-share maneuver**: 2025-12-24, UBTech agreed to pay ~**RMB 1.665B for up to 43% of Shenzhen-listed auto-parts maker Fenglong Co. (锋龙股份)** at ¥17.72/share (29.99% block + 13.02% partial tender); Zhou Jian becomes its actual controller. UBTech pledged no shell-restructuring/relisting via Fenglong within 36 months, but the market read it as an "H+A" beachhead and supply-chain integration platform; ~75% of the Dec-2025 placement is earmarked for upstream/downstream investment and JVs.

## Strengths / weaknesses vs peers

| Strengths | Weaknesses |
|---|---|
| First-mover listed status: 2.5 years of audited humanoid disclosures; deepest public capital access in the sector (HK$7.6B raised post-IPO) | Never profitable; ~RMB 5.8B cumulative losses; repeated dilution (six placements in 24 months) |
| Largest verified industrial order book (>RMB 1.3B 2025) and broadest blue-chip factory roster (BYD, Foxconn, Geely, FAW-VW, SF, TI, Airbus pilots) | Meaningful share of "industrial" orders are government data-collection centers, not recurring factory labor; Q4-loaded revenue |
| Only vendor shipping autonomous battery-hot-swap humanoids — a genuine 24/7-operations differentiator | Walker S2 at most ~50% of human efficiency (2026-03, Merics); productivity economics unproven |
| Full-stack IP from founding servo tech; #1 claimed humanoid patent portfolio; 1,079 units delivered = most full-size humanoids fielded in 2025 | Price/agility pressure from [Unitree](company-unitree.md) (60% gross margin, profitable, ~$5–30K products) and AgiBot volume; UBTech ASPs 10–30× higher |
| Shenzhen/PRD supply-chain depth + two owned plants + chain-master war chest | History of hype cycles (CES Walker demos, education pivot, retail robots) with slow conversions; 2024 delivered just 10 humanoids |
| Three-market hedge (industrial + consumer companion + education/consumer legacy cash lines) | Governance overhang: no controlling shareholder since 2024-12; Tencent trimmed HK$1.03B and Minsheng exited around the Jan-2025 49%-in-4-days crash |

- **The skeptic case in one line**: UBTech is a capital-markets-subsidized systems integrator whose humanoid margins depend on state-adjacent orders — and the U1's 13k "orders" must survive contact with September deliveries.
- **The bull case in one line**: the only company with >1,000 full-size humanoids actually fielded in one year, gross-margin-positive on them, with the cash, plants, and customer list to industrialize the category before rivals escape the lab.

## Manufacturing & supply-chain posture (the ODM lens)

- **Owned final assembly, orchestrated components** — the inverse of Unitree's make-everything model (purchased components ~14–18% of Unitree's cost; UBTech buys far more of its BOM externally, exact share undisclosed).
- **Two humanoid plants**: Shenzhen (HQ) and **Liuzhou, Guangxi** — the Liuzhou site crossed its **1,000th Walker S2 by end-December 2025** and anchors the 5,000-unit/yr 2026 capacity plan (10,000 by 2027). Liuzhou siting follows the customer: the Dongfeng Liuzhou order was explicitly government-brokered, and Liuzhou placed one of the ≥¥100M public orders — plant-for-orders reciprocity typical of Chinese industrial policy.
- **Kept in-house** (design + manufacture): servo joint actuators (founding IP), 4th-gen dexterous hands, whole-machine integration, BrainNet/Co-Agent software.
- **Sourced externally** (named design-wins per Chinese supply-chain coverage; treat individual names as industry-reported, not company-confirmed): harmonic reducers — **Leader Drive (绿的谐波)**; coreless/precision micro-motors for finger joints — **Moons' (鸣志电器)**; 3D vision — **Orbbec (奥比中光**, >70% share of China service-robot 3D vision, on Walker S/X); compute — Intel + NVIDIA (TI, a Walker S2 buyer, is also a plausible component supplier — inference, unverified). Battery packs and structural parts from the PRD ecosystem (unspecified).
- **Consumer lines are classic ODM/EMS territory**: mowers, pool robots, and pet devices are catalog products almost certainly built with contract manufacturers (inference, unverified) — and the U1's silicone-skin "ultra-realistic manufacturing... no precedent" line signals new specialized process partners will be needed at 10K+/yr volumes.
- **"Chain-master" (链主) strategy, funded**: ~75% of the HK$3.06B Dec-2025 placement is explicitly for investing in/absorbing upstream-downstream companies or forming JVs; the RMB 1.665B Fenglong acquisition gives UBTech an A-share-listed precision-manufacturing platform (auto parts) it controls. Expect UBTech to become an acquirer/anchor investor across actuator, sensor, and skin/materials suppliers through 2026–27.
- **Why this matters to ODMs**: UBTech is the highest-volume *externally-sourcing* humanoid OEM — every capacity step (5K→10K/yr industrial + 10K→50K/yr U1) flows to merchant suppliers rather than in-house lines, making it the best single customer-signal for the humanoid component ecosystem ([Hardware](hardware.md), [Landscape: China](landscape-china.md)).

## What to watch (as of 2026-07)

- **U1 delivery conversion** from mid-September 2026: how many of the 13,361 claimed orders ship and stick (returns/refunds), and whether the subscription/ecosystem layer materializes.
- **2026 delivery total vs the ~5,000 guidance** (2025: 1,079) and Walker S3 launch/pricing.
- H1 2026 interim results (due ~2026-08/09): humanoid gross margin durability, loss trajectory, cash burn against the ~RMB 4.9B pile.
- Fenglong integration and any further A-share moves ("H+A" structure); deployment of the placement war chest into component acquisitions.
- Repeat orders from BYD/Foxconn/Geely (the proof of factory ROI) vs continued reliance on data-center/state orders; Airbus concept-test and TI semiconductor-plant deployment outcomes.
- Competitive squeeze: Unitree's industrial push downmarket and AgiBot's volume — whether UBTech's six-figure ASPs compress before its 20–30%/yr cost-down lands.

## Sources

- https://www.163.com/dy/article/L00VH4QK05390H81.html — founding history: 2008 Japan expo trigger, RMB 20M self-funding, 2012 servo breakthrough at ~1/10 import cost, Alpha 1 (16 DoF)
- https://dag.njfu.edu.cn/2024/0913/c1744a15792/page.htm — Zhou Jian NJFU materials class-of-'99 alumnus interview; founding narrative
- https://www.siat.ac.cn/siatxww/mtbd/202412/t20241220_7506422.html — 540 Alpha 1S robots at 2016 CCTV Spring Festival Gala (Southern Daily reprint)
- https://zhuanlan.zhihu.com/p/675213921 — funding history incl. 2015 Qiming-led A round, iFlytek shareholding
- https://www.scmp.com/business/article/3246584/ubtech-maker-stormtrooper-robots-gains-hong-kong-trading-debut-after-pricing-final-ipo-2023-lower — IPO 2023-12-29: HK$90 pricing, HK$1B raise, HK$38B day-one cap, Tencent 6.3%, 760K cumulative robots sold
- https://www.prnewswire.com/apac/news-releases/as-walker-s-strikes-the-gong-ubtech-robotics-becomes-the-first-humanoid-robot-company-listed-on-the-main-board-of-the-hkex-302027943.html — official listing PR
- https://autonews.gasgoo.com/articles/icv/ubtech-2025-report-card-revenue-from-full-size-humanoid-robots-grows-over-22-fold-2039900685372407808 — 2025 annual results: RMB 2.001B revenue, RMB 820.6M humanoid segment (+2,203.7%), 1,079 units, loss RMB 789.8M, GM 37.7%
- https://www.humanoidsdaily.com/news/ubtech-s-2025-financials-humanoids-leap-to-center-stage-as-losses-narrow — 2025 financials detail: 2024 loss RMB 1,159.9M comparison, >6,000 annualized capacity, 5,000-unit 2026 target, 20–30%/yr cost-down, sub-$20K by 2030, TI deployment
- https://www.163.com/dy/article/KPFKA02L05118K7K.html — 2025 annual report coverage: end-2025 cash & equivalents ~RMB 4.888B, R&D RMB 508M (25.4% of revenue)
- https://news.qq.com/rain/a/20260403A06IUD00 — FY2025 annual-report coverage (2026-04-03): humanoid segment gross margin "高达约54.6%", ~¥760K average revenue per unit, 1,079 units
- https://finance.sina.com.cn/roll/2026-04-03/doc-inhtfvnv8689184.shtml — FY2025 年报点评: humanoid segment ¥821M (+2,204%), segment gross profit ¥448M (+1,568.1%, GM 54.6%); total gross profit ¥754M (+101.55%)
- https://cj.sina.com.cn/articles/view/1747383115/6826f34b02002dib0 — H1 2025 segment mix on RMB 621M revenue: education RMB 239.8M (38.6%), consumer RMB 260.1M (41.9%), logistics RMB 56.2M (9.1%), custom RMB 63.8M (10.3%)
- https://en.tmtpost.com/post/7680109 — H1 2025: +27.5% revenue, net loss RMB 439M (−17.2%), operating cash flow −RMB 370M; $1B Infini Capital strategic financing
- https://www.therobotreport.com/ubtech-secures-1b-financing-middle-east-humanoid-production/ — Infini Capital $1B facility (2025-08-31), Middle East production angle
- https://mp.ofweek.com/finance/a856714043587 — "5 years RMB 5B losses": 2020–2024 loss series (7.07/9.18/9.87/12.65/11.6 亿)
- https://www.guancha.cn/economy/2025_04_04_770926.shtml — 2024 reality check: 10 humanoids delivered in 2024, RMB 35.6M humanoid revenue
- https://stcn.com/article/detail/1625504.html — 2024 annual results: RMB 1.305B revenue (+23.7%); Walker S in auto-factory training
- https://www.stcn.com/article/detail/1632141.html — 2025 plan: ~1,000 humanoids produced, 500+ delivered target
- https://www.prnewswire.com/news-releases/ubtech-humanoid-robot-walker-s2-begins-mass-production-and-delivery-with-orders-exceeding-800-million-yuan-302616924.html — Walker S2 mass production (2025-11-17), >RMB 800M orders, customer list, 5K/10K capacity plan
- https://www.ubtrobot.com/en/humanoid/products/walker-s2 — official Walker S2 page: 52 DoF, hot-swap battery, specs
- https://blog.robozaps.com/b/ubtech-walker-s-review — Walker S2 aggregate specs: 1.76 m / 43–73 kg, 2 m/s, 15 kg lift, i7-1185G7 + Jetson AGX Orin 64 GB, BrainNet 2.0 / Co-Agent descriptions (aggregator)
- https://interestingengineering.com/ai-robotics/china-ubtech-builds-1000-humanoid-robots — (2025-12-30) 1,000th Walker S2 produced at Liuzhou; >500 units delivered and operational; Shenzhen + Liuzhou plants
- https://finance.yahoo.com/news/ubtechs-2026-humanoid-robot-output-093000689.html — SCMP: 2026 output to grow ~10-fold on scale economics (CBO comments)
- https://merics.org/en/comment/ubtech-humanoid-robots-future-manufacturing — (2026-03-04) Walker S2 "at most half as efficient as human workers", 80%-by-2027 target; Airbus 2026 purchase agreement for aircraft assembly ("early concept testing phase" per Airbus); TI purchased Walker S2s for semiconductor plants
- https://www.pconline.com.cn/zhizao/2026/20262672.html — (2025-11-28) Jiujiang RMB 143M; 2025 Walker orders "已突破13亿元" (>RMB 1.3B by end-Nov)
- https://www.yicai.com/news/102932034.html — Jiujiang ¥143M humanoid data-collection & training-center bid win (Walker S2); cumulative 2025 Walker orders ¥1.3B; Fangchenggang ¥264M (2025-11-21), Zigong ¥159M wins
- https://stcn.com/article/detail/3510555.html — RMB 264M order (2025-11-25), then-cumulative ¥1.1B 2025 orders, excl. Tien Kung Xingzhe / AI Wukong
- https://m.mp.oeeee.com/a/BAAFRD0000202504271078930.html — Dongfeng Liuzhou purchase contract (~RMB 50M, 20 units, 2025-04); prepayment received
- https://m.mp.oeeee.com/a/BAAFRD0000202508121111385.html — 500-unit 2025 delivery target; four ≥¥100M public orders (Liuzhou, Zigong, Fangchenggang, Jiujiang); focus on handling/sorting/inspection
- https://caifuhao.eastmoney.com/news/20260202231034097642180 — 2026 order book ~¥1.0–1.2B / 2,500–3,000 units, S2/S3 mix (retail-analyst estimate, unverified)
- https://www.scmp.com/tech/tech-trends/article/3302233/chinas-ubtech-debuts-us41000-humanoid-robot-race-build-cheaper-machines — Tien Kung Xingzhe ¥299K (~$41K), 1.7 m, 10 km/h, X-Humanoid collaboration, Q2 2025 delivery
- https://www.prnewswire.com/news-releases/ubtech-launches-uworld-u1-the-worlds-first-full-size-mass-produced-ultra-bionic-humanoid-robot-302815272.html — U1 launch PR (2026-06-30): three models, from RMB 119,800, 13,361 orders, mid-Sept deliveries
- https://technode.com/2026/07/01/ubtech-unveils-consumer-humanoid-robot-u1-says-orders-secure-11000-ahead-of-first-deliveries/ — independent U1 order count (~11,000+)
- https://finance.biggo.com/news/7e70bcd8-1dc9-422f-8cf1-3ff54e59764a — U1 pricing tiers: Lite ¥119,800 / Pro ¥169,800 / Ultra ¥990K
- https://www.sohu.com/a/1044889739_122219432 — U1 Ultra male ¥990K vs female ¥880K (¥110K gap; male preset 183 cm/42 kg vs female 168 cm/35.2 kg, both 88 joints)
- https://www.techradar.com/ai-platforms-assistants/ubtech-just-introduced-its-first-full-size-ultra-bionic-humanoid-robot-but-what-it-really-wants-to-do-is-make-robot-replicas-of-loved-ones-thats-a-hard-no — U1 replica-of-loved-ones ambition, companionship positioning
- https://m.21jingji.com/article/20260701/herald/c1acd8311c7d53441e7df27388e4445c.html — Zhou Jian interview (2026-07-01): "情感陪伴已成为当下的刚需" verbatim; "预计一到三年内，针对特定人群的'iPhone时刻'就会到来" (失独老人/空巢青年/孤独症群体); 50/50 industrial-vs-home effort split; declined to state a 2027 delivery target
- https://www.chnfund.com/article/AR8c5ff2c9-0e4f-3b1c-e5c3-3a222fa719ad — U1 launch-event coverage: Zhou — "U1系列今年量产规模预计达1万台"; "2027年的目标是实现5万台的规模化生产能力"; ~13K pre-orders
- https://www.21jingji.com/article/20251230/herald/b0276617203a86aca6b23944b5b45b46.html — Zhou Jian interview (2025-12-30): factories over performance shows; three-step strategy
- https://news.qq.com/rain/a/20260125A04UWK00 — LatePost long-form Zhou interview repost (2026-01-25; sessions 2025-04 & 2025-12), headlined "为了造出真正的人形机器人，我愿意赌上一切" (headline, not in-text verbatim)
- https://www.163.com/dy/article/L0MQK2A0053469RG.html — "人机共生" decade strategy at U1 launch; orders >13K
- https://www.cs.com.cn/gppd/ggzx/202507/t20250722_6503193.html — fifth placement (2025-07, net ~HK$2.41B); five placements within a year
- https://finance.sina.com.cn/stock/marketresearch/2025-12-25/doc-inhcymnr9123856.shtml — cumulative post-IPO placements ~HK$7.6B across six rounds; Dec-2025 placement HK$3.056B net; 3.5-yr losses RMB 3.85B framing; Fenglong shell-purchase critique
- https://m.gelonghui.com/p/3264974 — Dec-2025 HK$3.1B placement: ~75% earmarked for supply-chain (upstream/downstream) investment and JVs; "链主" (chain-master) positioning
- https://www.chinaventure.com.cn/news/114-20251226-389512.html — Fenglong Co. acquisition: RMB 1.665B for up to 43% at ¥17.72/share; structure (29.99% transfer + 13.02% tender); Zhou Jian becomes actual controller
- https://www.chnfund.com/article/ARba7645c9-a7e0-3f4d-e089-3a1e76fd7b08 — UBTech statement: no backdoor-listing restructuring via Fenglong within 36 months
- https://m.rccaijing.com/news-7282664928317208571.html — acting-in-concert agreement terminated 2024-12-29; no controlling shareholder thereafter
- https://news.qq.com/rain/a/20250110A05X7900 — Tencent's two January-2025 selldowns totaling ~HK$1.03B; Minsheng Capital full exit (2024-12-30)
- https://finance.sina.com.cn/stock/relnews/hk/2025-01-07/doc-ineecfif8242775.shtml — executive-director lock-up pledges after the early-2025 share crash
- https://finance.sina.com.cn/jjxw/2025-01-10/doc-ineenpix2323907.shtml — Jan-2025 ~50% drawdown coverage ("崩盘，暴跌50%")
- https://stockanalysis.com/quote/hkg/9880/ — close HK$108.90 on 2026-07-03 (+17.6% on the day), market cap HK$54.73B, 52-wk range 75.50–161
- https://caifuhao.eastmoney.com/news/20251224233123004329110 — Walker S2 A-share supply-chain map: Leader Drive harmonic reducers, Moons' micro-motors (finger joints), Orbbec 3D vision (industry-reported)
- https://www.icloudnews.net/a/75639.html — Orbbec as 3D-vision supplier to Walker S/X; >70% China service-robot 3D-vision share
- https://36kr.com/p/3115288957128192 — UBTech consumer lawnmower line at CES vs Segway-Ninebot/Dreame (consumer catalog context)
- https://m.chinabgao.com/info/1259131.html — 2024 consumer segment RMB 477M (+88.1%); product list (litter box C20, mower M10, pool PC10 etc.)
- https://eu.36kr.com/en/p/3780412419502851 — Unitree-profitable vs UBTech-loss-making divergence framing (RMB 790M 2025 loss)
