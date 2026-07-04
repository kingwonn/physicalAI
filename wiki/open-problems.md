---
title: Open Problems & Debates
slug: open-problems
updated: 2026-07-04
confidence: verified
---
> Physical AI's core disputes as of 2026-07: whether robot learning can close a
> data gap that Ken Goldberg sizes at "100,000 years" of human experience;
> whether sim2real transfer, mature for locomotion, can ever cover contact-rich
> manipulation; whether the dexterity gap (human hands carry ~17,000
> mechanoreceptors; robot tactile sensing is far behind) dooms video-trained
> humanoids, as Rodney Brooks argues; how to get from ~99% demo success rates
> to the multiple "nines" commercial deployment requires; a safety-standards
> scramble (ISO 10218:2025 shipped, ISO 25785-1 for dynamically stable robots
> still in draft, China's HEIS 2026 framework released 2026-02); an evaluation
> crisis in [VLA models](vla-models.md) with no trusted shared benchmark; and a
> timeline discourse that runs from Elon Musk's "AGI by 2026" to Brooks's
> "pure fantasy for decades."

## 1. Data scarcity — the central bottleneck

- **The gap, quantified.** Ken Goldberg (UC Berkeley) argues in two *Science
  Robotics* papers (2025-08-27) that LLMs trained on text equivalent to
  ~100,000 years of human reading, while robotics has nothing remotely
  comparable in physical-interaction data — and robot skills likely need
  *more* data than language, not less. He calls near-term humanoid claims
  "hype … so far ahead of the robotic capabilities that researchers in the
  field are familiar with."
- **The camps.** Goldberg's companion piece (with authors from MIT, Georgia
  Tech, ETH Zürich) frames the field's central debate: *scale data* ("data is
  all we need") vs. *good old-fashioned engineering* (models, physics,
  control). Goldberg's own position is a bootstrap: engineer robots good
  enough to sell, then harvest deployment data — see [Data](data.md).
- **Which data?** Competing bets, roughly (as of 2026):

| Data source | Champions | Pro | Con |
|---|---|---|---|
| Real-robot teleoperation | Physical Intelligence, AgiBot | Ground-truth actions, force-aware | Costly, slow, narrow; scales linearly with operators |
| Egocentric human video | Tesla, Figure | Internet + wearable scale | No force/tactile channel; ~1–3 cm effective precision (Brooks) |
| Simulation / synthetic | NVIDIA (Isaac/GR00T), many labs | Infinite, cheap, safe | Sim2real gap, esp. contact & deformables — see [Simulation](simulation.md) |
| Cross-embodiment aggregation (OXE, DROID, AgiBot World) | Google DeepMind, Levine et al. | Reuses everything | Embodiment mismatch; curation beats volume |

- **Quality vs. quantity.** 2025 work ("Is Diversity All You Need for Scalable
  Robotic Manipulation?", arXiv 2507.06219) pushes back on "more is better"
  aggregation, arguing data *composition* and diversity type matter more than
  raw trajectory counts (unverified).
- **Counter-view: constraints abating.** Investor/practitioner writing in
  2025–26 argues the bottleneck is easing via scalable teleop, sim-first
  pipelines, egocentric video, and [world models](world-models.md) — this is
  the load-bearing assumption of the current funding wave (see
  [Investment](investment.md)).
- Sergey Levine (Physical Intelligence / Berkeley) argues real-world
  cross-embodiment robot data — not simulation — is the path to robotic
  foundation models; simulation is "a re-packaging of conventional model-based
  approaches" whose fidelity always eventually diverges from reality
  (CoRL 2024 talk, position maintained through 2025–26).
- **Field reporting corroborates the gap (as of 2026-07).** Stephen Witt's
  New Yorker piece ("Are Humanoid Robots Ready to Be Deployed?", 2026-07-06
  issue): there is no repository — "legal or otherwise — of motion
  trajectories for joints," and even planet-scale motion capture would take
  decades to match ChatGPT-scale training data. Data-collection bets it
  documents: Neura (Germany) has put 1,000+ industrial workers in mocap suits
  (CEO David Reger: "We're getting, like, a lot of data"); 1X retains paid
  tele-operators partly *as* a data channel ("It's also useful data for us" —
  CEO Bernt Børnich), with Børnich touting fleet-level learning ("Whatever one
  robot learns, the others all learn at the same time"; "There is definitely a
  data flywheel there") — a network effect Witt infers "may account for" 1X's
  eagerness to ship home robots early.

## 2. Sim2real limits

- **Solved-ish for locomotion.** Zero-shot sim2real via domain randomization
  is standard for [locomotion](locomotion.md) (Humanoid-Gym line of work);
  2025–26 papers extend it: PolySim (multi-simulator dynamics randomization,
  2025-10), joint-torque-space perturbation injection (2025-04), contrastive
  representations for adaptive humanoid locomotion (2025-09).
- **Open for manipulation.** Contact-rich, deformable, and tactile-dependent
  tasks remain poorly simulated; this is why the manipulation data debate
  (§1) exists at all — see [Manipulation](manipulation.md).
- **Even the fix has limits.** A 2026-06 paper, "Too Much of a Good Thing:
  When sim2real Efforts Impede Policy Learning" (arXiv 2606.02636), reports
  that excessive sim2real effort — domain randomization producing overly
  conservative policies, simulator lock-in — can itself degrade policy
  learning; the correction has its own failure mode (single paper,
  Apptronik/UT Austin).
- **Diagnosis is immature.** "Robot Policy Evaluation for Sim-to-Real
  Transfer" (arXiv 2508.11117) argues the field lacks agreed methods to even
  *measure* transfer quality, tying sim2real to the evaluation crisis (§6).

## 3. The dexterity gap

- **The biological baseline.** Human glabrous (hairless) hand skin carries
  ~17,000 low-threshold mechanoreceptors, ~1,000 at each fingertip, across
  ~15 specialized neuron families (pressure, vibration, slip, temperature).
  No robot hand approaches this (Brooks, 2025-09).
- **Brooks's core technical argument.** Every ML domain that "went
  end-to-end" (speech, vision, LLMs) first had decades of domain-specific
  input encodings (spectrograms, convolutions, tokenization). Touch has no
  equivalent preprocessing stack, so video-only training for dexterity "is
  not collecting the right data" — aimed squarely at Tesla's and Figure's
  human-video pipelines.
- **Hardware progress, still far behind.** F-TAC Hand (*Nature Machine
  Intelligence*, 2025, PKU-led) achieves 0.1 mm spatial resolution tactile
  coverage over ~70% of the hand surface via 17 vision-based tactile
  sensors; visual-tactile pretraining from
  human demos improves sample efficiency and sim2real robustness (2026
  reports). See [Hardware](hardware.md).
- **Why it matters economically.** Brooks frames dexterous manipulation as
  *the* requirement for general-purpose humanoids to pencil out; without it
  they are expensive mobile platforms doing box-moving that wheeled robots do
  more cheaply.
- **Mainstream framing (as of 2026-07).** Witt (New Yorker, 2026-07-06 issue)
  suggests the hand may be the humanoid's "missing link": the human hand performs 27
  independent motions, and "we are years away from a robot that can both tie
  its shoes and shuffle a deck of cards" — mechanical engineering (e.g. 1X's
  tendon-driven fingers, durability-tested through 2.86M cycles) is "far
  ahead of the A.I." that must drive it.

## 4. Reliability — the "nines" problem

- **Demo ≠ deployment.** Lab/benchmark success rates of 70–95% are routine in
  VLA papers; logistics and manufacturing customers treat 99% as *failure*,
  because a 1% error rate means constant human intervention and destroyed
  ROI. Multiple nines (99.9%+) are the implicit bar for unattended operation.
- **Reported deployment numbers (all company-favorable, treat with care):**
  - Figure 02 at BMW Spartanburg: 30,000+ BMW X3s supported over an 11-month
    sheet-metal-loading deployment that **ended 2025-11** (robots retired,
    not scaled up); 90,000+ parts loaded across 1,250+ operating hours with
    >99% claimed placement accuracy per shift (company-derived numbers,
    widely re-reported but not independently audited).
  - BMW Leipzig pilot: 94.3% task success on body-in-white sub-assembly over
    a 90-day evaluation (unverified, single secondary source).
  - Agility Digit: most-deployed commercial humanoid, roughly ~75 units
    globally as of 2026-06 (unverified tracker estimate); see
    [Humanoid robots](humanoid-robots.md).
  - ~3,000 humanoids in commercial settings globally as of 2026-01, with only
    ~40% of pilots reaching production within 24 months (unverified market
    research).
- **Structural issue.** Autoregressive learned policies fail unpredictably
  and non-locally; there is no accepted engineering discipline (FMEA-style)
  for certifying a learned policy's failure envelope — connects directly to
  §5 and §6.
- **Demo-vs-reality, firsthand (New Yorker, as of 2026-07).** Stephen Witt's
  reported piece ("Are Humanoid Robots Ready to Be Deployed?", 2026-07-06
  issue): 1X's fluid Neo kitchen demo turned out to be driven by a
  VR-headset tele-operator ("the robot I was seeing was a marionette"); 1X
  declined to demonstrate Neo's autonomous AI at all; 1X product head Dar
  Sleeper on falls: "To say it doesn't fall is, like, a total stretch."
  CEO Bernt Børnich is explicitly testing consumer tolerance for "robotics
  slop" (clumsily executed tasks) — 10,000+ deposits at a $20k list price
  against a 2026 home-delivery promise. The day after VC Modar Alaoui told
  Witt "locomotion is solved," an Xpeng Iron seized and fell at a Shenzhen
  mall demo and took three handlers to drag away; Unitree's Lunar New Year
  kung-fu display was a preprogrammed script (most likely mocap-derived, per
  Witt).
- **Named positions on readiness (same piece):** Aaron Ames (Caltech) —
  reliable AI for autonomous robots is years away no matter how sophisticated
  the engineering. Carolina Parada (Google DeepMind robotics head) — home
  deployment is gated on safety, not interest or capability: "The same robot
  that can land a backflip might not be able to walk up a flight of stairs."
  Deepu Talla (NVIDIA robotics) — "The world still doesn't have a ChatGPT
  equivalent for a robot" (notably more guarded than Huang's imminence
  rhetoric, §8).
- **Tele-operation as the hidden intervention layer.** The piece documents
  teleop propping up "autonomous" systems industry-wide: Waymo's professional
  remote "pilots" in the Philippines, VR tele-stocking in Japanese 7-Elevens,
  and 1X's plan to seat operators next to its AI team (Neo's earpiece rings
  change color to disclose remote control). 1X previously marketed
  tele-operation, then re-branded around AI after customer pushback — without
  abandoning teleop.

## 5. Safety & certification

- **ISO 10218-1/-2:2025** (published early 2025, first major revision since
  2011): functional safety requirements made explicit, cybersecurity
  addressed, and **ISO/TS 15066** (collaborative robot force/pressure limits)
  consolidated into the 10218 series — collaborative operation is now a set
  of *applications*, not a robot class. US adoption via ANSI/A3 R15.06-2025.
- **The humanoid gap.** All of the above assumes fixed-base or statically
  stable robots. A dynamically balancing biped is *never* passively safe —
  e-stop can mean falling. Two responses:
  - **ISO 25785-1** — safety requirements for dynamically stable
    (actively balancing) industrial mobile robots, ISO/TC 299: Working Draft
    as of 2026-01, advanced to Committee Draft with CD ballot initiated
    2026-05-12; publication expected 2026–27 (timing unverified).
  - **IEEE Humanoid Study Group report** ("A Pathway Study for Future
    Humanoid Standards", published 2025-09-25, led by Aaron Prather of
    ASTM International, 60+ contributors): a roadmap, not a standard, naming
    three gap areas — classification/taxonomy, stability metrics & fall
    response, and human-robot interaction. Estimates **18–36 months to first
    ratified humanoid standards**, and ~2027 at the earliest for safe volume
    deployment around humans.
- **China moved first at national scale.** The *Humanoid Robots & Embodied
  Intelligence Standards System (2026 Edition)*, released 2026-02-28 by
  MIIT/TC08 with 120+ participating organizations: six-part framework (basic
  commonality; brain-like & intelligent computing; limbs & components; whole
  machine; applications; safety & ethics), an initial list of 52 standards
  published, 12 national/sector standard projects underway (led/managed by
  CESI), plus the first version of the Embodied Intelligence Evaluation
  Benchmark (EIbench, released by CESI). Positions China to set de facto
  global rules — see
  [Landscape: China](landscape-china.md).
- **Brooks's practical rule:** stay ~3 m from a walking full-size humanoid;
  fall energy scales badly (double the size → 8× the mass) and ZMP-style
  balance actively pumps kinetic energy into the system.
- **Practitioner caution from the New Yorker piece (as of 2026-07):**
  Apptronik CEO Jeff Cardenas — "Around small pets, around small children,
  there's still work to be done"; Apptronik's Apollo units at Mercedes-Benz
  factories remain fenced off from human workers. Aaron Ames (Caltech) on 1X
  shipping Neo to homes in 2026: "I would worry about the legal ramifications
  when one of those robots falls on a person." The piece also relays security
  researchers Andreas Makris & Kevin Finisterre's Unitree G1 Bluetooth
  vulnerability (a self-spreading "robot botnet," 2025) and a G1 kicking a
  small child at a Chinese amusement park — attack surface and
  fall/strike risk as first-class deployment blockers.

## 6. The evaluation crisis

- **The problem.** Real-robot evaluation is slow, unscalable, unsafe, and
  unreproducible across labs; papers self-select tasks, run small-n trials
  without statistical testing, and results don't transfer between setups.
  VLAs show sharp performance drops on out-of-distribution environments,
  so in-lab numbers systematically overstate capability.
- **"10 Open Challenges" (arXiv 2511.05936, AAAI 2026)** ranks evaluation
  among the field's ten principal open problems (alongside data, safety,
  cross-robot generalization, whole-body coordination).
- **2025–26 responses:**

| Effort | Date | Approach |
|---|---|---|
| RobotArena ∞ (arXiv 2510.23571) | 2025-10 | Real-to-sim translation of videos; OOD generalization tests |
| AutoEval | 2025 | Autonomous real-world eval of generalist policies, minimal human labor |
| REALM (arXiv 2512.19562) | 2025-12 | Real-to-sim-validated generalization benchmark |
| RoboChallenge | 2025–26 | Standardized large-scale real-robot eval platform |
| VLA-REPLICA (arXiv 2605.20774) | 2026-05 | Low-cost, off-the-shelf, lab-replicable physical benchmark |
| China EIbench | 2026-02 | State-backed embodied-intelligence benchmark (§5) |

- **Statistical rigor push.** 2025–26 papers on near-optimal stopping for
  policy comparison and repeatable performance measures attack the small-n /
  no-significance-testing norm (unverified individual results). No benchmark
  yet plays the role ImageNet or MMLU played — claims of SOTA in
  [State of the art](state-of-the-art.md) should be read accordingly.

## 7. The humanoid form-factor debate

- **For the human form:** the built world is designed for human bodies
  (stairs, shelves, tools, vehicles); one general SKU amortizes R&D across
  every task; human video becomes (arguably) directly usable training data.
  Championed by Tesla, Figure, 1X, Agility, and most of the Chinese
  ecosystem — see [Humanoid robots](humanoid-robots.md).
- **Against (Brooks, 2025-09):** bipeds are intrinsically hazardous near
  people (§5); dexterity won't come from video (§3); and the economics favor
  task-shaped machines. His 15-year prediction: machines still *called*
  "humanoids" but with wheels, task-specific grippers, and non-human sensors —
  the definition will quietly shift ("goal-post moving") as the bubble
  deflates.
- **Middle positions:** Goldberg doesn't reject the form factor, only the
  timeline; Agility already ships a pragmatic semi-humanoid (Digit's leaf-
  spring legs, no five-finger hands until 2025+); several warehouse operators
  argue wheeled bases + humanoid torsos win on cost and uptime (a config
  many Chinese vendors already sell).
- The debate was the explicit backdrop of the 2025-12 Silicon Valley Humanoid
  Summit, where Brooks's essay was repeatedly invoked despite his absence
  (per AP coverage).
- **New "against" voices (New Yorker, as of 2026-07):** Mike Haley (Autodesk
  senior researcher, career in factory robotics) has "never seen a humanoid
  do anything useful in an industrial setting" — task-shaped machines
  (detached paint arms, autonomous forklifts) win on cost, moving parts, and
  maintenance: "we look back at this humanoid thing and go, 'Boy, that was
  bloody stupid.'" Skild AI co-founder Deepak Pathak (CMU) refuses to keep a
  humanoid in his own home and argues the form factor itself misleads:
  "People are using appearance as a way to misguide the public. If you make a
  robot humanlike, you expect it to have humanlike capabilities. But
  technology is far behind that." (Skild's own bet — one cross-embodiment
  brain in any body, humanoid or not — is a hedge against the form factor.)
- **Adoption attitudes split sharply by geography (as of 2026-07).** Witt
  (same piece) cites a Stanford analysis of opinion polls across ~three dozen
  countries: respondents in **China, South Korea, Thailand, and Indonesia are
  the most excited** about consumer applications of AI; **US and
  Canada respondents the least**. This matches Stanford HAI's AI Index
  public-opinion chapters: the 2025 edition (Ipsos 2024, 32 countries) has
  strong majorities in China (83%), Indonesia (80%), Thailand (77%) seeing
  AI products as more beneficial than harmful vs 40% Canada / 39% US, and
  names China, South Korea, and Indonesia as the high-excitement cluster;
  the 2026 edition (Ipsos 2025, 30 countries) repeats the pattern — China,
  Malaysia, Thailand, Indonesia >80% expecting AI to profoundly change
  their lives, US/Canada in the low-excitement/high-nervousness corner.
  Witt's exact wording is "consumer applications of A.I." — robots are the
  article's context, not the survey question. Witt's cultural gloss: Čapek-to-
  Terminator narratives taint Western perception, while Neura's CEO reports
  South Korean journalists are simply "tired of waiting." Adoption-attitude
  datapoint, not a demand forecast — but it cuts against the US-first launch
  strategy of home humanoids like NEO, and suggests East/Southeast Asia may
  be the more willing early consumer market.

## 8. Timeline discourse — who argues what

| Voice | Position (with date) |
|---|---|
| Elon Musk (Tesla) | AGI by ~2026, Optimus doing "complex tasks" end-2026; annualized Gen-3 target reportedly raised from ~50,000 to ~70,000 units (2026, supply-chain reports, unverified). Track record: every major Optimus timeline since 2022 missed; 2025 target of ~5,000 units yielded only hundreds (>90% miss, confirmed by Musk on Q2-2025 earnings call); on the Q4-2025 call (2026-01) Musk said no Optimus was yet doing useful factory work; Gen-3/V3 unveil slipped again to mid-2026 (Electrek, 2026-04). |
| Jensen Huang (NVIDIA) | "ChatGPT moment for robotics is just around the corner" (2024–25); humanoids a "$40 trillion market" (2026-05, widely reported); reportedly said "I think we've achieved AGI" on Lex Fridman, 2026-03 (unverified). |
| Brett Adcock (Figure) | Home-capable humanoids imminent; Helix as the breakthrough; Figure valued at $39B (2025-09). Skeptics question actual deployed-unit counts and demo conditions; Adcock publicly denied teleoperation in Figure home-robot testing (Bloomberg, 2026-05). |
| Rodney Brooks (MIT/iRobot) | Human-level manual skill in decades is "pure fantasy"; ≥10 years to first profitable humanoid deployment *with minimal dexterity*; predicts funding collapse and definitional goal-post shifting (2025-09). |
| Ken Goldberg (UC Berkeley) | No robot surgeons/butlers in "2, 5, or even 10 years"; 100,000-year data gap; bootstrap via engineering + deployment data (2025-08). |
| Sergey Levine (Physical Intelligence) | Optimistic on robotic foundation models but via real-world cross-embodiment data at scale, not sim or video alone; timeline contingent on data flywheel spinning up. |
| Bernt Børnich (1X) | Humanoids can "do almost anything"; Neo home deliveries in 2026 — "a promise we've gotta keep" (per product head Dar Sleeper); bets consumers will accept "robotics slop" plus disclosed teleop while fleet learning improves autonomy (New Yorker, 2026-07). |
| Aaron Ames (Caltech) | Reliable AI for autonomous robots is years away regardless of engineering sophistication; "I don't know how 1X is actually going to get away with it" — flags legal exposure of home-humanoid falls (New Yorker, 2026-07). |
| IEEE/ASTM standards community | ~2027 earliest for safe volume deployment of humanoids around humans; 18–36 months to first ratified standards (2025-09). |
| Expert surveys | Median AGI estimate moved from 50–100 years (c. 2010) to ~5–15 years by 2026 (unverified aggregation). |

- **Meta-observation:** the loudest short-timeline voices are sellers of
  robots or compute; the loudest long-timeline voices are academics with no
  P&L exposure — both have incentives. The empirical tiebreaker to watch:
  whether any humanoid deployment reaches unattended multi-nine reliability
  (§4) on a task with real labor economics before standards land (§5). See
  [Key people](key-people.md) and [Organizations](organizations.md) for who's
  who.

## Sources

- https://rodneybrooks.com/why-todays-humanoids-wont-learn-dexterity/ — Brooks essay (2025-09): mechanoreceptor counts, video-data critique, biped safety, 10+/15-year predictions, 3 m rule.
- https://techcrunch.com/2025/09/26/famed-roboticist-says-humanoid-robot-bubble-is-doomed-to-burst/ — TechCrunch coverage of Brooks essay, bubble framing, Figure $39B valuation.
- https://news.berkeley.edu/2025/08/27/are-we-truly-on-the-verge-of-the-humanoid-robot-revolution/ — Goldberg's 100,000-year data gap, Science Robotics papers (2025-08-27), data-vs-engineering debate.
- https://techxplore.com/news/2025-08-year-gap-robots-lag-ai.html — secondary coverage of Goldberg's data-gap calculation.
- https://arxiv.org/abs/2511.05936 — "10 Open Challenges Steering the Future of VLA Models" (AAAI 2026): canonical open-problems list incl. data, evaluation, safety.
- https://arxiv.org/pdf/2507.06219 — "Is Diversity All You Need for Scalable Robotic Manipulation?" — data quality-vs-quantity debate.
- https://arxiv.org/pdf/2508.17449 — imitation-learning survey: in-domain data scarcity as fundamental bottleneck.
- https://medium.com/@jianming.wang07/robotic-foundation-models-corl-2024-sergey-levines-talk-notes-e42bb3eb618e — Levine's real-world cross-embodiment data position (talk notes, secondary).
- https://arxiv.org/pdf/2404.05695 — Humanoid-Gym: zero-shot sim2real for humanoid locomotion baseline.
- https://arxiv.org/pdf/2606.02636 — "Too Much of a Good Thing": domain randomization can impede policy learning.
- https://arxiv.org/pdf/2508.11117 — robot policy evaluation for sim-to-real transfer: no agreed transfer metrics.
- https://github.com/YanjieZe/awesome-humanoid-robot-learning — index of 2025–26 sim2real papers (PolySim, torque-perturbation injection).
- https://www.nature.com/articles/s42256-025-01053-3 — F-TAC Hand: high-resolution tactile coverage (Nature Machine Intelligence 2025).
- https://arxiv.org/html/2507.11840v1 — dexterous/embodied manipulation survey: dexterity-gap framing, teleop force-feedback limits.
- https://www.automate.org/robotics/news/updated-iso-10218-major-advancements-in-industrial-robot-safety-standards-now-available — A3 announcement of ISO 10218:2025; TS 15066 consolidation.
- https://www.wideautomation.com/en/robotic-safety-what-changes-with-the-new-iso-102182025-standards/ — ISO 10218:2025 entry into force and changes.
- https://www.therobotreport.com/ieee-study-group-publishes-framework-for-humanoid-standards/ — IEEE humanoid standards framework: Prather, 60+ contributors, 18–36 months, ~2027.
- https://spectrum.ieee.org/domestic-humanoid-robot-safety-standards — IEEE Spectrum on domestic humanoid safety standards shift.
- https://theresarobotforthat.com/blog/humanoid-robot-safety-standards-2026/ — ISO 25785-1 working-draft status, ANSI/A3 R15.06-2025 (secondary).
- https://sesec.eu/2026/04/01/chinas-first-standards-system-for-humanoid-robots-and-embodied-intelligence/ — China HEIS 2026 standards system details.
- https://govt.chinadaily.com.cn/s/202603/02/WS69a5171c498e23165e06dc3c/china-introduces-a-standard-framework-for-humanoid-and-embodied-intelligence.html — official Chinese coverage: 2026-02-28 release, six parts, MIIT/TC08, EIbench.
- https://arxiv.org/html/2510.23571v1 — RobotArena ∞: real-to-sim VLA benchmarking, OOD generalization drops.
- https://arxiv.org/pdf/2605.20774 — VLA-REPLICA: low-cost reproducible real-world VLA benchmark (2026-05).
- https://arxiv.org/pdf/2512.19562 — REALM real-to-sim validated manipulation generalization benchmark.
- https://abcnews.go.com/Technology/wireStory/humanoid-robots-center-stage-silicon-valley-summit-skepticism-128353889 — AP on 2025-12 Humanoid Summit; Brooks essay's field-wide resonance.
- https://www.iiot-world.com/artificial-intelligence-ml/robotics/physical-ai-deployment-roi-humanoid-robots/ — BMW/Figure 30K-car and 99%-accuracy claims (secondary, company-derived).
- https://www.figure.ai/news/production-at-bmw — Figure primary post: 30,000+ X3s, 90,000+ parts, 1,250+ hours, >99% per-shift placement accuracy.
- https://www.repairerdrivennews.com/2025/11/25/humanoid-robots-complete-11-month-project-at-bmw-plant/ — BMW Spartanburg deployment concluded after 11 months (2025-11); robots retired.
- https://www.iso.org/standard/91469.html — ISO/CD 25785-1 catalog entry: Committee Draft stage (30.20 CD ballot, 2026-05).
- https://www.automate.org/robotics/news/new-ansi-a3-r15-06-2025-american-national-standard-for-industrial-robot-safety-now-available-for-purchase — ANSI/A3 R15.06-2025 Parts 1–2 as US adoption of ISO 10218:2025; Part 3 US-developed.
- https://electrek.co/2026/04/22/tesla-optimus-production-fremont-model-sx-line/ — Optimus V3 reveal slipped again to mid-2026; Fremont line conversion.
- https://finance.biggo.com/news/e77c6e9b-d703-45fc-906d-1ea3d1272482 — reported ~50K→70K annualized Optimus Gen-3 target (supply-chain reporting, unverified).
- https://axis-intelligence.com/humanoid-robots-deployment-2026-case-studies/ — ~3,000 humanoids in commercial settings 2026-01; pilot-to-production rates (unverified market research).
- https://finance.yahoo.com/markets/stocks/articles/why-teslas-optimus-story-more-153200371.html — Optimus missed-targets accounting (secondary).
- https://www.bloomberg.com/news/videos/2026-05-15/figure-ceo-says-humanoid-robot-test-had-no-outside-aid-video — Adcock denies teleoperation in Figure home tests.
- https://247wallst.com/investing/2026/05/31/jensen-huang-just-called-humanoid-robots-a-40-trillion-market-heres-why-wall-street-is-loading-up-on-physical-ai-stocks/ — Huang $40T market claim (2026-05, secondary).
- https://www.newyorker.com/magazine/2026/07/06/are-humanoid-robots-ready-to-be-deployed — Stephen Witt, "Are Humanoid Robots Ready to Be Deployed?" (2026-07-06 issue): 1X Neo teleop demo & "robotics slop", Ames/Parada/Talla/Cardenas/Pathak/Haley positions, Xpeng Iron fall, Neura mocap program, teleop economy, Stanford cross-country attitude survey (paywalled; read in full via Wayback snapshot 2026-07-03).
- https://hai.stanford.edu/ai-index/2025-ai-index-report/public-opinion — Stanford HAI AI Index 2025 public-opinion chapter (Ipsos 2024, 32 countries): source of the China 83% / Indonesia 80% / Thailand 77% vs Canada 40% / US 39% benefit-vs-harm split and the China/South Korea/Indonesia high-excitement cluster behind Witt's claim.
- https://hai.stanford.edu/ai-index/2026-ai-index-report/public-opinion — Stanford HAI AI Index 2026 public-opinion chapter (Ipsos 2025, 30 countries): same pattern persists (China/Malaysia/Thailand/Indonesia >80% optimism; US/Canada lowest excitement, highest nervousness).
