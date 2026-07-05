---
title: Humanoid Component Supply Chain
slug: component-supply-chain
updated: 2026-07-05
confidence: draft
---
> A BOM-money-and-chokepoint map of the humanoid mechatronics value chain, written for an ODM/module-maker analyst (Quectel context). The single largest cost center is the **joint/actuator system (~50-57% of robot BOM** per sell-side breakdowns), inside which **reducers alone run ~30-36% of a rotary-joint actuator's cost** — commonly quoted as ~15-25% of whole-robot BOM (analyst estimate, single-chain-of-custody, unverified). The tightest physical bottleneck is **planetary roller screws** (precision thread-grinding capacity), where overseas leaders (GSA, Rollvis, Ewellix, Rexroth) still hold ~78% of the *China* market (2022 CR4) and China is racing to localize. China already **dominates harmonic reducers domestically** — 绿的谐波 (Suzhou Green Harmonic, LeaderDrive) 27.5% + 来福谐波 (Laifu) 21.4% = ~half of China's robot harmonic-reducer market by 2025 volume (灼识咨询/China Insights Consultancy via Laifu's HKEX prospectus) — while Japan's **Harmonic Drive Systems** keeps ~80% of the *global* harmonic-drive market and the high-precision tier. This page goes deeper on the **component layer** than [Hardware](hardware.md) (which covers the actuator/compute/battery overview) and [Tactile Sensing & Dexterous Hands](tactile-hands.md) (hand hardware + touch); it maps *who supplies what, dated design-wins, and where the money and chokepoints sit* — the arms-dealer geography for a supplier analyst. For the ODM/EMS assembly layer see [ODM Competitors](odm-competitors.md) and [ODM Opportunity](odm-opportunity.md); for supply-chain geography [Landscape: China](landscape-china.md); for the Tesla BOM anchor [Optimus](company-optimus.md).

Source-quality tags used below: `(primary)` company/regulator disclosure; `(secondary)` reputable press; `(single-source)` one outlet / one cross-referenced cluster; `(unverified)` uncorroborated or analyst-estimate-only.

## 1. BOM value-chain map — where the money and the chokepoints are

Humanoid BOM splits are **analyst estimates, not audited OEM disclosures**, and vary hugely by design (harmonic-heavy upper body vs roller-screw legs, DoF count, in-house vs bought hands). The most-cited anchor is the Tesla Optimus breakdown circulated by 高盛/Goldman + Chinese sell-side (Tianfeng 天风, Huaan 华安, others). Treat every % below as a **range, single-chain-of-custody** figure.

| Subsystem | ~% of robot BOM (analyst est.) | Chokepoint? | Who owns it today |
|---|---|---|---|
| **Reducers** (harmonic / RV / planetary) | **~15-25%** (reducers alone; ~30-36% of a *rotary-joint actuator's* cost) | ⚠️ High-precision harmonic still Japan-led globally; RV a Nabtesco stronghold | Japan HDS/Nabtesco (global high-end) + China 绿的/来福/中大力德 (domestic volume) |
| **Planetary roller screws** (linear leg actuators) | **~15-18%** (lead/roller screws, per unverified 36kr split) | 🔴 **Tightest bottleneck** — precision thread-grinding machine tools scarce | Overseas GSA/Rollvis/Ewellix/Rexroth ~78% of China market (2022 CR4); China 五洲新春/恒立/贝斯特/南京工艺 racing in |
| **Frameless torque motors + hollow-cup motors** | **~12%** (motors, per unverified 36kr split) | ⚠️ Medium — NdFeB magnet dependency (China ~90% magnet processing) | Global Kollmorgen/Parker/TQ + China 步科/昊志/鸣志 (incl. hollow-cup 空心杯); magnets ~China |
| **Dexterous hands** (hollow-cup motors + micro screws + tactile) | **~high single-digit → low-teens %** (highest per-unit share after actuators; hollow-cup motor ~54.5% of hand-actuator cost per one estimate) | ⚠️ Weakest branch — durability, tactile calibration | China volume tier (Inspire/LinkerBot/AgiBot); Tesla/Figure in-house — see [tactile-hands](tactile-hands.md) |
| **Force / tactile sensors** (6-axis F/T + fingertip taxels) | **~5-10%** (sensors + other, per unverified splits) | ⚠️ High-end 6-axis historically ATI/Schunk; now localizing fast | China 蓝点触控/Landot ~72.6% humanoid share (2025), 宇立/坤维/鑫精诚/柯力 |
| **Compute** (Jetson Thor / Qualcomm / custom) | **~5-10%** (falling as capability rises) | Low physically; strategic (NVIDIA lock-in) | NVIDIA de-facto; Qualcomm; module makers (Quectel/Fibocom/MeiG) — see [odm-competitors](odm-competitors.md) |
| **Battery** (~2 kWh Li-ion pack) | **~3-5%** | Low | China cell/pack dominance (CATL ecosystem) |
| **Structural / thermal / harness** | **~5-10%** | Low | EMS/ODM (Lens, Longcheer) — see [odm-competitors](odm-competitors.md) |

**Reads:**
- **Biggest cost = actuators/joints** (~50-57% of BOM as a system); **reducers are the single largest *component category*** inside it (~30-36% of a rotary joint). This is where the design-win money concentrates.
- **Tightest bottleneck = planetary roller screws**, not reducers — reducers have credible domestic second-sources, roller screws do not yet at volume. The binding constraint is upstream: precision thread-grinding machine tools (themselves supply-limited). See [Hardware](hardware.md) watch items and [Optimus](company-optimus.md).
- **Optimus reducer count anchor** (per 机器人大讲堂/leaderobot.com breakdown, `single-source`/unverified): ~20 harmonic + ~8 RV + ~6 planetary reducers across ~28 body joints; ~14 inverted planetary roller screws in the legs; ~20 coreless (hollow-cup) motors in the hands. Other designs vary widely (one Tianlian design cited at up to 41 harmonic units across 71 DoF).
- **"~30% of BOM is reducers" is a widely-repeated but single-chain analyst framing** — do not treat as an audited number.

---

## 2. Per-sub-chain competitor scoreboards (as of 2026-07)

Commitment ladder (hardest → softest): **shipping-to-humanoid > sampling/qualifying > pivoting-in > positioning > none-found**.

### 2A. 谐波 / RV 减速器 — Harmonic & RV reducers

The best-covered sub-chain; China's clearest localization win in *harmonic*, still importing high-end and RV.

| Supplier | Region | Makes | Humanoid design-wins (dated) | Commitment | Cost / localization | sq |
|---|---|---|---|---|---|---|
| **Harmonic Drive Systems (HDS, ハーモニック)** | Japan | Full precision harmonic (strain-wave) range; the global standard | No specific dated humanoid-OEM win found via primary source; feeds the broader ecosystem | shipping | **~80% global harmonic share**; ~RMB 3,000-4,000/unit (vs ~2,000 for 绿的); ~JPY 27.5bn 2024-26 capex incl. ~JPY 10.6bn Japan plant for humanoid reducers, production start ~2026-03 | `secondary` (share); `single-source` (capex claim) |
| **Nabtesco (ナブテスコ)** | Japan | RV™ cycloidal (14M+ cumulative units); new **RVmini® / Monocrank™** (announced 2025-12-02) for cobot/humanoid low-torque gap | None found — RVmini/Monocrank shown as *reference* items at iREX2025 (2025-12-03), no shipping customer named | sampling/qualifying | Global #1 in industrial-robot RV; new compact lines fill the humanoid gap but not yet shipping to a named humanoid | `primary` (product launch) |
| **绿的谐波 / Suzhou Green Harmonic (LeaderDrive, SH688017)** | China | Full-vertical harmonic (flexspline/wave-gen/bearings in-house) + mechatronic joint modules; claims only firm globally doing full self-supply core→assembly for precision harmonic | **Unitree** (Walker S2, CCTV Gala robot ~2025); **AgiBot/智元** bulk supply 2025; **Tesla** — passed Optimus Tier-2 plant audit + signed **10,000-unit order for 2026 delivery** at ~RMB 2,000/unit, 30-40% below HDS *(cross-verified across multiple Chinese outlets Dec 2025 but NO Tesla-side disclosure — treat as single-source cluster, unverified)* | shipping | FY2025 rev RMB 571M (+47.3%), NP RMB ~124M (+121%); 425,200 units shipped (+72.5%); capacity ~790k→~1.59M units/yr by 2027 + Mexico JV ~300k/yr; **#1 China 27.5% share** (2025 volume, 灼识咨询/CIC) | `primary` (financials); `single-source` (Tesla) |
| **来福谐波 / Laifu Harmonic (HKEX 3952.HK)** | China (Shengzhou, ZJ) | Harmonic 8-40mm+ range (+ claimed 13g "03 series" micro-reducer for hand joints), joint modules, torque motors | **星动纪元 / Xingdong Era** cooperation (2025); prospectus: one of only two domestic makers (with 绿的) delivering + mass-producing humanoid harmonic reducers as of end-2025 | shipping | **HK's first dedicated harmonic-reducer stock**, IPO'd 2026-06-30 raising ~HK$1.0bn+; rev RMB 94.5M→108M→261M (2023-25, +142%); **not yet profitable** (net loss ~RMB 171M in 2025, accum. ~RMB 508M); **#2 China 21.4% share**; 97.1% capacity utilization H1 2026 | `primary` (share/prospectus); `unverified` (13g micro-reducer) |
| **中大力德 / Zhongda Leader (SZ002896)** | China (Ningbo) | Only domestic firm mass-producing **all three** (planetary + RV + harmonic); + integrated actuator units | **AgiBot**: exclusive planetary-reducer supplier for 远征A2 & 灵犀X1, batch since 2024 (~RMB 5,000/robot, `secondary`); **Unitree**: ~63% of Unitree's planetary-reducer procurement (Go1/H1) `(single-source)` | shipping | One-stop reducer supplier positioning vs Nabtesco/HDS imports on cost. *Note: indirect capital link to Unitree via 深创投/Shenzhen Capital stake — NOT a direct shareholding (retail coverage conflates the two)* | `secondary`/`single-source` |
| **双环传动 / Shuanghuan Driveline (SZ002472)** via **环动科技 / Finemotion** | China (Taizhou, ZJ) | Full RV line (SHPR-E/C/H/XB, 50+ variants, 3-1000kg loads) + harmonic + planetary + new joint modules | Audited/disclosed customers are **industrial-robot integrators** (Efort/Kanop/Qianjiang/STEP/Kaierda/GSK/华中数控/等) — **no humanoid OEM in the audited customer list** `(primary)`; **Tesla** claim has since escalated (Chinese media, Dec 2025) from a joint RV-development *discussion* (~20-30 person project, ~RMB1,500/unit target) to a reported **pass of Optimus 2nd-round verification + ~4,000-unit small-batch RV delivery from 2025Q4** — **no Tesla-side disclosure; single-source cluster, unverified** `(single-source, unverified)` | pivoting-in / (claimed small-batch) | China RV share ~14% (parent); group reducer capacity ~150k units/yr @60-70% util; harmonic cap 50k (output 20-30k, mostly industrial); 环动科技 STAR Market IPO application accepted 2024-11 (~RMB 1.4bn target, not yet listed mid-2026) | `primary` (customer list); `single-source` (Tesla) |
| **昊志机电 / Guangzhou Haozhi (SZ300503)** | China (Guangzhou) | Harmonic (batch-verified since 2019) + torque motors + drives + encoders + joint modules; also frameless motors | Established customers are **industrial/cobot** makers (大族/沁峰/广数/众为兴), not humanoid OEMs; one roundup lists it feeding Tesla dexterous-hand chain alongside 绿的/汉宇 — **single-source, no company confirmation** | sampling/qualifying | H1 2025 total rev RMB 703M (+14%); **robotics core-component rev only RMB 12.21M** (+127% off tiny base) → humanoid business immaterial to revenue | `secondary`; `single-source` (Tesla-hand claim) |
| **丰立智能 / Zhejiang Fore (SZ301368)** | China (ZJ) | Small/micro harmonic + planetary + micro bevel/cylindrical gears — sized for **dexterous hands & small joints** | **星动纪元** deep cooperation since H2 2023; supplies harmonic + planetary + micro-reducers/gears into **XHAND1** 5-finger hand — **"小批量生产交货"/small-batch delivery**, and the 2025-03-18 IR record explicitly states the company "目前未对市场进行批量供货" (not yet doing mass-market batch supply) (IR filings 2025-03 & 2025-12, `primary`); also **XPeng/小鹏** (2025-12) | shipping (small-batch) | **Among the best-sourced humanoid design-wins in this sub-chain** (primary IR disclosure, not media inference) — but note the design-in is a small-batch partner supply, not confirmed mass production; 2025 harmonic capacity plan 50k units @>98% yield | `primary` (Xingdong); `secondary` (XPeng) |

### 2B. 行星滚柱丝杠 — Planetary roller screws (the strategic chokepoint)

The tightest bottleneck; overseas still dominant, China's domestic-substitution frontier. (Overview in [Hardware](hardware.md); this is the supplier detail.)

| Supplier | Region | Makes | Humanoid design-wins (dated) | Commitment | Cost / localization | sq |
|---|---|---|---|---|---|---|
| **GSA / Rollvis (Switz.) / Ewellix (Swe.)** | Europe | Precision & inverted planetary roller screws | The incumbent stack behind Western humanoid programs; no single dated humanoid OEM confirmed publicly here | shipping (industrial) | **Overseas CR4 ~78% of the China market (2022)** — the widely-cited ~78% is the *China-market* CR4 of **GSA + Ewellix + Rollvis + Rexroth/Bosch** (Rollvis 26% + GSA 26% + Ewellix 14% ≈ 66% for these three; Rexroth makes up the rest); often loosely repeated as "global." Rollvis acquired by GSA 2016; Ewellix acquired by Schaeffler 2022 — the high-precision incumbents China is trying to displace | `secondary` |
| **五洲新春 / Wuzhou New Spring (SZ603667)** | China | Planetary roller screws, micro-ball screws, robot bearings | Suspected Tesla transmission-component supply *via* Bosch / 拓普 Tuopu chain — **inferred, not confirmed** | shipping/qualifying | ~RMB 10.55bn raise; planned capacity **980k planetary roller screws + 2.1M micro-ball screws** → supports **~70,000 humanoid robots** | `secondary`; `single-source` (Tesla-via-Bosch inference) |
| **恒立液压 / Hengli Hydraulics (SH601100)** | China | Precision ball screws, planetary roller screws, linear guides | Linear-drive project; sample delivery began 2024-09, entering batch production | qualifying/shipping | RMB ~1.4bn 2022 linear-drive investment; broad linear-motion portfolio developed in ~2 yrs | `secondary` |
| **贝斯特 / Best (SZ300580)** | China | Planetary roller screws (via German **KISSLING** acquisition); C0/C5 precision (±0.005mm) | Completed tech/equipment prep for **2025 batch supply** of humanoid roller screws | qualifying → shipping | KISSLING acquisition = fast-track to high precision; batch-supply readiness 2025 | `secondary` |
| **南京工艺 / Nanjing Process + 博特/others** | China | Roller/ball screws | Domestic incumbents pre-humanoid | shipping (industrial) | Held only ~8% each of the *China* market where 4 overseas majors (GSA/Ewellix/Rollvis/Rexroth) held ~78% CR4 (2022) — the localization gap is widest here | `secondary` |
| **Beite Technology / 贝特科技 (Shanghai, Kunshan plant)** | China | Precision planetary roller screws | Building **RMB 1.85bn (~$260M) Kunshan plant**, 2.6M PRS sets/yr, mass-production 2026 (per [Hardware](hardware.md)) | pivoting-in → shipping | The most-cited China roller-screw capacity build; validates the "China is coming for PRS" thesis. *(Distinct from 贝斯特/Best SZ300580 above — different companies, similar names)* | `secondary` |

### 2C. 无框电机 / 执行器 — Frameless torque & hollow-cup motors

| Supplier | Region | Makes | Humanoid design-wins (dated) | Commitment | Cost / localization | sq |
|---|---|---|---|---|---|---|
| **Kollmorgen / Parker / TQ Systems / Allied Motion** | US/EU | Frameless torque motors (industrial/robotics standard) | Incumbent global suppliers; feed the ecosystem | shipping | The Western frameless-motor names China is localizing against; global torque/frameless motor market >RMB 4bn (2022), ~8%/yr growth | `secondary` |
| **步科 / Kinco (Bucke, SH688160)** | China | Full frameless hollow torque-motor series, OD 50-160mm, 0.11-9.2 Nm — shoulder→wrist→neck→waist joints | A **humanoid customer's motor order surged from hundreds → thousands → ~10,000-unit level in 2025** (customer unnamed, `secondary`); company-disclosed aggregate: frameless-torque-motor sales ~83,000 units 2025 (+247.84% YoY, single-motor basis) and ~35,000 units Q1 2026 (+246.28%), described as crossing from "小批量" to "批量" orders with domestic head humanoid customers `(primary, SSE disclosure)` | shipping | Company-disclosed volume ramp (2025 ~83k units) is the concrete data point; broadest domestic frameless range | `primary` (SSE) / `secondary` (per-customer trajectory) |
| **昊志机电 / Haozhi (SZ300503)** | China | Frameless torque motors + harmonic + drives + encoders + torque sensors (full joint stack) | Widely used in cobot/lightweight robots; positioning as humanoid Tier-2 (see 2A) | sampling/qualifying | Humanoid revenue still immaterial (RMB 12.21M H1 2025) | `secondary` |
| **鸣志电器 / Moons' (SH603728)** | China | Frameless torque motors + **hollow-cup (coreless) motors** — key for dexterous-hand fingers | Positioned for hand + joint motors; hollow-cup is the hand-actuation "gold standard" | pivoting-in / sampling | Hollow-cup motor cited at **~54.5% of hand-actuator cost** — the money node inside the hand; domestic hollow-cup precision still catching up | `secondary`; `unverified` (54.5% est.) |
| **CubeMars / 江苏雷利 / 鼎智 / 微创 / 汇川 / 和创 等** | China | Frameless outrunner torque motors, hollow-cup, integrated actuators | Various cobot/quadruped/humanoid design-ins | mixed (shipping→sampling) | Crowded domestic field; 9+ A-share listed firms disclosed frameless-motor humanoid layout | `secondary` |

- **Note**: hollow-cup/coreless motors (hand fingers) and frameless torque motors (body joints) are distinct sub-nodes; the hand's hollow-cup motors are the higher-value-density node (see [tactile-hands](tactile-hands.md)). NdFeB magnet dependency (China ~90% processing) sits under all of them — see [Hardware](hardware.md) rare-earth section.

### 2D. 灵巧手 — Dexterous hands

Full depth lives in [Tactile Sensing & Dexterous Hands](tactile-hands.md); this is the supply-chain-lens summary. The hand is verticalizing into a **component tier** (AgiBot/Zhiyuan spun off its hand unit 2026; ENCOS, Xynova scaling).

| Supplier | Region | What / DoF | Humanoid design-wins | Commitment | Price / localization | sq |
|---|---|---|---|---|---|---|
| **Tesla / Figure (in-house)** | US | Optimus Gen-3 22-DoF + Figure 03 ~16-DoF, forearm-tendon | Own robots only — not sold | shipping (captive) | Vertical integration; not a merchant supplier | `secondary` |
| **Inspire Robots / 因时** | China | RH56 series ~6 active DoF, linkage; tactile configs | The volume workhorse across Chinese humanoids; ~10k hands 2025 | shipping | ~$8.9k tactile config; the low-cost default | `secondary` |
| **LinkerBot / 灵心巧手** | China | Linker Hand L20, 20 DoF, 72-cell tactile | 10,000th hand shipped 2025-12; 50k-100k targeted 2026 | shipping | RMB 49,900 (~$7k), Lite <$5k | `secondary`/`company-reported` |
| **AgiBot OmniHand / Daimon / DexRobot / PaXini** | China | 13-22 DoF, tactile-dense | AgiBot own robots + merchant; Daimon VBT+VTLA | shipping | OmniHand RMB 9,800-14,800 — cheapest credible tactile hand | `secondary`/`company-reported` |
| **Shadow / SharpaWave / Wonik Allegro / Tesollo** | UK/SG/KR | 16-24 DoF premium / research | Research + premium tier; SharpaWave in NVIDIA/Unitree H2 Plus ref design (2026-06) | shipping (premium) | Shadow ~$100k-150k; SharpaWave ~$50k — no Western vendor in the $5-10k volume tier | `secondary` |

- **Sub-node money**: hand actuation is hollow-cup motors (2C) + micro planetary/harmonic reducers (2A: 来福 13g, 丰立) + micro ball screws + fingertip tactile (2E). 丰立智能's XHAND1 win is the best-sourced *micro-reducer-into-hand* design-in — though 丰立's own 2025-03 IR record calls it small-batch delivery and states no mass-market batch supply yet. (Note: 星动 has also described XHAND1 as a *full direct-drive* 12-active-DoF hand; 丰立 supplies the small gears/reducers used in the 星动 hand family, not necessarily every SKU.)

### 2E. 六维力 / 触觉传感器 — Six-axis force & tactile sensors

High-end 6-axis F/T was historically an ATI/Schunk/AMTI import ($3k-10k+); China localized fast and now has a clear humanoid leader.

| Supplier | Region | Makes | Humanoid design-wins (dated) | Commitment | Cost / localization | sq |
|---|---|---|---|---|---|---|
| **蓝点触控 / Landot** | China | 6-axis F/T + joint-torque sensors | **~72.6% China humanoid 6-axis share** (2025 first 3 quarters); batch orders from **AgiBot/智元, Xiaomi/小米, XPeng/小鹏, Beijing Humanoid Innovation Center**; multiple single-customer 1,000+ unit shipments; **>95% of domestic joint-torque-sensor shipments**, ~70k+ sets H1 2025 | shipping | Rev doubling 3 yrs running; ~RMB 100M B-round (2025-07) + >RMB 100M C-round led by Sequoia China; the domestic 6-axis leader | `secondary` |
| **宇立仪器 / Yuli Instruments** | China | 6-axis F/T | Supplies **ankle sensors for UBTech Walker** series | shipping | Established F/T maker, diversified customers | `secondary` |
| **坤维科技 / Kunwei** | China | 6-axis F/T (high-end domestic breakthrough) | Positioned as key unlock for humanoid mass-production | shipping/qualifying | High-end domestic substitution play | `secondary` |
| **鑫精诚 / Xinprecise, 柯力传感 / Keli (SZ603662), 安培龙 / Amphenol-CN** | China | 6-axis F/T + strain/pressure | Multiple listed-company entrants ("军备竞赛") | mixed | Crowded; Keli is a large strain-gauge incumbent moving in | `secondary` |
| **ATI / Schunk / AMTI** | US/DE | Premium 6-axis F/T | Legacy industrial standard; being displaced in China humanoids on price | shipping (premium) | $3k-10k+/sensor — the import tier China is undercutting | `secondary` |

- Market context: China 6-axis shipments ~14,500 units in 2024 (+53% YoY); humanoid 6-axis shipments ~12,300 in 2025 (+510% YoY); forecast >460k by 2030. Fingertip **taxel arrays** (Unitree 94-pt, LinkerBot 72-cell, AgiBot 400+-pt) are a separate node — see [tactile-hands](tactile-hands.md).

---

## 3. China localization story — dominates vs still imports

**China dominates (domestic volume, cost-down curve running):**
- **Harmonic reducers**: 绿的 (27.5%) + 来福 (21.4%) = ~half of China's robot harmonic market by 2025 volume; priced 30-40% below HDS (~RMB 2,000 vs 3,000-4,000). This is the clearest localization win.
- **6-axis force sensors**: 蓝点触控 ~72.6% humanoid share; displaced ATI/Schunk on price inside China.
- **Dexterous hands**: Chinese vendors own the $1.4k-10k volume tier outright; no Western vendor competes there.
- **Frameless motors**: broad domestic supply (步科 ramping to ~10k-unit orders), though against a global NdFeB-magnet backdrop China also controls (~90% magnet processing).

**China still imports / lags:**
- **Planetary roller screws** 🔴 — the **strategic chokepoint**. Overseas CR4 (GSA/Rollvis/Ewellix/Rexroth) ~78% of the *China* market; domestic 南京工艺/博特 ~8% each (2022). China is racing (五洲新春 980k-unit plan → ~70k robots; 恒立/贝斯特/Beite/Kunshan 2.6M sets), but the binding constraint is **precision thread-grinding machine tools**, themselves supply-limited. Localization is the *frontier*, not done.
- **High-end RV reducers** — Nabtesco (Japan) global stronghold; 双环/环动科技 is the domestic challenger, audited customers still industrial-only, with a *claimed* (single-source, no Tesla disclosure) Optimus RV 2nd-round pass + ~4,000-unit small-batch from 2025Q4 — humanoid RV localization is claimed-early, not primary-confirmed.
- **High-precision harmonic (top tier)** — HDS keeps ~80% *global* share and the precision segment; China leads *domestic volume* but not the absolute high end.
- **Premium tactile / VBT** — SharpaWave (SG), GelSight/Digit 360 research ecosystem remain ahead on the high end.

**Cost-down curve** (mirrors the EV playbook — integrated domestic supply + huge domestic pilot pull): reducers 30-40% below Japan; a 20-DoF tactile hand fell from ~$100k (2020) to ~$7k (2025) to ~$1.4k entry (see [tactile-hands](tactile-hands.md)); Morgan Stanley pegs Chinese per-unit robot cost at ~⅓-½ of Western. See [Landscape: China](landscape-china.md).

**⚠️ Tesla-supplier claims to treat as unverified** (they circulate widely; corroboration is Chinese-media-side only, no Tesla primary disclosure):
- **拓普集团 / Top Group + 三花智控 / Sanhua** as Optimus actuator-assembly suppliers, and the reported ~$685M Sanhua actuator-component order (Mexico, 2026) — **never confirmed by Tesla or Sanhua**; Sanhua declined to comment on "market rumors" `(single-source, unverified)`. Anchored in [Optimus §supply](company-optimus.md) and [Hardware](hardware.md).
- **绿的谐波** 10,000-unit Optimus harmonic order (2026 delivery) — cross-referenced across multiple Chinese outlets but no Tesla-side disclosure `(single-source cluster, unverified)`.
- **五洲新春** Tesla-via-Bosch transmission supply — inferred from customer relationships, not confirmed `(single-source, unverified)`.

---

## 4. Read for a module maker like Quectel

The component/mechatronics layer is a **different arms-dealer lane** than Quectel's compute/connectivity-module socket. Key reads:

- **The design-win money is in mechatronics, and it is off Quectel's turf.** The big BOM nodes — reducers (~15-25%), roller screws (~15-18%), motors (~12%) — are *precision-machining and materials* businesses (thread-grinding, flexspline fatigue, NdFeB magnets), not a connectivity/compute-module competency. A module maker cannot credibly enter these; they are a decade-deep manufacturing moat owned by 绿的/来福/五洲/Nabtesco/HDS. This is **adjacent-but-off-limits**.
- **Where the layers touch: the joint/actuator *module*.** The one place mechatronics converges toward Quectel's world is the **integrated joint module** (motor + reducer + encoder + drive + sometimes torque sensor) — a "smart actuator" that increasingly wants an MCU, a comms bus, and firmware. That is *closer* to a module maker's DNA than a bare reducer, but the incumbents there (绿的 mechatronic modules, 中大力德 actuator units, 昊志 full-stack) are the *component* firms integrating upward, not module makers integrating into hardware. Quectel's realistic role stays the **compute/connectivity brain that talks to** these actuators, not the actuator itself.
- **Sensors are the nearest adjacency — but still not the socket.** 6-axis F/T and tactile sensors need signal-conditioning + edge compute + a data bus; a connectivity/compute-module vendor is *nearer* here than in reducers. But 蓝点触控 already owns ~72.6% and the value is in the strain-gauge/silicon sensing element, not the readout module. Adjacency to watch, not a wedge to force.
- **Net for Quectel**: the component supply chain confirms the [ODM Competitors](odm-competitors.md) conclusion from the other direction — the defensible arms-dealer lane is the **compute/connectivity/positioning module**, and the mechatronics BOM (where most of the money is) is a *separate* arms-dealer lane owned by precision-manufacturing specialists. The two lanes barely overlap; the overlap point (smart joint modules) is being colonized by the reducer firms, not the module firms. Quectel should sell *into* every one of these robots' brains regardless of which reducer/motor/hand vendor wins — the classic arms-dealer posture (see [ODM Opportunity](odm-opportunity.md), [Quectel pitch](../pitch/quectel.md)).

---

## 5. Watch items (dated)

| Date / horizon | Item | Why it matters |
|---|---|---|
| 2026 (delivery) | **绿的谐波** claimed 10,000-unit Optimus harmonic order | If a Tesla-side disclosure ever confirms it, it's the first hard China-harmonic-into-Optimus proof; still `unverified` |
| ~2026-03 | **HDS** Japan plant (~JPY 10.6bn) for humanoid harmonic reducers, production start | Incumbent defending the high end vs China cost-down |
| 2025-12 launch → 2026 | **Nabtesco RVmini/Monocrank** — first shipping humanoid customer? | Nabtesco filling its low-torque humanoid gap; watch for a named design-win |
| 2026 | **五洲新春 / 恒立 / 贝斯特 / Beite-Kunshan** roller-screw batch-production ramps | The chokepoint test — does China roller-screw localization hit volume vs Optimus/Figure ramps? |
| mid-2026 | **环动科技 / Finemotion** STAR Market IPO (RV reducer) + claimed Optimus RV 2nd-round pass / ~4,000-unit small-batch (2025Q4, single-source) | Domestic RV-challenger listing; watch for a *primary-confirmed* humanoid (vs audited-industrial-only) design-win |
| 2025 → 2026 | **步科 / Kinco** unnamed humanoid customer scaling to ~10k-unit frameless-motor orders | Concrete frameless-motor volume signal; watch customer reveal |
| ongoing | **蓝点触控 / Landot** ~72.6% share durability + funding (Sequoia C-round) | Whether the 6-axis leader consolidates or fragments as volumes 40× to 2030 |
| ongoing | **拓普 / 三花 Optimus actuator claims** | Widely cited, never primary-confirmed — do not repeat as fact until Tesla-side disclosure |

## Sources

Reducers (harmonic / RV):
- Company 2025 annual reports via cninfo / xueqiu; finance.sina.com.cn + huxiu.com Feb 2026 — 绿的谐波 FY2025 rev RMB 571M, NP ~RMB 124M, 425,200 units shipped `(primary)`
- caifuhao.eastmoney.com 2025-12-27 — 绿的谐波 Tesla Optimus Tier-2 audit pass + 10,000-unit 2026 order, 30-40% below HDS, "多方信源交叉验证" `(single-source cluster)`
- 来福谐波 2026 HKEX prospectus via finance.sina.com.cn / jiemian.com / stcn.com (June 2026) — 灼识咨询/CIC China harmonic share 绿的 27.5% #1 / 来福 21.4% #2 (by 2025 shipment volume; by 2025 *revenue* the split is 绿的 27.6% / 来福 12.9%); Laifu rev RMB 261M (2025, +142%), net loss RMB 171M; HK$1.0bn+ IPO 2026-06-30 `(primary)`
- caifuhao.eastmoney.com July/Sept/Aug 2025 — 中大力德 AgiBot 远征A2/灵犀X1 exclusive planetary supplier (~RMB 5,000/robot); ~63% of Unitree planetary procurement `(single-source)`; 深创投 indirect-link correction `(secondary)`
- 21jingji.com + STAR Market prospectus coverage — 环动科技/Finemotion audited customer list industrial-only (Efort/Kanop/Qianjiang/STEP/Kaierda/GSK/华中数控); zhihu.com/leaderobot.com 特斯拉备选供应商 roundup + caifuhao.eastmoney.com 2025-12 — 双环/环动 Tesla RV claim escalated from joint-development discussion to a reported Optimus 2nd-round pass + ~4,000-unit small-batch (2025Q4), no Tesla-side disclosure `(primary customer list / single-source, unverified Tesla)`
- caiwennews.com / caijing.chinadaily.com.cn — 昊志机电 H1 2025 robotics core-component rev RMB 12.21M vs RMB 703M total `(secondary)`
- file.finance.qq.com IR filing 2025-03-18 + nbd.com.cn — 丰立智能 星动纪元 XHAND1 micro-reducer batch supply `(primary)`; finance.sina.com.cn 2025-12 — XPeng supply `(secondary)`
- Nabtesco press release 2025-12-02 (RVmini/Monocrank launch, iREX2025) `(primary)`; HDS ~80% global share + ~JPY 27.5bn capex — aggregated Chinese sell-side + zhihu/leaderobot roundup `(secondary / single-source)`

Roller screws:
- https://stcn.com/article/detail/1562897.html — A-share roller-screw investment wave `(secondary)`
- https://www.21jingji.com/article/20250617/herald/05cf32584a26e6fdfc4a7e696cbf7333.html — 五洲新春 RMB 10.55bn raise, 980k planetary roller screws → ~70,000 humanoid robots `(secondary)`
- https://www.aibangbots.com/a/2259 ; https://zhuanlan.zhihu.com/p/1888515581248008960 — 30+/38 domestic screw-supplier roundups (恒立/贝斯特/南京工艺/博特) `(secondary)`
- https://interestingengineering.com/ai-robotics/china-humanoid-robots-actuators — GSA/Rollvis/Ewellix ~70%+ combined share; Tuopu/Beite advancing `(secondary)`
- https://rollvis.com/rv-planetary-roller-screws/ — Rollvis product line (GSA-owned since 2016) `(primary)`
- [Hardware](hardware.md) — Beite RMB 1.85bn Kunshan plant, 2.6M PRS sets/yr, 2026 mass-production

Frameless / hollow-cup motors:
- https://www.aibangbots.com/a/1764 ; https://www.eet-china.com/mp/a413842.html — 无框力矩电机 supplier roundups (步科/昊志/鸣志 + 9 A-share firms) `(secondary)`
- https://www.9fzt.com/common/8c85e014da61e62f419e7c81ce38c9c7.html — 步科 frameless series OD 50-160mm, humanoid customer order → ~10k-unit level 2025 `(secondary)`; finance.sina.com.cn / cls.cn 2026-05-11 — 步科 SSE-disclosed frameless-motor sales ~83k units 2025 (+247.84%), ~35k Q1 2026 (+246.28%), "小批量→批量" `(primary, SSE)`
- https://www.honest-hls.com/humanoid-robot-frameless-torque-coreless-motors — Optimus 14 linear + 14 rotary frameless; hollow-cup ~54.5% of hand-actuator cost `(secondary / unverified est.)`
- https://pdf.dfcfw.com/pdf/H3_AP202308181595067132_1.pdf — 华福/华安 motor sub-chain deep-dive `(secondary)`

Force / tactile sensors:
- https://www.stcn.com/article/detail/3514923.html ; https://36kr.com/p/3381031938352899 — 蓝点触控 ~72.6% humanoid 6-axis share (2025 3Q), AgiBot/Xiaomi/XPeng/Beijing-Humanoid orders, >95% joint-torque-sensor share, ~70k sets H1 2025, B/C-round funding `(secondary)`
- https://www.aibangbots.com/a/2708 ; https://www.aibangbots.com/a/1907 — 6-axis + torque-sensor supplier roundups (宇立/坤维/鑫精诚/柯力/安培龙); 宇立 UBTech Walker ankle sensor `(secondary)`
- https://www.sohu.com/a/920418063_121864708 — 2025 China humanoid 6-axis market report (~12,300 units 2025 +510%, ~14,500 units 2024 +53%, >460k by 2030) `(secondary)`

BOM split + Optimus reducer counts:
- https://pdf.dfcfw.com/pdf/H3_AP202409261640063356_1.pdf — Tianfeng/华安 reducer ~30-36% of rotary actuator, joints ~50-57% of BOM `(secondary / analyst estimate)`
- 机器人大讲堂 / leaderobot.com Optimus reducer breakdown (~20 harmonic + ~8 RV + ~6 planetary; ~14 roller screws; ~20 hollow-cup hand motors) `(single-source / unverified)`
- 36kr circulated Optimus BOM split (actuators ~35%, sensors+other ~20%, lead/roller screws ~18%, reducers ~15%, motors ~12%) `(single-source / unverified)` — via [Hardware](hardware.md)

Cross-links (this repo): [Hardware](hardware.md) (actuator/compute/battery overview, rare-earth chokepoint), [Tactile Sensing & Dexterous Hands](tactile-hands.md) (hand hardware + touch + hand price collapse), [ODM Competitors](odm-competitors.md) (assembly/EMS + module-maker scoreboard), [ODM Opportunity](odm-opportunity.md) (market-sizing + strategic options), [Landscape: China](landscape-china.md) (supply-chain geography), [Optimus](company-optimus.md) (Tesla BOM anchor + supplier claims), [Quectel pitch](../pitch/quectel.md) (module-maker analysis).
