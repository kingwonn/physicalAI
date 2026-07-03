---
title: Vision-Language-Action Models
slug: vla-models
updated: 2026-07-03
confidence: verified
---
> Vision-language-action (VLA) models are multimodal neural networks that take camera images and a natural-language instruction and directly output low-level robot actions, making them the leading candidate architecture for a "general-purpose robot brain." The lineage runs from Google's RT-1 (2022) and RT-2 (2023, which coined the term) through open academic models (Octo, OpenVLA, 2024) to production-grade systems: Physical Intelligence's π0/π0.5/π*0.6/π0.7, NVIDIA's Isaac GR00T N series, Google DeepMind's Gemini Robotics family, and Figure's Helix/Helix 02. As of mid-2026 the field has converged on a common recipe — a pretrained vision-language model backbone plus a fast action-decoding head (flow matching, diffusion, or compressed action tokens) — while frontier work shifts toward reinforcement learning from deployment experience (π*0.6/RECAP), agentic "thinking" VLAs (Gemini Robotics 1.5, GR00T N1.7), and world-action models (GR00T N2/DreamZero).

## What a VLA is

- A VLA is a single foundation model mapping (images + language instruction + robot state) → action commands (joint targets, end-effector poses, gripper commands), typically emitted as short "action chunks" of 8–50 future steps at 3–200 Hz depending on the design.
- The key bet: internet-scale vision-language pretraining transfers semantic knowledge (objects, spatial relations, common sense) to robot control, so robots generalize beyond their demonstration data.
- Term "vision-language-action model" was introduced with Google DeepMind's RT-2 (July 2023), which showed a VLM fine-tuned to output actions as text tokens inherits web knowledge (e.g., "pick up the extinct animal" → grabs toy dinosaur).
- VLAs are the "policy" layer of the physical-AI stack; they increasingly sit under a reasoning/orchestration layer (see Gemini Robotics-ER, Figure's System 2) and are trained with data from real teleoperation, simulation, and human video — see [Data](data.md) and [Simulation](simulation.md).

## Lineage and key models

| Model | Org | Date | Params | Backbone | Action decoding | Weights |
|---|---|---|---|---|---|---|
| RT-1 | Google | 2022-12 | 35M | EfficientNet + Transformer | discrete token bins, 3 Hz | open (code) |
| RT-2 | Google DeepMind | 2023-07 | 12B / 55B | PaLM-E / PaLI-X | actions as text tokens | closed |
| RT-2-X / Open X-Embodiment | 21+ labs | 2023-10 | 55B | PaLI-X | discrete tokens | dataset open |
| Octo | UC Berkeley et al. | 2024-05 | 27M / 93M | custom transformer | diffusion head | open (Apache-2.0) |
| OpenVLA | Stanford/Berkeley et al. | 2024-06 | 7B | Prismatic (Llama-2-7B + DINOv2 + SigLIP) | discrete token bins | open (MIT) |
| RDT-1B | Tsinghua | 2024-10 | 1.2B | custom | diffusion transformer (bimanual) | open |
| π0 | Physical Intelligence | 2024-10 | ~3.3B | PaliGemma 3B + 300M action expert | flow matching, 50 Hz chunks | open (2025-02, Apache-2.0) |
| π0-FAST | Physical Intelligence | 2025-01 | ~3B | π0 arch | autoregressive FAST tokens | open |
| Helix | Figure | 2025-02 | 7B (S2) + 80M (S1) | open-source VLM (S2) | latent-conditioned 200 Hz visuomotor policy | closed |
| GR00T N1 | NVIDIA | 2025-03 | ~2B | Eagle-2 VLM | diffusion-transformer (flow-matching) head | open weights |
| Gemini Robotics | Google DeepMind | 2025-03 | n/a | Gemini 2.0 | continuous actions (details closed) | closed |
| π0.5 | Physical Intelligence | 2025-04 | ~3.3B | π0 arch + co-training | hierarchical: subtask tokens → flow matching | open (2025-09) |
| GR00T N1.5 | NVIDIA | 2025-05 | ~3B | Eagle 2.5 (frozen VLM) + FLARE | flow-matching DiT head | open weights |
| SmolVLA | Hugging Face | 2025-06 | 450M | SmolVLM-2 | flow matching | open |
| Gemini Robotics On-Device | Google DeepMind | 2025-06 | n/a (runs on-robot) | Gemini Robotics distill | continuous actions | closed, fine-tunable via SDK |
| WALL-OSS | X Square Robot (CN) | 2025-09 | 4B | 3B VLM | hybrid | open |
| Gemini Robotics 1.5 / ER 1.5 | Google DeepMind | 2025-09 | n/a | Gemini | "thinking" VLA + reasoning orchestrator | closed (ER 1.5 via API) |
| π0.6 / π*0.6 | Physical Intelligence | 2025-11 | 5B + action expert | upgraded π0.5 | flow matching + RECAP RL (advantage conditioning) | closed as of 2026-07 |
| GR00T N1.6 | NVIDIA | announced 2025-09 (CoRL), shipped 2026-01 (CES) | ~3B | Cosmos Reason | flow-matching DiT head, full-body control | open weights |
| Helix 02 | Figure | 2026-01 | S0 10M + S1 + S2 | Helix arch + 1 kHz reflex layer | 3-tier hierarchy | closed |
| UnifoLM-VLA-0 | Unitree (CN) | 2026-01 | n/a | — | — | open |
| LingBot-VLA | Ant Group / Robbyant (CN) | paper + weights 2026-01 | n/a | — | — | open |
| π0.7 | Physical Intelligence | 2026-04 | n/a | π0.6 lineage | steerable generalist: prompts via language coaching, metadata, visual subgoals | closed as of 2026-07 |
| GR00T N1.7 | NVIDIA | 2026-04 (early access) | 3B | Cosmos-Reason2-2B (Qwen3-VL arch) | 32-layer diffusion-transformer head | open weights (NVIDIA Open Model License) |
| GR00T N2 | NVIDIA | previewed 2026-03, ships late 2026 | n/a | DreamZero world-action model | world-model-based | announced open |

## Action decoding: the central design axis

- **Discrete binned tokens** (RT-1, RT-2, OpenVLA): each action dimension quantized into ~256 bins, predicted autoregressively. Simple, reuses the LM head, but slow (OpenVLA ran 3–5 Hz on an RTX 4090) and poorly suited to high-frequency dexterous control.
- **Compressed action tokens — FAST** (π0-FAST, 2025-01): DCT + byte-pair-encoding "Frequency-space Action Sequence Tokenization" compresses 50 Hz action chunks into short token sequences; Physical Intelligence reports up to ~5x cheaper training than diffusion/flow decoding at similar quality; FAST+ is a universal tokenizer trained on 1M real trajectories.
- **Diffusion heads** (Octo, RDT-1B, GR00T N series): a diffusion transformer denoises continuous action chunks conditioned on VLM embeddings; handles multimodal action distributions.
- **Flow matching** (π0, π0.5, SmolVLA): continuous-time variant of diffusion; π0's 300M-parameter "action expert" generates 50 Hz action chunks, a design widely copied in 2025–26 and the current default for new models.
- **Plain regression** (OpenVLA-OFT, 2025): parallel decoding + action chunking + L1 regression gave ~26x higher action-generation throughput than autoregressive OpenVLA and ~97.1% average success on LIBERO (up from 76.5%) — evidence that decoding recipe matters as much as scale.
- **Dual-system latent conditioning** (Helix; GR00T N1 is also explicitly dual-system): a slow VLM (7–9 Hz) emits a latent goal vector consumed by a small fast policy (200 Hz) — trades end-to-end purity for reactivity. Helix 02 extends this to three tiers with a 1 kHz reflex layer.
- **Hierarchical text-then-action** (π0.5, Gemini Robotics 1.5, GR00T N1.7): the same model first predicts a high-level subtask in text ("pick up the pillow"), then decodes motor actions — "thinking before acting."
- **World-action models** (GR00T N2/DreamZero, 2026): jointly predict future video and actions rather than bolting an action head onto a VLM — the VLA and [world model](world-models.md) research threads are merging.

## Physical Intelligence (π series)

- **π0** (2024-10): PaliGemma-3B VLM + 300M action expert, flow matching, trained on ~10k hours of teleop across 7–8 robot embodiments (single-arm, bimanual, mobile). Demonstrated laundry folding, table bussing, box building. Weights + code open-sourced 2025-02 in `openpi` (Apache-2.0).
- **π0.5** (2025-04-22): targets open-world generalization — cleaned kitchens and bedrooms in homes never seen in training. Co-trained on web multimodal data, verbal instructions, subtask annotations, cross-embodiment robot data; hierarchical inference (discrete autoregressive subtask reasoning in FAST tokens + flow-matching motor control). Scaling study: performance approached in-environment-trained baselines after ~100 distinct training environments. Weights released 2025-09 (with "knowledge insulation" training and PyTorch support); checkpoints include π0.5-base, π0.5-DROID, π0.5-LIBERO.
- **π*0.6 + RECAP** (2025-11-17): π0.6 is a 5B-param VLM augmented with an action expert (per model card). RECAP = "RL with Experience & Corrections via Advantage-conditioned Policies": three stages — demonstrations → real-time teleop corrections ("coaching") → advantage-conditioned RL from autonomous experience with a learned value function that assigns credit for downstream success. Reported results (as of 2025-11, company-reported): espresso making ~40%→~90%+ success and roughly doubled throughput; box assembly ~60%→~95%+; ran an espresso station autonomously for ~18 hours, folded 50 novel laundry items in a new home, assembled and labeled 59 factory boxes. π*0.6 weights not released as of 2026-07 (open request tracked in openpi issue #789; openpi still ships only π0/π0-FAST/π0.5).
- **π0.7** (announced 2026-04-16): "steerable" generalist — company reports a single checkpoint matching fine-tuned specialists across diverse dexterous tasks, compositional generalization (recombining learned skills for novel problems), executing unseen tasks via step-by-step language coaching, and prompting through metadata (speed/quality), visual subgoals and control specifications; demonstrated laundry folding on a bimanual UR5e with no training data for that platform (company-reported). Weights not released as of 2026-07.
- Funding: raised **$600M at a $5.6B valuation in 2025-11**, led by Alphabet's CapitalG with Jeff Bezos, Thrive, Lux, Index, Emergence and T. Rowe Price participating; ~$1.1B raised in total as of 2025-11 (prior round: $400M at $2.4B, 2024-11, investors incl. Jeff Bezos, OpenAI, Thrive, Lux, Bond). In 2026-03 Bloomberg reported the company in talks to raise ~$1B more at a valuation above $11B (Founders Fund, Lightspeed in talks; deal not confirmed closed as of 2026-07). See [Investment](investment.md) and [Key people](key-people.md) (Hausman, Levine, Finn).

## NVIDIA Isaac GR00T N series

- **N1** (2025-03, GTC): billed by NVIDIA as the first open foundation model for generalist humanoid robots. ~2B params; dual-system design — Eagle-2 VLM (System 2) + diffusion-transformer action head (System 1); trained on a "data pyramid" of real teleop, synthetic data (Omniverse/Cosmos, GR00T-Dreams), and human video. Validated on Fourier GR-1 and 1X NEO among others.
- **N1.5** (2025-05): frozen, upgraded Eagle 2.5 VLM for better grounding; adds FLARE (Future LAtent Representation Alignment) enabling learning from human videos; NVIDIA says the DreamGen/GR00T-Dreams synthetic pipeline compressed ~3 months of manual data collection into 36 hours (company claim). Targets Jetson Thor onboard compute ([Hardware](hardware.md)).
- **N1.6** (announced CoRL 2025-09-29, shipped around CES 2026-01-05): integrates **Cosmos Reason** as the reasoning-VLM "deep-thinking brain"; extends to full-body humanoid control — simultaneous locomotion + manipulation, e.g. opening heavy doors; post-trainable on NVIDIA's open Physical AI Dataset (4.8M+ downloads as of 2025-10); distributed via Hugging Face LeRobot integration.
- **N1.7** (early access 2026-04-17): 3B params; backbone swapped to Cosmos-Reason2-2B (Qwen3-VL architecture) + 32-layer DiT action head; pretraining adds **EgoScale** — 20,854 hours of egocentric human video across 20+ task categories (vs a few thousand teleop hours in N1.6), with a relative end-effector action space shared across human and robot embodiments. NVIDIA claims the "first scaling law for robot dexterity": scaling 1k→20k video-hours more than doubles average dexterous task completion (company-reported, unverified). Embodiments include Unitree G1 (incl. whole-body SONIC controller), LIBERO Panda, OXE WidowX, bimanual YAM, AGIBot Genie 1. Code Apache-2.0; weights under NVIDIA Open Model License (commercial use allowed).
- **N2** (previewed GTC 2026-03-16): built on the **DreamZero** world-action-model architecture; NVIDIA claims robots "succeed at new tasks in new environments more than twice as often as leading VLA models" and #1 rank on MolmoSpaces and RoboArena generalist-policy leaderboards (as of 2026-03, company claim); general availability slated for late 2026. NVIDIA's GTC framing: swap robotics' data problem for a compute problem via world models. See [World models](world-models.md).
- Strategic posture: NVIDIA positions GR00T as the "Android of robotics" — open(-ish) models that drive demand for its Jetson Thor / Jetson T4000 on-robot compute (see [Hardware](hardware.md), [Organizations](organizations.md)).

## Google DeepMind Gemini Robotics

- **Gemini Robotics + Gemini Robotics-ER** (2025-03-12): VLA built on Gemini 2.0 plus a separate embodied-reasoning (ER) model for spatial understanding, pointing, and planning; developed with partners including Apptronik (Apollo humanoid).
- **Gemini Robotics On-Device** (2025-06-24): the first Gemini VLA that runs fully on-robot (no cloud), for latency-sensitive and offline use; first DeepMind VLA opened to fine-tuning — adapts with as few as 50–100 demonstrations; ships with a Gemini Robotics SDK including MuJoCo simulation evaluation.
- **Gemini Robotics 1.5 + ER 1.5** (2025-09-25): agentic stack — ER 1.5 is the orchestrator (plans, calls digital tools such as web search, issues natural-language subcommands), while Robotics 1.5 is a "thinking VLA" that emits interpretable reasoning traces before acting. Demonstrated **motion transfer**: skills trained only on ALOHA-2 transfer zero-shot to Apptronik Apollo and a bi-arm Franka, and vice versa. ER 1.5 claimed SOTA across 15 embodied-reasoning benchmarks (ERQA, Point-Bench, RefSpatial) plus the ASIMOV safety benchmark. ER 1.5 is generally available via the Gemini API; the 1.5 VLA remains restricted to select partners (as of 2026-06).
- **Gemini Robotics-ER 1.6** (released 2026-04-14 via Gemini API / AI Studio): improved spatial and multi-view reasoning; new ability to read analog gauges and sight glasses, developed with Boston Dynamics, which is integrating the model into its Spot inspection platform; DeepMind calls it its safest robotics model to date on adversarial spatial-reasoning safety evals.

## Figure Helix

- **Helix** (2025-02-20): "System 1, System 2" VLA for humanoid upper-body control — S2 is a 7B open-source VLM at 7–9 Hz; S1 is an 80M-parameter visuomotor transformer at 200 Hz outputting continuous commands over a 35-DoF action space (wrists, fingers, torso, head gaze). Trained on ~500 hours of teleop; runs entirely onboard dual embedded GPUs; a single set of weights ran two robots collaborating on a shared task. Figure claims several firsts: first high-rate full-upper-body humanoid VLA, first multi-robot VLA, first fully-onboard commercial VLA (company claims). Figure dropped its OpenAI partnership (2025-02) to build Helix in-house. Closed weights.
- **Logistics scaling** (2025): scaling demos from ~10 to ~60 hours cut per-package cycle time from ~6.84 s to ~4.31 s and lifted barcode-scan success from 88.2% to 94.4%; added stateful visual memory, force-sensing input, and a "Sport Mode" (+50% execution speed) (company-reported, as of 2025-06).
- **Helix 02** (2026-01-27): adds **System 0** — a 10M-param whole-body reflex/balance controller running at 1 kHz beneath S1/S2, trained on 1,000+ hours of human motion data across 200k+ parallel simulated environments with domain randomization; adds tactile sensing (detects ~3 g forces) and palm cameras for in-hand visual feedback. Headline demo: a continuous ~4-minute kitchen sequence — 61 sequential loco-manipulation actions unloading/reloading a dishwasher with no resets or intervention; Figure calls it the longest-horizon autonomous humanoid task to date (company-reported, no third-party benchmark). Also shown: pill singulation, precise syringe dispensing.
- Helix drives Figure 02/03 robots in logistics pilots and home testing; Figure 03 (2025-10) was designed around Helix — see [Humanoid robots](humanoid-robots.md).

## Open academic/community models and benchmarks

- **Open X-Embodiment / RT-X** (2023-10): pooled ~1M+ episodes from 22 robot embodiments across 21 institutions; RT-1-X outperformed original per-lab models by ~50% average; became the standard pretraining corpus for Octo and OpenVLA.
- **Octo** (2024-05): 27M/93M-param transformer with diffusion head, trained on 800k OXE trajectories; first widely used fully open generalist policy, runs on consumer GPUs.
- **OpenVLA** (2024-06): 7B, trained on 970k OXE episodes; outperformed the 55B RT-2-X by ~16.5% absolute success across 29 evaluation tasks — the headline result that open, smaller VLAs can beat closed giants.
- **OpenVLA-OFT** (2025): optimized fine-tuning recipe reaching 97.1% average on LIBERO's four suites, beating π0, Octo, and diffusion-policy baselines on that benchmark.
- **SmolVLA** (2025-06): 450M flow-matching VLA trained largely on community-contributed LeRobot datasets; outperforms Octo/OpenVLA on LIBERO and Meta-World despite ~15x fewer params than OpenVLA (single-lab claim); runs on consumer hardware; the default hobbyist/researcher entry point via the LeRobot framework.
- **Benchmarks in use** (as of 2026-06): LIBERO (130 sim tasks; saturating at ~97%, now a sanity check) and SimplerEnv (simulated manipulation), DROID (real-world Franka corpus/eval), RoboArena (crowdsourced real-robot head-to-head evals), MolmoSpaces (2026, spatial/generalist policy benchmark), GM-100 (Ant Group, 100 real-robot tasks across 3 platforms — best average success still ~17%, a sobering counterweight to demo videos). Real-world evaluation and self-reported numbers remain the field's weakest link (a recurring ICLR 2026 community critique) — see [Open problems](open-problems.md).

## China's VLA ecosystem (brief)

- Chinese labs shipped a dense wave of VLAs in 2025–26, skewing heavily toward open weights as a distribution strategy: ByteDance Seed **GR-3** (2025-07); AgiBot **GO-1** plus the AgiBot World Colosseo data platform; Unitree's open-sourced **UnifoLM-VLA-0** (weights + code released 2026-01-29) driving G1 household tasks; X Square Robot's **WALL-OSS** open 4B model (2025-09; the company raised $140M for embodied foundation models, as of 2025-11), with the WALL-OSS-0.5 technical report (2026) adding single-stage training on a 90M-sample multimodal corpus.
- **LingBot-VLA** (Ant Group / Robbyant; paper, weights and codebase released 2026-01-27): Ant's first open embodied-AI model; trained on ~20,000 hours of teleoperated bimanual data across 9 dual-arm embodiments (AgileX, Galaxea R1Pro, AgiBot G1...); on GM-100 scores 17.30% average success / 35.41% progress with depth input — above π0.5, GR00T N1.6 and WALL-OSS under the same post-training protocol (self-reported).
- A ResearchInChina report counts 100+ VLA models in development across Chinese robotics and automotive (XPeng, Li Auto use VLA-style driving stacks) (unverified). Details in [Landscape: China](landscape-china.md).

## Training data: the binding constraint

- Typical modern mix (π0.5, GR00T N1.7, Gemini Robotics): web-scale image-text data (semantics) + cross-embodiment robot teleop (10k–20k hours for frontier models: π0 ~10k h, LingBot-VLA ~20k h) + synthetic/simulation rollouts + egocentric human video (GR00T N1.7's ~20k-hour EgoScale corpus; FLARE and motion-transfer techniques to exploit it).
- Cross-embodiment transfer is now demonstrated at product level (Gemini Robotics 1.5 motion transfer; π0.5's multi-robot co-training), meaning demonstrations collected on any robot can in principle improve all robots.
- RL from deployment experience (π*0.6/RECAP) is the newest data source, converting fleet operating time into training signal rather than relying solely on human teleop; world models are the other claimed escape from teleop scarcity (NVIDIA GTC 2026: turn the data problem into a compute problem). See [Data](data.md).

## State of play, mid-2026

- Production deployments exist but are narrow: Helix in logistics package handling, π-based models in commercial pilots (espresso, laundry, factory kitting), GR00T-based stacks across NVIDIA's humanoid partners (as of 2026-06) — see [State of the art](state-of-the-art.md).
- Open-weight frontier: openpi (π0, π0-FAST, π0.5) and GR00T N1–N1.7 are the strongest openly downloadable VLAs; Chinese open releases (LingBot-VLA, WALL-OSS, UnifoLM-VLA) are closing the gap; Gemini Robotics VLAs, Helix, and π0.6/π*0.6/π0.7 remain closed (as of 2026-07). Pattern: US frontier labs keep their best deployment models closed while NVIDIA and Chinese players open-weight aggressively to seed hardware/platform ecosystems.
- Architecture direction: hierarchy (reasoner + fast policy, now three tiers in Helix 02) is winning over monolithic decoding; world-action models (GR00T N2/DreamZero) and experience-based RL ("RL is back", π*0.6) are the two main claimed paths past imitation-learning ceilings.
- Key open questions: reliable evaluation, long-horizon error recovery, safety cases for uncaged deployment, and whether human video can substitute for scarce teleop data — tracked in [Open problems](open-problems.md) and [Tech tree](tech-tree.md).

## Sources

- https://www.pi.website/blog/pi05 — π0.5 release (2025-04-22), architecture, co-training, unseen-home cleaning results
- https://github.com/Physical-Intelligence/openpi — open weights/licensing for π0, π0-FAST, π0.5; checkpoint list; π0.6 not released (issue #789)
- https://www.pi.website/blog/pistar06 — π*0.6 + RECAP method and throughput/success numbers (2025-11-17)
- https://www.pi.website/blog/pi07 — π0.7 "steerable model" announcement (2026-04-16): specialist-level generality, language coaching, cross-embodiment transfer
- https://arxiv.org/abs/2511.14759 — π*0.6 paper ("a VLA That Learns From Experience")
- https://website.pi-asset.com/pi06star/PI06_model_card.pdf — π0.6 model card: 5B VLM + action expert, training tasks
- https://www.pi.website/research/fast — FAST action tokenizer, FAST+ universal tokenizer, ~5x training-cost claim
- https://www.bloomberg.com/news/articles/2025-11-20/robotics-startup-physical-intelligence-valued-at-5-6-billion-in-new-funding — $600M at $5.6B valuation, CapitalG-led (2025-11)
- https://www.cnbc.com/2024/11/04/jeff-bezos-and-openai-invest-in-robot-startup-physical-intelligence.html — prior round: $400M at $2.4B (2024-11), Bezos/OpenAI/Thrive/Lux/Bond
- https://techcrunch.com/2026/03/27/physical-intelligence-is-reportedly-in-talks-to-raise-1-billion-again/ — reported talks for ~$1B at >$11B valuation (2026-03, per Bloomberg)
- https://github.com/NVIDIA/Isaac-GR00T — GR00T N1.7 specs (3B, Cosmos-Reason2-2B backbone, EgoScale data, licenses)
- https://huggingface.co/blog/nvidia/gr00t-n1-7 — GR00T N1.7 deep dive: 20,854 h EgoScale, 32-layer DiT, dexterity scaling law, embodiments (2026-04-17)
- https://nvidianews.nvidia.com/news/nvidia-isaac-gr00t-n1-open-humanoid-robot-foundation-model-simulation-frameworks — GR00T N1 launch (2025-03)
- https://research.nvidia.com/labs/gear/gr00t-n1_5/ — GR00T N1.5 improvements (Eagle 2.5, FLARE)
- https://nvidianews.nvidia.com/news/nvidia-releases-new-physical-ai-models-as-global-partners-unveil-next-generation-robots — GR00T N1.6 + Cosmos Reason announcement (CoRL, 2025-09-29)
- https://nvidianews.nvidia.com/news/nvidia-and-global-robotics-leaders-take-physical-ai-to-the-real-world — GTC 2026-03: GR00T N2 preview, DreamZero, MolmoSpaces/RoboArena #1 claims, late-2026 availability
- https://the-decoder.com/gtc-2026-nvidia-wants-to-swap-robotics-data-problem-for-a-compute-problem/ — GTC 2026 world-model/data framing
- https://deepmind.google/blog/gemini-robotics-15-brings-ai-agents-into-the-physical-world/ — Gemini Robotics 1.5 / ER 1.5 (2025-09-25), thinking VLA, motion transfer, benchmark claims, availability
- https://deepmind.google/blog/gemini-robotics-on-device-brings-ai-to-local-robotic-devices/ — Gemini Robotics On-Device (2025-06), 50–100-demo fine-tuning, SDK
- https://deepmind.google/blog/gemini-robotics-er-1-6/ — Gemini Robotics-ER 1.6 release (2026-04-14), gauge reading, safety claims
- https://roboticsandautomationnews.com/2026/04/15/boston-dynamics-integrates-google-deepminds-gemini-robotics-model-into-spot-inspection-platform/100585/ — Boston Dynamics Spot + Gemini Robotics-ER 1.6 integration
- https://www.figure.ai/news/helix — Helix architecture (S2 7B @ 7–9 Hz, S1 80M @ 200 Hz), 500 h teleop, 35-DoF, claimed firsts (2025-02-20)
- https://www.figure.ai/news/helix-02 — Helix 02: System 0 10M @ 1 kHz, 1,000 h human motion data, 61-action dishwasher demo (2026-01-27)
- https://www.humanoidsdaily.com/news/from-pixels-to-torque-figure-unveils-helix-02-and-the-era-of-whole-body-autonomy — independent coverage confirming Helix 02 date, System 0 specs, 61-action / ~4-min dishwasher demo and longest-horizon claim
- https://www.figure.ai/news/scaling-helix-logistics — Helix logistics scaling metrics (cycle time, barcode success)
- https://arxiv.org/abs/2406.09246 — OpenVLA paper: 7B, 970k OXE episodes, +16.5% absolute over 55B RT-2-X across 29 tasks
- https://openvla-oft.github.io/ — OpenVLA-OFT recipe: 76.5%→97.1% LIBERO average, 26x action-generation throughput (arXiv:2502.19645)
- https://arxiv.org/html/2506.01844v1 — SmolVLA (450M, flow matching, LeRobot community data)
- https://arxiv.org/html/2601.18692v1 — LingBot-VLA paper: 20k h bimanual teleop across 9 embodiments, GM-100 results
- https://www.businesswire.com/news/home/20260127455032/en/Robbyant-Open-Sources-LingBot-VLA-as-a-Universal-Brain-for-Robots — Robbyant press release: LingBot-VLA open-sourced 2026-01-27 (weights + codebase)
- https://www.marktechpost.com/2026/01/29/ant-group-releases-lingbot-vla-a-vision-language-action-foundation-model-for-real-world-robot-manipulation/ — independent confirmation of LingBot-VLA weights release and GM-100 scores (17.30% SR / 35.41% PS; beats π0.5, GR00T N1.6, WALL-OSS)
- https://arxiv.org/html/2605.30877 — WALL-OSS-0.5 technical report (4B open VLA, data mixture)
- https://github.com/unitreerobotics/unifolm-vla — UnifoLM-VLA-0 weights/code release (2026-01-29)
- https://mbreuss.github.io/blog_post_iclr_26_vla.html — ICLR 2026 VLA research survey (community trends, benchmark critique)
- https://en.wikipedia.org/wiki/Vision-language-action_model — VLA definition, RT-2 origin of the term
- https://www.therobotreport.com/x-square-robot-secures-140m-in-funding-for-ai-foundation-models/ — X Square Robot WALL-OSS and $140M raise
- https://techcrunch.com/2026/01/05/nvidia-wants-to-be-the-android-of-generalist-robotics/ — NVIDIA's open-model strategy framing at CES 2026
