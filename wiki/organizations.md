---
title: Organizations: Global Who's-Who
slug: organizations
updated: 2026-07-04
confidence: verified
---
> The Physical AI field is organized around four kinds of players: **software-first "robot brain" labs** (Physical Intelligence, Skild AI, Google DeepMind Robotics), **vertically integrated humanoid makers** (Figure, Tesla, 1X, Apptronik in the US; Unitree, AgiBot, UBTech, Galbot in China; Neura in Europe), **big-tech platform divisions** (NVIDIA's Isaac/GR00T stack, Amazon warehouse robotics, Toyota Research Institute, Hyundai/Boston Dynamics), and **academic + state-backed programs** (Stanford, Berkeley, CMU, ETH Zurich, Ai2, China's national innovation centers, Korea's K-Humanoid Alliance). As of 2026-07 the capital league table is led by Figure ($39B valuation), Skild AI ($14B), Neura (~$7B), Unitree (~$6B IPO target), and Physical Intelligence ($5.6B), while China dominates unit volume — Unitree + AgiBot alone are forecast to take ~80% of 2026 humanoid shipments. Deeper regional detail lives in [Landscape: USA](landscape-usa.md), [Landscape: China](landscape-china.md), and [Landscape: rest of world](landscape-row.md).

## Master table — organizations that matter (as of 2026-07)

| Organization | Region | Type | Focus | Flagship result | Scale signal |
|---|---|---|---|---|---|
| Figure AI | USA (San Jose) | Startup | Humanoids + in-house VLA | Figure 03 + Helix 02 whole-body VLA (2026-01) | $39B valuation, >$1.9B raised (as of 2025-09) |
| Tesla | USA | Big-tech division | Humanoid mass production | Optimus V3, Fremont line starting ~2026 summer | Targets Model S/X line conversion; 22-DoF-per-hand V3 (unverified) |
| Physical Intelligence (π) | USA (SF) | Startup (software-only) | Cross-embodiment robot foundation models | π*0.6 w/ RECAP RL (2025-11); π0.7 (2026-04) | $5.6B valuation, >$1B raised (as of 2025-11) |
| Skild AI | USA (Pittsburgh) | Startup (software-only) | "Omni-bodied" Skild Brain | One model controlling arms, quadrupeds, humanoids | $14B valuation after $1.4B SoftBank-led round (2026-01) |
| NVIDIA robotics | USA | Big-tech platform | Full-stack: chips, sim, models | Isaac GR00T reference humanoid (Jetson Thor + Unitree H2 Plus, 2026-05) | De-facto compute/sim monopoly (Isaac Sim/Lab, Cosmos, Thor) |
| Google DeepMind Robotics | USA/UK | Big-tech lab | Agentic VLAs on Gemini | Gemini Robotics 1.5 + ER 1.5 (2025-09) | ER 1.5 in public Gemini API; Apptronik + Agile Robots partners |
| Boston Dynamics | USA (Hyundai-owned) | Corporate subsidiary | Electric Atlas humanoid | LBM-driven whole-body manipulation w/ TRI (2025-08) | Hyundai factory deployment path |
| Toyota Research Institute | USA/Japan | Corporate lab | Large Behavior Models | 450M-param diffusion LBM controlling Atlas end-to-end | Joint BD partnership since 2024-10 |
| Apptronik | USA (Austin) | Startup | Apollo humanoid | Mercedes-Benz + GXO pilots; DeepMind partner | ~$5B valuation, ~$520M raised (as of 2026) (unverified) |
| Agility Robotics | USA (Oregon) | Startup | Digit warehouse humanoid | Digit moving totes at GXO — first humanoid RaaS in production | RoboFab factory; earliest commercial humanoid deployments |
| 1X Technologies | Norway/USA | Startup | Home humanoid (NEO) | NEO home-robot deliveries to early adopters at $20K (2026) | OpenAI-backed; first at-scale home humanoid bet |
| Ai2 (Allen Institute) | USA (Seattle) | Nonprofit lab | Fully open robot FMs | MolmoAct 2 — open weights + 720h bimanual data (2026-05) | Claims wins over π0.5 on manipulation benchmarks |
| Unitree Robotics | China (Hangzhou) | Startup → public | Low-cost humanoids/quadrupeds | G1 (~$16K) volume leader; STAR Market IPO cleared 2026-06, registration approved 2026-07-03 | ~$5.9–6.2B IPO valuation target, ~$618M (¥4.2B) raise |
| AgiBot / Zhiyuan | China (Shanghai) | Startup | Humanoids + GO-1 FM + open datasets | 10,000th unit produced (2026-03); AgiBot World dataset | Backdoor A-share listing in progress |
| UBTech | China (Shenzhen) | Public company | Walker S industrial humanoids | Walker S2 with hot-swap battery; >1,000 units shipped 2025 | HK-listed; auto-factory orders (BYD, Foxconn et al.) |
| Galbot | China (Beijing) | Startup | Wheeled dual-arm retail robots | G1 running unmanned retail stores | ~$3B valuation after ¥2.5B round (2026-03) (unverified) |
| X-Humanoid (Beijing HRIC) | China (Beijing) | State-backed center | Open humanoid platform | Tien Kung robot; open "Hui Si Kai Wu" embodied stack | Founded 2023-11 by Jingcheng + Xiaomi Robotics + UBTech |
| Neura Robotics | Germany | Startup | Cognitive robots + 4NE-1 humanoid | Series C up to $1.4B, Tether-led (2026-06) — Europe's largest | ~$7B valuation; claims >$1B order book (unverified) |
| Fourier | China (Shanghai) | Startup | GR-series humanoids (rehab origin) | GR-3 care-oriented humanoid | Among top-5 China humanoid shippers (as of 2025) |
| Sanctuary AI | Canada (Vancouver) | Startup | Dexterous hands + Phoenix | Hydraulic high-DoF hands | New round closed 2026-05 (amount undisclosed) |
| K-Humanoid Alliance | South Korea | National program | Shared "robot brain" + platform | ~$770M state investment pledged to 2030 | ~40 companies/labs incl. Samsung–Rainbow Robotics |

## Software-first "robot brain" labs

- **Physical Intelligence (π)** — founded 2024, San Francisco, by Karol Hausman, Sergey Levine, Chelsea Finn et al. (ex-Google Brain/DeepMind, Stanford, Berkeley). Trajectory: π0 (2024-10) → open-sourced `openpi` (2025) → π0.5 open-world generalization (2025-04) → **π*0.6 + RECAP** (RL from deployment experience; >2x throughput and ~half the failure rate on hardest tasks incl. laundry folding and a 13h espresso run; 2025-11-17) → Multi-Scale Embodied Memory for ~15-min long-horizon tasks (2026-03) → **π0.7** "steerable" 5B-param generalist with compositional skill recombination (2026-04). Raised $600M led by Alphabet's CapitalG at **$5.6B valuation (as of 2025-11)**; total >$1B. Sells no hardware. See [VLA models](vla-models.md).
- **Skild AI** — founded 2023, Pittsburgh, by CMU professors Deepak Pathak and Abhinav Gupta. "Skild Brain": one **omni-bodied** model for quadrupeds, arms, humanoids, mobile manipulators. **$1.4B Series C led by SoftBank at >$14B valuation (announced 2026-01-14)**, with NVentures, Macquarie Capital, Bezos Expeditions, LG, Schneider Electric, Salesforce Ventures, and returning Lightspeed/Felicis/Coatue/Sequoia; ~$30M revenue ramp in 2025 (unverified). Tripled valuation in ~7 months (from $4.5B in 2025 summer).
- **Google DeepMind Robotics** — Gemini Robotics family on Gemini 2.0+: Gemini Robotics + ER (2025-03), On-Device (2025-06), **Gemini Robotics 1.5 + ER 1.5 (2025-09)** — agentic multi-step reasoning, cross-embodiment transfer demonstrated ALOHA2 → Franka → Apptronik Apollo without retraining. ER 1.5 publicly available via Gemini API; VLA restricted to partners. Hardware partners: Apptronik (humanoids), Agile Robots (2026-03, CNBC).
- **Ai2 (Allen Institute for AI)** — the open-science counterweight: **MolmoAct 2** (2026-05) released weights **plus** 720 hours of bimanual training data, code, and evals; claims wins over π0.5 on real-world manipulation benchmarks (single-source, company blog). Also a named partner on NVIDIA's GR00T reference humanoid.
- Related open efforts: Physical Intelligence's `openpi`, AgiBot's GO-1 + AgiBot World dataset, X-Humanoid's open platform — see [Data](data.md) and [State of the art](state-of-the-art.md).

## Big-tech platform divisions

- **NVIDIA** — sells the picks and shovels for the whole field: Jetson Thor onboard compute, Isaac Sim/Lab simulation, Cosmos world models, GR00T N open robot foundation models, Newton physics engine. At GTC Taipei (2026-05-31) announced the **Isaac GR00T Reference Humanoid Robot**: Unitree H2 Plus chassis (31 DoF) + Sharpa Wave tactile hands (22 DoF each) + Jetson Thor T5000 (2,070 FP4 TFLOPS, 128GB), ~3h battery; sold via Unitree from late 2026; launch research partners Ai2, ETH Zurich, Stanford Robotics Center, UCSD ARCLab. NVIDIA/NVentures also holds stakes in Figure, Skild, Neura, and others — it invests across all competing bets. See [Hardware](hardware.md), [Simulation](simulation.md).
- **Tesla** — Optimus program; V3 design with 22-DoF hands (unverified). Production slated for Fremont on the retired Model S/X line starting ~2026 summer; Musk warns initial output "extremely slow" (~10,000 unique parts) and declined a 2026 volume target; long-term aspiration ~1M units/yr, $20–30K price (aspirational, as of 2026-04).
- **Amazon** — largest robot fleet on Earth (>1M mobile robots as of 2025); Vulcan touch-enabled picking arm (2025-05); DeepFleet foundation model for fleet routing (2025-06). Investor in Agility (earlier) and Neura's 2026 Series C.
- **Hyundai / Boston Dynamics + Toyota Research Institute** — BD's electric Atlas is trained with TRI's Large Behavior Models: a single 450M-param diffusion-transformer, language-conditioned policy controls the whole body (hands and feet treated alike) for long-horizon manipulation + locomotion (2025-08). Deployment path into Hyundai Metaplant manufacturing.
- **SoftBank** — emerging robotics super-aggregator: led Skild's $1.4B round; agreed to acquire ABB's robotics division for ~$5.4B (announced 2025-10) (unverified).
- **Meta** — Reality Labs robotics group building a humanoid software platform (announced 2025-02) (unverified); no shipped robot as of 2026-07.
- **Samsung** — majority stake in Rainbow Robotics (KAIST Hubo lineage) completed 2025; anchor of Korea's K-Humanoid effort (as of 2025).

## China: companies + state apparatus

China ships the large majority of global humanoid units — TrendForce forecasts China's 2026 humanoid output up 94% YoY with **Unitree + AgiBot capturing ~80% of shipments**; one report puts China at ~90% of global units (unverified). Embodied intelligence is named a "future industry" in the national five-year plan; forecast domestic market ~¥870B (~$128B) by 2030 (state-media figure).

| Org | Note |
|---|---|
| Unitree | Price-war leader (G1 ~$16K, R1 entry model ~$6K at 2025 launch); first "embodied AI" company cleared for a STAR Market IPO — listing committee passed 2026-06-01, CSRC registration approved 2026-07-03; ~¥40B (~$5.9–6.2B) target valuation |
| AgiBot (Zhiyuan) | Founded by ex-Huawei "Genius Youth" Peng Zhihui; 10,000 cumulative units (2026-03); GO-1 foundation model; open AgiBot World dataset; listing via reverse takeover |
| UBTech | Walker S series in auto plants; >1,000 units shipped in 2025; HK-listed |
| Galbot | PKU spin-off (Wang He); wheeled dual-arm G1 in unmanned retail; ¥2.5B round (2026-03) |
| Fourier | Shanghai; GR-3 humanoid, rehab-robotics origin |
| X-Humanoid (Beijing HRIC) | State-backed innovation center (Jingcheng + Xiaomi + UBTech, 2023-11); Tien Kung robot won 2025 Beijing robot half-marathon |
| Shanghai Embodied AI Innovation Center | "National and local co-built" center expanded at WAIC 2025; open OpenLoong/Qinglong humanoid platform |
| New entrants | Consumer-electronics giants entering: Xiaomi (CyberOne lineage), Honor — the smartphone maker's "Lightning" robot ("Flash" in some translations) won the 2026 Beijing half-marathon in 50:26 running autonomously, beating the ratified human world record (57:20) — independently confirmed (Scientific American, CBS, NPR), though the winner fell late in the race after clipping a barricade and was set upright by handlers (2026-04) |

The 2026 Beijing Yizhuang half-marathon's rule change (1.2x time penalty for teleoperated robots) pushed ~38% of entrants to run fully autonomously (per Scientific American) — a useful proxy for China's locomotion-autonomy progress, albeit on a dedicated, pre-mapped course. See [Locomotion](locomotion.md), [Landscape: China](landscape-china.md).

## US & European humanoid makers

- **Figure AI** — best-capitalized pure-play: >$1B Series C at **$39B post-money (2025-09)**, led by Parkway Venture Capital with NVIDIA, Intel Capital, LG, Salesforce, Qualcomm Ventures, Brookfield. In-house **Helix** VLA (2025-02, post-OpenAI split) → Figure 03 designed for mass manufacture + home (2025-10) → **Helix 02** whole-body autonomy — single learned controller for walking + balance + manipulation, flagship 61-action dishwasher load/unload demo (2026-01-27). BotQ factory tooled for 12,000 units/yr; prior BMW Spartanburg deployment ran ~11 months (unverified).
- **Apptronik** (Austin; NASA Valkyrie lineage via UT Austin HCRL) — Apollo humanoid; pilots with Mercedes-Benz and GXO; Google DeepMind model partner; ~$5B valuation (as of 2026) (unverified).
- **Agility Robotics** — Digit is the workhorse of the "boring but real" deployment thesis: tote-moving at GXO under RaaS contracts; RoboFab volume factory.
- **1X Technologies** (Norway/Redwood City; OpenAI-backed) — NEO home humanoid, early-adopter deliveries at **$20,000 (or subscription)**, the first serious consumer-home humanoid program (as of 2026).
- **Boston Dynamics** — see above (Hyundai + TRI LBM).
- **Neura Robotics** (Metzingen, Germany) — Europe's top-funded humanoid maker: Series C **up to $1.4B (announced 2026-06-10)** at ~$7B valuation (valuation per press reports; company declined comment); led by Tether, with Qualcomm, Amazon, NVIDIA, Bosch, Schaeffler, EIB, imec.xpand. Note: the $1.4B is a milestone-contingent ceiling, not cash banked. 4NE-1 humanoid + MAiRA cobots + "Neuraverse" data platform; claims >$1B order book + deployment pipeline and "millions of robots by 2030" (company claims, unverified).
- **Agile Robots** (Munich) — DLR spin-off; Google DeepMind partnership (2026-03).
- **Sanctuary AI** (Vancouver) — Phoenix humanoid, hydraulic dexterous hands; new funding 2026-05.
- Also in the ecosystem: Dyna Robotics, Generalist AI, Dexterity, Collaborative Robotics (Cobot) — smaller/less-documented; see [Landscape: USA](landscape-usa.md).

## Academic labs (talent + open research pipeline)

| Lab | Why it matters |
|---|---|
| Stanford (IRIS, Stanford Robotics Center) | Chelsea Finn (PI co-founder), ALOHA/Mobile-ALOHA lineage; GR00T reference-robot launch partner |
| UC Berkeley (BAIR/RAIL) | Sergey Levine (PI co-founder); deep-RL-for-robotics intellectual home |
| CMU (Robotics Institute) | Pathak & Gupta → Skild; largest US robotics department |
| ETH Zurich (Robotic Systems Lab) | Marco Hutter; ANYmal, legged-robot RL; spin-offs ANYbotics, Flexion; GR00T partner |
| UCSD (ARCLab) | GR00T reference-robot partner; surgical/embodied autonomy |
| Ai2 | Fully open models + data (MolmoAct 2) |
| KAIST / Korean universities | Hubo DRC-2015 lineage; core of K-Humanoid Alliance |
| Tsinghua / Peking Univ. | Feeder labs for Galbot, Unitree, AgiBot talent; embodied-AI benchmarks |

The dominant 2024–2026 pattern: professor-founded startups (Skild, PI, Galbot) pull entire labs into industry — see [Key people](key-people.md).

## National programs

- **China** — whole-of-nation push: embodied intelligence in the five-year plan; national + provincial innovation centers (Beijing X-Humanoid, Shanghai center); state-orchestrated IPO channel opening (Unitree first approval 2026-06); municipal subsidy stacks. See [Landscape: China](landscape-china.md).
- **South Korea** — **K-Humanoid Alliance** (launched 2025-04): ~$770M (₩1T) state investment to 2030, shared "robot brain," target 1,000 humanoids/yr production by 2029 and global top-tier humanoids by 2030; Samsung/Rainbow, LG, Doosan, Hyundai participating (as of 2026).
- **Japan** — robotics incumbents (Fanuc, Yaskawa, Kawasaki, Honda/Toyota labs) + state-backed long-term VC vehicle (~¥1.4T target, 2025-03) (unverified); strength in components and industrial arms rather than humanoid startups.
- **EU/Germany** — High-Tech Strategy 2025 (~€350M robotics-relevant R&D to 2026); EIB directly invested in Neura's 2026 round; Horizon Europe robotics calls.
- **USA** — no dedicated national humanoid program; leadership rests on private capital (robotics companies raised **$55.8B globally in 2026 YTD** per Dealroom, heavily US/China) plus DARPA/NSF/NASA project funding. See [Investment](investment.md).

## Reading the field

- **Brains vs. bodies**: billion-dollar checks now go to software-only labs (PI, Skild) on the thesis that the model layer captures the value; hardware margins compress toward Chinese price points (Unitree G1 ~$16K, R1 ~$6K).
- **NVIDIA sits under everyone**: compute (Thor), sim (Isaac/Cosmos/Newton), open models (GR00T N), and equity stakes in most major players — cooperative monopoly dynamics.
- **China wins volume, US wins valuation** (as of 2026-07): ~50,000 global humanoid shipments forecast for 2026 (TrendForce, ~8x YoY), dominated by Unitree/AgiBot; the five most valuable private players are majority-US.
- **Verification gap**: many flagship claims (BMW hours, order backlogs, revenue ramps) are company-sourced and marked unverified above; treat scale signals as directional. See [Open problems](open-problems.md).

## Sources
- https://nvidianews.nvidia.com/news/nvidia-open-humanoid-robot-reference-design — NVIDIA Isaac GR00T reference humanoid specs, date, partners, late-2026 availability
- https://www.figure.ai/news/series-c — Figure >$1B Series C at $39B post-money, investor list (2025-09)
- https://en.wikipedia.org/wiki/Figure_AI — Figure timeline: Helix, Figure 03, Helix 02 (2026-01)
- https://www.figure.ai/news/helix-02 — Helix 02 announcement (2026-01-27), whole-body controller + dishwasher demo
- https://deepmind.google/blog/gemini-robotics-15-brings-ai-agents-into-the-physical-world/ — Gemini Robotics 1.5 / ER 1.5 capabilities and availability
- https://deepmind.google/models/gemini-robotics/ — Gemini Robotics family; Apptronik partnership
- https://www.cnbc.com/2026/03/24/google-agile-robots-ai-robotics.html — Google–Agile Robots partnership (2026-03)
- https://www.pi.website/blog/pi0 — π0 first generalist policy
- https://www.pi.website/download/pistar06.pdf — π*0.6 + RECAP (2025-11), throughput/failure numbers
- https://github.com/Physical-Intelligence/openpi — PI open-source release
- https://www.humanoidsdaily.com/news/physical-intelligence-unveils-0-7-the-rise-of-compositional-generalization-in-robotics — π0.7 5B-param steerable generalist (2026-04)
- https://www.humanoidsdaily.com/news/don-t-forget-the-salt-physical-intelligence-equips-robots-with-15-minute-multi-scale-memory — Multi-Scale Embodied Memory, ~15-min task horizon (2026-03)
- https://www.therobotreport.com/physical-intelligence-raises-600m-advance-robot-foundation-models/ — PI $600M at $5.6B (2025-11), founders
- https://www.therobotreport.com/skild-ai-raises-1-4b-building-omni-bodied-robot-skild-brain/ — Skild $1.4B Series C, $14B valuation, investors, revenue (2026-01)
- https://www.skild.ai/blogs/series-c — Skild Series C primary announcement (2026-01-14); full investor list (no Samsung)
- https://news.crunchbase.com/venture/robotics-startup-skild-ai-triples-valuation/ — Skild valuation tripling in 7 months
- https://bostondynamics.com/blog/large-behavior-models-atlas-find-new-footing/ — BD/TRI LBM Atlas, 450M-param diffusion policy (2025-08)
- https://pressroom.toyota.com/ai-powered-robot-by-boston-dynamics-and-toyota-research-institute-takes-a-key-step-towards-general-purpose-humanoids/ — BD–TRI partnership framing
- https://www.techtimes.com/articles/317632/20260602/unitree-ipo-cleared-agibot-hits-10000-units-china-humanoid-robot-duopoly-takes-shape.htm — Unitree IPO clearance (2026-06-01), AgiBot 10,000 units
- https://kraneshares.com/a-complete-guide-to-unitree-robotics-2026-ipo-why-it-matters-for-star-market-etf-kstr-humanoid-robotics-etf-koid/ — Unitree IPO valuation/raise figures
- https://www.caixinglobal.com/2026-07-03/unitree-robotics-wins-approval-for-618-million-star-market-ipo-102460136.html — CSRC approved Unitree IPO registration (2026-07-03); ¥4.2B/$618M raise, ~¥40B ($5.9B) valuation
- https://www.trendforce.com/presscenter/news/20260409-13007.html — China 2026 humanoid output +94%, Unitree+AgiBot ~80% share
- https://techcrunch.com/2026/02/28/why-chinas-humanoid-robot-industry-is-winning-the-early-market/ — China early-market dynamics; Galbot/UBTech shipment context
- https://en.people.cn/n3/2026/0420/c90000-20448083.html — 2026 Beijing half-marathon results, autonomy rules (state media)
- https://www.scientificamerican.com/article/a-humanoid-robot-beat-the-human-half-marathon-record-at-a-beijing-race-but-what-did-it-actually-prove/ — independent confirmation of Honor "Lightning" 50:26 result; 38% autonomy rate; fall/handler-assist and pre-mapped-course caveats
- https://electrek.co/2026/04/22/tesla-optimus-production-fremont-model-sx-line/ — Optimus V3 Fremont production timing, Musk caveats
- https://neura-robotics.com/record-series-c/ — Neura Series C up to $1.4B (2026-06), company claims
- https://www.cnbc.com/2026/06/10/neura-robotics-funding-ai-humanoid-robots.html — Neura backers, ~$7B valuation, Dealroom $55.8B 2026 YTD robotics funding
- https://allenai.org/blog/molmoact2 — MolmoAct 2 open model + 720h data, π0.5 benchmark claims (2026-05)
- https://www.korea.net/NewsFocus/Sci-Tech/view?articleId=269677 — K-Humanoid Alliance launch and goals
- https://www.goldmansachs.com/insights/articles/south-koreas-growing-role-in-humanoid-robot-development — Korea investment figures, 2029 production target
- https://ifr.org/news/robotics-research-goverment-programs-asia-europe-and-america-2025/ — government robotics R&D programs (Germany, Japan, China)
