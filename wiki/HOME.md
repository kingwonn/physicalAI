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
| [State of the Art (2026-07)](state-of-the-art.md) | Hub snapshot of the frontier: leading VLAs, first commercial humanoid fleets (BMW/GXO/Toyota), shipment shares, record capital |
| [Physical AI Tech Tree](tech-tree.md) | Layered dependency map (hardware → perception → control → learning → foundation models → deployment) with per-branch bottlenecks |
| [On-Device Embodied Brain](on-device-brain.md) | Deep technical+strategic report on building a good edge robot brain: dual/tri-system arch (S2 5-10Hz / S1 100-200Hz / S0 500Hz-1kHz), cloud-edge split, compute/model-opt, SoC landscape, power, software, edge models, eval rubric, reference architecture + module-maker read |
| [Visions & Theses](visions.md) | How the leaders frame Physical AI — dated primary quotes from Huang, Musk, Hassabis, Li, LeCun, Son, Wang Xingxing + the skeptic counterweight; convergence/divergence matrix |

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
