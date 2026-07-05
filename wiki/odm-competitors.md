---
title: "ODM / EMS / Module-Maker Competitive Landscape in Physical AI"
slug: odm-competitors
updated: 2026-07-05
confidence: verified
---
> The deep competitor companion to [ODM Opportunity Map](odm-opportunity.md): who among the contract-manufacturing and module-making world has actually *committed* to Physical AI, ranked by hardness of commitment (own-brand robot > JV/plant > investment > design-win > pilot > announcement > nothing). As of 2026-07 the honest picture: **almost nobody has a shipping own-brand humanoid, but the design-in race is real and dated.** The steel-in-the-ground leaders are Chinese A-share ODMs winning assembly of domestic champions — **Lens Technology (蓝思科技)** JV-plus-assembling AgiBot's full lineup, **Longcheer (龙旗科技)** running AgiBot 精灵 G2 on a live 3C production line (~1,000-unit framework order, 15,000th AgiBot unit delivered) — plus **Luxshare (立讯精密)** building its *own* robot (channel-conflict risk). The Taiwan EMS giants play the arms-dealer/investor hand: **Foxconn** leads Agility's ~$200M+ PIPE and manufactures for UBTech/Robust.AI/Kawasaki without an own-brand body; **Quanta/Techman** has a not-yet-shipped wheeled humanoid (TM Xplore I). Module/compute makers (**Quectel 移远, Fibocom 广和通, MeiG 美格, Thundercomm 创通**) sell the cross-form-factor "brain + connectivity + positioning" that every robot needs regardless of who wins. For a module maker like Quectel, this map says: rivals are *strong* in final-assembly design-ins (Foxconn, Lens, Longcheer own those relationships) but *weak/absent* in the compute-module socket where Quectel already ships — the defensible ground is arms-dealing, not own-brand robots. Sibling context: [ODM Opportunity](odm-opportunity.md), [Quectel pitch](../pitch/quectel.md), [AgiBot](company-agibot.md), [Agility](company-agility.md), [Hardware](hardware.md), [Landscape: China](landscape-china.md).

Scope note: written for an ODM/module-industry analyst (Quectel-style module maker sizing rivals). This page goes *deep on competitors*; the market-sizing, value-chain-opening map, and strategic-options matrix live in [ODM Opportunity](odm-opportunity.md) — cross-referenced, not repeated. Two mislabels that circulate in industry channels are corrected here and must not be reintroduced: (a) the ¥124M China Mobile humanoid tender (2025-07) was won by **AgiBot (¥78M) + Unitree (¥46M)**, *not* Luxshare; (b) the AgiBot listing vehicle **上纬新材 (Shangwei/Swancor)** is *not* the PC/server ODM **Wistron (纬创)** — different companies, similar romanization.

Source-quality tags: `(primary)` company/regulator disclosure; `(secondary)` reputable press; `(single-source)` one outlet only; `(unverified)` uncorroborated; `(company-reported)` self-asserted claim.

## 1. Commitment-ranked scoreboard (as of 2026-07)

Commitment ladder (hardest → softest): **own-brand robot > JV/plant-scale > equity investment > design-win/supply > pilot > announcement > none-found**. "最硬的一个动作" = the single hardest dated move on record. All rows sourced in [§Sources](#sources).

| 公司 | 类型 | 承诺度 | 最硬的一个动作 (dated) | 证据 |
|---|---|---|---|---|
| **Foxconn / Hon Hai (富士康/鸿海, incl. 工业富联 FII)** | EMS | design-win/supply + invest (no own brand) | Led **>$200M PIPE** in Agility's $2.5B SPAC (2026-06-24); manufactures Robust.AI Carter (2025-05-15); UBTech Walker S1 trials on own lines | `primary` |
| **Lens Technology (蓝思科技)** | EMS/components | **JV + plant-scale** | JV *Hunan Zhiqi Future (湖南智启未来)* w/ AgiBot (2025-04, Lens 70%) + assembly of **AgiBot's full 2025 humanoid lineup** (2025-08) | `primary`/`secondary` |
| **Longcheer (龙旗科技)** | ODM | **plant-scale customer + framework order** | ~¥several-hundred-M framework order for **~1,000 AgiBot 精灵 G2**; 15,000th AgiBot unit delivered; 8-hr live line demo Nanchang (2026-04-14) | `secondary` |
| **Luxshare Precision (立讯精密)** | ODM/EMS | **own-brand robot** (+ components) | Guided **~3,000 humanoid units shipped 2025, all external** (company-reported, 2025-11); "Manufacturing 2.0" line early 2026 | `company-reported` |
| **Quanta / Techman (广达/达明), incl. QCT** | ODM/module | own-brand robot (pre-production) | Wheeled humanoid **TM Xplore I** shown NVIDIA GTC 2026 (2026-03-18); mass-prod targeted 2H 2026 | `primary` |
| **Huaqin (华勤技术)** | ODM | pilot + own-brand (in-house) | Gen-1 humanoid tested; **wheeled robots batch-delivery targeted June 2026** into own plants; in-house actuators/control boards | `secondary`/`company-reported` |
| **BYD Electronics (比亚迪电子)** | EMS | pilot (group-level, not BYDE) | UBTech Walker S1 pilots in **BYD** car plants; BYDE entity discloses only "some layout" | `secondary` |
| **Pegatron (和硕)** | ODM | announcement / components-first | 5-yr robotics BU; "Aria" service robot + robot dog (COMPUTEX 2025–26); no external OEM customer | `secondary` |
| **Wingtech (闻泰科技)** | ODM/semis | announcement / components-first | Automotive-grade chip (MOSFET/IGBT/SiC) reliability pitch for robotics; humanoid "early stage" | `secondary` |
| **Inventec (英业达)** | ODM | adjacent infra (no humanoid) | COMPUTEX 2026: Atlas Edge AI server (IGX Thor), iTwin cobot, inspection UGV | `company-reported` |
| **Compal (仁宝)** | ODM | none-found (robotics) | Only vague smart-medical/healthcare framing; no humanoid/robot-assembly move found | `single-source`/none |
| **Wistron (纬创资通)** | ODM | none-found | RPA *software* only + AI-server capacity; **no** physical-robot move (do not confuse w/ 上纬/Swancor) | `secondary` |
| **Quectel (移远通信)** | module | design-win (arms-dealer) | Robrain brain × LimX TRON 1 (MWC 2025-06); 5G module mass-prod to Unitree; ¥4.11亿 AI-robot fund-raise | `primary`/`secondary` |
| **Fibocom (广和通)** | module | design-win + platform + invest | **Fibot** embodied-AI dev platform (2024-03); co-led Pre-A in Robopoet (2026-04, note: AI-companion toy, not humanoid) | `primary`/`secondary` |
| **MeiG Smart (美格智能)** | module | design-win | SNM970 (48 TOPS) ×2 = ~100 TOPS in **通天晓/Ultra Magnus** humanoid (AidLux/阿加犀 × Qualcomm, CES 2025) | `secondary` |
| **Thundercomm (创通/中科创达系)** | module/integrator | design-win (high-end compute) | **TurboX IRB10** (Qualcomm Dragonwing IQ10, peak 700 TOPS), Embedded World 2026; names full-size humanoid | `primary` |

Pattern: **China A-share ODMs hold the hardest cards** (Lens, Longcheer, Luxshare = real assembly/own-brand), **Taiwan EMS play invest-and-supply** (Foxconn) or **own-subsidiary-robot** (Quanta), and **module makers arms-deal** across all of it. Three different risk postures on the same bet.

---

## 2. Company profiles

Four dimensions each: ① 产品线布局 (product-line) ② 投资 (investment) ③ 抢客户/设计导入 (design-win) ④ 落地部署 (deployment). Bullet-dense, dated, source-quality marked.

### 2A. Taiwan EMS giants

#### Foxconn / Hon Hai (富士康/鸿海精密, incl. listed 工业富联 FII) — EMS

- **① 产品线**: Robotics is one of chairman Young Liu's "3 future industries" (EV, digital health, robotics). Dedicated automation BU under iPEBG (自动化机器人事业处); 170+ factories with internal automation (Kunshan plant: 2,000+ self-developed arms since 2010; workforce cut ~110k→~50k). At **COMPUTEX 2026 (June)** showed three lines `(primary)`: (1) **Nurabot** nursing robot (co-dev w/ NVIDIA, 75–80 tasks/day, ~30% nurse-workload cut, in clinical validation); (2) a **surgical "scrub nurse" collaborative robot** co-developed with **Kawasaki Heavy Industries** + Taichung Veterans General Hospital + Yuan High-Tech (on NVIDIA Isaac for Healthcare / GR00T VLA; simulation/workflow validation done, clinical validation pending); (3) a **wheeled industrial humanoid** for pick-and-place / force-controlled screw fastening on NVIDIA Isaac Teleop + "MOMClaw" — explicitly a **partner-hardware/system-integration** play (NVIDIA brain, ecosystem hardware), **not** a proprietary Foxconn robot body. Uses NVIDIA Omniverse digital twin for the Houston plant; early adopter of GR00T-Mimic synthetic-motion pipeline. **No confirmed in-house dexterous-hand product** — the oft-cited "灵巧手 LH-L02, 30,000 units/yr, 40% cost cut" claim **could not be traced to any primary Foxconn source** `(unverified — treat as possibly misattributed)`.
- **② 投资**: **(a) Agility Robotics** — existing investor pre-2026; **led >$200M PIPE** (at $10/share) in Agility's $2.5B SPAC with Churchill Capital Corp XI, announced **2026-06-24**, expected to list as "AGLT" `(primary)`. Prior stake size undisclosed. **(b) NUWA Robotics (女娲机器人**, Taiwan, f. 2016) — Foxconn subs *Maxwell Holdings* + FII's *Cloud Network Technology Singapore* jointly hold **22.71%** equity (per June-2025 disclosure tied to A-share 祥鑫科技 buying a further 1.25%); NUWA targets >$100M 2026 revenue `(primary)`. **(c) Robust.AI** — no equity stake found (manufacturing partnership, see ③).
- **③ 抢客户/设计导入**: **(1) UBTech (优必选)** — "comprehensive long-term strategic partnership" (2025-01-15) to validate Walker S1 industrial humanoids; joint smart-manufacturing lab; Walker S1 completed ~2-month field trials at **Shenzhen Longhua**, moved to phase-2 at **Zhengzhou** auto plant `(primary)`. **(2) NVIDIA** — deep co-dev on Isaac GR00T N1, Jetson Thor, Omniverse, GR00T-Mimic (announced ~2025-06, reaffirmed GTC/COMPUTEX 2026). **(3) Robust.AI** — strategic manufacturing partnership **2025-05-15** to scale the **"Carter"** warehouse robot (already >60% productivity gains at a DHL Supply Chain Las Vegas site) `(primary)`. **(4) Kawasaki** — joint surgical robot (COMPUTEX 2026). **(5) Tianqi Co. (天奇股份)** — per Feb-2026 report, plan to jointly deploy embodied robots across Foxconn's auto-manufacturing over 5 yrs, cumulative **≥2,000 units** `(secondary)`.
- **④ 落地部署**: **Houston TX** — Foxconn/NVIDIA Blackwell Ultra **GB300** AI-server plant (242,287 sq ft); GR00T-N1/Jetson-Thor humanoid/wheeled robots slated to begin production-line deployment **Q1 2026** (live status unconfirmed as of 2026-07) `(primary)`. **Kaohsiung** — service-humanoid co-dev w/ NVIDIA announced 2025-01-03, reiterated 2026-01/02. **Nurabot** — clinical validation done at TCVGH; expanding to Taipei VGH, Tung's Hospital, LTC sites; commercial launch targeted 2026; TCVGH expects "dozens" of units by year-end.
- **Read**: best understood as a **vertically-integrated manufacturing/investment hub** (own automation BU + Agility/NUWA equity + UBTech/NVIDIA/Robust.AI/Kawasaki partnerships) — **not** a single own-brand humanoid line. No Foxconn-branded humanoid sold to third parties yet. Highest-evidenced tier = **design-win/supply**, with a strong equity-investment second angle approaching plant-scale once Houston goes live.

#### Quanta Computer / Techman Robot (广达电脑/达明机器人), incl. Quanta Cloud Technology (QCT) — ODM/module

- **① 产品线**: **Techman Robot (TRI)** is Quanta's established cobot-arm subsidiary. **TM Xplore I** (unveiled 2025-08) is a **wheeled-base** (not bipedal) humanoid: 22+ joints, integrated inspection cameras, quick-change end-effectors, "See/Think/Act" stack on **NVIDIA Jetson Thor** (some early coverage cited Orin) for VLA inference `(primary)`. Officially shown at **NVIDIA GTC 2026 (2026-03-18)** as a three-way QCT + NVIDIA + Techman demo: QCT supplies GPU servers / "Dev. Kit for Physical AI," NVIDIA supplies Cosmos/Isaac GR00T + Jetson Thor, Techman supplies the platform — a **compute-to-robot full-stack** offering. Target apps: semiconductor fab, electronics assembly, automotive. Quanta's ODM component competency (motors/sensors/batteries/semis for Apple/Meta/Tesla) cited as supply-chain advantage, though **no specific Quanta-branded robot-component product line found**.
- **② 投资**: **No robotics equity/M&A found** — the robotics move is **organic** (Techman, wholly-owned). (A Quanta $5M/cumulative-$20M stake in **Vuzix** exists but that's AR/smart-glasses, not robotics — flagged for completeness, not counted.)
- **③ 抢客户/设计导入**: **NVIDIA** three-way co-dev (Jetson Thor/Isaac GR00T/Cosmos/Isaac Sim) is the *only* named partner angle — positions QCT as **infra supplier to the NVIDIA humanoid ecosystem**, not Techman selling to independent robot makers. **No third-party robot-maker design wins found** (no UBTech/Unitree/Figure component supply).
- **④ 落地部署**: Techman AI cobots upgrading production lines at **Quanta's Germany** automotive-electronics plant (reported 2026-07-01, DigiTimes — unit counts paywalled) `(single-source)`. TM Xplore I to be **tested in own/Quanta factories** before scaling in 2H 2026 (self-testing, not third-party deployment). **No numeric humanoid-unit deployment figures found.**
- **Read**: narrower/more recent than Foxconn — one in-house humanoid, no robotics M&A, deployment limited to internal cobot upgrades + a not-yet-shipped humanoid. Ceiling tier = **design-win/supply** (QCT as Physical-AI infra alongside NVIDIA/Techman), short of confirmed third-party customer wins.

#### Pegatron (和硕) — ODM
- **①** Robotics BU on a 5-year buildout, **components-first**; showcased **"Aria"** service robot + robot dog (COMPUTEX/investor events 2025–26) `(secondary)`.
- **②** No robotics equity/JV found. **③** Chairman Tung Tzu-hsien says NVIDIA names Pegatron among humanoid supply-chain beneficiaries; **no named external OEM customer**. **④** No mass-production humanoid; no unit deployment. **Read**: **announcement / components-first**.

#### Wistron (纬创资通) — ODM
- **①** **No dedicated robot/embodied-AI BU or robot-component line.** Public "robot" activity is **RPA software** (~1,800 RPA+AI apps, ~468,000 work-hrs/yr saved) `(single-source)`, *not* physical robotics. Core Physical-AI-adjacent business is **AI-server / GPU-rack manufacturing**: NVIDIA reportedly secured Wistron's new Zhubei AI-server plant capacity through 2026 for Blackwell/Rubin `(secondary)`; $761M Texas AI supercomputer facility w/ NVIDIA (H1 2026) `(secondary)`; among ~150 Taiwan firms building NVIDIA Vera Rubin NVL72 racks.
- **②③④** No robotics equity/design-win/deployment found. **Read**: **none-found** in physical robotics — it is a data-center infra play. **⚠ Entity warning**: do NOT conflate with **上纬新材 (Shangwei/Swancor, STAR 688585)**, the AgiBot/Peng-Zhihui listing vehicle that launched the 启元Q1 (Qiyuan Q1) mini humanoid (2025-12-31) — different company (see [ODM Opportunity §3](odm-opportunity.md#3-competitor-友商-scoreboard)).

#### Inventec (英业达) — ODM
- **①** COMPUTEX 2026: "Atlas Edge" AI server (NVIDIA IGX Thor), dual-arm cobot **iTwin**, inspection UGV; Omniverse/Isaac sim-to-real tooling `(company-reported)`. **②③④** No humanoid build/assembly, no robotics equity, no named OEM customer found. **Read**: **adjacent infrastructure**, no humanoid move.

#### Compal (仁宝) — ODM
- **①–④** Notebook/smart-device ODM with vague **smart-medical/healthcare** interest; **no humanoid, robot-assembly, or robot-component move found** in this pass `(single-source / absence of findings)`. **Read**: **none-found** in Physical-AI robotics (as of 2026-07) — treat as a watch item, not a rival.

### 2B. China ODM / EMS

#### Lens Technology (蓝思科技) — EMS/components
- **①** Glass/structural-parts giant (Apple supply chain) extending into robot **assembly + structural/thermal parts**. **②** Strategic stake in AgiBot's cleaning-robot subsidiary **Zhiding (智鼎)**. **③④** **JV** — *Hunan Zhiqi Future Technology (湖南智启未来科技)* w/ AgiBot, registered **2025-04**, RMB 10M capital, Changsha; **Lens holds 70%** (co-shareholders 上海智元新创 + 湖南东方数智能源投资; their splits undisclosed) `(primary)`; disclosed taking on **manufacturing/assembly across AgiBot's full 2025 humanoid lineup** (2025-08) `(secondary)`. No capacity/unit figures disclosed (RMB 10M is an option, not yet a factory). **Read**: **JV + plant-scale** — one of the two hardest-committed China ODMs, anchored to a volume-credible OEM (AgiBot shipped ~5,000+ in 2025, see [AgiBot](company-agibot.md)).

#### Longcheer (龙旗科技) — ODM
- **①** Global smart-product ODM (phones/tablets/wearables); positions as **industrial embodied-AI manufacturing partner**. **②** No disclosed equity stake found; relationship is customer + manufacturing partner. **③④** **AgiBot (智元)** strategic cooperation announced **~2025-10**: Longcheer placed a **framework order of "several hundred million yuan"** for **~1,000 精灵 G2** robots — among the largest domestic industrial embodied-AI orders at the time `(secondary)`. **2026-04-14**: 8-hour live production-line demo at Longcheer's **Nanchang tablet plant** — G2 as line "employee" doing precision load/unload, **>99.5% success**, 18–20 s/cycle, ~310 units/hr `(secondary)`. **June 2026**: six-day continuous run (64+ hrs, **64,828 tasks, 99.99% success**, 17,625 tablet units); AgiBot's **15,000th** robot delivered to Longcheer `(secondary)`. Plan to scale **from 4 → ~100 units** on the Longcheer line by **Q3 2026** `(company-reported, AgiBot exec Yao Maoqing)`. **Read**: **plant-scale customer deployment** — the most operationally proven China ODM×humanoid relationship on this page; note it is Longcheer *buying/hosting* AgiBot units on its own lines (customer + assembly partner), not building an own-brand robot.

#### Luxshare Precision (立讯精密) — ODM/EMS
- **①** **Own-brand robot** + components: guided **~3,000 humanoid units shipped 2025, all to external customers** `(company-reported, 2025-11)`; "Manufacturing 2.0" flexible line early 2026; targets ~80% self-developed core components (reducers, tendon-driven hand) by mid-2026 + a general-purpose robot prototype `(company-reported)`. **②** No third-party robotics equity found. **③④** Customer names undisclosed; all figures company-side. **⚠ Correction**: the circulated "~¥124M China Mobile order to Luxshare" (2025-07) is **contested/likely conflation** — primary tender coverage shows the ¥124.05M China Mobile contract-manufacturing procurement went to **AgiBot (¥78M) + Unitree (¥46.05M)** `(primary)`. Do not re-attribute to Luxshare. **Read**: **own-brand robot** — the highest ladder tier, but it carries **channel-conflict risk**: by building its own robot Luxshare becomes a competitor to any prospective assembly customer.

#### BYD Electronics (比亚迪电子) — EMS
- **①–④** Humanoid program (incl. reported ~20,000-robots-on-BYD-lines-by-2026 aspiration `(unverified)`) sits at **BYD Group level, not the listed BYDE entity**; BYDE discloses only "some business layout." **UBTech Walker S1** pilots in BYD car plants are a **customer relationship, not BYDE manufacturing** `(secondary)`. **Read**: **pilot** (group-level); no external humanoid manufacturing contract disclosed for the listed entity.

#### Huaqin Technology (华勤技术) — ODM
- **①** Positions to be a **"full-stack robot solution head supplier for 3C manufacturing."** **Gen-1 humanoid tested/debugged**; **Gen-2 bipedal** in development. Key components (**actuators, brain-body control boards**) pursued **in-house** for supply security + cost control `(secondary/company-reported)`. **②** No robotics equity found. **③** Building **data-collection robots** for domestic large-model companies (mass-prod/delivery 2026). **④** **Wheeled robots** for flexible manufacturing targeted for **batch delivery June 2026** into Huaqin's **own plants** — three uses: incoming-material sorting, cargo handling, production-line OBE inspection `(secondary)`. **Read**: **pilot → own-brand (internal-first)** — a genuine vertically-integrated program, early but concrete; a direct structural analog to Foxconn's own-automation approach at smaller scale.

#### Wingtech (闻泰科技) — ODM/semiconductors
- **①** Post-Nexperia, an ODM + power-semi maker (MOSFET/IGBT/GaN/SiC). Robotics posture is **components/reliability-first**: pitches automotive-grade chip reliability + accumulated customer base in industrial/collaborative/household robots; **humanoid explicitly "early stage"** `(secondary)`. **②③④** No humanoid build, robotics equity, or named humanoid-OEM customer found. **Read**: **announcement / components-first**.

### 2C. Module / compute makers (the "arms-dealer" layer)

This is Quectel's own competitive set — cross-form-factor compute/connectivity/positioning modules that sell into *any* robot. Full Quectel-specific analysis lives in the [Quectel pitch](../pitch/quectel.md); here is the rival scan. Structural finding: this market is **three layers** — (1) Chinese cellular-module makers (Quectel/Fibocom/MeiG), (2) Qualcomm-ecosystem specialist integrators (Thundercomm/Lantronix), (3) chip principals selling direct (Qualcomm/NVIDIA), the last of which threatens to **disintermediate** the module makers.

#### Quectel (移远通信, 603236) — module (arms-dealer)
- **①** Robot-targeted compute modules: **SG885G** (QCS8550, 48 TOPS), **SH602HA-AP** (D-Robotics Sunrise5, 10 TOPS BPU, names humanoid/wheel-arm/quadruped/service robots), CES-2026 flagship **SP895BD-AP** (Snapdragon Q-8750, 3nm, **77 TOPS**, on-device 11B-param LLM) `(primary)`; plus cellular/GNSS/Wi-Fi across the stack. **②** ¥4.11亿 "AI compute-module & solution industrialization" fund-raise item incl. **AI-robot solutions** `(primary)`. **③** **Robrain** robot-brain × **LimX (逐际动力)** running on bipedal **TRON 1** (MWC Shanghai 2025-06) `(primary)`; 5G quadruped module **mass-produced to Unitree** `(secondary)`; named 星动纪元/RobotEra as a client `(secondary)`; Deyi (德壹) physiotherapy robot, EEVE mower AMR. **④** Pilot-level design-ins; no unit-count disclosure. **Read**: **design-win (arms-dealer)** — global cellular-module #1 (~36–37% share), already in-market with named robot cases; short on peak compute vs Thundercomm/Jetson.

#### Fibocom (广和通, 300638) — module
- **①** **Fibot** embodied-AI dev platform (arm + compute + omnidirectional base; SC171/QCM6490, 12 TOPS; reproduces Stanford Mobile ALOHA), launched **2024-03-29** `(primary)` — a fuller **platform/subsystem** bind than a bare module. **②** **Co-led Pre-A in Robopoet (珞博智能)**, **2026-04-20** `(primary)` — **⚠ note**: Robopoet is an **AI-companion toy/collectible** maker (Fuzozo/芙崽), **not** a humanoid/embodied-robot company; Fibocom's role is "cellular + global SIM tariff + strategic investment." Do not overstate this as a humanoid-equity move. **③④** Platform + connectivity design-ins. **Read**: **design-win + platform + (adjacent) invest** — the "platform+investment" binding model is the sharpest competitive pressure on a bare-module vendor like Quectel.

#### MeiG Smart (美格智能, 002881) — module
- **①** **SNM970** (QCS8550, 48 TOPS); SG880 series spans 0.2→48 TOPS, humanoid-targeted. **③** Two SNM970 modules = **~100 TOPS** power the **通天晓 / Ultra Magnus** humanoid prototype (partner **AidLux/阿加犀智能**, Chengdu × Qualcomm), unveiled **CES 2025 (2025-01-07/08)** — billed as the first fully Qualcomm-SoC on-device-AI humanoid `(secondary)` — a concrete named humanoid design-win. **②④** No robotics equity found; deployment pilot-level. **Read**: **design-win** — Quectel's most direct QCS8550-vs-QCS8550 rival, same Qualcomm ecosystem, same humanoid target.

#### Thundercomm (创通/中科创达系) — module/integrator
- **①③** **TurboX IRB10** (Qualcomm Dragonwing IQ10, **peak 700 TOPS**, 20 concurrent cameras), Embedded World 2026 — names industrial AMR / **full-size humanoid** / service robots `(primary)`. A pure Qualcomm-ecosystem integrator (not a telecom-module maker) attacking the humanoid SoM socket at **high compute** (700 TOPS » module makers' 77 TOPS tier). **Read**: **design-win (high-end compute)** — the peak-compute threat to Quectel's tier.

- **Chip-principal overhang** (not module makers, but the disintermediation risk): **Qualcomm** launched a full robotics suite at CES 2026 (Dragonwing IQ10; Figure collaboration to "define next-gen compute") `(primary)`; **NVIDIA** Jetson Thor (2,070 FP4 TFLOPS) is the high-end humanoid-brain de-facto standard (see [NVIDIA](company-nvidia.md)). Both increasingly sell **direct to OEMs**, squeezing the module layer — the central long-term risk for every arms-dealer here.

---

## 3. 读数 (Synthesis): committed vs announcement-only, own-brand vs arms-dealer

### Who is actually committed (steel-in-the-ground) vs announcement-only

- **Genuinely committed (dated, operational)**: **Longcheer** (AgiBot G2 on a live 3C line, 64,828 tasks logged, ~1,000-unit framework order, 15,000th unit delivered — the single most *operationally proven* row); **Lens** (JV + full-lineup assembly of AgiBot); **Luxshare** (own line, ~3,000 units guided — though all figures are company-reported and customer-unnamed); **Foxconn** (a real >$200M PIPE + live manufacturing partnerships, but Houston robot-line "live" status unconfirmed). **Huaqin** is a real internal-first program but pre-volume (June-2026 batch target).
- **Announcement / options-dressed-as-commitments**: **Quanta/Techman** (own humanoid but not yet shipped; self-testing only); **Pegatron, Wingtech** (components-first, no OEM customer); **BYDE** (group-level pilots, listed entity discloses "some layout"); **Fibocom's** Robopoet stake (an AI-toy connectivity bind, not humanoid equity — a common overstatement). **Inventec** is infra-adjacent. **Wistron, Compal** = **none-found** in physical robotics.
- **The RMB-10M / PIPE / forum-remark caveat**: as in [ODM Opportunity §6](odm-opportunity.md#6-what-would-make-this-urgent-fomo-evidence-honestly-framed), grade peers by *steel-in-the-ground*. Lens's JV is RMB 10M (an option); Foxconn's PIPE buys information rights, not build rights. By an operational-deployment test, **only Longcheer, Lens, and Luxshare have done manufacturing-scale things with humanoids that are visible on a factory floor today.**

### The structural split: "own-brand robot" vs "arms-dealer/supply"

| Posture | Players | Upside | The catch |
|---|---|---|---|
| **Own-brand robot** | **Luxshare** (~3,000 units); **Quanta/Techman** (TM Xplore I); **Huaqin** (internal-first) | Captures full robot value; controls roadmap | **Channel conflict** — you become a competitor to every prospective assembly customer, and the moat is *software you don't have* (VLA/[world models](world-models.md)). Luxshare is the canonical channel-conflict case. |
| **Arms-dealer / supply** | **Foxconn** (Agility PIPE + UBTech/Robust.AI manufacturing); **Lens** (AgiBot assembly JV); **Longcheer** (AgiBot G2 host); module makers (**Quectel/Fibocom/MeiG/Thundercomm**) | Sells regardless of which robot brand survives the shakeout ([NDRC](landscape-china.md) warned >150 near-identical programs); survives the form-factor debate | Small near-term pool; component tiers China owns face 15–20%/yr deflation; chip principals (Qualcomm/NVIDIA) may disintermediate the module layer |

The cleanest reads: **Foxconn is the arms-dealer's arms-dealer** (invests in Agility, manufactures for UBTech/Robust.AI, never ships an own body — maximal optionality, minimal channel conflict). **Luxshare took the opposite bet** (own robot, foreclosing assembly-for-others). **Lens and Longcheer sit between** — pure assembly/host partners to one champion (AgiBot), high commitment but concentrated counterparty risk if AgiBot stumbles.

### What this means for a module maker like Quectel (where rivals are strong / weak)

- **Rivals are STRONG where Quectel doesn't play**: final-assembly and structural/thermal design-ins are owned by **Foxconn** (UBTech/Robust.AI/Agility), **Lens** (AgiBot bodies), **Longcheer** (AgiBot host lines). A module maker should **not** try to out-assemble these EMS giants — that is their moat, and entering it means channel conflict (the Luxshare trap).
- **Rivals are WEAK / absent where Quectel is strong**: none of the EMS giants ship a **compute/connectivity/positioning module** — Foxconn/Lens/Longcheer *consume* modules, they don't sell them. Quectel's real competitors are the **other module makers** (Fibocom, MeiG, Thundercomm) and, structurally, the **chip principals** (Qualcomm/NVIDIA) selling direct. Quectel's edge over them: **#1 cellular share + GNSS positioning + mass-production maturity + already-named robot cases (LimX/Unitree)**. Its gaps: **peak compute** (77 TOPS vs Thundercomm 700 TOPS / Jetson Thor), **software/middleware depth**, and **disintermediation risk**.
- **Net**: the arms-dealer lane is the defensible one for Quectel — but the *most contested* sub-lane is exactly its own (module socket), where Fibocom's platform+investment binding and Thundercomm's 700-TOPS ceiling are the live threats, not Foxconn's PIPE. See [ODM Opportunity §5](odm-opportunity.md#5-strategic-options-for-a-generic-odm-build--partner--invest--wait) and the [Quectel pitch §5–6](../pitch/quectel.md) for the strategic-options detail.

---

## 4. Watch items (fast-churning ledger — each dated)

Grade freshness by date; any item >~30 days stale is a re-check candidate.

| Date | Item | Why it matters |
|---|---|---|
| 2026-06-24 | **Foxconn-led >$200M PIPE** in Agility's $2.5B SPAC (close expected end-2026, ticker AGLT) | Turns Foxconn's Agility stake into a public position; watch close + whether it converts to a manufacturing contract |
| 2026-04-14 → Q3-2026 | **Longcheer × AgiBot** scaling 4 → ~100 units on the Nanchang line | The most concrete China ODM humanoid ramp; if it hits 100, it is the first plant-scale embodied-AI 3C line |
| 2026-06 | **Huaqin** wheeled-robot batch delivery into own plants (targeted June 2026) | Confirms/denies a second internal-first China ODM program at volume |
| 2H 2026 | **Quanta/Techman TM Xplore I** mass-production target (after internal testing) | First Taiwan own-brand humanoid to ship? Or slips like most humanoid timelines |
| Q1 2026 (unconfirmed) | **Foxconn Houston** GR00T humanoid line "live" status | Slated Q1 2026; live status unconfirmed as of 2026-07 — a key steel-in-ground test |
| 2026-07-01 | **Quanta/Techman** cobots in Germany auto-electronics plant (DigiTimes, paywalled) | Unit counts unconfirmed; watch for a de-paywalled/confirmed figure `(single-source)` |
| ongoing | **Qualcomm/NVIDIA direct-to-OEM** (Figure×Qualcomm; Jetson Thor adoption) | Disintermediation risk to *all* module makers incl. Quectel/Fibocom/MeiG |
| 2026-02 (reported) | **Tianqi (天奇股份) × Foxconn** ≥2,000 embodied robots over 5 yrs in auto-manufacturing | Second large Foxconn deployment vector; watch for a signed contract vs plan `(secondary)` |
| unverified | Foxconn **"LH-L02" dexterous hand, 30,000 units/yr** | Widely cited but **untraceable to a primary Foxconn source** — do not repeat as fact until confirmed |

---

## Sources

Foxconn:
- https://www.datacenterdynamics.com/en/news/foxconns-houston-nvidia-server-factory-could-use-humanoid-robots/ ; https://www.humanoidsdaily.com/news/foxconn-to-deploy-nvidia-powered-humanoid-robots-in-houston-ai-server-plant — Houston GB300 plant, GR00T/Jetson-Thor humanoid deployment Q1 2026, 242,287 sq ft, Omniverse digital twin. `primary`
- https://www.agilityrobotics.com/content/agility-robotics-to-go-public-through-merger-with-churchill-capital-corp-xi ; https://techfundingnews.com/agility-robotics-goes-public-at-a-2-5b-valuation-and-its-humanoid-robots-are-already-working-in-warehouses/ — Foxconn-led >$200M PIPE, $2.5B SPAC, 2026-06-24. `primary`
- https://www.21jingji.com/article/20250611/herald/a0ccf01f6f1d77959f1863fe9231e22f.html ; https://finance.sina.com.cn/roll/2025-06-11/doc-inezskcm9447343.shtml — Foxconn subs hold 22.71% of NUWA Robotics; Xiangxin 1.25% stake (June 2025). `primary`
- https://finance.sina.com.cn/roll/2025-01-15/doc-ineezwyx7735815.shtml ; https://www.qbitai.com/2025/01/244112.html — FII × UBTech strategic partnership (2025-01-15); Walker S1 Shenzhen→Zhengzhou trials. `primary`
- https://www.businesswire.com/news/home/20250515789852/en/Robust.AI-Partners-With-Foxconn-to-Accelerate-and-Scale-Manufacturing-of-Carter-Warehouse-Automation-Robots — Robust.AI × Foxconn Carter manufacturing (2025-05-15); DHL Las Vegas >60% productivity. `primary`
- https://www.foxconn.com/en-us/press-center/events/foxconn-events/2044 ; https://www.technice.com.tw/technology/robot/225246/ — COMPUTEX 2026: Nurabot, Kawasaki surgical robot, wheeled industrial humanoid (Isaac Teleop/MOMClaw). `primary`
- https://finance.sina.com.cn/roll/2025-01-03/doc-inecthkr4573819.shtml — Young Liu: Foxconn × NVIDIA Kaohsiung service humanoid (2025-01-03). `primary`
- https://www.21jingji.com/article/20260210/herald/c7e320646a87f919e869c3f343841278.html — Tianqi (天奇股份) × Foxconn ≥2,000 embodied robots over 5 yrs (reported Feb 2026). `secondary`

Quanta / Techman / QCT:
- https://roboticsandautomationnews.com/2025/08/27/techman-robot-unveils-humanoid-prototype-aims-for-2026-launch/93937/ ; https://www.digitimes.com/news/a20250822PD203/taiwan-techman-humanoid-robot-quanta-subsidiary.html — TM Xplore I unveiled Aug 2025; wheeled base, 22+ joints, quick-change end-effectors. `primary`
- https://www.tm-robot.com/en/company/news/Techman-Robot-at-GTC-2026_Unveils-New-AI-Strategy-and-Humanoid-Robot-TM-Xplore-I ; https://www.qct.io/Press-Releases/index/PR/Server/QCT-Collaborates-with-Techman-Robot-and-NVIDIA-to-Accelerate-Physical-AI-Innovation-at-NVIDIA-GTC-2026/1/ — GTC 2026 (2026-03-18) three-way QCT/Techman/NVIDIA Physical-AI collaboration; Jetson Thor. `primary`
- https://interestingengineering.com/ai-robotics/nvidia-powered-wheeled-humanoid-robot ; https://en.wikipedia.org/wiki/TM_Xplore_I — 2H 2026 production scaling after internal testing. `secondary`
- https://www.digitimes.com/news/a20260701PD237/techman-quanta-automotive-production-germany.html — Techman cobots at Quanta Germany auto-electronics plant (2026-07-01, paywalled, headline/lead only). `single-source`

Lens / Longcheer / Luxshare / China ODMs (several also in [ODM Opportunity](odm-opportunity.md) Sources):
- https://www.nbd.com.cn/articles/2025-08-04/4000682.html — Lens assembly across AgiBot's full 2025 lineup; Zhiding investment (2025-08). `secondary`
- https://finance.sina.com.cn/stock/relnews/cn/2025-04-06/doc-inesemyu9846834.shtml — 湖南智启未来科技 JV: RMB 10M capital, **Lens 70%**, co-shareholders 上海智元新创 + 湖南东方数智能源投资 (splits undisclosed), legal rep 陈运华 (registered ~2025-04). `primary`
- https://interestingengineering.com/ai-robotics/china-agibot-robots-hit-99-percent-success-during-six-day-live-factory-demo — AgiBot G2 six-day demo at Longcheer Nanchang: 64+ hrs, 64,828 tasks, 99.99% success, 17,625 tablets; 15,000th unit delivered to Longcheer (reported 2026-06-29). `secondary`
- https://finance.sina.com.cn/stock/wbstock/2026-04-15/doc-inhurayu3303895.shtml ; https://field.10jqka.com.cn/20260415/c676021115.shtml — AgiBot 精灵 G2 on Longcheer Nanchang line: 8-hr live demo 2026-04-14, >99.5% success, plan 4→~100 units by Q3 2026 (exec Yao Maoqing). `secondary`
- https://www.donews.com/news/detail/4/6520156.html — AgiBot humanoid mass-production landing on Longcheer line; ~1,000-unit framework order (~several hundred million yuan), announced ~Oct 2025. `secondary`
- https://finance.sina.com.cn/tech/roll/2025-11-27/doc-infyvtha0077094.shtml ; https://m.ofweek.com/im/2025-11/ART-201900-8100-30674854.html — Luxshare ~3,000-unit 2025 guidance, Manufacturing 2.0, ~80% self-developed components by mid-2026 (company-reported). `company-reported`
- https://www.guancha.cn/economy/2025_07_12_782708.shtml — China Mobile ¥124.05M humanoid contract-manufacturing tender won by AgiBot (¥78M) + Unitree (¥46.05M) — corrects the Luxshare misattribution. `primary`
- https://zhuanlan.zhihu.com/p/2020563250752882215 ; https://en.huaqin.com/chanpinyufuwu/chuangxinyewu/jiqiren ; https://www.digitimes.com/news/a20260701VL213/china-humanoid-robot-robotics-production-policy.html — Huaqin gen-1 humanoid tested, gen-2 bipedal in dev, wheeled-robot batch delivery June 2026 into own plants, in-house actuators/control boards. `secondary`/`company-reported`
- https://www.wingtech.com/cn/syxpfb/6680 — Wingtech robotics posture: automotive-grade chip reliability, humanoid "early stage," industrial/collaborative/household robot customer base. `secondary`
- https://www.stcn.com/article/detail/1353689.html ; https://www.qbitai.com/2024/12/238878.html — BYD Electronics listed-entity "some layout"; BYD Group-level ~20,000-robot 2026 aspiration (unverified). `secondary`/`unverified`

Taiwan ODMs (Pegatron/Wistron/Inventec/Compal):
- https://www.technice.com.tw/issues/ai/158236/ ; https://news.cnyes.com/news/id/4329179 — Pegatron robotics BU components-first; Tung Tzu-hsien on NVIDIA naming Pegatron. `secondary`
- https://www.uipath.com.cn/resources/automation-case-studies/wistron-kunshan — Wistron RPA software (~1,800 apps, ~468,000 hrs/yr) — software bots, not physical robots. `single-source`
- https://www.digitimes.com/news/a20250620PD217/wistron-ai-server-production-demand-capacity.html — Wistron $761M Texas AI supercomputer w/ NVIDIA (H1 2026). `secondary`
- https://www.21jingji.com/article/20251231/herald/ee50c1ec508547b9420530135d3f5166.html ; https://www.jiemian.com/article/13834840.html — **Entity-separation proof**: 上纬新材 (Shangwei/Swancor, STAR 688585, founder 蔡朝阳/SWANCOR-Samoa) — Peng Zhihui (稚晖君) became chairman 2025-11-25, launched 启元Q1 mini humanoid 2025-12-31 under 上纬启元 brand; ~¥2.1B control acquisition by AgiBot-affiliate 智元恒岳. This is NOT Wistron (纬创资通). `primary`/`secondary`
- https://ai.inventec.com/英業達於computex-2026展現ai落地實力/ — Inventec COMPUTEX 2026 Atlas Edge / iTwin cobot / inspection UGV. `company-reported`
- https://www.compal.com/en-us/ — Compal ODM; smart-medical/healthcare interest, no humanoid/robot-assembly move found this pass. `single-source`/absence

Module makers:
- (Quectel, Fibocom, MeiG, Thundercomm, Qualcomm, NVIDIA module-layer facts sourced in the [Quectel pitch §5 & Sources](../pitch/quectel.md)): SG885G/SH602HA-AP/SP895BD-AP (77 TOPS), Robrain × LimX TRON 1, Unitree quadruped module; Fibocom Fibot platform + Robopoet Pre-A (AI-companion toy, not humanoid); MeiG SNM970 ×2 (~100 TOPS) in 通天晓/Ultra Magnus (CES 2025); Thundercomm TurboX IRB10 (700 TOPS, Embedded World 2026); Qualcomm CES 2026 robotics suite + Figure; NVIDIA Jetson Thor. `primary`/`secondary` as marked there.
- https://www.meigsmart.com/articledetail/496.html — MeiG SNM970 (QCS8550, 48 TOPS) ×2 = ~100 TOPS in 通天晓/Ultra Magnus; partner **阿加犀/AidLux** (Chengdu) × Qualcomm, CES 2025 (2025-01-07/08). `primary`
- https://www.fibocom.com/newscenter/info_itemid_8664.html ; https://www.ctoy.com.cn/n/d43521.html — Fibocom × Robopoet (珞博智能) Fuzozo/芙崽 **AI-companion toy** (LE270-CN module); Fibocom co-led Pre-A 2026-04. Confirms AI-toy, not humanoid. `primary`/`secondary`
- https://www.thundercomm.com/turbox-irb10-launches-at-embedded-world-2026/ — Thundercomm TurboX IRB10 (Qualcomm Dragonwing IQ10, **peak 700 TOPS**), Embedded World 2026, names full-size humanoid. `primary`

Cross-links (this repo): [ODM Opportunity](odm-opportunity.md) (market-sizing, value-chain map, strategic options — not repeated here), [Quectel pitch](../pitch/quectel.md) (module-maker-specific analysis), [AgiBot](company-agibot.md), [Agility](company-agility.md), [UBTech](company-ubtech.md), [Hardware](hardware.md), [NVIDIA](company-nvidia.md), [Landscape: China](landscape-china.md).
