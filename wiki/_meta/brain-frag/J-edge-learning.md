## 端侧学习 / 自适应 & 数据飞轮 (On-Device Learning & Data Flywheel)

An on-device brain that ships frozen is a dead brain. The economically decisive property is not peak inference quality on day one but **the rate at which the deployed fleet improves itself** — the loop from *deploy → collect experience → curate → fine-tune → redeploy*. This section separates three distinct regimes that are routinely conflated: (1) **cloud-scale training** (thousands of episodes to acquire a genuinely new skill), (2) **on-device few-shot adaptation** (tens of demos to calibrate/adapt an existing skill), and (3) **test-time compute** (spend more FLOPs *per action* at inference to buy accuracy, trading directly against control-loop Hz). All three feed a fleet-level **data flywheel**, whose real engineering content is curation, OTA safety, and privacy — not the model.

### The two data regimes — cloud-scale acquisition vs. on-device adaptation

The single most abused number in this space is "50 demos." It is real, but it applies only to *adaptation*, not *new-skill acquisition*. The Gemini Robotics technical report states both bounds explicitly:

| Regime | Data budget | What it buys | Where it runs | Source |
|---|---|---|---|---|
| On-device few-shot adaptation | **50–100 demonstrations** | task-specific calibration/adaptation of an *existing* skill; **"for 7 of 8 tasks, fine-tuning achieved success rate above 70% with at most 100 demonstrations"** (per-task breakdown in Fig. 26; no explicit cross-task average is reported *(unverified: ">60% avg" is an interpolation)*) | on-robot (Gemini Robotics On-Device) | arXiv:2503.20020 (primary) |
| Cloud-scale skill acquisition | **2,000–5,000 episodes / task** | genuinely new long-horizon / dexterous skills | cloud training | arXiv:2503.20020 (primary) |

**Gemini Robotics On-Device** (Google DeepMind, launched **2025-06-24**) is the first VLA in the Gemini Robotics family opened for fine-tuning, and it runs **inference fully locally on the robot's onboard computer, "independent of a data network"** (robust to intermittent/zero connectivity); developers fine-tune via the Gemini Robotics SDK (MuJoCo sim + "Trusted Tester" program) (primary). *(Note: DeepMind confirms network-independent **inference**; it does not explicitly state the **fine-tuning** step itself runs offline — "fully local training with no network" is (unverified).)* This is architecturally distinct from the **full cloud-hybrid Gemini Robotics** model, which is a **split fast/slow design**: a large cloud-hosted VLA backbone (distilled from Gemini Robotics-ER) paired with a **local low-level action decoder**. That hybrid reports **~250 ms** end-to-end observation→action-chunk latency, an **effective 50 Hz** control rate (each chunk = multiple actions), and a backbone query→response latency cut from "seconds" to **<160 ms** via distillation to the smaller on-robot decoder (primary). *Takeaway: "50 demos on-device" and "250 ms cloud-hybrid" describe two different products; do not merge them.*

### Continual learning — is catastrophic forgetting actually the enemy?

Two opposing findings, both worth carrying:

- **Explicit architectural insulation.** Physical Intelligence's **"Knowledge Insulation"** (introduced with **π0.5 + KI**; arXiv:2505.23705): the VLM backbone trains on π0-FAST discrete action tokens + web-data co-training targets, while a *separate action expert* produces continuous actions (flow/diffusion) and **its gradients are blocked ("Stop Gradient") from flowing back into the VLM backbone** — "gradients from the action expert do not flow into the VLM backbone." This is gradient isolation against semantic/language forgetting during action fine-tuning — not replay buffers, not EWC-style regularization (primary — pi.website/research/knowledge_insulation, arXiv:2505.23705). *(π0.6, Nov 2025, builds on the same PI recipe lineage; explicit "Knowledge Insulation" naming is documented for π0.5 — π0.6 attribution (unverified).)*
- **Counter-narrative: VLAs may not need heavy machinery.** A **2026** arXiv study (Liu et al.) found pretrained VLA models are **"surprisingly resistant to forgetting in continual learning"** vs. small-policy-from-scratch baselines. Its actual mechanism is **simple Experience Replay (ER) in supervised continual imitation learning** — *not* an anti-forgetting-machinery-free result and *not* on-policy RL. The load-bearing finding: **large-scale pretraining changes the dynamics** so that ER achieves near-zero forgetting with a **tiny replay buffer (~2% of data)**, where from-scratch models need **>20%**; "forgotten" skills also recover rapidly with minimal fine-tuning (secondary, single-source — arXiv:2603.03818). *Caveat: still contradicts classical RL/vision continual-learning results where forgetting is severe; treat as VLA-specific and provisional — and note it does still use a replay buffer.*

**Engineering read:** insulation (π-style) is the safe default when a *single* model must keep both language and motor competence; the "resistant to forgetting" result is promising but not yet load-bearing enough to design against.

### Fleet-scale RL and the closed loop ("Learning While Deploying")

- **LWD** closes deploy→shared-experience→improve→redeploy across a **fleet of 16 dual-arm robots** on **8 real-world manipulation tasks**, reaching **95% average success** (primary — arXiv:2605.00416). Mechanism: **DIVL** (Distributional Implicit Value Learning) for stable value estimation + **QAM** (Q-learning via Adjoint Matching) to extract policies from flow-based VLA models, fed by autonomous rollouts **plus human interventions** collected fleet-wide — i.e. **offline-to-online RL**, not imitation learning. The load-bearing point: *human interventions are a first-class data source*, not a fallback.

### The data flywheel, quantified (Scanford / "Robot-Powered Data Flywheels")

The clearest end-to-end flywheel measurement in the literature:

| Stage | Concrete number | Source |
|---|---|---|
| Deploy | Franka FR3 + TidyBot++ base, **10 days × 4 h/day = 40 h** scanning library shelves | arXiv:2511.19647 (primary) |
| Human cost | only **26 interventions total** (~2.6/day, each **<5 min**); est. **18.7 h manual labor saved** | " |
| Curation | **8,232** raw labeled images → **5,019** training images via string-similarity DB matching | " |
| In-domain gain | accuracy **32.4% → 71.8%** after **one** fine-tuning cycle | " |
| Domain-adjacent gain | OCR far weaker: EN **24.8%→46.6%**, ZH **30.8%→38.0%** | " |

**Lesson:** the flywheel's real engineering is **automated curation** (which filtered ~39% of raw images) and the **in-domain vs. domain-adjacent gap** — flywheels compound fast on the exact deployed distribution and *much* more slowly on adjacent capabilities.

### Test-time compute — buying accuracy against the Hz budget

The System-2-for-robots question is a resource-allocation problem: every extra sample/iteration spent reasoning is subtracted from control frequency. The quantified tradeoffs:

| Method | Compute spent | Accuracy gain | Latency / Hz cost | Source |
|---|---|---|---|---|
| **RoboMonkey** | sample **16 actions** + Gaussian-perturbation verifier | **+25 pts** OOD (60% vs 35% OpenVLA); power-law error↓ vs sample count across CogACT/Octo/OpenVLA/SpatialVLA | **+~650 ms** on 1×H100 (−41.3% vs naive); real-world **~1.5 Hz** | arXiv:2506.17811 (primary) |
| **E-TTS** | co-scale reasoning + action sampling, history-aware verify | **+150% relative** success (optimal config) | only **+46.6%** latency | arXiv:2606.27268 (secondary) |
| **Recurrent-Depth VLA** | latent iterative reasoning (not token CoT) | tasks at **0%@1-iter → >90%@4-iter**; simple tasks saturate fast | avoids token-CoT memory/latency; designed for on-device budget | arXiv:2602.07845 (secondary) |

**Key architectural answer** — the mainstream reconciliation is the **dual-system (System-1/System-2)** split: a large VLM "slow system" at **~1–9 Hz** for scene/language/planning, a lightweight (often diffusion) "fast system" for motor control (typically **20–50 Hz**, up to **200 Hz** at the extreme). Figure **Helix**: onboard VLM System-2 (7B) at **7–9 Hz**, paired with an **80M System-1 running at 200 Hz** (its fast side sits *well above* the 20–50 Hz band — do not lump Helix's fast loop into 20–50 Hz); HiRT / RoboDual / OpenHelix / FiS-VLA / UniFS follow the more typical **1–5 Hz slow / 20–50 Hz fast** split (secondary — figure.ai/news/helix, arXiv:2506.01953 + dual-system VLA literature). RoboMonkey's ~1.5 Hz shows why naive 16-sample verification is a *slow-system* technique — it cannot live in the fast loop.

**Budget ceiling:** all of the above must fit **NVIDIA Jetson Thor** if run locally rather than via a cloud backbone — up to **2,070 (sparse) FP4 TFLOPS** (1,035 dense), **128 GB** LPDDR5X, **40–130 W**; **up to 7.5× AI compute** and **3.5× energy efficiency** vs. Jetson AGX Orin, and **"up to 5× on generative AI models"** — but this 5× is the *max* across LLMs/VLMs/VLAs; the measured **VLA (GR00T N1.5) speedup is ~2.74×**, not 5× (primary — NVIDIA developer blog). RoboMonkey's 16-sample verifier is budgeted for an **H100**, not Thor; on-device test-time scaling must therefore favor *cheap* schemes (recurrent-depth latent iteration) over *sample-heavy* ones (16× verification).

### Fleet operations — flywheel plumbing (teleop, OTA, privacy)

- **Teleop-as-flywheel (1X NEO "Expert Mode").** Human operators remotely pilot the robot through not-yet-autonomous tasks; **every teleop session is recorded, labeled, and fed into the Redwood model** (CEO Børnich: "the first NEO will be less capable than the thousandth NEO"). Privacy mitigations disclosed: operators need owner permission, video can be blurred, owner-defined no-go zones, no takeover without approval — framed as a "social contract" (secondary — therobotreport / engadget).
- **Fleet OTA + cross-robot transfer (Figure).** Whole-fleet simultaneous behavior pushes via OTA, paired with **cross-robot policy transfer** (a policy trained on one robot applies across many without per-robot fine-tuning) — ties flywheel economics to production ramp: more robots → more fleet-hours → more failures → more Helix training data (secondary — figure.ai/news/helix).
- **OTA safety = staged canary.** Best practice: push to **~1%** of fleet first, monitor boot-success / heartbeat / sensor-data-quality; proceed to **10%+** only if nominal; per-device status chain (downloaded→verified→applied→booted→health-check-passed); **automatic rollback** on failed post-update health check without human intervention (secondary — roboticscenter.ai; arXiv:2605.28097 "ICAN-Deploy").
- **Privacy: federated learning (proposed).** The formal privacy mechanism for fleet learning is **federated learning** — raw sensor/interaction data never leaves the device; only model-weight updates are aggregated centrally (e.g. secure aggregation / differential-privacy noise) (secondary; *source text truncated in research — treat as directional, verify aggregation-scheme specifics before citing*).

### Takeaway

Design the brain to **learn after it ships**, and instrument the three regimes separately: (1) reserve cloud training for new-skill acquisition (**2,000–5,000 episodes**), (2) expose **on-device few-shot adaptation** (**50–100 demos**) for per-site calibration, (3) budget **test-time compute** as a *slow-system* resource (dual-system 1–9 Hz / 20–50 Hz), preferring latent-iteration over sample-heavy verification when local. The flywheel's engineering value lives in **automated curation** (Scanford filtered 8,232→5,019) and **fleet safety plumbing** (canary OTA + rollback), while **teleop interventions** are first-class training data and **federated learning** is the privacy story that makes home deployment socially acceptable.

来源:
- https://deepmind.google/blog/gemini-robotics-on-device-brings-ai-to-local-robotic-devices/
- https://arxiv.org/html/2503.20020v1 (Gemini Robotics technical report)
- https://www.pi.website/research/knowledge_insulation ; https://arxiv.org/pdf/2505.23705 (Knowledge Insulation — introduced with π0.5+KI; "Stop Gradient" isolates action-expert gradients from the VLM backbone) ; https://website.pi-asset.com/pi06star/PI06_model_card.pdf (π0.6 lineage)
- https://arxiv.org/pdf/2603.03818 (VLAs "resistant to forgetting", secondary/single-source)
- https://arxiv.org/abs/2605.00416 (Learning While Deploying, DIVL + QAM)
- https://arxiv.org/html/2511.19647v1 (Robot-Powered Data Flywheels / Scanford)
- https://arxiv.org/html/2506.17811 (RoboMonkey)
- https://arxiv.org/html/2606.27268v1 (E-TTS)
- https://arxiv.org/pdf/2602.07845 (Recurrent-Depth VLA)
- https://arxiv.org/html/2506.01953v1 (Fast-in-Slow) + dual-system VLA literature
- https://blogs.nvidia.com/blog/jetson-thor-physical-ai-edge/ ; https://developer.nvidia.com/blog/introducing-nvidia-jetson-thor-the-ultimate-platform-for-physical-ai
- https://www.therobotreport.com/teleop-not-autonomy-the-path-for-1x-neo-humanoid/ ; https://www.engadget.com/ai/1x-neo-is-a-20000-home-robot-that-will-learn-chores-via-teleoperation-040252200.html
- https://www.figure.ai/news/helix ; https://www.figure.ai/news/helix-logistics
- https://www.roboticscenter.ai/learn/remote-robot-fleet-management-guide ; https://arxiv.org/pdf/2605.28097 (ICAN-Deploy)
