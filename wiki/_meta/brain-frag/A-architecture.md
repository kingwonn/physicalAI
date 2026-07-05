## 大脑架构基础与双系统 (Architecture & Dual-System)

The on-device embodied "brain" is not one model. Across the four production-grade systems that define the 2025-26 state of the art — Figure Helix, NVIDIA GR00T N1/N1.5, Physical Intelligence π0/π0.5, and Google DeepMind Gemini Robotics — the field has converged on a **dual-system split**: a slow, internet-pretrained **System 2 (S2)** that does semantic scene/language understanding and planning, feeding a fast, lightweight **System 1 (S1)** that turns that intent into continuous motor commands. This is the concrete architecture any on-device brain must instantiate.

### Why split at all (the speed-vs-generality tradeoff)

- Figure's framing is the field's rationale (primary): *"VLM backbones are general, but not fast, and robot visuomotor policies are fast but not general. Helix resolves this tradeoff through two complementary systems, trained end-to-end to communicate."* [figure.ai/news/helix]
- A single monolithic VLM is semantically general but too slow for closed-loop control (large internet-pretrained transformers run at single-digit-to-~10 Hz); a small visuomotor policy is fast (100-200+ Hz) but does not generalize beyond its demo data. The split lets each layer run at its own clock and own scale. (primary)
- The pattern maps onto a neuroanatomical analogy widely used in the field: **S2 ≈ cerebral cortex** (symbolic/semantic deliberation), **S1 ≈ cerebellum** (fast motor control + environmental feedback); some literature adds a spinal-cord / reflex tier. (unverified — analogy, cross-cited but not from a single canonical primary source)

### The four reference architectures

| System | S2 (slow / "brain") | S2 rate | S1 (fast / "cerebellum") | S1 rate | Coupling | Deploy |
|---|---|---|---|---|---|---|
| **Figure Helix** | 7B open-weight VLM | 7-9 Hz | 80M cross-attn enc-dec transformer | 200 Hz | single continuous latent vector; async | dual low-power embedded GPUs, fully onboard |
| **NVIDIA GR00T N1** | Eagle-2 VLM (1.34B) | 10 Hz | Diffusion Transformer (flow-matching) | 120 Hz | cross-attention on VLM tokens; jointly trained | Jetson-class; 2.2B total |
| **NVIDIA GR00T N1.5** | Eagle 2.5 VLM (2.1B), **frozen** | (~10 Hz) | flow-matching DiT + FLARE aux | (~120 Hz) | LN'd MLP connector; joint flow-matching + world-model loss | ~3B total |
| **PI π0 / π0.5** | PaliGemma VLM (3B) | (chunk-triggered) | 300M flow-matching "action expert" | ~50 Hz | two streams, one jointly-trained model | 3.3B total; π0-small 470M variant |
| **Gemini Robotics** | Gemini Robotics-ER ("cognitive brain") | cloud/edge | Gemini Robotics VLA + local action decoder | 50 Hz local | ER emits per-step NL instruction; rolling-horizon chunks | cloud backbone + on-device decoder (or fully local) |

All figures (primary) except GR00T N1.5 S2/S1 rates in parentheses (inferred to match N1; the N1.5 page does not restate them — treat as (unverified) at the exact-Hz level).

### Figure Helix — the purest asynchronous dual-clock design

- **S2**: a 7B-parameter open-weight VLM, pretrained on internet-scale data, fine-tuned on 500+ hours of robot teleoperation; runs at **7-9 Hz**. (primary, verified vs figure.ai/news/helix)
- **S1**: an **80M-parameter** cross-attention encoder-decoder transformer (~90x smaller than S2), runs at **200 Hz** — a ~25-30x rate gap between the two systems. (primary, verified)
- **Communication is a single continuous latent vector**, not language tokens: S2 *"distills all semantic task-relevant information into a single continuous latent vector"* consumed by S1. During training, gradients backpropagate from S1 into S2 through this vector (full end-to-end differentiability); at deploy, S1 reads *"the most recent S2 latent vector"* from shared memory — this decoupling is exactly what lets the two systems run **asynchronously at their own clock rates**. (primary, verified)
- **Action space**: full upper-body **35-DoF** at 200 Hz — wrist poses, per-finger flexion + abduction, torso and head orientation targets — enabling dexterous bimanual manipulation. (primary, verified)
- **Deployment**: both S1 and S2 run **entirely onboard on dual low-power embedded GPUs**, splitting inference across two chips — a literal "brain-vs-cerebellum on separate silicon" instance and the single most relevant on-device precedent here. (primary, verified) See also [Figure](company-figure.md).

### NVIDIA GR00T N1 → N1.5 — jointly-trained VLM + Diffusion Transformer

- **N1** pairs an Eagle-2 VLM System-2 (1.34B params; Eagle-2 = SmolLM2 LLM + SigLIP-2 image encoder) with a **Diffusion-Transformer (flow-matching) System-1** that cross-attends to the VLM tokens. Both are **trained jointly end-to-end**, not as separate stages. Released checkpoint GR00T-N1-2B = **2.2B** total. (primary)
- **N1 throughput**: S1 samples a **16-action chunk in 63.9 ms** on an L40 GPU (bf16), with **K=4 flow-matching integration steps**; S2 updates conditioning at **10 Hz**, S1 sustains **120 Hz** closed-loop control. Chunking amortizes the slow VLM over many fast actions. (primary, verified vs arXiv 2503.14734 — "inference time for sampling a chunk of 16 actions is 63.9ms on an L40 GPU using bf16"; VLM "1.34B", total "2.2B", SmolLM2 LLM + SigLIP-2 encoder, S2 10Hz / S1 120Hz all confirmed verbatim)
- **N1.5** upgrades S2 to **Eagle 2.5 (2.1B)**, **freezes the VLM during pretraining and finetuning**, adds a layer-norm to the MLP connector, and co-trains flow-matching + **FLARE** (Future LAtent Representation Alignment — aligns to target future embeddings rather than generating future frames), letting it learn from human video too. Trained **250K steps on 1K H100 GPUs, global batch 16,384**. (primary, verified vs research.nvidia.com/labs/gear/gr00t-n1_5)
- **Payoff of a stronger, decoupled S2**: on a real Fourier GR-1 humanoid (pick a language-specified fruit → plate), **language-following 93.3% (N1.5) vs 46.6% (N1)**; overall success **83.0% vs 43.3%** — evidence that strengthening/freezing S2 sharply improves instruction-following without touching the control-rate S1. (primary, verified — all four figures 93.3/46.6 and 83.0/43.3 confirmed verbatim on research.nvidia.com/labs/gear/gr00t-n1_5) See also [NVIDIA](company-nvidia.md).

### Physical Intelligence π0 / π0.5 — two streams, flow-matching action expert

- **π0**: PaliGemma **3B** VLM backbone + a separate **300M flow-matching "action expert"** (init from scratch, handles proprioceptive state + action generation); **3.3B** total. Conceptually the same S2/S1 split as Helix, but implemented as **two streams inside one jointly-trained model** rather than two asynchronously-clocked systems. (primary, verified vs arXiv 2410.24164 — "300M parameters for the action expert…for a total of 3.3 billion parameters")
- **Chunking**: predicts a full **H=50 action chunk (1 s @ 50 Hz)** per forward pass via conditional flow matching, **10 integration steps** (δ=0.1); the chunk executes open-loop before regeneration. (primary, verified — "we use H=50", "10 integration steps (corresponding to δ=0.1)")
- **Rate**: ~**50 Hz** motor output; onboard inference latency **~73 ms (RTX 4090, bf16, 3 cameras)** — a new pass fires every ~0.5-0.8 s. This is how a not-real-time VLM+diffusion stack still sustains 50 Hz: chunking amortizes slow inference over many fast open-loop actions. (~73 ms figure secondary — not in 2410.24164 main text, corroborated by external benchmarks; the ~86 ms off-board/network figure could not be sourced and is dropped as (unverified))
- **π0-small (470M, no VLM pretraining)** makes the tradeoff explicit: dropping internet-scale pretraining shrinks the model ~7x but sacrifices generalization — why the field keeps a large pretrained VLM specifically for the S2 role. (primary, verified — "π0-small, has 470M parameters, does not use VLM initialization")
- **π0.5** makes the hierarchy explicit: the model first **verbalizes the next subtask in natural language** ("what to do next"), then the 300M action expert decodes it into a 50-step chunk — chain-of-thought-to-action (shared with PI's "Hi Robot"). Heterogeneous co-training (multi-robot + web/semantic + subtask annotations) yields open-world generalization: **10-15 min multi-stage mobile-manipulation** in entirely new kitchens/bedrooms unseen in training. (primary) See also [Physical Intelligence](company-pi.md).

### Google DeepMind Gemini Robotics — explicit cloud/edge two-model split

- **Two models**: **Gemini Robotics-ER** (the "cognitive brain" / embodied-reasoning model) does spatial understanding, task planning, and success detection; **Gemini Robotics (VLA)** turns each ER-emitted per-step NL instruction into low-level motor commands, with its own internal chain-of-thought and long-task decomposition. (primary)
- **Latency hiding**: a large VLA backbone runs in the **cloud**, sending compressed guidance to a **lightweight local action decoder** that predicts multiple short motion chunks at once to mask a backbone **query-to-response latency optimized to under 160 ms** behind a **50 Hz effective control frequency**, for ~**250 ms end-to-end** (raw observations → low-level action chunks) closed-loop latency. (primary, verified vs arXiv 2503.20020 — "optimized from seconds to under 160ms", "end-to-end latency…is approximately 250ms", "effective control frequency is 50Hz") A separately-released **fully on-device variant** (Gemini Robotics On-Device) runs the whole loop locally, but **no per-step ms figure is published** — DeepMind's on-device materials give no hard latency number, so the earlier "under 10 ms/step" claim is **(unverified)** and likely wrong (on-device control loops are documented only at ≥15-30 Hz, i.e. ~33-67 ms/cycle).
- **Cross-embodiment "Motion Transfer"**: skills trained only on ALOHA 2 transfer **zero-shot** to Apptronik Apollo and a bi-arm Franka — because the shared backbone learns embodiment-agnostic representations and only the lightweight local decoder needs per-robot adaptation. Splitting brain (backbone) from cerebellum (decoder) aids **cross-embodiment transfer, not just speed**. (primary)

### Takeaways for an on-device brain

- **Two clocks, two sizes**: budget for a big slow S2 (single-digit-to-~10 Hz, 1-7B params) and a small fast S1 (~50-200 Hz, 80-300M params). The rate gap is the whole point. (primary, cross-model)
- **Latent (not tokens) is the tightest coupling**: Helix's single continuous latent vector + shared memory is what makes true async on-device dual-GPU deployment work. (primary)
- **Chunking is the latency trick**: π0/GR00T show a slow non-real-time stack still hits 50-120 Hz by amortizing one inference over a 16-50-step chunk. Any on-device brain lives or dies on chunk-horizon vs regeneration-latency budgeting. (primary)
- **Freezing/strengthening S2 pays off** (GR00T N1.5's 46.6%→93.3% language-following, 43.3%→83.0% overall) — decoupling lets you upgrade the reasoning half independently of the control half. (primary)

来源:
- https://www.figure.ai/news/helix
- https://arxiv.org/abs/2503.14734
- https://research.nvidia.com/labs/gear/gr00t-n1_5/
- https://arxiv.org/abs/2410.24164
- https://www.pi.website/blog/pi0
- https://arxiv.org/abs/2504.16054
- https://www.pi.website/blog/pi05
- https://deepmind.google/blog/gemini-robotics-15-brings-ai-agents-into-the-physical-world/
- https://arxiv.org/abs/2503.20020
