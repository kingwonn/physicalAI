---
title: "如何在端侧做好具身智能大脑 (Building a Good On-Device Embodied-AI Brain)"
slug: on-device-brain
updated: 2026-07-05
confidence: verified
lang: zh
source: ../wiki/on-device-brain.md
---
> 深度技术+战略调查:一个跑在机器人**机身上(on-device / edge)** 的具身智能"大脑"要怎么设计才算做好?本页由一个 6 轮研究循环(每个子课题经 Sonnet 采集 → Opus 写作 → Opus 对抗核查,数字全部对准 arXiv / 官方规格一手源)建成,覆盖架构、云边分工、算力需求、模型优化、实时控制切分、SoC 版图、功耗散热、软件栈、端侧模型、端侧学习、评价判据、参考架构。**四条收官结论**:(1) 架构已收敛为**双/三系统**——慢的深思 System 2(VLM,5–10 Hz)+ 快的反应 System 1(视觉运动策略,100–200 Hz)+ 硬实时 System 0(电机/反射环,500 Hz–1 kHz 在 MCU 上),跨"富 SoC + 确定性 MCU"切分。(2) 实时控制与安全环**必须在端侧**(Linux+GPU 栈给不出 µs–ms 确定性;断网机器人不能停),重推理可"云边混合"。(3) **算力已基本不是瓶颈**——Jetson Thor 2,070 FP4 TFLOPS、量化(INT4/FP4)、动作分块(action chunking)、小型 VLA 已把端侧推理压到可用频率;真正卡住的是**可靠性(9 个 9)与泛化**,不是 FLOPS。(4) 对模组厂(移远式)的读数:**端侧大脑(算力+连接模组)是可防御的军火商赛道**——机电 BOM([零部件供应链](component-supply-chain.md))十年护城河进不去,而真正的威胁是高通/NVIDIA 芯片原厂**越过模组商直供整机**([友商全景](odm-competitors.md))。

配套阅读:[VLA 模型](vla-models.md)、[硬件底座](hardware.md)、[NVIDIA 机器人栈](company-nvidia.md)、[零部件供应链](component-supply-chain.md)、[评测与基准](evaluation.md)、[开放问题](open-problems.md)、[移远 pitch](../pitch/quectel.md)、[ODM 机会图谱](odm-opportunity.md)。

方法与证据说明:本页每个 section 由独立研究+对抗核查产出;所有关键数字(Hz、TOPS、ms、参数量)在核查阶段逐条对准一手源(arXiv 论文、NVIDIA/高通/Figure/DeepMind 官方规格与博客);单源/未证实项在正文显式标注 `(unverified)`/`(secondary)`。一手源标 `(primary)`。构建循环日志见 [on-device-brain-plan](_meta/on-device-brain-plan.md) 与 [loop-log](_meta/loop-log.md) 的 `loop(brain-N)` 条目。

---

## 阅读导航 (Reading guide)

| # | Section | 一句话 |
|---|---|---|
| A | 架构基础与双系统 | S2 慢而通用 + S1 快而专;为何单一模型不能又聪明又快 |
| B | 云边分工 | 什么必须本地(实时/安全)、什么可上云;云边混合 |
| C | 端侧算力需求 | 跑一个 VLA 到可用频率要多少 TOPS + 内存带宽;VLA-Perf 实测阶梯 |
| D | 面向端侧的模型优化 | 量化/蒸馏/动作头选择;扩散比自回归快 ~100x;动作分块藏延迟 |
| E | 实时控制的切分 | AI 脑 + MCU 脊髓;确定性/安全为何必须分层 |
| F | SoC / 硬件版图 | Jetson Thor / 高通 / D-Robotics / Tesla AI5 分档 |
| G | 功耗/散热/成本 | ~2kWh 移动电源约束;TOPS/W 才是真指标 |
| H | 软件栈与运行时 | Ubuntu+PREEMPT_RT+ROS2+TensorRT/QNN;尚无标准"机器人脑 OS" |
| I | 为端侧而生的模型 | Gemini On-Device / GR00T N1.6 / Helix / SmolVLA / LiteVLA / BitVLA |
| J | 端侧学习与数据飞轮 | 云训练+端适配;车队数据飞轮;OTA;测试时算力 |
| K | "做好"的判据与评价 | 延迟/泛化/可靠性/功耗/成本/可更新的评分标尺 |
| L | 参考架构与模组厂视角 | 三层收官架构 + 模组规格清单 + 移远战略读数 |

---


## 大脑架构基础与双系统 (Architecture & Dual-System)

端侧具身"大脑"从来不是单一模型。纵观定义 2025–26 年产业最高水平的四套量产级系统——Figure Helix、NVIDIA GR00T N1/N1.5、Physical Intelligence π0/π0.5、Google DeepMind Gemini Robotics——这一领域已收敛到同一个**双系统切分 (dual-system split)**:一个慢的、互联网预训练的 **System 2 (S2)** 负责语义场景/语言理解与规划,把意图喂给一个快的、轻量的 **System 1 (S1)**,由后者把这个意图转化为连续的电机指令。这就是任何端侧大脑都必须具体落地的架构。

### 为什么非切分不可(速度 vs. 通用性的权衡)

- Figure 的表述是本领域最核心的立论依据(primary):*"VLM 骨干很通用,但不快;机器人视觉运动策略很快,但不通用。Helix 通过两个互补系统的端到端联合训练来化解这一权衡。"* [figure.ai/news/helix]
- 单一的整体式 VLM 在语义上足够通用,但对闭环控制来说太慢(大型互联网预训练 transformer 通常只能跑到个位数到约 10 Hz);而一个小的视觉运动策略很快(100–200+ Hz),但泛化能力局限于其示教数据。切分让每一层能以各自的时钟、各自的规模独立运行。(primary)
- 这一模式对应到业界广泛使用的神经解剖学类比:**S2 ≈ 大脑皮层**(符号/语义层面的深思),**S1 ≈ 小脑**(快速运动控制 + 环境反馈);部分文献还加入了脊髓/反射一档。(unverified——这是跨文献引用但非出自单一权威一手来源的类比)

### 四套参考架构

| System | S2(慢/"大脑") | S2 频率 | S1(快/"小脑") | S1 频率 | 耦合方式 | 部署 |
|---|---|---|---|---|---|---|
| **Figure Helix** | 7B 开放权重 VLM | 7-9 Hz | 80M 交叉注意力编码器-解码器 transformer | 200 Hz | 单个连续潜向量;异步 | 双低功耗嵌入式 GPU,全部机载 |
| **NVIDIA GR00T N1** | Eagle-2 VLM (1.34B) | 10 Hz | 扩散 Transformer(flow-matching) | 120 Hz | 对 VLM token 做交叉注意力;联合训练 | Jetson 级;共 2.2B |
| **NVIDIA GR00T N1.5** | Eagle 2.5 VLM (2.1B),**冻结** | (~10 Hz) | flow-matching DiT + FLARE 辅助头 | (~120 Hz) | 带 LayerNorm 的 MLP 连接层;flow-matching + 世界模型损失联合训练 | 共 ~3B |
| **PI π0 / π0.5** | PaliGemma VLM (3B) | (由 chunk 触发) | 300M flow-matching "动作专家" | ~50 Hz | 两路数据流,一个联合训练的模型 | 共 3.3B;π0-small 470M 变体 |
| **Gemini Robotics** | Gemini Robotics-ER("认知大脑") | 云/边 | Gemini Robotics VLA + 本地动作解码器 | 本地 50 Hz | ER 逐步发出自然语言指令;滚动窗口 chunk | 云端骨干 + 端侧解码器(或全本地) |

所有数字均为 primary,唯 GR00T N1.5 的 S2/S1 频率带括号(推断与 N1 一致;N1.5 官方页面未重复给出——精确 Hz 层面应视为 (unverified))。

### Figure Helix ——最纯粹的异步双时钟设计

- **S2**:一个 **7B 参数**的开放权重 VLM,基于互联网规模数据预训练,在 500+ 小时机器人遥操作数据上微调;运行频率 **7-9 Hz**。(primary,已对照 figure.ai/news/helix 核实)
- **S1**:一个 **80M 参数**的交叉注意力编码器-解码器 transformer(比 S2 小约 90 倍),运行频率 **200 Hz**——两个系统间约 25-30 倍的频率差。(primary,已核实)
- **通信方式是单个连续潜向量**,而非语言 token:S2 *"把所有与任务相关的语义信息蒸馏进单个连续潜向量"*,供 S1 消费。训练阶段,梯度从 S1 反向传播穿过这个向量进入 S2(完全端到端可微分);部署时,S1 从共享内存中读取*"最近一次的 S2 潜向量"*——正是这种解耦让两个系统能够**以各自的时钟频率异步运行**。(primary,已核实)
- **动作空间**:完整上半身 **35 自由度** @ 200 Hz——手腕位姿、逐指屈伸+外展、躯干与头部朝向目标——支持灵巧双臂操作。(primary,已核实)
- **部署方式**:S1 与 S2 **全部机载,运行在两个低功耗嵌入式 GPU 上**,推理跨两颗芯片拆分——这是"大脑对小脑分别落在不同硅片上"的一个真实实例,也是本文最相关的端侧先例。(primary,已核实)另见 [Figure](company-figure.md)。

### NVIDIA GR00T N1 → N1.5 ——联合训练的 VLM + 扩散 Transformer

- **N1** 将 Eagle-2 VLM 作为 System-2(1.34B 参数;Eagle-2 = SmolLM2 LLM + SigLIP-2 图像编码器)与一个**扩散 Transformer(flow-matching)System-1** 配对,后者对 VLM token 做交叉注意力。两者**端到端联合训练**,而非分阶段独立训练。已发布权重 GR00T-N1-2B = 共 **2.2B**。(primary)
- **N1 吞吐**:S1 在 L40 GPU(bf16)上采样一个 **16-动作 chunk 耗时 63.9 ms**,**K=4 步 flow-matching 积分步**;S2 以 **10 Hz** 更新条件输入,S1 维持 **120 Hz** 闭环控制。分块把慢 VLM 的开销摊薄到大量快动作上。(primary,已对照 arXiv 2503.14734 核实——"在 L40 GPU 上用 bf16 采样 16 个动作的 chunk 推理耗时 63.9ms";VLM "1.34B"、总计 "2.2B"、SmolLM2 LLM + SigLIP-2 编码器、S2 10Hz / S1 120Hz 均逐字确认)
- **N1.5** 把 S2 升级为 **Eagle 2.5(2.1B)**,在预训练和微调阶段**冻结 VLM**,给 MLP 连接层加了层归一化,并联合训练 flow-matching + **FLARE**(Future LAtent Representation Alignment——对齐到目标未来表征而非生成未来帧),使其也能从人类视频中学习。训练 **250K 步,1K 张 H100,全局 batch 16,384**。(primary,已对照 research.nvidia.com/labs/gear/gr00t-n1_5 核实)
- **更强、被冻结的 S2 带来的收益**:在真实 Fourier GR-1 人形机器人上(用语言指定水果 → 放盘子任务),**语言跟随成功率 93.3%(N1.5)对 46.6%(N1)**;整体成功率 **83.0% 对 43.3%**——证据表明强化/冻结 S2 能大幅提升指令跟随能力,而无需触碰控制频率所在的 S1。(primary,已核实——93.3/46.6 与 83.0/43.3 四个数字均在 research.nvidia.com/labs/gear/gr00t-n1_5 逐字确认)另见 [NVIDIA](company-nvidia.md)。

### Physical Intelligence π0 / π0.5 ——两路数据流,flow-matching 动作专家

- **π0**:PaliGemma **3B** VLM 骨干 + 一个独立的 **300M flow-matching "动作专家"**(从零初始化,负责本体感知状态+动作生成);共 **3.3B**。概念上与 Helix 相同的 S2/S1 切分,但实现为**一个联合训练模型内的两路数据流**,而非两个异步时钟的系统。(primary,已对照 arXiv 2410.24164 核实——"动作专家 3 亿参数……共计 33 亿参数")
- **分块**:每次前向传播通过条件 flow matching 预测一个完整的 **H=50 动作 chunk(50 Hz 下 1 秒)**,**10 步积分**(δ=0.1);该 chunk 在重新生成前以开环方式执行。(primary,已核实——"我们使用 H=50","10 个积分步(对应 δ=0.1)")
- **频率**:约 **50 Hz** 电机输出;板载推理延迟约 **73 ms(RTX 4090,bf16,3 个摄像头)**——每约 0.5-0.8 秒触发一次新的前向传播。这就是一个非实时的 VLM+扩散栈如何仍能维持 50 Hz:分块把慢推理摊薄到许多次快的开环动作上。(~73 ms 数字为 secondary——不在 2410.24164 正文,由外部基准佐证;~86 ms 的离板/网络数字无法溯源,已作为 (unverified) 舍弃)
- **π0-small(470M,无 VLM 预训练)** 让这一权衡变得显性:去掉互联网规模预训练,模型缩小约 7 倍,但牺牲了泛化能力——这也是为什么该领域始终为 S2 角色保留一个大型预训练 VLM。(primary,已核实——"π0-small 有 4.7 亿参数,不使用 VLM 初始化")
- **π0.5** 让层级结构显性化:模型首先用**自然语言口述下一个子任务**("接下来该做什么"),然后 300M 动作专家把它解码为 50 步的 chunk——即从思维链到动作(与 PI 的 "Hi Robot" 共享这一思路)。异构协同训练(多机器人 + 网络/语义数据 + 子任务标注)带来了开放世界的泛化能力:在训练中从未见过的全新厨房/卧室里,能完成 **10-15 分钟的多阶段移动操作任务**。(primary)另见 [Physical Intelligence](company-pi.md)。

### Google DeepMind Gemini Robotics ——显式的云/边双模型切分

- **两个模型**:**Gemini Robotics-ER**("认知大脑"/具身推理模型)负责空间理解、任务规划和成功检测;**Gemini Robotics (VLA)** 把 ER 逐步发出的自然语言指令转化为底层电机指令,并有自己内部的思维链和长任务分解能力。(primary)
- **隐藏延迟**:一个大型 VLA 骨干运行在**云端**,把压缩后的指导信息发给一个**轻量本地动作解码器**,后者一次预测多个短动作 chunk,以在一个**优化到 160 ms 以下**的骨干查询-响应延迟背后,藏住这一延迟,呈现出 **50 Hz 有效控制频率**,端到端(原始观测 → 底层动作 chunk)闭环延迟约 **250 ms**。(primary,已对照 arXiv 2503.20020 核实——"从数秒优化到 160ms 以下"、"端到端延迟……约为 250ms"、"有效控制频率为 50Hz")另有一个单独发布的**完全端侧变体**(Gemini Robotics On-Device)在本地运行整个闭环,但**没有发布逐步的 ms 数字**——DeepMind 的端侧材料没有给出硬性的延迟数字,因此早先"每步 10 ms 以下"的说法为 **(unverified)**,且很可能不准确(端侧控制闭环的公开文档仅给出 ≥15-30 Hz,即约每周期 33-67 ms)。
- **跨本体的"运动迁移" (Motion Transfer)**:仅在 ALOHA 2 上训练的技能能够**零样本**迁移到 Apptronik Apollo 和一个双臂 Franka——因为共享骨干学到了本体无关的表征,只有轻量的本地解码器需要针对每个机器人做适配。把大脑(骨干)和小脑(解码器)分开,不仅有利于速度,也有利于**跨本体迁移**。(primary)

### 对端侧大脑的启示

- **两套时钟,两种尺寸**:为一个大而慢的 S2(个位数到约 10 Hz,1-7B 参数)和一个小而快的 S1(约 50-200 Hz,80-300M 参数)分别做预算。这个频率差正是整个设计的意义所在。(primary,跨模型共性)
- **潜向量(而非 token)才是最紧密的耦合方式**:Helix 的单个连续潜向量 + 共享内存,正是真正实现异步端侧双 GPU 部署的关键。(primary)
- **分块是延迟的核心技巧**:π0/GR00T 表明一个慢的、非实时的技术栈仍能靠把一次推理摊薄到 16-50 步的 chunk 上,达到 50-120 Hz。任何端侧大脑的成败都系于"chunk 时长 vs. 重新生成延迟"这个预算权衡。(primary)
- **冻结/强化 S2 是划算的**(GR00T N1.5 的语言跟随从 46.6%→93.3%,整体从 43.3%→83.0%)——解耦让你可以独立升级推理这一半,而不用动控制这一半。(primary)

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

---

## 云边分工 (Cloud vs Edge / Split-Brain)

端侧具身大脑的核心设计决策是**什么留在本地、什么可以离开机器人**。业界已收敛到一个*分层延迟预算*和一个*反射/认知切分*(System 1 / System 2,即"小脑/大脑")。实时控制闭环必须在本地,因为网络往返时延远超其周期预算数个数量级;高层推理则可上云,因为它是间歇性的、对延迟不敏感的。

### 1. 延迟预算层级(为什么控制闭环永远不能离开本地)

控制各层以截然不同的频率运行,而最快的那些从根本上无法容忍任何网络往返:

| 层级 | 频率 | 周期预算 | 是否必须本地? |
|---|---|---|---|
| 底层关节/力矩控制 | ~1000 Hz(GR1 全身力矩) | ~1 ms | 是——亚毫秒级 |
| 全身 QP / 平衡控制 | ~100–200 Hz(QP@100 Hz;REEM-C PC@200 Hz) | 5–10 ms | 是 |
| 逆运动学 / 运动规划 | ~30–50 Hz(IK 上限约 30 Hz) | 20–33 ms | 是(反应性) |
| 感知 / VLM 场景理解 | ~7–9 Hz(Helix S2) | 100+ ms | 边缘优先 |
| 深思式规划 / 多步推理 | 秒级 | 数百 ms–秒 | 可上云 |

- 锚点对比:即便是*高度优化的遥操作*通道 **ExtremControl(2026)**,直接肢体控制的网络端到端延迟也只有约 **50 ms**(secondary)——已经比一个本地关节控制闭环(亚毫秒到数毫秒)差一个数量级,这正是遥操作只能作为*监督/兜底*模式、永远不能是主控制闭环的原因。
- 一份通用边缘-云机器人综述将边缘设备定位在 **10 ms 以内**响应,多机器人边缘驻留流水线展示了边缘部分平均命令-响应 **<1 ms**(0.001 秒)**(unverified——该具体亚毫秒数字未能在所引综述中再次确认)**;云端保留给复杂生成/推理卸载(secondary)。

### 2. 大型 VLA 全端侧化的代价(VLA-Perf,π0 家族)

硬推理数字显示数据中心与端侧芯片之间存在 **100 倍以上**的差距——这是全本地大型 VLA 受频率制约的核心证据(primary,VLA-Perf arXiv 2602.18397v1):

| 模型 | Jetson Thor(端侧) | RTX 4090(消费级) | 数据中心 |
|---|---|---|---|
| π0 baseline | 52.57 ms/步(19.0 Hz)* | 31.06 ms(32.2 Hz) | H100 6.15 ms(162.5 Hz);B100 3.18 ms(314.4 Hz);A100 16.20 ms(61.7 Hz) |
| π0-L(9.1B) | 3.9 Hz | 8.0 Hz | — |
| π0-XL(16.7B) | 2.1 Hz | — | — |
| π0-XXL(81.3B) | — | — | B100 9.6 Hz |
| 长上下文(1K 时间步) | 768.3 ms(1.3 Hz) | — | — |

\*Thor 上 π0 baseline 分解:视觉编码 6.06 ms + VLM 骨干 20.30 ms + 动作专家 26.20 ms。

- 架构和位置一样重要:**基于扩散的动作解码比朴素自回归(带分块)快 102.4 倍**;去噪步数从 10 增到 50,端到端延迟增加 **2.15 倍**(primary)。
- **5G + 数据中心 GPU(B100)上的异步推理吞吐量是同步云端推理的 5.99 倍**(primary)——量化了解耦异步、可云端卸载的感知/规划路径与同步、本地动作闭环所带来的收益。

### 3. 光有位置不够——模型大小才是关键(端侧 vs. 云端的反证)

在 **Unitree G1-EDU** 人形机器人上进行的受控 VLM 基准测试(边缘节点为 NVIDIA L4 24 GB,一个现实的 ORAN/MEC 节点)表明,把算力搬到边缘*并不*自动带来巨大收益(primary,arXiv 2601.14921):

| 模型 | 边缘(端到端) | 云端基线 | Δ |
|---|---|---|---|
| LLaMA-3.2-11B-Vision(4-bit NF4) | 1600.03 ms | 1685.20 ms | 仅约 5% |
| Qwen2-VL-2B | "亚秒级" | — | 不到云端基线的一半 |

- 无论位置在哪,文本生成都占**超过 85%** 的延迟——所以一个大模型从边缘部署中几乎得不到收益;真正的收益来自一个**更小、量化过**的端侧模型。启示:把分脑设计和*恰到好处大小*的本地模型配对,不要只是把一个大模型原样搬到边缘。

### 4. 云-边光谱上的产业架构

| System | 切分模式 | 端侧算力 | 云端角色 | SQ |
|---|---|---|---|---|
| **Figure Helix** | S2(7B VLM @7–9 Hz → 潜向量)+ S1(80M 交叉注意力 transformer @200 Hz,35 自由度上半身) | 双低功耗嵌入式 GPU,模型并行 | **无**——全部机载,消除了"云依赖系统的延迟与在线率风险" | primary |
| **Gemini Robotics On-Device** | VLA 基础模型**完全本地**运行;用 50–100 条示教适配 | 机器人本地 | 保留旗舰云端 Gemini Robotics 以获得"不受端侧限制"的 SOTA 能力——明确的能力/延迟权衡 | primary |
| **Quectel Robrain(移远 v2.0)** | 端云协同(edge-cloud collaboration);实时检测网络,动态分配算力;以端侧为主、云端为辅 | 端侧为主;敏感数据本地 | 云端迭代优化;联网时接入豆包/DeepSeek + 搜索 | primary(85% 离线数字:secondary) |
| **RoboOS** | "大脑"(云端推理/规划)+ "小脑"(端侧反应控制);跨本体、多智能体 | 每台机器人自带小脑 | 多步推理 + 跨机器人协同 | primary |
| **Tesla Optimus** | 纯视觉、云无关推理;定制机载芯片(Gen 3 为 AI5 级,FSD 血统) | 定制 SoC | 控制闭环不依赖云端 | **unverified**(爱好者媒体报道;芯片名称/规格未证实) |
| **1X Neo** | 端侧自主 + **远程人工遥操兜底**("Redwood"),发布时自主率约 60–70% | 机载 | 兜底方案是*人类操作员*,不是更大的云模型 | **unverified**(secondary;断线安全行为未见文档) |

- **Robrain** 宣称**"断网环境下仍维持 85% 核心功能"**(secondary);部署在 LimX Dynamics 的 TRON 1 双足机器人上。这是端侧优先设计中一个具体的优雅降级目标。
- **Helix 的数据效率**:约 **500 小时**训练数据——是此前所采集 VLA 数据集规模的**不到 5%**(**减少超过 95%**),据 Figure 官方博客(primary)——且没有多本体采集或多阶段训练;证明 S1/S2 切分(小型反应网络由预训练 VLM 条件驱动)比整体式端侧巨兽更省数据,倾向混合而非整体式方案。
- **Gemini Robotics On-Device** 在分布外任务和多步指令上超过此前最好的端侧 VLA,能在本地完全跑通灵巧双臂任务(拉拉链袋子、叠衣服)(primary)——端侧能力差距正在缩小。

### 5. 端侧算力锚点(2025–2026)

- **NVIDIA Jetson Thor(Blackwell)**——许多人形机器人厂商(Boston Dynamics Atlas、Agility Digit gen-6)正在采用的参考平台:最高 **2,070 FP4 TFLOPS**、**128 GB** 内存、**40–130 W**、约 273 GB/s 带宽;2,560 个 CUDA 核心,96 个第五代 Tensor Core,14 核 Arm Neoverse-V3AE(primary)。这是 AGX Orin 的 **7.5 倍 AI 性能与 3.5 倍能效**——比 B100/H100 低几个数量级,但足以以个位数到几十 Hz 跑一个 7-9B VLM 骨干,**外加**一个 100-200 Hz 的小型动作专家网络。这正是 Helix 式 S1/S2 切分所量身设计的算力空间。

### 6. 通用 CS 趋势

- Splitwise 式的边云 LLM 协同推理研究把切分定位到**token/层级**,用基于 Lyapunov 优化的强化学习依网络条件动态满足延迟 SLA(primary/secondary)——这是 Robrain 实时网络感知算力分配的非机器人领域对应物。预计机器人大脑会采纳同样的动态、SLA 驱动切分,而非静态的边云边界。

### 设计启示

- **绝不**把 ≥100 Hz 的反应/平衡闭环走网络——无条件把这留给边缘。
- 沿 **System 1 / System 2** 边界切分:本地快动作网络,延迟容忍的 VLM/规划器(本地优先,可上云)。
- 恰当地缩放本地模型(量化、蒸馏)——把大模型搬到边缘几乎无收益(见第 3 节)。
- 设计一个明确的**降级梯度**:完整云端推理 → 本地 VLM → 仅反射自主 → 人工遥操(1X 模式)→ 安全停止。
- 瞄准一个具体的离线底线(Robrain 的 85%),把云端当作*迭代优化*,而非依赖项。

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
- https://robotwale.com/article/tesla-optimus-14 ; https://optimusk.blog/blog/what-is-tesla-optimus/(secondary/爱好者媒体,unverified)
- https://www.humanoidsdaily.com/news/1x-neo-launch-sparks-debate-on-autonomy-and-teleoperation ; https://www.therobotreport.com/teleop-not-autonomy-the-path-for-1x-neo-humanoid/(unverified)

---

## 端侧 VLA 推理算力需求 (On-Device Compute Requirements)

一个端侧具身大脑到底需要多少算力?2026 年实测工作给出的老实答案是:比营销宣传里暗示的**"峰值 TOPS"更少,而对内存带宽的需求更多**。现代 VLA(视觉-语言-动作模型)真正的瓶颈不在视觉/语言骨干——而在扩散**动作专家(action expert)**,它在测试过的每一颗端侧芯片上都是内存带宽受限的。本节量化真实的算力空间、规格表 TOPS 与实际交付 Hz 之间的差距,以及当前端侧硅片的实际水平。

### 1. 基线:π0(2.7B)在硬件阶梯上的延迟

最有用的单一参考是 **VLA-Perf**(arXiv 2602.18397),它对同一个 π0(2.7B 参数,BF16,10 去噪步,动作 chunk = 50)在整条硬件阶梯上做基准,并分解为视觉编码器 / VLM 骨干 / 扩散动作专家(primary):

| 硬件 | 层级 | 视觉 | VLM 骨干 | 动作专家 | 端到端 | 吞吐 |
|---|---|---|---|---|---|---|
| B100 | 数据中心 | 0.40 ms | 1.87 ms | 0.91 ms | **3.18 ms** | **314.4 Hz** |
| H100 | 数据中心 | — | — | — | **6.15 ms** | **162.5 Hz** |
| A100 | 数据中心 | — | — | — | **16.20 ms** | **61.7 Hz** |
| RTX 4090 | 消费级 | 4.02 ms | 19.79 ms | 7.25 ms | **31.06 ms** | **32.2 Hz** |
| Jetson Thor | **端侧** | 6.06 ms | 20.30 ms | 26.20 ms | **52.57 ms** | **19.0 Hz** |

所有数字均为 primary(VLA-Perf 表 3,§4.2)。端侧与数据中心之间的差距约为 **16.5 倍**(Thor 对比 B100),同一模型下测得。注意在 Thor 上动作专家占主导(52.6 ms 中的 26.2 ms,约 50%),而在 B100/4090 上是 VLM 骨干占主导——这是一种硬件相关的反转,§3 会解释原因。

### 2. 模型规模近似线性压垮频率

把 π0 放大对端侧极其不利——频率随参数量近似线性下降,且端侧/消费级芯片比数据中心芯片更早爆内存(primary,VLA-Perf 表 5,§4.3):

| 变体 | 参数 | Jetson Thor | RTX 4090 | B100 |
|---|---|---|---|---|
| π0 | 2.7B | 19.0 Hz | 32.2 Hz | 314.4 Hz |
| π0-L | 9.1B | 3.9 Hz | 8.0 Hz | 73.6 Hz |
| π0-XL | 16.7B | 2.1 Hz | **OOM** | 39.7 Hz |
| π0-XXL | 81.3B | **OOM** | **OOM** | 9.6 Hz |

设计推论:如果一个端侧大脑必须完全本地运行到可用速率,现实上被限制在 **~2–3B 骨干**这一档;任何 ≥9B 的模型在目前最好的端侧芯片上都只能跑到个位数 Hz。

### 3. 为什么 TOPS 会骗人:动作专家是内存带宽受限的

这是机制层面的核心。VLA-Perf 给出了每个组件相对每颗芯片 roofline 拐点的算术强度(FLOPs/Byte)(primary,表 4,§4.2,要点 2):

| 组件 | 算术强度 | 行为 |
|---|---|---|
| 视觉编码器 | 321.4 FLOPs/Byte | 计算受限(Thor 除外) |
| VLM 骨干 | 542.8 FLOPs/Byte | 计算受限(Thor 除外) |
| **扩散动作专家** | **54.0 FLOPs/Byte** | **在所有硬件上都是内存受限** |

| 芯片 | Roofline 拐点(平衡点) | 含义 |
|---|---|---|
| RTX 4090 | 163.7 | 视觉/VLM 计算受限;动作内存受限 |
| B100 | 218.8 | 视觉/VLM 计算受限;动作内存受限 |
| **Jetson Thor** | **1481.5** | **三个组件都是内存受限** |

Thor 的拐点约是 4090 的 **9 倍**,因为它的 FLOPs 与带宽比例严重偏向计算(巨大的 FP4 TOPS,却只有 273 GB/s)。所有三个组件都落在拐点左侧 → 内存受限 → 头条 TOPS 数字根本不是约束条件。另一项独立研究(arXiv 2604.24447,secondary)佐证了这一点:在一次推理调用中,VLM 骨干的 SM 利用率**超过 90%**,而扩散动作专家只有 **20–40%**——一个约 3 倍的效率差,峰值 TOPS 评级根本反映不出来。

### 4. 营销数字 vs. 实际交付的差距,双重量化

两个差距叠加:

- **Roofline 理论值 vs. 真实内核**:即使是*理论*roofline 也高估了。经过优化的 Triton 代码只能达到 roofline 的 **73–83%**——单摄像头:14.7 ms roofline vs. 20.0 ms 实测(73.3%);三摄像头:30.4 vs. 36.8 ms(82.6%)(primary,VLA-Perf 表 1,§3)。未经优化的部署差距更大。
- **精度基准(FP4 头条数字 vs. BF16 现实)**:Jetson Thor 的"**2070 FP4 稀疏 TFLOPS**"头条数字在 BF16 下缩水到约 **258 BF16 TFLOPS**——约 8 倍差距——而大多数 VLA 策略跑的是 BF16,不是 FP4(secondary,arXiv 2604.24447)。该论文的*纯 BF16* 端侧 π0 实测数字甚至比 VLA-Perf 的 FP4 调优数字更差:Thor 上 **246 ms 未编译 → 163 ms 编译后(约 6.1 Hz)**;RTX 4090 102.3 → 35.2 ms(28.4 Hz);昇腾 Ascend 310P 818 → 350 ms(2.86 Hz)。

启示:在信任任何规格之前,**永远要问"这是什么精度下的 TOPS,稠密还是稀疏,我的策略是否真的用了那个数据类型?"**

### 5. 真正有用的杠杆(以及一个没用的)

- **去噪步数才是真实开销,chunk 大小几乎免费。** 在 B100(chunk 50)上,去噪步数从 10→50 = 动作专家延迟 **5 倍**,总延迟 **2.15 倍**;动作 chunk 大小"影响可忽略"(primary,VLA-Perf §4.5,要点 6)。所以可以随意为每次调用增加动作 chunk,只在精度确实需要时再增加去噪步数。
- **扩散 >> 自回归,用于动作头。** 扩散式动作解码比朴素自回归**快约 102 倍**(B100,chunk 50:3.2 ms/312.5 Hz vs. 327.6 ms/3.0 Hz);仅在 chunk ≤10 时并行自回归才具竞争力(primary,§4.6,要点 7–8)。
- **长上下文(KV-cache 增长)扼杀端侧吞吐。** B100 上:1 步 = 3.2 ms/314 Hz/0.01 GB KV;100 步 = 11.3 ms/88 Hz/1.3 GB;1K 步 = 85.2 ms/11.7 Hz/13.2 GB;10K 步 = 823.7 ms/1.2 Hz/131.8 GB。端侧/消费级 GPU 在实时条件下被限制在**约 100 个历史时间步**;只有数据中心 GPU 能维持约 1K(primary,表 6,§4.4,要点 5)。
- **量化对 VLA 而言不是免费午餐。** 一个 4-bit NF4 骨干 + FP32 头达到约 9 倍加速,但对完整 OpenVLA 做 INT4 只带来 1.14 倍加速,且**成功率下降 9%**(secondary)——不同于纯 LLM 量化,VLA 任务成功率会明显退化。

### 6. 真实端侧硅片的位置(算力阶梯)

端侧大脑设计者实际会选的芯片,规格表 TOPS(所有数字均标出精度/稀疏度基准——**没有基准就不可跨芯片比较**):

| 档位 | 芯片 | 头条算力 | 基准 | 内存/带宽 |
|---|---|---|---|---|
| 模组 | Qualcomm QCS8550 | 48 TOPS | INT8(HTP/NPU) | 8/16 GB LPDDR5X @4200 |
| 模组 | Qualcomm Dragonwing Q-8750 | 77 TOPS 稠密;最高支持 11B LLM | 稠密 | (SD 8 Elite 级) |
| Jetson | Orin Nano | 67 TOPS | INT8 稀疏 | 7–25 W |
| Jetson | Orin NX | 157 TOPS | INT8 稀疏 | 10–40 W |
| Jetson | AGX Orin | 275 TOPS | INT8 稀疏 | 15–60 W |
| 高端 | Qualcomm Dragonwing IQ10 | 700 TOPS 稀疏(350 稠密) | 稀疏 | 18 核 Oryon CPU + NPU + GPU |
| 高端 | **NVIDIA Jetson Thor** | **2070 TFLOPS**(约 258 BF16) | **FP4 稀疏** | 128 GB LPDDR5X,**273 GB/s**,40–130 W |

除 Thor 的 BF16 数字为 secondary 外,其余均为 primary。Thor 宣称相对 AGX Orin 有 7.5 倍性能 / 3.5 倍能效提升(primary)。IQ10(Thundercomm TurboX IRB10 参考设计,最高 20 路摄像头)是目前"700-TOPS 人形档"的代表(primary)。

### 7. 伺服频率下的带宽墙

算力余量解决不了最高频率的闭环。一份聚合估算认为,要维持 π0/GR00T 级策略在 **500 Hz** 伺服级控制下运行需要约 **1,750 GB/s** 带宽——是 Thor 实际 273 GB/s 的 **6.4 倍**(unverified)。即使只是近似值,这也印证了结构性差距:2026 年的端侧硅片对 S1(电机伺服)闭环而言是**带宽饥渴**的,与 TOPS 余量无关。这正是双系统切分(快而微小的本地 S1,慢一些的 VLM S2)存在的*原因*——用 2026 年的端侧内存子系统,你无法靠蛮力在端侧跑出 500 Hz 的 VLA 推理。

### 8. 设计目标与启示

VLA-Perf 明确给出的 Hz 分档:**10 Hz = "可接受"**(接近摄像头帧率);**100 Hz = "高性能"**(超过典型视频摄入速率)(primary,§4.11)。

- **端侧(Thor)已经能达到 10 Hz**(π0 跑到 19 Hz),但要达到 100 Hz 需要通过压缩/量化再获得约 **5 倍**提升(要点 13,primary)。
- **服务端卸载在快速/中速链路上胜过端侧**——B100 服务端*总*延迟(3.18 ms 计算 + 网络往返):**3.3 ms(以太网 10G)/ 8.4 ms(WiFi7)/ 27.8 ms(5G)/ 73.0 ms(4G)**,对比 Thor 端侧 **52.57 ms**。所以以太网/WiFi7/5G 都优于本地,但**4G 路径(73.0 ms)反而比 Thor 端侧更慢**——卸载只有在链路够好时才划算。完全本地是一个*策略/隐私/在线率*的选择;仅从延迟看,只有链路降级到 4G 级或更差时它才占优(primary,§4.7,表 8,要点 9)。
- **异步 S1/S2 重叠能挽回吞吐——在快链路上收益最大**(此时 S1 可以以高原生频率运行):B100 异步加速比(S2 上限 10 Hz)**2.24 倍(以太网 10G)→ 1.26 倍(WiFi7)→ 1.05 倍(5G)**;双系统在 Thor 端侧给出 **1.30 倍**(10 Hz S2 上限)。未见 4G 异步的数据行(primary,表 9)。

**给端侧大脑的底线**:骨干规模定在约 2-3B,扩散动作专家(带宽受限——最大化内存带宽,而非 TOPS)、保持去噪步数低、chunk 长,本地上下文控制在约 100 时间步以内,并把伺服闭环作为*独立*的小型反射网络单独预算——因为 2026 年没有任何端侧芯片有足够带宽以伺服速率运行完整 VLA 推理。

来源:
- https://arxiv.org/abs/2602.18397 ; https://arxiv.org/html/2602.18397v1 — VLA-Perf:π0 延迟阶梯、roofline/内存受限分析、去噪/chunk/上下文扫描、Hz 目标(primary)
- https://arxiv.org/abs/2604.24447 — Characterizing VLA Models across XPUs:BF16 π0 延迟、SM 利用率差距、FP4 vs. BF16 规格差距(secondary)
- https://www.nvidia.com/en-us/autonomous-machines/embedded-systems/jetson-thor/ ; https://blogs.nvidia.com/blog/jetson-thor-physical-ai-edge/ — Thor 规格(primary)
- https://www.nvidia.com/en-us/autonomous-machines/embedded-systems/ — Jetson Orin 系列 TOPS 阶梯(primary)
- https://www.qualcomm.com/products/internet-of-things/industrial/industrial-processors/qcs8550 — QCS8550 48 TOPS INT8(primary)
- https://www.qualcomm.com/products/technology/processors/dragonwing — Dragonwing Q-8750(77 TOPS)& IQ10(700 TOPS 稀疏)(primary)
- https://www.thundercomm.com/product/turbox-irb10/ — TurboX IRB10 / IQ10 参考设计,20 摄像头(primary)

---

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
- **TinyVLA(<1B backbone)** (primary):在小型高速多模态骨干上挂扩散 policy decoder,**跳过大规模机器人预训练**。MetaWorld sim +21.5%,真机比 OpenVLA (7B) 高 **25.7%**,且更快——小扩散头 VLA 在速度和精度上双杀更大的自回归模型。
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

---

## 实时控制的切分 (The Real-Time Control Split)

端侧具身大脑的核心架构事实是:**单一时钟无法服务整个技术栈。** 语义推理想要秒级;全身协调想要毫秒级;电机电流环想要微秒级。没有任何一种计算底座能同时把这三者都做好,所以每个认真的人形技术栈都把控制切分成一个**频率层级**,把每一档映射到确定性保证与该档周期相匹配的硅片上。工程上的取舍在于*每一刀切在哪里*、*每一侧跑在什么硬件上*。

### 端侧控制频率阶梯

各档按闭环周期排序。频率越高,底座越从 Linux+GPU(不确定的、尽力而为)转向专用 MCU / 实时核(硬确定性)。

| 档位 | 典型频率 | 计算内容 | 底座 | 确定性 |
|---|---|---|---|---|
| S2 语义推理 | 慢速/规划时间尺度 | 场景理解、语言、行为排序 | Linux + GPU(VLM) | 无(尽力而为) |
| S1 全身策略 | 30–200 Hz | 感知 → 全身关节目标 | Linux + GPU(transformer 策略) | 软/坚实实时 |
| S0 反射层 | ~1 kHz | 平衡、接触、协调;关节执行器指令 | 实时核 / MCU | 硬实时 |
| 电流/力矩环 (FOC) | 1–20 kHz | 磁场定向电流控制、PWM | 关节 MCU 固件 | 硬实时(原生) |

### 参考架构——各厂商把切口放在哪

| System | 慢/语义 | 快策略(S1) | 反射/底层(S0) | 来源 |
|---|---|---|---|---|
| Figure Helix 02 | S2,规划时间尺度 | 200 Hz,transformer,所有传感器→所有执行器(**80M 参数数字未证实——官方页面只说"基于 transformer"**) | **1 kHz、1000 万参数 NN**;在 **200,000+ 并行仿真环境**中重定向的 **1,000+ 小时**人类动作上训练 | figure.ai/news/helix-02(primary) |
| Figure Helix v1 | System 2 VLM,低频 | **200 Hz 单一电机策略,35 自由度**动作空间(手指、末端执行器、头部注视、躯干) | *(无独立反射层——在 v02 中才加入)* | figure.ai/news/helix(primary) |
| Boston Dynamics electric Atlas | 大行为模型策略 | **30 Hz**(图像+本体感知+语言→动作) | 底层**基于 MPC 的全身控制器**(频率未披露) | bostondynamics.com(primary) |
| 学术界 WBC(综述) | 质心 MPC / 学习策略 **10–50 Hz** | 任务空间/全身控制器 **50–120 Hz** | *(专用关节固件,超出综述范围)* | 分层 WBC 综述(secondary) |

**关键观察:** Helix v1 → v02 是业界承认一刀不够——200 Hz 策略对平衡和接触而言太慢/不够确定,所以在它下面又切出一个 **1 kHz 反射层(S0)**(primary)。Atlas 的学习式"大脑"跑得更慢,只有 **30 Hz**,并且*指挥*底下一个经典 MPC 控制器——同样是慢策略→快经典控制器的模式,只是策略层明显比 Helix 的 200 Hz S1 更慢(primary)。注意**所调查的学术架构中没有一个直接达到 500 Hz–1 kHz 的 MCU 档**——那一档活在全身控制器之下的专用关节固件里(secondary)。

### 为什么 Linux+GPU 撑不起快闭环(为什么大脑算力≠实时算力)

AI 底座在结构上被排除出 ≥1 kHz 档位的定量证据:

- **原生 Linux 的尾延迟对 1 kHz 闭环是致命的。** ROS2 跑在未打实时补丁的原生内核上,测得**最大调度延迟 6,243 µs(6.2 ms)** *(该确切数字单一来源于一篇付费论文的结果表;多毫秒级原生 Linux 尾延迟由独立测量结果 1.5–13.4 ms 最坏情况佐证)*——平均约 3 µs,但真正要命的是尾部。1 kHz 闭环预算只有 **1 ms**;一次 6.2 ms 的卡顿就是错过截止时间(primary,《中国机械工程学报》)。
- **PREEMPT_RT 是缓解措施,不是保证。** 同一套装置打上 PREEMPT_RT 补丁后,无论空载还是满载,最坏延迟都被限制在 **94 µs**——足以应对 kHz 级的*软/坚实*实时,但这是一种通常只用到**约 1 kHz**、而非 10–20 kHz 电流环的软件补丁,不是硬件层面的保证(primary)。
- **ros2_control 展示了所需的工程纪律。** `controller_manager` 运行一个固定速率闭环(常见为 **200 Hz–1000 Hz**),申请 **SCHED_FIFO 优先级 50**,支持各组件的异步速率(例如 IMU 以 1000 Hz 读取,其他以 500 Hz 运行),其文档*明确警告*非实时安全的调用(如 `get_lifecycle_state()`)必须留在实时路径之外,并建议使用实时/低延迟内核(primary,control.ros.org)。
- **GPU 能加速 S1 档,但不能让它变成硬实时。** ReLU-QP(一个把 QP 求解器重构为权重绑定 ReLU 网络、跑在 GPU 上的方案)把单脚 Atlas 平衡的全身 MPC 频率从 **约 65 Hz(CPU QP)提高到 1,300+ Hz**——证明全身档是计算受限的,GPU 能把它推过 1 kHz,但这仍是**尽力而为的 GPU 计算,不是确定性保证**,这正是最内层力矩环仍需一个独立 MCU 的原因(primary,arXiv:2311.18056,ICRA 2024)。

**架构层面的根本原因:** AI SoC 的主 **Cortex-A / GPU** 复合体带有 **MMU**——TLB 缺失、页表遍历、缓存与调度器的变动都会注入抖动。实时/安全核用 **Cortex-R 配 MPU** 取而代之:确定性地址转换、无 TLB 缺失、无页表遍历,通常采用**双核锁步 (dual-core lockstep)** 通过输出比对捕获单粒子翻转(secondary,Arm Newsroom)。这正是硅片厂商*额外挂上*一个独立确定性域,而不是与 Linux 复合体分时共享的原因。

### 硬件边界——一个计算模组必须暴露什么

这一刀不仅是软件层面的;它也是硅片层面的。即使在"富 SoC"内部,也有一个物理隔离的实时域:

- **NVIDIA Jetson(Orin 级)功能安全岛(FSI):** **4× 双核锁步 Cortex-R52(Armv8-R)**,独立电源/电压隔离,评级 **ASIL-D(系统性)/ ASIL-D(随机性)**——FSI 是 Orin SoC 上*唯一*达到 ASIL-D 随机性等级的域(SoC 其余部分等级更低),**约 10K ASIL-D MIPS**,**每个 R52 核 512 KB TCM**(ATCM 256 KB + BTCM 128 KB + CTCM 128 KB),**3 MB 共享 SRAM**。一个硬件安全管理器(HSM)监控故障,并向外部 MCU 触发一个 **`SOC_ERROR` GPIO**(primary,NVIDIA DRIVE OS 6.0.9/7.0.3 FSI 文档)。这是"一个模组必须暴露什么"的最清晰证据:一个与 AI 计算域**物理隔离**的确定性实时/安全域。
- **EtherCAT 作为确定性现场总线:** 数十个伺服轴的周期时间可低至 **62.5–100 µs**,**抖动 <1 µs**;一项研究测得千兆网上 50 台设备(每台 100 字节)的**最小周期 50 µs**;一个真实人形实现达到 **250 µs** 周期(secondary——acontis/elmomc/ASIX)。这种微秒级确定性让单个主站能在一个约 1 kHz 周期内同步指挥数十台驱动器。
- **acontis EC-Master 跑在 Jetson Orin/Thor 上:** "富 SoC 通过 EtherCAT 对分布式关节 MCU 跑 ROS2"这一模式的直接商业化实例——为 AI 推理/感知/导航保留 **>99% 的 CPU 可用率**,同时在后台处理现场总线,具备**微秒级确定性**(primary——acontis.com,*注:该页面给出了 >99% 与微秒级确定性的说法,但没有给出明确的 Jetson 周期时间数字*)。
- **关节级 MCU 档("脊髓"):** TI **C2000 TMS320F28P650DK** 在一块 **9×9 mm BGA** 上集成了硬件 **EtherCAT** 控制器 **+ CAN-FD**,通过 **IEC 61508 SIL 2** 认证,带 FOC 能力的 PWM/ADC——一颗芯片桥接确定性总线+电机控制+安全(primary,TI 产品页 + AppBrief slla659a)。
- **EtherCAT 之下的总线:** 在不需要完全确定性的地方,**CAN-FD** 把数据阶段速率从 CAN 2.0 的 **1 Mbps 提升到 5–8 Mbps**(部分资料称最高 10 Mbps),载荷从 **8 → 64 字节**;文档记录的收益为关节位置反馈吞吐 **1 → 5 Mbps**(secondary——Dorleco/Grid Connect)。
- **FOC 电流环,最内层档:** 运行在 **10–20 kHz**;常见模式是一个 **10 kHz 电流/力矩环嵌套在 1 kHz 速度环内**(NXP MCUXpresso SDK 参考),PWM 开关频率 **10–20 kHz**(primary,NXP FOC 用户指南)。这一层*在*上述一切之下,完全活在关节固件里。

### 人形的特殊之处——安全层不能只是急停 (安全层不能只是急停)

相对固定基座工业机械臂的一个关键不对称性:**人形机器人的急停不能简单地切断电源。** IEC 61508(与 ISO 10218 / ISO/TS 15066 并用)要求 SIL 目标、故障隔离区和安全状态;关节力矩超限名义上会触发一次 **Cat 0 停止(IEC 60204-1)**。但一个欠驱动的双足机器人在单侧接地的情况下,如果突然断电会**摔倒/碰撞**——所以确定性安全层必须运行一个**预定义的兜底控制器**(保持平衡、调节接触、到达一个安全终止姿态),也就是说它必须是**具备控制能力的,而不是一个断电开关**(secondary——kitecompliance.ai;arXiv 2603.22703《学习人形机器人的安全可停性监控器》)。这提高了确定性档的门槛:它不只是一个监控器,而是运行在隔离实时/安全核上的一个真正的控制器。

### 启示

把大脑设计成**若干刀,而非一块整料。** 把 S2/S1(语义 + 全身策略,30–200 Hz)放在 Linux+GPU 上;接受它是尽力而为的。把 S0(约 1 kHz 反射/平衡)和安全兜底放在一个隔离的确定性核上(Cortex-R FSI 或专用 MCU)。把 1–20 kHz 的 FOC 环放在关节 MCU 固件里,通过 EtherCAT(微秒级确定性)或 CAN-FD(5–8 Mbps)触达。计算模组不可协商的必备特性是**一个与 AI 域电气隔离的实时/安全域**——Jetson Orin 正是以 Cortex-R52 FSI 的形式提供了这一点。

来源:
- https://www.figure.ai/news/helix-02
- https://www.figure.ai/news/helix
- https://bostondynamics.com/blog/large-behavior-models-atlas-find-new-footing
- https://www.acontis.com/en/humanoid-robotics.html
- https://www.ti.com/(C2000 TMS320F28P650DK 实时电机控制 MCU 产品页;App Brief slla659a "Motor Control in Humanoid Robots")
- NXP MCUXpresso SDK FOC 用户指南(PMSMMC56F80000EVK、PMSMMKV31UG)
- https://doi.org/10.1186/s10033-023-00976-5(《中国机械工程学报》,"ROS2 Real-time Performance Optimization and Evaluation")
- https://control.ros.org(Controller Manager;"Different update rates for Hardware Components")
- https://arxiv.org/abs/2311.18056(ReLU-QP,ICRA 2024)
- NVIDIA DRIVE OS 6.0.9 / 7.0.3 "功能安全岛 (FSI)" 开发者文档
- Arm Newsroom,"Cortex-R and the Next-generation of Vehicles"
- Dorleco / Grid Connect(CAN 2.0 vs. CAN-FD 对比)
- kitecompliance.ai "A Primer on Humanoid Robot Compliance";arXiv 2603.22703 "Learning Safe-Stoppability Monitors for Humanoid Robots"

---

## SoC / 硬件版图 (On-Device Brain SoC Landscape)

> 具身智能端侧"大脑"不是一颗芯片,而是一个按 TOPS 和价格分层的**分级市场**,并且越来越围绕一个**大脑-小脑 (brain-cerebellum) 融合**问题展开:认知(VLA 感知/策略)与硬实时电机控制是活在同一颗芯片上,还是两颗。截至 2026-07,NVIDIA Jetson Thor 稳坐高端,Qualcomm Dragonwing IQ10 是可信的约 700 TOPS 挑战者,而一个稠密的中国档位(Horizon/D-Robotics、Black Sesame、Rockchip、Ascend)以价格取胜。关键在于,大型 VLA 策略在实时速率下真正的约束是**内存带宽,而非原始 TOPS**——规格表上的 TOPS 数字并不能预测可用的控制闭环频率。

### 高端:人形大脑参考档

| SoC / 模组 | 峰值 AI 算力 | 内存 / 带宽 | 功耗 | 价格 | 状态(截至 2026-07) |
|---|---|---|---|---|---|
| **NVIDIA Jetson AGX Thor (T5000)** | 2,070 FP4 稀疏 TFLOPS;Blackwell GPU(2,560 CUDA + 96 Tensor 核心);14 核 Neoverse-V3AE | 128 GB LPDDR5X @ **273 GB/s** | 40–130 W | $3,499 开发套件 | GA 2025-08-25;事实上的高端标准(primary) |
| **NVIDIA Jetson T4000** | 1,200 FP4 稀疏 TFLOPS | 64 GB LPDDR5X | 40–70 W | $1,999 @1k | 2026 年 1 月 CES 发布;成本档 Thor(primary) |
| **Qualcomm Dragonwing IQ10** | 700 TOPS(18 核 Oryon + NPU + GPU) | 64 GB LPDDR5x ECC / 512 GB UFS 4.0 | 12V/24V,−40→70 °C | — | 2026 年 6 月 Computex 发布;2026 年 9 月量产(primary) |
| **Tesla AI5**(定制) | 每板约 2,500 INT8 TOPS *(unverified——一手流片报道中没有 TOPS 数字;引用的是相对 AI4 约 8–10 倍算力这一指标)*;Musk 宣称约 H100 级单芯片,功耗 <150 W | 192 GB LPDDR5X(相对 AI4 约 9 倍容量 / 约 5 倍带宽) | <150 W(声明) | 自用 | 2026-04-15 流片(TSMC AZ + 三星 TX,**3 nm**);2027 年中后期量产;Optimus + Cybercab/超算集群优先(secondary) |

- NVIDIA 声称 Thor 相对 Jetson AGX Orin 提供 **7.5× AI 算力**与 **3.5× 能效**(primary)。
- Thor T5000 还配有 1 TB NVMe + 100GbE——一份完整的"躯干里的数据中心"规格,不是单片机(primary)。
- Dragonwing IQ10 被设计为可插入 Thor 插座级角色:原生 **12 路 GMSL2 摄像头**(3× MAX96724)+ 激光雷达/ToF/IMU、2×10GBase-T + 2.5G + 4×1G EtherCAT、**8 路 CAN-FD**、Wi-Fi 7 + 5G。10 家早期合作伙伴(含 NEURA Robotics、Thundercomm)于 2026 年 6 月拿到样机(primary)。

### 在位/传统主力

- **Jetson AGX Orin**——275 INT8 TOPS、64 GB、15–60 W、约 $1,999 开发套件——截至 2026 年年中仍是量产机器人中的在位主力(secondary)。Unitree **G1** 标准配置用的是 Orin,**不是** Thor;Unitree **H1-2** 规格表列出最多 3× Jetson Orin NX 搭配一颗 Intel Core i5/i7(secondary)。
- 向 Thor 的迁移刚刚开始,尚未完成:NVIDIA 的 **Isaac GR00T 参考人形机器人**(Unitree 联合设计:H2 Plus + Sharpa Wave + Thor T5000)先面向学术用户,Unitree 面向普通用户的供货定在 **2026-10**(primary)。
- 首个把 Thor 装进人形机器人的设计案例:**Galbot G1 Premium**,声称获得完整的 7.5×/3.5× 提升;Galbot G1 机器人已在**北京 10+ 家药店**自主运行,目标 2026 年底前**全国 100+ 家**(secondary)。

### 中国本土档(价格驱动,大脑-小脑融合)

| 芯片/板卡 | AI 算力 | 显著特点 | 已命名的设计案例 |
|---|---|---|---|
| **D-Robotics RDK S100 / S100P**(Horizon Robotics 子公司;Nash BPU) | 80 / 128 TOPS(INT8) | **大脑+小脑同片**("CPU+BPU+MCU"):6× Cortex-A78AE + Nash BPU + 4× Cortex-R52+(1× DCLS 锁步 + 1× Split-Lock)用于硬实时控制;2025-06-11 发布价 ¥2,799(约 $390) | 宣传为"约 NVIDIA 一半价格、同等算力"(secondary) |
| **D-Robotics Sunrise5/X5** | 约 10 TOPS BPU | 八核 A55 @1.5 GHz,双 4-lane MIPI CSI-2,CAN FD,PoE;中国 BPU 低端标准 | RDK X5 板卡;Quectel SH602HA-AP 模组(primary) |
| **Black Sesame Huashan A2000 + Wudang C1236** | A2000 声称约 4× Orin-X | **两颗芯片**的大脑(A2000,"九霄"NPU)+ 小脑(C1236) | 武汉大学"天问"人形机器人;2026 年 1 月 CES(secondary) |
| **Rockchip RK3588/S** | 6 TOPS NPU | 8 核(4×A76+4×A55),INT4/8/16+FP16;入门档 | AgiBot Lingxi X2、LimX Oli、高擎 Pi/Pi+(secondary) |
| **Huawei Ascend 310 系列** | 单芯片最高 176 TOPS;双芯片 352 TOPS | Orange Pi AI Studio Pro(2×310,192 GB RAM)——**开发套件形态,尚无确认的整机设计案例** | 国产 Thor 级替代方案(secondary) |

- **分脑坍缩**是中国架构的标志性赌注:D-Robotics(Horizon Robotics 的机器人业务分支)的 RDK S100 把认知 AI 与锁步运动控制融合进单颗 SoC;Black Sesame 则保留为两颗专用芯片。两者都在冲击 NVIDIA "大 GPU SoC + 独立 MCU" 的隐含模式(secondary)。
- 中国对 NVIDIA 的价格差是明确的厂商营销说法:D-Robotics 把 RDK S100(80–128 TOPS)定价为"大约同等 TOPS 的 NVIDIA 方案的一半"——注意此处 TOPS 口径不同(Horizon Nash-BPU 的 INT8 TOPS 对比 NVIDIA 的 FP4 稀疏 TFLOPS),所以这是营销说法,不是同口径对比(secondary)。

### 高通中端(模组生态)

- **QCS8550/QCM8550**——48 INT8 TOPS / 12 FP16 TOPS;Kryo 8 核(1×X3 @3.2 GHz + A710/A715)、Adreno 740,第 8 代 AI 引擎支持 INT4/FP16 + transformer "micro-tile inferencing"(primary)。
- 由 **Quectel**(SG885G)和 **MeiG Smart**(SNM970)打包。MeiG 的**双 SNM970** 设计(合计约 100 TOPS)驱动了 **通天晓 / Ultra Magnus** 人形机器人——号称首个全高通 SoC 端侧 AI 人形机器人(合作方 AidLux/阿加犀,2025 年 CES)(secondary)。
- **Thundercomm TurboX IRB10** 把 Dragonwing IQ10 打包进一个人形机器人命名的 SoM:峰值 700 TOPS、20 路并发摄像头(2026 年 Embedded World)——对约 48–100 TOPS 模组档(Quectel/MeiG)的"峰值算力威胁"(primary)。

### 真正的约束:内存带宽墙,而非 TOPS

- 对一个 **70 亿参数的 VLA**(LLaMA-2-7B 规模),要达到 <1 ms/token(>1 kHz 控制响应所需),粗略估算所需内存带宽约为 **13.67 TB/s** *(unverified——这是一个推导数字,不是所引 XPU 特性论文中给出的;数量级取决于精度:一个 FP16 的 7B 模型每 token 读取约 14 GB ⇒ 1 ms 内约需 14 TB/s,4-bit 下约需 4 TB/s)*——大约是 Jetson Thor 273 GB/s 的 **50 倍**。所引论文确实证实了定性主张:在端侧加速器上,VLA 动作专家推理是**内存受限,而非计算受限**(secondary)。
- 固定功能 NPU(高通 NPU、Horizon BPU)能很好地映射 MAC,但**映射不了 attention/softmax/layernorm**,迫使 VLA transformer 层退化到 CPU/DSP——这是高端场景下**GPU 级(Jetson)优于纯 NPU** 的结构性论据(secondary)。
- 具体差距:**LiteVLA-Edge** 报告在 Jetson AGX Orin 上完全端侧的多模态控制达到 **150.5 ms/步(约 6.6 Hz)**——用一个 4-bit(Q4_K_M)SmolVLM-256M 骨干,跑在 llama.cpp CUDA 运行时上,全部 42 层都卸载到 GPU。这远低于 >100 Hz–1 kHz 的全身控制目标。注意这是一个小型(256M)VLM,所以即使一个远小于十亿参数的策略在 Orin 上也只能封顶约 6.6 Hz。这正是**为什么感知/策略与底层关节控制要分开**跑在不同算力上(分脑模式)(secondary)。
- 促使端侧推理的传感器洪流:一台 12 摄像头 + 3D 激光雷达的人形机器人据报生成约 **4.7 GB/s** 原始传感器数据;另有一个独立的 **RISC-V 安全看门狗**核被引用达到 **18 µs 故障安全关机**以满足 IEC 61508 **SIL-3**——*(unverified,单一来源)*。

### 启示

- **是分档,不是一个赢家**:Thor($3.5k,2,070 TFLOPS)→ IQ10/T4000(约 700–1,200)→ 高通模组(约 48–100 TOPS)→ Horizon/Black Sesame(中国中端)→ Rockchip(6 TOPS 入门)。按价格 × 实时带宽预算选型,而非头条 TOPS。
- **规格 TOPS ≠ 控制 Hz**:即使是一个 275-TOPS 的 Orin,跑一个不到十亿参数的 VLA(LiteVLA-Edge,256M,4-bit)也只有约 6.6 Hz;永远要对照实际策略的带宽和算子组合来验证,而非头条 TOPS。
- **架构分野**:NVIDIA/高通卖的是大 SoC 加 MCU;中国(Horizon RDK S100)押注单片大脑-小脑融合——一个值得持续关注的真实分叉。

来源:
- https://developer.nvidia.com/blog/introducing-nvidia-jetson-thor-the-ultimate-platform-for-physical-ai/
- https://nvidianews.nvidia.com/news/nvidia-blackwell-powered-jetson-thor-now-available-accelerating-the-age-of-general-robotics
- https://developer.nvidia.com/blog/accelerate-ai-inference-for-edge-and-robotics-with-nvidia-jetson-t4000-and-nvidia-jetpack-7-1/
- https://www.nvidia.com/en-us/autonomous-machines/embedded-systems/jetson-thor/
- https://nvidianews.nvidia.com/news/nvidia-open-humanoid-robot-reference-design
- https://roboticsandautomationnews.com/2025/08/26/galbot-becomes-first-company-in-the-world-to-integrate-nvidia-jetson-thor-into-a-humanoid-robot/93911/
- https://www.engineering.com/galbot-adopts-nvidia-jetson-thor-for-robotics/
- https://www.semiaccurate.com/2026/06/01/qualcomm-releases-the-dragonwing-iq10-rrd-robotics-platform/
- https://docs.qualcomm.com/doc/87-A0789-1/87-A0789-1_REV_A_Qualcomm_Dragonwing_IQ10_Robotics_Reference_Design_Product_Brief.pdf
- https://www.qualcomm.com/internet-of-things/products/q8-series/qcs8550
- https://www.meigsmart.com/articledetail/496.html
- https://www.thundercomm.com/turbox-irb10-launches-at-embedded-world-2026/
- https://www.cnx-software.com/2025/06/30/d-robotics-rdk-x5-development-board-features-sunrise-x5-octa-core-soc-with-10-tops-bpu-for-ros-projects/
- https://www.hackster.io/news/d-robotics-launches-the-10-tops-edge-ai-rdk-x5-and-teases-the-96-tops-rdk-ultra-c88714dab9d5
- https://eu.36kr.com/en/p/3473485924538759
- https://www.equalocean.com/news/2026010821715
- https://www.cnx-software.com/2025/09/30/orange-pi-ai-studio-pro-huawei-ascend-310-ai-mini-pc-with-up-to-352-tops-192gb-ram/
- https://www.tomshardware.com/tech-industry/artificial-intelligence/orange-pi-ai-studio-pro-mini-pc-debuts-with-huawei-ascend-310-and-352-tops-of-ai-performance-also-features-up-to-192gb-of-memory-but-relies-on-a-single-usb-c-port
- https://www.orientdeck.com/tech-trend/ai-robotics/8895.html
- https://electrek.co/2026/04/15/tesla-ai5-chip-taped-out-musk-ai6-dojo3/
- https://www.notebookcheck.net/Tesla-AI5-FSD-computer-to-run-inference-10x-cheaper-than-Nvidia-AI-chips.1145221.0.html
- https://arxiv.org/pdf/2604.24447 — "Characterizing VLA Models across XPUs":VLA 动作专家推理是内存受限而非计算受限;引用 Jetson Thor 273 GB/s(13.67 TB/s 数字为推导估算,非该论文原文)
- https://arxiv.org/pdf/2603.03380 — LiteVLA-Edge:Jetson AGX Orin 上 150.5 ms/步(约 6.6 Hz),4-bit Q4_K_M SmolVLM-256M,llama.cpp CUDA,42 层全部卸载到 GPU
- https://www.spheron.network/blog/ai-memory-wall-inference-latency-guide-2026/

---

## 功耗 / 散热 / 成本工程 (Power, Thermal & Cost)

端侧大脑不是货架上的免费硅片——它是一个封闭、移动机器人电池预算内的热源。三个约束绑在一起:**每瓦性能**(perf-per-watt)胜过峰值 TOPS,**散热设计**决定真正的持续上限,**成本分层**意味着大多数机器人*不该*买最大的大脑。工程论点是:通过降精度(量化)把同样的瓦数转化为更多可用推理,再设计散热路径让这些瓦数在 SoC 跳闸前真正被排出去。

### 芯片级功耗与能效 (Chip-level power & efficiency)

Jetson AGX Thor 是已在 [hardware.md](hardware.md) 算力表中引用过的参考"大脑"模组;下表数字是它所暴露的设计空间。

| 指标 | Jetson AGX Orin | Jetson AGX Thor (T5000) | 来源 |
|---|---|---|---|
| 功耗范围 | 15–60 W | **40–130 W** | NVIDIA 博客(primary) |
| 峰值 AI 算力 | 275 TOPS INT8 | **2,070 TFLOPS FP4 稀疏** / 1,035 稠密 FP4 / 517 稠密 FP8 | NVIDIA 博客(primary) |
| CPU | 12 核 A78AE | 14 核 Neoverse-V3AE @ 2.6 GHz | NVIDIA 博客(primary) |
| 内存 | 64 GB | 128 GB LPDDR5X | NVIDIA 博客(primary) |
| 代际提升声明 | 基线 | 相对 Orin **7.5× AI 算力,仅 3.5× 能效** | NVIDIA 博客(primary) |

- 关键观察是 **7.5× 对 3.5× 的差距**(primary):从 Orin 到 Thor 这一代,原始算力提升速度大约是能效提升速度的 **2.1 倍**。更大的 VLA 模型想要*不成比例地*更多功耗——除非软件(量化)来弥合这一差距。光靠硅片本身不会带来免费的每瓦性能提升。
- 实际来看,这正是 40–130 W 范围如此宽的原因:同一个模组既可能是跑小策略的 40 W 部件,也可能是跑数十亿参数级 [VLA](vla-models.md) 的 130 W 部件——正如散热一节所示,这两个工作点需要物理上不同的散热硬件。

### 量化换算功耗:软件才是每瓦性能的杠杆 (Quantization as the perf-per-watt lever)

在**固定功耗预算**下,可用速度提升主要来自精度降低,而非新硅片:

| 技术 | 加速比 | 能效/延迟 | 保留的任务质量 | 来源 |
|---|---|---|---|---|
| FP4 量化 + Eagle 投机解码(Qwen2.5-VL-7B,Thor 对比 Orin W4A16) | **最高 3.5×** 推理加速 | — | — | NVIDIA 开发者博客(primary 声明,secondary 聚合) |
| Thor 对比 Orin,生成式 AI(LLM/VLM/VLA)整体 | **最高 5×** 加速 | — | — | NVIDIA 开发者博客(primary 声明,secondary 聚合) |
| INT8 对比 BF16(VLA / 模仿学习策略,Jetson 级 GPU) | **约 1.6×** | **约 1.7×** 能效 | **约 97%** 全精度抓放成功率 | arXiv 2412.01034 / 2505.15304(secondary) |
| INT4 对比 BF16(同上) | **约 2.5×** | **约 2.5×** 能效 | (进一步退化;需用显著性感知量化) | arXiv 2412.01034 / 2505.15304(secondary) |
| GR00T N1 压缩动作 token + 并行解码 | 策略推理**最高 2.5×** 加速 | 单步延迟 **<5 ms** | — | NVIDIA Isaac GR00T 材料(secondary) |

- **"TOPS/W 胜过峰值 TOPS" 在模型层面(而不只是芯片层面)可测量**(secondary):INT8 在保留约 97% 全精度任务成功率的同时,把能耗削减约 1.7 倍——这是量化才是真正杠杆的具体量化证据。INT4 让收益翻倍,但需要显著性感知量化来保护任务质量。
- **实时性差距**(secondary):人形机器人的关节控制器想要**约 1 kHz** 硬实时周期(即 [hardware.md](hardware.md) 中的"分脑" MCU/x86 闭环),而 VLA "大脑" 跑得慢得多。GR00T N1 的压缩动作 token + 并行解码把每步 VLA 延迟压到 **5 ms 以下**,在*同样的功耗预算下*缩小了这一差距——这是架构上的技巧,而不是更多瓦数。
- **不同的轴,不同的硅片**(primary/secondary):每瓦性能是一个独立于峰值 TOPS 的真实设计维度——EnCharge AI EN100 在 200 TOPS INT8 下声称约 **40 TOPS/W**;Hailo-8 以 **2.5–3 W 提供 26 TOPS**(约 9–10 TOPS/W)。这些都处于 Thor 之下的"小脑"档,能效而非头条 TOPS 才是采购标准。

### 散热:真正的持续性能天花板 (Thermal — the true sustained ceiling)

峰值 TOPS 是规格表数字;持续数字则取决于散热路径在跳闸或触发保护前允许多少。

- **硬跳闸,而非软降频**(primary):按 NVIDIA 的 Jetson Thor 散热设计指南(TDG12271001),Thor SoC 的结温额定**不超过 118 °C**,一旦超过就由**硬件热跳闸自动执行系统复位**来强制执行。在一个密封的人形机器人上,这是一种比降频更强的失效模式——散热设计不到位的风险是任务途中**直接重启**,而不仅是变慢。
- **散热质量随 TDP 缩放**(secondary;Advanced Thermal Solutions 的 SOM 散热片,DigiKey + Power Systems Design 均佐证):

| 方案 | 50 °C 环境温度下的额定 TDP | 气流 | 尺寸/质量 | 来源 |
|---|---|---|---|---|
| 被动铝散热片 | 最高 **100 W** | 需要系统气流 **500 LFM** | 87×100.8×20 mm,**168 g** | ATS via DigiKey / PSD(secondary) |
| 主动无边框风扇(fan-in-fin) | **95 W** | 自带风扇 | 87×100.8×20 mm,**104 g** | ATS(secondary) |
| 主动鼓风散热片 | **175 W** | 自带风扇 | 92×100.8×28.6 mm,**174 g** | ATS(secondary) |

  一个标注"40–130 W"的模组,依据它在这一区间中被驱动到什么位置,需要重量/成本明显不同的散热——这是真实的 **BOM 与集成重量**,不是免费的。注意被动 100 W 方案假设有 500 LFM 的强制气流,而一个密封外壳可能提供不了。
- **密封外壳的现实**(unverified,资深分析师框架):密封/追求外观的人形机器人会困热,一项分析估计在 35 °C 的天气下满载 30 分钟内内部温度可超过 **70 °C**,热保护降频会把**最大执行器力矩削减 40%+**——这是一个与算力降频*分开*的负载/操作能力打击。应把具体数字视为方向性的;定性上推向**主动液冷 + 被动散热混合**设计才是启示所在。
- **产业信号**(unverified,单一来源,付费墙):DIGITIMES(2026-05-27)将散热管理描述为人形机器人量产的"**关键瓶颈**"——狭窄的关节结构、有限的散热空间。仅为方向性;无可提取的具体数字。

### 功耗预算与"大脑占比"辨析 (Power budget & the "brain share" question)

一个反复出现的说法(经由 [data.md](data.md) 中已引用的 Witt / New Yorker 文章)是,算力占机器人耗电的**约 60%**,而人脑只占人体能量的**约 20%**。这个框架**取决于负载状态,对一台工作中的机器人来说大体上是错的**:

| 系统状态 | 整机功耗 | Thor 占比(@130 W 上限) | 来源 |
|---|---|---|---|
| 待机/站立 | 250–500 W | **约 26–52%** | Longsing Tech(secondary) |
| 正常行走 | 700–1,500 W | **约 9–19%** | Longsing Tech(secondary) |
| 峰值(抬举/上楼梯/恢复,5–10 秒) | 2,000–4,000 W | **约 3–6%** | Longsing Tech(secondary) |

- 参考电池组:约 **1.99 kWh**(51.8 V,38.4 Ah NMC)——与 [hardware.md](hardware.md) 中约 2 kWh 档一致。只有当机器人**几乎静止**时,算力才占耗电的大头;在移动过程中,**移动本身占主导**(一份聚合估算认为移动占 >70%,算力/"agentic 自主性"约占 **20–25%** 的活跃运行占比——精确归因未证实,但与上文约 9–19% 的行走状态数字一致)。在峰值负载区间,一个 130 W 的 Thor 只占耗电的**约 3–6%**,而不是一刀切的 <5%——在 2,000 W 低端,占比约 6.5%,所以"<5%"只在约 2,600 W 以上才成立。
- **人脑基准**(secondary):大脑约持续 **20 W**,约占人体约 100 W 基础代谢率的 20%。Witt 的对比暗示机器人大脑所占比例*高于*这一数字——但它究竟是否真的超过 20%(更不用说达到 60%)完全取决于活动状态。
- **核实说明(unverified,单一来源,无法再核实确切措辞)**:本轮**无法**独立重新核实 New Yorker 那个具体的"约 60%"数字(付费墙;直接访问与 Wayback 抓取均失败;没有第二来源重复这个确切数字)。建议本 wiki 将其标注为单一来源说法,用负载相关的 Longsing 数字 + 20–25% 区间来做诚实的背景说明,而不是"约 60% 的电池电量流向芯片"。

### 成本分层:大多数机器人不该买最大的大脑 (Cost tiering — don't over-buy the brain)

"小脑档"之所以存在,是因为 AMR/服务机器人需要足够的 TOPS 做导航/感知,但无法为 Thor 级的功耗、散热或价格买单。

| 档位 | 举例 | 算力 | 功耗/价格 | 来源 |
|---|---|---|---|---|
| 大脑档(人形 VLA) | Jetson AGX Thor T5000 | 2,070 TFLOPS FP4 | 40–130 W / **$3,499** 开发套件 | NVIDIA(primary) |
| Thor 中档 | Jetson T4000 | 1,200 TFLOPS FP4 | 40–70 W / $1,999 @1k | NVIDIA(primary) |
| 小脑档(AMR/服务) | Qualcomm RB5(2020)→ RB6 | **15 TOPS → 70–200 TOPS** | 功耗/价格低得多 | Qualcomm(primary + secondary) |
| 超低功耗加速器 | Hailo-8 | 26 TOPS | **2.5–3 W** | 厂商(secondary) |

- 高通的产品线(primary/secondary)显示小脑档从 **15 TOPS(RB5)扩展到 70–200 TOPS(RB6)**——比 Thor 的 2,070 FP4 TFLOPS 低一个数量级,对应更低的功耗和价格。一台整机功耗与成本预算只是人形机器人一小部分的仓储/清洁/配送机器人,没有理由背负一颗 130 W、$3,499 的大脑。
- **设计经验法则**:(1) 把算力档位定在量化后能达到你的控制闭环和任务成功目标的*最小*模型上;(2) 按*持续*而非峰值工作点预算散热路径(尊重 118 °C 硬跳闸);(3) 认识到大脑只是一台工作中机器人功耗的**个位数到约 20%** 这一小部分——移动和执行,而非算力,才是电池消耗的主导者。

来源:
- https://developer.nvidia.com/blog/introducing-nvidia-jetson-thor-the-ultimate-platform-for-physical-ai/(primary — Thor 40–130 W 范围、2,070 TFLOPS FP4、7.5×/3.5× 代际声明、FP4+投机解码 3.5×/5× 加速)
- https://developer.nvidia.com/downloads/assets/embedded/secure/jetson/thor/docs/jetson_thor_thermal_dg_tdg12271001.pdf(primary — 118 °C 结温硬热跳闸/系统复位)
- https://arxiv.org/abs/2412.01034(secondary — Quantization-Aware Imitation Learning:INT8 约 1.6×/约 1.7×,约 97% 成功率;INT4 约 2.5×)
- https://arxiv.org/abs/2505.15304(secondary — Saliency-Aware Quantized Imitation Learning)
- https://github.com/NVIDIA/Isaac-GR00T(secondary — GR00T N1 压缩动作 token,最高 2.5×,<5 ms 单步)
- https://www.longsingtech.com/humanoid-robot-power-system/(secondary — 整机功耗待机 250–500 W / 行走 700–1,500 W / 峰值 2,000–4,000 W;约 1.99 kWh 电池组)
- https://www.digitimes.com/news/a20260527PD226/robot-cooling-production-efficiency-management.html(unverified,单一来源,付费墙——散热"关键瓶颈"框架)
- https://www.qualcomm.com/developer/hardware/robotics-rb5-development-kit(primary — RB5 15 TOPS;RB6 70–200 TOPS 经 5G Americas/ActuIA 二手报道)
- https://www.newyorker.com/magazine/2026/07/06/are-humanoid-robots-ready-to-be-deployed(unverified,关于"约 60%"算力占比数字;已在 data.md 中引用)
- ATS 散热方案 via DigiKey / Power Systems Design(secondary — 被动 100 W、主动风扇 95 W/104 g、鼓风 175 W/174 g);airobotseidos.com / rigidchill.com(unverified — 密封外壳 70 °C/30 分钟,40%+ 力矩降额);神经科学科普来源(secondary — 人脑约 20 W ≈ 约 100 W BMR 的约 20%)

---

## 软件栈 & 运行时 (Software Stack & Runtime)

> 目前**没有标准的"机器人脑 OS"**。事实上的主流技术栈是一个两层切分——一个 Linux+PREEMPT_RT(或厂商 RTOS 增强的 Linux)主机跑感知/规划/VLA 推理,加上一个裸机 MCU/RTOS 负责硬实时电机闭环,二者由 ROS 2(软实时中间件)和各厂商专用加速器运行时(TensorRT / QNN / BPU 工具链)粘合在一起——而这些运行时**跨硅片不可移植**。每个厂商都要自己缝合一套;可移植性是靠反复移植来买单的。

### OS 层:实时性 (Real-time OS layer)

- **PREEMPT_RT 直到内核 6.12 才合入主线**(最终使能提交合并于 2024 年 9 月 20 日;6.12 于 2024 年 11 月发布),结束了约 20 年(rt-patch 工作始于约 2004 年)的树外存在;最终的 printk PR 于 2024 年 9 月的欧洲开源峰会(维也纳)提交给 Linus Torvalds;实时支持首先在 x86 / x86_64、ARM64、RISC-V 上启用。(primary)
  - 对机器人大脑的影响:在 6.12 之前,*每一套*"实时 Linux" 技术栈(包括 Jetson/Ubuntu)都需要单独打一套树外补丁,按内核版本各不相同,且常常落后厂商 BSP 数月——这是一项反复出现的集成税。(primary)
- **PREEMPT_RT 仍然只是*软*实时。** 主流模式是把工作拆开:Ubuntu(通常是 22.04)跑在 AI SoC 上做感知/规划/VLA;一个**专用 MCU/RTOS** 负责亚毫秒级的力矩/伺服闭环,因为标准 Linux 在这些速率下给不出*硬*保证。(secondary)
- **实时内核确实能可测量地帮助 ROS 2**:一项受控基准测试(CJME/Springer)发现,PREEMPT_RT-Linux-ROS2 在各种消息负载大小下的最大延迟明显更小、波动更小,相比原生非实时内核——这是把 ROS 2 和实时内核在机器人 SoC 上配对的标准理由。(secondary)

### 中间件:ROS 2 仍是软实时 (Middleware — ROS 2 remains soft-RT)

- ROS 2 的实时性故事**从根本上是概率性/软实时的,不是硬实时**。截至 2025–2026,学术工作仍在*刻画*(而非解决)执行器/DDS 最坏情况延迟:例如《A Survey of Real-Time Support… in ROS 2》(arXiv 2601.10722)、ReDAG-RT 多 DAG 调度(arXiv 2603.18238)、《Probabilistic Latency Analysis of DDS in ROS 2》(arXiv 2508.10413)。(primary)
- **在默认 DDS/RTPS 下,发现机制随节点数量增长扩展性很差。** 基于 Zenoh 的 `rmw_zenoh` 相比默认 DDS 发现机制,把发现时间削减了**最高 99.97%**——与端侧大脑上多节点的启动时发现相关;PX4 也支持 `rmw_zenoh` 作为 uORB→ROS 2 桥接。(secondary)
- **面向 GPU 密集型流水线的零拷贝——Isaac ROS NITROS**:在节点间传递 GPU 内存句柄(类型适配 REP-2007 / 协商 REP-2009),而不是序列化完整的图像/张量负载,从而避免 CPU↔GPU 拷贝。**注意事项(经文档核实):零拷贝只有当所有 NITROS 节点跑在同一个进程内才成立。**(primary)

### 推理运行时 & 硬件分层 (Inference runtime & hardware tiering)

各厂商专用运行时是机器人大脑领域的"CUDA 时刻"类比物——但它们**不**互操作(Jetson 引擎 ≠ D-Robotics BPU 模型 ≠ 高通 QNN 图)。

| 运行时 | 硅片/角色 | 关键事实 | sq |
|---|---|---|---|
| **TensorRT** | NVIDIA Jetson/RTX/H100 | GPU 架构专用引擎(跨架构不可移植) | primary |
| **TensorRT Edge-LLM** | Jetson Thor/Orin(JetPack 7.1,2026) | 无 Python 依赖的 C++ LLM/VLM 运行时;EAGLE-3 投机解码、NVFP4、分块预填充;已开源(NVIDIA/TensorRT-Edge-LLM);在 Thor 上演示了 Cosmos-Reason2-8B(NVFP4,约 4× 内存削减),在 Orin Nano 上演示了 Qwen3-4B(INT4 AWQ,约 2GB);Bosch/ThunderSoft/联发科在其上构建(2026 年 CES) | primary |
| **QNN / AI Engine Direct**(QAIRT SDK) | Qualcomm Snapdragon 8 Gen2/3/8 Elite、X 系列笔记本、汽车/XR | 取代旧版 SNPE;对 CPU/Adreno GPU/Hexagon NPU 提供逐算子控制 | secondary |
| **BPU 工具链** | D-Robotics RDK X5 | 专有的,与 TensorRT 并行且不互操作 | primary |

**SoC 与模型大小的分档经验法则:**(primary)

| SoC | 目标模型档位 | 备注 |
|---|---|---|
| Jetson AGX Thor 128GB | **20B–120B**(如 Llama 3.2 Vision 70B) | 旗舰人形大脑 |
| Jetson AGX Orin 64GB | **4B–20B** | 主流 |
| D-Robotics RDK X5 | 小型 VLA / 经典 ROS 2 | Ubuntu 22.04,八核 A55 "Sunrise 5",**10 TOPS BPU** + 32 GFLOPS GPU;附带 "NodeHub" 200+ 即插即用 ROS 2 模块(primary) |
| Qualcomm Snapdragon 8 级 | 移动/边缘 | 约 **15 TOPS @ 5–8W**(unverified) |

### VLA 部署:System 1 / System 2 与异步分块 (VLA deployment — S1/S2 split & async chunking)

- **双系统现在是具体的,不再只是一个比喻。** GR00T N1(2025 年 3 月论文):System 2(VLM)在 **10Hz**(NVIDIA L40 上报告),System 1(扩散 Transformer flow-matching 动作头)在 **120Hz**,紧密耦合且端到端联合训练。(secondary)
- **只有 DiT 动作头被 TensorRT 编译**;VLM 骨干(视觉编码器+语言模型)仍留在 PyTorch 中。实测 **GR00T-N1.6-3B** 的 DiT 加速比(NVIDIA 部署文档;该基准表来自 N1.6 发布,而非原始 N1)——引擎是 GPU 架构专用的("在 RTX 4090 上构建的引擎在 H100 上无法工作"):(primary)

| 设备 | PyTorch | TensorRT | 加速比 |
|---|---|---|---|
| RTX 5090 | 58ms / 17.3Hz | 31ms / 32.1Hz | 1.86× |
| H100 | 77ms / 13.0Hz | 36ms / 27.9Hz | 2.14× |
| RTX 4090 | 82ms / 12.2Hz | 43ms / 23.3Hz | 1.92× |
| Jetson Thor | 117ms / 8.6Hz | 92ms / 10.9Hz | 1.27× |
| Jetson Orin | 300ms / 3.3Hz | 173ms / 5.8Hz | 1.73× |

- **动作分块摊薄延迟。** Physical Intelligence **π0** = 约 3B PaliGemma VLM + 300M flow-matching "动作专家";运行在 **50Hz**,一次 **约 73ms** 的前向传播(消费级 RTX GPU 上)发出一个 50 步的 chunk(约 1 秒控制量)。(primary)
- **实时分块(Real-Time Chunking, RTC)**——无需训练、适用于任何扩散/流 VLA:在当前 chunk 执行的*同时*预测下一个 chunk,"冻结"已提交的动作,"内补"其余部分,把新旧动作混合,消除"机器人空转等待下一个 chunk" 的停顿。(primary)
- **LeRobot 异步推理**(RobotClient ↔ PolicyServer)是开放的 S1/S2 参考模式:旋钮 `actions_per_chunk`(默认 50,常见 10–50)与 `chunk_size_threshold`(文档表默认 0.7;推荐 0.5–0.6——当队列填充比例低于该值时发送新观测);重叠部分通过 `aggregate_fn_name=weighted_average` 合并。(primary)
- **策略内存占用决定硬件门槛**:**π0 约 14GB** 推理内存,对比 **SmolVLA 约 2GB**——这是选型端侧算力(Orin Nano 对比 AGX)与可行控制帧率的首要检查项。(primary)

### 碎片化的证据 (Fragmentation, concretely)

- LeRobot——"开放参考栈"——在 NVIDIA/高通硅片上运行仍需要一层**厂商专用移植层**:D-Robotics 提供 **`rdk_LeRobot_tools`**,一个专用 BPU 适配器(PyTorch→ONNX→Horizon 工具链→`.hbm`;面向 RDK X5 "bayes" 和 RDK S100 "nash";**目前仅验证过 ACT 策略**,在 S100 上),而一个 NodeHub 模块若不经过重新移植是无法移植到 Jetson/Isaac ROS 上的。(primary)→ 同一份策略代码,需要 N 个厂商级缝合工作。

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

---

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

---

## 端侧学习 / 自适应 & 数据飞轮 (On-Device Learning & Data Flywheel)

一个出厂即冻结的端侧大脑是一个死大脑。经济上真正决定成败的属性,不是第一天的峰值推理质量,而是**已部署车队自我改进的速度**——即从*部署 → 采集经验 → 整理 → 微调 → 再部署*的闭环。本节区分三种经常被混为一谈的不同机制:(1) **云端规模训练**(需数千条 episode 才能获得一项真正的新技能),(2) **端侧少样本适配**(用几十条示教来校准/适配一项已有技能),(3) **测试时算力**(推理时对*每个动作*多花 FLOPs 来换精度,直接拿控制闭环 Hz 做交易)。这三者共同喂养一个车队级**数据飞轮**,其真正的工程含量在于数据整理、OTA 安全和隐私,而不是模型本身。

### 两种数据机制——云端规模采集 vs. 端侧适配

这个领域被滥用最多的数字是"50 条示教"。这是真实的,但只适用于*适配*,不适用于*新技能获取*。Gemini Robotics 技术报告明确给出了两个界限:

| 机制 | 数据预算 | 换来什么 | 运行位置 | 来源 |
|---|---|---|---|---|
| 端侧少样本适配 | **50–100 条示教** | 对*已有*技能做任务专属的校准/适配;**"8 项任务中的 7 项,微调后成功率在最多 100 条示教下达到 70% 以上"**(逐任务分解见图 26;未报告明确的跨任务平均值 *(unverified:">60% 平均" 是插值推断)*) | 机器人本地(Gemini Robotics On-Device) | arXiv:2503.20020(primary) |
| 云端规模技能获取 | **每任务 2,000–5,000 条 episode** | 真正的新长时程/灵巧技能 | 云端训练 | arXiv:2503.20020(primary) |

**Gemini Robotics On-Device**(Google DeepMind,**2025-06-24** 发布)是 Gemini Robotics 家族中首个开放微调的 VLA,它**完全在机器人自带算力上本地推理,"不依赖数据网络"**(对间歇/零连接场景鲁棒);开发者通过 Gemini Robotics SDK(MuJoCo 仿真 + "受信测试者"项目)进行微调(primary)。*(注:DeepMind 确认的是网络无关的**推理**;并未明确说明**微调**这一步本身是否离线运行——"完全本地训练、无需网络" 为 (unverified)。)* 这在架构上不同于**完整的云混合 Gemini Robotics** 模型,后者是一个**快慢分离设计**:一个大型云端托管的 VLA 骨干(从 Gemini Robotics-ER 蒸馏而来)配一个**本地底层动作解码器**。该混合方案报告了约 **250 ms** 的端到端观测→动作 chunk 延迟、**有效 50 Hz** 的控制频率(每个 chunk = 多个动作),以及通过蒸馏到更小的机载解码器,把骨干查询→响应延迟从"数秒"降到 **160 ms 以下**(primary)。*启示:"端侧 50 条示教" 和 "云混合 250 ms" 描述的是两种不同的产品;不要把它们混为一谈。*

### 持续学习——灾难性遗忘真的是敌人吗?

两个对立的发现,都值得记住:

- **显式的架构隔离。** Physical Intelligence 的**"知识绝缘 (Knowledge Insulation)"**(随 **π0.5 + KI** 引入;arXiv:2505.23705):VLM 骨干在 π0-FAST 离散动作 token + 网络数据协同训练目标上训练,而一个*独立的动作专家*产生连续动作(flow/扩散),且**其梯度被"停止梯度"阻断,不会流回 VLM 骨干**——"来自动作专家的梯度不会流入 VLM 骨干"。这是针对动作微调过程中语义/语言遗忘的梯度隔离——不是重放缓冲区,不是 EWC 式正则化(primary — pi.website/research/knowledge_insulation,arXiv:2505.23705)。*(π0.6,2025 年 11 月,沿用了同一套 PI 配方血统;"知识绝缘" 这一明确命名记录在 π0.5 上——π0.6 的归属为 (unverified)。)*
- **反叙事:VLA 或许不需要重型机制。** 一项 **2026 年**的 arXiv 研究(Liu 等)发现,预训练 VLA 模型相比从零开始训练的小策略基线,**"在持续学习中对遗忘出人意料地有抵抗力"**。它实际的机制是在监督式持续模仿学习中使用简单的**经验回放 (Experience Replay, ER)**——*不是*一个无需抗遗忘机制的结果,也*不是*在线策略强化学习。核心发现是:**大规模预训练改变了动态过程**,使得 ER 用**极小的回放缓冲区(约 2% 数据)**就能实现接近零的遗忘,而从零训练的模型需要 **>20%**;"遗忘"的技能也能通过最少的微调快速恢复(secondary,单一来源——arXiv:2603.03818)。*注意事项:这仍然与经典的强化学习/视觉持续学习结果相矛盾(在那些结果里遗忘是严重的);应视为 VLA 特有的、暂定的结论——并且要注意它确实仍然使用了一个回放缓冲区。*

**工程解读:** 当单个模型必须同时保持语言和运动能力时,绝缘式方法(π 风格)是安全的默认选择;"对遗忘有抵抗力"的结果很有前景,但还不足以据此设计系统。

### 车队规模强化学习与闭环("边部署边学习")

- **LWD** 在**16 台双臂机器人**组成的车队上、**8 项真实操作任务**中闭合了 部署→共享经验→改进→再部署 的循环,达到 **95% 的平均成功率**(primary — arXiv:2605.00416)。机制:**DIVL**(Distributional Implicit Value Learning,分布式隐式价值学习)用于稳定的价值估计 + **QAM**(Q-learning via Adjoint Matching)从基于流的 VLA 模型中提取策略,由自主 rollout **加上人工干预** 的车队级数据共同驱动——即**离线到在线强化学习**,而非模仿学习。核心要点:*人工干预是一等公民的数据来源*,而非兜底方案。

### 数据飞轮的量化(Scanford /「机器人驱动的数据飞轮」)

文献中最清晰的端到端飞轮测量:

| 阶段 | 具体数字 | 来源 |
|---|---|---|
| 部署 | Franka FR3 + TidyBot++ 底座,**10 天 × 每天 4 小时 = 40 小时**扫描图书馆书架 | arXiv:2511.19647(primary) |
| 人工成本 | 仅 **26 次干预**总计(约 2.6 次/天,每次 **<5 分钟**);估计节省 **18.7 小时**人工 | 同上 |
| 整理 | **8,232** 张原始标注图像 → 通过字符串相似度数据库匹配后得到 **5,019** 张训练图像 | 同上 |
| 域内提升 | 一次微调周期后准确率 **32.4% → 71.8%** | 同上 |
| 相邻域提升 | OCR 弱得多:英文 **24.8%→46.6%**,中文 **30.8%→38.0%** | 同上 |

**教训:** 飞轮真正的工程含量在于**自动化整理**(过滤掉约 39% 的原始图像)以及**域内 vs. 相邻域的差距**——飞轮在确切的部署分布上收敛很快,而在相邻能力上则慢得多。

### 测试时算力——用 Hz 预算换精度

面向机器人的 System-2 问题是一个资源分配问题:每一份多花在推理上的采样/迭代都会从控制频率中扣掉。量化的权衡如下:

| 方法 | 花费的算力 | 精度提升 | 延迟/Hz 代价 | 来源 |
|---|---|---|---|---|
| **RoboMonkey** | 采样 **16 个动作** + 高斯扰动验证器 | OOD **+25 分**(60% vs. OpenVLA 35%);误差随采样数呈幂律下降,跨 CogACT/Octo/OpenVLA/SpatialVLA | 单张 H100 上 **+约 650 ms**(相对朴素方案 -41.3%);真机约 **1.5 Hz** | arXiv:2506.17811(primary) |
| **E-TTS** | 协同缩放推理+动作采样,带历史感知验证 | 成功率**相对提升 150%**(最优配置) | 延迟仅 **+46.6%** | arXiv:2606.27268(secondary) |
| **Recurrent-Depth VLA** | 潜空间迭代推理(非 token 思维链) | 任务从 **1 次迭代 0% → 4 次迭代 >90%**;简单任务很快饱和 | 避免了 token 思维链的内存/延迟开销;为端侧预算设计 | arXiv:2602.07845(secondary) |

**关键架构答案**——主流的调和方案是**双系统(System-1/System-2)**切分:一个大型 VLM "慢系统" 在 **约 1–9 Hz** 做场景/语言/规划,一个轻量(常为扩散式)"快系统" 做电机控制(通常 **20–50 Hz**,极端情况下最高 **200 Hz**)。Figure **Helix**:机载 VLM System-2(7B)在 **7–9 Hz**,配一个 **200 Hz 运行的 80M System-1**(它的快端*远高于* 20–50 Hz 区间——不要把 Helix 的快闭环归入 20–50 Hz 那一档);HiRT / RoboDual / OpenHelix / FiS-VLA / UniFS 遵循更典型的 **1–5 Hz 慢 / 20–50 Hz 快** 切分(secondary — figure.ai/news/helix,arXiv:2506.01953 + 双系统 VLA 文献)。RoboMonkey 的约 1.5 Hz 说明为什么朴素的 16 采样验证是一种*慢系统*技术——它无法活在快闭环里。

**预算上限:** 上述所有方案若要在本地运行(而非通过云端骨干),都必须装进 **NVIDIA Jetson Thor**——最高 **2,070(稀疏)FP4 TFLOPS**(1,035 稠密)、**128 GB** LPDDR5X、**40–130 W**;相对 Jetson AGX Orin **最高 7.5× AI 算力**与 **3.5× 能效**,以及"生成式 AI 模型最高 5×"——但这个 5× 是跨 LLM/VLM/VLA 的*最大值*;实测的 **VLA(GR00T N1.5)加速比约为 2.74×**,不是 5×(primary — NVIDIA 开发者博客)。RoboMonkey 的 16-采样验证器是为 **H100** 预算的,不是 Thor;端侧测试时缩放因此必须偏爱*廉价*方案(潜空间循环迭代)而非*采样密集型*方案(16× 验证)。

### 车队运维——飞轮的管路(遥操作、OTA、隐私)

- **遥操作即飞轮(1X NEO "专家模式")。** 人类操作员远程驾驶机器人完成尚不能自主的任务;**每一次遥操作会话都被记录、标注,并喂给 Redwood 模型**(CEO Børnich:"第一台 NEO 会比第一千台 NEO 能力弱")。已披露的隐私缓解措施:操作员需要机主授权,视频可打码,机主自定义禁入区域,未经批准不得接管——被定位为一种"社会契约"(secondary — therobotreport / engadget)。
- **车队 OTA + 跨机器人迁移(Figure)。** 通过 OTA 对整个车队同时推送行为更新,配合**跨机器人策略迁移**(在一台机器人上训练的策略无需逐机器人微调即可应用到许多台上)——把飞轮经济学与产能爬坡绑在一起:更多机器人 → 更多车队小时数 → 更多失败案例 → 更多 Helix 训练数据(secondary — figure.ai/news/helix)。
- **OTA 安全 = 分级金丝雀发布。** 最佳实践:先推给车队的**约 1%**,监控开机成功率/心跳/传感器数据质量;只有正常才推进到 **10%+**;逐设备状态链(已下载→已验证→已应用→已启动→健康检查通过);健康检查失败后**自动回滚**,无需人工介入(secondary — roboticscenter.ai;arXiv:2605.28097 "ICAN-Deploy")。
- **隐私:联邦学习(方案)。** 车队学习的正式隐私机制是**联邦学习**——原始传感器/交互数据永不离开设备;只有模型权重更新在中心聚合(如安全聚合/差分隐私噪声)(secondary;*源文本在研究中被截断——应视为方向性,引用前需核实具体聚合方案*)。

### 启示

把大脑设计成能**出厂后继续学习**,并把三种机制分开度量:(1) 为新技能获取保留云端训练(**2,000–5,000 条 episode**),(2) 为逐场地校准提供**端侧少样本适配**(**50–100 条示教**),(3) 把**测试时算力**作为一种*慢系统*资源来预算(双系统 1–9 Hz / 20–50 Hz),本地场景下优先用潜空间迭代而非采样密集型验证。飞轮的工程价值体现在**自动化整理**(Scanford 从 8,232 过滤到 5,019)和**车队安全管路**(金丝雀 OTA + 回滚)上,而**遥操作干预**是一等公民的训练数据,**联邦学习**是让家庭部署在社会层面可被接受的隐私叙事。

来源:
- https://deepmind.google/blog/gemini-robotics-on-device-brings-ai-to-local-robotic-devices/
- https://arxiv.org/html/2503.20020v1(Gemini Robotics 技术报告)
- https://www.pi.website/research/knowledge_insulation ; https://arxiv.org/pdf/2505.23705(知识绝缘——随 π0.5+KI 引入;"停止梯度" 把动作专家的梯度与 VLM 骨干隔离); https://website.pi-asset.com/pi06star/PI06_model_card.pdf(π0.6 血统)
- https://arxiv.org/pdf/2603.03818(VLA "对遗忘有抵抗力",secondary/单一来源)
- https://arxiv.org/abs/2605.00416(Learning While Deploying,DIVL + QAM)
- https://arxiv.org/html/2511.19647v1(Robot-Powered Data Flywheels / Scanford)
- https://arxiv.org/html/2506.17811(RoboMonkey)
- https://arxiv.org/html/2606.27268v1(E-TTS)
- https://arxiv.org/pdf/2602.07845(Recurrent-Depth VLA)
- https://arxiv.org/html/2506.01953v1(Fast-in-Slow)+ 双系统 VLA 文献
- https://blogs.nvidia.com/blog/jetson-thor-physical-ai-edge/ ; https://developer.nvidia.com/blog/introducing-nvidia-jetson-thor-the-ultimate-platform-for-physical-ai
- https://www.therobotreport.com/teleop-not-autonomy-the-path-for-1x-neo-humanoid/ ; https://www.engadget.com/ai/1x-neo-is-a-20000-home-robot-that-will-learn-chores-via-teleoperation-040252200.html
- https://www.figure.ai/news/helix ; https://www.figure.ai/news/helix-logistics
- https://www.roboticscenter.ai/learn/remote-robot-fleet-management-guide ; https://arxiv.org/pdf/2605.28097(ICAN-Deploy)

---

## "做好"的判据 & 评价 (What Makes an On-Device Brain Good)

前面每一节讲的都是*怎么*造大脑;这一节定义*它好不好*——并揭示这一领域目前**无法用公开数据回答这个问题**。诚实的总结是:存在一场**基准危机**(自我报告的数字,没有同口径的任务集),叠加在一场**评价危机**之上(几乎没有公开的 MTBF/干预率披露)。采购者的工作是把营销 Hz/TOPS 转化为一张记分卡,**每个数字都要挂一个具体硬件型号**,**每个成功率都要挂一个占空比**。本节给出这张记分卡、它的锚点数字,以及数字缺失的地方。

### 记分卡(七维判据)

七个维度。每格把一个*可要求的指标*与最好的公开锚点及其来源质量标签配对。**经验法则:拒绝任何没有绑定具体 SoC 型号、且不是持续(而非突发)占空比的 Hz/TOPS 数字。**

| 判据 (axis) | 可要求的指标 | 公开锚点(现有最好数据) | 标签 |
|---|---|---|---|
| **实时性 Real-time** | *出货*模组上的 S1 控制频率,而非桌面 GPU | S1 200 Hz / S2 7–9 Hz(Figure Helix,但 S1 = 仅 80M 参数);完整 7B VLA 在 Jetson AGX Orin @INT4 上约 3 FPS | (primary) |
| **延迟 Latency** | 模组型号上的端到端感知→动作 ms | LiteVLA-Edge 150.5 ms(约 6.6 Hz)Jetson 级;LiteVLA-H 单台 AGX Orin 上外环 19.74 Hz / 语义感知 6.08–6.67 Hz(最好的端侧双速率结果) | (primary) |
| **泛化 Generalization** | 分任务类别的 OOD 实例/空间/语言成功率 | π0:Clean-Dish 87% vs. Unzip-Bag 67%(同分布内的散布);ACT 86%→约 12%(未见过的餐具);预训练 Qwen-VLA 在 OOD 语言上超过 π0.5,确切 32.0%/12.6% 数字 *(unverified)* | (primary) |
| **可靠性 Reliability** | 8 小时×5 天占空比下的 MTBI / MTBF;在线率 % | AutoInspect MTBI **78 小时**(非人形);工业目标 95–99% 在线率;人形机器人目前每充一次电 30–90 分钟;安全关键门槛 = 99.999% | (primary 锚点 / secondary 目标) |
| **功耗热 Power/thermal** | 持续负载下*持续*的 W 和 TOPS/W | Jetson AGX Thor 40–130 W,≤2,070 FP4 TFLOPS,128 GB,相对 Orin 约 3.5× 每瓦性能;Hailo-8 约 26 TOPS @2.5–3 W(约 10 TOPS/W,ASIC) | (primary / secondary) |
| **成本 Cost** | $/TOPS,大脑占系统 BOM 的百分比 | 芯片约占人形机器人 BOM 的 8%(2025)→ 到 2035 年约 5%;每台约 $1,400 半导体 BOM(UBS);总 BOM 约 $35k,执行器占 >30%(BofA) | (secondary) |
| **可更新 & 安全 Updatability/Safety** | OTA 节奏,金丝雀 vs. 全车队同推,认证兜底 | SSE→MRC 正式安全停止方案(arXiv 2603.22703);ISO 10218:2025 把停止距离与延迟+控制频率绑定;Optimus 夜间全车队 OTA(厂商声明) | (primary / unverified) |

### 锚点 1 ——实时性/延迟鸿沟

评价层面最有分量的一个事实:**在真实端侧硅片上,全尺寸 VLA 跑得比灵巧操作所需的速度慢 5–30 倍**,而论文里看到的快速率通常是桌面 GPU 上的速率。

- **量产级双速率确实存在,但只能靠缩小 S1 才做到。** Figure Helix 把 S2(互联网预训练 VLM)跑在 **7–9 Hz**,S1(反应式视觉运动策略,**80M 参数**)跑在 **200 Hz**,覆盖上半身 **35 自由度**(primary,figure.ai/news/helix)。更广泛的双系统综述给出慢端 **1–5 Hz** / 快端 **20–50 Hz**(primary,arXiv 2510.24795)。关键注意事项:200 Hz 是在 *80M 参数* 下实现的,不是用一个完整的 VLA。
- **端侧全尺寸 VLA 远低于控制频率。** OpenVLA(**7B**)即使 INT4 在 Jetson AGX Orin 上也**只有约 3 FPS**(primary)。LiteVLA-Edge:在 Jetson 级 ROS2 流水线上平均端到端 **150.5 ms**(约 **6.6 Hz**);LiteVLA-H:在单台 **AGX Orin** 上外环动作发出 **19.74 Hz**,语义感知 **6.08–6.67 Hz**——是目前报告的最好*端侧*双速率结果(primary,arXiv 2511.05642 / 2603.03380 / 2605.00884)。
- **提防"GPU 级 Hz"。** 并行/异步解码(PD-VLA)把 VLA 延迟削减**约 2.5 倍**(2.52 倍动作频率加速),推向 **100–200 Hz**——但是在**桌面级 GPU** 上,不是端侧模组(primary,arXiv 2503.02310;综述见 2505.04769)。这正是记分卡要求"标明具体型号"这条规则的原因。

见 §E(实时控制切分)了解这些切口在硅片上落在哪里,§I(端侧原生模型)了解让 200 Hz S1 成为可能的模型收缩手段。

### 锚点 2 ——泛化记分卡(泛化崩塌)

成功率**不是一个数字**;同一个策略在不同任务类别间摆动 40 多分,模仿学习基线在 OOD 迁移下会崩溃。

| 策略 | 指标 | 数字 | 标签 |
|---|---|---|---|
| π0 | 同分布内任务散布 | **87%** Clean-Dish vs. **67%** Unzip-Bag vs. **52%** Folding-Shorts(200 条示教) | (primary) |
| ACT | 标准 → 未见餐具(OOD 实例) | **86% → 约 12%**(降 74 分) | (primary) |
| Qwen-VLA vs. π0.5 | 平均 OOD *语言*条件下成功率 | 一个预训练的 Qwen-VLA 在 OOD 语言上超过 π0.5;确切的 **32.0% / 12.6%** 这一对数字为 *(unverified——在所引来源中未找到)* | (unverified) |
| GR-Dexter(跨本体) | 未见物体 / 未见指令 | **0.85 / 0.83** | (primary) |

由此直接得出的采购者检查清单:(1) 要求*分任务类别*的成功率,而非一个头条平均值;(2) 询问该策略是否**跨本体训练**——GR-Dexter 的 0.83–0.85 OOD 相对单本体基线,表明这是一个可测量的杠杆(primary,arXiv 2512.24210);(3) 把任何低于约 30% 语言跟随的 OOD 数字视为当前*领域*的地板,而不是某个厂商的缺陷。来源:arXiv 2511.11298(π0/ACT)。*注意事项:那个具体的"Qwen-VLA-Instruct 32.0% vs. π0.5 12.6%"数字对,既未能在 arXiv 2505.15660(即 X-ICM 跨任务上下文模仿,与该数字无关)中找到,也未能在 Qwen-VLA 论文 2605.30280(报告 Qwen-VLA-aloha 平均 OOD 76.9% vs. π0.5 41.5%,也不是 32.0/12.6)中找到——32.0/12.6 这一对数字应视为 (unverified)。*

### 锚点 3 ——可靠性数据缺口

这是行业**最不老实**的一个维度,因为几乎没人公布 MTBF。

- **从演示到 24/7 之间的差距是量化的。**"舞台走秀"式的成功率对比"每天 8 小时、每周 5 天、无人干预"——一个经过精心策划、成功率 >90% 的演示**不**意味着车队级可靠性(secondary,therobotreport/mindstudio)。
- **占空比现实。** 工业买家期待 **95–99%** 在线率,而大多数人形机器人今天在充电/干预前只能运行 **30–90 分钟**,电池化学特性把持续使用上限压在 **1–4 小时**(secondary,awesomerobots.xyz / patentpc.com)。功耗/散热与机械故障会与 AI 大脑故障**叠加**。
- **公开 MTBF 几乎为零。** 最干净的、有明确日期的公开数字是 AutoInspect 的 **MTBI = 78 小时**(长期自主工业*巡检*,非人形但有启发意义)(primary,arXiv 2404.12785)。对照安全关键的 **99.999%("五个九")** 期望目标(secondary,patentpc.com),人形机器人/VLA 厂商的 MTBF **基本上未发布**——这个空缺本身*就是*发现。

### 锚点 4 ——如何真正做基准测试(评测方法学)

因为自我报告的数字不可比较,方法学本身就是一项评判标准。

- **可复现性问题是结构性的。** 大多数 VLA/策略结果使用实验室专属的硬件、任务定义和成功率指标;即使共享相同的物体集,摄像头/光照/硬件的差异也会导致——已发表的成功率**不是同口径**的(secondary,arXiv 2510.04354 / 2508.11117)。
- **目前领先的解决方案:RoboArena。** 去中心化的、**双盲成对**真机评测,横跨 **7 个机构**,基于共享的 **DROID** 平台,把 **600+ 组成对 episode**(更大数据集中总计 **4,284** 次评测 episode)汇总到 7 个通才策略上,形成一个类 ELO 排名——这是"如何为一个无法固定任务清单的通才策略做基准测试"的直接答案(primary,arXiv 2506.18123)。采购者应优先选择数字来自**第三方成对评测**而非自跑固定任务演示的厂商。

见 [evaluation](evaluation.md) 和 [open-problems](open-problems.md) 了解全领域的基准测试讨论。

### 锚点 5 ——成本、功耗、可更新性与安全(成本 / 功耗 / 更新 / 安全)

- **大脑不是成本杠杆。** 算力约占人形机器人 BOM 的 **8%(2025)→ 到 2035 年约 5%**;每台约 **$1,400** 半导体 BOM,到 2050 年上升到约 $2,000(UBS);总 BOM 约 **$35k**,**执行器占 >30%**(简单配置下 >50%)(secondary,UBS / BofA 2025 年 4 月)。优化 $/TOPS 远不如执行/机械重要——但功耗/散热仍然决定占空比。
- **功耗/散热:要求持续而非突发数据。** Jetson AGX Thor 在 **40–130 W** 区间提供最高 **2,070 FP4 TFLOPS** / 128 GB,相对 Orin 约 **3.5× 每瓦性能**——要问工作负载在**持续**负载下落在这一区间的哪个位置(primary,nvidia.com)。对比 Hailo-8 约 **26 TOPS @2.5–3 W(约 10 TOPS/W)**——专用 ASIC 在 TOPS/W 上占优,但无法承载大型 VLA/VLM(secondary,hailo.ai)。见 §G(功耗与散热)。
- **可更新性 = 一个带风险标记的车队学习闭环。** Tesla Optimus 被描述为"把经过验证的模型权重更新……一夜之间推送给所有 Optimus 单元"(Cortex 相当于 67k+ 台 H100、每周期 70k GPU 小时、每任务 10k+ 合成变体)——但来源是一个**粉丝/分析师博客**,所以应把这些数字视为**厂商声明(unverified)**。可要求的项目:OTA *节奏*、**金丝雀/分级发布 vs. 全车队同步发布**(同步发布在回归风险上更大),以及任何适配是端侧完成还是云端训练后推送。见 §J(端侧学习)。
- **安全必须具备控制能力,且对延迟敏感。** 正式的锚点是一个**安全可停止包络 (Safe-Stoppable Envelope, SSE)**:一个状态集合,从中一个经过认证的兜底控制器能到达一个动态稳定的**最小风险状态 (Minimum Risk Condition, MRC)**,并有监控器检测包络偏离(primary,arXiv 2603.22703)。**ISO 10218:2025** 现在明确要求功能安全,并要求保护分离距离的计算必须包含**系统延迟和控制闭环频率**——把延迟维度直接与认证安全绑定,所以一个慢的大脑*字面意义上*就是一个更不安全的大脑(primary/标准)。见 [safety-regulation](safety-regulation.md)。

### 启示

一个"好"的端侧大脑,**不是**头条 TOPS 或 Hz 最大的那个。它是这样一个大脑:(1) 在*出货 SoC* 上、在持续负载下维持其 S1 控制频率(Figure 的 200 Hz 基准——但注意那是 80M 参数,完整 VLA 在 Jetson 上仍只能爬到 3–7 Hz);(2) 报告*分任务类别*的 OOD 成功率,并且是**跨本体训练**的;(3) 能展示一个**第三方成对**评测(RoboArena 式),而非自跑演示;(4) 在 8 小时×5 天占空比下公布 **MTBF/干预率**——今天几乎没有厂商做到这一点;(5) 出货一个**经认证的、具备控制能力的安全停止**,其停止计算已经把大脑延迟考虑在内。大脑只占 BOM 的约 5–8%,所以把这五件事做对的回报是不成比例的高。厂商引用的每一个数字都应该带一个**型号和一个占空比**——缺失本身就是答案。

来源:
- https://www.figure.ai/news/helix
- https://arxiv.org/pdf/2510.24795(Survey on Efficient VLA Models)
- https://arxiv.org/pdf/2511.05642(Lite VLA) ; https://arxiv.org/pdf/2603.03380(LiteVLA-Edge) ; https://arxiv.org/html/2605.00884(LiteVLA-H)
- https://arxiv.org/abs/2503.02310(PD-VLA — 并行解码,2.52× 动作频率加速,桌面 GPU) ; https://arxiv.org/html/2505.04769(VLA Models 综述——引用 PD-VLA,GPU 级 Hz 注意事项)
- https://arxiv.org/pdf/2511.11298(Experiences from Benchmarking VLA Models — π0 同分布内 87/67/52%,ACT 86%→12% OOD;已对照表 3 核实)
- https://arxiv.org/html/2505.15660(Exploring the Limits of VLA Manipulations in Cross-task Generalization / X-ICM——不含 32.0/12.6 的 Qwen 数字) ; https://arxiv.org/abs/2605.30280(Qwen-VLA——报告 76.9% 平均 OOD vs. π0.5 41.5%,同样不是 32.0/12.6)
- https://arxiv.org/pdf/2512.24210(GR-Dexter 技术报告——跨本体 0.85/0.83)
- https://arxiv.org/pdf/2404.12785(AutoInspect — MTBI 78 小时)
- https://arxiv.org/abs/2506.18123(RoboArena — 分布式双盲成对真机评测)
- https://arxiv.org/html/2510.04354 ; https://arxiv.org/html/2508.11117(可复现性 / sim-to-real 评价)
- https://www.therobotreport.com/ ; https://mindstudio.ai(人形部署差距分析——secondary)
- https://awesomerobots.xyz(Enterprise Humanoid Robots Guide 2026) ; https://patentpc.com(Robot Downtime Rates & Reliability Data)
- https://www.nvidia.com/en-us/autonomous-machines/embedded-systems/jetson-thor/ ; https://thinkrobotics.com(Jetson AGX Thor 评测)
- https://hailo.ai/blog/evaluating-edge-ai-processor-in-the-generative-ai-era
- UBS 人形机器人半导体分析(via financialmodelingprep.com) ; https://institute.bankofamerica.com(Humanoid Robots 101,2025 年 4 月)
- https://optimusk.blog/blog/tesla-optimus-software-update(粉丝/分析师博客——厂商声明未证实)
- https://arxiv.org/pdf/2603.22703(Learning Safe-Stoppability Monitors for Humanoid Robots — SSE/MRC)
- ISO 10218:2025 修订版(功能安全;停止距离必须包含延迟+控制频率)

---

## 参考架构 & 模组厂视角 (Reference Architecture & the Module-Maker Read)

> 从双系统模型(见 §A,架构)和 SoC 菜单(见 §F,SoC 版图)后退一步看,这一领域已收敛到一个任何端侧大脑都必须物理落地的**三层控制层级**:一个 **S2 深思型 VLM**(7–10 Hz)、一个 **S1 反应型视觉运动策略**(100–200 Hz)、以及一个 **S0 硬实时电机/反射闭环**(500 Hz–1 kHz)。S2/S1 活在 AI SoC 上;S0 活在一个确定性 MCU / 协处理器 / 安全岛上,与 Linux 时钟域解耦。对模组厂(模组厂)而言,最有分量的洞察是:**难点不在 TOPS 数字**——而在于把这个异构的、按抖动切分的、不可移植的技术栈,缝合成一个内置连接性与功能安全的、可出货的模组。

### 收敛出的三层参考技术栈

| 档位 | 角色 | 频率 | 硅片/时钟域 | OS/运行时 | 延迟预算 |
|---|---|---|---|---|---|
| **S2** 深思 | 场景/语言理解、规划 | **7–10 Hz** | AI SoC GPU(Jetson)或 NPU+CPU | Ubuntu + PREEMPT_RT;TensorRT/QNN/BPU | 每步约 100–140 ms 可接受;可上云 |
| **S1** 反应 | VLA/视觉运动策略 → 连续动作 chunk | **100–200 Hz** | AI SoC GPU/NPU | 同一 SoC,软实时(ROS2) | **120 Hz 下 8.3 ms**——必须本地 |
| **S0** 硬实时 | 关节/力矩/伺服环、反射、安全停止 | **500 Hz–1 kHz+** | 确定性 **MCU / RTOS / 安全岛** | 裸机 / RTOS | **亚毫秒**,不容忍任何 OS 抖动 |

- **Figure Helix(primary)**:S2 = 7B 互联网预训练 VLM @ 7–9 Hz;S1 = 80M 交叉注意力编解码 transformer @ 200 Hz;S2 把**单个连续潜向量**发给 S1 的 token 空间;两者**全部机载,跑在双低功耗嵌入式 GPU 上**。[figure.ai/news/helix]
- **NVIDIA GR00T N1(primary)**:S2(Eagle-2 VLM)@ **10 Hz**(论文在一台 NVIDIA L40 上做的基准);S1(扩散 transformer,flow-matching 动作头)@ **120 Hz**;两个模块**端到端联合训练**。公开的 GR00T-N1-2B = 共 2.2B 参数(VLM 内 1.34B)。二者之下是一个约 1000 Hz(GR1 级)的全身力矩环,卸载到 MCU/RTOS。[arXiv 2503.14734]
- S0 档正是**无法容忍软件/OS 抖动**的那一层——因此被物理放逐到一个独立的确定性协处理器。这正是中国单片 SoC(D-Robotics RDK S100:6× A78AE + BPU + **4× Cortex-R52+ 锁步**)试图在保留 R52 核处于片上**独立硬实时孤岛**的同时,把这个边界折叠到一个封装里的同一条边界(secondary)。(见 §F,SoC 版图)

### S0 现场总线:反射档如何与执行器通信

- S0 闭环跑在 **EtherCAT 和/或 CAN-FD** 现场总线上,**与 Linux/AI SoC 时钟域解耦**(secondary):
  - EtherCAT 人形控制架构达到 **1 kHz 更新、控制频率 >2 kHz、I/O 延迟 <1 ms**;EtherCAT 从站在 **1 kHz–9 kHz** 范围内验证无误码(secondary——researchgate/mediatum 人形论文)。
  - **CAN-FD** 被描述为非常适合需要确定性时序的同步多轴机器人系统(secondary——TI slla659a)。
  - 灵巧手数据点:**BrainCo Revo 2** 支持最高通信频率 **1 kHz,跨 RS-485、CAN-FD、EtherCAT 均如此**(secondary)。
- 模组厂读数:旗舰算力 SoC 现在已内置这些总线——**Qualcomm Dragonwing IQ10** 提供 **EtherCAT(4× 1G Base-T)** + **8× CAN-FD**(4 路原生 + 4 路经 SPI 外接)+ TSN-ready 以太网 + 一个分段的 **2.5G Base-T 安全域(SAIL)链路**;现场总线不再是一个外挂的 FPGA(primary——docs.qualcomm.com IQ10 产品简报 87-A0789-1 Rev. A)。

### S1/S2 的高端硅片选择(另见 [SoC 版图]

| SoC | 峰值 AI | 内存/带宽 | 功耗 | 价格 | S0 方案 |
|---|---|---|---|---|---|
| **Jetson AGX Thor(T5000)** | 2,070 FP4 稀疏 TFLOPS;Blackwell(2,560 CUDA+96 Tensor);14 核 Neoverse-V3AE | 128 GB LPDDR5X @ **273 GB/s** | 40–130 W | $3,499 开发套件;GA 2025-08-25 | 独立 MCU(隐含) |
| **Jetson T4000** | 1,200 FP4 TFLOPS | 64 GB LPDDR5X | 40–70 W | 约 $1,999 @1k;2026 年 CES | 独立 MCU |
| **Qualcomm Dragonwing IQ10** | 约 700 TOPS 稀疏(18 核 Oryon CPU + NPU + GPU) | 64 GB LPDDR5x | 12/24 V | 2026 年 6 月早期接入;2026 年 9 月量产 | **片上安全岛(SAIL)** |

- Thor 声称相对 Orin 有 **7.5× AI 算力 / 3.5× 能效**;配有 1 TB NVMe + 100GbE;NVIDIA 自己的 **Isaac GR00T 参考人形机器人** = Unitree H2 Plus + Sharpa Wave 手 + 机载 Thor + Isaac GR00T 软件(primary)。
- **IQ10 的 SAIL 是架构上的信号**:一个硬件隔离的安全岛,即使**主 OS 抛出软件异常**,刹车/避障仍能继续执行(secondary——高通发布会新闻;产品简报本身只说了"安全岛 + 域隔离支持功能安全架构")——也就是说,S0 确定性协处理器**内置在算力档硅片里**,而不是一颗分立的 MCU。按简报所述 I/O:**2× 10G Base-T(主域)+ 1× 2.5G Base-T(SAIL 安全域)**、**8× CAN-FD**(4 路原生+4 路经 SPI 外接)、**EtherCAT 4× 1G Base-T**、TSN-ready 以太网、最高 **12 路 GMSL2 摄像头**(3× MAX96724——secondary)+ 激光雷达/ToF/IMU、**Wi-Fi 7 + BT;5G 调制解调器可选加装**。早期接入样机于 **2026 年 6 月**发给企业客户(Thundercomm 通过 TurboX IRB10 确认;"10 家合作伙伴/NEURA" *unverified*)。

### 两个约束条件(为什么各档存在)

- **内存带宽,而非 TOPS,才是墙(secondary)。** VLA 动作专家推理在端侧加速器上是**内存受限,而非计算受限**(arXiv 2604.24447)。规格表 TOPS**不能**预测可达 Hz:
  - **LiteVLA-Edge**:在 Jetson AGX Orin 上完全端侧,只有 **150.5 ms/步(约 6.6 Hz)**(4-bit SmolVLM-256M,全部 42 层卸载到 GPU)——远低于 >100 Hz–1 kHz 的目标,尽管 Orin 有 275 INT8 TOPS(secondary,arXiv 2603.03380)。
  - 固定功能 NPU(高通 NPU、Horizon BPU)能映射 MAC,但**映射不了 attention/softmax/layernorm**,迫使 VLA transformer 层退化到 CPU/DSP——这是高端场景下**GPU 级硅片优于纯 NPU** 的结构性论据(secondary)。
- **真实的 Thor VLA 数字量化了为什么重推理会被逐出到 S2/云端(primary,arXiv 2602.18397 VLA-Perf):**

  | 模型 | 端侧速率(Jetson Thor) | 备注 |
  |---|---|---|
  | π0 baseline | **19.0 Hz**(52.57 ms/步) | 视觉编码 6.06 + VLM 20.30 + 动作专家 26.20 ms |
  | π0-L(9.1B) | 3.9 Hz | 更大骨干急剧退化 |
  | π0-XL(16.7B) | 2.1 Hz | — |
  | π0 + 1K 时间步上下文 | 1.3 Hz(768.3 ms) | 长上下文压垮它 |
  | π0 baseline 在 **H100** | **162.5 Hz** | 端侧-数据中心差距超过约 100 倍 |
  | π0 baseline 在 **B100** | **314.4 Hz** | — |

  基于扩散的动作解码比朴素自回归(带分块)**快 102.4 倍**(primary)——这正是让一个非实时技术栈仍能达到 S1 频率的机制。

### 云边混合仅对 S2 是合理的

- 网络延迟(5G/WiFi 上数十 ms,较差的 LTE 上 >100 ms)**从数量级上超过** S1 预算(**120 Hz 下 8.3 ms**),所以只有 S2/深思档能上云——之所以能行,是因为 S2 的输出可以**被缓冲/与网络往返时延解耦**(primary)。
  - **"投机式策略编排"**(arXiv 2603.19418):把预先计算好的路径点从一个云端世界模型流式传给一个本地边缘缓冲区,配合 ε-管验证器 + 自适应视野缩放;相对静态缓存,**减少 60% 的网络导致的空转时间**,减少约 60% 被丢弃的云端预测(primary)。
  - 5G + 数据中心 B100 上的异步推理带来相对同步云端 **5.99× 吞吐**(35.9 Hz 同步 → 215.3 Hz 异步;VLA-Perf 表 8);在 4G + 慢云的情况下异步加速比在 **13.79×** 达到峰值(3.7 → 50.5 Hz)——链路越差,解耦的收益越大(primary,VLA-Perf)。
- **光有位置不是杠杆——模型大小/量化才是(primary,arXiv 2601.14921):** 在一台 Unitree G1-EDU + NVIDIA L4 24GB 边缘节点上,LLaMA-3.2-11B-Vision(4-bit)边缘跑 **1600 ms**,云端 **1685 ms**——只快约 5%;Qwen2-VL-2B 跑到亚秒级。无论位置在哪,文本生成都占超过 85% 的延迟。**恰当缩放+量化;不要只是把一个大模型原样搬到边缘。**
- **MEC/5G** 基础设施能达到 **5–10 ms 端到端**,相对传统云端 >50 ms *(unverified——网络综合信息,未钉在单一论文上)*——这是把蜂窝连接(模组厂的核心能力)视为 S2 云辅助档**基础设施层面举足轻重**的依据,而非锦上添花。

### 软件栈也已收敛(而且不可移植)

- 事实上的模式(primary):**Ubuntu 22.04 + PREEMPT_RT**(或厂商 RTOS)跑在 AI SoC 上做感知/规划/VLA,通过 **ROS2**(软实时中间件)粘合,配**各厂商不可移植的推理运行时**(TensorRT / QNN / BPU 工具链),再加一个**独立的裸机 MCU/RTOS** 负责 S0 闭环。
  - PREEMPT_RT 直到**内核 6.12(2024 年 9 月)**才合入主线,结束约 20 年的树外存在——但仍**只是软实时**,这正是*为什么*专用 S0 MCU 是普遍存在的。截至 2025–26,ROS2 的实时性故事仍是"概率性/软实时,不是硬实时"(primary;arXiv 2601.10722 等)。
- **运行时确实不可移植——这正是模组厂的护城河(primary):** NVIDIA 自己的文档说*"在 RTX 4090 上构建的引擎在 H100 上无法工作"*。一个 D-Robotics BPU 模型跑不了 Jetson;一个高通 QNN 图两边都跑不了。D-Robotics 提供一个专用的 **rdk_LeRobot_tools** 移植层(PyTorch→ONNX→Horizon→.hbm),目前**仅验证过 ACT 策略**,在 RDK S100 上——同一份开放策略代码需要 **N 个独立的厂商级缝合工作** 才能部署。"中间件支持" 是一个真实的差异化因素,不是大宗商品。

### 功能安全映射到 S0 层

- 人形功能安全实践要求一个**独立的硬件看门狗/联锁,强制执行安全运动边界,即使经 OTA 更新的软件失效也能存活**,目标 **IEC 61508 SIL-2/SIL-3**(secondary,automate.org/QNX)。指南将其明确与 OTA 绑定:因为高层软件是远程更新的,所以要使用独立的联锁/看门狗。
- 一个引用的危险检测/干预系统报告 **>99% 的可靠性**,定位为 SIL-2 的风险降低(secondary,arXiv 2603.22703)。另有一个独立报道的 RISC-V 安全看门狗核声称 **18 µs 故障安全关机**,目标 SIL-3 *(单一来源,unverified)*。
- 这一要求**直接落在确定性 MCU / 安全岛这一档**——这也是为什么 IQ10 的片上 SAIL 是一个战略赌注:安全协处理器成了所售硅片的一部分。

### 模组厂(模组厂)的读数

- **卡位在集成,不在算力。** 参考技术栈是一堆异构、按抖动分区的东西——大 SoC(S2/S1)+ 确定性 MCU/孤岛(S0)+ 现场总线(EtherCAT/CAN-FD)+ 连接性(供 S2 云辅助档使用的 5G/Wi-Fi)+ 一个不可移植的各厂商运行时 + 一个功能安全看门狗。一个能把这一切**预集成好、移植层和蜂窝技术栈都做完**并出货的模组厂,卖的是稀缺的东西。
- **连接性举足轻重,不是外围配件**——因为 MEC/5G 是唯一可云端卸载档(S2)的使能基础设施。这正是一家蜂窝模组厂商的核心能力能插入的地方。
- **具体的量产实例——Quectel SH602HA-AP(部分;模组具体规格为单一来源)**:一款模组厂的端侧大脑模组,基于 **D-Robotics Sunrise5(X5M)**(最高 **10 TOPS BPU**)、Ubuntu 系统、默认 **4 GB LP4/LP4x RAM + 64 GB 存储**(40.5×40.5×2.9 mm;2026 年 CES 发布),搭配 Quectel 自家的 **LTE Cat1/Cat4/5G/Wi-Fi6/GNSS** 模组提供连接性,支持 VSLAM / 双目深度 / 3D 点云 / Transformer-BEV-Occupancy 模型 + 激光雷达。它处于**低端(10 TOPS,S1-轻量/感知档)**,不是 Thor/IQ10 旗舰——但它是一个真实的、正在出货的证据,证明"军火商"式的模组打法(算力芯片 + 连接性 + OS 预集成)今天就存在。(见 §F,SoC 版图;Quectel 产品页)

来源:
- https://www.figure.ai/news/helix
- https://arxiv.org/abs/2503.14734
- https://arxiv.org/abs/2602.18397 — VLA-Perf:π0 在 Jetson Thor 上 19.0 Hz;π0-L 3.9 Hz;π0-XL 2.1 Hz;H100 162.5 Hz / B100 314.4 Hz;扩散比自回归快 102.4×
- https://arxiv.org/abs/2603.19418 — Speculative Policy Orchestration:减少 60% 网络空转时间;ε-管验证器 + 自适应视野缩放
- https://arxiv.org/abs/2601.14921 — VLMs on the Edge:11B-Vision 边缘 1600 ms vs. 云端 1685 ms(约 5%);Qwen2-VL-2B 亚秒级;文本生成占延迟 >85%
- https://arxiv.org/abs/2604.24447 — Characterizing VLA across XPUs:内存受限而非计算受限
- https://arxiv.org/abs/2603.03380 — LiteVLA-Edge:Jetson AGX Orin 上 150.5 ms/步(约 6.6 Hz),4-bit SmolVLM-256M
- https://docs.qualcomm.com/doc/87-A0789-1/87-A0789-1_REV_A_Qualcomm_Dragonwing_IQ10_Robotics_Reference_Design_Product_Brief.pdf — IQ10 RRD:最高 700 TOPS 稀疏,18× Oryon CPU + NPU + GPU,64 GB LPDDR5x,安全岛(SAIL 2.5G Base-T 域),8× CAN-FD(4 原生 + 4 经 SPI 外接),EtherCAT 4× 1G Base-T,2× 10G Base-T 主域,最高 12 路 GMSL2 摄像头,Wi-Fi 7 + BT,5G 可选;2026 年 9 月量产
- https://developer.nvidia.com/blog/introducing-nvidia-jetson-thor-the-ultimate-platform-for-physical-ai/ — Thor 2,070 FP4 TFLOPS,128 GB @ 273 GB/s,相对 Orin 7.5×/3.5×
- https://nvidianews.nvidia.com/news/nvidia-open-humanoid-robot-reference-design — Isaac GR00T 参考人形机器人(Unitree H2 Plus + Sharpa + Thor)
- https://en.wikipedia.org/wiki/PREEMPT_RT — 内核 6.12(2024 年 9 月)合入主线,仅软实时
- https://www.ti.com/lit/an/slla659a — 用于确定性多轴机器人的 CAN-FD
- https://automate.org/ — QNX/机器人功能安全:独立看门狗/联锁,IEC 61508 SIL-2/3,OTA 依据
- https://arxiv.org/abs/2603.22703 — Learning Safe-Stoppability Monitors for Humanoid Robots

---
