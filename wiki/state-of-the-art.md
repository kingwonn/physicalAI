---
title: State of the Art (2026-07 snapshot)
slug: state-of-the-art
updated: 2026-07-04
confidence: verified
---
> As of July 2026, Physical AI has crossed from lab demos into first commercial deployments: generalist [VLA models](vla-models.md) (Physical Intelligence's π0.7, Google DeepMind's Gemini Robotics 1.5/ER 1.6, NVIDIA's GR00T line, Figure's Helix 02) can execute multi-minute household and industrial tasks zero-shot across robot embodiments; [humanoids](humanoid-robots.md) are working paid jobs at BMW and GXO sites (with Toyota's RAV4 line contracted for 2026) while China ships ~80–90% of global humanoid units; [world models](world-models.md) (Genie 3, NVIDIA Cosmos 3) have become both simulation engines and, increasingly, the policy backbone itself; and capital has followed, with Figure at a $39B valuation, Skild AI at ~$14B, and Physical Intelligence reportedly raising at $11B+. Dexterous [manipulation](manipulation.md) remains the clearest unsolved bottleneck.

## Executive snapshot: who leads what (as of 2026-07)

| Domain | Frontier leader(s) | Evidence |
|---|---|---|
| Generalist VLA policy | Physical Intelligence (π0.7), Google DeepMind (Gemini Robotics 1.5) | π0.7 matches specialist fine-tuned models zero-shot; Gemini Robotics-ER 1.5 SOTA aggregate on 15 academic embodied-reasoning benchmarks |
| Embodied reasoning (high-level "brain") | Google DeepMind (Gemini Robotics-ER 1.6) | 93% instrument-reading accuracy vs 23% for ER 1.5 (Apr 2026) |
| Open robot foundation model | NVIDIA (GR00T N1.7 / N2 preview), Cosmos 3 | GR00T N2 ranks #1 on MolmoSpaces and RoboArena leaderboards (Mar 2026) |
| Humanoid commercial deployment | Figure (BMW), Agility (GXO/Toyota), UBTech (China) | Figure 03s doing logistics sequencing at BMW Spartanburg (from 2026-06); Digit moved 100k+ totes at GXO; UBTech claims 1,000+ industrial humanoids (unverified) |
| Humanoid shipment volume | AgiBot, Unitree (China) — #1 rank disputed | 2025 global shipments ~13k (Omdia) to ~18k (IDC); AgiBot ~5.2k per Omdia/IDC vs Unitree >5.5k per its own prospectus; ~80–90% Chinese — see shipment-count reconciliation below |
| Dynamic locomotion | Unitree, Boston Dynamics | Televised autonomous kung-fu with flips (Spring Festival Gala, 2026-02-16); production electric Atlas with 56 DoF |
| World models | Google DeepMind (Genie 3), NVIDIA (Cosmos 3) | Real-time 720p/24fps interactive worlds; open-source omnimodal WFM trained on ~20T tokens |
| Consumer home humanoid | 1X (NEO) | ~10,000 pre-orders in 5 days at $20k (company-reported); first US deliveries slated for 2026 |

## VLA / robot foundation models

See [VLA models](vla-models.md) for architecture detail and [data](data.md) for the training-data picture.

- **Physical Intelligence π0.7** (released 2026-04-16) is the current reference point for generalist policies: a "steerable" VLA that accepts language, speed/quality metadata, and visual subgoals as prompts. Claims compositional generalization (recombining skills for unseen tasks, e.g., operating unfamiliar kitchen appliances) and matches specialist fine-tuned models without fine-tuning across mobile manipulators, bimanual UR5e, and Franka arms. Laundry-folding success reported comparable to expert human teleoperators on a new robot platform (company-reported, unverified).
  - Lineage: π0 (Oct 2024) → π0.5 open-world generalization (Apr 2025) → π*0.6 RL-from-experience (Nov 2025) → π0.7 (Apr 2026). Supporting tech: FAST action tokenizer (~5× faster training), real-time action chunking, multi-scale embodied memory for 10+ minute tasks (Mar 2026).
- **Google DeepMind Gemini Robotics 1.5** (Sep 2025): two-model agentic stack — Gemini Robotics-ER as orchestrating "brain," Gemini Robotics as VLA executor. Gemini Robotics-ER 1.5 reported the highest aggregate score on 15 academic *embodied-reasoning* benchmarks (pointing, image/video QA: Point-Bench, ERQA, RefSpatial, etc. — per the tech report; not end-to-end robotics benchmarks), and the VLA demonstrated motion transfer across embodiments (dual-arm lab robots to humanoids) without per-robot specialization. **Gemini Robotics-ER 1.6** (2026-04-14) improved spatial reasoning, success detection, and added agentic "instrument reading" (93% accuracy vs 23% for ER 1.5); available via Gemini API / AI Studio.
- **NVIDIA GR00T**: GR00T N1.7 in early access with commercial licensing (dexterous control focus); **GR00T N2** previewed at GTC 2026-03-16 — a "world-action model" built on DreamZero research, claimed >2× success of leading VLAs on new tasks in new environments and #1 on MolmoSpaces and RoboArena; shipping targeted end of 2026. See [world models](world-models.md) for the world-model-as-policy convergence.
- **Figure Helix 02** (2026-01-27): in-house end-to-end "full-body autonomy" VLA — pixels and proprioception in, torques out — powering Figure 03 in both BMW logistics work and home-task demos (dishwasher loading, laundry, room tidying).
- **Others**: Skild AI ("omni-bodied" brain; $14B+ valuation as of 2026-01); RLWRLD's RLDX-1, a dexterity-first foundation model for five-finger hands (2026, single-source, unverified capability claims).
- **Research field**: 164 VLA submissions at ICLR 2026 (18× the 9 at ICLR 2025). Dominant trends: discrete-diffusion action decoding, embodied chain-of-thought, better action tokenizers (residual VQ, splines), and cross-embodiment/action-space transfer. Notable open models: FLOWER, X-VLA, OpenVLA descendants.

### Benchmark reality check (as of 2026-07)

| Benchmark | Status | Notes |
|---|---|---|
| LIBERO | Saturated | Most ICLR 2026 submissions at 95–98%; robustness variants (LIBERO-Plus/PRO/X) now used instead |
| CALVIN | Near ceiling | SOTA >4.5 avg. task chain length on ABC→D |
| SIMPLER | In use, noisy | 40–99% depending on setup; cross-paper comparison unreliable |
| RoboArena / MolmoSpaces | Rising standard | Zero-shot, real-robot-ish evaluation; large gap visible between closed frontier models and open-weight research models |

Takeaway: simulation benchmarks no longer separate frontier systems; the field is shifting to zero-shot real-robot evaluation, where closed models (Gemini Robotics, π-series, GR00T N2) lead. See [open problems](open-problems.md) on evaluation.

## Humanoids: from pilots to first commercial fleets

Full detail in [Humanoid robots](humanoid-robots.md); company profiles in [Organizations](organizations.md).

| Company | Robot | Status (as of 2026-07) |
|---|---|---|
| Figure | Figure 03 (Helix 02) | Figure 03s started complex logistics sequencing at BMW Spartanburg — project announced by BMW 2026-06-25, Figure announced deployment 2026-06-30 — after Figure 02's completed pilot (30,000+ X3s supported over ~10 months, ~1,250 hrs); reported initial 40-unit fleet contract (single aggregator source, unverified); Catalyst Brands logistics agreement (2026-05-26, Reno, NV DC); billing reportedly ~$25/robot-hour (unverified). Note: BMW's Leipzig pilot (summer 2026) uses Hexagon Robotics' AEON, not Figure |
| Tesla | Optimus V3 | Production start at Fremont ~late July/Aug 2026 on converted Model S/X line, "very slow" initial volume; first Optimus line delivered to Fremont with installation begun (per Tesla VP Lars Moravy); Musk posted a photo walking the line 2026-07-01; Gen-3 hands: ~25 actuators per forearm/hand side (22 DoF per hand, tendon-driven, 50 actuators across both hands); high volume targeted 2027; consumer sales targeted "end of 2027" (Musk, Davos, 2026-01) |
| Boston Dynamics | Electric Atlas | Production version unveiled CES 2026-01-05; 56 DoF, 2.3 m reach, 50 kg certified lift; 2026 fleet allocations fully committed (Hyundai RMAC, Google DeepMind partnership); Hyundai building a 30,000-robots/yr US factory; reported 25,000-unit internal commitment (unverified) |
| 1X | NEO | $20,000 (or $499/mo) consumer home humanoid; ~10,000 pre-orders in first 5 days (Oct 2025, company-reported); full-scale production at Hayward, CA since 2026-04-30 (10k/yr capacity claimed); first home deliveries promised before end of 2026 |
| Agility Robotics | Digit | GXO logistics: 100,000+ totes moved at Flowery Branch (as of late 2025); 7-unit RaaS contract for Toyota's RAV4 plant (Woodstock, Ontario; signed 2026-02) with rollout during 2026 |
| Unitree | G1 / R1 / H2 | >5,500 humanoids sold and delivered in 2025 per its IPO prospectus (bipedal only, wheeled models excluded; Omdia/IDC credit it with 4,200 and rank it #2 — see shipment reconciliation below); G1 at ~$16k (listed on Amazon at $17,990); R1 at ~$5,900; Shanghai STAR IPO cleared exchange listing review 2026-06-01 and won CSRC registration approval 2026-07-02 (reported 2026-07-03; ~¥4.2B / ~$618M raise); 2025 revenue ¥1.70B; GAAP net profit ~¥288M, 扣非 (excl. non-recurring) >¥600M (SCMP: "adjusted" ¥591M) — see [Company: Unitree](company-unitree.md) |
| AgiBot (Zhiyuan) | Expedition A3 etc. | 10,000th general-purpose robot rolled out late March 2026; 5,168 humanoids shipped in 2025 per Omdia (5,200 per IDC), which both rank it #1 globally; pursuing backdoor listing |
| UBTech | Walker S2 | Claims 1,000+ industrial humanoids deployed in auto/electronics/logistics plants (company-reported, unverified); launched UWORLD U1 consumer companion line 2026-06-30, from ~RMB 119,800, 13k+ orders claimed (company-reported), deliveries from ~2026-09 |
| Apptronik | Apollo / Apollo 2 | $935M total Series A (+$520M extension 2026-02-11) at ~$5.3B reported post-money valuation; Mercedes-Benz, Google, John Deere among backers; unveiled Apollo 2 + 90,000 sq ft "Robot Park" training campus (Austin, 2026-06-30) with Google DeepMind |

- Market scale: TrendForce forecasts global humanoid shipments >50,000 units in 2026 (~700% YoY — note this growth rate implies a ~6–7k 2025 base, well below the ~13–18k tracker range reconciled below; forecast baselines diverge too); China projected +94% output YoY with Unitree + AgiBot capturing ~80% of Chinese shipments (as of 2026-04 forecast).
- Regional split: ~80–90% of 2025 humanoid unit shipments were Chinese — ~87% within Omdia's top-10 table, ~90% per IDC coverage, ">80%" per Morgan Stanley ([Landscape: China](landscape-china.md)) — while the highest-value deployments and frontier models remain US-led ([Landscape: USA](landscape-usa.md)); Europe/Korea/Japan positions covered in [Landscape: rest of world](landscape-row.md).

### Reconciling 2025 shipment counts (as of 2026-07)

Published 2025 humanoid totals range from ~13,000 to ~18,000 units. The divergence is mostly definitional — each tracker counts a different thing:

| Tracker (report) | 2025 figure | What it counts |
|---|---|---|
| Omdia — *Market Radar: General-purpose Embodied Intelligent Robots* (2026-01) | 13,317 global | Vendor unit shipments, global. Top 10: AgiBot 5,168 (#1, ~39% share), Unitree 4,200, UBTech 1,000, Leju 500, EngineAI 400, Fourier 300, Figure/Agility/Tesla ~150 each, others ~1,350 |
| IDC — *Global Humanoid Robot Market Analysis* (2026-01; this is the "~18,000" figure carried by Xinhua/CCTV/Global Times) | ~18,000 global, +508% YoY | Shipments by company and application scenario (entertainment, research, manufacturing, warehousing, etc.); AgiBot #1 at 5,200, Unitree 4,200, UBTech 1,000; ~90% Chinese |
| Unitree — STAR IPO prospectus (filed 2026-03) | >5,500 (own units only) | Units "actually sold and delivered to end customers" — orders were higher, and mass-production output was >6,500; bipedal humanoids only, wheeled models excluded; claims the top global share (~32% per one prospectus read — single-source, unverified), which would imply a ~17k global market |
| Morgan Stanley (analyst Sheng Zhong, 2026-06) | >16,000 deployed globally in 2025; China >80% | External sales only — explicitly excludes prototypes, trial units, and internal-use builds; the baseline for its China-only 2026 forecast, raised 14k → 28k → 50k over H1 2026 |

Why they diverge:

- **Shipments ≠ production ≠ orders**: Unitree alone reports three numbers (>5,500 delivered, >6,500 produced, orders higher still); trackers sample different points in this funnel.
- **Form-factor scope**: whether wheeled/dual-arm platforms count as "humanoids." Unitree's figure explicitly excludes its wheeled models; scope differences like this are the likely wedge between Omdia's ~13k and IDC's ~18k, and behind the AgiBot-vs-Unitree #1 dispute — both claim the 2025 top spot (likely wedge: inference, unverified).
- **China-only vs global**: Morgan Stanley's widely quoted 50,000-unit 2026 forecast covers China only; Omdia/IDC totals are global (~80–90% Chinese either way).
- **Vendor-level disagreement persists**: Omdia and IDC both credit Unitree with 4,200 units, ~24% below Unitree's own prospectus disclosure — a sign of how immature humanoid market tracking still is (press coverage notes demo/test units are hard to separate from sales).

Wiki convention: quote 2025 global humanoid shipments as "~13,000–18,000 depending on tracker" with attribution, and treat any single-company #1 claim as disputed.

## Locomotion

Deep dive: [Locomotion](locomotion.md).

- Whole-body RL control is effectively solved for flat-ground walking and increasingly for acrobatics: Unitree G1/H2 humanoids performed a fully autonomous cluster kung-fu routine ("WuBOT") — aerial flips exceeding 3 m, table vaults, wall-assisted backflips, cluster speeds up to 4 m/s — at China's Spring Festival Gala (2026-02-16, Unitree's third Gala appearance).
- Research frontier moved to **single-policy versatility**: one learned policy handling walking/jumping/standing/hopping with real-time adjustable gait parameters while tolerating arbitrary upper-body manipulation commands (e.g., HugWBC), plus general motion-tracking policies that imitate arbitrary human motion capture.
- **Perceptive parkour and skill-chaining** (2026 papers: Deep Whole-body Parkour, motion-matching skill chains) extends this to vision-conditioned dynamic terrain traversal.
- Enabler: massively parallel GPU physics simulation ([Simulation](simulation.md)) — thousands of environments per GPU — remains the standard training recipe; sim-to-real for locomotion is now routine, in contrast to manipulation.

## Manipulation

Deep dive: [Manipulation](manipulation.md); hands and actuators in [Hardware](hardware.md).

- Dexterous five-finger manipulation is widely cited as **the** biggest unsolved problem in practical robotics: deformable objects, human tools, small-part assembly.
- Hardware race: Tesla Optimus V3 hands carry 25 actuators per forearm/hand (~4.5× Gen 2); Figure 03 hands add fingertip tactile sensing and palm cameras; sub-$25k commercially viable dexterous hands projected for 2027 (analyst projection, unverified).
- Model race: π0.7's laundry folding/espresso making at claimed specialist-level throughput; RLWRLD RLDX-1 trains from bare-human-hand video with a retargeting stack; NVIDIA GR00T N1.7 markets "advanced dexterous control."
- Tactile benchmarking is emerging (Daimon Robotics + Galbot's RobOmni, ICRA 2026) but there is no accepted community-wide dexterity benchmark yet — see [Open problems](open-problems.md).

## World models

Deep dive: [World models](world-models.md).

- **Genie 3** (DeepMind, announced 2025-08-05): prompt-to-interactive-world at 720p/24fps with multi-minute consistency; productized as "Project Genie" for AI Ultra subscribers (2026-01-29). Closed API only.
- **NVIDIA Cosmos 3** (launched 2026-05-31, GTC Taipei): open-source "omnimodal" world foundation model — mixture-of-transformers pairing a reasoning transformer (Reasoner) with a generation expert (Generator) — trained on ~20T tokens spanning text, image, ~400M videos, audio, and robot/human action trajectories; variants Super/Nano/Edge; top rankings claimed on Physics-IQ, PAI-Bench, RoboLab; adopters include Skild AI, Agile Robots, LG, Samsung, Doosan, Li Auto.
- **Convergence with policies**: GR00T N2's "world action model" (DreamZero) and π0.7's internal world model for visual subgoals signal that world models are becoming part of the policy, not just the simulator. This is arguably the defining architectural bet of 2026 — see [Tech tree](tech-tree.md).

## Compute, platforms, and ecosystem

- NVIDIA is the de facto platform layer: Jetson Thor onboard compute, Isaac Sim/Lab, Cosmos world models, GR00T policies, plus an open **Isaac GR00T reference humanoid** design (built with Unitree, available late 2026) for academia (Ai2, ETH Zurich, Stanford, UCSD). See [Hardware](hardware.md) and [Simulation](simulation.md).
- Incumbent industrial robotics (FANUC, ABB, Yaskawa, KUKA — combined install base >2M robots) is integrating NVIDIA Omniverse libraries and Isaac simulation frameworks into virtual-commissioning workflows rather than building foundation models in-house (as of GTC 2026-03).
- Data remains the moat: teleoperation fleets, human-video pretraining, and synthetic generation via world models are the three competing recipes — see [Data](data.md).

## Investment snapshot (as of 2026-07)

Details and history in [Investment](investment.md).

| Company | Latest round | Valuation |
|---|---|---|
| Figure | $1B+ Series C (2025-09) | $39B post-money |
| Skild AI | $1.4B Series C (2026-01-14, SoftBank-led; Nvidia, Bezos) | >$14B |
| Physical Intelligence | ~$1B round in progress (reported 2026-03) | >$11B target (unverified until closed) |
| Apptronik | $520M Series A extension (2026-02-11) | ~$5.3B reported post-money |
| Unitree | Shanghai STAR IPO: listing review passed 2026-06-01, CSRC registration approved 2026-07-02 (~$618M raise); pricing/subscription next, debut possibly late July 2026 (press reports, unverified) | ~$6.2B target (per Caixin) |

- Physical-AI startups raised >$6.4B across 27 deals in Q1 2026 alone (single tracker, unverified); full-year dedicated humanoid investment projected >$20B if H1 pace holds (projection, unverified).

## What is *not* state of the art yet

Cross-reference: [Open problems](open-problems.md).

- No humanoid runs a full shift of economically-positive, unattended, multi-task work; deployments are narrow-task fleets with human oversight.
- Dexterous manipulation, long-horizon error recovery (>10 min tasks are the frontier, per π's embodied-memory work), and trustworthy real-world evaluation remain open.
- Sim benchmarks (LIBERO/CALVIN) are saturated and no longer informative; RoboArena-style zero-shot real evaluation is young.
- Safety certification for humanoids around untrained humans (homes, public spaces) has no settled standard; 1X NEO's 2026 home deliveries will be the first large test.

## Sources

- https://www.pi.website/ — Physical Intelligence model timeline (π0 → π0.5 → π*0.6 → π0.7) and research posts
- https://www.pi.website/blog/pi07 — π0.7 release details, steerability, evaluation claims (2026-04-16)
- https://deepmind.google/blog/gemini-robotics-er-1-6/ — Gemini Robotics-ER 1.6 capabilities and benchmark numbers (2026-04-14)
- https://deepmind.google/blog/gemini-robotics-15-brings-ai-agents-into-the-physical-world/ — Gemini Robotics 1.5 agentic stack, motion transfer, 15-benchmark SOTA claim
- https://arxiv.org/pdf/2510.03342 — Gemini Robotics 1.5 technical report; source of the ER 1.5 "15 academic embodied-reasoning benchmarks" aggregate-SOTA claim
- https://nvidianews.nvidia.com/news/nvidia-launches-cosmos-3-the-open-frontier-foundation-model-for-physical-ai — Cosmos 3 launch, architecture, openness, partners (2026-05-31)
- https://nvidianews.nvidia.com/news/nvidia-and-global-robotics-leaders-take-physical-ai-to-the-real-world — GTC 2026 GR00T N2 preview, MolmoSpaces/RoboArena #1 claims, partner ecosystem (2026-03-16)
- https://nvidianews.nvidia.com/news/nvidia-open-humanoid-robot-reference-design — Isaac GR00T reference humanoid with Unitree, academic partners
- https://mbreuss.github.io/blog_post_iclr_26_vla.html — ICLR 2026 VLA field survey: 164 submissions, benchmark saturation, trends
- https://www.figure.ai/news — Figure timeline: Helix 02, Figure 03, BMW deployments, $39B Series C
- https://www.press.bmwgroup.com/global/article/detail/T0455864EN/ — BMW Germany humanoid pilot (Leipzig, summer 2026, with Hexagon Robotics' AEON); Spartanburg Figure 02 pilot results (2026-02-27)
- https://www.press.bmwgroup.com/global/article/detail/T0458778EN/ — BMW press release: Figure 03 logistics-sequencing project at Spartanburg (2026-06-25)
- https://techcrunch.com/2026/04/16/physical-intelligence-a-hot-robotics-startup-says-its-new-robot-brain-can-figure-out-tasks-it-was-never-taught/ — independent confirmation of π0.7 release and claims (2026-04-16)
- https://www.bloomberg.com/news/articles/2026-03-27/ex-deepmind-staffers-robotics-startup-in-talks-for-11-billion-valuation — Physical Intelligence in talks for ~$1B at >$11B valuation (2026-03-27)
- https://techcrunch.com/2026/01/14/robotic-software-maker-skild-ai-hits-14b-valuation/ — Skild AI $1.4B Series C at >$14B, SoftBank-led (2026-01-14)
- https://www.caixinglobal.com/2026-07-03/unitree-robotics-wins-approval-for-618-million-star-market-ipo-102460136.html — Unitree CSRC registration approval (approved Thursday 2026-07-02, reported 2026-07-03), ~$618M raise, 2025 financials
- https://www.stcn.com/article/detail/3735182.html — Securities Times: Unitree 2025 GAAP net profit ~¥288M ("近3亿"); companion filing-stage piece (stcn.com 3688950) identifies the >¥600M figure as 扣非净利润 (excl. non-recurring items), +674.29%
- https://www.scmp.com/tech/tech-trends/article/3340446/chinas-unitree-ships-more-5500-humanoid-robots-2025-surpassing-us-peers — Unitree 5,500+ shipped / 6,000+ produced in 2025 (via 36Kr/insider, bipedal only, wheeled excluded; Unitree declined comment); Omdia's ~150-unit counts for Tesla/Figure/Agility
- https://technode.com/2026/01/09/chinas-agibot-leads-global-humanoid-robot-shipments-in-2025-omdia-says/ — Omdia Market Radar: ~13k global 2025 shipments; AgiBot 5,168 (39%), Unitree 4,200, UBTech 1,000
- https://www.forbes.com/sites/johnkoetsier/2026/01/09/top-10-humanoid-robot-companies-by-shipments-revealed/ — Omdia full top-10 table and 13,317-unit global total; notes sales/demo/test-unit ambiguity
- https://www.globaltimes.cn/page/202601/1354054.shtml — IDC Global Humanoid Robot Market Analysis: ~18,000 units 2025, +508% YoY, AgiBot #1 at 5,200 (the figure carried by Xinhua/state media)
- https://www.humanoidsdaily.com/news/unitree-files-for-580m-ipo-humanoid-sales-surpass-robot-dogs-as-profits-soar — Unitree prospectus: 5,500 humanoids 2025, wheeled excluded, humanoids >51% of revenue
- https://roboticsandautomationnews.com/2026/03/31/unitree-robotics-files-for-610-million-ipo-as-humanoid-robot-sales-surge/100272/ — Unitree prospectus definitions: >5,500 "sold and delivered to end customers," orders higher, output >6,500
- https://www.scmp.com/tech/article/3358210/morgan-stanley-raises-china-humanoid-robot-shipment-forecast-50000-units — Morgan Stanley raises China-only 2026 forecast to 50,000 (from 28,000; 446,000 by 2030), 2026-06-24
- https://www.cryptopolitan.com/morgan-stanley-doubles-chinas-humanoid-shipment-target-to-50000/ — Morgan Stanley methodology (external sales only, excl. prototypes/trials/internal use); >16,000 deployed globally 2025, China >80%; analyst Sheng Zhong
- https://www.prnewswire.com/news-releases/kung-fu-meets-spring--unitree-spring-festival-gala-robots-present-cyber-real-kung-fu-in-the-year-of-the-horse-302689291.html — Unitree autonomous kung-fu at Spring Festival Gala (2026-02-16)
- https://www.eweek.com/news/tesla-optimus-robot-2027-sale/ — Musk: Optimus consumer sales targeted end of 2027 (Davos, 2026-01)
- https://techcrunch.com/2026/02/19/toyota-hires-seven-agility-humanoid-robots-for-canadian-factory/ — Toyota Woodstock 7-Digit RaaS contract (2026-02)
- https://www.agilityrobotics.com/content/digit-moves-over-100k-totes — Digit 100,000+ totes at GXO Flowery Branch
- https://blog.google/innovation-and-ai/models-and-research/google-deepmind/project-genie/ — Project Genie rollout to AI Ultra subscribers (2026-01-29)
- https://www.figure.ai/news/figure-signs-agreement-with-catalyst-brands — Figure–Catalyst Brands logistics agreement (2026-05-26)
- https://www.trendforce.com/presscenter/news/20260409-13007.html — China humanoid output +94% 2026 forecast, Unitree/AgiBot share
- https://restofworld.org/2026/unitree-china-humanoid-robot-shanghai-ipo/ — Unitree $608M Shanghai IPO filing
- https://www.techtimes.com/articles/317632/20260602/unitree-ipo-cleared-agibot-hits-10000-units-china-humanoid-robot-duopoly-takes-shape.htm — Unitree IPO approval 2026-06-02; AgiBot 10,000th unit
- https://electrek.co/2026/04/22/tesla-optimus-production-fremont-model-sx-line/ — Optimus V3 production timing, Fremont line conversion
- https://www.automate.org/robotics/industry-insights/boston-dynamics-to-begin-production-on-redesigned-atlas-humanoid-in-2026 — Atlas production launch at CES 2026, specs, 2026 allocations
- https://www.hyundainews.com/releases/4664 — Hyundai AI robotics strategy, US robot factory
- https://www.therobotreport.com/1x-announces-pre-order-launch-neo-humanoid-robot/ — 1X NEO pricing and pre-order launch
- https://www.forbes.com/sites/johnkoetsier/2026/04/30/1x-kicks-off-full-scale-production-of-humanoid-robot-neo/ — NEO full-scale production, factory capacity
- https://techcrunch.com/2026/02/11/humanoid-robot-startup-apptronik-has-now-raised-935m-at-a-5b-valuation/ — Apptronik funding
- https://news.crunchbase.com/venture/ai-humanoid-robot-funding-apptronik/ — humanoid funding context, Skild $14B, PI $11B talks
- https://www.therobotreport.com/rlwrld-releases-rldx-1-a-dexterity-first-foundation-model-for-robot-hands/ — RLDX-1 dexterity foundation model
- https://deepmind.google/blog/genie-3-a-new-frontier-for-world-models/ — Genie 3 capabilities (720p/24fps real-time interactive worlds)
- https://arxiv.org/pdf/2510.13626 — LIBERO-Plus robustness analysis (benchmark saturation evidence)
- https://www.benzinga.com/markets/tech/26/07/60209589/elon-musk-says-teslas-model-s-model-x-line-is-now-building-optimus-robots — Musk photo post from first Fremont Optimus line (2026-07-01); Moravy: line landed, installation begun
- https://www.prnewswire.com/news-releases/ubtech-launches-uworld-u1-the-worlds-first-full-size-mass-produced-ultra-bionic-humanoid-robot-302815272.html — UBTech UWORLD U1 consumer launch (2026-06-30), pricing, order claims
- https://apptronik.com/news-collection/welcome-to-robot-park-where-apptroniks-apollo-goes-to-work — Apptronik Apollo 2 + Robot Park unveiling (2026-06-30)
- https://news.futunn.com/en/post/75500836/robotics-sector-surges-unitree-technology-s-star-market-ipo-registration — Unitree IPO registration effective; possible late-July 2026 debut (press report)
