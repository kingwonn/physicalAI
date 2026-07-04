---
title: "Company Deep Dive: Unitree"
slug: company-unitree
updated: 2026-07-04
confidence: verified
---
> Unitree Robotics (Hangzhou, founded 2016 by Wang Xingxing out of his master's-thesis "XDog" quadruped) is the price disruptor of Physical AI: it collapsed the quadruped price floor from ~$45K (Laikago, 2017) to $1,600 (Go2, 2023), then did the same to humanoids — H1 ~$90K (2023) → G1 from ~$13.5K (2024) → R1 from ~$4,200–5,900 (2025–26) — while staying profitable on ~60% gross margins thanks to extreme vertical integration (purchased components are only ~14–18% of cost). Its IPO prospectus shows 2025 revenue of ~RMB 1.70B (+335% YoY, ~$235M) with humanoids at 51.5% of revenue and >5,500 humanoid units shipped. As of 2026-07-04 it holds CSRC registration approval (granted 2026-07-02) for a ~RMB 4.2B (~$618M) Shanghai STAR Market IPO at an implied ~RMB 42B (~$5.9–6.2B) valuation — the A-share market's first humanoid pure-play, with pricing/subscription still ahead and a debut expected between late July and early August 2026. Counterweights: viral safety incidents (H1 "flailing" 2025-05, G1 child-kick 2026-06), a documented Go1 firmware backdoor (CVE-2025-2894), and escalating US action — a dedicated congressional hearing (2026-03), the GUARD Act and Blocking CCP Spy Tech Act bills, and addition to the Pentagon's 1260H Chinese-military-companies list (2026-06). See [Humanoids](humanoid-robots.md), [Landscape: China](landscape-china.md), [Investment](investment.md).

## Company at a glance (as of 2026-07)

| Field | Value |
|---|---|
| Founded | 2016-08-26, Binjiang District, Hangzhou (registered as Hangzhou Yushu Technology / 宇树科技) |
| Founder/CEO/CTO | Wang Xingxing (王兴兴, b. 1990, Ningbo); 23.8% direct equity, 68.78% voting rights pre-IPO |
| Headcount | ~480 employees, ~175 in R&D (prospectus, as of 2026-03) |
| 2025 revenue | ~RMB 1.70B (~$235M; Caixin cites RMB 1.69B, SCMP RMB 1.71B), +335% YoY |
| 2025 profitability | Adjusted (non-GAAP) net profit ~RMB 600M (~$84M), +674% YoY; ~60% gross margin |
| 2025 volumes | >5,500 humanoids (prospectus; Omdia counts 4,200 — methodology conflict); >30,000 quadrupeds cumulative 2022–2025-09 |
| Product lines | Go/A/B quadruped series; G1, H1/H1-2, H2, R1 humanoids; GD01 manned mecha; Dex3/Dex5 hands; LiDAR; components |
| IPO status | CSRC registration approved 2026-07-02; ~RMB 4.2B raise; pricing not yet set (as of 2026-07-04); debut expected late 2026-07 to early 2026-08 |
| Implied valuation | ~RMB 42B (~$5.9–6.2B) at ≥10% float |

## Founding story and the XDog lineage

- **2013–2015, Shanghai University**: during his mechanical-engineering master's, Wang Xingxing built **XDog**, a low-cost electric-motor quadruped, betting that small, electrically driven legged robots (not Boston Dynamics-style hydraulics) were the scalable path. He deferred graduation in 2015 to enter XDog in a robot design competition, winning second place and an RMB 80,000 prize.
- XDog videos went viral in Chinese tech media; buyers and investors approached him before he had a company.
- **2016**: after a brief stint at DJI in Shenzhen, Wang quit at age 26 and registered **Hangzhou Unitree Technology Co., Ltd.** on 2016-08-26 in a ~50 m² office in Hangzhou's Binjiang district, funded by angel money that followed the XDog videos.
- The founding thesis — cheap, mass-manufacturable electric actuation + in-house everything — has never changed; it later transferred directly from quadrupeds to humanoids. Wang is now also a vice-chair of MIIT's national humanoid standards committee (TC08, est. 2025-12) and sat front-row at Xi Jinping's private-sector symposium (2025-02) — see [Key people](key-people.md) and [Safety & regulation](safety-regulation.md).

## Product line evolution — quadrupeds

| Model | Launch | Launch/list price | Notes |
|---|---|---|---|
| Laikago | 2017 | ~$45K | First product; proof that electric quadrupeds could be sold at all; discontinued |
| Aliengo | 2019 | research-grade (n/d) | Perception + payload upgrade for labs |
| A1 | 2020 | <$10K | First sub-$10K performance quadruped |
| Go1 | 2021 | from ~$2,700 | First consumer-priced robot dog; mass adoption in universities |
| B1 | 2021 | industrial (n/d) | Industrial line debut (inspection, IP68) |
| Go2 | 2023-07 | from $1,600 (Air); $2,800 (Pro); EDU tiers to ~$22.5K | Built-in LiDAR + LLM voice integration at consumer price |
| B2 / B2-W | 2023 (B2); wheeled B2-W later | US store list $100K (as of 2026-07) | 6 m/s industrial platform; B2-W wheel-leg videos went viral 2025 |
| A2 | 2025-08 (unveiled ~2025-08-06/07, a week after R1) | no launch price disclosed; reseller pre-orders took $3K deposits for early-2026 delivery; US store list $100K (as of 2026-07) | "Stellar Explorer" industrial/inspection flagship; dual front/rear LiDAR, 5 m/s, 25 kg walking / 100 kg standing payload, 20 km unloaded range |

- Unitree is routinely credited with ~60–70% of global quadruped-robot shipments (secondary reports, unverified); quadrupeds were the majority of revenue until 2025, when humanoids overtook them for the first time.
- Quadruped unit manufacturing cost fell from ~$3,300 (2022) to ~$1,800 (mid-2025) per the prospectus — the template for humanoid cost-down.

## Product line evolution — humanoids

| Model | Launch | Price | Notes |
|---|---|---|---|
| H1 | 2023-08 | ~RMB 650K (~$90K) | Then the cheapest full-size humanoid; Guinness speed record 3.3 m/s (2024-03), later 4.78 m/s in competition (2025-08); first electric full-size backflip (company claim) |
| H1-2 | 2024 | n/d | Upgraded joints/perception for research fleets |
| G1 | 2024-05 | from RMB 99K (~$13.5K official); EDU variants to ~$73.9K | 1.32 m / ~35 kg, 23–43 DoF; the de-facto global research humanoid; collapsed the humanoid price floor |
| R1 | 2025-07-25 | RMB 39,900 (~$5,900); R1 Air repriced RMB 29,900 (~$4,200) 2026-06; dual-arm modular variant from $4,290 | 1.21 m / ~25 kg, ~26 DoF; TIME Best Inventions 2025; cheapest humanoid on the market |
| H2 | 2025-10 | tiered (resolved 2026-07-04): $29.9K official standard direct (no dexterous hands, no secondary development); $40.9K US/CA distributor "Commercial" (no SDK, 8-mo warranty) / $68.9K EDU; H2 Plus $100K (shop.unitree.com) | 1.8 m (official) / ~70 kg (unverified), 31 DoF (3-DoF waist, 2-DoF neck); 360 N·m peak leg torque; bionic-face option; hands sold separately (Dex3-1/Dex5-1) |

- Optional **Dex5-1** 20-DoF dexterous hand (94-point tactile array @1 kHz) and the NVIDIA/Unitree **H2 Plus reference design** with Sharpa visuo-tactile hands (2026-06) — see [Tactile & hands](tactile-hands.md) and [Hardware](hardware.md).
- **GD01 manned mecha (unveiled 2026-05-12)**: a ~500 kg (with pilot) rideable "transformable civilian vehicle" that walks on two legs and can lean back into a quadruped crawl mode; Wang Xingxing piloted it in the launch video (which also showed it smashing through a brick wall with its arms). Priced from RMB 3.9M (~$574K; Unitree's international listing says "from $650,000"). Marketed as the world's first mass-produced manned mecha (company claim); minimal technical detail published beyond the ~1-minute demo — a halo/brand product rather than a volume line (as of 2026-07).
- 2026 shipment target: up to **20,000 humanoids** — Wang's stated range was 10,000–20,000 units in a post-Gala 36Kr interview (2026-02), reiterated in press through 2026-04; 5-year capacity plan: 75,000 humanoids + 115,000 quadrupeds per year (prospectus).

## Price-disruption strategy

- **Fleet-average humanoid ASP fell ~72% in two years** — ~RMB 593,400 (~$85K, 2023) → ~RMB 167,600 (~$25K, 2025) — while gross margin *rose* to ~60% (prospectus). Price cuts are cost-curve-led, not subsidy-led.
- Humanoid unit manufacturing cost fell from ~$10,800 to ~$9,200 (2022→mid-2025); quadruped cost nearly halved (prospectus figures via analyst coverage).
- The ladder is deliberate: a sub-$2K quadruped and sub-$5K humanoid seed the developer/education base; EDU tiers ($20–74K) monetize labs; industrial quadrupeds ($100K) and H2 monetize enterprises. Every rung feeds training data, developer mindshare, and component volume back into the stack.
- Each launch resets the market floor and forces competitor repricing (EngineAI PM01 ~$12K, Booster K1 ~$6K) — the EV/drone playbook applied to humanoids. See [Landscape: China](landscape-china.md) for sector-wide dynamics.

## 2025 financials (IPO prospectus, as of 2026-03)

| Year | Revenue | Notes |
|---|---|---|
| 2022 | RMB 123M | quadruped-dominated |
| 2023 | RMB 159M | humanoids just 1.9% of revenue |
| 2024 | RMB 392M | H1/G1 ramp; adjusted profit turns meaningfully positive |
| 2025 | ~RMB 1.69–1.71B (~$235M) | +335% YoY; **humanoids 51.5% of revenue** — overtaking quadrupeds for the first time |

- **Profitability**: 2025 adjusted (扣非) net profit ~RMB 600M, +674% YoY (implying ~RMB 78M in 2024); GAAP net margin ~18%, adjusted ~35% (single analyst source, unverified). Wang has claimed the company has been profitable since 2020 (company claim, unverified for pre-2022 years). This makes Unitree the rare profitable humanoid maker — UBTech lost RMB 790M in 2025; Western peers burn venture capital. See [Investment](investment.md).
- **Customer mix (2025 humanoid revenue)**: research/education ~74%, commercial/consumer ~17%, industrial ~9% — i.e., today's humanoid business sells to labs, not factories. Quadrupeds skew more commercial (>40%) with customers incl. State Grid, China Southern Power Grid, PetroChina, Sinopec, and JD.com (largest customer).
- **Geography**: overseas sales exceeded **55% of revenue in each of 2022–2024**, falling to **39.2% in 2025** (domestic 60.8%) — the first year domestic revenue overtook exports, though exports still more than doubled in absolute terms. The prospectus's own conservative phrasing is that overseas revenue exceeded 35% in every reporting-period year. Significant US academic base (international shipments since 2018).
- **Share-count caveat**: prospectus claims 32.4% of 2025 global humanoid shipments (>5,500 units); Omdia credits Unitree with 4,200 units (#2 behind AgiBot's 5,168) on a ~13,000-unit global total. The counts cannot share a methodology — treat all 2025 share figures as methodology-dependent (see [Humanoids](humanoid-robots.md)).

## STAR Market IPO — status as of 2026-07-04

| Date | Event |
|---|---|
| 2025-06 | Series C ~RMB 700M at >RMB 12B (~$1.7B) post — Alibaba, Tencent, Ant, Geely, China Mobile fund, HongShan, Jinqiu. Largest outside shareholder is Meituan: **9.65% combined** via Hanhai Information (7.61%), Chengdu Longzhu (1.02%) and Galaxy Z (1.02%) per the prospectus — built from its 2024-02 Series B2 lead at ~RMB 3.1B valuation; HongShan (Sequoia China) next at 7.11% |
| 2025-07 | IPO tutoring begins with CITIC Securities (lead underwriter/sponsor) |
| 2026-03-20 | SSE accepts STAR Market filing: ~RMB 4.202B raise, ≥40.446M shares (≥10% float) |
| 2026-06-01 | SSE Listing Committee approval — first "embodied AI" company cleared for A-shares |
| 2026-07-02 | **CSRC registration approved** — 104 days filing-to-registration, among the fastest on record |
| next | Underwriting plan, price discovery, online subscription (T/T+1/T+2 process); **no offer price or subscription date announced as of 2026-07-04** |
| expected | Debut late 2026-07 to early 2026-08 (press expectation, unverified) |

- Implied valuation at the planned raise/float: ~**RMB 42B (~$5.9–6.2B)** — modest against US comps (Figure at $39B with no disclosed revenue) given Unitree's ~$235M revenue and actual profits.
- **Use of proceeds** (four projects): robot AI-model R&D (~half of proceeds — ~$300M over 3 years for model training), robot-body R&D, new product development, and a smart-manufacturing base to deepen vertical integration.
- Strategic read: A-share listing gives China's humanoid champion a domestic war chest and retail-investor halo insulated from US capital-market restrictions; it also forces the sector's first audited humanoid unit economics into the public record. See [Investment](investment.md).

## Vertical integration and supply chain

- Unitree self-designs and manufactures most critical components: high-torque joint motors, precision reducers, encoders, joint modules, controllers, force sensors, dexterous hands, LiDAR, and cameras. **Purchased components are only ~14–18% of total cost** (prospectus); outsourcing is limited to commodity parts (battery cells, flash storage) and the core compute board.
- Actuation is 40–60% of a humanoid BOM industry-wide ([Hardware](hardware.md)); building it in-house is the stated source of Unitree's ~60% gross margin and pricing power.
- Domestic sourcing rate >90%, with suppliers concentrated in the Yangtze River Delta within a ~2-hour logistics radius of Hangzhou — the mirror image of US makers' ~70% dependence on Chinese components (see [Landscape: China](landscape-china.md)).
- IPO proceeds fund a new manufacturing base for modular, flexible production across humanoid and quadruped platforms — capacity ahead of the 20K/75K unit targets.

## Viral milestones

| Date | Event |
|---|---|
| 2021-02 | 24 ox-costumed Unitree quadrupeds dance at CCTV Spring Festival Gala — first Gala appearance |
| 2025-01 | H1 humanoids perform yangko folk dance (twirling handkerchiefs) at the Spring Festival Gala — wobbly but a national sensation (~1B+ audience event) |
| 2025 (H1) | G1 kung-fu demo videos: standing side-flip, kip-up, 720° spin-kick (company demo videos) |
| 2025-04-19 | Beijing robot half-marathon: a third-party-operated G1 falls at the start and goes viral; Unitree issues a statement that it **did not officially enter** and was focused on a combat-livestream project |
| 2025-05 | "Unitree Iron Fist King" — world-first humanoid kickboxing livestream with G1 units (Hangzhou; teleoperated) |
| 2025-08 | World Humanoid Robot Games (Beijing): Unitree tops medal haul with 11 medals incl. 4 golds; H1 hits 4.78 m/s — see [Locomotion](locomotion.md) |
| 2026-02 | Third Spring Festival Gala appearance: dozens of G1s in the first fully autonomous humanoid cluster kung-fu performance (Drunken Fist, nunchaku, parkour, ~3 m launched aerial flip); H2 as armored Monkey King riding B2-W "clouds" |
| 2026-04 | Unitree humanoid breaks the human 1,500 m world record in robot half-marathon qualifying (Xinhua/People's Daily, state media) |

- The Gala arc (2025 wobbly dance → 2026 autonomous cluster kung-fu) is the most-watched public benchmark of Chinese locomotion iteration speed; it doubles as brand-building for the IPO retail audience.

## Safety incidents

- **H1 "flailing" incident (2025-05, viral)**: a crane-suspended H1 thrashed violently near workers; attributed to running a full-body policy with feet not load-bearing. No serious injury; canonical clip in humanoid-safety debates.
- **G1 kicks a child (video shared 2026-06-04)**: a wig-wearing G1's roundhouse kick struck a child in the stomach during a public demo in China; Chinese media reported no serious injury. Renewed scrutiny of performance-mode robots around crowds.
- Context: Unitree sits on the committee writing China's humanoid safety standards (Wang is a TC08 vice-chair) — manufacturers holding the pen is a noted structural conflict. See [Safety & regulation](safety-regulation.md).

## US security scrutiny and procurement exposure

| Date | Event |
|---|---|
| 2025-03/04 | **CVE-2025-2894**: researchers document a pre-installed remote-access tunnel ("CloudSail") in Go1 firmware — an effective backdoor; units at MIT, Princeton, CMU potentially exposed; Unitree deactivates the service |
| 2025-09-20 | **"UniPwn" BLE exploit publicly disclosed** by researchers Andreas Makris (Bin4ry) and Kevin Finisterre: the BLE Wi-Fi-config interface uses a hardcoded encryption key/IV, accepts any handshake secret containing "unitree", and passes unsanitized input to root shell scripts — giving proximity attackers root on Go2, B2, G1, H1, and wormable robot-to-robot (CVE-2025-60017/-60250/-60251). Reported to Unitree 2025-05; unpatched at publication; Unitree statement (2025-09-29, LinkedIn) claimed the "majority of fixes" were complete. Separately, researchers report G1 transmitting multi-modal sensor/telemetry data to servers in China without operator notification (research claim, unverified) |
| 2026-03-17 | House Homeland Security subcommittee hearing "DeepSeek and Unitree Robotics" on CCP-linked robotics risks |
| 2026-05-20 | **Blocking CCP Spy Tech Act** (S.4586) introduced (Sens. Scott, Cotton): names Unitree among Hangzhou's "six little dragons"; would trigger an investigation that could add it to the FCC Covered List |
| 2026-06-04 | **GUARD Act** (H.R.9129) introduced (Moolenaar/Obernolte/McClellan): mandates national-security review of adversary-state humanoid/quadruped robots, with import bans via the FCC Covered List (automatic listing if no determination within one year) |
| 2026-06-08 | Pentagon adds Unitree to the **1260H list** of "Chinese military companies" (65 additions, 188 total; listing basis: indirect SASAC ownership/affiliation); FY24 NDAA bars DoD **direct contracts** with listed entities from 2026-06-30, indirect from 2027-06-30 |

- Exposure assessment: DoD was never a customer, but US universities and developers are — the heart of Unitree's export base (overseas >55% of revenue 2022–2024, 39.2% in 2025). The realistic risk is contagion from DoD listing to federal research-grant restrictions, state-level bans, and import prohibition under a passed GUARD Act — none of which had occurred as of 2026-07 (bills not enacted). The prospectus flags overseas trade friction as a risk factor.
- Unitree's public response: newer models are claimed more secure; no independent security audit of its humanoids has been published (as of 2026-07).

## Distribution and developer ecosystem

- **Channels**: direct web store (shop.unitree.com), Amazon (G1 listed at $17,990) and AliExpress (R1 Air international debut 2026-06 at ~$4,900), plus a global reseller network (RobotShop, RoboStore, MyBotShop and others) — consumer-electronics-style distribution no Western humanoid maker matches.
- **De-facto research standard**: G1/Go2 are the default embodiments in academic RL/VLA papers and in NVIDIA's GR00T demos; sub-$20K pricing made them the "Raspberry Pi of humanoids." See [State of the art](state-of-the-art.md).
- **Open-source stack** (github.com/unitreerobotics): `unitree_ros`, `unitree_rl_gym` (Isaac Gym sim2sim/sim2real workflows for Go2/H1/H1-2/G1), `unitree_rl_lab` (IsaacLab), `unitree_rl_mjlab` (MuJoCo) — lowering the barrier for labs to train and deploy policies. See [Simulation](simulation.md).
- **Models**: open-sourced **UnifoLM-WMA-0** (world-model–action architecture doubling as a synthetic-data engine — see [World models](world-models.md)) and **UnifoLM-VLA-0** (manipulation VLA — see [VLA models](vla-models.md)). The strategy: win the body, commoditize the ecosystem, and use IPO proceeds (~$300M for model training) to close the software gap with US model-first labs.
- **WVLA 2.0 demo (video 2026-05-25)**: Unitree showed a G1 running its "WVLA 2.0" model — described as coupling world-model (WMA) prediction with VLA action generation — autonomously completing six consecutive tidy-up tasks in a deliberately disturbed conference room with no teleoperation; reported perception stack fuses a RealSense depth camera, Livox MID360 LiDAR, and two lateral cameras (company demo + Chinese media coverage, unverified). Positions Unitree's in-house autonomy against the "labs awaiting real autonomy" critique above.
- Roughly half of IPO proceeds going to AI-model R&D signals Unitree knows hardware alone won't hold the moat — its own prospectus shows 74% of humanoid revenue still comes from research/education buyers awaiting real autonomy.

## What to watch (as of 2026-07-04)

- IPO pricing announcement and subscription dates (imminent); first-day pop as sentiment gauge for the ~10 Chinese humanoid IPOs queued behind it (AgiBot, Galbot, EngineAI…).
- Whether 2026 humanoid shipments approach the 20,000 guidance (vs >5,500 in 2025).
- H2 international pricing and whether industrial customers materialize beyond research/education (the 9% industrial share is the number to move).
- GUARD Act / Blocking CCP Spy Tech Act progress — enactment would formalize US market closure.
- Independent security audits of G1/H2 firmware; any recurrence of crowd-adjacent safety incidents.

## Sources

- https://en.wikipedia.org/wiki/Wang_Xingxing — founder biography, Shanghai University, DJI stint
- https://www.ourchinastory.com/en/14416/Unitree-founder-Wang-Xingxing:-A-post-90s- — XDog development 2013–15, competition second place + RMB 80K prize, deferred graduation
- https://en.wikipedia.org/wiki/Unitree_Robotics — founding registration 2016-08-26, Binjiang Hangzhou, 50 m² office
- https://www.caixinglobal.com/2026-07-03/unitree-robotics-wins-approval-for-618-million-star-market-ipo-102460136.html — CSRC registration approval 2026-07-02; ¥4.2B raise; revenue history 2022–2025 (¥1.69B in 2025)
- https://news.futunn.com/en/post/75500836/robotics-sector-surges-unitree-technology-s-star-market-ipo-registration — 104-day filing-to-registration; pricing/subscription next; possible late-July debut
- https://finance.sina.com.cn/stock/marketresearch/2026-07-02/doc-inifmrtq5804408.shtml — ≥40.4464M shares, ~¥42B implied valuation, subscription mechanics, listing expected mid/late-July–early-August
- https://www.caixinglobal.com/2026-03-21/unitree-robotics-files-for-608-million-star-market-ipo-102425491.html — IPO filing accepted 2026-03-20
- https://restofworld.org/2026/unitree-china-humanoid-robot-shanghai-ipo/ — prospectus: ASP fall $85K→$25K, >5,500 humanoids, 32.4% share claim, 480 staff/175 R&D, 75K/115K capacity plan
- https://www.scmp.com/business/banking-finance/article/3347365/chinas-unitree-robotics-rides-humanoid-tide-it-targets-us610m-ipo — RMB 1.71B 2025 revenue (+335%), adjusted net profit ~RMB 600M (+674%)
- https://www.scmp.com/tech/article/3347611/inside-unitrees-landmark-ipo-what-know-about-chinas-humanoid-giant — Wang 23.8% equity, 68.78% voting rights
- https://hellochinatech.com/p/unitree-ipo-humanoid-robotics-really-sells — humanoids 51.5% of 2025 revenue (vs 1.9% in 2023); ~35% adjusted margin
- https://www.tanayj.com/p/unitrees-ipo-filing-the-state-of — customer mix (74/17/9 humanoid; JD.com largest customer), purchased components 14–18% of cost, unit-cost declines, international >55% of revenue for most of company history, ~$300M IPO proceeds to AI training
- https://eu.36kr.com/en/p/3731404085015046 — prospectus deep-dive: overseas revenue >55% in each of 2022–2024; 2025 split 60.8% domestic / 39.2% overseas
- https://kraneshares.com/a-complete-guide-to-unitree-robotics-2026-ipo-why-it-matters-for-star-market-etf-kstr-humanoid-robotics-etf-koid/ — Series C (RMB 12.7B post, 2025-06) and investor list
- https://technode.com/2026/06/02/unitree-ipo-approved-meituan-backed-group-emerges-as-top-shareholder/ — Meituan-backed entities 9.65% combined, largest external shareholder; HongShan 7.11%
- https://eu.36kr.com/en/p/3835853052392576 — Meituan stake breakdown per prospectus: Hanhai Information 7.61% + Chengdu Longzhu 1.02% + Galaxy Z 1.02%; Series B2 lead 2024-02 at ~RMB 3.1B valuation
- https://www.bloomberg.com/news/articles/2025-07-25/china-s-unitree-r1-is-a-humanoid-robot-costing-less-than-6-000 — R1 launch 2025-07-25 at RMB 39,900
- https://www.scmp.com/tech/article/3349489/chinas-unitree-debut-cheapest-humanoid-robot-globally-alibaba-site-sources — R1 Air repriced RMB 29,900; AliExpress international debut (2026-06)
- https://www.humanoidsdaily.com/news/unitree-expands-r1-lineup-with-dual-arm-modular-platform-starting-at-4-290 — R1 dual-arm modular variant from $4,290
- https://www.unitree.com/g1/ — G1 official specs and from-$13.5K pricing
- https://www.humanoidsdaily.com/news/unitree-unveils-h2-humanoid-successor-to-h1 — H2 unveiling (2025-10), 180 cm/70 kg
- https://robohorizon.com/en-us/news/2025/11/unitree-h2-price-and-limitations/ — H2 $29.9K base-config caveats; domestic-market pricing; hands sold separately
- https://shop.unitree.com/ — current US store prices: B2 $100K, A2 $100K, Go2 from $1,600 (as of 2026-07)
- https://roboticsandautomationnews.com/2025/08/07/unitree-unveils-new-a2-quadruped-robot-with-100-kg-load-capacity-and-20-km-range/93591/ — A2 unveiled 2025-08-07: 100 kg standing load, 20 km range
- https://www.therobotreport.com/unitree-launches-a2-quadruped-equipped-with-front-and-rear-lidar/ — A2 launch (article 2025-08-08, "this week", a week after R1); dual LiDAR specs; no launch pricing disclosed
- https://spectrum.ieee.org/quadruped-robot-unitree-go2 — Go2 launch at $1,600 with LiDAR
- https://www.inceptivemind.com/unitree-a1-latest-quadruped-robot-costs-less-10k/13054/ — A1 under $10K (2020)
- https://www.i-programmer.info/news/169-robotics/14640-unitree-go1.html — Go1 from ~$2,700 (2021)
- https://www.mybotshop.de/Unitree_1 — Laikago ~$45K original price, discontinued
- https://www.prnewswire.com/news-releases/kung-fu-meets-spring--unitree-spring-festival-gala-robots-present-cyber-real-kung-fu-in-the-year-of-the-horse-302689291.html — 2026 Gala official PR: third Gala appearance, autonomous G1 cluster kung fu, H2 Monkey King on B2-W
- https://www.globaltimes.cn/page/202602/1355439.shtml — 2026 Gala: parkour, Drunken Fist, nunchaku after 2025 yangko dance
- https://www.cnbc.com/2026/02/20/china-humanoid-robots-spring-festival-gala-unitree-tesla-ai-race.html — Gala arc from 2025 stumbles to 2026 kung fu
- https://www.globaltimes.cn/page/202504/1332429.shtml — 2025 half-marathon; Unitree statement on third-party-operated G1 fall and non-participation; combat-livestream project
- https://english.news.cn/20260419/9653ab0720774bfc8b150bd3775b3ec6/c.html — Unitree humanoid beats human 1,500 m world record in 2026 marathon qualifying (state media)
- https://www.cnbc.com/2025/08/18/world-humanoid-robot-games-china-tesla-unitree.html — World Humanoid Robot Games 2025-08; Unitree medal haul
- https://roboticsandautomationnews.com/2025/05/08/ai-robot-attacks-worker-viral-video-shows-unitree-humanoid-going-berserk/90524/ — H1 flailing incident (2025-05) and cause
- https://interestingengineering.com/ai-robotics/viral-humanoid-robot-kicks-child-in-stomach — G1 child-kick incident (2026-06)
- https://www.axios.com/2025/04/01/threat-spotlight-backdoor-in-chinese-robots-future-of-cybersecurity — Go1 CloudSail backdoor (CVE-2025-2894); MIT/Princeton/CMU exposure
- https://oecd.ai/en/incidents/2025-05-05-0a57 — lawmaker warnings on Unitree backdoor; G1 telemetry and BLE-vulnerability claims
- https://spectrum.ieee.org/unitree-robot-exploit — UniPwn: Makris/Finisterre, disclosure timeline (vendor contacted 2025-05, public 2025-09-20), Unitree LinkedIn response 2025-09-29
- https://github.com/Bin4ry/UniPwn — UniPwn PoC repo: hardcoded key/IV, "unitree" handshake bypass, root command injection, wormability
- https://github.com/advisories/GHSA-cmhh-362m-7qph — CVE-2025-60017: root OS command injection on Go2, G1, H1, B2 via Wi-Fi-config parameters
- https://www.congress.gov/119/meeting/house/118982/witnesses/HHRG-119-HM08-Wstate-DoshiPhDR-20260317.pdf — House Homeland Security hearing "DeepSeek and Unitree Robotics" (2026-03-17)
- https://chinaselectcommittee.house.gov/media/press-releases/moolenaar-obernolte-mcclellan-introduce-legislation-to-ban-dangerous-chinese-robots — GUARD Act introduction
- https://dronelife.com/2026/06/04/congress-introduces-guard-act-extending-fcc-covered-list-framework-to-robotics/ — GUARD Act introduced 2026-06-04; FCC Covered List mechanism, one-year automatic listing
- https://www.rickscott.senate.gov/2026/5/sen-rick-scott-introduces-bill-to-restrict-ccp-aligned-companies-access-to-american-markets — Blocking CCP Spy Tech Act (S.4586, 2026-05): names Unitree among the "six little dragons"; FCC Covered List investigation
- https://www.wilmerhale.com/en/insights/client-alerts/20260611-pentagon-adds-65-new-entities-to-the-1260h-list-of-chinese-military-companies — 1260H update 2026-06-08: 188 entities; DoD contract bans from 2026-06-30/2027-06-30
- https://thenextweb.com/news/pentagon-1260h-alibaba-baidu-byd-unitree-chinese-military — Unitree added to 1260H; SASAC-affiliation listing basis
- https://www.forbes.com/sites/jonmarkman/2026/04/27/unitree-g1-humanoid-robots-are-reshaping-the-robotics-investment-stack/ — 20,000-unit 2026 humanoid shipment target
- https://www.scmp.com/tech/big-tech/article/3343825/kung-fu-somersaults-and-scale-unitree-eyes-20000-robot-output-2026-after-gala — Wang's 10,000–20,000-unit 2026 guidance (36Kr interview, 2026-02)
- https://www.prnewswire.com/news-releases/omdia-ranks-agibot-no1-worldwide-in-humanoid-robot-shipments-in-2025-302656788.html — Omdia 2025 count: Unitree 4,200 units vs AgiBot 5,168
- https://github.com/unitreerobotics — open-source org: unitree_ros, unitree_rl_gym, unitree_rl_lab, unitree_rl_mjlab
- https://github.com/unitreerobotics/unifolm-world-model-action — UnifoLM-WMA-0 open world-model–action architecture
- https://roboticsandautomationnews.com/2026/06/09/sharpa-brings-dexterous-robot-hands-to-nvidia-and-unitree-humanoid-reference-design/102424/ — NVIDIA/Unitree H2 Plus reference design with Sharpa hands (2026-06)
- https://cnevpost.com/2026/05/12/unitree-unveils-manned-mecha-gd01/ — GD01 unveiling 2026-05-12: RMB 3.9M/~$574K, ~500 kg with pilot, biped↔quadruped transform, Wang piloted, "transformable civilian vehicle"
- https://english.news.cn/20260512/715d3be8a90e4bc29ea081a2954bf9b0/c.html — Xinhua: "world's first manned transformable robotic vehicle" (state media)
- https://www.scmp.com/tech/tech-trends/article/3353262/real-life-transformers-chinas-unitree-debuts-mecha-robot-shifts-2-legs-4 — SCMP independent coverage: GD01 biped-to-quadruped transform, launch details
- https://www.youtube.com/watch?v=oWOyUMJWptc — Unitree official GD01 video, "from $650,000" international pricing
- https://www.youtube.com/watch?v=zqqIpVsMYkE — WVLA 2.0 conference-room cleanup demo (company video, 2026-05-25)
