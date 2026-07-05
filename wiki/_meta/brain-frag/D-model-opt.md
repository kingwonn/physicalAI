## 面向端侧的模型优化 (Model Optimization for Edge)

端侧具身大脑的核心矛盾:VLA (Vision-Language-Action) 模型要在受限的算力/内存/功耗预算内跑到可用的控制频率。四条主线撑起全部优化空间——**动作头架构 (action-head architecture)**、**动作分块 (action chunking)**、**量化 (quantization)**、**异步/协同推理 (async / collaborative inference)**。以下数字大量来自 NVIDIA 的 VLA-Perf 基准 (arXiv 2602.18397),这是目前唯一横跨嵌入式→数据中心硬件的公开 VLA 延迟基准。

### 1. 动作头架构:扩散/流匹配 vs. 自回归 (Action Head: Diffusion/Flow vs. Autoregressive)

- 最大的单点杠杆。自回归 VLA 逐维生成动作 token(14-DoF × chunk 50 ≈ **700 个串行 decode 步**),扩散/流匹配一次性预测整个 chunk,只需固定的少量去噪 pass。
- VLA-Perf 在 NVIDIA B100 上:50-action chunk,标准扩散头 **3.2ms** 端到端 vs. 经典自回归 decode **327.6ms** → **102.4x 加速** (primary)。
- 去噪步数是**次要成本**:B100 上 10 步 = 3.2ms,步数从 10→50(×5)端到端延迟仅 ×2.15(≈6.9ms);transformer 前向传播才是主导项 (primary)。
- 因此**动作头类型 >> 去噪步数 >> chunk 大小**,这是端侧优化的优先级排序(综合 VLA-Perf 分项结论——chunk 影响可忽略、去噪步影响显著、头类型 102x——的推论,论文未直接给出此排序)。

### 2. 硬件层与模型大小的延迟曲线 (Hardware Tier & Model-Size Latency Curve)

π0 (2.7B) 同一模型跨硬件(VLA-Perf,均为短上下文,primary;注:VLA-Perf 将 π0 计为 2.7B = SigLIP-So 0.4B + Gemma-2B 2.0B + Act-M 0.3B,Physical Intelligence 原论文计为 ~3.3B,因把 PaliGemma 整体计为 ~3B——数字差异源于计数口径,非矛盾):

| 硬件 (Hardware) | 端到端延迟 | 频率 | 层级 |
|---|---|---|---|
| Jetson Thor | 52.57ms | 19.0 Hz | 嵌入式端侧 |
| RTX 4090 | 31.06ms | 32.2 Hz | 消费级 |
| A100 | 16.20ms | 61.7 Hz | 数据中心 |
| H100 | 6.15ms | 162.5 Hz | 数据中心 |
| B100 | 3.18ms | 314.4 Hz | 数据中心 |

嵌入式↔数据中心存在 **>16x** 差距。模型大小近似线性缩放频率(B100,同族,primary):

| 模型 | 参数 | 频率 (B100) |
|---|---|---|
| π0 | 2.7B | 314.4 Hz |
| π0-L | 9.1B | 73.6 Hz |
| π0-XL | 16.7B | 39.7 Hz |
| π0-XXL | 81.3B | 9.6 Hz |

- **KV-cache 才是长时程杀手** (primary):1,000 步累积上下文(13.2GB KV cache)时,Jetson Thor 从 19Hz 跌到 **768.3ms (1.3Hz)**,RTX 4090 跌到 900.6ms (1.1Hz),连 B100 也只剩 85.2ms (11.7Hz)。端侧在短上下文领先、长上下文崩溃——因为 Thor 的算力/带宽无法摊薄增长的 cache。端侧设计必须**限制上下文窗口 / 定期清 cache**,不能靠堆历史。

### 3. 动作分块:最省力的延迟隐藏 (Action Chunking)

- **predict-H, execute-open-loop** 是所有现代 VLA 共用的头号延迟隐藏手段 (primary)。chunk 成本**次线性**:VLA-Perf 测得 chunk 50→250(×5)端到端延迟仅 +11%——放大开环 chunk 是"廉价换吞吐"的旋钮(牺牲反应性换频率)。
- 各模型 H 取值差异巨大,反映不同的反应性/吞吐权衡:

| 模型 | H (chunk) | 去噪步数 K | 输出率 |
|---|---|---|---|
| π0 (3.3B) | 50 | 10 (δ=0.1) | 20Hz(臂)~50Hz(移动) |
| GR00T N1 (2.2B) | 16 | 4 (K) | 120Hz(System 1)/10Hz(System 2) |
| SmolVLA (~450M) | 显式 async chunk | flow-matching | 提升控制率 |

### 4. 端侧代表 VLA:小模型 + 扩散/流头 (Edge-Class VLAs)

- **π0 (Physical Intelligence, 3.3B)** (primary):PaliGemma VLM (~3B) + 从零训练的 action expert (~300M);流匹配用 linear-Gaussian 概率路径 + Beta 时间步采样,**仅 10 积分步** vs. 扩散常需数百步(流匹配学到更平滑的 ODE 向量场)。RTX 4090 板载分解:图像编码 14ms + observation 前向 32ms + 10× action 前向 27ms = **73ms**(离板含 WiFi 86ms)。
- **π0-small (470M)** (primary):DistilBERT + ViT + DiT,**无 VLM 初始化**的消融——π0 (VLM 初始化) 显著胜出,尤其细粒度语言跟随任务,证明互联网级 VLM 预训练能有效迁移到动作生成(不只是参数量)。
- **SmolVLA (HF LeRobot, ~450M)** (primary):SmolVLM-2 骨干 + flow-matching action expert (~100M);单 GPU 训练,交错 cross/self-attention,含 async 推理栈解耦感知/规划与执行。**~78.3% 真机平均成功率**,号称可比 10x 大的 VLA。可跑消费级 GPU 甚至 CPU。
- **TinyVLA (<1B backbone)** (primary):在小型高速多模态骨干上挂扩散 policy decoder,**跳过大规模机器人预训练**。MetaWorld sim +21.5%,真机比 OpenVLA (7B) 高 **25.7%**,且更快——小扩散头 VLA 在速度和精度上双杀更大的自回归模型。
- **GR00T N1 (NVIDIA, 2.2B)** (primary):Eagle-2 VLM = 1.34B(System 2,10Hz 推理)+ DiT flow-matching policy(System 1,120Hz);**仅 K=4 去噪步**、H=16。L40 GPU bf16 采样 16-action chunk = **63.9ms**(以上均经 arXiv 2503.14734 逐项核实)。扩散头额外去噪缓冲显存 **~4–6GB**(unverified)——GR00T N1 与 VLA-Perf 原文均未给出该 GB 区间,系推测数字。

### 5. 量化:从 INT8 到 1-bit (Quantization)

| 方案 | 显存 | 性能损失 | 备注 |
|---|---|---|---|
| OpenVLA-7B INT8 (secondary) | 14GB→~7GB | <5% | 自回归仍慢 |
| OpenVLA-7B INT4 (secondary) | →~3.5GB | 8–12% | 损失大于 OFT 变体 |
| OpenVLA bf16 vs INT4 (secondary) | — | — | ~500ms/action (A100) → INT4 仍 ~100–200ms |
| Llama-3.2-11B-Vision NF4 (primary) | 20GB→6.5GB | 近云端精度 | Unitree G1-EDU 边缘部署;VLM 非 VLA |
| **BitVLA 1-bit/ternary** (primary) | **11x↓** | 持平 4-bit OpenVLA-OFT | 4.4x 延迟↓,仅用 29.8% 显存 |

- 关键结论:**量化改善内存/精度,但改不了架构瓶颈** (secondary)。OpenVLA 即使 INT4 仍 ~100–200ms/action,远高于扩散/流 VLA 的个位数 ms——自回归逐 token decode 是结构性瓶颈,不是精度问题。
- **BitVLA** (primary) 是本轮研究最激进点:基于 BitNet b1.58 2B4T(权重∈{-1,0,1})+ "Quantize-then-Distill" 把视觉编码器压到 1.58-bit(全精度 teacher 对齐表征),**11.0x 显存↓ + 4.4x 端到端延迟↓** vs. 全精度 OpenVLA-OFT,精度持平 4-bit PTQ 基线而仅用其 29.8% 显存。

### 6. 异步与协同推理 (Async & Collaborative Inference)

- 独立 async(System-2 限 10Hz)在 **5G 网络**上(VLA-Perf Table 8,B100):**async 215.3Hz vs sync 35.9Hz = 5.99x** (primary)。异步解耦(慢规划 / 快执行)是端侧提频的正解。
- **但纯设备-服务器卸载是净亏损** (primary):服务端协同加速随网络递减——Ethernet 10G **2.24x**、WiFi 7 1.26x、5G 仅 1.05x(VLA-Perf Table 9,B100+10Hz cap);而 KV-cache 下载开销 Eth 10G 12.4ms / WiFi7 43.7ms / **5G 257.7ms**。原文结论:协同推理**总是慢于纯服务端推理**,且除快速有线网(Eth 10G)外通常也慢于纯设备推理。→ 端侧要么全本地异步,要么全云端,**"半卸载"往往最差**。

### 7. 端侧硬件的营销 vs. 实测 (Vendor Claims vs. Measured)

- **NVIDIA Jetson Thor** (secondary):Blackwell GPU,128GB LPDDR5X 统一内存,2070 FP4 TFLOPS,40–130W;NVIDIA 官方博客/产品页仅明确宣称"生成式 AI 较 Jetson Orin 提速最高 5x"(2070 TFLOPS、128GB、40–130W 均已核实)。**"120 action tokens/sec 用于 π0.5 类 VLA"这一具体营销值未能在 NVIDIA 官方博客或产品页找到 (unverified)**——引用需谨慎;AGX Orin 的"275 TOPS INT8 / 60W"来自 Orin spec sheet(该博客未给 Orin 绝对 TOPS)。无论如何,VLA-Perf 独立实测同级 π0 (2.7B) 在 Thor 上仅 **19Hz / 52.57ms**——独立端到端实测远低于任何峰值/token-rate 宣称,端侧选型别信 spec sheet 峰值。
- **Quectel SP895BD-AP 模组(CES 2026,2026-01-05 发布)** (unverified):Qualcomm Dragonwing Q-8750 SoC(3nm,8 核 Oryon),支持 INT4/INT8/INT16/FP16;NPU 口径不一——Qualcomm 官方称"最高 **77 TOPS** 密集 AI 算力",Quectel/CNX 报道则称"**80 TOPS** NPU"(约差 3 TOPS),声称"支持端侧运行最高 **110 亿参数** LLM"(此点两家一致)。**无任何 11B 实跑 accuracy/Hz**,非 VLA 专用基准——纯厂商声明,谨慎引用。

### 端侧优化决策清单 (Edge Optimization Checklist)

1. **先选扩散/流动作头**(~100x 杠杆),自回归只在必须逐 token 输出时用。
2. **动作头类型 > 去噪步数 > chunk 大小**:去噪步 10 通常够,chunk 可大(次线性成本)。
3. **限制上下文/清 KV-cache**:长时程 cache 是端侧真正的墙,不是模型大小。
4. **量化到内存预算**:BitVLA 1-bit 是激进上限;但别指望量化解决自回归慢。
5. **异步全本地,或全云端**;避开半卸载(传输开销吃掉收益)。
6. **选型看实测不看峰值 TOPS**:Thor 端到端实测仅 19Hz(52.57ms),远低于任何峰值 TFLOPS / token-rate 营销宣称。

来源:
- VLA-Perf: How Fast Can I Run My VLA? — arXiv 2602.18397 / github.com/NVlabs/vla-perf
- π0: A Vision-Language-Action Flow Model — arXiv 2410.24164 / pi.website/blog/pi0
- SmolVLA — arXiv 2506.01844 / huggingface.co/lerobot/smolvla_base
- TinyVLA — arXiv 2409.12514
- GR00T N1 — arXiv 2503.14734
- OpenVLA — arXiv 2406.09246
- BitVLA — arXiv 2506.07530
- Vision-Language Models on the Edge for Real-Time Robotic Perception — arXiv 2601.14921
- Quectel SP895BD-AP — quectel.com/product/sp895bd-ap-smart-module / iotbusinessnews.com (2026-01) / cnx-software.com (2026-01)
- NVIDIA Jetson Thor — NVIDIA 产品页 + developer blog "Introducing NVIDIA Jetson Thor"
