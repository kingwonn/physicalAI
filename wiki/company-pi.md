---
title: "Company Deep Dive: Physical Intelligence"
slug: company-pi
updated: 2026-07-04
confidence: verified
---
> Physical Intelligence ("PI", stylized π; San Francisco) is the flagship of the "robot brain, no robot body" thesis: a ~80-person lab founded in 2024-03 by the core of Google's robotics diaspora (Karol Hausman, Sergey Levine, Chelsea Finn, Brian Ichter, Quan Vuong) plus Stripe-veteran investor Lachy Groom, building embodiment-agnostic foundation models — π0 (2024-10, flow matching) → π0.5 (2025-04, open-world generalization) → π*0.6 (2025-11, RECAP RL from experience) → π0.7 (2026-04, steerable generalist with world-model visual subgoals). It open-sourced π0/π0.5 (openpi, 12.6k GitHub stars), keeps its frontier models closed, and has raised ~$1.07B ($600M at $5.6B, 2025-11, CapitalG-led); a reported ~$1B round at >$11B has **not** been confirmed closed as of 2026-07-04. It is deliberately pre-revenue — Groom refuses to give investors commercialization answers — making PI the purest research bet among frontier Physical AI labs. Context: [VLA models](vla-models.md), [Landscape: USA](landscape-usa.md), [Investment](investment.md), [Key people](key-people.md).

## Founding and thesis

- **Announced 2024-03** (seed dated 2024-03-12; some profiles date incorporation to late 2023). Lachy Groom — early Stripe employee, angel in Figma/Notion/Ramp — spent "five years looking for the company to start post-Stripe," tracked down Levine and Finn via their academic work, then Hausman; "one of those meetings where you walk out and it's like, *This is it*."
- **Co-founders** (lists vary slightly by source): **Karol Hausman** (CEO; led Google Brain's robot-manipulation moonshot — SayCan/RT era), **Sergey Levine** (UC Berkeley RAIL; deep RL canon — SAC, offline RL, Open X-Embodiment), **Chelsea Finn** (Stanford IRIS; MAML, ALOHA/Mobile ALOHA, DROID), **Brian Ichter** (ex-Google Brain), **Lachy Groom** (operations/fundraising/GTM), **Quan Vuong** (ex-Google DeepMind), **Adnan Esmail** (ex-Anduril SVP Engineering, ex-Tesla), plus **Jasmine Hsu** per some accounts (unverified — absent from most rosters, incl. the 2026-01 TechCrunch profile). Levine and Finn keep their faculty posts (see [Key people](key-people.md)).
- **The thesis**: one generalist "robot brain" — Levine: "Think of it like ChatGPT, but for robots" — trained across many cheap, heterogeneous robot bodies, so intelligence transfers to any new platform. Vuong: "The marginal cost of onboarding autonomy to a new robot platform... is just a lot lower." PI builds **no hardware of its own** and treats bodies as commodities (its lab arms cost ~$3,500; Levine estimates <$1,000 BOM if made in-house).
- Explicit anti-humanoid-hype positioning: rather than one expensive humanoid, train across single arms, bimanual rigs, and mobile manipulators — betting cross-embodiment data breadth beats vertical integration ([Figure](company-figure.md) is the opposing bet).

## Team and talent density

- **~80 employees as of 2026-01** (TechCrunch profile) — roughly 1/10th the headcount-per-valuation of typical hardware peers; Groom wants to grow "as slowly as possible"; most spend is compute, not payroll.
- Arguably the densest robot-learning author cluster anywhere: the π0.7 paper lists ~90 authors including Danny Driess; the founding group co-authored much of the field's canon (RT-1/RT-2, SayCan, Open X-Embodiment, ALOHA, DROID).
- Groom claims the founding 5–10-year research roadmap was completed within ~18 months (company claim, unverified).
- HQ San Francisco, with an in-office test kitchen (espresso machine, laundry stations) used for both data collection and evaluation.

## Funding arc (as of 2026-07)

| Round | Date | Amount | Valuation (post) | Lead / notable investors |
|---|---|---|---|---|
| Seed | 2024-03 | $70M | ~$400M (reported) | Thrive Capital; Khosla, Lux, Sequoia, OpenAI |
| Series A | 2024-11 | $400M | $2.4B | Jeff Bezos, OpenAI, Thrive, Lux, Bond |
| Series B | 2025-11 | $600M | $5.6B | CapitalG (Alphabet); Bezos, Thrive, Lux, Index, Emergence, T. Rowe Price |
| Reported next round | first reported 2026-03-27 | ~$1B | >$11B | Founders Fund "set to participate," Lightspeed in talks (Bloomberg) |

- **Watch item — checked 2026-07-04: the ~$1B at >$11B round has NOT been announced as closed.** All reporting still traces to Bloomberg's 2026-03-27 "in talks" story; no primary confirmation from PI or investors since. If closed, it would double the valuation in ~4 months and take total raised to ~$2.1B. Treat the $11B mark as (unverified) until announced.
- Total confirmed raised: **~$1.07B** across three rounds. Note the investor pattern: OpenAI invested at seed and Series A; Alphabet's growth fund led the B — both big AI labs hold stakes in the leading independent robot-brain lab (see [Investment](investment.md) for sector context and repricing-velocity concerns).
- No disclosed revenue against any of these marks (see skeptic case below).

## Model lineage: π0 → π0.7

Full architectural detail and cross-lab comparison live in [VLA models](vla-models.md); this table adds company-trajectory context.

| Model | Date | Core advance | Weights |
|---|---|---|---|
| π0 | 2024-10 | First generalist policy: PaliGemma-3B VLM + 300M action expert, flow matching, 50 Hz chunks; ~10k h teleop across 7–8 embodiments | open 2025-02 (Apache-2.0) |
| π0-FAST | 2025-01 | FAST action tokenizer (DCT + BPE): ~5x cheaper training vs diffusion/flow decoding (company claim) | open |
| π0.5 | 2025-04-22 | Open-world generalization — cleans never-seen homes; hierarchical subtask-then-action inference; ~100-environment scaling study | open 2025-09 |
| π*0.6 | 2025-11-17 | RECAP ("RL with Experience & Corrections via Advantage-conditioned Policies"): demos → teleop corrections → advantage-conditioned RL from autonomous experience; 5B VLM + action expert; >90% success on espresso/laundry/box tasks, ~2x throughput | closed |
| π0.7 | 2026-04-16 | "Steerable generalist with emergent capabilities" (arXiv:2604.15483): one checkpoint matches RL-tuned π*0.6 specialists (0.9–2.0x throughput ratios); prompted via language coaching, speed/quality metadata, control-modality labels, and **visual subgoals generated at test time by a lightweight world model** | closed |

- The lineage tells a strategy: 2024 = prove the architecture (flow-matching VLA); 2025 = prove generalization (π0.5) then reliability (π*0.6 RL); 2026 = prove one model can do it all, steerably (π0.7). Frontier models went closed exactly when they became commercially relevant.
- π0.7's world-model subgoal mechanism ("images that show what the end of the current sub-step should look like... generated at test time by a world model") makes PI part of the 2026 VLA/world-model convergence alongside NVIDIA's DreamZero — see [World models](world-models.md).
- Levine's scaling claim for π0.7: once the model crosses into skill-remixing, "the capabilities are up more than linearly with the amount of data" — the field's clearest "GPT-3 moment" framing to date (company-affiliated claim; PI itself hedges with "early signs" language in the paper).
- Supporting research cadence between releases: FAST+ universal tokenizer (1M trajectories), knowledge-insulation training (π0.5 release), real-time action chunking, Hi Robot hierarchical instruction-following (2025) and multi-scale embodied memory for 10+ minute tasks (2026-03) (last two per company research pages, unverified detail).

## Open source: openpi and ecosystem impact

- **openpi** (github.com/Physical-Intelligence/openpi, Apache-2.0, **12.6k stars as of 2026-07**): ships π0 and π0-FAST base checkpoints (2025-02) and π0.5 (2025-09, with PyTorch support), plus fine-tuned variants — π0-DROID / π0-FAST-DROID (Franka), π0-ALOHA (towel folding, tupperware, pen uncapping), π0.5-LIBERO, π0.5-DROID. Docs support DROID, ALOHA, LIBERO, UR5.
- Hugging Face **LeRobot** integrated π0 (2025) and π0.5 as first-class policies — making π models the default "serious" open VLA for academics and hobbyists alongside SmolVLA and GR00T ([Data](data.md), [VLA models](vla-models.md)).
- Ecosystem effect: π0's flow-matching action-expert design became the de facto template for new VLAs in 2025–26 (SmolVLA and many Chinese models copy it), and openpi checkpoints are standard baselines in VLA papers (e.g., GM-100, LingBot-VLA comparisons).
- The open/closed line is strategic: **π*0.6 and π0.7 remain closed as of 2026-07** (open request tracked in openpi issue #789). PI open-sources ~12–18-month-old models to seed the ecosystem while withholding deployment-grade ones — mirroring the pattern of US frontier labs described in [VLA models](vla-models.md).

## Demos and what they prove

| Demo | Model / date | What it proves (and doesn't) |
|---|---|---|
| Laundry folding, table bussing, box building | π0, 2024-10 | Multi-minute dexterous manipulation of deformables — historically a robotics nightmare — is tractable for a flow-matching VLA. Doesn't prove generalization beyond training scenes. |
| Cleaning kitchens/bedrooms in never-seen homes | π0.5, 2025-04 | Open-world generalization; scaling study shows ~100 training environments approach in-domain performance. Success rates well below product-grade. |
| **18-hour espresso marathon** (5:30am–11:30pm continuous), 50 novel laundry items in a new home, 59 factory boxes assembled/labeled | π*0.6, 2025-11 | The commercially decisive axis: reliability and throughput over marathon durations, not one-shot success. RL from autonomous experience (RECAP) roughly doubled throughput and cut failures ~2x (company-reported). |
| Air-fryer sweet potato: operates a never-seen appliance from 2 fragmented training episodes + web knowledge; new tasks via step-by-step language coaching; zero-shot laundry folding on an untrained bimanual UR5e | π0.7, 2026-04 | Compositional generalization and embodiment-agnosticism — the core thesis claims. All benchmarked against PI's *own* prior models; no standardized external benchmark exists (company acknowledges). |
| Live press demo failure: robot folds curated T-shirts fine, fails on guest-supplied shirt, down vest, sweater | Washington Post visit, published 2026-06-08 | The gap between curated demo distribution and the real world remains; PI's own showcase task is not robust to adversarial garments. |

- Pattern to note: PI's demo genre shifted from "can it do X at all" (2024) to "can it do X all day" (2025) to "can it do X it was never taught" (2026) — tracking exactly what each funding round needed to believe.
- Company-reported numbers throughout; no third-party audits (see [Evaluation](evaluation.md)).

## Embodiments and partnerships

- **Training embodiments** (π0 paper: 8 distinct robots): single and bimanual UR5e, Franka, bimanual Trossen (ALOHA-class), bimanual ARX, bimanual AgileX, and mobile manipulators — deliberately cheap, mostly commodity arms rather than humanoids.
- **Evaluation embodiments** (π0.7): mobile manipulator, bimanual UR5e with Robotiq grippers, Franka (via DROID). Fine-tuned checkpoints target DROID/Franka and ALOHA platforms.
- **No humanoid partnership announced** as of 2026-07 — conspicuous given the thesis; PI models run on arms and mobile bases, while humanoid makers (Figure, Tesla, 1X) build in-house brains (unverified whether private humanoid evaluations exist).
- **Data partnerships**: named client of Scale AI's Physical AI Data Engine (100k+ production hours logged; see [Data](data.md)).
- **Testing partners** (per TechCrunch, 2026-01): unnamed companies in logistics, grocery, and chocolate manufacturing — pilots generating no revenue. Earlier π*0.6 materials show factory box-assembly and espresso-bar settings consistent with such pilots.
- Investor-strategic web: OpenAI (seed + A), Alphabet/CapitalG (B lead), Bezos (A + B) — PI is wired into every major AI-capital bloc except NVIDIA's ([Organizations](organizations.md)).

## Business model: the deliberate void

- PI is **pre-revenue by choice** (as of 2026-01, per the TechCrunch profile: no revenue, product, pricing, or paying customer disclosed; partnerships framed as tests, not commercial deployments): Groom — "I don't give investors answers on commercialization. That's sort of a weird thing, that people tolerate that." Spending goes overwhelmingly to compute; Groom: "There's no limit to how much money we can really put to work."
- Implied end-state: license the brain to a fragmented robot-hardware universe — the "Android layer" position — via model licensing/API rather than robot sales. Third-party analyses sketch subscription/per-device licensing tiers, but **PI has announced no pricing, no product, and no named paying customer** (as of 2026-07).
- Sharpest contrast in the sector: **Skild AI** (the other US robot-brain lab, $14B+ valuation) claims ~$30M 2025 revenue from security/warehouse/manufacturing deployments (per TechCrunch; company claim); PI, at $5.6B (or a reported $11B), claims $0 and calls that discipline. [Figure](company-figure.md) monetizes hardware+brain vertically. Three incompatible theses, all funded at multi-billion marks — see [Landscape: USA](landscape-usa.md).
- Bull read: avoiding premature productization preserved focus that produced π0.5→π0.7 in 24 months, and openpi seeded the ecosystem that may standardize on π interfaces. Bear read: below.

## Skeptic case

- **Valuation with zero revenue**: $5.6B closed / $11B reported against $0 disclosed revenue; the reported round would be a ~2x repricing in ~4 months — velocity resembling 2021-style momentum rounds ([Investment](investment.md) bubble-watch).
- **Self-referential evaluation**: every headline claim (18-h espresso, >90% success, specialist-matching) is benchmarked against PI's own earlier models on PI-chosen tasks; the company itself acknowledges no standardized robotics benchmarks exist. No RoboArena/GM-100-style third-party numbers for π*0.6/π0.7 as of 2026-07.
- **Demo fragility**: WaPo's 2026-06 live test — failure on a guest's vest and sweater — shows the flagship task still breaks just outside the curated distribution; Rodney Brooks's broader critique (video-trained dexterity as "pure fantasy thinking") applies squarely.
- **Embodiment-agnostic ≠ embodiment-proven**: π runs on cheap arms in labs and pilots; no announced humanoid, no announced fleet, no announced OEM design win. The licensing thesis is untested against hardware makers' strong incentive to own their brains (Figure fired OpenAI over exactly this).
- **Open-source generosity has limits**: the models that matter commercially (π*0.6, π0.7) are closed; the openness that built PI's reputation lags the frontier by ~a year and could narrow further under monetization pressure.
- **Key-person concentration**: the bet is inseparable from a handful of dual-hat academics (Levine, Finn) and Hausman; competitors (Skild, NVIDIA GEAR, DeepMind) recruit from the same thin pool ([Key people](key-people.md)).
- Steel-man: PI's papers are unusually detailed and reproducible (openpi lets outsiders verify the architecture claims), its 2024→2026 capability slope is real and externally visible in open checkpoints, and it has repeatedly shipped the technique the rest of the field copies a quarter later (flow-matching action expert, FAST, RL-from-experience, steerability).

## Sources

- https://www.pi.website/ — company site: model timeline (π0 → π0.7), investor list, research posts
- https://x.com/svlevine/status/1767636367717310708 — Levine's founding announcement (2024-03)
- https://www.crunchbase.com/funding_round/physical-intelligence-834b-seed--0936ae55 — seed round dated 2024-03-12
- https://www.maginative.com/article/physical-intelligence-raises-70m-to-build-ai-powered-robots-for-any-application/ — $70M seed, ~$400M valuation, Thrive/Khosla/Lux/Sequoia/OpenAI
- https://www.cnbc.com/2024/11/04/jeff-bezos-and-openai-invest-in-robot-startup-physical-intelligence.html — $400M Series A at $2.4B (2024-11), Bezos/OpenAI/Thrive/Lux/Bond
- https://www.bloomberg.com/news/articles/2025-11-20/robotics-startup-physical-intelligence-valued-at-5-6-billion-in-new-funding — $600M at $5.6B, CapitalG lead (2025-11)
- https://www.therobotreport.com/physical-intelligence-raises-600m-advance-robot-foundation-models/ — Series B corroboration, investor list
- https://www.bloomberg.com/news/articles/2026-03-27/ex-deepmind-staffers-robotics-startup-in-talks-for-11-billion-valuation — ~$1B at >$11B "in talks" (2026-03-27); Founders Fund, Lightspeed
- https://techcrunch.com/2026/03/27/physical-intelligence-is-reportedly-in-talks-to-raise-1-billion-again/ — corroboration that the $11B round was unclosed talks as of reporting
- https://techcrunch.com/2026/01/30/physical-intelligence-stripe-veteran-lachy-grooms-latest-bet-is-building-silicon-valleys-buzziest-robot-brains/ — inside profile: ~80 employees, Groom's no-commercialization stance, $3,500 arms, test partners (logistics/grocery/chocolate), co-founder roster incl. Quan Vuong, Skild contrast
- https://www.pi.website/blog/pi0 — π0 announcement (2024-10-31): architecture (3B VLM, flow matching, 50 Hz), 8 distinct robots, laundry/bussing/box demos (hours not stated in post)
- https://www.pi.website/research/fast — FAST tokenizer, ~5x training-cost claim, FAST+ universal tokenizer
- https://www.pi.website/blog/pi05 — π0.5 (2025-04-22): unseen-home cleaning, ~100-environment scaling study, training mixture
- https://www.pi.website/blog/pistar06 — π*0.6 + RECAP (2025-11-17): espresso 5:30am–11:30pm (18 h), >90% success on all three tasks, ~2x throughput
- https://arxiv.org/abs/2511.14759 — π*0.6 paper ("a VLA That Learns From Experience")
- https://website.pi-asset.com/pi06star/PI06_model_card.pdf — π0.6 model card: 5B VLM + action expert
- https://www.pi.website/blog/pi07 — π0.7 (2026-04-16): steerability inputs, world-model-generated visual subgoals, 0.9–2.0x specialist throughput ratios, UR5e/Robotiq and mobile-manipulator evals
- https://arxiv.org/abs/2604.15483 — π0.7 paper ("a Steerable Generalist Robotic Foundation Model with Emergent Capabilities"), ~90 authors
- https://techcrunch.com/2026/04/16/physical-intelligence-a-hot-robotics-startup-says-its-new-robot-brain-can-figure-out-tasks-it-was-never-taught/ — π0.7 coverage: Levine "more than linearly" quote, air-fryer example, admission that standardized benchmarks don't exist
- https://www.humanoidsdaily.com/news/physical-intelligence-unveils-0-7-the-rise-of-compositional-generalization-in-robotics — independent π0.7 coverage: compositional generalization, two-episode air-fryer detail
- https://github.com/Physical-Intelligence/openpi — openpi repo: 12.6k stars, Apache-2.0, checkpoint list (π0/π0-FAST/π0.5 + DROID/ALOHA/LIBERO variants), PyTorch support 2025-09; π0.6/π0.7 absent
- https://www.therobotreport.com/physical-intelligence-open-sources-pi0-robotics-foundation-model/ — π0 open-sourcing (2025-02)
- https://huggingface.co/blog/pi0 — π0/π0-FAST integration into Hugging Face LeRobot; corroborates 10k+ h pre-training data figure
- https://huggingface.co/docs/lerobot/pi05 — π0.5 as a LeRobot policy (ecosystem adoption)
- https://www.washingtonpost.com/opinions/interactive/2026/06/08/this-ai-robot-promises-fold-your-laundry-would-you-buy-it/ — live demo: curated T-shirts fold, guest garments fail; "selling a promise" framing (skeptic anchor)
- https://arxiv.org/html/2410.24164v1 — π0 paper: 8 distinct robots (UR5e, Franka, Trossen, ARX, AgileX; single/bimanual/mobile configs)
