## 为端侧而生的模型 (Models Built for On-Device)

上一节讲优化手段;本节盘点**为端侧设计/部署的 VLA 模型本身**——谁真能在机器人自带的芯片上离线跑,跑到多少 Hz。核心分野:**端侧原生模型 (edge-native)**(Octo/SmolVLA/TinyVLA/LiteVLA-Edge/BitVLA、以及厂商随机部署的 Helix/GR00T/π0.5/GR-3)vs. **端侧勉强 (server-bound)** 模型(OpenVLA-7B、原生 π0——文献称量化后仍需一台协同服务器,而非真正跑在 Jetson 级边缘)(secondary,建议对照 OpenVLA/π0 原文核实)。

### 1. 参考硬件:Jetson Thor (Reference Edge SoC)

GR00T N1.5/N1.6/N1.7 与 π0.5 端侧部署的公开基准几乎都跑在同一颗芯片上,先立标尺 (primary):

- Blackwell 级 GPU,原生 **FP4** 量化 + Transformer Engine 动态 FP4/FP8 切换;峰值 **2070 FP4 TFLOPS**。
- **128GB** 统一 LPDDR5x 内存,带宽 **273GB/s**;14 核 Arm Neoverse-V3AE CPU;可配 **40–130W**。
- 对比上代 Jetson AGX Orin:**7.5x** AI 算力、**3.5x** 能效。NVIDIA 的 Isaac GR00T Reference Humanoid 用它配 Unitree H2 Plus 本体。

### 2. 端侧模型全景 (The On-Device Model Roster)

| 模型 (Model) | 参数 | 骨干/架构 | 目标芯片 | 最佳公开 Hz(芯片) | 源 |
|---|---|---|---|---|---|
| Figure **Helix S1** | 80M | visuomotor policy | 板载嵌入式双 GPU | **200Hz**(onboard) | primary |
| Figure **Helix S2** | 7B | 互联网预训练 VLM | 同上 | 7–9Hz(onboard) | primary |
| **GR00T-N1.6-3B** | 3B | VLM + DiT 动作头 | Jetson Thor | 10.9Hz(TensorRT 现货)/ 22–24Hz(手写 CUDA) | primary |
| **π0.5** | ~3B | PaliGemma 系 | Jetson Thor | ~10–11Hz(TensorRT+NVFP4)/ 23Hz(手写 CUDA) | primary |
| **π0** | ~3B | PaliGemma | Jetson Thor | 22Hz(手写 CUDA) | primary |
| **π0-small** | 470M | 跳过 VLM 初始化 | 轻/边缘定位 | 未公布板载 Hz | primary |
| **SmolVLA** | 450M | SmolVLM(层跳过)+ 异步 | 消费级 GPU/CPU/MacBook | 15–30Hz(RTX 4090,非嵌入式) | primary |
| **LiteVLA-Edge** | 256M | SmolVLM-256M,Q4_K_M 4-bit | Jetson AGX Orin | **6.6Hz**(150.5ms,全离线) | primary |
| **BitVLA** | ~2B | BitNet b1.58(三值 {-1,0,1}) | 通用(1-bit) | 未公布板载 Hz(见下) | primary |
| **TinyVLA(-H)** | 70M–1.4B | Pythia + 扩散 policy 解码 | 边缘定位 | 未公布板载 Hz | primary |
| **Octo** | 93M | — | Jetson AGX Orin | 唯一"无需额外优化即可舒适运行" | secondary |
| ByteDance **GR-3** | 4B | Qwen2.5-VL-3B + DiT(MoT,flow-matching) | 机器人自带 NUC(ByteMini) | 延迟/Hz **未公布** | primary |
| AgiBot **GO-1** | — | Genie Operator-1 | 未公布边缘芯片 | 30Hz(训练/评测率,非板载) | unverified |
| Gemini Robotics **On-Device** | 未披露 | DeepMind VLA | 机器人本体(离线) | 未公布 Hz(见下) | primary |

### 3. 三种"为端侧而生"的路线 (Three Design Routes)

**A. 厂商随机随芯片交付(硬件-模型捆绑)**

- **Figure Helix**(primary):整套双系统 VLA 全部**板载、零云依赖**、跑在嵌入式低功耗 GPU 上。S2(7B VLM)7–9Hz 做场景/语言理解与目标序列;S1(80M)**200Hz** 把 S2 的 latent 转成 35-DoF(含手指)连续关节指令。~500 小时遥操数据训练;是首个给人形上半身(含手指)全连续控制、且**同一份权重同时跑两台机器人**的 VLA,展示行为无需任务级微调。**200Hz 反射环 vs. 单位数~30Hz 的 VLM 推理环差一个数量级——这正是双系统 (System1/System2) 架构的核心工程理由。**
- **Gemini Robotics On-Device**(primary,2025-06-24):DeepMind 首个开放**本地微调**的 VLA,**完全离线跑在机器人硬件上、无网络依赖**(官方称对延迟敏感、间歇/零连接场景有用)。用 Gemini Robotics SDK(基于 MuJoCo)**仅需 50–100 条演示**即可微调;在 ALOHA(主训)、Franka FR3 双臂、Apptronik Apollo 人形上测试,官方声称在 7 项灵巧任务(拉拉链、发牌、装午餐盒等)分布外(OOD)基准上超越同类端侧模型。**注:官方博客未给出具体数值成功率(仅对比图)——"7 项任务 >60% 平均成功率" 无法在一手来源核实,标 (unverified)。参数量 Google 未披露**——横比时是空洞。
- **ByteDance GR-3**(primary):4B,Qwen2.5-VL-3B-Instruct 骨干 + 扩散-transformer 动作头(mixture-of-transformers,flow-matching);部署在**机器人自带 NUC**(ByteMini 平台)而非云。三类数据协同训练(视觉-语言 / 机器人轨迹 / 人类轨迹),强少样本适应与长时程灵巧任务声明。**推理延迟/Hz 技术报告未披露**——相对 GR00T/π0 已公布的 TensorRT 数字是明显缺口。
- **AgiBot GO-1**(unverified):以 AgiBot World 数据集的采集率 **30Hz** 原生训练/评测(本体感知、关节/末端位姿、图像均 30Hz 记录)。但**未公布专门的边缘芯片目标或板载 Hz/延迟**——GO-1 的 30Hz 是训练/评测控制频率,**不能等同真机板载性能**,应标 (unverified)。

**B. 端侧原生小模型(下探到 <500M 甚至 <100M)**

- **SmolVLA**(HF/LeRobot,450M)(primary):**纯社区数据**训练——Hugging Face 上 487 个 LeRobot 标注数据集共 **10M 帧**。VLM 骨干**层跳过 (layer-skipping)** + **异步推理**(当前动作块执行时预算下一块)带来响应快 30%、任务吞吐 2x。单张 RTX 4090 上 15–30Hz;小到能跑 CPU 甚至 MacBook,单张消费级 GPU 可训。
- **TinyVLA**(70M–1.4B,Pythia 骨干)(primary):**TinyVLA-H 成功率超 OpenVLA 25.7%、参数少 5.5x**。LoRA 微调(可训参仅占 5%),扩散 policy 解码器经线性投影挂到冻结的预训练多模态骨干上;定位快速、数据高效,低端 70M 远在 SmolVLA 的 450M 地板之下。
- **LiteVLA-Edge**(arXiv 2603.03380)(primary):**Jetson AGX Orin 上全离线**,256M SmolVLM 骨干经 **Q4_K_M 4-bit GGUF** 量化(llama.cpp CUDA 后端)。平均延迟 **150.5ms ≈ 6.6Hz**,在 ROS2 感知-推理-动作闭环里跑,输出 `geometry_msgs/Twist`。**明确定位为纯端侧(无云回退)**,以此对照它所说"OpenVLA/π0 边缘用需要一台服务器"。
- **Octo**(93M)(secondary):被引为"当前唯一无需额外优化即可在 Jetson AGX Orin 上舒适运行的基础模型",反衬 OpenVLA/π0(3B–7B)一代与真·端侧原生(Octo/SmolVLA/TinyVLA/LiteVLA-Edge/BitVLA)之间的体量鸿沟。

**C. 极致量化路线(1-bit 原生)**

- **BitVLA**(arXiv 2506.07530)(primary):**全原生 1-bit(三值 {-1,0,1})** VLA,建于 BitNet b1.58 2B4T。三段管线:(1) 多模态 1-bit 预训练 →(2) "Quantize-then-Distill" 把视觉编码器压到 1.58-bit 权重 →(3) 机器人适配训练。**~11x 显存↓、端到端 4.4x 加速**,而在 sim 基准与真机任务上**持平全精度 OpenVLA-OFT**;部分对比称可达 32x 模型压缩。代码/权重公开(CC-BY-4.0,GitHub ustcwhy/BitVLA)。**板载具体 Hz 未公布**,但它是本轮"内存下限"最激进的答案。

### 4. π0 家族的端侧成员 (The π0-Family Edge Members)

- **π0-small(470M)**(primary):**跳过 VLM 预训练/初始化**,是原 π0 论文里对照 ~3B 全 π0(建于 PaliGemma)的轻量/边缘定位消融成员。openpi 开源库在 JAX/Flax 与 PyTorch 上实现了 π0、π0-FAST、π0.5。
- **π0.5 于 Jetson AGX Thor**(primary):TensorRT + NVFP4 量化把 ~163ms(PyTorch BF16)降到 **~94ms 总 / ~90ms 纯模型**(TensorRT FP8+NVFP4),**1.73x** 加速 ≈ **10–11Hz** 端到端。而社区论坛用**手写 CUDA kernel**(非官方 TensorRT 路径)报到 **23Hz(44ms)**——官方与手搓路径存在巨大优化落差。
- **GR00T-N1.6-3B 的 TensorRT 分层真相**(primary):Jetson Thor 端到端 92ms / **10.9Hz**,对 PyTorch 仅 **1.27x**——是全表最差加速比(RTX 5090 1.86x、H100 2.14x、RTX 4090 1.92x、Orin 1.73x)。原因:**只有 DiT 动作头拿到 TensorRT 大头(Action Head 3.59x)**,视觉编码器/LLM 仍留在 PyTorch;TensorRT engine 还**绑 GPU 架构,换芯片必须重编**。绕开 TensorRT 的 Q/DQ 开销、用手写 CUDA kernel,Thor 才升到 **22–24Hz**。

### 端侧选型要点 (Selection Takeaways)

1. **先分"原生"还是"server-bound"**:OpenVLA-7B/原生 π0 即便量化,文献仍说需协同服务器;真上机器人自带芯片选 Octo/SmolVLA/TinyVLA/LiteVLA-Edge/BitVLA,或厂商捆绑的 Helix/GR00T/π0.5/GR-3。
2. **官方数字 ≠ 可达上限**:Thor 上 GR00T 10.9Hz(TensorRT)vs. 22–24Hz(手写 CUDA)、π0.5 10–11Hz vs. 23Hz——官方/手搓落差常达 2x,预算频率要给手工优化留空间。
3. **警惕"训练率冒充板载率"**:GO-1 的 30Hz、GR-3 未公布 Hz——训练/评测频率不是真机端到端性能。
4. **反射环与推理环分层**:Helix S1 200Hz vs. S2 7–9Hz 差一个量级,这是双系统架构存在的根本原因,单模型很难同时满足两端。

来源:
- Gemini Robotics On-Device — deepmind.google/blog/gemini-robotics-on-device-brings-ai-to-local-robotic-devices
- NVIDIA GR00T TensorRT 基准 — nvidia-isaac-gr00t.mintlify.app/deployment/tensorrt
- NVIDIA 开发者论坛(Thor/RTX 手写 CUDA)— forums.developer.nvidia.com/t/real-time-inference-on-thor-rtx-pi0-5-gr00t-n1-6-1-7-.../368788
- NVIDIA Jetson Thor — developer.nvidia.com/blog/introducing-nvidia-jetson-thor-the-ultimate-platform-for-physical-ai
- Figure Helix — figure.ai/news/helix
- π0 论文 — arxiv.org/html/2410.24164v1 ; openpi — github.com/Physical-Intelligence/openpi
- π0.5 on Thor — jetson-ai-lab.com/tutorials/openpi_on_thor
- SmolVLA — huggingface.co/blog/smolvla
- LiteVLA-Edge — arxiv.org/abs/2603.03380
- BitVLA — arxiv.org/abs/2506.07530
- TinyVLA — arxiv.org/abs/2409.12514
- Foundation Models for Robot Manipulation 2025(secondary 聚合)— roboticscenter.ai/research/foundation-models-robot-manipulation-2025
- ByteDance GR-3 — arxiv.org/html/2507.15493
- AgiBot World Colosseo / GO-1 — arxiv.org/abs/2503.06669
