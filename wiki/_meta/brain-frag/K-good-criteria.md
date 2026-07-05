## "做好"的判据 & 评价 (What Makes an On-Device Brain Good)

Every prior section describes *how* to build the brain; this one defines *whether it is good* — and exposes that the field currently **cannot answer that question with public data**. The honest summary: there is a **benchmark crisis** (self-reported numbers, no apples-to-apples task set) stacked on top of an **evaluation crisis** (near-zero public MTBF/intervention-rate disclosure). A buyer's job is to convert marketing Hz/TOPS into a scorecard with a **hardware SKU attached to every number** and a **duty-cycle attached to every success rate**. This section gives that scorecard, its anchor numbers, and where the numbers are missing.

### The scorecard (七维判据)

Seven axes. Each cell pairs a *demandable metric* with the best public anchor and its source-quality tag. **Rule of thumb: reject any Hz/TOPS figure not bound to a named SoC SKU and a sustained (not burst) duty cycle.**

| 判据 (axis) | Demandable metric | Public anchor (best available) | Tag |
|---|---|---|---|
| **实时性 Real-time** | S1 control rate on the *shipping* module, not a desktop GPU | S1 200 Hz / S2 7–9 Hz (Figure Helix, but S1 = 80M params only); full 7B VLA = ~3 FPS on Jetson AGX Orin @INT4 | (primary) |
| **延迟 Latency** | end-to-end perception→action ms on the module SKU | LiteVLA-Edge 150.5 ms (~6.6 Hz) Jetson-class; LiteVLA-H 19.74 Hz outer / 6.08–6.67 Hz semantic on one AGX Orin (best edge dual-rate) | (primary) |
| **泛化 Generalization** | OOD instance/spatial/language success, per task class | π0: 87% Clean-Dish vs 67% Unzip-Bag (in-dist. spread); ACT 86%→~12% unseen dishes; pretrained Qwen-VLA out-generalizes π0.5 on OOD language, exact 32.0%/12.6% figures *(unverified)* | (primary) |
| **可靠性 Reliability** | MTBI / MTBF at 8h×5d duty; uptime % | AutoInspect MTBI **78 h** (non-humanoid); industrial target 95–99% uptime; humanoids today 30–90 min/charge; safety-critical bar = 99.999% | (primary anchor / secondary targets) |
| **功耗热 Power/thermal** | *sustained* W and TOPS/W under continuous load | Jetson AGX Thor 40–130 W, ≤2,070 FP4 TFLOPS, 128 GB, ~3.5× perf/W vs Orin; Hailo-8 ~26 TOPS @2.5–3 W (~10 TOPS/W, ASIC) | (primary / secondary) |
| **成本 Cost** | $/TOPS, brain as % of system BOM | Silicon ~8% of humanoid BOM 2025 → ~5% by 2035; ~$1,400 semi BOM/unit (UBS); ~$35k total BOM, actuators >30% (BofA) | (secondary) |
| **可更新 & 安全 Updatability/Safety** | OTA cadence, canary vs fleet-wide, certified fallback | SSE→MRC formal safe-stop (arXiv 2603.22703); ISO 10218:2025 ties stop-distance to latency+control-freq; Optimus overnight fleet OTA (vendor-claimed) | (primary / unverified) |

### Anchor 1 — the real-time / latency gap (延迟鸿沟)

The single most load-bearing evaluation fact: **full-size VLAs on real edge silicon run 5–30× too slow for smooth manipulation**, and the fast rates you see in papers are usually desktop-GPU rates.

- **Production dual-rate exists, but only by shrinking S1.** Figure Helix runs S2 (internet-pretrained VLM) at **7–9 Hz** and S1 (reactive visuomotor policy, **80M params**) at **200 Hz** across **35 DoF** of the upper body (primary, figure.ai/news/helix). Broader dual-system surveys quote Slow **1–5 Hz** / Fast **20–50 Hz** (primary, arXiv 2510.24795). Key caveat: the 200 Hz is achieved *at 80M params*, not with a full VLA.
- **Full VLA on edge is far below control rate.** OpenVLA (**7B**) hits only **~3 FPS on Jetson AGX Orin even at INT4** (primary). LiteVLA-Edge: **150.5 ms** mean end-to-end (~**6.6 Hz**) on a Jetson-class ROS2 pipeline; LiteVLA-H: **19.74 Hz** outer-loop action emission with **6.08–6.67 Hz** semantic perception on a single **AGX Orin** — the best-reported *edge* dual-rate result (primary, arXiv 2511.05642 / 2603.03380 / 2605.00884).
- **Beware GPU-class Hz.** Parallel/async decoding (PD-VLA) cuts VLA latency **~2.5×** (2.52× action-frequency speedup) and pushes toward **100–200 Hz** — but on **desktop-class GPUs**, not edge modules (primary, arXiv 2503.02310; surveyed in 2505.04769). This is why the scorecard rule is *demand the SKU*.

See [E — the real-time control split](E-realtime-split.md) for where these cuts land in silicon, and [I — edge-native models](I-edge-models.md) for the model-shrinking that makes 200 Hz S1 possible.

### Anchor 2 — the generalization scorecard (泛化崩塌)

Success rate is **not one number**; the *same* policy swings 40+ points across task classes, and imitation baselines collapse under OOD shift.

| Policy | Metric | Number | Tag |
|---|---|---|---|
| π0 | in-dist. task spread | **87%** Clean-Dish vs **67%** Unzip-Bag vs **52%** Folding-Shorts (200 demos) | (primary) |
| ACT | standard → unseen-dishes (OOD instance) | **86% → ~12%** (−74 pts) | (primary) |
| Qwen-VLA vs π0.5 | avg OOD *language*-conditioned success | a pretrained Qwen-VLA out-generalizes π0.5 on OOD language; the exact **32.0% / 12.6%** pair is *(unverified — not found in cited source)* | (unverified) |
| GR-Dexter (cross-embodiment) | unseen objects / unseen instructions | **0.85 / 0.83** | (primary) |

Buyer checklist items that fall straight out of this: (1) demand success rates *per task class*, not a headline average; (2) ask whether the policy was **trained cross-embodiment** — GR-Dexter's 0.83–0.85 OOD vs single-embodiment baselines shows this is a measurable lever (primary, arXiv 2512.24210); (3) treat any single OOD number below ~30% language-following as the current *field* floor, not a vendor defect. Sources: arXiv 2511.11298 (π0/ACT). *Caveat: the specific "Qwen-VLA-Instruct 32.0% vs π0.5 12.6%" figures could not be located in arXiv 2505.15660 (which is X-ICM cross-task in-context imitation) or in the Qwen-VLA paper 2605.30280 (which reports Qwen-VLA-aloha 76.9% avg OOD vs π0.5 41.5%) — treat the 32.0/12.6 pair as (unverified).*

### Anchor 3 — the reliability data void (可靠性数据缺口)

This is the axis where the industry is **least honest**, because almost no one publishes MTBF.

- **The demo→24/7 gap is quantitative.** "Stage-walk vs eight hours a day, five days a week, without intervention" — a >90% curated demo success rate does **not** imply fleet reliability (secondary, therobotreport/mindstudio).
- **Duty-cycle reality.** Industrial buyers expect **95–99% uptime**; most humanoids today run **30–90 min** before recharge/intervention, with battery chemistry capping active use at **1–4 h** (secondary, awesomerobots.xyz / patentpc.com). Power/thermal and mechanical failure **compound** with AI-brain failure.
- **Near-zero public MTBF.** The cleanest dated public number is **MTBI = 78 h** from AutoInspect (long-term autonomous industrial *inspection*, non-humanoid but instructive) (primary, arXiv 2404.12785). Against a safety-critical **99.999% ("five nines")** aspirational bar (secondary, patentpc.com), humanoid/VLA vendor MTBF is **essentially unpublished** — this absence *is* the finding.

### Anchor 4 — how to actually benchmark (评测方法学)

Because self-reported numbers aren't comparable, the methodology itself is a criterion.

- **The reproducibility problem is structural.** Most VLA/policy results use lab-specific hardware, task defs, and success metrics; even shared object sets suffer camera/lighting/hardware variance — published rates are **not apples-to-apples** (secondary, arXiv 2510.04354 / 2508.11117).
- **The leading proposed fix: RoboArena.** Decentralized, **double-blind pairwise** real-robot evaluation across **7 institutions** on a shared **DROID** platform, aggregating **600+ pairwise episodes** over 7 generalist policies (**4,284** total eval episodes in the broader dataset) into an ELO-like ranking — the direct answer to "how do you benchmark generalist policies you can't fix a task list for" (primary, arXiv 2506.18123). A buyer should prefer vendors whose numbers come from **third-party pairwise** evaluation over self-run fixed-task demos.

See [evaluation](../wiki/evaluation.md) and [open-problems](../wiki/open-problems.md) for the field-wide benchmark discussion.

### Anchor 5 — cost, power, updatability & safety (成本 / 功耗 / 更新 / 安全)

- **The brain is not the cost lever.** Compute is **~8% of humanoid BOM (2025) → ~5% by 2035**; ~**$1,400** semi BOM/unit rising to ~$2,000 by 2050 (UBS); total BOM ~**$35k**, **actuators >30%** (>50% in simple configs) (secondary, UBS / BofA Apr 2025). Optimizing $/TOPS matters far less than actuation/mechanics — but power/thermal still gates duty cycle.
- **Power/thermal: demand sustained, not burst.** Jetson AGX Thor spans **40–130 W** for ≤**2,070 FP4 TFLOPS** / 128 GB, ~**3.5× perf/W** vs Orin — ask *where in that band* the workload sits under **continuous** load (primary, nvidia.com). Contrast Hailo-8 at ~**26 TOPS @2.5–3 W (~10 TOPS/W)** — dedicated ASICs win TOPS/W but can't host large VLA/VLM (secondary, hailo.ai). See [G — power & thermal](G-power-thermal.md).
- **Updatability = a fleet-learning loop, with a risk flag.** Tesla Optimus is described as pushing "validated model weight updates… to all Optimus units overnight" (Cortex 67k+ H100-equiv, 70k GPU-h/cycle, 10k+ synthetic variations/task) — but sourcing is a **fan/analyst blog**, so treat figures as **vendor-claimed (unverified)**. Demandable: OTA *cadence*, **canary/staged vs fleet-wide-simultaneous** (simultaneous rollout is riskier on regression), and whether any adaptation is on-device vs cloud-trained-then-pushed. See [J — edge learning](J-edge-learning.md).
- **Safety must be control-capable and latency-aware.** The formal anchor is a **Safe-Stoppable Envelope (SSE)**: a state-set from which a certified fallback controller reaches a dynamically-stable **Minimum Risk Condition (MRC)**, with monitors detecting envelope departure (primary, arXiv 2603.22703). **ISO 10218:2025** now makes functional-safety explicit and requires protective-separation-distance math to include **system latency and control-loop frequency** — directly tying the latency axis to certified safety, so a slow brain is *literally* a less-safe brain (primary/standard). See [safety-regulation](../wiki/safety-regulation.md).

### Takeaway

A "good" on-device brain is **not** the one with the biggest headline TOPS or Hz. It is the one that (1) sustains its S1 control rate on the *shipping SoC* under continuous load (Figure's 200 Hz benchmark — but note that's 80M params, and full VLAs still crawl at 3–7 Hz on Jetson); (2) reports OOD success **per task class** and was trained **cross-embodiment**; (3) can show a **third-party pairwise** eval (RoboArena-style) rather than self-run demos; (4) publishes an **MTBF/intervention rate** at 8h×5d duty at all — which today almost none do; and (5) ships a **certified, control-capable safe-stop** whose stopping math already accounts for brain latency. The brain is only ~5–8% of BOM, so the return on getting these five right is disproportionate. Every number a vendor quotes should arrive with a **SKU and a duty cycle** — its absence is the answer.

来源:
- https://www.figure.ai/news/helix
- https://arxiv.org/pdf/2510.24795 (Survey on Efficient VLA Models)
- https://arxiv.org/pdf/2511.05642 (Lite VLA) ; https://arxiv.org/pdf/2603.03380 (LiteVLA-Edge) ; https://arxiv.org/html/2605.00884 (LiteVLA-H)
- https://arxiv.org/abs/2503.02310 (PD-VLA — parallel decoding, 2.52× action-frequency speedup, desktop-GPU) ; https://arxiv.org/html/2505.04769 (VLA Models survey — cites PD-VLA, GPU-class Hz caveat)
- https://arxiv.org/pdf/2511.11298 (Experiences from Benchmarking VLA Models — π0 in-dist. 87/67/52%, ACT 86%→12% OOD; verified against Table 3)
- https://arxiv.org/html/2505.15660 (Exploring the Limits of VLA Manipulations in Cross-task Generalization / X-ICM — does NOT contain the 32.0/12.6 Qwen figures) ; https://arxiv.org/abs/2605.30280 (Qwen-VLA — reports 76.9% avg OOD vs π0.5 41.5%, also not 32.0/12.6)
- https://arxiv.org/pdf/2512.24210 (GR-Dexter Technical Report — cross-embodiment 0.85/0.83)
- https://arxiv.org/pdf/2404.12785 (AutoInspect — MTBI 78 h)
- https://arxiv.org/abs/2506.18123 (RoboArena — distributed double-blind pairwise real-robot eval)
- https://arxiv.org/html/2510.04354 ; https://arxiv.org/html/2508.11117 (reproducibility / sim-to-real eval)
- https://www.therobotreport.com/ ; https://mindstudio.ai (humanoid deployment gap analysis — secondary)
- https://awesomerobots.xyz (Enterprise Humanoid Robots Guide 2026) ; https://patentpc.com (Robot Downtime Rates & Reliability Data)
- https://www.nvidia.com/en-us/autonomous-machines/embedded-systems/jetson-thor/ ; https://thinkrobotics.com (Jetson AGX Thor review)
- https://hailo.ai/blog/evaluating-edge-ai-processor-in-the-generative-ai-era
- UBS Humanoid Robots semiconductor analysis (via financialmodelingprep.com) ; https://institute.bankofamerica.com (Humanoid Robots 101, Apr 2025)
- https://optimusk.blog/blog/tesla-optimus-software-update (fan/analyst blog — vendor claims unverified)
- https://arxiv.org/pdf/2603.22703 (Learning Safe-Stoppability Monitors for Humanoid Robots — SSE/MRC)
- ISO 10218:2025 revision (functional-safety; stop-distance must include latency + control frequency)
