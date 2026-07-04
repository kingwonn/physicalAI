---
title: 机器人世界模型
slug: world-models
updated: 2026-07-04
confidence: verified
lang: zh
source: ../wiki/world-models.md
---
> 世界模型(world model)是一类神经网络,能够在给定动作、文本或先前帧的条件下,预测环境如何演化——以像素、潜变量或完整可交互 3D 的形式。从 2025 年初到 2026 年中,它们从研究界的新奇玩意变成了 Physical AI 的核心基础设施:NVIDIA 的 Cosmos 系列(以 2026 年 6 月发布的全模态 Cosmos 3 为顶点)充当开放的合成数据与策略骨干;Google DeepMind 的 Genie 3(2025 年 8 月)实时生成可交互世界,如今用于训练 SIMA 2 智能体并支撑 Waymo World Model;1X 用动作条件视频模型来评估并教学其 NEO 人形机器人;Meta 的 V-JEPA 2 在潜空间中规划,实现零样本机器人操作;Tesla 则运行一个基于车队视频训练的"神经世界模拟器",为 FSD 和 Optimus 同时闭环。世界模型如今在机器人训练中承担四种角色——学习型模拟器、规划器、策略评估器和数据引擎——但幻觉、rollout 误差累积、动作条件保真度不足以及算力成本仍是主要瓶颈。

## 世界模型为何对机器人重要

- 机器人领域的核心瓶颈是数据和评估,而不是算力:真实机器人试验缓慢、昂贵且不可复现。参见 [机器人学习数据](data.md) 和 [仿真](simulation.md)。
- 世界模型用一个在视频上训练出来的*学习型*模拟器替代(或增强)手工搭建的物理模拟器——绕开了资产制作和部分模拟到现实(sim2real)差距,代价是失去物理保证。
- 目前已凝结出四种明确角色(分类沿用 2026 年 5 月的综述 "World Model for Robot Learning",arXiv:2605.00080):
  1. **模拟器 / 评估器** —— 在模型内部而非硬件上运行策略 rollout(1X World Model、Tesla 神经模拟器、WorldEval)。
  2. **规划器** —— 想象候选动作的结果并择优执行(V-JEPA 2-AC、1X NEO 的"视频预测 + 逆动力学"闭环)。
  3. **数据引擎** —— 生成合成轨迹来训练策略(NVIDIA DreamGen 的"神经轨迹"、Cosmos Transfer 域增强)。
  4. **策略骨干** —— 先在世界预测上预训练,再微调为动作模型(基于 Cosmos 3 的"World Action Models";面向 [VLA 模型](vla-models.md) 的 WMPO 式世界模型强化学习)。
- 两大架构阵营:**生成式像素空间**模型(Cosmos、Genie、1XWM、Tesla —— 逼真、人类可检视、昂贵)与**潜空间预测式**模型(V-JEPA 2 —— 不生成像素、规划更便宜、更难检视)。可交互 3D 生成器(Genie 3、World Labs Marble)构成更接近游戏引擎的第三分支。

## 格局对比

| 模型 / 产品线 | 机构 | 关键发布 | 类型 | 是否动作条件? | 主要机器人角色 |
|---|---|---|---|---|---|
| Cosmos 1 → Cosmos 3 | NVIDIA | 2025 年 1 月(CES)→ 2026 年 6 月 | 像素视频 WFM;Cosmos 3 全模态(文本/图像/视频/声音/动作) | 是(Cosmos 3 可输出关节角、夹爪位姿、轨迹) | 合成数据引擎、策略骨干(开放权重) |
| Genie 1/2/3 | Google DeepMind | Genie 3:2025 年 8 月 | 可交互实时世界生成(24 fps,720p) | 导航/智能体动作;可提示的世界事件 | 智能体训练环境(SIMA 2);经 Waymo World Model 用于自动驾驶仿真 |
| 1X World Model(1XWM / Redwood) | 1X Technologies | 论文 2025 年 6 月;产品 2026 年 1 月 | 面向完整人形机器人的动作条件视频预测 | 是(精确机器人轨迹) | 离线策略评估;NEO 从视频学习任务 |
| V-JEPA 2 / V-JEPA 2-AC | Meta FAIR | 2025 年 6 月 | 潜空间预测式(JEPA),不生成像素 | AC 变体:是(机械臂动作/位姿) | 操作任务的零样本规划;表征骨干 |
| 神经世界模拟器 | Tesla | 2025 年 10 月 ICCV 展示 | 像素视频,基于车队视频训练,闭环 | 是(响应驾驶/机器人动作) | 闭环评估、对抗性场景合成、FSD + Optimus 的大规模强化学习 |
| Waymo World Model | Waymo(基于 Genie 3) | 2026 年 2 月 | 生成式驾驶仿真,输出相机 + 激光雷达 | 是(驾驶输入、语言、场景布局) | 长尾自动驾驶场景仿真 |
| Marble | World Labs | 2025 年 11 月 | 由文本/图像/视频生成 3D 场景(高斯泼溅/网格) | 否(静态场景) | 仿真资产/环境创建 |

## 2026 年世界模型融资潮

- 2026 年初,资本为这一赛道背书:三笔约 10 亿美元以上的世界模型融资在三周内相继**完成交割**(逐轮溯源的详表见 [投资](investment.md)):
  - **World Labs**(李飞飞,空间智能 / Marble):**10 亿美元成长轮于 2026-02-18 完成交割**,由 Autodesk 领投(2 亿美元),AMD、Nvidia、Fidelity、Emerson Collective 和 Sea 参投;累计融资 12.3 亿美元。被广泛引用的**约 54 亿美元投后估值出自 Forbes,公司从未确认**(Bloomberg 在洽谈期间曾报道约 50 亿美元)。
  - **Wayve**(英国,驾驶世界模型 / 具身智能):**12 亿美元 D 轮于 2026-02-25 完成交割,投后估值 86 亿美元**,另有 **Uber 提供的 3 亿美元里程碑式资金**(合计锁定 15 亿美元);Eclipse、Balderton 和 SoftBank Vision Fund 2 联合领投。
  - **AMI Labs**(巴黎,Yann LeCun 离开 Meta 后创立的世界模型实验室):**10.3 亿美元种子轮于 2026-03-09 完成交割,投前估值 35 亿美元** —— 欧洲有史以来最大的种子轮;Nvidia、Samsung、Temasek 和 Toyota Ventures 参投。
- 解读:世界模型现已成为独立于机器人硬件的受资助赛道——横跨空间智能(World Labs)、自动驾驶(Wayve)和 LeCun 的反生成式 JEPA 研究纲领(AMI Labs;见下文 V-JEPA 一节)。这三轮合计约 32 亿美元,贡献了 2026 年上半年创纪录的 Physical AI 融资总额的很大一部分。

## NVIDIA Cosmos:开放的世界模型平台

- **Cosmos 1(CES,2025-01-06):**开放权重"世界基础模型"(WFM)平台——扩散和自回归视频模型,外加分词器、护栏和数据整理管线。训练数据约 9,000 万亿 token,包含 **2,000 万小时**驾驶/机器人及相关视频(截至 2025-01)。早期采用者包括 1X、Agility、Figure AI、Fourier、Galbot、Skild AI、Waabi、XPENG 和 Uber。论文:arXiv:2501.03575;宽松的开放许可。
- **Cosmos Reason(GTC,2025-03):**加入产品家族的 Physical AI 推理 VLM;用于数据整理/打标,并充当物理合理性的评判器。
- **Cosmos Predict 2.5 / Transfer 2.5(2025-10-06):**Predict 2.5 是基于流(flow)的模型,统一了 Text2World / Image2World / Video2World,以 Cosmos-Reason1 作为文本编码器,可生成**最长 30 秒**的连贯 rollout。Transfer 2.5 在空间控制输入(深度、分割、边缘)条件下进行可控的模拟到现实风格迁移——是把一条演示扩增为大量逼真变体的主力工具。
- **Cosmos 3(GTC Taipei at COMPUTEX,2026-06-01,截至 2026-06):**号称首个"完全开放的全模态模型"(omnimodel)——原生理解并生成文本、图像、视频、环境音以及**动作**(关节角、夹爪位置、轨迹点)。混合 transformer 架构把一个推理 transformer 与一个专家生成 transformer 配对。变体:Super(物理精度)、Nano(快速推理)、Edge(已宣布,端侧实时)。NVIDIA 宣称在 Physics-IQ、PAI-Bench、R-Bench、RoboArena 等榜单上位居开放模型第一(厂商口径,截至 2026-06)。随之发起"Cosmos Coalition"(Agile Robots、Black Forest Labs、Generalist、LTX、Runway、Skild AI)。
- **Cosmos Policy(论文 2026-01-22,arXiv:2601.16163):**将 Cosmos Predict-2 后训练为统一控制模型,把机器人动作、未来状态和期望回报编码成同一扩散过程中的"帧"——一个模型同时完成视觉运动控制、观测预测和回报估计。报告 **LIBERO 平均成功率 98.5%**(超过此前的扩散策略和 VLA,如 CogVLA 97.4%、OpenVLA-OFT 97.1%),在每任务 50 条演示下 RoboCasa 达 67.1%;在两个真实世界双臂(ALOHA)操作任务上,用该模型规划带来平均 +12.5% 的任务完成率提升。把 Cosmos 定位为"World Action Models"(WAM)的骨干——预训练学会想象,微调学会行动。
- 战略解读:Cosmos 是 NVIDIA 争当"Physical AI 的 Android"的押注——用开放权重带动对其仿真与算力栈的需求。参见 [机构](organizations.md) 和 [格局:美国](landscape-usa.md)。

## DeepMind 的 Genie 系列及其衍生

- **Genie 1(2024-02):**在 2D 平台游戏视频上训练的基础世界模型;无需动作标签即学到潜在动作。**Genie 2(2024-12):**从单张图像生成 3D 具身世界,但一致性仅约 10–20 秒。
- **Genie 3(2025-08-05):**文本提示生成可交互世界,**24 fps、720p**,可实时游走,一致性维持数分钟,视觉记忆可回溯约 1 分钟;支持"可提示的世界事件"(在 rollout 中途注入天气、物体、角色)。以受限研究预览形式发布;面向公众的"Project Genie"演示于 2026 年 1 月底跟进(截至 2026-01)。
- **对机器人的意义:**DeepMind 将 Genie 3 与其通用智能体 **SIMA 2**(2025-11)配对——智能体在生成的世界中练习多步任务,据称无需新的人类演示即可提升,是"世界模型即无限训练场"的存在性证明(除 DeepMind 自述外未证实)。
- **Waymo World Model(2026-02):***基于* Genie 3 构建的前沿生成式驾驶模拟器,产出多传感器(相机 + 激光雷达)rollout;可模拟从未观测到的长尾事件(龙卷风、路上的动物),并可通过语言、驾驶输入和场景布局控制。这是 Genie 系列最清晰的生产化部署。
- Genie 3 已承认的局限:智能体动作空间受限、多智能体交互薄弱、真实世界地理不准确、文本渲染差,以及交互时长以分钟计而非小时计。

## 1X World Model:面向人形机器人的评估优先路线

- 论文 "1X World Model: Evaluating Bits, not Atoms"(2025-06-16):一个动作条件视频模型,为**全身人形机器人**(NEO)预测高保真、富接触的未来——由精确机器人轨迹驱动,而非语言,这一点不同于文生视频模型。参见 [人形机器人](humanoid-robots.md)。
- 核心用途是**离线策略评估**:在不动用硬件的情况下预测候选策略检查点的任务成功率。1X 报告其与真实世界评估高度相关;当两个策略真实成功率相差 15 个百分点时,一个准确率仅约 70% 的世界模型仍能在约 90% 的情况下选出更优者。
- 缩放规律结果:预测准确率随训练算力和真实 NEO 数据单调提升;多任务训练数据(货架 + 街机)优于单任务。已知失败模式:未见过的物体类别。
- **产品发布(2026-01-12):**1X 将世界模型部署进 NEO——一条语音/文本指令让 NEO 生成未来动作的视频,内置**逆动力学模型**再把预测帧翻译成电机指令,使 NEO 能尝试从未被演示过的任务(空气炸锅篮、烤面包机)。CEO Bernt Børnich 称之为"NEO 自我教学能力的起点";媒体报道指出实际能力仍限于简单任务(截至 2026-01)。1X 还组建了专门的 World Model Lab。

## V-JEPA 2:潜空间替代路线

- Meta FAIR 于 2025-06-11 发布,开源(允许商用):一个 **12 亿参数**的自监督联合嵌入预测架构,预训练于 **100 万+ 小时**互联网视频和 100 万张图像;在表征空间而非像素空间做预测(Yann LeCun 的反生成式论点——见 [关键人物](key-people.md))。
- **V-JEPA 2-AC:**动作条件变体,仅用 **<62 小时**无标注 DROID 机器人视频后训练;通过面向图像目标的模型预测控制,在两个实验室的 Franka 机械臂上实现**零样本**抓放——无需环境特定数据、任务训练或奖励工程——在陌生环境中成功率 **65–80%**。
- 随模型发布了三个新的物理推理基准:**IntPhys 2**(物理合理性检测)、**MVPBench**(控制捷径的视频问答)、**CausalVQA**(因果推断)——三者都显示人类接近满分而模型远低于人类,量化了物理理解差距。
- 基准成绩(截至 2025-06):Something-Something v2(运动理解)top-1 77.3%,Epic-Kitchens-100 动作预判 recall@5 39.7;与 8B LLM 对齐后 PerceptionTest 84.0 / TempCompass 76.9。
- Meta 声称用 V-JEPA 2-AC 做规划比 Cosmos 等像素生成式方案快约 30 倍(厂商对比,方法论有争议)(未证实)。
- 权衡:潜空间模型在规划/合理性检查上便宜快速,但不产出视频,因此无法充当合成数据引擎或人类可检视的模拟器。

## Tesla:一个神经模拟器同时服务汽车与人形机器人

- 在 ICCV(2025-10)上,Ashok Elluswamy(AI 软件副总裁,同时主管 Optimus)详述了一个基于 Tesla 车队视频洪流训练的**神经世界模拟器**:它根据 AI 的动作合成多相机视频——一个学习出来的闭环模拟器,而非手工编码的物理引擎。
- 用途:新 FSD 版本的闭环评估(Elluswamy:开环预测损失"可能与真实世界的优秀表现并不相关")、对历史数据的回放、合成对抗性极端场景生成,以及大规模强化学习。
- 同一模拟器还能生成 **Optimus** 行动的视频(在工厂环境中行走、转身),支撑 Tesla 关于源自 FSD 的世界建模可"无缝迁移"到人形机器人的说法——一套跨汽车与机器人的单一基础模型战略。在 CVPR 2026(6 月,丹佛)上,Elluswamy 据报道展示了一个 36 Hz 端到端模型并重申了 FSD-Optimus 统一愿景(仅有二手来源)(未证实)。
- Tesla 的路线封闭且垂直整合——没有论文、权重或基准——外部验证无从谈起;相关声明应据此打折看待。可交叉参考 [格局:美国](landscape-usa.md)。

## 世界模型作为数据引擎:DreamGen 配方

- NVIDIA GEAR 的 **DreamGen**(2025)是把视频世界模型变成机器人数据工厂的标准管线,共四步:(1)在目标本体上微调视频 WFM(Cosmos-Predict2);(2)用初始帧 + 语言指令提示生成合成机器人视频;(3)通过潜动作或逆动力学模型恢复**伪动作**;(4)在得到的"神经轨迹"上训练视觉运动策略。
- 头条结果:仅凭**单一环境中单个抓放任务**的遥操作(teleoperation)数据,DreamGen 让 GR1 人形机器人在 **10 个新环境中完成 22 种新行为**——零样本的行为与环境泛化。还在 Franka、100 美元的 SO-100 机械臂和 RoboCasa 上得到验证。
- 缩放规律:神经轨迹数量(测试至 24 万条)与下游策略性能呈对数线性关系。
- 对经典模拟器难以处理的富接触和可变形任务(叠衣、锤击)同样有效——其卖点是"real-to-real"数据生成,绕过了 [仿真](simulation.md) 的模拟到现实差距。
- 相关的 2026 年研究线:WMPO(面向 VLA 的基于世界模型的策略优化,arXiv:2511.09515)、用于策略训练/评估的可交互世界模拟器(arXiv:2603.08546),以及 VLA 与世界模型的迭代共同提升(VLAW,arXiv:2602.12063)。这已成为世界模型与 [VLA 模型](vla-models.md) 之间的主要耦合点。

## 优势与局限

| 角色 | 已经可行(截至 2026-07) | 仍会失效 |
|---|---|---|
| 模拟器/评估器 | 策略排序与现实相关(1XWM、WorldEval arXiv:2505.19017);无需资产制作 | 幻觉会污染评估信号本身——伪影(手臂重影、物体瞬移)恰恰在评估差策略时更严重(MiraBench) |
| 规划器 | 经潜空间规划实现零样本操作(V-JEPA 2-AC);可解释的视觉未来(1X NEO) | 恶性循环:幻觉 → 坏动作 → 进一步偏离分布 → 更严重幻觉;长时程误差累积 |
| 数据引擎 | 神经轨迹带来对数线性策略提升(DreamGen);逼真的域随机化(Cosmos Transfer) | 伪动作提取有噪;生成的物理可能存在细微错误,让策略学到错误动力学 |
| 策略骨干 | 视频预训练可迁移到动作(Cosmos 3 WAM、GR00T 系列) | 相对纯 VLA 训练尚未在大规模上得到证明;像素空间模型算力开销大 |

- **物理保真度是症结所在:**视频模型优化的是视觉合理性而非动力学正确性——Physics-IQ 和 MiraBench(arXiv:2605.29360)等基准的存在正说明两者会背离。一篇立场论文(arXiv:2606.15032)主张应以决策效用而非视频质量来评估世界模型。
- **时程限制:**即便是 Genie 3 也只能维持数分钟的一致性;大多数与机器人相关的 rollout 仍不超过 30 秒(Cosmos Predict 2.5)。
- **动作空间贫乏:**可交互模型只暴露狭窄的动作接口(导航、简单事件),远不及操作任务所需的完整富接触动作空间——参见 [操作](manipulation.md) 和 [开放问题](open-problems.md)。
- **算力成本:**像素空间 rollout 比经典仿真贵几个数量级;潜空间模型(V-JEPA)以可检视性换取速度。
- **收敛信号:**到 2026 年中,几乎所有主要 Physical AI 玩家——NVIDIA、DeepMind/Waymo、Tesla、1X、Meta、World Labs,以及发布开放视频世界模型的中国实验室——都把世界模型视为与 VLA 并列的 [技术树](tech-tree.md) 主支柱。悬而未决的问题是:它们最终会成为*策略*本身(WAM),还是停留在*工厂*角色(数据/评估基础设施)。

## 来源

- https://nvidianews.nvidia.com/news/nvidia-launches-cosmos-world-foundation-model-platform-to-accelerate-physical-ai-development — Cosmos CES 2025 发布(2025-01-06)、开放模型许可、采用者名单
- https://blogs.nvidia.com/blog/cosmos-world-foundation-models/ — 训练规模:来自 2,000 万小时真实世界/机器人/驾驶视频的 9,000 万亿 token
- https://arxiv.org/abs/2501.03575 — Cosmos WFM 平台论文(组件、开放许可)
- https://huggingface.co/blog/nvidia/cosmos-predict-and-transfer2-5 — Cosmos Predict 2.5 / Transfer 2.5 细节(基于流的统一架构、30 秒 rollout,2025 年 10 月)
- https://nvidianews.nvidia.com/news/nvidia-launches-cosmos-3-the-open-frontier-foundation-model-for-physical-ai — Cosmos 3 发布(日期、全模态声明、变体、Coalition、榜单)
- https://blogs.nvidia.com/blog/cosmos-3-physical-ai-open-world-foundation-model/ — Cosmos 3 架构(混合 transformer)、原生动作生成、WAM 框架
- https://arxiv.org/abs/2601.16163 — Cosmos Policy 论文(2026-01-22 提交;LIBERO 98.5% / RoboCasa 67.1%)
- https://www.therobotreport.com/nvidia-adds-cosmos-policy-world-foundation-models/ — Cosmos Policy 报道(2026-02-19):RoboCasa 50 条演示细节、真实世界 ALOHA 规划 +12.5% 提升、基线对比
- https://deepmind.google/blog/genie-3-a-new-frontier-for-world-models/ — Genie 3 能力、局限、可用性(2025 年 8 月)
- https://en.wikipedia.org/wiki/Genie_(world_model) — Genie 谱系、Genie 2 时程、SIMA 2 与 Project Genie 时间线
- https://www.techtimes.com/articles/317932/20260606/deepmind-world-models-train-robots-imagined-worlds-sima-practices-inside-genie-3-model.htm — SIMA 2 在 Genie 3 世界中的自我提升(二手来源)
- https://waymo.com/blog/2026/02/the-waymo-world-model-a-new-frontier-for-autonomous-driving-simulation/ — 基于 Genie 3 的 Waymo World Model、相机+激光雷达、长尾仿真
- https://www.1x.tech/1x-world-model.pdf — 1XWM 论文 "Evaluating Bits, not Atoms"
- https://www.1x.tech/discover/redwood-ai-world-model — 1XWM 策略评估结果、缩放规律、局限
- https://www.1x.tech/discover/world-model-self-learning — 1X 公告(2026-01-12):视频预测 + 逆动力学模型部署进 NEO
- https://techcrunch.com/2026/01/13/neo-humanoid-maker-1x-releases-world-model-to-help-bots-learn-what-they-see/ — 1X 发布的媒体报道(Børnich 引语、能力保留意见)
- https://arxiv.org/abs/2506.09985 — V-JEPA 2 论文(训练规模、V-JEPA 2-AC、基准、零样本操作)
- https://ai.meta.com/blog/v-jepa-2-world-model-benchmarks/ — V-JEPA 2 官方博文:12 亿参数、62 小时 DROID 后训练、65–80% 抓放成功率、IntPhys 2 / MVPBench / CausalVQA 基准
- https://www.marktechpost.com/2025/06/12/meta-ai-releases-v-jepa-2-open-source-self-supervised-world-models-for-understanding-prediction-and-planning/ — V-JEPA 2 发布背景、对 Cosmos 的 30 倍规划速度声明
- https://www.humanoidsdaily.com/news/tesla-ai-chief-details-unified-world-simulator-for-fsd-and-optimus — Tesla 神经世界模拟器(ICCV 演讲、用途、FSD-Optimus 统一)
- https://research.nvidia.com/labs/gear/dreamgen/ — DreamGen 管线、22 种行为结果、缩放至 24 万条神经轨迹
- https://arxiv.org/abs/2605.00080 — 综合综述:机器人学习的世界模型(角色分类)
- https://arxiv.org/pdf/2505.19017 — WorldEval:世界模型作为机器人策略评估器
- https://arxiv.org/pdf/2605.29360 — MiraBench:动作条件可靠性、机器人世界模型中的幻觉伪影
- https://arxiv.org/pdf/2511.09515 — WMPO:面向 VLA 模型的基于世界模型的策略优化
- https://techcrunch.com/2025/11/12/fei-fei-lis-world-labs-speeds-up-the-world-model-race-with-marble-its-first-commercial-product/ — World Labs Marble 发布(2025 年 11 月)
- https://finance.yahoo.com/news/ai-pioneer-fei-fei-lis-192214332.html — World Labs 10 亿美元融资于 2026-02-18 交割(Reuters):Autodesk 领投 2 亿美元;AMD、Nvidia、Emerson Collective、Fidelity、Sea;公司拒绝确认估值
- https://www.forbes.com/sites/josipamajic/2026/06/30/world-model-startups-raise-3-billion-vcs-bet-beyond-llms/ — World Labs 约 54 亿美元投后估值(Forbes 数字,公司未确认)、累计融资 12.3 亿美元;2026 年上半年逾 30 亿美元流入世界模型初创公司
- https://wayve.ai/press/series-d/ — Wayve D 轮交割(一手来源,2026-02-25):12 亿美元、投后估值 86 亿美元;另有 3 亿美元 Uber 里程碑式资金,合计锁定 15 亿美元
- https://techcrunch.com/2026/03/09/yann-lecuns-ami-labs-raises-1-03-billion-to-build-world-models/ — AMI Labs 10.3 亿美元种子轮以 35 亿美元投前估值交割(2026-03-09);投资方阵容
