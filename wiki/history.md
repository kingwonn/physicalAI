---
title: History of Physical AI
slug: history
updated: 2026-07-03
confidence: verified
---
> Physical AI — AI that perceives, reasons, and acts in the physical world through robots — evolved through four broad eras: (1) a classical era (1950s–2011) of hand-engineered industrial arms and symbolic-planning research robots like Unimate and Shakey; (2) a deep-learning/deep-RL era (2012–2021) in which learned policies, sim-to-real transfer, and legged-robot breakthroughs replaced hand-coded control but stayed narrow and data-starved; (3) a foundation-model turn (2022–2023) when Google's RT-1/RT-2 and the Open X-Embodiment project imported the "scale + transformers + web knowledge" recipe from LLMs into robotics; and (4) the current robot-foundation-model and humanoid wave (2024–2026), marked by generalist vision-language-action (VLA) models (π0, Helix, Gemini Robotics, GR00T), record capital (Figure at $39B, Physical Intelligence at $5.6B, ~$26.5B into robotics startups in 2025 per Dealroom), Chinese mass production of humanoids, and NVIDIA's CES 2026 declaration that the "ChatGPT moment for physical AI" has arrived.

## Timeline of inflection points

| Year | Milestone | Why it was an inflection |
|---|---|---|
| 1954/1961 | Devol patents a programmable arm (1954); first **Unimate** installed at GM (1961) | Birth of industrial robotics; robots become an industry |
| 1966–72 | **Shakey** (SRI International) | First mobile robot to reason about its actions; birthplace of A*, STRIPS, sense-plan-act |
| 1986 | Brooks' **subsumption architecture**; Honda starts humanoid R&D | Embodiment-first counter-paradigm to symbolic AI; road to ASIMO |
| 2000 | Honda **ASIMO** | Humanoids as engineered flagship demos, not products |
| 2002 | iRobot **Roomba** | First mass-market consumer robot (tens of millions sold) |
| 2004–07 | **DARPA Grand/Urban Challenges** (2005: Stanley; 2007: Boss) | Seeded the autonomous-vehicle industry and its talent tree |
| 2005 | Boston Dynamics **BigDog** | Dynamic legged locomotion enters public consciousness |
| 2012 | AlexNet; Amazon buys **Kiva** (~$775M); Rethink **Baxter** | Learned perception arrives; warehouse robotics proven commercial |
| 2013–15 | DQN (2013/2015); **DARPA Robotics Challenge** Finals (Jun 2015, KAIST wins) | Deep-RL era opens; humanoid reality check (the falling-Atlas reel) |
| 2016 | **AlphaGo**; Levine et al. end-to-end grasping; Google "arm farm" | Deep RL at superhuman level; robot learning framed as a data problem |
| 2017–18 | Domain randomization; PPO; OpenAI **Dactyl** (Jul 2018) | Sim-to-real becomes the standard recipe |
| 2019–20 | ANYmal RL controllers (Science Robotics 2019); Dactyl Rubik's Cube (Oct 2019); Spot ships; Waymo driverless service | Learning beats classical control in locomotion; physical AI reaches paying customers |
| 2021 | OpenAI disbands robotics team (Jul); Tesla announces **Optimus** (Aug) | Per-task RL declared data-starved; the humanoid bet is placed |
| 2022 | **SayCan** (Apr); ChatGPT (Nov); **RT-1** (Dec) | LLM planning + transformer control; robotics adopts the scaling recipe |
| Jul 2023 | **RT-2**, first named VLA | Web knowledge → robot actions; unseen-task success ~62% vs RT-1's ~32% |
| Oct 2023 | **Open X-Embodiment / RT-X** (21 institutions, 1M+ episodes, 22 embodiments) | Cross-embodiment data pooling works; the field's shared-dataset moment |
| 2024 | Mobile ALOHA (Jan); electric Atlas (Apr); OpenVLA (Jun); **π0** (Oct); Unitree G1 at ~$16k (May); Project GR00T (Mar) | Robot foundation models become a startup category; humanoid hardware price floor collapses |
| 2025 | Huang popularizes "Physical AI" + Cosmos (CES, Jan); **Helix** (Feb); **Gemini Robotics** and **GR00T N1** (Mar); π0.5 (Apr); Figure Series C at $39B (Sep); record ~$26.5B into robotics startups (Dealroom) | Every major lab ships a VLA; record funding; factory pilots begin |
| 2026 | CES: ChatGPT moment for physical AI "is here"; Unitree STAR-market IPO; Hyundai commits 25,000+ Atlas units; China output +94% YoY (TrendForce proj.) | Commercial-deployment year; China dominates shipments |

## Era 1 — Classical robotics and symbolic embodied AI (1950s–2011)

- **1954/1961 — Unimate, the first industrial robot.** George Devol filed his "programmed article transfer" patent in December 1954 (granted 1961); with Joseph Engelberger he founded Unimation, and in 1961 the ~4,000 lb Unimate arm began unloading hot die-castings on a General Motors line in Ewing Township, NJ — spawning the industrial-robot industry whose installed base still dwarfs humanoids.
- **1966–1972 — Shakey (SRI).** The first mobile robot to reason about its own actions: TV camera + rangefinder + wheeled base, driven by remote computers running STRIPS planning and A\* search (both invented for the project). Shakey established the sense-plan-act paradigm — and demonstrated its brittleness outside controlled environments.
- **1969–1978 — Stanford Arm → PUMA**: Victor Scheinman's electric, computer-controlled arm lineage became the template for decades of industrial manipulators.
- **1973 — WABOT-1 (Waseda University)**, generally credited as the first full-scale anthropomorphic robot — the deep root of today's humanoid programs.
- **1986 — Rodney Brooks' subsumption architecture** rejected central world models in favor of layered reactive behaviors ("the world is its own best model"). Brooks co-founded iRobot (1990), whose **Roomba** (2002) put robots in millions of homes. Honda's secret bipedal program began the same year, culminating in **P2 (1996)** and **ASIMO (2000)** — marvels of engineered, not learned, control. See [Key people](key-people.md).
- **2004–2007 — DARPA Grand Challenges** (2004: no finisher; 2005: Stanford's Stanley; 2007 Urban Challenge: CMU's Boss) proved autonomous driving feasible; alumni staffed Google's self-driving project (2009, later Waymo) and most of the AV industry — the first physical-AI domain to attract billions in capital.
- **2005 — Boston Dynamics BigDog** and the hydraulic **Atlas** (2013, for the DARPA Robotics Challenge) set the bar for dynamic locomotion using hand-engineered model-based control, no deep learning.
- **2007–2010 — ROS and the Willow Garage PR2** standardized robot software infrastructure and trained a generation of roboticists.
- **2012 — Amazon acquired Kiva Systems (~$775M)** — the era's clearest signal that mobile warehouse robotics was commercially real; Rethink Robotics' Baxter popularized (but failed to commercialize) collaborative arms.
- Throughout this era, autonomy meant engineered pipelines: perception, state estimation, planning, and control were separate hand-built modules. Learning played almost no role in deployed systems.

## Era 2 — Deep learning and deep RL reach robotics (2012–2021)

- **2012 — AlexNet** made learned perception dominant; robotics inherited deep vision almost immediately.
- **June 2015 — DARPA Robotics Challenge Finals**: KAIST's DRC-HUBO won the $2M prize; the falling-robots blooper reel became the canonical image of how far humanoids then were from usefulness — a useful baseline for judging the 2024–2026 wave.
- **2015–2016 — DQN (Nature), TRPO, AlphaGo**; Levine et al. demonstrated end-to-end visuomotor policies, and Google's "arm farm" collected grasping data in parallel — an early bet that robot learning was fundamentally a data problem.
- **2017 — domain randomization** (Tobin et al.) and PPO made **sim-to-real** the era's central methodology: train in randomized [simulation](simulation.md), deploy zero-shot on hardware.
- **July 2018 — OpenAI Dactyl**: a 24-DoF Shadow Hand learned in-hand cube reorientation entirely in simulation (PPO + dynamics randomization), transferring to the physical hand with emergent human-like finger gaiting; in **October 2019** the same line solved a Rubik's Cube one-handed using automatic domain randomization (~10,000 years of simulated experience).
- **2019–2020 — learned legged locomotion matured**: Hwangbo et al. (Science Robotics, 2019) trained ANYmal controllers in simulation that outperformed model-based control; Lee et al. (2020) achieved blind rough-terrain quadruped locomotion. RL became the default for [locomotion](locomotion.md) — the first subfield where learning decisively beat classical control. Boston Dynamics' Spot went on general commercial sale (2020); Waymo opened fully driverless robotaxi service in Phoenix (2020).
- **2021 — the era's ceiling became visible.** OpenAI disbanded its robotics team (July 2021), citing insufficient real-world data — a widely cited marker that per-task RL did not scale to general [manipulation](manipulation.md). That August, Tesla announced the Optimus humanoid program at AI Day.
- Net result of Era 2: superhuman-looking demos in narrow regimes (locomotion, in-hand dexterity), but every task needed its own reward function, training run, and engineering. Generalization was the missing ingredient.

## Era 3 — The foundation-model turn (2022–2023)

- **April 2022 — SayCan (Google)** used an LLM to plan robot task sequences — the first major "LLM as robot brain" result. **May 2022 — DeepMind Gato** showed one transformer spanning Atari, captioning, and real robot stacking.
- **November 2022 — ChatGPT.** The spillover into robotics was direct: it validated the scaling recipe, redirected talent and capital toward "GPT for robots," and set the framing ("robot foundation model," "ChatGPT moment for robotics") used by every major lab since.
- **December 2022 — RT-1 (Google)**: a robotics transformer trained on ~130,000 real episodes across 700+ tasks; widely regarded as the first VLA-style generalist control model.
- **July 2023 — RT-2 (Google DeepMind)**: the first named vision-language-**action** model, co-fine-tuning a web-pretrained VLM (PaLI-X / PaLM-E) to emit robot actions as tokens. Across 6,000+ trials, success on unseen tasks roughly doubled vs RT-1 (~62% vs ~32%) — the founding result of the [VLA model](vla-models.md) paradigm. (PaLM-E, the 562B embodied multimodal LM, preceded it in March 2023.)
- **October 2023 — Open X-Embodiment / RT-X** (arXiv 2310.08864; ICRA 2024): 21 institutions pooled 1M+ trajectories from 22 robot embodiments and 527 skills; RT-1-X improved success ~50% on partner robots and RT-2-X roughly tripled performance on emergent skills — proof that **cross-embodiment data pooling works**, and the template for later open [data](data.md) efforts.
- **2023 — the imitation-learning renaissance**: Stanford's ALOHA/ACT made bimanual teleoperated data collection cheap (Mobile ALOHA, Jan 2024, ~$32k), and diffusion policies became the dominant action-generation architecture for dexterous manipulation.

## Era 4 — Robot foundation models and the humanoid wave (2024–2026)

### 2024: founding year of the "OpenAI-of-robotics" race
- **Figure AI**: $675M Series B at $2.6B valuation (Feb 2024) with an OpenAI collaboration; BMW Spartanburg deal announced Jan 2024. (The OpenAI partnership ended Feb 2025 when Figure went all-in on in-house models.)
- **NVIDIA** announced **Project GR00T** and Jetson Thor at GTC (Mar 2024), positioning itself as the picks-and-shovels vendor of physical AI ([hardware](hardware.md)).
- **Physical Intelligence** founded by Hausman, Levine, Finn et al. (~$70M initial funding); released **π0** on 2024-10-31 — a 3B-parameter VLM backbone plus flow-matching action head emitting continuous control at up to 50 Hz across 8 robot platforms, trained on the largest robot-interaction dataset to date; folded laundry and bussed tables end-to-end. Raised $400M Series A at $2.4B (Nov 2024; Bezos, OpenAI, Thrive).
- **OpenVLA** (Jun 2024) gave academia an open 7B VLA baseline. **Unitree G1** launched at ~$16k (May 2024, as of announcement), collapsing the humanoid hardware price floor. Boston Dynamics retired hydraulic Atlas for an all-electric redesign (Apr 2024).
- Tesla's Optimus "We, Robot" demo (Oct 2024) drew scrutiny for undisclosed teleoperation — emblematic of the era's demo-vs-autonomy credibility gap.

### 2025: every major lab ships a robot foundation model
- **Jan 2025 — CES**: Jensen Huang popularized "**Physical AI**" as the umbrella term, launched **Cosmos** world foundation models (trained on ~20M hours of video; see [World models](world-models.md)), and declared robotics' ChatGPT moment "just around the corner."
- **2025-02-20 — Figure Helix**: first VLA controlling a full humanoid upper body (wrists, torso, head, individual fingers) at high rate; first to run a single set of weights across two cooperating robots; runs entirely on onboard low-power GPUs.
- **Feb 2025 — π0 open-sourced** (weights + code). **April 2025 — π0.5** demonstrated mobile manipulation generalizing to cleaning tasks in homes never seen in training.
- **2025-03-12 — Gemini Robotics + Gemini Robotics-ER** (Google DeepMind): VLA built on Gemini 2.0 with action output; ER variant for embodied spatial reasoning; partners incl. Apptronik, Agility, Boston Dynamics. **Jun 2025 — Gemini Robotics On-Device** (first DeepMind VLA available for fine-tuning; runs locally on bi-arm robots); **Sep 2025 — Gemini Robotics 1.5** added agentic multi-step reasoning.
- **2025-03-18 — NVIDIA Isaac GR00T N1**: first open, customizable humanoid foundation model with a dual-system architecture (System 2 VLM planner + System 1 diffusion action module), announced alongside the open-source **Newton** physics engine (NVIDIA + Google DeepMind + Disney Research). NVIDIA claimed 780k synthetic trajectories (≈9 months of human demos) generated in 11 hours, +40% over real-data-only (vendor claim).
- **Money and scale-up (as of 2025-12)**: Figure Series C >$1B at **$39B** post-money (2025-09-16; led by Parkway Venture Capital, with NVIDIA, Intel Capital, Brookfield — a 15x valuation jump in 19 months); Physical Intelligence $600M Series B at **$5.6B** (Nov 2025, led by CapitalG); 1X opened consumer NEO pre-orders at $20k or $499/month (Oct 2025); Unitree hit unicorn status (~$1.3B, Jun 2025) and shipped ~5,500 humanoids in 2025; AgiBot shipped ~5,100 (TrendForce). China accounted for ~85–90% of global humanoid unit shipments in 2025 (~18,000 units per Xinhua; global tracker estimates range ~13k–20k across Omdia/IDC/HRAA). Robotics startups raised a record **$26.5B in 2025** (Dealroom figure via CNBC — single source for the exact number; trackers diverge by methodology: PitchBook ~$27.6B, Crunchbase ~$14B venture-only).

### 2026 (H1): "ChatGPT moment" declared; deployment and mass production
- **Jan 2026 — CES**: NVIDIA declared "the ChatGPT moment for physical AI is here" (Huang's keynote hedged to "nearly here" per Fortune); GTC 2026 centered on physical AI (Alpamayo end-to-end AV model, Rubin platform). Huang repeatedly frames humanoid labor automation as a **$40T addressable market** — a promotional figure, not a forecast.
- **Deployment (as of 2026-07)**: Figure 03 robots work BMW Spartanburg lines after an ~11-month pilot that reportedly touched 30,000+ vehicles; ~40 units billed at ~$25/robot-operating-hour (unverified — aggregator-sourced). Hyundai announced plans (May 2026) for 25,000+ Atlas robots in its plants, scaling from ~2028. Tesla reportedly ended Model S/X production and is converting Fremont lines toward Optimus, with Gen 3 mass production slipping to mid/late 2026 (unverified). Counterpoint estimates >50,000 humanoids operating commercially in 2026, up from ~16,000 at end-2025.
- **China industrializes the category** ([landscape-china](landscape-china.md)): AgiBot rolled out its 10,000th general-purpose robot (Mar 2026); Unitree's STAR-market IPO application was accepted (filed Mar 2026, cleared Jun 2026; raising ~¥4.2B at a target ≈$6.2B valuation) — its humanoid revenue exceeded quadruped revenue for the first time in 2025; TrendForce projects China humanoid output +94% YoY in 2026 with Unitree + AgiBot taking ~80% of shipments; 140+ Chinese humanoid makers and 330+ released models; H1 2026 Chinese embodied-AI funding exceeded ¥46B across 288 deals (as of 2026-06); government policy treats embodied intelligence as a strategic priority with deployment quotas ("work mode") for end-2026.
- **Model iteration continues (as of 2026-07)**: Gemini Robotics-ER 1.6 (2026-04-14); NVIDIA GR00T N1.7 early access (2026-04-17), a 3B open VLA on a Cosmos-Reason2 backbone pretrained on ~20,854 hours of egocentric human video, with NVIDIA claiming a first "scaling law for robot dexterity" (unverified — vendor claim); Ant Group's LingBot-VLA (Jan 2026) and a crowded open-model field (SmolVLA, X-VLA, Wall-OSS). Physical Intelligence reportedly in talks to raise ~$1B at ~$11B (first reported 2026-03 by Bloomberg/TechCrunch; not confirmed closed as of 2026-07). Current capabilities: [State of the art](state-of-the-art.md).

## Recurring patterns

- **Moravec's paradox held for 40 years**: abstract reasoning (chess, Go, language) fell to AI long before folding laundry. The 2023–2026 VLA era is the first credible attack on it — yet dexterous [manipulation](manipulation.md) still lags language ability by a wide margin (see [Open problems](open-problems.md)).
- **Data is the recurring bottleneck**: Shakey's world model was hand-coded; deep RL substituted simulation for data; VLAs substitute web-scale pretraining + teleoperation + egocentric human video. Each era's winners found a cheaper data source (see [Data](data.md)).
- **Each era over-promised generality and was corrected by an embodiment reality check**: Shakey's symbolic reasoning, ASIMO's choreography, deep RL's sim champions. Demos have historically led deployment by 5–10 years — though paid deployments (BMW, Hyundai, Chinese factories) are a genuinely new feature of this cycle.
- **Hype cycles are capital cycles**: DARPA money (1960s–70s, 2004–15), corporate labs (2012–21), venture capital at record scale (2023–; see [Investment](investment.md)). Figure's 15x valuation jump in 19 months (as of 2025-09) is historically anomalous for a hardware company.
- **Simulation keeps compounding**: from Dactyl's domain randomization to Isaac/Newton and world models, the sim stack is the most durable legacy of the deep-RL era (see [Simulation](simulation.md), [World models](world-models.md)). Key institutional actors across all four eras: [Organizations](organizations.md).

## Sources
- https://ai.stanford.edu/~nilsson/OnlinePubs-Nils/General%20Essays/Shakey-aimag-17.pdf — Nilsson's primary account of Shakey (1966–72), STRIPS/A*.
- https://en.wikipedia.org/wiki/Unimate — Unimate/Devol/Engelberger dates; 1961 GM installation.
- https://spectrum.ieee.org/unimation-robot — IEEE Spectrum on the first industrial robot arm.
- https://en.wikipedia.org/wiki/DARPA_Grand_Challenge — 2004 no-finisher, 2005/2007 winners.
- https://openai.com/index/learning-dexterity/ — OpenAI Dactyl (Jul 2018), sim-to-real via domain randomization.
- https://openai.com/index/solving-rubiks-cube/ — Dactyl Rubik's Cube (Oct 2019), automatic domain randomization.
- https://journals.sagepub.com/doi/10.1177/02783649241312698 — survey of learning-based legged locomotion (ANYmal RL milestones 2019–20).
- https://deepmind.google/blog/rt-2-new-model-translates-vision-and-language-into-action/ — RT-2 as first VLA; 62% vs 32% unseen-task result.
- https://arxiv.org/abs/2310.08864 — Open X-Embodiment / RT-X: 22 embodiments, 1M+ trajectories, RT-1-X +50%.
- https://deepmind.google/blog/scaling-up-learning-across-many-different-robot-types/ — DeepMind RT-X blog.
- https://arxiv.org/abs/2401.02117 — Mobile ALOHA paper (cost, co-training results).
- https://www.pi.website/blog/pi0 — π0 primary source: 2024-10-31, 3B VLM + flow matching, 8 platforms.
- https://www.therobotreport.com/physical-intelligence-raises-600m-advance-robot-foundation-models/ — PI $600M Series B at $5.6B (Nov 2025).
- https://techcrunch.com/2026/03/27/physical-intelligence-is-reportedly-in-talks-to-raise-1-billion-again/ — PI ~$11B raise talks (Mar 2026, reported).
- https://www.bloomberg.com/news/articles/2026-03-27/ex-deepmind-staffers-robotics-startup-in-talks-for-11-billion-valuation — Bloomberg confirmation of PI $1B/$11B talks (Mar 2026).
- https://www.figure.ai/news/helix — Helix primary source: first full-upper-body, multi-robot VLA (2025-02-20).
- https://www.figure.ai/news/series-c — Figure Series C >$1B at $39B post-money (2025-09-16), investor list.
- https://techcrunch.com/2025/09/16/figure-reaches-39b-valuation-in-latest-funding-round/ — independent confirmation of Figure valuation.
- https://deepmind.google/blog/gemini-robotics-brings-ai-into-the-physical-world/ — Gemini Robotics + ER announcement (2025-03-12).
- https://www.infoq.com/news/2025/07/google-gemini-robotics/ — Gemini Robotics On-Device (Jun 2025).
- https://blog.google/innovation-and-ai/models-and-research/google-deepmind/gemini-robotics-er-1-6/ — Gemini Robotics-ER 1.6 (Apr 2026).
- https://nvidianews.nvidia.com/news/nvidia-isaac-gr00t-n1-open-humanoid-robot-foundation-model-simulation-frameworks — GR00T N1 + Newton engine primary source (2025-03-18).
- https://blogs.nvidia.com/blog/ces-2025-jensen-huang/ — CES 2025: "Physical AI" framing, Cosmos launch.
- https://www.axios.com/2026/01/05/nvidia-ces-2026-jensen-huang-speech-ai — CES 2026 "ChatGPT moment for physical AI is here"; Alpamayo, Rubin.
- https://fortune.com/2026/01/06/nvidia-jensen-huang-chatgpt-moment-for-robotics/ — Fortune on CES 2026 "here" vs "nearly here" hedging.
- https://www.cnbc.com/2026/01/21/nvidia-jensen-huang-robotics-opportunity-europe-.html — record $26.5B robotics funding in 2025 (Dealroom); single source for the exact figure.
- https://news.crunchbase.com/robotics/startup-venture-funding-surges-2026-data/ — Crunchbase: ~$14B robotics venture funding in 2025 (methodology differs from Dealroom/PitchBook).
- https://247wallst.com/investing/2026/05/31/jensen-huang-just-called-humanoid-robots-a-40-trillion-market-heres-why-wall-street-is-loading-up-on-physical-ai-stocks/ — Huang's repeated $40T humanoid-labor TAM framing (May 2026 coverage).
- https://bostondynamics.com/blog/electric-new-era-for-atlas/ — hydraulic Atlas retired; electric Atlas (Apr 2024).
- https://www.foxnews.com/tech/hyundai-send-25000-atlas-robots — Hyundai 25,000+ Atlas deployment plan (May 2026).
- https://www.trendforce.com/presscenter/news/20260409-13007.html — TrendForce: China humanoid output +94% YoY 2026; Unitree/AgiBot ~80% share.
- https://www.techtimes.com/articles/317632/20260602/unitree-ipo-cleared-agibot-hits-10000-units-china-humanoid-robot-duopoly-takes-shape.htm — Unitree STAR IPO cleared; AgiBot 10,000th unit.
- https://www.news.cn/tech/20260108/46b1220e159d4f80bc6a4240eb3b47b5/c.html — Xinhua: China ~18,000 humanoid shipments in 2025.
- https://www.scmp.com/tech/tech-trends/article/3340446/chinas-unitree-ships-more-5500-humanoid-robots-2025-surpassing-us-peers — SCMP: Unitree >5,500 humanoids shipped in 2025 (per its own IPO prospectus); AgiBot ~5,168 per Omdia.
- https://caifuhao.eastmoney.com/news/20260627181443427425560 — H1 2026 China embodied-AI funding >¥46B across 288 deals.
- https://merics.org/en/report/embodied-ai-chinas-ambitious-path-transform-its-robotics-industry — Chinese embodied-AI policy framing.
- https://www.ctco.blog/posts/humanoid-robots-state-of-the-art-2026/ — 2026 deployment details (Figure 03/BMW, Optimus status); single blog source, flagged cautiously.
- https://www.marktechpost.com/2026/04/28/top-10-physical-ai-models-powering-real-world-robots-in-2026/ — 2026 model landscape incl. GR00T N1.7 (single-source details).
