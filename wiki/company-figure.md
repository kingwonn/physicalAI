---
title: "Company Deep Dive: Figure AI"
slug: company-figure
updated: 2026-07-04
confidence: verified
---
> Figure AI (founded 2022 by Brett Adcock, HQ San Jose, CA) is the most highly valued pure-play humanoid company in the world — >$1B Series C at a **$39B post-money valuation** (2025-09), a 15x step-up in 18 months — and the flagship of the US "vertical integration" thesis: its own robot (Figure 03), its own VLA stack (Helix → Helix 02, built after dumping OpenAI in 2025-02), and its own factory (BotQ, ramped from 1 robot/day to ~1/hour with >350 Figure 03s built by 2026-04). Its deployment proof points are BMW Spartanburg (Figure 02 supported 30,000+ X3s; Figure 03 now doing sequencing logistics) and a retail-logistics deal with Catalyst Brands (JCPenney et al., 2026-05). The skeptic case is equally concrete: no disclosed revenue, a documented gap between CEO claims and BMW-confirmed facts (Fortune, 2025-04), a safety whistleblower lawsuit (2025-11), and delivery numbers that are mostly self-reported internal fleet, not customer-sold units. Context: [Humanoids](humanoid-robots.md), [VLA models](vla-models.md), [Landscape: USA](landscape-usa.md), [Investment](investment.md).

## Founding and team

- **Founded 2022** by **Brett Adcock** — serial founder (Vettery, sold to Adecco for ~$100M; Archer Aviation, took public via SPAC). Adcock initially bootstrapped Figure and put **$20M of personal capital into the Series A** (per Wikipedia's sourcing); he reportedly retains ~50% ownership (unverified).
- Early team recruited from **Boston Dynamics, Tesla, Apple, Google DeepMind** — deliberately hardware-heavy at first, then AI-heavy after the OpenAI split.
- **Corey Lynch** (ex-Google Brain, language-conditioned imitation learning) joined 2023-06 and led the Helix effort as Director of AI — part of the broader Google-robotics diaspora that seeded the US field (see [Key people](key-people.md)).
- Headcount has stayed small relative to valuation: ~180 employees in early coverage (Wikipedia), growing to ~400 by end-2025 and ~650–660 in 2026 per the "Headcount vs Robots" chart Adcock published. Adcock posted **"For the first time, robots now outnumber humans at Figure"** (X, 2026-06-20 — primary post confirmed); the chart shows the robot fleet crossing the headcount line in Q2 2026 at roughly **700–750 robots vs ~650 staff** (both company-reported; no third-party audit). A widely repeated "~200–250 staff" figure traces to a single aggregator and is inconsistent with the chart's mid-2026 crossover (>350 robots already existed by 2026-04) — treat it as erroneous.
- Adcock has also launched **Hark**, a separate personal-AI hardware/model lab seeded with $100M of his own capital (The Information, 2026-03); Hark raised a **$700M Series A at $6B post-money** led by Parkway Venture Capital — the same lead as Figure's Series A/C (TechCrunch, 2026-05-21).
- Mission framing ("Master Plan"): general-purpose humanoids for labor shortage → commercial logistics/manufacturing first, then the home.

## Funding history (as of 2026-07)

| Round | Date | Amount | Post-money | Lead / notable investors |
|---|---|---|---|---|
| Bootstrap | 2022 | Adcock personal | — | — |
| Series A | 2023-05 | $70M | undisclosed | Parkway Venture Capital; incl. $20M from Adcock |
| Series B | 2024-02-29 | **$675M** | **$2.6B** | Microsoft, OpenAI Startup Fund, NVIDIA, Jeff Bezos (via Bezos Expeditions), Parkway, Intel Capital, Align Ventures, ARK Invest (per official PR; some coverage adds Amazon Industrial Innovation Fund, which the PR does not name) |
| Series C | 2025-09-16 | **>$1B** ("exceeds $1B", exact undisclosed) | **$39B** | Parkway Venture Capital (lead); Brookfield, NVIDIA, Macquarie Capital, Intel Capital, LG Technology Ventures, Qualcomm Ventures, Salesforce, T-Mobile Ventures |

- Total raised **~$1.9B** (as of 2026-01). The Series C was reportedly marketed as "$1.5B at $39.5B" during the raise (TechCrunch, 2025-04); the closed round was announced as ">$1B at $39B post-money" — use the official figures.
- The $2.6B → $39B step-up (15x in 18 months) made Figure one of the ~20 most valuable startups in the world with **no disclosed revenue** — see [Investment](investment.md) for the valuation-vs-revenue gulf (contrast [Unitree](company-unitree.md): ~$6B IPO valuation *with* ~$235M 2025 revenue).
- Signed alongside the Series C: a data partnership with **Brookfield** ("Project Go-Big") opening ~100,000 residential units for egocentric/humanoid pre-training data collection — see [Data](data.md).
- During the raise Figure sent **cease-and-desist letters to secondary-market brokers** trading its shares (TechCrunch, 2025-04-29) — read variously as standard cap-table hygiene or as valuation control.

## Helix: the in-house model bet

### Architecture

- **Helix** (announced 2025-02-20): dual-system VLA for full upper-body humanoid control. **System 2** — a 7B open-source-based VLM running at 7–9 Hz for scene/language understanding — emits a latent goal vector consumed by **System 1**, an 80M-parameter visuomotor transformer at **200 Hz** outputting continuous commands over a 35-DoF action space (wrists, individual fingers, torso, head gaze). Trained on ~500 h of teleop; runs fully onboard dual embedded GPUs; one set of weights ran two robots collaborating (company-claimed firsts: first full-upper-body humanoid VLA, first multi-robot VLA, first fully-onboard commercial VLA). Closed weights.
- **Helix 02** (2026-01-27): adds **System 0**, a 10M-param whole-body reflex/balance controller at **1 kHz** below S1/S2, trained on 1,000+ h of human motion across 200k+ parallel simulated environments; integrates Figure 03's tactile fingertips (~3 g sensitivity) and palm cameras. Headline demo: ~4-minute, 61-action dishwasher unload/reload with no resets — company-reported, no third-party benchmark. Adcock frames Helix 02 as "Software 2.0": Figure says it deleted its last ~109,504 lines of hand-engineered C++ robot code (company claim via interview).
- Company claims Helix 02 robots have completed full 8-hour autonomous logistics shifts (2026-05, company claim, unverified).
- **~200-hour livestreamed endurance run (2026-05)**: an 8-hour endurance challenge publicly issued by automation analyst Scott Walter grew into a 200-hour continuous package-sorting run (started ~2026-05-13, completed 2026-05-22; streamed publicly as the YouTube "F.03 Livestream" series, Days 1–9) at Figure's HQ (San Jose per Sherwood; some coverage says Sunnyvale) — a small team of Figure 03s on Helix 02 (three or four units; reports differ; rotated via battery swaps; viewer-nicknamed Rose/Bob/Frank/Jim, among others) sorted **~249,560 packages with zero reported hardware failures or system-halting crashes** (occasional software-level errors, e.g. dropped packages, acknowledged). Figure's most externally observable reliability datapoint to date, though throughput/failure metrics remain self-reported (as of 2026-07).
- Full lineage and technical context in [VLA models](vla-models.md); Helix logistics-scaling metrics (cycle times approaching human speed on package handling) are company-published.

### vs. competitor VLAs (as of 2026-07)

| Stack | Owner | Design | Embodiment strategy | Weights |
|---|---|---|---|---|
| Helix / Helix 02 | Figure | 3-tier: S2 7B VLM (7–9 Hz) → S1 80M policy (200 Hz) → S0 10M reflex (1 kHz); fully onboard | **Single-embodiment** (Figure robots only); trained heavily on own fleet + teleop | Closed |
| π0 / π0.5 / π*0.6 / π0.7 | Physical Intelligence | ~3B VLM + flow-matching action expert (~50 Hz); RECAP RL from deployment | Cross-embodiment (arms, mobile, humanoids) | π0/π0.5 open |
| GR00T N1–N2 | NVIDIA | Dual-system (like Helix); N2 adds world-action modeling | Cross-embodiment ecosystem play across partner robots | Open |
| Gemini Robotics 1.5 | Google DeepMind | ER reasoner + VLA; on-device variant | Cross-embodiment; deployed on Atlas, Apollo | Closed |
- Figure's differentiators: deepest vertical integration (model + hardware + factory + fleet data flywheel), highest control-rate hierarchy (1 kHz reflex tier), everything onboard. Its risk: single-embodiment closed stack means no ecosystem revenue and no external validation; all headline capabilities are company-reported.

### OpenAI: partnership (2024) → split (2025)

- **2024-02-29**: collaboration agreement signed alongside the Series B (OpenAI Startup Fund invested) — OpenAI to develop specialized AI models for Figure robots. The 2024-03-13 Figure 01 voice-conversation demo (GPT-backed) went viral and defined the partnership publicly.
- **2025-02-04**: Adcock announced the split, citing a "major breakthrough" in fully end-to-end in-house robot AI (revealed 16 days later as Helix). Stated rationale: embodied AI must be vertically integrated ("we can't outsource AI for the same reason we can't outsource our hardware"); LLMs "getting smarter yet more commoditized." Adcock later said the partnership delivered "very little" and that OpenAI signaling it would pursue humanoids internally ended it ("I was just like, 'This is over'").
- Aftermath: OpenAI built its own robotics division (2025–26) and remains an investor in Physical Intelligence and 1X — see [Landscape: USA](landscape-usa.md).

## Figure 03 hardware (announced 2025-10-09)

- Third-generation robot, designed jointly for **BotQ mass manufacture** (die-cast/injection-molded parts replacing CNC) and **home settings**; TIME Best Invention 2025.
- **5'8" (~1.73 m), 61 kg, 20 kg payload, 5 h runtime, 1.2 m/s** per Figure's official spec page; **9% less mass than Figure 02** (announcement). The ~1.68 m figure in earlier secondary coverage is not supported by Figure's own spec sheet (corrected 2026-07-04).
- **2 kW inductive wireless charging** through foot coils (self-docking); ~2.3 kWh battery (reported); 5 h runtime (official spec page).
- Perception/manipulation: cameras with 2× frame rate, 75% lower latency, 60% wider FoV; **palm cameras** in each hand; **fingertip tactile sensors detecting ~3 g** (see [Tactile & hands](tactile-hands.md)); 2× faster actuators than 02; speech-to-speech audio.
- Soft washable textile covering — a home-safety/aesthetics signal unusual among industrial humanoids.
- Not for individual sale (as of 2026-07): commercial deployments plus a stated ~$20K consumer price target (unverified) and "broader home availability late 2026" (company target).

## BotQ manufacturing

- **Announced 2025-03**: dedicated humanoid factory; first-generation line rated **up to 12,000 robots/yr**; 4-year goal **100,000 robots** (company targets). Vertically integrated: in-house actuators, dedicated lines for critical modules, custom manufacturing execution software across 150+ networked workstations.
- **Ramp (official, 2026-04-29)**: production went **1 robot/day (2026-01) → ~1 robot/hour**, a claimed 24× throughput gain in under 120 days; **>350 Figure 03s built**; >9,000 actuators produced across 10+ SKUs; end-of-line first-pass yield >80%; battery-line yield 99.3% over 500+ packs; >50 in-process inspections and >80 end-of-line functional tests per robot.
- Caveat: all figures are company-published and the >350 units are largely allocated to *internal* R&D, Helix data collection, and household-task development, with only a share going to commercial deployment — this is a data-flywheel fleet more than a sales record.
- Note ~1/hour ≠ 12,000/yr sustained (that would require ~24/7 operation); treat "1/hour" as demonstrated peak line rate. An earlier "1 robot per ~90 minutes" report (2026-04) is consistent with the ramp trajectory (unverified).

## BMW Spartanburg — confirmed vs. claimed

The wiki's canonical example of separating primary-source fact from aggregator drift.

**BMW-confirmed (primary press releases):**
- **2024-01**: commercial agreement — BMW is Figure's first customer; Spartanburg (SC) the site.
- **2026-02-27 (BMW press — the Leipzig/"Physical AI in Europe" release)**: Figure 02 pilot results — ten-hour shifts Mon–Fri over ~10 months in the body shop (Figure counts an 11-month deployment overall), **90,000+ components moved in ~1,250 operating hours (~1.2M steps), supporting production of 30,000+ BMW X3s**. These figures were first self-published by Figure (2025-11-19) and then confirmed by BMW; BMW's 2026-06 release restates "30,000+ X3s over ten months".
- **2026-06-25 (BMW press; Figure's own post 2026-06-30)**: **Figure 03** deployed in Hall 52 for **sequencing logistics** — picking unsorted components from containers into sequencing trolleys for just-in-sequence assembly delivery, with Helix 02 coordinating hands/arms/torso/feet (including pulling wheeled carts); part of BMW's iFACTORY program, with development running in parallel at Spartanburg and Figure.
- **BMW-confirmed scale in early 2025** (via BMW spokesperson to Fortune): a **single robot**, working non-production hours until ~2025-03, then the same limited task during live production — materially more modest than contemporaneous public framing.

**Aggregator-sourced / unverified — do not upgrade without primary confirmation:**
- "~40 Figure 03 units at Spartanburg" — traces to a single aggregator (unverified).
- "~$25/robot-hour" billing at BMW (reported, unverified).
- "Figure expanded to BMW Leipzig" — **contradicted by BMW's own announcement**: BMW's first German humanoid pilot (Leipzig, summer 2026) uses **Hexagon Robotics' AEON**, not Figure. See [State of the art](state-of-the-art.md).

## Customers and verticals (as of 2026-07)

| Customer / vertical | Status | Confirmed by |
|---|---|---|
| BMW (auto manufacturing) | Figure 02 pilot completed; Figure 03 sequencing live | BMW + Figure primary |
| Catalyst Brands (retail logistics: JCPenney, Aéropostale, Brooks Brothers) | Commercial agreement 2026-05-26; first site Reno, NV distribution center (Joey Pouch sort system); first Figure↔Brookfield-portfolio bridge | Both parties' announcements |
| Unnamed "commercial clients" | Figure said it began shipping Figure 02 to commercial clients 2024-12; identities undisclosed | Company claim (unverified) |
| UPS (parcel logistics) | Talks reported 2025-04; never confirmed by either party | Secondary reports (unverified) |
| Home / consumer | Figure 02 home alpha testing from 2025 (accelerated 2 years, credited to Helix); Figure 03 designed for home; broader availability "late 2026" | Company statements; no shipped home product yet |

## Delivery record vs. public claims — the skeptic case

- **No disclosed revenue** at a $39B valuation; the entire mark is narrative + capability demos (see [Investment](investment.md)).
- **Fortune investigation (2025-04-06)**: found one robot at BMW working off-hours where public framing implied a fleet in production; Adcock called it "downright lies" and threatened defamation claims; no suit known to have been filed. At a 2025-06 conference he skipped a live demo and sidestepped BMW-deal questions (TechCrunch).
- **Whistleblower lawsuit (filed 2025-11)**: Robert Gruendel, former head of product safety (joined 2024-10), alleges he was fired days after warning that Figure robots could exert forces "twenty times the ISO 15066 pain threshold" — enough to fracture a skull — that a malfunctioning robot gashed a steel refrigerator door, and that a safety roadmap shown to Series C investors was downgraded after close ("could be interpreted as fraudulent"). Figure says he was terminated for performance and calls the allegations "falsehoods"; it has since **countersued Gruendel**, alleging he violated trade-secret law and company policy by saving company documents to a personal Google account (The Information). Possibly the first humanoid-safety whistleblower case — see [Safety & regulation](safety-regulation.md).
- **Delivery numbers are self-reported and mostly internal**: >350 built ≠ >350 sold; publicly confirmed external deployments are BMW (small fleet; exact count unverified) and Catalyst Brands (just starting). Compare Agility's published 65,000+ customer-site fleet hours — Figure's closest equivalent is the livestreamed ~200-hour HQ sorting run (2026-05), impressive but in-house rather than customer-site.
- **All Helix milestones lack third-party benchmarks** (61-action dishwasher run, 8-hour shifts, logistics cycle times) — plausible but unaudited; see [Evaluation](evaluation.md).
- **Aspirational-timeline pattern**: 100K robots in 4 years, home availability late 2026, "alpha in homes in 2025" — Figure has a better shipping record than Tesla Optimus but the same incentive structure for forward-leaning claims.
- Steel-man for the bull case: BMW *did* independently confirm the 02 pilot results and *did* expand to a harder Figure 03 use case; BotQ yield/throughput specifics are unusually detailed for a private company; and the Brookfield→Catalyst structure gives Figure a captive deployment channel.

## Sources

- https://www.prnewswire.com/news-releases/figure-raises-675m-at-2-6b-valuation-and-signs-collaboration-agreement-with-openai-302074897.html — Series B $675M at $2.6B + OpenAI collaboration agreement, investor list (official PR, 2024-02-29)
- https://www.prnewswire.com/news-releases/figure-exceeds-1b-in-series-c-funding-at-39b-post-money-valuation-302556936.html — Series C ">$1B" at $39B post-money (official PR, 2025-09-16)
- https://www.figure.ai/news/series-c — Series C investor list, use of funds, Brookfield data partnership (official)
- https://en.wikipedia.org/wiki/Figure_AI — founding (2022), HQ, Series A $70M incl. Adcock $20M, ~180 employees, partnership/controversy timeline
- https://www.figure.ai/news/helix — Helix architecture: S2 7B @ 7–9 Hz, S1 80M @ 200 Hz, 35-DoF, ~500 h teleop, claimed firsts (official, 2025-02-20)
- https://www.figure.ai/news/helix-02 — Helix 02: System 0 10M @ 1 kHz, tactile/palm-camera integration, 61-action dishwasher demo (official, 2026-01-27)
- https://www.humanoidsdaily.com/news/the-end-of-c-brett-adcock-on-helix-02-and-figure-s-path-to-room-scale-autonomy — Adcock interview: ~109K lines of C++ deleted, "Software 2.0" framing
- https://www.figure.ai/news/introducing-figure-03 — Figure 03 specs: 9% lighter, 2 kW wireless charging, 3 g tactile, palm cameras, mass-manufacture design (official, 2025-10; no height/weight given)
- https://www.figure.ai/figure — Figure 03 official spec page: 5'8", 61 kg, 20 kg payload, 5 h runtime, 1.2 m/s (settles the 1.68 m vs 1.73 m conflict)
- https://www.figure.ai/news/botq — BotQ announcement: 12,000/yr first-gen line, 100K 4-year goal, vertical integration (official, 2025-03)
- https://www.figure.ai/news/ramping-figure-03-production — >350 units, 1/day→1/hour in <120 days, >9,000 actuators, yield stats (official, 2026-04-29)
- https://www.press.bmwgroup.com/global/article/detail/T0458778EN/bmw-group-advances-the-use-of-physical-ai-in-production-with-figure-03-project-in-spartanburg?language=en — BMW primary: Figure 03 sequencing in Hall 52, Figure 02 pilot recap (2026-06-25)
- https://www.figure.ai/news/f-03-at-bmw — Figure's own Figure 03-at-BMW announcement (official, 2026-06-30)
- https://www.figure.ai/news/production-at-bmw — Figure 02 → 30,000+ cars, 90,000+ parts, 1,250+ h, 10-hr Mon–Fri shifts (official, 2025-11-19)
- https://www.press.bmwgroup.com/global/article/detail/T0455864EN/bmw-group-to-deploy-humanoid-robots-in-production-in-germany-for-the-first-time?language=en — BMW primary (2026-02-27): confirms Figure 02 pilot numbers (90,000+ components, ~1,250 h, 30,000+ X3s, ten months of ten-hour Mon–Fri shifts); announces Leipzig pilot with Hexagon AEON, not Figure
- https://www.therobotreport.com/bmw-group-deploys-figure-03-humanoid-after-tests-previous-version/ — independent confirmation of Figure 03 Spartanburg scope, Helix 02 cart-pulling
- https://fortune.com/2025/04/06/figure-ai-bmw-humanoid-robot-partnership-details-reality-exaggeration/ — Fortune: BMW confirmed single robot, non-production hours (skeptic anchor)
- https://mikekalil.com/blog/figure-ai-vs-fortune/ — Adcock "downright lies" response, defamation threat
- https://techcrunch.com/2025/04/29/figure-ai-sent-cease-and-desist-letters-to-secondary-markets-brokers/ — cease-and-desist letters; $1.5B/$39.5B raise reporting
- https://techcrunch.com/2025/06/06/figure-ai-ceo-skips-live-demo-sidesteps-bmw-deal-questions-on-stage-at-tech-conference/ — Adcock skips live demo, deflects BMW questions
- https://techcrunch.com/2025/02/04/figure-drops-openai-in-favor-of-in-house-models/ — OpenAI split announcement and rationale
- https://x.com/adcock_brett/status/1886860098980733197 — Adcock's split announcement post (primary, 2025-02-04)
- https://www.aol.com/articles/figure-ceo-speaks-openai-split-163554400.html — Adcock retrospective: partnership gave "very little," OpenAI going in-house on humanoids
- https://www.figure.ai/news/figure-signs-agreement-with-catalyst-brands — Catalyst Brands agreement, Reno NV DC (official, 2026-05-26)
- https://corporate.jcpenney.com/2026/05/26/catalyst-brands-taps-figure-ai-for-humanoid-automation/ — customer-side confirmation; Joey Pouch sorting, Brookfield link
- https://www.cnbc.com/2025/11/21/figure-ai-sued.html — CNBC: Gruendel suit (filed 2025-11-21), 20x ISO 15066 forces, refrigerator gash, Figure's "poor performance" response
- https://gizmodo.com/you-must-read-this-riveting-whistleblower-lawsuit-about-allegedly-dangerous-robots-2000688737 — Gruendel whistleblower suit details (2025-11)
- https://www.theinformation.com/briefings/figure-countersues-safety-whistleblower — Figure countersuit vs. Gruendel: trade-secret claims over documents saved to personal account
- https://roboticsandautomationnews.com/2025/11/26/former-figure-ai-engineer-at-claims-companys-humanoid-robots-powerful-enough-to-fracture-human-skull/96962/ — suit specifics: ISO 15066 forces, refrigerator incident, safety-roadmap allegation
- https://techcrunch.com/2025/02/27/figure-will-start-alpha-testing-its-humanoid-robot-in-the-home-in-2025/ — home alpha acceleration credited to Helix
- https://www.ttnews.com/articles/ups-figure-ai-robots — UPS–Figure talks (2025-04, unconfirmed)
- https://www.therobotreport.com/brookfield-partners-figure-ai-develop-humanoid-pre-training-dataset/ — Brookfield pre-training-data partnership
- https://x.com/adcock_brett/status/2068040783295627609 — Adcock post (primary, 2026-06-20): "For the first time, robots now outnumber humans at Figure" + Headcount-vs-Robots chart
- https://robohorizon.com/en-us/news/2026/06/figure-ceo-the-robots-have-officially-outnumbered-the-humans/ — chart reading: robots >700 crossing ~650 headcount in Q2 2026
- https://newskarnataka.com/technology/robots-now-outnumber-humans-at-figure-ai-says-ceo/21062026/ — independent chart reading: ~740 robots by Q2 2026, ~650–660 staff, ~400 staff end-2025
- https://explainx.ai/blog/figure-ai-robots-outnumber-humans-milestone-2026 — aggregator; its ">750 fleet vs ~200–250 staff" framing conflicts with Adcock's own chart (~650 staff) — do not reuse
- https://www.techtimes.com/articles/316632/20260514/figure-ais-helix-02-robots-complete-full-8-hour-autonomous-shifts-humanoid-race-intensifies.htm — 8-hour autonomous shift claim (company-sourced, unverified)
- https://sherwood.news/tech/figures-robots-just-sorted-packages-for-200-hours-straight/ — ~200-hour livestreamed sorting run, ~249,560 packages (2026-05)
- https://interestingengineering.com/ai-robotics/figure-03-humanoid-robot-200-hour-shift — zero-failure claim; Scott Walter 8-hour challenge origin; three robots (Bob/Jim/Rose); says Sunnyvale HQ (conflicts with Sherwood's San Jose)
- https://www.humanoidsdaily.com/news/figure-ai-pops-champagne-as-autonomous-marathon-crosses-200-hours-without-hardware-failure — run completed 2026-05-22; fleet rotation/battery swaps; software-level errors acknowledged alongside zero-hardware-failure claim
- https://www.technology.org/2026/05/20/figure-ai-humanoid-robots-livestream-package-sorting/ — stream start 2026-05-13; viewer naming of robots (Bob/Frank/Gary/Rose/Jim); 10-hour man-vs-machine contest (intern won 12,924 to 12,732)
- https://www.youtube.com/@figureai — "F.03 Livestream" day-by-day video series (primary livestream record)
- https://techcrunch.com/2026/05/21/hark-raises-700m-series-a-for-its-secretive-universal-ai-interface/ — Hark (Adcock's separate AI lab): $700M Series A at $6B post-money, Parkway lead
