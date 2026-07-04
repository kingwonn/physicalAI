---
title: Data Foundry Economics
slug: data-foundry
updated: 2026-07-04
confidence: verified
---
> Robot training data is now a manufactured commodity with its own supply chains, factories, labor markets, and price curves — a "data foundry" industry sitting under the model labs. As of 2026-07 the segment spans US brokers (Scale AI's Physical AI Data Engine), vertically integrated collectors (Generalist AI's 500,000+ hour wearables corpus), Chinese state-subsidized teleoperation halls (40+ centers; JD.com alone plans 10M hours over two years), in-house fleets at [Physical Intelligence](company-pi.md)/[Figure](company-figure.md)/[Tesla](company-optimus.md), and a first wave of data marketplaces. Unit economics are the story: fully loaded US teleop data reportedly fell from ~$340/hour (early 2024) to ~$118/hour (2026-03), US operators earn $20–50/h against $3–20/h in China, and egocentric human video undercuts teleop by roughly an order of magnitude — which is why every major lab is pivoting toward wearables. This page covers the business; the technical data problem is in [Data](data.md).

## Why a foundry industry exists

- Robot actions have no free internet corpus; every hour of training data has a marginal production cost (operator labor + rig amortization + QA + annotation). See [Data](data.md) for method trade-offs.
- Scaling-law results (ICLR 2025 diversity power laws; GEN-0's pretraining-hours law) converted data from "nice to have" into the primary capital sink — labs now budget data acquisition like compute. See [Investment](investment.md).
- Three business models have emerged: **brokers/service bureaus** (Scale AI, annotation BPOs) selling collection-as-a-service; **vertically integrated labs** (Generalist, AgiBot, Tesla) that own collection and keep the data; and **state-subsidized infrastructure** (China's municipal training centers) that socializes the cost across government, hardware vendors, and cheap labor.
- Structural tension: the labs with the best models increasingly refuse to share or sell data (it's the moat), so the open ecosystem depends on state-backed releases (AgiBot World, RoboMIND) and academic consortia — see the proprietary-vs-open section below.

## Scale AI Physical AI Data Engine

- **Offering** (launched/expanded 2025-09): end-to-end collection + annotation for robotics — 100,000+ production hours logged at a San Francisco robotics prototyping lab plus a global contributor network; covers teleoperation, human-video, and evaluation data (company figures).
- **Named customers** (as of 2025-09): [Physical Intelligence](company-pi.md), Generalist AI, Cobot — i.e., Scale sells picks and shovels to the very labs also building in-house engines.
- **Universal Robots partnership** (announced at GTC 2026-03): "UR AI Trainer" leader-follower imitation-learning kit embeds Scale's engine into UR's ~100k-unit installed industrial-arm base — a play to turn deployed cobots into a distributed collection fleet.
- **Post-Meta status**: Meta paid $14.3B for 49% (2025-06, ~$29B valuation); founder Alexandr Wang left to run Meta Superintelligence Labs; Google, OpenAI and xAI subsequently cut or paused LLM data-labeling work over confidentiality concerns, and Scale laid off ~200 data-labeling staff (2025-07). Physical AI is one of the growth bets under new CEO Jason Droege — the robotics customer list above was announced *after* the Meta deal, suggesting robot labs are less spooked than LLM labs (robot data is customer-specific, not model-secret-revealing). Also launched "Scale Labs" (2026-03), a research division on agentic/multimodal-system reliability. Forbes reported the broader business under margin pressure (2026-05) (single-source).

## Generalist AI: the vertically integrated foundry

- **Founders** (verified): Pete Florence (CEO, ex-Google DeepMind; PaLM-E/RT-2 lineage), Andy Zeng (Chief Scientist, ex-Google Brain), Andy Barry (CTO, ex-Boston Dynamics). Note: Eric Jang is not a Generalist founder — a common conflation; he was VP of AI at 1X Technologies until departing 2026-01 (on sabbatical as of mid-2026).
- **Data engine**: wrist-worn "data hands" wearables that make a human hand act as a pincer-style robot end-effector while recording visual + sensory streams; Generalist has "shipped thousands of robot hands across new geographies" to a network of contracted **data foundry partners** operating in thousands of homes, warehouses and workplaces (company statements; partner identities, geographies, and pay rates undisclosed). This is human-embodied collection, not robot teleoperation — no robot needed at collection time (UMI-style economics).
- **Corpus**: 270,000+ hours (2025-11, GEN-0) → **500,000+ hours** by GEN-1 (2026-04), growing ~10,000 h/week at last disclosure — the largest disclosed physical-interaction corpus anywhere, several times all open datasets combined.
- **GEN-1** (2026-04-02): claims 99% average success on tasks where GEN-0-class models hit 64%, ~3× faster task execution, and ~1 hour of robot-specific data per task after pretraining (vs 19% success training from scratch) — the commercial pitch is that a big enough pretraining corpus collapses per-customer data cost by ~10× (company claims, no third-party evals).
- **Capital**: $400M at ~$2B valuation (2026-06, Radical Ventures-led; NVIDIA, Bezos Expeditions among backers; total raised >$500M) — the round is effectively data-foundry capex. Earlier: ~$140M raised through 2025 at a ~$440M valuation (Forbes).
- Contrast with PI: Forbes reports Physical Intelligence relies on teleoperation with staged environments and even rented Airbnbs for in-home collection, while Generalist bets on cheap wearables — the two poles of the cost-per-hour spectrum.

## Chinese state-backed data factories

China industrialized data collection as policy; [Landscape: China](landscape-china.md) has the policy timeline — this section covers the facilities and economics.

- **AgiBot (Shanghai Lingang)**: self-described largest embodied data collection facility — 4,000 m² per the AgiBot World paper (kr-asia reports 3,000 m²), ~100 robots collecting continuously across five simulated domains (home, retail, service, dining, industrial) with 3,000+ real objects, generating ~30,000–50,000 episodes/day via VR teleoperation (company figures). Source of the open AgiBot World corpus (1M+ trajectories) and the follow-up **AgiBot World 2026** open release; also demoed beyond-line-of-sight teleoperation on G2 for remote collection.
- **X-Humanoid / Beijing Embodied-AI Robotics Innovation Center (Yizhuang)**: "embodied intelligence data and training base" where **120+ different robot models** train across 30+ scenarios in six sectors (household, retail, office, industrial, pharma, healthcare), plus a high-precision mocap venue used to set collection-quality benchmarks; produced RoboMIND/RoboMIND 2.0 (6M+ downloads per Xinhua); raised RMB 700M+ (~$100M) in its first market-oriented funding round (2026-02, Caixin; Baidu among investors) (facility figures: Xinhua, as of 2026-06).
- **Municipal training grounds**: Shanghai Kylin (~5,000 m², 100+ heterogeneous humanoids, opened 2025-01); Beijing Shijingshan (10,000+ m², 16 staged scenarios); 40+ state-owned centers had been announced by 2025-12 with ~two dozen operational (Interact Analysis count, via Rest of World, early 2026). Shenzhen/Guangdong host vendor-run operations embedded in dozens of electronics and packaging factories (workers wearing head cameras + wrist sensors on live assembly lines).
- **JD.com (Suqian)**: plans to generate **10 million hours** of robot training data over two years — a purpose-built "data collection neighborhood" where residents film chores, eventually involving ~100,000 employees plus ~500,000 external workers (Rest of World; company plan, execution unverified). Would dwarf every disclosed Western corpus if delivered.
- **Demand driver**: the MIIT+SASAC **real-scene training special action** (2026-06-09) mandates 100+ deployed application scenarios and "10,000-unit-scale" deployment capacity by end-2026 across 10 provinces and central SOEs — each deployment scenario doubles as a data-collection site, effectively a state purchase order for foundry capacity. UBTech's RMB 159M order for a Zigong data-collection center shows the revenue loop: government buys robots to staff centers that produce data to improve the robots.
- **Labor model**: full-time "data collectors" repeat single actions up to ~600×/day in VR headsets and arm exoskeletons; wages $5–20/hour depending on region (Rest of World). Side-gig egocentric capture pays far less — one documented case: ¥20 (~$3)/hour for filming household chores 6 h/day in Shandong. In-home robot-service sessions run the subsidy the other way: one Beijing customer *paid* ¥149 (~$22) for a 3-hour robot-service visit whose real product was the training data collected in his apartment — data value underwriting a below-market service price.

## In-house data ops at the US labs

| Lab | Model of collection | Disclosed scale | Notes |
|---|---|---|---|
| [Physical Intelligence](company-pi.md) | In-house teleop; staged environments + rented Airbnbs; also a named Scale AI customer | π0-era corpus reported ~10k h (unverified); π0.5 added ~400 h mobile-manipulation demos | Does not sell data or teleop services; collection is a cost center for its own models |
| [Figure](company-figure.md) | In-house multi-operator teleop fleet + Brookfield egocentric human video ("Go-Big") | Helix trained on ~500 h high-quality teleop (2025-02); Go-Big taps 100k+ residential units | Auto-labels teleop clips with a VLM generating hindsight language instructions — annotation cost pushed to GPUs |
| [Tesla Optimus](company-optimus.md) | Salaried "Data Collection Operators" in Palo Alto — $48/h max, mocap suit + VR, 5'7"–5'11" height requirement, 7+ h walking/day; >50 people had held the role by 2024-08 (Business Insider LinkedIn analysis) | Undisclosed | Pivoted 2025-06 to camera-only helmet/backpack rigs (five cameras) capturing everyday tasks — dropped the mocap suits, kept the payroll model |
| Apptronik | "Robot Park" (Austin, 90,000 sq ft, announced 2026-06-30): Apollo fleets doing real logistics/manufacturing/retail work under mixed teleop + autonomy | Undisclosed | Feeds Google DeepMind's Gemini Robotics; satellite sites at Mercedes-Benz and GXO — work-as-data-collection, revenue offsets collection cost |

- The Tesla wage anchor ($48/h, i.e. ~$100k/yr full-time) is the clearest public price for US first-party collection labor — 5–15× Chinese center wages.
- Common pattern: US labs treat collection labor as skilled in-house work (quality control, consistent rigs), then push scale to cheaper channels — human video (Tesla, Figure), customer-site fleet data (Apptronik), or contracted foundry networks (Generalist).

## Teleop-hour unit economics

Best available numbers, mostly from one industry-analytics source (SVRC / roboticscenter.ai) — treat as directional (single-source for most rows):

| Metric | US (as of 2026) | China (as of 2026) |
|---|---|---|
| Operator base wage | $20–35/h mid-cost cities; $30–50/h SF/NY; $20–30/h remote VR from home | $5–20/h at training centers (Rest of World); ~$3/h for gig egocentric capture |
| Fully loaded operator cost | $36–40/h for a $28/h operator (+30–40% benefits/taxes) | not disclosed; centers subsidized by municipal programs + vendor hardware deals |
| Fully loaded cost per delivered teleop-data hour | ~$340/h (early 2024) → ~$136/h (Q4 2025) → **~$118/h** (2026-03, standard pick-and-place with wrist cam + external RGBD) | no published figure; labor share suggests several-fold lower (unverified inference) |
| Cost per demonstrated trajectory | $6–11 simple pick-and-place; $11–23 varied grasps; $20–42 tool use; $31–79 contact-rich assembly; $54–157 bimanual/deformable | not published |
| Throughput per operator | 80–120 demos/day simple; 20–70 moderate; 5–25 complex (≈ the ~35 demos/h teleop ceiling in [Data](data.md)) | up to ~600 repetitions/day of a single action per worker |
| Egocentric human video (all-in) | $10–30/h participant compensation + equipment amortization vs $50–200/h teleop operator time (vendor claim, Claru) | ~$3/h documented gig rate |

- Implications: at ~$118/h, Generalist's 500k-hour corpus would cost ~$59M to replicate with US teleop — but wearable human capture likely cost them a fraction of that, which is the whole thesis. At Chinese center wages, the same corpus costs single-digit millions in labor (back-of-envelope, unverified).
- Cost decline drivers: cheaper rigs (ALOHA-class $20–30k → commodity VR), remote operation removing site costs, VLM auto-annotation (Figure's hindsight labeling), and policy-assisted teleop where a partial policy handles easy sub-segments.
- No vendor publishes a real price sheet for "cost per hour, delivered, quality-guaranteed" — pricing is bespoke/enterprise, which itself signals an immature market.

## Egocentric human video: the cheap substitute

- The economic argument, not just the scientific one, drives the wearables pivot: humans need no robot, no rig, no dedicated site — collection cost approaches the local wage floor. Cross-reference the scaling evidence (NVIDIA EgoScale log-linear dexterity law) in [Data](data.md).
- **Meta Aria Gen 2**: broad rollout to qualified researchers targeted Q2 2026; nearly 300 academic labs in 27 countries have used 1,000+ Aria Gen 1 devices; NVIDIA partnership pairs Aria Gen 2 with FoundationStereo for wearable depth sensing. EgoMimic's headline economics: 90 minutes of Aria recordings yielded up to 400% task-performance improvement when co-trained (Meta/Georgia Tech claim).
- Meta also bought robotics-AI startup ARI (Assured Robot Intelligence; team joined Meta Superintelligence Labs, 2026-05) as part of a physical-AI push — positioning Aria-style egocentric capture as strategic infrastructure, not just a research program.
- Startup layer (all as of 2026, mostly YC-adjacent, all company-reported): **Claru** (YC W26; 10,000+ camera-wearing contributors across 100+ cities, delivers depth/pose/segmentation/action labels precomputed), **Cortex AI** (marketplace where workplaces get paid to host collection/eval sessions; egocentric + robot trajectories from real industry settings), **Sensei** (founded 2024; claims human-demonstration capture at ~1/10 the cost and 2× the speed of teleop; "Scale AI for robotics data" positioning), plus BPO-style vendors (Objectways, Unidata, Macgence, Labellerr) doing collection/annotation offshore.
- China runs the same playbook with gig labor: JD's Suqian neighborhood, factory head-camera programs, and ~$3/h chore-filming — egocentric capture is where the US-China cost gap is widest in absolute terms but narrowest in moat terms (anyone can buy cameras).
- Unresolved: egocentric video carries no force/haptic signal and no robot action labels — if contact-rich tasks resist video-only learning, the cost advantage evaporates for exactly the tasks worth automating. See [Open problems](open-problems.md) and [World models](world-models.md) for the neural-data alternative.

## Marketplaces and licensing

- A thin but real market for *selling* robot data emerged in 2025–2026 (all figures company-reported, unverified):
  - **SVRC / Robotics Center marketplace**: 20,000+ hours cataloged, 11M+ episodes indexed from collectors in 30+ countries; sellers pick commercial / research-only / exclusive licenses and price per episode or per dataset — the first visible attempt at standardized robot-data licensing terms.
  - **Cortex Marketplace**: two-sided — venues (warehouses, kitchens) get paid to host collection; labs buy in-the-wild data.
  - **Scale AI** sells collection-as-a-service (not a marketplace — buyers own their data).
  - Hugging Face **LeRobot** format is becoming the de-facto interchange standard, which any real marketplace needs.
- What is *not* for sale: the frontier corpora. Generalist, PI, Figure, Tesla, and AgiBot's proprietary layers are strictly internal; AgiBot open-sources curated slices (AgiBot World 2026) while keeping the live firehose. Simulation data is effectively free to replicate and so resists monetization — see [Simulation](simulation.md).
- Licensing open questions (as of 2026-07): no settled norms on consent/privacy for egocentric video captured in homes and workplaces (Brookfield tenants, Chinese factory workers), no standard quality warranties, and no case law on whether demonstrated trajectories embed the demonstrator's IP. Expect this to look like the 2023–2024 LLM text-licensing scramble, a few years behind.

## Proprietary vs open gap

- Trajectory (disclosed corpus sizes, hours, as of 2026-07): Generalist 500k+ (proprietary) vs AgiBot World ~3k open + larger internal, RoboMIND 2.0 ~1k, DROID 350, AIRoA ~10k — the largest proprietary corpus is now ~50× the largest open real-robot release and growing ~10k h/week. The gap widened through 2025–2026 despite bigger open releases.
- China is the main counterweight: state-backed centers treat open releases (AgiBot World 2026, RoboMIND, Kylin outputs) as ecosystem subsidies, mirroring the open-weight strategy of Chinese LLM labs — see [Landscape: China](landscape-china.md).
- Egocentric datasets may reopen the field: human-video capture is cheap enough that academic consortia (Aria partners) and startups can plausibly match lab scale, unlike robot-fleet data.
- Strategic read: if scaling laws hold, data compounds like capex — the 2026 funding rounds (Generalist $400M, Apptronik Robot Park, JD's 10M-hour plan) are bets that today's hour gap becomes tomorrow's capability gap. See [Investment](investment.md) and [State of the art](state-of-the-art.md).

## Quality vs quantity: audits and curation

- **Traceplane audit** (2026, automated checks on 10 popular open datasets): Open X-Embodiment sub-dataset `utokyo_saytap` contains only black frames; 28 of 55 listed OXE sub-datasets are unavailable for download; a misspelled dataset name ("manpulation") breaks programmatic access; `berkeley_rpt` documents 3 camera views but ships 1 (single-source audit, but findings are mechanically checkable).
- Curation research is professionalizing: **Re-Mix** (optimizing dataset mixture weights for imitation learning), influence-function demonstration curation ("Quality over Quantity," 2026), and audits showing action-only quality scorers miss the structural defects that actually degrade policies (2026). Consistent finding: curated homogeneous data beats larger heterogeneous piles (AgiBot World's ~30% edge over OXE pretraining — see [Data](data.md)).
- Foundry implication: QA is becoming the margin. Vendors advertise "training-ready" labels and quality benchmarks (X-Humanoid's mocap-calibrated collection standards; Scale's evaluation offerings); buyers are learning that a cheap hour of bad data has negative value. No third-party certification or standard quality metric exists yet (as of 2026-07) — a gap MIIT's standards program may fill first in China.

## Open questions

- Does the market consolidate to brokers (Scale model) or verticals (Generalist model)? LLM history suggests labs internalize data once it becomes the moat — bad news for pure-play foundries.
- What happens to Chinese center economics when subsidies taper? The MIIT special action runs through end-2026; sustained demand depends on deployments generating real revenue.
- Can anyone build a liquid data marketplace before the frontier labs stop needing external data (fleet learning from deployed robots closes the loop)?
- Where does the price floor land? Teleop $/h fell ~65% in two years; egocentric capture is already near wage floors; the marginal cost of *simulation* and world-model "neural data" is GPU-time — see [World models](world-models.md).

## Sources
- https://scale.com/physical-ai — Scale Physical AI Data Engine offering: 100k+ production hours, SF robotics lab, collection + annotation stack.
- https://www.universal-robots.com/news-and-media/news-center/universal-robots-scale-ai-launch-imitation-learning-system-accelerate-ai-training-lab-to-factory/ — UR AI Trainer partnership (announced GTC 2026-03), UR installed base as collection fleet.
- https://techcrunch.com/2025/08/29/cracks-are-forming-in-metas-partnership-with-scale-ai/ — post-Meta customer losses (Google/OpenAI/xAI), ~200 labeling layoffs (2025-07), Meta researchers preferring Surge/Mercor.
- https://www.forbes.com/sites/richardnieva/2026/05/14/scale-meta-deal/ — Scale's business under pressure post-Meta deal (2026-05).
- https://scale.com/blog/scale-ai-announces-next-phase-of-company-evolution — Alexandr Wang departure to Meta; Jason Droege as CEO.
- https://generalistai.com/blog/apr-02-2026-GEN-1 — GEN-1 (2026-04-02): 500k+ h pretraining corpus, wearable-device human data, 99% vs 64% success, ~1 h robot data per task, 3× speed.
- https://www.forbes.com/sites/annatong/2026/04/02/generalist-is-betting-its-robot-training-gloves-will-usher-in-robotics-chatgpt-moment/ — Generalist "data hands" wrist wearables, thousands shipped across geographies, founders (Florence/Zeng/Barry), PI teleop/Airbnb contrast, prior $140M raised at $440M valuation.
- https://www.bloomberg.com/news/articles/2026-06-04/nvidia-backed-robotics-startup-generalist-ai-valued-at-2-billion — Generalist $400M at ~$2B (2026-06), Radical Ventures-led, total >$500M.
- https://generalistai.com/blog/nov-04-2025-GEN-0 — GEN-0: 270k+ h, +10k h/week, "data foundry partners" network.
- https://restofworld.org/2026/china-ai-robotics-training-data/ — Chinese collection economics: ¥20 (~$3)/h chore filming, ¥149/3-h home sessions, JD.com 10M-hour Suqian plan (100k employees + 500k external), Guangdong factory head-camera programs.
- https://restofworld.org/2026/china-robots-training-centers-workers/ — 40+ announced state centers, ~two dozen operational, $5–20/h wages, ~600 repetitions/day, Hubei center with ~100 teleoperated humanoids.
- https://english.news.cn/20260613/5d8906d63b2a4586a04fe160bd5d7a65/c.html — Xinhua (2026-06): X-Humanoid Yizhuang data/training base — 120+ robot models, 30+ scenarios, 6 sectors, mocap-calibrated collection standards, RoboMIND 6M+ downloads.
- https://www.caixinglobal.com/2026-02-04/beijing-humanoid-robotics-hub-raises-100-million-in-first-funding-round-102411145.html — X-Humanoid RMB 700M+ (~$100M) first funding round (2026-02), state-linked investors + Baidu.
- https://kr-asia.com/inside-agibots-shanghai-center-robots-learn-to-master-tasks-in-human-like-ways — AgiBot Lingang facility: ~100 robots, 30k–50k data points/day, five scenario domains (reports 3,000 m²).
- https://arxiv.org/html/2503.06669v4 — AgiBot World paper: 4,000 m² facility, 100 robots, 3,000+ distinct objects (primary for facility figures).
- https://www.therobotreport.com/agibot-world-2026-dataset-open-source-accelerate-embodied-ai-development/ — AgiBot World 2026 open-source dataset release.
- https://www.ncsti.gov.cn/kjdt/tzgg/202606/t20260609_249248.html — MIIT+SASAC real-scene training special action (2026-06-09): scenario quotas creating state demand for training grounds (primary).
- https://www.roboticscenter.ai/research/robot-data-collection-cost-breakdown — US unit economics: $20–50/h operator wages, $36–40/h loaded, $6–157 per demo by task complexity, 5–120 demos/day throughput (single industry source).
- https://www.roboticscenter.ai/state-of-robotics-2026 — teleop data cost decline $340/h (early 2024) → $136/h (Q4 2025) → ~$118/h (2026-03) (single industry source; SVRC "State of Robotics 2026" report).
- https://www.roboticscenter.ai/marketplace — SVRC data marketplace: 20k+ hours cataloged, 11M+ episodes indexed, 30+ countries, per-episode licensing tiers.
- https://fortune.com/2024/08/19/tesla-robot-hiring-workers-optimus-training-ai/ — Tesla Data Collection Operators: $25.25–$48/h, mocap suit + VR, height 5'7"–5'11", 7+ h walking/day.
- https://www.heise.de/en/news/Tesla-hires-over-50-people-for-Optimus-training-in-motion-capture-suits-9841052.html — >50 people through the DCO role by 2024-08 (Business Insider LinkedIn review); Palo Alto location.
- https://www.eweek.com/news/tesla-optimus-robot-training/ — Tesla 2025 pivot to five-camera helmet/backpack human-video rigs.
- https://www.figure.ai/news/helix — Helix: ~500 h multi-robot multi-operator teleop corpus; VLM hindsight auto-labeling pipeline.
- https://www.forbes.com/sites/johnkoetsier/2026/06/30/apptronik-announces-robot-park-a-90000-square-foot-humanoid-data-factory-teases-new-robot/ — Apptronik Robot Park: 90,000 sq ft Austin data factory; Mercedes/GXO satellite sites; DeepMind models.
- https://www.meta.com/blog/aria-gen-2-updates/ — Aria Gen 2 applications open, broad rollout Q2 2026, 200+ partners, NVIDIA FoundationStereo pairing.
- https://ai.meta.com/blog/egomimic-project-aria-georgia-tech-ego4d-robotics-embodied-ai/ — EgoMimic: 90 min Aria data → up to 400% task-performance gain (co-training claim).
- https://www.eweek.com/news/meta-acquires-ari-humanoid-robotics-ai/ — Meta acquisition of robotics-AI startup ARI (2026-05).
- https://techcrunch.com/2026/05/01/meta-buys-robotics-startup-to-bolster-its-humanoid-ai-ambitions/ — independent confirmation of the ARI (Assured Robot Intelligence) acquisition; team into Meta Superintelligence Labs.
- https://evjang.com/2026/01/21/leaving-1x.html — Eric Jang's own announcement of leaving 1X (2026-01), supporting the founder-conflation note.
- https://claru.ai/guides/how-to-collect-egocentric-video-data — egocentric-vs-teleop cost comparison ($10–30/h vs $50–200/h of operator time) (vendor source).
- https://claru.ai/blog/best-egocentric-data-providers — Claru contributor network (10,000+ contributors, 100+ cities) and precomputed enrichment layers; provider landscape (vendor source).
- https://www.ycombinator.com/companies/cortex-ai — Cortex AI marketplace: paid host venues, egocentric + robot-trajectory data from industry settings.
- https://www.ycombinator.com/companies/sensei — Sensei: human-demo capture claimed at ~1/10 teleop cost, 2× speed; operator-network model.
- https://traceplane.ai/blog/we-audited-10-robotics-datasets — audit of 10 open datasets: OXE black-frame subset, 28/55 sub-datasets unavailable, metadata defects.
- https://arxiv.org/pdf/2408.14037 — Re-Mix: optimizing data-mixture weights for large-scale imitation learning.
- https://arxiv.org/pdf/2603.09056 — influence-function demonstration curation ("Quality over Quantity", 2026).
- https://www.pi.website/blog/pi05 — π0.5 data mixture (~400 h mobile-manipulation demos) as PI in-house collection anchor.
