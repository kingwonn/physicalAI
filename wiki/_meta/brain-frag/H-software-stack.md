## 软件栈 & 运行时 (Software Stack & Runtime)

> There is **no standard "robot brain OS."** The de-facto stack is a two-tier split — a Linux+PREEMPT_RT (or vendor RTOS-augmented Linux) host running perception/planning/VLA inference, plus a bare-metal MCU/RTOS owning the hard-real-time motor loop — glued together by ROS 2 (soft-real-time middleware) and per-vendor accelerator runtimes (TensorRT / QNN / BPU toolchains) that are **not portable across silicon**. Every vendor stitches its own; portability is paid for in re-ports.

### OS 层:实时性 (Real-time OS layer)

- **PREEMPT_RT merged into mainline Linux only in kernel 6.12** (final enabling commit merged Sept 20 2024; 6.12 released Nov 2024), ending a ~20-year (rt-patch work from c.2004) out-of-tree existence; final printk PR presented to Linus Torvalds at Sept 2024 Open Source Summit Europe (Vienna); real-time support enabled first on x86 / x86_64, ARM64, RISC-V. (primary)
  - Consequence for robot brains: before 6.12, *every* "real-time Linux" stack (Jetson/Ubuntu included) needed a separately-applied out-of-tree patch series, versioned per kernel and often lagging vendor BSPs by months — a recurring integration tax. (primary)
- **PREEMPT_RT is still only *soft* real-time.** The dominant pattern splits work: Ubuntu (typically 22.04) on the AI SoC for perception/planning/VLA; a **dedicated MCU/RTOS** for the sub-millisecond torque/servo loop, because standard Linux cannot give *hard* guarantees at those rates. (secondary)
- **RT-kernel does measurably help ROS 2**: a controlled benchmark (CJME/Springer) found PREEMPT_RT-Linux-ROS2 yields substantially smaller and less-variable max latency across message payload sizes vs. a stock non-RT kernel — the standard justification for pairing ROS 2 with an RT kernel on robot SoCs. (secondary)

### 中间件:ROS 2 仍是软实时 (Middleware — ROS 2 remains soft-RT)

- ROS 2's real-time story is **fundamentally probabilistic/soft, not hard**. As of 2025–2026, academic work is still *characterizing* (not solving) executor/DDS worst-case latency: e.g. *A Survey of Real-Time Support… in ROS 2* (arXiv 2601.10722), *ReDAG-RT* multi-DAG scheduling (arXiv 2603.18238), *Probabilistic Latency Analysis of DDS in ROS 2* (arXiv 2508.10413). (primary)
- **Discovery scales poorly** with node count under default DDS/RTPS. `rmw_zenoh` (Zenoh-based) cuts discovery time by **up to 99.97%** vs. default DDS discovery — relevant to boot-time discovery on multi-node on-device brains; PX4 also supports `rmw_zenoh` as a uORB→ROS 2 bridge. (secondary)
- **Zero-copy for GPU-heavy pipelines — Isaac ROS NITROS**: passes GPU memory handles between nodes (type adaptation REP-2007 / negotiation REP-2009) instead of serializing full image/tensor payloads, avoiding CPU↔GPU copies. **Caveat (verified against docs): zero-copy holds only when all NITROS nodes run in the *same process*.** (primary)

### 推理运行时 & 硬件分层 (Inference runtime & hardware tiering)

Per-vendor runtimes are the robot-brain analog of a "CUDA moment" — and they do **not** interoperate (a Jetson engine ≠ a D-Robotics BPU model ≠ a Qualcomm QNN graph).

| Runtime | Silicon / role | Key facts | sq |
|---|---|---|---|
| **TensorRT** | NVIDIA Jetson/RTX/H100 | GPU-arch-specific engines (non-portable across archs) | primary |
| **TensorRT Edge-LLM** | Jetson Thor/Orin (JetPack 7.1, 2026) | Python-free C++ LLM/VLM runtime; EAGLE-3 spec-decode, NVFP4, chunked prefill; open-sourced (NVIDIA/TensorRT-Edge-LLM); demoed Cosmos-Reason2-8B (NVFP4, ~4× mem cut) on Thor, Qwen3-4B (INT4 AWQ, ~2GB) on Orin Nano; Bosch/ThunderSoft/MediaTek building on it (CES 2026) | primary |
| **QNN / AI Engine Direct** (QAIRT SDK) | Qualcomm Snapdragon 8 Gen2/3/8 Elite, X-laptops, auto/XR | Supersedes older SNPE; per-operator control across CPU/Adreno GPU/Hexagon NPU | secondary |
| **BPU toolchain** | D-Robotics RDK X5 | Proprietary, parallel to & non-interoperable with TensorRT | primary |

**SoC-vs-model-size tiering (sizing rule of thumb):** (primary)

| SoC | Target model class | Notes |
|---|---|---|
| Jetson AGX Thor 128GB | **20B–120B** (e.g. Llama 3.2 Vision 70B) | flagship humanoid brain |
| Jetson AGX Orin 64GB | **4B–20B** | mainstream |
| D-Robotics RDK X5 | small VLA / classic ROS 2 | Ubuntu 22.04, octa-core A55 "Sunrise 5", **10 TOPS BPU** + 32 GFLOPS GPU; ships "NodeHub" 200+ plug-and-play ROS 2 modules (primary) |
| Qualcomm Snapdragon 8-class | mobile/edge | ~**15 TOPS @ 5–8W** (unverified) |

### VLA 部署:System 1 / System 2 与异步分块 (VLA deployment — S1/S2 split & async chunking)

- **Dual-system is now concrete, not just a metaphor.** GR00T N1 (Mar 2025 paper): System 2 (VLM) at **10Hz** (as reported on an NVIDIA L40), System 1 (Diffusion-Transformer flow-matching action head) at **120Hz**, tightly coupled and jointly trained end-to-end. (secondary)
- **Only the DiT action head is TensorRT-compiled**; VLM backbone (vision encoder + language model) stays in PyTorch. Measured **GR00T-N1.6-3B** DiT speedups (NVIDIA deployment docs; the benchmark table is from the N1.6 release, not the original N1) — engines are GPU-arch-specific ("an engine built on RTX 4090 will not work on H100"): (primary)

| Device | PyTorch | TensorRT | Speedup |
|---|---|---|---|
| RTX 5090 | 58ms / 17.3Hz | 31ms / 32.1Hz | 1.86× |
| H100 | 77ms / 13.0Hz | 36ms / 27.9Hz | 2.14× |
| RTX 4090 | 82ms / 12.2Hz | 43ms / 23.3Hz | 1.92× |
| Jetson Thor | 117ms / 8.6Hz | 92ms / 10.9Hz | 1.27× |
| Jetson Orin | 300ms / 3.3Hz | 173ms / 5.8Hz | 1.73× |

- **Action chunking amortizes latency.** Physical Intelligence **π0** = ~3B PaliGemma VLM + 300M flow-matching "action expert"; runs at **50Hz**, emitting a 50-step chunk (≈1s of control) in one **~73ms** pass on a consumer RTX GPU. (primary)
- **Real-Time Chunking (RTC)** — training-free, any diffusion/flow VLA: predicts the next chunk *while the current one executes*, "freezing" already-committed actions and "inpainting" the rest, blending old/new to kill the "robot idles waiting for next chunk" stall. (primary)
- **LeRobot async-inference** (RobotClient ↔ PolicyServer) is the open reference S1/S2 pattern: knobs `actions_per_chunk` (default 50, typical 10–50) and `chunk_size_threshold` (docs-table default 0.7; 0.5–0.6 recommended — when queue is ≤ that fraction full, send fresh observation); overlaps merged via `aggregate_fn_name=weighted_average`. (primary)
- **Policy memory footprint gates hardware**: **π0 ≈ 14GB** at inference vs. **SmolVLA ≈ 2GB** — the first check when choosing on-device compute (Orin Nano vs AGX) and feasible control fps. (primary)

### 碎片化的证据 (Fragmentation, concretely)

- LeRobot — the "open reference stack" — still needs a **per-vendor porting layer** to run off NVIDIA/Qualcomm silicon: D-Robotics ships **`rdk_LeRobot_tools`**, a dedicated BPU adapter (PyTorch→ONNX→Horizon toolchain→`.hbm`; targets RDK X5 "bayes" and RDK S100 "nash"; **currently verified for ACT policies only**, on S100), and a NodeHub module is not portable to Jetson/Isaac ROS without a re-port. (primary) → Same policy code, N vendor stitch-jobs.

来源:
- https://www.hackster.io/news/linux-can-now-power-real-time-operating-systems-as-the-preempt-rt-patch-set-is-merged-into-mainline-dde8fe8c7308
- https://en.wikipedia.org/wiki/PREEMPT_RT
- https://developer.d-robotics.cc/en/rdkx5
- https://www.cnx-software.com/2025/06/30/d-robotics-rdk-x5-development-board-features-sunrise-x5-octa-core-soc-with-10-tops-bpu-for-ros-projects/
- https://arxiv.org/pdf/2601.10722 ; https://arxiv.org/pdf/2603.18238 ; https://arxiv.org/pdf/2508.10413
- https://cjme.springeropen.com/articles/10.1186/s10033-023-00976-5
- https://github.com/ros2/rmw_zenoh ; https://docs.px4.io/main/en/middleware/zenoh
- https://nvidia-isaac-ros.github.io/concepts/nitros/index.html ; https://developer.nvidia.com/blog/boosting-custom-ros-graphs-using-nvidia-isaac-transport-for-ros
- https://www.jetson-ai-lab.com/tutorials/tensorrt-edge-llm/ ; https://developer.nvidia.com/blog/accelerating-llm-and-vlm-inference-for-automotive-and-robotics-with-nvidia-tensorrt-edge-llm/
- https://developer.nvidia.com/blog/getting-started-with-edge-ai-on-nvidia-jetson-llms-vlms-and-foundation-models-for-robotics/
- https://nvidia-isaac-gr00t.mintlify.app/deployment/tensorrt
- https://arxiv.org/abs/2503.14734
- https://huggingface.co/blog/pi0 ; https://www.cloderic.com/content/2025-02-27-notes-on-pi0
- https://arxiv.org/pdf/2506.07339
- https://huggingface.co/docs/lerobot/async ; https://huggingface.co/papers/2506.01844
- https://docs.qualcomm.com/bundle/publicresource/topics/80-63442-2/setup.html
