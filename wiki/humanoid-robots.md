---
title: Humanoid Robots Landscape
slug: humanoid-robots
updated: 2026-07-04
confidence: verified
---
> As of mid-2026 the humanoid robot industry has crossed from demos into early mass production: forecasts converge on ≥50,000 units shipped globally in 2026 (Morgan Stanley's China-only forecast was raised from 14K to 50K during the year), Chinese vendors lead on volume (AgiBot passed its 10,000th cumulative unit in 2026-03; Unitree targets up to 20,000 shipments), Figure 03 and Apptronik Apollo are working real shifts at BMW and Mercedes-Benz, Agility Robotics is going public via a $2.5B SPAC with $300M in contracted Digit v5 orders, Hyundai plans 25,000+ Boston Dynamics Atlas units in US plants from 2028, Tesla is converting Fremont's Model S/X line to build Optimus V3, and 1X opened $20K consumer pre-orders for NEO. Prices now span ~$4,300 (Unitree R1 variant) to $100K+ (Western industrial platforms), with commercial-grade BOM estimated at ~$46K/unit on Chinese supply chains vs ~$130K without.

## Market snapshot (as of 2026-07)

- **Volume inflection**: 2025 closed with **~13.3K (Omdia) to ~18K (IDC)** humanoids shipped worldwide depending on tracker (see the reconciliation table in [State of the art](state-of-the-art.md)); 2026 forecasts cluster at or above **50,000 units**, overwhelmingly built in China. Morgan Stanley raised its 2026 China shipment forecast twice — 14K (2026-01) → 28K (spring) → **50K (2026-06)**.
- **2025 shipment leaders**: AgiBot **5,168 units** (Omdia #1, 39% share), Unitree **4,200 per Omdia (#2)** — though Unitree's own IPO prospectus claims **>5,500** and the top spot (sources conflict); UBTech **>500** industrial units. Morgan Stanley puts Chinese makers at **>80%** of global volume; one 2026-06 report claims ~90% (unverified aggregate). See [Landscape: China](landscape-china.md).
- **Two distinct markets**: industrial/logistics (Digit, Apollo, Atlas, Walker S2, Figure-at-BMW) and home/consumer (1X NEO, Figure home push, Tesla's long-term pitch).
- **Capital concentrates in the US**: Figure **>$1B Series C at $39B post-money** (2025-09); Apptronik **$520M at ~$5B** (2026-02, Series A total >$935M); Agility **$2.5B pre-money SPAC** (2026-06-24); Unitree **~$618M Shanghai STAR IPO** — listing committee cleared 2026-06-01, CSRC registration approved 2026-07 — at ~RMB 42B (~$6.2B) valuation. See [Investment](investment.md).
- **Long-range forecasts**: Goldman Sachs $38B market by 2035; Morgan Stanley $5T by 2050 with consumer-era prices of $15–50K.
- **Software is the moat**: hardware specs are converging; differentiation shifts to VLA/foundation-model stacks (Figure Helix, Google DeepMind models on Atlas and Apollo, XPeng VLA 2.0, 1X Redwood). See [VLA models](vla-models.md) and [State of the art](state-of-the-art.md).
- **RaaS is the dominant industrial business model**: GXO signed the industry's first multi-year humanoid RaaS contract (Agility, 2024); Schaeffler, Toyota Canada, Mercado Libre followed; 1X pioneered the consumer subscription ($499/mo).

## Platform comparison table (as of 2026-07)

Specs from official pages where available, otherwise press coverage; volatile figures stamped or marked.

| Platform | Maker (country) | Height / weight | DoF | Payload | Price | Status |
|---|---|---|---|---|---|---|
| Optimus V3 (Gen 3) | Tesla (US) | ~1.73 m / ~57 kg | ~28 body actuators + 22-DoF hands (unverified) | ~20 kg (unverified) | target $20–30K; build cost est. $50–100K+ | several hundred deployed internally "primarily for learning" (Musk, Q4'25 call 2026-01-28); a ">1,000 on the floor" figure is aggregator-only, no primary source (unverified); Fremont line start ~2026-08; no external sales before 2027 |
| Figure 03 | Figure (US) | 5'8" (~1.73 m) / 61 kg (official) | Helix drives ~25 body actuators; multi-DoF hands, 3 g tactile fingertips | 20 kg (official) | not sold; ~$25/robot-hr at BMW (reported); ~$20K consumer target (unverified) | BMW Spartanburg commercial; BotQ at ~1 robot/hour, >350 units built (official, 2026-05) |
| Atlas (electric) | Boston Dynamics (US/Hyundai) | ~1.5 m / ~89 kg (unverified) | 56 (reported) | 30 kg sustained / 50 kg burst (unverified) | not for sale | 2026 output fully committed to Hyundai RMAC + Google DeepMind; Metaplant work from 2028 |
| Digit v5 | Agility Robotics (US) | ~1.75 m | — | ~16 kg (v4) | RaaS (undisclosed) | 65,000+ hrs across 9 customer sites; $300M contracted v5 orders |
| Apollo | Apptronik (US) | 1.73 m / ~73 kg | — | 25 kg | undisclosed | Pilots at Mercedes-Benz, GXO, Jabil; commercial delivery from 2027 |
| NEO | 1X (NO/US) | ~1.68 m / 30 kg | 22-DoF hands; tendon-driven body | carries ~25 kg, lifts 68 kg | **$20K or $499/mo** | Consumer pre-orders (2025-10); US home deliveries 2026, teleop-assisted |
| G1 | Unitree (CN) | 1.32 m / ~35 kg | 23–43 | ~2–3 kg/arm | from **$13.5K** (official); EDU to $73.9K | De-facto global research platform; 2 m/s, ~2 h battery |
| H2 | Unitree (CN) | 1.8 m (official) / ~70 kg (weight unverified) | 31 (official) | — | from **$29.9K** (official base, direct: no dexterous hands, no secondary development); $40.9K "Commercial" / $68.9K EDU via US-CA distributors; H2 Plus $100K (official) | Launched 2025-10; bionic face option |
| R1 | Unitree (CN) | ~1.21 m / ~25 kg | ~26 | light | from **$4,290–5,900** | Launched 2025-07; TIME Best Inventions 2025; collapsed the hobby/research price floor |
| Expedition A2 / A3 | AgiBot / Zhiyuan (CN) | A2 ~1.69 m | — | — | ~$100K class (A2, reported) | 10,000th cumulative unit 2026-03; logistics, retail, service |
| Walker S2 | UBTech (CN) | ~1.76 m | — | — | ~$150K class (unverified) | Mass delivery since 2025-11; BYD, Foxconn, Geely, FAW-VW, BAIC, SF Express; >RMB 800M orders |
| IRON (next-gen) | XPeng (CN) | 1.78 m / 70 kg | **82** (22/hand) | — | est. ~$150K (unverified) | 3× Turing chips (2,250–3,000 TOPS reported), solid-state battery; mass production target late 2026 |
| GR-3 | Fourier (CN) | 1.65 m / 71 kg | 55 | GR-line up to 50 kg patient support | undisclosed | "Care-bot" for healthcare/companionship; ~300 units shipped cumulative (unverified) |
| Galbot G1 | Galbot (CN) | wheeled base + dual arm | — | — | ~$87K est. (unverified) | Retail/pharmacy in 30+ cities; CATL, Bosch pilots; $3B valuation |
| CyberOne | Xiaomi (CN) | 1.77 m / 52 kg | — | — | ~$100K (est.) | Internal R&D; no mass production |
| T1 / K1 | Booster Robotics (CN) | T1 ~1.2 m | 23 | — | K1 from ~$6K | Education + RoboCup platform of choice |
| SE01 / PM01 | EngineAI (CN) | full-size + compact | — | — | PM01 ~$12–14K (unverified) | $200M Series B 2026-04 |

## Real deployments — what is actually working (as of 2026-07)

| Deployment | Robot | Status |
|---|---|---|
| BMW Spartanburg (US) | Figure 02 → 03 | Figure 02 ran daily 10-hr shifts for ~11 months, loaded 90,000+ parts across 1,250+ runtime hours, supporting **30,000+ BMW X3s**; Figure 03 now doing sequencing logistics (~40 units reported); German plant pilots reported |
| GXO Logistics (US) | Agility Digit (+ Apollo pilots) | First commercial humanoid RaaS deployment (2024-06); >100,000 totes moved at Flowery Branch, GA (2025-11) |
| Schaeffler, Toyota Canada, Mercado Libre | Agility Digit | Live production floors; Toyota Woodstock, Ontario took 7 Digits under RaaS (2026-02); part of 65,000+ cumulative hours across 9 facilities |
| Mercedes-Benz (Germany/Hungary) | Apptronik Apollo | Intralogistics + quality checks at Berlin-Marienfelde Digital Factory Campus and Kecskemét; Mercedes is an investor; commercial delivery planned 2027 |
| Hyundai/Kia US plants | Boston Dynamics Atlas | **>25,000 Atlas units** planned (announced 2026), starting Metaplant Georgia 2028, Kia Georgia 2029; 30K/yr robot factory planned; union pushback reported |
| BYD, Foxconn, Geely, FAW-VW, Dongfeng, BAIC, SF Express (CN) | UBTech Walker S2 | Hundreds of units; >RMB 800M (~$112M) cumulative Walker orders; Liuzhou plant targeting 5K/yr; Airbus aviation pilot signed 2026-01 (unverified) |
| Retail/pharmacy China | Galbot G1 (wheeled) | Galbot Store autonomous retail in 30+ cities; 10+ Beijing pharmacies; FamilyMart partnership from 2026-04 |
| Tesla Fremont (internal) | Optimus | Several hundred robots deployed internally, "primarily for learning and data collection" per Musk (Q4'25 call, 2026-01-28); an aggregator-circulated ">1,000 on the floor" figure has no primary source (unverified); all numbers self-reported |
| US homes | 1X NEO | Pre-orders open; deliveries from late 2026; complex chores rely on human teleoperators ("Expert Mode") |

More detail on the two dominant national ecosystems: [Landscape: China](landscape-china.md) and [Landscape: USA](landscape-usa.md); Europe/Japan/Korea in [Landscape: RoW](landscape-row.md).

## Key company notes

### United States
- **Tesla** announced the end of Model S/X production 2026-01 (final cars built 2026-05) to convert Fremont to Optimus; line start slipped to late July–August 2026 with ~10,000 unique parts and "quite slow" initial output; second line at Giga Texas ~2027 (Gen 4). Musk targets consumer sales by end-2027 and an eventual 1M/yr at Fremont, 10M/yr at Giga Texas — aspirational; Tesla has missed every Optimus timeline since 2021. V3 public reveal slipped again (2026-04). Hardware: AI5 chip, Grok voice integration (unverified secondary reporting). Line installation is underway: Tesla VP Lars Moravy said the first Optimus production line has landed at Fremont and installation has begun, touting its "modular" design; Musk posted a photo captioned "Walking the Optimus production line in Fremont" on 2026-07-01 (as of 2026-07) — production start still guided for late July–August.
- **Figure** is the best-capitalized pure-play (~$1.9B raised; $39B post-money 2025-09; investors incl. Parkway, Brookfield, NVIDIA, Intel Capital, Qualcomm Ventures, Salesforce). Figure 03 (announced 2025-10): 9% lighter than 02, 2× actuator speed, 2 kW inductive wireless charging, cameras with 2× frame rate and 60% wider FoV, fingertip tactile sensing to 3 grams (official). BotQ line capacity 12,000/yr, 4-year goal 100,000 robots; output ramped 1/day → ~1/hour in under 4 months (official claim, 2026-05). Brookfield "Project Go-Big" opens ~100,000 residential units for egocentric training data — see [Data](data.md).
- **Boston Dynamics** fully retired hydraulics; electric Atlas uses Hyundai Mobis direct-drive actuators (~220 Nm/kg torque density, unverified) and won "Best Robot" at CES 2026; Google DeepMind partnership puts Gemini-family models on Atlas. See [Organizations](organizations.md).
- **Agility** goes public via Churchill Capital XI SPAC: $2.5B pre-money, >$620M gross proceeds ($420M trust + ~$200M PIPE at $10/sh), Nasdaq ticker AGLT, close expected by end-2026. Digit v5 pitched as first "cooperatively safe" humanoid (NVIDIA Halos); RoboFab (Salem, OR) designed for 10K units/yr with ~75% US-domestic parts. Backers: DCVC, NVIDIA, Amazon, SoftBank Vision Fund 2, Schaeffler, Foxconn, Playground Global.
- **Apptronik** Series A totals >$935M (incl. $520M extension at ~$5B, 2026-02); Jabil both contract-manufactures Apollo and pilots it internally; Google DeepMind supplies foundation-model AI.
- **Sanctuary AI (CA)** is the cautionary tale: after leadership turnover it decoupled its AI stack from Phoenix hardware and now sells "Physical AI" for existing industrial arms.

### China
- **Unitree** is the price disruptor and set to be the first "embodied AI" listing on China's A-share market: Shanghai STAR IPO (~$618M / RMB 4.2B, ~$6.2B valuation) cleared the listing committee 2026-06-01 and won CSRC registration approval 2026-07; prospectus shows 2025 revenue ~RMB 1.7B (+335%), adjusted net profit up ~674% YoY (already profitable in 2024 — see [Unitree deep dive](company-unitree.md)), humanoids >50% of revenue; targets up to 20,000 humanoid shipments in 2026 vs >5,500 claimed for 2025 (Omdia counts 4,200). Widest price ladder in the industry: R1 $4,290 → G1 $13.5K → H2 $29.9K → industrial. See [Hardware](hardware.md).
- **AgiBot (Zhiyuan)**, founded 2023-02 by ex-Huawei's Deng Taihua and Peng Zhihui, is the cumulative-volume leader (10,000th unit 2026-03); A2 set a Guinness record walking 106.3 km (Suzhou→Shanghai); Expedition A3 (2026-02) targets interactive service venues; pursuing a backdoor STAR-market listing (unverified status).
- **UBTech** (HKEX-listed): Walker S2's autonomous 3-minute battery hot-swap enables continuous shifts; order book >RMB 800M and growing; broadest blue-chip factory customer list in the industry.
- **Galbot** raised RMB 2.5B (~$362M, 2026-03 close; >$300M tranche announced 2025-12) including China's state "Big Fund" — first national-level fund bet on embodied AI; ~$800M total raised at ~$3B valuation, China's highest-valued unlisted humanoid firm.
- **XPeng** treats IRON as a car-adjacent product: dedicated ~110,000 m² humanoid factory broke ground Q1 2026, mass production targeted end-2026, 1M-unit cumulative goal by 2030 (aspirational); first deployments in showrooms, museums, retail.
- **Fourier** leverages rehab-robotics channels into "care-bot" humanoids (GR-3) — healthcare is its wedge, unlike everyone else's factory/warehouse focus.

## Unit economics and pricing trend

- **BOM (as of 2026)**: Morgan Stanley estimates **~$46K/unit with Chinese supply chains vs ~$131K without** (modeled on a Tesla Optimus Gen 2-class robot; actuators alone $22K → $58K) — the ~2.8× gap driving both China's price advantage and US tariff/reshoring tension.
- **Cost structure**: actuators ~35–40% of BOM, batteries ~15–20%, onboard compute ~10–15% (industry estimate, unverified).
- **Price history**: 2023 research humanoids $150K–500K (Unitree H1 at $90K was "cheap") → 2025 G1 at $16K street, R1 at $5,900 → 2026 R1 dual-arm from $4,290, Booster K1 ~$6K, 1X NEO consumer at $20K, G1 listed on Amazon at $17,990. Western industrial platforms remain $100K+ or RaaS-only (Figure ~$25/robot-hour at BMW, reported, unverified).
- **Counter-trend**: Morgan Stanley forecasts humanoid BOM *rising* ~15% 2025→2030 (and +40% by 2045) as onboard compute requirements grow, even as $/FLOP falls.
- **Deflation driver**: Chinese actuator/hand supply chains (harmonic and planetary reducers, dexterous hands) deflating component costs ~15–20%/yr (reported estimate). Open question: do Western vendors compete on price or on autonomy software?
- **Margins reality-check**: Agility's SPAC filings show heavy losses typical of the sector; revenue remains small relative to valuations across all players (as of 2026-06).

## Open questions

- Can teleop-backstopped home robots (NEO) convert to genuine autonomy fast enough to retain consumers? See [Open problems](open-problems.md).
- Do industrial humanoids beat fixed automation + AMRs on ROI at scale, or stay niche for brownfield sites?
- How far do tariffs/export controls fragment the supply chain given the $46K-vs-$130K BOM gap?
- Reliability data is scarce: only Agility publishes fleet-hours; MTBF numbers are essentially unpublished industry-wide.

For how the field got here, see [History](history.md); for what still doesn't work (dexterity, reliability, data), see [Open problems](open-problems.md).

## Sources

- https://www.figure.ai/news/introducing-figure-03 — Figure 03 design, tactile/camera specs, 2 kW wireless charging, BotQ 12K/yr capacity (official)
- https://www.figure.ai/figure — Figure 03 official spec page: 5'8", 61 kg, 20 kg payload, 5 h runtime, 1.2 m/s (settles earlier 1.68 m secondary-source figure)
- https://www.figure.ai/news/ramping-figure-03-production — BotQ 1 robot/hour ramp, >350 units delivered (official)
- https://www.figure.ai/news/series-c — Figure >$1B Series C at $39B post-money; investor list; Brookfield (official)
- https://www.press.bmwgroup.com/global/article/detail/T0458778EN/bmw-group-advances-the-use-of-physical-ai-in-production-with-figure-03-project-in-spartanburg?language=en — BMW: Figure 02 pilot (30,000+ X3s), Figure 03 sequencing at Spartanburg (official)
- https://www.1x.tech/discover/neo-home-robot — NEO official specs: 30 kg, 68 kg lift, 22 dB, 22-DoF hands, $20K / $499/mo (official)
- https://www.therobotreport.com/1x-announces-pre-order-launch-neo-humanoid-robot/ — NEO pre-order launch, 2026 US / 2027 international timeline
- https://www.unitree.com/g1/ — G1 official specs: 35 kg, 23–43 DoF, from US$13.5K, ~2 h battery (official)
- https://www.humanoidsdaily.com/news/unitree-expands-r1-lineup-with-dual-arm-modular-platform-starting-at-4-290 — Unitree R1 lineup from $4,290
- https://shop.unitree.com/products/unitree-h2 — H2 official: $29.9K standard, H2 Plus $100K; 180 cm, 31 DoF, 360 N·m; only EDU supports secondary development
- https://robohorizon.com/en-us/news/2025/11/unitree-h2-price-and-limitations/ — H2 $29.9K fine print: base config, no dexterous-hand upgrades, app-driven control
- https://botinfo.ai/articles/unitree-h2-humanoid-robot — US/Canada distributor tiers: $40.9K "Commercial" (no SDK, 8-mo warranty), $68.9K EDU (full SDK/ROS 2)
- https://autonews.gasgoo.com/articles/news/unitree-wins-ipo-approval-as-robot-makers-face-tougher-profit-challenges-2061816669448765440 — Unitree Shanghai IPO approval (~$6.2B valuation)
- https://www.caixinglobal.com/2026-07-03/unitree-robotics-wins-approval-for-618-million-star-market-ipo-102460136.html — Unitree CSRC registration approval ($618M raise, RMB 42B target valuation, 2025 revenue RMB 1.69B)
- https://roboticsandautomationnews.com/2026/03/31/unitree-robotics-files-for-610-million-ipo-as-humanoid-robot-sales-surge/100272/ — Unitree prospectus: revenue +335% in 2025, >5,500 humanoids shipped (article's "first profitable year" framing is imprecise — prospectus shows 2024 already profitable)
- https://www.forbes.com/sites/jonmarkman/2026/04/27/unitree-g1-humanoid-robots-are-reshaping-the-robotics-investment-stack/ — Unitree revenue growth, 20K shipment target 2026
- https://www.agilityrobotics.com/content/agility-robotics-to-go-public-through-merger-with-churchill-capital-corp-xi — SPAC terms ($2.5B, $420M trust + $200M PIPE, AGLT), $300M Digit v5 orders, 65K hours, 9 facilities, RoboFab 10K/yr, 75% US parts (official)
- https://www.agilityrobotics.com/content/gxo-signs-industry-first-multi-year-agreement-with-agility-robotics — first humanoid RaaS contract (official)
- https://www.geekwire.com/2026/digit-maker-agility-robotics-to-go-public-in-2-5b-deal-heres-what-the-filings-say-about-its-finances/ — Agility financials from SPAC filings
- https://www.therobotreport.com/humanoid-maker-agility-robotics-go-public-through-spac-merger/ — independent confirmation of SPAC terms, 65,000+ hours across 9 customer facilities, $300M v5 orders
- https://apptronik.com/news-collection/apptronik-closes-over-935-million-series-a — Apptronik >$935M Series A total (official)
- https://www.cnbc.com/2026/02/11/apptronik-raises-520-million-at-5-billion-valuation-for-apollo-robot.html — $520M extension at ~$5B; Mercedes/GXO/Jabil pilots
- https://group.mercedes-benz.com/company/production/procuction-network/mbdfc-humanoid-robots.html — Apollo roles at Mercedes Berlin/Kecskemét (official)
- https://www.hyundainews.com/releases/4664 — Hyundai CES 2026 robotics strategy, Atlas at Metaplant by 2028, 30K/yr robot plant (official)
- https://interestingengineering.com/ai-robotics/hyundai-25000-atlas-humanoid-robots-us-plants — Hyundai plan for 25,000+ Atlas units across US plants
- https://bostondynamics.com/blog/boston-dynamics-unveils-new-atlas-robot-to-revolutionize-industry/ — electric Atlas announcement (official)
- https://electrek.co/2026/04/22/tesla-optimus-production-fremont-model-sx-line/ — Optimus V3 delay, Fremont Model S/X line conversion
- https://electrek.co/2026/01/28/musk-admits-no-optimus-robots-are-doing-useful-work-at-tesla-after-claiming-otherwise/ — Q4'25 call: several hundred deployed "primarily for learning," "still in the R&D phase"
- https://www.benzinga.com/markets/tech/26/07/60209589/elon-musk-says-teslas-model-s-model-x-line-is-now-building-optimus-robots — Musk photo post from the first Fremont Optimus line (2026-07-01); Moravy: line landed, installation begun, "modular" design
- https://www.electrive.com/2026/05/11/final-tesla-model-s-rolls-off-the-production-line/ — final Model S/X built at Fremont 2026-05
- https://www.automate.org/robotics/industry-insights/boston-dynamics-to-begin-production-on-redesigned-atlas-humanoid-in-2026 — all 2026 Atlas output committed to Hyundai RMAC + Google DeepMind; other customers from early 2027
- https://www.prnewswire.com/news-releases/ubtech-humanoid-robot-walker-s2-begins-mass-production-and-delivery-with-orders-exceeding-800-million-yuan-302616924.html — Walker S2 mass delivery, RMB 800M orders, 5K/yr capacity target (official PR)
- https://www.therobotreport.com/agibot-rolls-out-10000th-humanoid-robot/ — AgiBot 10,000th robot (2026-03-31), Omdia/IDC 2025 rankings
- https://www.xpeng.com/news/019a56f54fe99a2a0a8d8a0282e402b7 — next-gen IRON: 82 DoF, Turing chips, VLA 2.0, solid-state battery (official)
- https://www.humanoidsdaily.com/news/xpeng-to-break-ground-on-full-chain-humanoid-factory-to-meet-2026-production-goal — XPeng 110,000 m² humanoid factory, late-2026 mass production
- https://technode.com/2026/03/02/humanoid-robot-maker-galbot-raises-rmb-2-5-billion/ — Galbot RMB 2.5B round with state Big Fund
- https://www.prnewswire.com/news-releases/galbot-secures-over-300-million-in-new-funding-breaking-records-with-3-billion-valuation-in-chinas-humanoid-robot-sector-302647204.html — Galbot $300M+ tranche, $3B valuation (official PR)
- https://www.therobotreport.com/galbot-brings-in-300m-to-scale-mobile-manipulator-deployments/ — Galbot deployments: 30+ cities, pharmacies
- https://www.cnbc.com/2026/06/24/morgan-stanley-china-humanoid-robot-market-forecast.html — Morgan Stanley 2026 China forecast raised 14K → 28K → 50K (2026-06-24); Chinese firms >80% of 2025 global shipments
- https://www.cryptopolitan.com/morgan-stanley-doubles-chinas-humanoid-shipment-target-to-50000/ — Morgan Stanley 2026 China shipment forecast raised to 50K
- https://www.scmp.com/tech/tech-trends/article/3339346/chinese-firms-outpace-us-rivals-2025-humanoid-robot-shipments-agibot-takes-lead — Omdia 2025 rankings: AgiBot 5,168 (39%), Unitree 4,200 (32%), ~13K global total
- https://www.scmp.com/tech/article/3337151/china-packs-patent-punch-race-build-humanoid-robots — Morgan Stanley BOM: $46K with China supply chain vs $131K without (Optimus Gen 2 model; actuators $22K → $58K)
- https://www.investing.com/news/stock-market-news/morgan-stanley-projects-a-humanoids-chip-tam-of-305b-by-2045-4384088 — Morgan Stanley: humanoid BOM +15% 2025→2030 (+40% by 2045) on rising compute/chip ASPs
- https://www.morganstanley.com/insights/articles/humanoid-robot-market-5-trillion-by-2050 — $5T-by-2050 projection, BOM trend (+15% to 2030)
- https://www.goldmansachs.com/insights/articles/the-global-market-for-robots-could-reach-38-billion-by-2035 — Goldman $38B-by-2035 forecast
- https://www.techtimes.com/articles/318641/20260618/humanoid-robots-china-ships-90-global-units-now-leads-ai-benchmarks.htm — China ~90% share claim; AgiBot/UBTech/Galbot/Fourier cumulative milestones
- https://cnmra.com/who-will-be-the-real-winner-in-the-implementation-of-embodied-ai-scenarios-in-2026/ — EngineAI $200M Series B (2026-04)
