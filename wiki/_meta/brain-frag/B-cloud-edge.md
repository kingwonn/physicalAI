## 云边分工 (Cloud vs Edge / Split-Brain)

The central design decision for an on-device embodied brain is **what stays local and what may leave the robot**. The industry has converged on a *layered latency budget* and a *reflex/cognition split* (System 1 / System 2, or "小脑/大脑", cerebellum/brain). The real-time control loop must be local because network round-trips exceed its cycle budget by orders of magnitude; high-level reasoning is cloud-offloadable because it is intermittent and latency-tolerant.

### 1. The latency-budget hierarchy (why the control loop can never leave)

Control layers run at radically different frequencies, and the fastest ones categorically cannot absorb any network round-trip:

| Layer | Frequency | Cycle budget | Must be local? |
|---|---|---|---|
| Low-level joint/torque control | ~1000 Hz (GR1 whole-body torque) | ~1 ms | Yes — sub-ms |
| Whole-body QP / balance control | ~100–200 Hz (QP@100 Hz; REEM-C PC@200 Hz) | 5–10 ms | Yes |
| Inverse kinematics / motion planning | ~30–50 Hz (IK caps ~30 Hz) | 20–33 ms | Yes (reactive) |
| Perception / VLM scene understanding | ~7–9 Hz (Helix S2) | 100+ ms | Edge-preferred |
| Deliberative planning / multi-step reasoning | seconds | 100s ms–s | Cloud-offloadable |

- Anchor comparison: even a *well-optimized teleoperation* channel, **ExtremControl (2026)**, hits only ~**50 ms** end-to-end for direct extremity control over a network link (secondary) — that is already an order of magnitude worse than a local joint-control loop (sub-ms to a few ms), which is precisely why teleop is a *supervisory/fallback* mode, never the primary control loop.
- A general edge-cloud robotics survey frames edge devices for **sub-10 ms** response, with multi-robot edge-resident pipelines demonstrating **<1 ms** (0.001 s) average command-response for the edge portion **(unverified — specific sub-ms figure not reconfirmed in cited surveys)**; cloud is reserved for complex generation/reasoning offload (secondary).

### 2. The cost of pushing large VLAs fully on-device (VLA-Perf, π0 family)

Hard inference numbers show a **100x+** gap between datacenter and edge silicon — the load-bearing evidence that fully-local large VLAs are frequency-limited (primary, VLA-Perf arXiv 2602.18397v1):

| Model | Jetson Thor (edge) | RTX 4090 (consumer) | Datacenter |
|---|---|---|---|
| π0 baseline | 52.57 ms/step (19.0 Hz)* | 31.06 ms (32.2 Hz) | H100 6.15 ms (162.5 Hz); B100 3.18 ms (314.4 Hz); A100 16.20 ms (61.7 Hz) |
| π0-L (9.1B) | 3.9 Hz | 8.0 Hz | — |
| π0-XL (16.7B) | 2.1 Hz | — | — |
| π0-XXL (81.3B) | — | — | B100 9.6 Hz |
| long-context (1K timesteps) | 768.3 ms (1.3 Hz) | — | — |

\*π0 baseline breakdown on Thor: vision enc 6.06 ms + VLM backbone 20.30 ms + action expert 26.20 ms.

- Architecture matters as much as location: **diffusion-based action decoding is 102.4x faster** than vanilla autoregressive with chunking; raising denoising steps 10→50 increases end-to-end latency **2.15x** (primary).
- **Asynchronous inference over 5G + datacenter GPU (B100) yields 5.99x throughput** vs. synchronous cloud inference (primary) — quantifying the payoff of decoupling the async, cloud-offloadable perception/planning path from the synchronous, local action loop.

### 3. Location alone is not the win — model size is (edge-vs-cloud counter-point)

A controlled VLM benchmark on a **Unitree G1-EDU** humanoid (edge node = NVIDIA L4 24 GB, a realistic ORAN/MEC node) shows moving compute to the edge is *not* automatically a big win (primary, arXiv 2601.14921):

| Model | Edge (end-to-end) | Cloud baseline | Δ |
|---|---|---|---|
| LLaMA-3.2-11B-Vision (4-bit NF4) | 1600.03 ms | 1685.20 ms | only ~5% |
| Qwen2-VL-2B | "sub-second" | — | <½ of cloud baseline |

- Text generation dominates **>85%** of latency regardless of location — so a big model gains almost nothing from edge placement; the win comes from a **smaller, quantized** on-device model. Takeaway: pair the split-brain design with a *right-sized* local model, don't just relocate a large one.

### 4. Industry architectures on the cloud-vs-edge spectrum

| System | Split pattern | On-device compute | Cloud role | SQ |
|---|---|---|---|---|
| **Figure Helix** | S2 (7B VLM @7–9 Hz → latent vector) + S1 (80M cross-attn transformer @200 Hz, 35-DoF upper-body) | dual low-power embedded GPUs, model parallelism | **none** — fully onboard, removes "latency and uptime risk of cloud-dependent systems" | primary |
| **Gemini Robotics On-Device** | VLA foundation model run **entirely locally**; adapts w/ 50–100 demos | robot-local | flagship cloud Gemini Robotics kept for SOTA "without on-device limitations" — explicit capability/latency tradeoff | primary |
| **Quectel Robrain (移远 v2.0)** | 端云协同 (edge-cloud collaboration); detects network in real time, dynamically allocates compute; 以端侧为主、云端为辅 | edge-primary; sensitive data local | 云端迭代优化; plugs into Doubao (豆包)/DeepSeek + search when connected | primary (85%-offline figure: secondary) |
| **RoboOS** | "Brain" (cloud reasoning/planning) + "Cerebellum" (on-device reactive control); cross-embodiment, multi-agent | per-robot cerebellum | multi-step reasoning + cross-robot coordination | primary |
| **Tesla Optimus** | vision-only, cloud-independent inference; custom onboard chip (AI5-class for Gen 3, FSD lineage) | custom SoC | none for control loop | **unverified** (enthusiast press; chip name/specs unverified) |
| **1X Neo** | edge autonomy + **remote-human teleop fallback** ("Redwood"), ~60–70% autonomy at launch | onboard | *human operator*, not a bigger cloud model, is the fallback | **unverified** (secondary; outage-safety behavior undocumented) |

- **Robrain** claims **"断网环境下仍维持85%核心功能"** (maintains 85% core functionality when disconnected) (secondary); deployed on LimX Dynamics' TRON 1 bipedal robot. This is the concrete graceful-degradation target for an edge-primary design.
- **Helix data efficiency**: ~**500 hours** of training data — **<5% of the size of previously collected VLA datasets** (a **>95% reduction**), per Figure's own post (primary) — with no multi-embodiment collection or multi-stage training; evidence that the S1/S2 split (small reactive net conditioned by a pretrained VLM) is more data-efficient than a monolithic on-device giant, favoring hybrid over monolithic.
- **Gemini Robotics On-Device** outperforms the prior best on-device VLA on out-of-distribution tasks and multi-step instructions, running dexterous bimanual tasks (unzipping bags, folding clothes) fully local (primary) — the on-device capability gap is closing.

### 5. On-device compute anchor (2025–2026)

- **NVIDIA Jetson Thor (Blackwell)** — the reference platform many humanoid makers (Boston Dynamics Atlas, Agility Digit gen-6) are adopting: up to **2,070 FP4 TFLOPS**, **128 GB** memory, **40–130 W**, ~273 GB/s bandwidth; 2,560 CUDA cores, 96 5th-gen Tensor Cores, 14-core Arm Neoverse-V3AE (primary). That is **7.5x the AI perf and 3.5x the power efficiency** of AGX Orin — orders of magnitude below B100/H100, but enough to run a 7–9B VLM backbone at single-digit-to-tens of Hz **plus** a small action-expert net at 100–200 Hz. This is exactly the compute envelope Helix-style S1/S2 splits are engineered for.

### 6. The general CS trend

- Splitwise-style edge-cloud LLM collaborative-inference research frames the split at the **token/layer level** using Lyapunov-optimization-based RL to meet latency SLAs dynamically per network conditions (primary/secondary) — the non-robotics analog of Robrain's real-time network-aware compute allocation. Expect robot brains to adopt the same dynamic, SLA-driven splitting rather than a static edge/cloud boundary.

### Design takeaways

- **Never** route the ≥100 Hz reactive/balance loop through the network — reserve the edge for it unconditionally.
- Split at the **System 1 / System 2** boundary: fast local action net, latency-tolerant VLM/planner (local-preferred, cloud-offloadable).
- Right-size the local model (quantize, distill) — edge placement of a large model buys almost nothing (§3).
- Design an explicit **degradation ladder**: full cloud reasoning → local VLM → reflex-only autonomy → human teleop (1X pattern) → safe-stop.
- Target a concrete offline floor (Robrain's 85%) and treat cloud as *iterative optimization*, not a dependency.

来源:
- https://deepmind.google/blog/gemini-robotics-on-device-brings-ai-to-local-robotic-devices/
- https://www.figure.ai/news/helix
- https://www.quectel.com.cn/news-and-pr/robrain-v2-0
- https://www.quectel.com.cn/news-and-pr/%E5%90%AC%E5%BE%97%E8%A7%81%E3%80%81%E6%83%B3%E5%BE%97%E9%80%9A%E3%80%81%E5%81%9A%E5%BE%97%E5%88%B0%EF%BC%9A%E7%A7%BB%E8%BF%9C%E9%80%9A%E4%BF%A1%E6%90%BA%E6%89%8B%E9%80%90%E9%99%85%E5%8A%A8%E5%8A%9B
- https://arxiv.org/html/2602.18397v1
- https://arxiv.org/html/2601.14921
- https://arxiv.org/pdf/2505.03673
- https://arxiv.org/pdf/2507.16731
- https://extremcontrol.github.io/ ; https://arxiv.org/html/2602.11321v2
- https://www.nvidia.com/en-us/autonomous-machines/embedded-systems/jetson-thor/ ; https://blogs.nvidia.com/blog/jetson-thor-physical-ai-edge/
- https://aiweekly.co/alerts/figure-ai-helix-02-runs-200-hours-sorts-149K-packages
- https://robotwale.com/article/tesla-optimus-14 ; https://optimusk.blog/blog/what-is-tesla-optimus/ (secondary/enthusiast, unverified)
- https://www.humanoidsdaily.com/news/1x-neo-launch-sparks-debate-on-autonomy-and-teleoperation ; https://www.therobotreport.com/teleop-not-autonomy-the-path-for-1x-neo-humanoid/ (unverified)
