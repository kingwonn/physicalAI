---
title: HOME — physicalAI wiki index
slug: HOME
updated: 2026-07-03
confidence: verified
---
> Annotated index of the physicalAI wiki: 37 topic pages on Physical AI worldwide,
> each researched by a web-research agent and passed through an adversarial
> fact-check (`confidence: verified`). Start with the three core pages, then go
> deep by technology, people/orgs, region, or capital.

## Field overview (as of 2026-07)

Physical AI crossed from demos into first commercial deployments in 2025-26.
Generalist vision-language-action models (π0.7, Gemini Robotics 1.5, GR00T N2,
Helix 02) define the model frontier; world models are converging with policies
as the defining 2026 architecture bet. China ships ~90% of humanoid volume on a
deep component supply chain and sub-$6k price disruption, while US labs hold the
frontier-model lead and record capital ($39B Figure, $14B Skild valuations).
The binding constraints, per the [tech tree](tech-tree.md): robot data scale,
dexterous hands/tactile sensing, and deployment reliability. The field's live
disputes are catalogued in [Open problems](open-problems.md).

## Core (read first)

| Page | What it covers |
|---|---|
| [History of Physical AI](history.md) | Unimate (1961) and Shakey → deep-RL/sim2real era → the 2022-26 robot-foundation-model turn and the humanoid mass-production wave |
| [Lineage: Embodied Cognition & Behavior-Based Robotics](lineage-embodied-cognition.md) | The pre-2022 philosophical/scientific lineage behind "embodiment," "grounding," "affordance" — Brooks' subsumption architecture + physical grounding hypothesis, Gibson's affordances, Varela/Thompson/Rosch enactivism, Pfeifer/Bongard morphological computation, Braitenberg, Thelen & Smith, Asada/Cangelosi developmental robotics, Friston's contested free-energy principle, Lakoff & Johnson — primary citations, verbatim quotes, and the testable predictions each strand makes about what disembodied AI can't do |
| [Lineage: Learning & Control — the Engineering Throughline](lineage-learning-control.md) | The parallel engineering lineage (1960s-2026): Kalman filter/LQR/MPC, Raibert's dynamic-balance legged robots (with a flagged "controlled falling" mis-citation), Sutton/Barto RL + TD-learning + the Bitter Lesson (verbatim) vs. Brooks' dated rebuttal "A Better Lesson," Schaal/Atkeson/Ross(DAgger) imitation learning, Levine/Abbeel deep-RL + domain randomization + OpenAI Dactyl, the RT-2 paper's exact "VLA" coinage, Sutton's Dyna + Schmidhuber's contested 1990 world-model priority claim vs. LeCun + Ha&Schmidhuber's verbatim "hallucinated dream," and Smith & Gasser's explicit "embodiment hypothesis" vs. Sutskever's substrate-independence quote |
| [State of the Art (2026-07)](state-of-the-art.md) | Hub snapshot of the frontier: leading VLAs, first commercial humanoid fleets (BMW/GXO/Toyota), shipment shares, record capital |
| [Physical AI Tech Tree](tech-tree.md) | Layered dependency map (hardware → perception → control → learning → foundation models → deployment) with per-branch bottlenecks |
| [On-Device Embodied Brain](on-device-brain.md) | Deep technical+strategic report on building a good edge robot brain: dual/tri-system arch (S2 5-10Hz / S1 100-200Hz / S0 500Hz-1kHz), cloud-edge split, compute/model-opt, SoC landscape, power, software, edge models, eval rubric, reference architecture + module-maker read |
| [Visions & Theses](visions.md) | How the leaders frame Physical AI — dated primary quotes from Huang, Musk, Hassabis, Li, LeCun, Son, Wang Xingxing + the skeptic counterweight; convergence/divergence matrix |
| [Physical AI: Portrait & Essential Patterns](physical-ai-essence.md) | The field-level capstone: the complete portrait (stack pyramid, load-bearing numbers, three running plots) + 8 essential X-patterns beneath the business layer (skill-capitalization engine, embodiment-tax contact gradient, three atomic irreversibilities, clock-layering law, dual-clock phase lag, metrology-lemon unification, factor-endowment mirror, pricing-power topology) — X1 skill-capitalization adjudicated deepest with an explicit generation chain down to P1-P8 and an honest dethrone clause |

## Technology

| Page | What it covers |
|---|---|
| [Vision-Language-Action Models](vla-models.md) | RT-1/RT-2 → π0/π0.5/π*0.6, GR00T N1-N2, Gemini Robotics 1.x, Helix 02: architectures, action decoding, training data, open-vs-closed, benchmarks |
| [World Models for Robotics](world-models.md) | Cosmos, Genie 3, 1X world model, V-JEPA 2, Tesla's neural simulator — learned simulators, planners, policy evaluators, data engines |
| [Dexterous Manipulation](manipulation.md) | Grippers vs dexterous hands, tactile sensing, ALOHA/Diffusion-Policy/UMI lineage, the 2026 capability frontier |
| [Legged Locomotion](locomotion.md) | ZMP/MPC → massively-parallel sim-to-real RL: standard training recipes, parkour milestones, field robustness |
| [Simulation & Sim2Real](simulation.md) | GPU-parallel simulators, domain randomization, synthetic-data pipelines as the scalable middle tier of the data strategy |
| [Hardware Substrate](hardware.md) | Actuators, dexterous hands, tactile/force sensing, onboard compute, batteries, BOM cost curves, China-dominated supply chain |
| [The Robot Data Problem](data.md) | Teleop, egocentric human video, sim data, open datasets, commercial data factories, first scaling-law evidence |
| [Data-Collection Devices & Rigs](data-collection-devices.md) | The hardware of data: embodiment-free (UMI/DexUMI/Dobb·E/gloves/egocentric) vs teleop (ALOHA 2/VR/mocap/exo) vs on-robot — 60 devices, a 3-family tradeoff matrix (cost/throughput/embodiment-gap/action-fidelity/scalability) with critical verdicts, per-system engineering-design breakdowns (sensing→pose-recovery→data-format), and the China data-collection ecosystem (星海图/松灵 Cobot Magic/帕西尼/光轮/数据训练场 + "genrobot" resolved) |
| [Tactile Sensing & Dexterous Hands](tactile-hands.md) | Hand landscape with prices, GelSight-lineage vs taxel arrays, tactile datasets/models, China's hand mass-production economics, why dexterity hardware remains the gap |
| [Humanoid Component Supply Chain](component-supply-chain.md) | BOM-money-and-chokepoint map + per-sub-chain supplier scoreboards (谐波/RV减速器, 行星滚柱丝杠, 无框电机, 灵巧手, 六维力/触觉传感器); China localization vs imports; roller-screw chokepoint; module-maker (Quectel) read |
| [Data Foundry Economics](data-foundry.md) | The business of manufacturing robot data: Scale post-Meta, Generalist's wearables foundry, China's state-subsidized data factories, teleop $/hour economics, marketplaces |
| [SOTA Data-Engine Design & 3-Gen Roadmap](data-engine-roadmap.md) | **Design proposal** (not survey): our own SOTA data-collection system derived from brain-scaling needs — W/L/R three-terminal data spine, Gen-1 COTS ($520 wearable, 0-6mo) → Gen-2 custom sensor-head module (2mm/200Hz, 6-15mo) → Gen-3 custom C1 SoC + future sensors (1µs on-chip sync, 15-24mo); judge-panel synthesis (C 140/B 131/A 125), dated endgame (2028/2030/terminal) with falsifiers |
| [LeCun World Models vs Our Data Engine](lecun-worldmodels-rethink.md) | Critical collision test: LeCun's ETH Zürich 2026-05-29 world-models talk (primary-confirmed) summarized faithfully, claim-by-claim collision with our verified scaling evidence, steelman + track-record critique, and the roadmap rethink — spine survives, passive ego-video upgraded to co-primary product line, new pretrain-vs-label gate ablation, force data gains a third buyer (world-model physics calibration) |
| [Data-Engine Blueprint & Hardware Implementation](data-engine-blueprint.md) | The engineering layer: closed-loop 5-plane system architecture (device/clock/data/QC-cert/brain planes with per-plane invariants), interface-contract table, data/power/timing budget arithmetic, buildable W1/W1e/L1/R1/dock implementations (electrical/firmware/mechanical/calibration/EVT-DVT-PVT), data-spine shard+cert schemas, Gen-2 dual-source sensor-head board plan — 6 inline integration arbitrations (e.g. RK3588 has no AV1 hw-encode → site transcode node), 12 verify fixes |
| [First-Principles Data Engine (Clean-Room)](data-engine-first-principles.md) | The control experiment: strip ALL vendor/commercial constraints, re-derive products + 3 generations from 12 axioms (incl. measurement back-action, measured-relative label class, utilization-inversion economics) via two independent designers — product family re-cast as Cicada (passive worn) / Mantis (handheld GS-stereo) / Anvil (metrology instrument) + Gen-2 CORE shared board; 18-row delta attribution vs the old roadmap (~6.5 equivalent / 4.5 first-principles / 4.5 commercial residue / 1.5 vendor residue); biggest delta: the chirp architecture eliminated by an $8 single-clock island (≤50µs constructive); silicon fully optioned; 12-item invariant core |
| [Case Study: MiFeng/Maniformer — Full Dossier](case-mifeng.md) | The definitive Maniformer dossier: company profile + product teardown + 资料全录 (every interview/launch-event/site+marketplace deep-read incl. hidden /api/news, patents/hiring/open-source incl. negative findings, claim-propagation map exposing one-press-release echo chains and the refuted 29k-stars number) + critical synthesis (claims-density vs disclosure-density; the reproducible id=341 NULL defect) + axiom collision + revision instructions + sentinel table with programmatic API polling |
| [Our Direction & Maniformer-Aware 3-Gen Plan v2](data-engine-v2.md) | The response: honest no-go list (anchor buyer/capital/volume/brand-blitz — we forfeit), three structural voids graded by defensibility (metrology / neutrality — their 75% AgiBot equity makes every rival body-maker our natural customer / open-auditable), positioning: "不与觅蜂争数据货架,做具身数据的度量衡"; 10 targeted design principles (disclosure-as-weapon spec sheet, multi-body jaw cartridges vs G2-Air lock, error-distribution report as shipping feature), 3-gen deltas on the clean-room base + new G-J gate, head-to-head table, they-close-the-gap response plan (≤4-week counter) |
| [Dossier: GenRobot 简智新创](case-genrobot.md) | Closest pure-play peer: DAS 5-device lineup + Gen Matrix; CEO 陈建兴 (RoboMaster/小鹏→Momenta); the most open-source of the Chinese pack (real GitHub/HF orgs); novice-friendly full workup with explicit unknowns |
| [Dossier: 鹿明 Lumos Robotics](case-luming.md) | Identity resolved (Shenzhen; founder 喻超, Tsinghua + ex-Dreame humanoid lead): robots + collectors + data-mart triple line; ~¥1B cumulative funding, A1/A2 led by Mitsubishi Electric |
| [Dossier: 它石智航 TARS](case-morphic.md) | Brand corrected (our prior "Morphic" label was our own error — zero external sources): TARS-Vision/Glove wearables, WIYH dataset, industrial-robot GTM with self-used collection; founders 陈亦伦/李震宇/丁文超/陈同庆 |
| [Dossier: 灵初智能 PsiBot](case-lingchu.md) | The data-glove bet: CEO Viktor Wang 王启斌, chief scientist 杨耀东; ¥2.0B angel+Pre-A (2026-03); distinct from BeingBeyond; dexterous-first thesis |
| [Dossier: 京东具身数据业务](case-jd-data.md) | The platform giant: 探索研究院 Joy Future Academy (何晓冬) + robotdata.jdcloud.com data-trading platform; headsets to gig collectors; 2 arXiv papers; HF org exists with zero public datasets — internalize-vs-sell unresolved |
| [Dossier: Generalist AI](case-generalist.md) | The US benchmark: Pete Florence/Andy Zeng/Andy Barry; $400M led by Radical Ventures (2026-06), ~$2B valuation, >$500M total; devices strictly self-used — sells capability, not data or hardware |
| [Dossier: 星海图 Galaxea AI — Data Business](case-galaxea.md) | The reverse pattern vs Maniformer: robot-maker-first (R1/R1 Pro/R1 Lite/Kengo humanoid), founders 高继扬(CEO)/赵行/许华哲/李天威 all verified; Galaxea Open-World Dataset (arXiv 2509.00576, 16,610 HF downloads/mo, 400k-cumulative press claim reconciles with steady-state); new Galaxea Data Hub (1.27M-hour claim single-sourced, ISO/IEC 23053:2024 "certification" is a misapplied standard number); named customers (Huawei Cloud/VW/Haier/Samsung/ByteDance/Stanford/MIT) but data-vs-hardware revenue split undisclosed; data business organized as a govt-backed JV (亦数智能, Beijing Yizhuang) not a controlled spin-out — direct answer to "would they spin out like Maniformer" |
| [Category Scoreboard: 数采公司全景横评](data-companies-compare.md) | All 7 dossiers on one table: vision/products/tech-disclosure grades/GTM/funding/biggest unknown; 2×2 grid placement; claims-density vs disclosure-density ranking; category-level information voids (nobody publishes error distributions) — our metrology lane confirmed vacant category-wide |
| [Dossier: 松灵 AgileX](case-agilex.md) | The commodity-rig vendor: DJI-lineage chassis maker (Dongguan, 2017) that pivoted a product line into the data rush — Cobot Magic/PiPER economics, nine years of hardware cash flow, no funding since 2021; the "sell shovels and survive" archetype |
| [Dossier: 帕西尼 PaXini](case-paxini.md) | The tactile-component vendor: Waseda-lineage founder 许晋诚, sensor price collapse 10万→¥199 (~500×), customer-shareholder overlap (BYD/JD/TCL/商汤), HK-IPO pipeline — the category's first forced-disclosure event when the prospectus lands |
| [Dossier: 光轮 LightWheel](case-lightwheel.md) | Synthetic-data-as-a-service: ex-Cruise/NVIDIA founder 谢晨, NVIDIA GR00T/Newton ecosystem node, revenue >¥100M claimed (unaudited), CN/EN order books that do not reconcile — the sim-first AV-playbook transplant that worked best |
| [Dossier: 星海图 Galaxea(数据业务)](case-galaxea.md) | Robot-maker-with-open-data: CEO 高继扬 (Waymo→Momenta) + 赵行/许华哲; Open-World dataset as ecosystem play; "127万 hours"+wrong-ISO-number single-source flagged; government JV holds the data platform |
| [Dossier: Scale AI 机器人业务](case-scale.md) | The labeling giant's pivot: Physical AI unit (2025-09, GM Ben Levin — since poached by NVIDIA), UR/Teradyne AI Trainer partnership, 150k+ delivered hours, the only named-external-buyer business in the category; Meta owns 49% |
| [数据生意的底层 Pattern](data-business-patterns.md) | The answer to "what pattern connects 12 companies": 8 named patterns (AV-sequel, two-layer convergence, parent+state-pays, shovels-priced-gold-unpriced, lemon equilibrium, open≠metrology, annexation endgame, pulse+fracture-order) each with evidence/counterexample/dated falsifiable prediction; the self-critical centerpiece adjudicates WHY the metrology lane is empty (H2 no-paying-buyer strongest) and DOWNGRADES our lane-1 from revenue line to instrument-backed option — 4 revision verdicts written back into data-engine-v2 |
| [Data-Scaling Channel & Optimal Strategy](data-scaling-strategy.md) | The decision page: 3-lens red-team re-review of our own roadmap (spine survives, 4 fatal fixes: C1 downgrade, revenue gate, R-series white-label, ladder arithmetic rebuild); bull/bear/referee panel on "can data scaling open an LLM-style channel" (our estimate P(full channel@2030)≈0.30 — the channel is an economics inequality: $/h must fall ~10×/OOM, observed 2–3×); the 3-world ownership map and 7-principle optimal strategy (barbell, dual gates, sell-picks-own-the-ruler) + the 3-step ODM translation ("sell the scale first, then decide on the granary") |
| [Evaluation & Benchmarks](evaluation.md) | Saturated sim suites vs real-robot arenas (RoboArena, RoboChallenge, GM-100), embodied-reasoning exams, industry throughput metrics, the self-reported-benchmark credibility problem |

## People & organizations

| Page | What it covers |
|---|---|
| [Key People](key-people.md) | Researchers, US/Europe founder-executives, China's humanoid founders; 2024-26 moves and talent flows |
| [Organizations: Global Who's-Who](organizations.md) | Reference table of companies, big-tech divisions, academic labs, national programs — funding, flagship results, scale |
| [Academic Lab Map](academic-labs.md) | Global lab map with PIs, signature datasets/benchmarks, lab→startup pipelines, and the Google-diaspora talent flows |

## Regional landscapes

| Page | What it covers |
|---|---|
| [Landscape: USA & Canada](landscape-usa.md) | Company-by-company map: humanoid makers, robot-brain labs, NVIDIA's platform play, big tech, academia, funding climate |
| [Landscape: China](landscape-china.md) | ~90% of 2025 humanoid volume: Unitree/AgiBot/UBTech, supply chain, Five-Year-Plan policy, price disruption, IPO wave |
| [Landscape: Europe, Japan, Korea & RoW](landscape-row.md) | Europe's venture champions, Japan's incumbents + sovereign foundation-model JV, Korea's chaebol push, Israel/India/Gulf |

## Capital & frontier

| Page | What it covers |
|---|---|
| [Investment & Market](investment.md) | As-of-dated ledger of mega-rounds, valuations, IPOs, state funds, market forecasts — with bubble-watch skepticism |
| [ODM Opportunity Map](odm-opportunity.md) | Where contract manufacturers fit: honest market bound (~$2B hardware pool 2026), value-chain entry map, ODM/EMS competitor scoreboard (Jabil/Foxconn/Lens/Luxshare…), timing and strategic-options matrix |
| [ODM/EMS Competitor Landscape](odm-competitors.md) | Deep commitment-ranked scoreboard of 16 ODM/EMS/module makers (Foxconn, Luxshare, Longcheer, Lens, Huaqin, Quanta, Fibocom, MeiG…) across product-line / investment / design-win / deployment — own-brand vs arms-dealer split |
| [Open Problems & Debates](open-problems.md) | Data scarcity, sim2real limits, dexterity gap, reliability, safety certification, evaluation crisis, form-factor and timeline debates |
| [Safety & Regulation](safety-regulation.md) | ISO 25785-1 / 10218:2025 / UL 3300, EU Machinery Regulation + AI Act, China's HEIS, certification gates for factory and home deployment, incidents and insurance |

## Company deep dives

| Page | What it covers |
|---|---|
| [Figure AI](company-figure.md) | Founding, $2.6B→$39B funding arc, Helix architecture, BotQ manufacturing, BMW engagement (confirmed vs aggregator claims), OpenAI split, skeptic case |
| [Unitree](company-unitree.md) | XDog-to-IPO arc, full price ladder, prospectus financials, STAR IPO status, vertical integration, viral milestones, safety incidents, US scrutiny |
| [Physical Intelligence](company-pi.md) | Google-diaspora founding, ~$1.07B raised, π0→π0.7 model arc, openpi ecosystem, pre-revenue posture, skeptic case |
| [NVIDIA Robotics Stack](company-nvidia.md) | Three-computer thesis, Isaac/GR00T/Cosmos/Jetson/Halos, partnership graph, ~1%-of-revenue reality vs $40T TAM rhetoric, platform-bet challengers |
| [Tesla Optimus](company-optimus.md) | Generation timeline, Musk claims-vs-delivery ledger, Fremont line status, AI5 silicon, supply-chain choke points, demo skepticism record |
| [Boston Dynamics](company-bostondynamics.md) | 100% Hyundai-owned pivot from research theater to production Atlas; partner-built brain; 25,000+ captive units; Spot/Stretch economics |
| [Agility Robotics](company-agility.md) | Boring-warehouse-work-first thesis, $2.5B SPAC (Foxconn PIPE), most documented deployment record, RaaS economics |
| [1X Technologies](company-1x.md) | Home-first consumer bet, tendon-driven safety hardware, teleop data flywheel, $20K NEO, delivery-risk falsifiers |
| [Skild AI](company-skild.md) | Omni-bodied brain at >$14B, revenue-first contrast to PI, In-Q-Tel/defense angle, SoftBank convergence |
| [AgiBot 智元](company-agibot.md) | China volume leader, open data/model ecosystem (AgiBot World, GO-1), ODM/EMS-partnered manufacturing (Lens JV), HK IPO path |
| [UBTech 优必选](company-ubtech.md) | First listed humanoid maker, Walker S2 industrial ramp, U1 consumer launch, losses-vs-order-book financial reality |

## Reference

| Page | What it covers |
|---|---|
| [Glossary](glossary.md) | ~35 core terms (models, learning methods, data machinery, actuators, control, business shorthand), each cross-linked to its covering page |

## Meta

- [Loop log](_meta/loop-log.md) — what each loop iteration changed
- [Research queue](_meta/queue.md) — backlog for future iterations
- [LOOP.md](../LOOP.md) — how the maintenance loop works; live HTML console linked in [README](../README.md)
