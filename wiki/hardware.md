---
title: Hardware Substrate
slug: hardware
updated: 2026-07-03
confidence: verified
---
> The hardware substrate of Physical AI — actuators, hands, tactile/force sensing, onboard compute, and batteries — has consolidated around a recognizable "standard stack" as of mid-2026: harmonic-drive or quasi-direct-drive rotary joints in the upper body, planetary-roller-screw linear actuators in hips/knees/ankles, tendon-driven 20+ DoF hands with fingertip tactile sensing, NVIDIA Jetson (Orin → Thor) for onboard inference, and ~2 kWh lithium packs giving 2–5 hours of runtime. BOM costs are falling fast (Goldman Sachs measured ~40% YoY manufacturing-cost decline; Tesla targets ~$20k/unit at scale), but roughly 70% of components for even US-built humanoids trace to Chinese suppliers, and China's ~90% grip on rare-earth magnet processing was demonstrated as a live chokepoint when 2025 export controls disrupted Optimus production. See [Humanoid robots](humanoid-robots.md) for full-system platforms and [Landscape: China](landscape-china.md) for the supply-chain geography.

## Actuators

The industry has largely converged on a **hybrid joint architecture**: rotary harmonic/QDD modules for arms and torso, linear roller-screw actuators for high-force leg joints.

| Actuator type | Mechanism | Strengths | Weaknesses | Typical placement |
|---|---|---|---|---|
| Harmonic (strain-wave) drive | Flexspline + wave generator, ratios 50–160:1 | Zero-backlash (≤15 arcsec), compact, high ratio | Poor shock tolerance, flexspline fatigue, not backdrivable | Arms, wrists, torso |
| Quasi-direct-drive (QDD) | High-torque motor + low-ratio (~6–10:1) planetary gear | Backdrivable, compliant, high-bandwidth force control, robust to impact | Lower torque density per volume, motor mass/cost | Legs (MIT-Cheetah lineage), some full-QDD designs |
| Planetary gearbox | Multi-stage planetary | Load spread across teeth, shock-tolerant, cheap | Backlash, larger for high ratios | Hips, knees (rotary variants) |
| Planetary roller screw (PRS) | Rotary→linear via threaded rollers | Very high force density, stiffness, shock-load capacity | Precision grinding is a manufacturing bottleneck; expensive | Linear leg actuators (hips, knees, ankles) |
| Cycloidal / RV | Cycloidal cam reduction | High shock capacity, rigidity | Weight, cost, complexity | Some hips/waists; industrial-arm heritage |

- Tesla Optimus uses ~28 actuators per robot (mix of rotary + linear), including ~14 inverted planetary roller screws for the legs and ~20 coreless motors for the hands, per Chinese supply-chain reporting (as of 2026-06, unverified).
- QDD (pioneered in the MIT Mini Cheetah lineage) trades gear ratio for backdrivability — key for contact-rich locomotion and safe human interaction; most 2025–26 humanoids use QDD-style low-ratio joints in legs or throughout (e.g., Unitree).
- Figure 03's actuators run ~2× faster with improved torque density (Nm/kg) vs Figure 02 (company claim, as of 2025-10).
- PRS supply is the tightest actuator bottleneck: precision thread-grinding machines and aerospace-grade alloys are scarce; Chinese maker Beite Technology is building a 1.85B-yuan (~$260M) Kunshan plant targeting 2.6M PRS sets/year, with mass production expected in 2026 (Chinese industry reporting, multiple outlets).
- Chinese joint-module vendor EYOU claims 95,000 joint module sets delivered in 2025 across harmonic and planetary lines (single source, unverified).
- Rare-earth-free motors (ferrite-assisted) remain aspirational: designs matching NdFeB output run ~30% heavier, and as of early 2026 no commercial rare-earth-free drive unit is confirmed deployed by Tesla despite its 2023 announcement.

## Dexterous hands

Hands are the highest-churn subsystem — see [Manipulation](manipulation.md) for the software side.

| Hand (as of 2026-06) | DoF | Actuation | Tactile | Notes |
|---|---|---|---|---|
| Tesla Optimus Gen 3 hand | 22 (hand) + 3 (wrist) | ~25 actuators per forearm (50 total), tendon-driven, actuators in forearm | Extended tactile coverage in development | 4.5× actuator count vs Gen 2 (11 DoF); demoed catching objects (2025–26) |
| Figure 03 hand | 16+ per hand (F02 baseline); softer adaptive fingertips | In-hand + palm | Fingertip sensors detect ~3 g force; palm camera per hand | Palm cameras give close-range vision when main cameras are occluded |
| Unitree Dex5-1 | 20 (16 active + 4 passive) | Direct-drive fingers, ~1 kg | Optional 94 pressure points, 1 kHz update | ~10 N fingertip force, ~1 mm repeatability; sold as add-on for H1/G1 |
| Shadow Dexterous Hand | 24 | Tendon, pneumatic/electric variants | BioTac/GelSight options | Research benchmark since the OpenAI Rubik's-cube era |
| Inspire RH56 series | ~6 active | Linkage | Basic force | The low-cost workhorse on many Chinese humanoids |

- Design trend: move actuators out of the hand into the forearm with tendon transmission (Optimus Gen 3, Figure) — frees hand volume for sensing, cuts hand inertia, eases thermal limits.
- Second trend: cheap under-actuated hands (~6 DoF) for factory pilots vs 20+ DoF fully-actuated hands for general manipulation; the market splits accordingly, with Chinese vendors (Inspire, Unitree, BrainCo) pushing prices down.

## Sensing

**Vision-based tactile (VBT)** — a camera watches deformation of an illuminated gel skin, giving high-resolution contact geometry:
- GelSight (MIT spinout) is the reference technology; micron-level spatial resolution.
- **Meta AI × GelSight Digit 360** (announced 2024-10): fingertip-shaped VBT sensor with 18+ sensing modalities, omnidirectional fingertip deformation capture, sensitivity down to ~1 mN forces; positioned as a research standard with open tooling.
- VBT remains mostly research-grade as of mid-2026; production humanoids ship simpler piezoresistive/capacitive fingertip arrays for durability reasons (Figure explicitly cites durability as the design driver for its in-house sensor).

**Production tactile** (as of 2026):
- Figure 03: in-house fingertip sensors detecting ~3 g of force, plus palm cameras (redundant close-range vision).
- Unitree Dex5-1: optional 94-point pressure array at 1 kHz.
- Optimus Gen 3: tactile-sensing integration with more surface coverage stated as in progress (as of 2026-06, unverified).

**Force/torque sensing**:
- Six-axis F/T sensors sit at wrists/ankles for balance and compliant contact; historically the domain of ATI, Schunk, AMTI at $3k–$10k+ per sensor.
- Chinese suppliers (Hypersen, Kunwei, Keli, Yuli) are scaling: ~60k six-axis units sold globally in 2024, ~17k in China (+40% YoY); one forecast puts the humanoid torque-sensor market at $7.9B by 2032, 48% CAGR (market-research figures, unverified).
- Joint-level torque sensing vs current-based torque estimation is an open cost/performance tradeoff; QDD designs often skip dedicated sensors and estimate torque from motor current.

## Onboard compute

NVIDIA is the de-facto standard; see [Organizations](organizations.md) for the ecosystem play.

| Platform | AI compute | Memory | Power | Price (as of 2026-01) | Status |
|---|---|---|---|---|---|
| NVIDIA Jetson AGX Orin | 275 TOPS (INT8) | 64 GB | 15–60 W | ~$1,999 dev kit | The 2023–25 workhorse (Walker S2, many others) |
| NVIDIA Jetson AGX Thor (T5000) | 2,070 TFLOPS (FP4, sparse) | 128 GB LPDDR5X | 40–130 W | $3,499 dev kit (2025-08) | GA 2025-08-25; 7.5× Orin compute, 3.5× efficiency; 14-core Neoverse-V3AE |
| NVIDIA Jetson T4000 | 1,200 TFLOPS (FP4, sparse) | 64 GB | 40–70 W | $1,999 @1k units | Mid-tier Thor module, announced 2026-01 (CES) |
| Tesla AI5 (custom) | undisclosed; Musk claims ~H100-class inference for Tesla workloads, ~10× AI4 | — | — | — | Taped out 2026-04-15 (Samsung + TSMC fabs); volume production targeted mid-to-late 2027, aimed at Optimus + clusters rather than vehicles initially |

- Thor's 128 GB memory is the headline for Physical AI: it fits multi-billion-parameter [VLA models](vla-models.md) plus perception on-device. Early adopters (as of 2025-08): Agility, Amazon Robotics, Boston Dynamics, Figure, Caterpillar, Meta; 1X, OpenAI, Physical Intelligence evaluating.
- Common pattern is **split-brain compute**: a real-time controller CPU (x86 or MCU, hard-real-time joint control at ~1 kHz) + an NVIDIA module for perception/policy — e.g., UBTECH Walker S2 pairs an Intel i7-1185G7 with Jetson AGX Orin 64 GB.
- Chinese platforms (Horizon Robotics, Black Sesame, Huawei Ascend) are positioned as domestic alternatives but had no widely-adopted humanoid design win reported as of mid-2026 (absence-of-evidence, unverified).
- The frontier architectural question — how much inference runs onboard vs offboard — is discussed in [Open problems](open-problems.md).

## Batteries and runtime

| Robot (as of 2026-06) | Pack | Claimed runtime | Charging/swap |
|---|---|---|---|
| Tesla Optimus | 2.3 kWh, 52 V | ~8 h claimed for light work (unverified) | Plug charge |
| Figure 03 | 2.3 kWh | ~5 h claimed at peak performance (real-world estimates ~3–4 h, unverified) | 2 kW inductive wireless via foot coils; autonomous docking |
| UBTECH Walker S2 | Dual 48 V Li-ion packs | ~2 h per pack | **Autonomous self-swap in ~3 min** — robot exchanges its own battery, enabling 24/7 ops |
| Unitree G1 | 9 Ah (~0.8 kWh) | ~2 h | Quick-release pack |
| Apptronik Apollo | swappable pack | ~4 h per pack | Hot-swap design |

- Reality check: most commercial humanoids deliver 1.5–5 h per charge depending on task intensity; heavy manipulation or fast locomotion cuts spec-sheet numbers roughly in half.
- Fleet operators solve runtime with hot-swap rotation or opportunistic charging (Figure's wireless dock), not bigger packs — pack mass compounds the "mass penalty spiral" (heavier battery → bigger actuators → heavier robot).
- Battery certification (UN38.3, multi-layer BMS protections) became a marketed feature in 2025 as robots entered homes and factories (Figure 03).

## BOM cost trends

- Goldman Sachs (report 2024-02): humanoid manufacturing cost fell ~40% YoY — from $50k–$250k/unit to $30k–$150k in roughly a year — versus prior expectations of 15–20%/yr; a key driver of its >6× upward market-forecast revision ($6B → $38B by 2035, shipments 4× to 1.4M units).
- Tesla's stated Optimus mass-production cost target: ~$20,000/unit (as of 2026). A circulated BOM split (unverified, via 36kr): actuators ~35%, sensors+other ~20%, lead/roller screws ~18%, reducers ~15%, motors ~12%.
- Street pricing (as of 2026-06): Unitree G1 from ~$13.5k–16k (EDU configs $43.9k–$73.9k); most industrial-grade humanoids cluster at $20k–$30k; Boston Dynamics signaled Atlas pricing below ~$320k ("under two years of two US manufacturing workers' payroll"; no public MSRP, direct sales only). Unitree launched G1 at $16k in 2024-05, so entry price has been roughly flat while capability rose.
- Chinese manufacturers achieve per-unit costs roughly ⅓–½ of Western equivalents (Morgan Stanley, as of 2026), replaying the EV cost playbook: integrated domestic supply chain + huge domestic pilot deployments.
- Compute is becoming a smaller BOM share even as capability jumps ($1,999 for a T4000 module vs ~$7k of actuators in a $20k robot).
- Cost curves and volume forecasts feed directly into [Investment](investment.md) theses; production-scaling attempts (Figure BotQ: 12k robots/yr initial capacity, 100k over four years; Tesla Fremont line conversion targeting ~1M/yr, volume start planned late 2026 (unverified)) are tracked in [State of the art](state-of-the-art.md).

## Supply chain and China's component dominance

- **Rare-earth magnets**: China controls ~69% of rare-earth mining and ~90% of magnet processing/refining (as of 2025, McKinsey). The average humanoid contains ~0.9 kg of rare-earth metals (McKinsey; up to ~1.3 kg NdPr for a human-sized robot); total NdFeB magnet mass per Optimus is reported at ~3.5 kg. China's 2025-04 export controls on heavy rare-earth magnets directly disrupted Optimus production — Musk confirmed this on the 2025-04-22 earnings call, saying Tesla was seeking an export license.
- **Reducers**: Japan's Harmonic Drive Systems and Nabtesco still lead the high-end; Chinese makers (Suzhou Green Harmonic, Zhejiang FORE) are taking share in medium-precision tiers on price.
- **Roller screws**: historically a European/Japanese monopoly (Rollvis, GSA, Ewellix, NSK); Chinese entrants (Wuzhou New Spring, Beite, Hengli) are scaling aggressively — the key constraint is precision thread-grinding machine tools, themselves supply-limited.
- **Broader shares** (McKinsey, as of 2025): China holds ~40% of precision bearings, ~35% of motors, ~30% of power electronics for the humanoid value chain.
- ~70% of Tesla Optimus components trace to Chinese suppliers across actuator assembly (Top Group, Sanhua), transmission (Green Harmonic, Wuzhou New Spring, Double Ring), and motors/sensors (Zhaowei, Inovance) (as of 2026-06, unverified). Reported 2025-10 Sanhua order for Optimus actuator components: ~$685M, delivered from a Mexico plant starting 2026 — neither Tesla nor Sanhua confirmed the order, and Sanhua declined to comment on "market rumors" (single source via 36kr, unverified).
- Strategic consequence: US/EU humanoid programs face a component-sovereignty problem that mirrors early EV batteries — a de-risking push (reshoring PRS grinding, non-Chinese magnet processing via MP Materials et al.) is underway but years from parity. Geography details in [Landscape: China](landscape-china.md) and [Landscape: USA](landscape-usa.md).

## Watch items

- Whether VBT tactile (GelSight-class) crosses into production hands, or piezoresistive arrays stay "good enough."
- Rare-earth-free actuator motors reaching torque-density parity (ferrite penalty ~30% mass as of 2026).
- PRS grinding capacity vs Tesla/Figure volume ramps in H2 2026 — the most-cited physical bottleneck.
- Onboard-compute bifurcation: NVIDIA Thor standardization vs custom silicon (Tesla AI5) vs Chinese domestic chips.
- Battery: solid-state or high-silicon packs pushing runtime past 5 h without the mass spiral.

## Sources
- https://nvidianews.nvidia.com/news/nvidia-blackwell-powered-jetson-thor-now-available-accelerating-the-age-of-general-robotics — Jetson Thor GA date, specs (2,070 FP4 TFLOPS, 128 GB, 130 W), $3,499 dev kit, adopter list
- https://developer.nvidia.com/blog/introducing-nvidia-jetson-thor-the-ultimate-platform-for-physical-ai/ — Thor architecture detail (Neoverse-V3AE CPU, PVA, I/O)
- https://www.stocktitan.net/news/NVDA/nvidia-releases-new-physical-ai-models-as-global-partners-unveil-77essf0i9cjv.html — Jetson T4000 announcement: 1,200 FP4 TFLOPS, 64 GB, $1,999 @1k units
- https://www.cnx-software.com/2025/08/19/3499-nvidia-jetson-agx-thor-developer-kit-2070-tops-jetson-t5000-som-for-robotics-and-edge-ai/ — T5000 module details and power range
- https://www.figure.ai/news/introducing-figure-03 — Figure 03 hands (3 g fingertip sensitivity, palm cameras), 2 kW wireless charging, actuator speed/torque claims, BotQ capacity
- https://www.businesswire.com/news/home/20241031980322/en/GelSight-and-Meta-AI-Introduce-Digit-360-Tactile-Sensor — Digit 360 specs: 18+ sensing features, ~1 mN force sensitivity, omnidirectional deformation
- https://www.unitree.com/mobile/Dex5-1/ — Unitree Dex5-1 hand: 20 DoF, 94 optional tactile points, force/repeatability specs
- https://www.ubtrobot.com/en/humanoid/products/walker-s2 — Walker S2 autonomous 3-min battery swap, dual 48 V packs, 52 DoF, compute stack
- https://eu.36kr.com/en/p/3780414717129481 — Optimus component counts (~28 actuators, ~14 roller screws), $20k cost target, BOM split, Chinese supplier map, Sanhua $685M order (single-source)
- https://fortune.com/article/elon-musk-tesla-optimus-robots-china-rare-earths/ — China rare-earth export controls disrupting Optimus production
- https://www.adamasintel.com/tesla-rare-earth-free-motor/ — status of Tesla rare-earth-free motor ambitions
- https://rareearthexchanges.com/news/teslas-rare-earth-exit-a-strategy-ahead-of-its-time-or-the-market/ — no confirmed rare-earth-free deployment as of early 2026; ferrite ~30% mass penalty
- https://www.mckinsey.com/industries/industrials/our-insights/turning-humanoid-supply-chain-constraints-into-billion-dollar-wins — China component shares (bearings ~40%, motors ~35%, power electronics ~30%), NdPr per robot
- https://advisor.morganstanley.com/john.howard/documents/field/j/jo/john-howard/The_Humanoid_100_-_Mapping_the_Humanoid_Robot_Value_Chain.pdf — Humanoid 100 value-chain mapping; Chinese cost advantage
- https://www.goldmansachs.com/insights/articles/the-global-market-for-robots-could-reach-38-billion-by-2035 — 40% YoY cost decline, $30k–150k unit costs, $38B/2035 forecast (report "Humanoid Robot: The AI Accelerant", 2024-02-26; >6× raise from $6B, shipments 4× to 1.4M)
- https://interestingengineering.com/ai-robotics/china-humanoid-robots-actuators — China joint-architecture strengths/gaps; harmonic-upper/planetary-lower convergence
- https://botinfo.ai/articles/unitree-g1 — Unitree G1 2026 pricing across configurations
- https://www.therobotreport.com/nvidia-jetson-thor-brings-2k-teraflops-of-ai-compute-to-robots/ — independent confirmation of Thor specs and positioning
- https://www.yicaiglobal.com/news/six-axis-force-sensors-for-humanoid-robots-are-close-to-achieving-mass-production — Chinese six-axis F/T sensor mass-production progress
- https://www.intelmarketresearch.com/torque-sensor-for-humanoid-robot-market-2830 — humanoid torque-sensor market forecast (unverified market research)
- https://www.robotwale.com/article/humanoid-robot-battery-runtime-reality-check — spec-sheet vs real-world runtime gap; hot-swap operational patterns
- https://developer.nvidia.com/blog/accelerate-ai-inference-for-edge-and-robotics-with-nvidia-jetson-t4000-and-nvidia-jetpack-7-1/ — Jetson T4000 official specs: 1,200 FP4 sparse TFLOPS, 64 GB LPDDR5X, 40–70 W envelope
- https://www.figure.ai/news/f-03-battery-development — Figure 03 battery: 2.3 kWh, ~5 h claimed runtime at peak performance, 2 kW fast charging, active cooling + custom BMS
- https://www.cnbc.com/2025/04/23/teslas-optimus-hit-by-chinas-rare-earth-restrictions-says-musk.html — Musk on 2025-04-22 earnings call: Optimus production impacted by China rare-earth export controls; seeking export license
- https://www.teslarati.com/tesla-optimus-v3-hand-arm-details-revealed-new-patents/ — Optimus Gen 3/V3 hand patents: 22 DoF hand, tendon-driven, 25 forearm actuators per arm
- https://electrek.co/2026/04/15/tesla-ai5-chip-taped-out-musk-ai6-dojo3/ — Tesla AI5 taped out 2026-04-15; Samsung + TSMC fabs; volume production targeted mid-to-late 2027; Optimus/cluster focus
- https://www.humanoidsdaily.com/news/tesla-optimus-production-rumors-fuel-supplier-stock-surge — reported $685M Sanhua order not confirmed by Tesla or Sanhua; Sanhua declined to comment on market rumors
- https://www.kedglobal.com/robotics/newsView/ked202601200007 — Boston Dynamics to price Atlas below ~two years of two US manufacturing workers' payroll (~$320k); no public MSRP
- https://cnevpost.com/2025/07/17/ubtech-humanoid-robot-autonomous-battery-swap/ — independent confirmation of Walker S2 3-min autonomous battery swap, dual 48 V packs, ~2 h walking per pack
