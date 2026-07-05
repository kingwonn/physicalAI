---
title: "Visions & Theses: How the Leaders Frame Physical AI"
slug: visions
updated: 2026-07-05
confidence: verified
---
> The dozen most influential voices in Physical AI agree on remarkably little beyond "this is enormous." Jensen Huang sells a $40–50T labor-automation TAM and his CES 2026 keynote declared the "ChatGPT moment for physical AI" nearly here; Elon Musk claims "~80% of Tesla's value will be Optimus" (X, 2025-09) against the industry's worst delivery record; Demis Hassabis frames embodied intelligence as a core pillar of AGI with robotics breakthroughs "over the next 18 months or so" (2026-02); Fei-Fei Li and Yann LeCun both argue LLMs are the wrong substrate and world models the right one — Li via "spatial intelligence," LeCun via anti-generative JEPA and a billion-dollar startup (AMI Labs); Masayoshi Son is spending $5.4B on ABB Robotics to "fuse Artificial Super Intelligence and robotics"; Jeff Bezos has personally seeded nearly every US robot-brain lab while insisting his own physical-AI startup has "nothing to do with robotics"; Brett Adcock and Wang Xingxing bet on humanoids from opposite ends of the cost curve; Karol Hausman and Sergey Levine bet the brain matters more than any body. The counterweight — Rodney Brooks, Gary Marcus, Ken Goldberg — pushes back hard; Brooks calls video-trained humanoid dexterity "pure fantasy thinking." The theses converge on world models and the software (not hardware) bottleneck; they conflict violently on form factor, timelines, and whether the market is $38B or $50T. Context: [Key people](key-people.md), [Investment](investment.md), [Open problems](open-problems.md), [State of the art](state-of-the-art.md).

## How to read this page

- Quotes below are dated and, where possible, primary (keynotes, earnings calls, X posts, official releases, published essays). Secondary attributions are marked.
- Three rhetoric classes matter: **investor-pitch framing** (TAM figures, "biggest product ever"), **operational guidance** (production dates, unit counts — the legally riskier class), and **research theses** (falsifiable architectural bets). The same person often mixes all three in one sentence; this page separates them.
- Claims-vs-delivery ledgers live in the company deep dives ([Optimus](company-optimus.md), [Figure](company-figure.md)); this page covers the *framing* layer that sits on top.

## The TAM ladder — who claims what (as of 2026-07)

| Claim | Claimant, venue, date | Class |
|---|---|---|
| $50T market opportunity across factories, transportation, and humanoid robots | Jensen Huang, GTC Paris keynote, 2025-06 (press paraphrase, not a verbatim quote) | Investor-pitch |
| Humanoid robots a "~$40T" labor-automation market | Huang, repeatedly per financial press (as of 2026-05, secondary) | Investor-pitch |
| Manual labor ≈ 50% of global GDP, "~$42 trillion/yr" | Figure "Master Plan" (official company document) | Investor-pitch |
| "~80% of Tesla's value will be Optimus" | Elon Musk, X post, 2025-09-01 | Investor-pitch |
| Optimus could make Tesla "a $25 trillion company" | Musk, Tesla annual meeting, 2024-06 (widely reported) | Investor-pitch |
| Robotics as trillion-dollar-scale next SoftBank frontier; ¥1,000T (~$6.2T) NAV target | Masayoshi Son, SoftBank AGM, 2026-06-24 | Investor-pitch |
| ~$5T humanoid ecosystem by 2050 | Morgan Stanley (2025) | Analyst forecast |
| $38B humanoid TAM by 2035, ~1.4M units | Goldman Sachs (2024-02 revision) | Analyst forecast |

- The gap between the top and bottom rows is roughly **three orders of magnitude**; every trillion-dollar figure assumes solved [manipulation](manipulation.md), cheap [hardware](hardware.md), and data breakthroughs that remain [open problems](open-problems.md). Total disclosed 2025 revenue of the segment's biggest discloser (Unitree) was ~$235M ([Investment](investment.md)).

## Jensen Huang (NVIDIA) — Physical AI as the next wave

- **Thesis**: AI progresses in waves — perception AI → generative AI → agentic AI → **physical AI** ("AI that understands the laws of physics, AI that can work among us"); NVIDIA sells the platform for the last wave regardless of which robot maker wins. See [NVIDIA deep dive](company-nvidia.md).
- **"ChatGPT moment" arc** (a marketing clock that keeps ticking): "The ChatGPT moment for general robotics is just around the corner" (CES keynote, 2025-01-06) → "The age of generalist robotics is here" (GTC, 2025-03) → "The ChatGPT moment for physical AI is nearly here, but the challenge is clear. The physical world is diverse and unpredictable" (CES keynote, 2026-01, per the Rev transcript — the line is narrated in the keynote's Cosmos video segment, not spoken by Huang directly; some coverage rendered it as "is here") → "Physical AI has arrived — every industrial company will become a robotics company" (GTC, 2026-03).
- **Three-computer thesis** (canonical since late 2024): "Building autonomous vehicles, like all robots, requires three computers: NVIDIA DGX to train AI models, Omniverse to test drive and generate synthetic data, and DRIVE AGX, a supercomputer in the car" (CES 2025) — train (DGX) / simulate (Omniverse+Cosmos) / act (Jetson), all on NVIDIA silicon.
- **TAM framing**: $50T across factories, transportation, humanoids (GTC Paris, 2025-06, secondary); ~$40T humanoid labor automation (financial press, 2026-05, secondary). He defines physical AI as needing "common sense of how the world works. Object permanence… causality… friction and gravity" (CES 2026).
- **Rhetoric vs disclosure**: NVIDIA's automotive-and-robotics segment was ~$2.3B of $215.9B FY2026 revenue (~1%), robotics not broken out — the TAM talk is demand creation for compute, and Cosmos explicitly "swaps the data problem for a compute problem" (GTC 2026 framing).

## Elon Musk (Tesla) — Optimus as the biggest product of all time

- **Value claim**: "~80% of Tesla's value will be Optimus" (X, 2025-09-01 — posted the same day Tesla published its "Master Plan Part 4" manifesto on "sustainable abundance"); earlier: Optimus could make Tesla "a $25 trillion company" (annual meeting, 2024-06, widely reported via CNBC recap). His ~$1T compensation package (approved 2025-11-06) embeds **"1 million bots delivered"** as a milestone — the claim is now a capital-allocation framework, not just talk.
- **Product claim**: "I think Optimus will be our biggest product, not just Tesla's biggest product ever, but probably the biggest product ever… I remain convinced of that conclusion" (Q1 2026 earnings call, 2026-04-22, per call transcript).
- **Operational guidance is far humbler than the vision**: on the Q4 2025 call (2026-01-28) Musk conceded "We are still very much at the early stages of Optimus. It's still in the R&D phase" and that it is "not in usage in our factories in a material way"; on 2026-07-02 he warned "production will be extremely slow at first… This is not like making a car."
- **Timeline record**: every major production target since 2021 missed (10,000 units promised for 2025 → "hundreds" built) — the full claims-vs-delivery ledger is in [Optimus deep dive](company-optimus.md). Musk's framing is the field's purest case of investor-pitch and operational classes diverging in the same speaker.
- **Architecture thesis**: a car is "a robot on wheels" (AI Day, 2021-08) — FSD's vision-only end-to-end stack, fleet data, neural world simulator, and custom silicon transfer directly to the humanoid; one foundation model projected onto different embodiments (Elluswamy, CVPR 2026, aggregator-sourced).

## Demis Hassabis (Google DeepMind) — embodied intelligence on the path to AGI

- **Thesis**: true general intelligence requires understanding the spatio-temporal physical world; "intelligent physical agency" is a core pillar of AGI, not an application bolted on afterward. AGI itself: "in the next five to ten years" (Google I/O fireside with Sergey Brin, 2025-05).
- **Bottleneck claim**: "the bottleneck in robotics isn't so much the hardware… but it's actually the software intelligence that has always held robotics back" (interview, 2025, secondary attribution) — directly opposite Brooks's hardware/sensing argument, aligned with Hausman and Wang Xingxing.
- **Timeline**: AI-powered robotics "is going to have its breakthrough moment in the next couple of years" (to WIRED, ~2025-11, via Semafor); tightened to "over the next 18 months or so, we're going to see breakthrough moments in robotics" (Fortune, 2026-02-11).
- **Strategy**: Gemini as the "operating system" for robotics (Semafor, 2025-11) — cross-embodiment closed-weight models (Gemini Robotics 2025-03 → On-Device 2025-06 → Robotics 1.5 with ER reasoner, 2025-09) licensed onto partner hardware (Apptronik investment + partnership; deployments on Atlas and Apollo) rather than building robots. Capital-light and embodiment-agnostic; contrast [Figure](company-figure.md)'s vertical integration. See [VLA models](vla-models.md).

## Fei-Fei Li (World Labs / Stanford) — the spatial-intelligence manifesto

- **Manifesto**: "From Words to Worlds: Spatial Intelligence is AI's Next Frontier" (Substack, 2025-11-10). Core critique of LLMs: "they remain wordsmiths in the dark; eloquent but inexperienced, knowledgeable but ungrounded."
- **Positive thesis**: the next frontier is **world models** — generative, multimodal, interactive systems that "generate worlds with perceptual, geometrical, and physical consistency" and "output the next states based on input actions" — requiring new training objectives grounded in geometry/physics and architectures beyond 1D tokenization. See [World models](world-models.md).
- **Robotics is downstream, not the product**: "Animals from insects to humans depend on spatial intelligence to understand, navigate and interact with their worlds. Robots will be no different." World Labs sells the world model (Marble, first commercial generative-3D world model, 2025-11; $1B round led by Autodesk, 2026-02-18), not robots — robotics is one of several application markets alongside creative tools and science.

## Yann LeCun (AMI Labs) — world models against the LLM consensus

- **Negative thesis** (held publicly since ~2022, sharpened 2024–26): scaling LLMs will not reach human-level intelligence; autoregressive token prediction lacks persistent memory, world modeling, and planning. At Davos (2025-01-23) he predicted a "new paradigm of AI architectures" within 3–5 years and declared the coming years the **"decade of robotics."**
- **Positive thesis**: anti-generative **JEPA-family world models** that predict in representation space, not pixels — the architecture robots need to predict consequences of actions (V-JEPA 2, 2025-06; see [World models](world-models.md)). He prefers "Advanced Machine Intelligence" (AMI) over "AGI."
- **Acted on it**: left Meta 2025-11 after 12 years; co-founded **AMI Labs** (Paris; CEO Alexandre LeBrun), which closed a **$1.03B seed at $3.5B pre-money (2026-03-09)** — Europe's largest seed round — with Bezos Expeditions co-leading (alongside Cathay Innovation, Greycroft, Hiro Capital, HV Capital) and NVIDIA, Samsung, Temasek, Toyota Ventures participating. First announced application is healthcare (Nabla partnership), with world models framed as the key to unlocking everything from "truly useful domestic robots" to Level 5 autonomous driving (MIT Technology Review, 2026-01-22, which headlined the venture "a contrarian bet against large language models").
- Note the irony: the field's loudest LLM skeptic and its loudest humanoid skeptic (Brooks) agree on the diagnosis (current stacks can't ground themselves in the physical world) but not the prescription (LeCun: new architecture will fix it; Brooks: touch/force data and the form factor are the wall).

## Masayoshi Son (SoftBank) — ASI fused with robotics

- **Thesis quote**: "SoftBank's next frontier is Physical AI. Together with ABB Robotics, we will unite world-class technology and talent under our shared vision to fuse Artificial Super Intelligence and robotics — driving a groundbreaking evolution that will propel humanity forward" (official release, 2025-10-08). Son has long framed ASI as "10,000 times smarter than a human," targeted ~2035 (SoftBank AGM, 2024-06).
- **Checkbook record (as of 2026-07)**: **ABB robotics arm for $5.375B** (2025-10-08; closing mid-to-late 2026) — buying an incumbent #2 industrial-robot maker as the "body" for the AI thesis; **led Skild AI's $1.4B round at >$14B** (2026-01); robotics assets consolidated under a "Robo HD" holding company (reported); plus the OpenAI-side **Stargate** exposure. Reported: a US AI+robotics company "Roze" targeting a ~$100B-valuation IPO as early as H2 2026 (aggregator-only sourcing, unverified).
- **2026 AGM rhetoric** (2026-06-24): NAV target of ¥1,000T (~$6.2T, a ~14× increase) in 16 years on the ASI thesis; "I think it's blasphemy against AI if you say it's a bubble," with the AI revolution "just beginning"; claims to be "the first in the world to have robots manufacturing robots at scale" at a "physical AI plant" (company-reported, unverified); dismissed Musk's orbital data centers as having little merit in the AI race — the battle will be won by compute on Earth in "the next few years" (Bloomberg/Japan Times).
- Distinctive position: Son is the only mega-allocator buying **industrial robotics incumbents** (ABB's install base) rather than only humanoid startups — a bet that Physical AI monetizes first through existing factory automation. See [Investment](investment.md), [Company: Skild](company-skild.md).

## Jeff Bezos — the portfolio thesis (and a pointed exception)

- No manifesto; the thesis is legible in the checkbook. Personal/Bezos Expeditions bets span **every layer**: robot brains ([Physical Intelligence](company-pi.md) Series A+B; [Skild](company-skild.md)), a vertically integrated humanoid ([Figure](company-figure.md) Series B, 2024-02), legged delivery hardware (RIVR seed; acquired by Amazon 2026-03), and world models (**co-led** LeCun's AMI Labs seed, 2026-03) — i.e., long the model layer across *competing* architectural theses.
- **Project Prometheus** (co-CEO with Vik Bajaj; launched with $6.2B, 2025-11; $12B at $41B valuation, 2026-06-11): building an "artificial general engineer" for design/manufacturing in computing, aerospace, autos — AI that learns "from real-world trial and error," not just digital data. Bezos was explicit the company has "nothing to do with robotics" (CNBC, 2026-06-11) — the clearest statement on record that **physical AI ≠ robots**: the intelligence-for-atoms layer is a market even without embodiment.
- Context remark: AI is "a kind of industrial bubble" but the benefits are "gigantic" and real (Italian Tech Week, 2025-10, widely reported) — bubble-acknowledging while increasing exposure.

## Brett Adcock (Figure) — humanoid-first vertical integration

- **Master Plan framing** (official): manual labor compensation ≈ 50% of global GDP ("~$42 trillion/yr"); as humanoids "join the workforce," labor cost trends toward the price of renting a robot; end state is labor-optional abundance. Adcock puts the opportunity at "roughly $40 trillion" (secondary) and claims: "We will have the ability to ship, if the robots work well, billions of robots in the commercial workforce"; "We think there will be billions in the workforce… ultimately over time they'll be in space too" (TIME, 2025-10).
- **Vertical-integration thesis**: one company must own model + hardware + factory + fleet data — stated when dumping OpenAI: "we can't outsource AI for the same reason we can't outsource our hardware" (2025-02-04); Helix framed as "Software 2.0" replacing the last ~109K lines of hand-written robot C++ (2026-01, company claim).
- **Form-factor argument**: the world is built for humans, so one humanoid that generalizes beats many special-purpose machines — the direct antithesis of Brooks (below) and of embodiment-agnostic Pi/Skild.
- Symbolic milestone: "For the first time, robots now outnumber humans at Figure" (X, 2026-06-20 — internal fleet, company-reported). Delivery-vs-claims ledger in [Figure deep dive](company-figure.md).

## Karol Hausman & Sergey Levine (Physical Intelligence) — the embodiment-agnostic robot brain

- **Thesis**: the bottleneck is intelligence, not hardware or mechanical design; build **one generalist model** ("a robot brain") trained on heterogeneous data from many robot types, and sell intelligence to every body — π0 → π0.5 → π*0.6 → π0.7 across arms, mobile bases, humanoids ([Company: PI](company-pi.md), [VLA models](vla-models.md)). LLM-style scaling dynamics are expected to transfer: "the same scaling dynamics that transformed language models may also unlock robotic intelligence" (Generalist interview framing, 2026-03-17).
- **Levine's scaling claim**: with π0.7, capabilities scale "more than linearly with data" once cross-task "skill remixing" emerges (TechCrunch, 2026-04) — the field's strongest on-record claim of an emergent-capability regime in robotics. His long-held position: the path runs through **real-world cross-embodiment robot data at scale**, not simulation or human video alone (CoRL talks, 2024–25).
- **Physical intelligence as AGI path**: Hausman frames solving physical intelligence as solving intelligence — the physical world is "far harder to simulate than it is to describe," so an AI that masters it subsumes the rest (interview framing, 2026-03).
- Same brain-first thesis, different flavor: **Deepak Pathak's Skild** pitches an "omni-bodied" brain spanning quadrupeds to humanoids ([Company: Skild](company-skild.md)); NVIDIA's GR00T is the platform version ([Company: NVIDIA](company-nvidia.md)).

## Wang Xingxing / 王兴兴 (Unitree) — cost-down mass market, model-bottleneck contrarian

- **Cost thesis (executed, not just stated)**: collapse the price floor until robots are consumer electronics — quadrupeds $45K → $1,600 (2017→2023); humanoids H1 ~$90K (2023) → G1 ~$13.5K (2024) → **R1 ¥39,900 (~$5,900, 2025-07)** — at ~60% gross margin via extreme vertical integration ([Unitree deep dive](company-unitree.md)). Hardware first, intelligence catches up on an installed base.
- **"ChatGPT moment" definition** (2026中国网络媒体论坛, 2026-03-29): if a robot dropped into unfamiliar scenes can complete ~80% of tasks in ~80% of them from voice/language commands — his recurring "double 80%" (双80%) formulation, also stated to Xinhua 2025-11; some coverage of the forum renders it "80–90% of tasks" — embodied AI has had its ChatGPT moment. He expects it in **~2–3 years** (2026-03-29); at his WRC keynote (2025-08-09) he put the range at 1–3 years fast case, 3–5 years slow case, and he has said the whole embodied-AI wave won't take more than ~10 years. He describes the field as pre-critical-point: direction found, threshold not yet crossed (2025–26 remarks).
- **Contrarian bottleneck claim** (World Robot Conference keynote, 2025-08-09): the binding constraint is **the model, not data** — "attention to robot data is a bit too high; the biggest problem is the model" (paraphrase of 数据关注度太高，最大问题在模型); current VLA models are a "傻瓜式" ("simpleton") architecture; he expects **video-generation / world-model-driven control** to converge faster. This directly contradicts the data-bottleneck consensus of Pi/Figure/NVIDIA ([Data](data.md)).
- **Volume view**: global humanoid shipments can keep doubling annually; given a major AI breakthrough within 2–3 years, single-year shipments could jump to hundreds of thousands — "even a million+" — of units (2025–26 interviews, company-aligned optimism).

## The counterweight — named skeptics on the record

- **Rodney Brooks** (iRobot/Rethink co-founder; subsumption-architecture pioneer — see [History](history.md)). Essay "Why Today's Humanoids Won't Learn Dexterity" (rodneybrooks.com, 2025-09-26): believing today's humanoids will learn human-level dexterity "any time within decades is pure fantasy thinking" because video carries no touch/force signal while human hands have ~17,000 low-threshold mechanoreceptors; full-size bipeds are intrinsically unsafe near people (his ~3 m rule); successful robots "fifteen years from now… will look like neither today's humanoid robots nor humans" (wheels, multiple arms); expects the hype to end in a Gartner-style "trough of disillusionment" with goal-post redefinition. His companion dated prediction (2025-09/10, restated in his 2026-01-01 Predictions Scorecard): deployable "dexterity will remain pathetic compared to human hands **beyond 2036**." Restated re Musk: humanoid catchall assistants are "pure fantasy thinking" (Fortune, 2026-02-25). Full technical treatment in [Open problems](open-problems.md).
- **Gary Marcus** (NYU emeritus; serial deep-learning skeptic). On robotics specifically: called the Optimus reveal "a bit of a dud" with no articulated go-to-market (IEEE Spectrum roundup, 2022-10; Substack "Sub-Optimal"); on Musk's prediction that humanoids will outnumber humans by 2040: "Elon has a track record of overoptimistic predictions about AI, and this one is no different," noting only ~1.5B cars exist as an adoption-ceiling analogy (Decrypt, 2024-10); repeatedly amplifies teleoperation concerns in humanoid demos. Robotics is a secondary front for Marcus (his primary target is LLM reasoning), so his robot-specific record is thinner than Brooks's (analysis).
- **Ken Goldberg** (UC Berkeley): "100,000-year data gap" between what robots need and what exists; no robot butlers/surgeons in "2, 5, or even 10 years" (2025-08) — the academic version of Brooks's data argument, though Goldberg backs bootstrapping via engineering plus deployment data.
- Meta-observation (from [Open problems](open-problems.md) §8): the shortest timelines come from sellers of robots or compute; the longest from academics with no P&L. Both are incentive-laden; watch reliability-at-economics milestones instead.

## Convergence / divergence matrix

Where the theses **agree** (as of 2026-07):

- **Software/intelligence is the bottleneck, not actuators** — Huang, Hassabis, Hausman/Levine, Adcock, Wang, Son all state versions of this; even Brooks agrees hardware exists, he just adds sensing (touch/force) to the missing list.
- **World models are the next architectural layer** — explicit in Li (manifesto), LeCun (JEPA/AMI), Huang (Cosmos/DreamZero), Wang (video-gen-driven control), Tesla (neural world simulator), 1X; the VLA and world-model threads are visibly merging ([World models](world-models.md), [VLA models](vla-models.md)).
- **Data scarcity defines the race** — near-consensus (Pi, Figure×Brookfield, NVIDIA synthetic data, Goldberg's gap, Brooks's tactile-data critique), with Wang Xingxing as the loudest dissenter (model architecture first).
- **The prize is labor, i.e., tens of trillions** — every seller's TAM is a share-of-global-labor calculation (Huang $40–50T, Figure $42T/yr framing, Musk's 80%-of-Tesla), not a bottoms-up unit forecast.

Where they **conflict**:

| Axis | Positions |
|---|---|
| Form factor | Humanoid-first: Musk, Adcock, Wang, (Son via ABB+humanoid bets) ↔ embodiment-agnostic brain: Hausman/Levine, Pathak, NVIDIA, Hassabis ↔ anti-humanoid: Brooks (wheels + task-specific bodies win) |
| Bottleneck | Data: Pi, Figure, NVIDIA, Goldberg ↔ model architecture: Wang, LeCun, Li ↔ touch/force sensing + physics of contact: Brooks |
| LLM lineage | VLAs built on VLM backbones (Pi, DeepMind, Figure, NVIDIA) ↔ LLMs are the wrong substrate entirely (LeCun, Li; Wang calls VLA "simpleton architecture") |
| Timeline to "ChatGPT moment" | Already here / imminent: Huang (CES/GTC 2026), Adcock ↔ 18 months–3 years: Hassabis, Wang ↔ 5–10+ years: Goldberg ↔ beyond 2036 for dexterity: Brooks |
| TAM | $40–50T (Huang, Adcock, Musk-adjacent) ↔ $5T by 2050 (Morgan Stanley) ↔ $38B by 2035 (Goldman) — a 1,000× spread |
| Who captures value | Platform/compute (Huang) ↔ vertical integrator (Musk, Adcock) ↔ model layer sold to all bodies (Hausman, Pathak, Hassabis) ↔ low-cost hardware at scale (Wang) ↔ incumbent install base + capital (Son) |
| Robotics ↔ AGI | Embodiment required for/central to AGI: Hassabis, Hausman, LeCun (grounding) ↔ physical AI valuable without robots: Bezos-Prometheus ("nothing to do with robotics"), Li (robotics one application of spatial intelligence) |
| Is it a bubble? | "Blasphemy" to say so: Son ↔ bubble but worth it: Bezos ↔ bubble that will burst: Brooks; China's NDRC has warned too ([Investment](investment.md)) |

- **Executive read**: the bull theses are not one thesis. A portfolio exposed to "Physical AI" is simultaneously long incompatible bets — humanoid vs non-humanoid, data-scaling vs new-architecture, platform vs vertical. The only universally shared, falsifiable near-term claim is Hassabis/Wang-style: a visible generalization breakthrough by ~2028. Brooks's dexterity line (no human-level manual skill for decades) is the cleanest standing counter-claim to score everyone against.

## Sources

- https://blogs.nvidia.com/blog/ces-2025-jensen-huang/ — CES 2025 keynote: "ChatGPT moment for general robotics is just around the corner"; three-computers quote (official)
- https://www.rev.com/transcripts/nvidia-at-ces-2026 — CES 2026 transcript: "ChatGPT moment for physical AI is nearly here" (narrated in the Cosmos video segment); Huang's physical-AI/common-sense definition (primary transcript)
- https://www.manufacturingdive.com/news/industrial-robotics-companies-everywhere-says-nvidia-ceo-gtc-2026-abb-fanuc-ai/815042/ — GTC 2026 (2026-03-16): Huang: "every industrial company will become a robotics company"; "Physical AI has arrived" framing
- https://gamesbeat.com/nvidia-believes-physical-ai-systems-are-a-50-trillion-market-opportunity/ — Huang $50T physical-AI framing at GTC Paris (2025-06, secondary; press paraphrase, no verbatim quote)
- https://247wallst.com/investing/2026/05/31/jensen-huang-just-called-humanoid-robots-a-40-trillion-market-heres-why-wall-street-is-loading-up-on-physical-ai-stocks/ — $40T humanoid TAM attribution (2026-05, secondary)
- https://x.com/elonmusk/status/1962618811141812475 — Musk primary post: "~80% of Tesla's value will be Optimus" (2025-09-01)
- https://www.cnbc.com/2025/09/02/musk-tesla-value-optimus-robot.html — context: Master-Plan-4 same-day timing; prior $25T-company claim recap
- https://www.npr.org/2026/04/22/nx-s1-5791653/tesla-earnings-first-quarter-2026 — Q1'26 call coverage: biggest-product framing; production summer 2026, useful "outside Tesla" next year
- https://www.investing.com/news/transcripts/earnings-call-transcript-tesla-beats-q1-2026-eps-forecasts-stock-rises-93CH-4631008 — Q1'26 call transcript: "I think Optimus will be our biggest product, not just Tesla's biggest product ever, but probably the biggest product ever"; "I remain convinced of that conclusion" (verbatim)
- https://www.semafor.com/article/11/23/2025/deepmind-deepens-push-into-robotics — Hassabis to WIRED: robotics "breakthrough moment in the next couple of years"; Gemini-as-OS strategy (2025-11)
- https://fortune.com/article/fortune-500-titans-and-disruptors-of-industry-google-deepmind-demis-hassabis-isomorphic-artificial-intelligence/ — Hassabis: "over the next 18 months or so, we're going to see breakthrough moments in robotics, too" (2026-02-11)
- https://kantrowitz.medium.com/demis-hassabis-and-sergey-brin-on-ai-scaling-agi-timeline-robotics-simulation-theory-ef3f7a740eeb — I/O 2025 fireside: AGI "next five to ten years" (2025-05)
- https://www.digit.in/features/general/demis-hassabis-says-ai-led-robot-revolution-is-unfolding-right-now-heres-why.html/amp/ — Hassabis "bottleneck… software intelligence" quote (secondary)
- https://drfeifei.substack.com/p/from-words-to-worlds-spatial-intelligence — Fei-Fei Li manifesto (2025-11-10): "wordsmiths in the dark", world-model definition, robots "will be no different" (primary)
- https://techcrunch.com/2025/01/23/metas-yann-lecun-predicts-a-new-ai-architectures-paradigm-within-5-years-and-decade-of-robotics/ — LeCun at Davos 2025-01: new-paradigm prediction, "decade of robotics"
- https://www.technologyreview.com/2026/01/22/1131661/yann-lecuns-new-venture-ami-labs/ — AMI Labs as "contrarian bet against large language models" (2026-01)
- https://techcrunch.com/2026/03/09/yann-lecuns-ami-labs-raises-1-03-billion-to-build-world-models/ — AMI Labs $1.03B seed at $3.5B pre-money (2026-03-09); LeBrun quotes; Bezos Expeditions co-lead
- https://group.softbank/en/news/press/20251008 — Son primary quote: "SoftBank's next frontier is Physical AI… fuse Artificial Super Intelligence and robotics"; ABB deal $5.375B (2025-10-08)
- https://www.forbes.com/sites/iansayson/2025/10/08/billionaire-masayoshi-sons-softbank-deepens-ai-push-with-54-billion-abb-robotics-deal/ — ABB robotics deal coverage, closing timeline
- https://www.thestandard.com.hk/innovation/article/335487/Talk-of-a-bubble-is-blasphemy-against-AI-says-SoftBanks-Son — Son AGM 2026-06-24: "I think it's blasphemy against AI if you say it's a bubble"; robots-manufacturing-robots claim
- https://www.japantimes.co.jp/business/2026/06/23/companies/softbank-dismissal-musk-idea-data-centers/ — Son dismisses Musk's orbital data centers (little merit; Earth compute wins "the next few years")
- https://finance.biggo.com/news/bdc0a37f-28fe-453d-b8e6-ba8af661a224 — Son AGM: ¥1,000T NAV target, ASI 10,000× framing (secondary)
- https://www.outlookbusiness.com/deeptech/masayoshi-son-rejects-ai-bubble-fears-outlines-softbanks-plans-of-robots-manufacturing-robots — "robots manufacturing robots at scale"; Roze $100B IPO target (reported, unverified)
- https://www.businesswire.com/news/home/20260114335623/en/Skild-AI-Raises-$1.4B-Now-Valued-Over-$14B — SoftBank-led Skild round (2026-01)
- https://www.cnbc.com/2026/06/11/project-prometheus-bezos-bajaj-live-updates.html — Bezos on Prometheus: "artificial general engineer," "nothing to do with robotics" (2026-06-11)
- https://techcrunch.com/2026/06/11/jeff-bezoss-prometheus-raises-12b-to-build-an-artificial-general-engineer-for-the-physical-world/ — Prometheus $12B at $41B; real-world trial-and-error framing
- https://www.figure.ai/master-plan — Figure Master Plan: labor ≈50% of global GDP (~$42T/yr), rent-a-robot cost logic (primary)
- https://time.com/7324233/figure-03-robot-humanoid-reveal/ — Adcock: "billions in the workforce… space too" (2025-10)
- https://techcrunch.com/2025/02/04/figure-drops-openai-in-favor-of-in-house-models/ — Adcock vertical-integration rationale ("can't outsource AI")
- https://techcrunch.com/2026/01/30/physical-intelligence-stripe-veteran-lachy-grooms-latest-bet-is-building-silicon-valleys-buzziest-robot-brains/ — Pi thesis: bottleneck is intelligence, not hardware; one model many embodiments
- https://www.generalist.com/p/karol-hausman-physical-intelligence — Hausman interview (2026-03-17): scaling-dynamics framing; "harder to simulate than describe"
- https://techcrunch.com/2026/04/16/physical-intelligence-a-hot-robotics-startup-says-its-new-robot-brain-can-figure-out-tasks-it-was-never-taught/ — Levine: capabilities scale "more than linearly with data" (π0.7)
- https://www.chinanews.com.cn/cj/2026/03-29/10594954.shtml — Wang Xingxing 2026-03-29 forum: embodied-AI "GPT moment" definition (this outlet renders it "80–90% of tasks" in unfamiliar scenes), ~2–3 years (Chinese primary coverage)
- http://www.news.cn/energy/20251106/0ee9e5e4f67a482884b7ee537912895d/c.html — Xinhua 2025-11-06: Wang's "两个80%" (double-80%) critical-point definition, 1–3 year window
- https://zhidx.com/p/496440.html — Wang WRC 2025-08-09 keynote: model (not data) bottleneck; VLA "傻瓜式"; world-model/video-gen path; 1–3 yr fast / 3–5 yr slow (Chinese)
- https://finance.ifeng.com/c/8lgDwnjxZgX — Wang interview: global humanoid shipments to keep doubling annually; breakout to hundreds of thousands (even 1M+) units/yr on an AI breakthrough (Chinese)
- https://www.21jingji.com/article/20250809/herald/fecc404938f03df050143f46e4922853.html — Wang: "robot-data attention too high; biggest problem is the model" (2025-08-09, Chinese)
- https://rodneybrooks.com/why-todays-humanoids-wont-learn-dexterity/ — Brooks essay (2025-09-26): "pure fantasy thinking," ~17,000 mechanoreceptors, 3 m rule, 15-year form-factor prediction, "trough of disillusionment" (primary; the 2036 line is NOT in this essay)
- https://rodneybrooks.com/predictions-scorecard-2026-january-01/ — Brooks dated prediction (primary): "dexterity will remain pathetic compared to human hands beyond 2036"; walking humanoids "too unsafe to be in close proximity to real humans"
- https://techcrunch.com/2025/09/26/famed-roboticist-says-humanoid-robot-bubble-is-doomed-to-burst/ — Brooks: bubble framing; non-humanoid forms win in ~15 years
- https://fortune.com/2026/02/25/mit-roboticist-irobot-cofounder-roomba-robot-vacuum-elon-musk-tesla-optimus-pure-fantasy-thinking/ — Brooks restated "pure fantasy thinking" re Musk vision (2026-02-25)
- https://spectrum.ieee.org/robotics-experts-tesla-bot-optimus/gary-marcus — Marcus on Optimus: "a bit of a dud", no go-to-market (2022)
- https://garymarcus.substack.com/p/sub-optimal — Marcus "Sub-Optimal": Optimus skepticism, teleoperation questions (primary)
- https://decrypt.co/289058 — Marcus to Decrypt (2024-10, on Musk's robots-outnumber-humans-by-2040 prediction): "track record of overoptimistic predictions"; ~1.5B-cars analogy
- https://news.berkeley.edu/2025/08/27/are-we-truly-on-the-verge-of-the-humanoid-robot-revolution/ — Goldberg: 100,000-year data gap; no butlers in 2/5/10 years (2025-08)
