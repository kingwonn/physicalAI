---
title: 视觉-语言-动作模型
slug: vla-models
updated: 2026-07-04
confidence: verified
lang: zh
source: ../wiki/vla-models.md
---
> 视觉-语言-动作模型(VLA)是一类多模态神经网络,输入相机图像和自然语言指令,直接输出底层机器人动作,是"通用机器人大脑"的头号候选架构。其谱系从 Google 的 RT-1(2022)和 RT-2(2023,该术语由其提出)延伸到开放学术模型(Octo、OpenVLA,2024),再到生产级系统:Physical Intelligence 的 π0/π0.5/π*0.6/π0.7、NVIDIA 的 Isaac GR00T N 系列、Google DeepMind 的 Gemini Robotics 家族,以及 Figure 的 Helix/Helix 02。截至 2026 年中,该领域已收敛到一个共同配方——预训练视觉-语言模型骨干加上快速动作解码头(流匹配、扩散或压缩动作 token)——而前沿工作正转向从部署经验中做强化学习(π*0.6/RECAP)、具备智能体式"思考"的 VLA(Gemini Robotics 1.5、GR00T N1.7)以及世界-动作模型(GR00T N2/DreamZero)。

## 什么是 VLA

- VLA 是一个单一基础模型,将(图像 + 语言指令 + 机器人状态)映射为动作指令(关节目标、末端执行器位姿、夹爪指令),通常以 8–50 个未来步长的短"动作块(action chunk)"形式输出,频率视设计而定,从 3 到 200 Hz 不等。
- 核心押注:互联网规模的视觉-语言预训练可以把语义知识(物体、空间关系、常识)迁移到机器人控制中,让机器人在演示数据之外泛化。
- "视觉-语言-动作模型"一词由 Google DeepMind 的 RT-2(2023 年 7 月)提出,该工作证明将 VLM 微调为以文本 token 输出动作后能继承网络知识(例如"拿起那只灭绝的动物"→ 抓起玩具恐龙)。
- VLA 是物理 AI 技术栈中的"策略"层;它们越来越多地位于推理/编排层之下(见 Gemini Robotics-ER、Figure 的 System 2),训练数据来自真实遥操作(teleoperation)、仿真和人类视频——见[数据](data.md)与[仿真](simulation.md)。

## 谱系与关键模型

| 模型 | 机构 | 日期 | 参数量 | 骨干 | 动作解码 | 权重 |
|---|---|---|---|---|---|---|
| RT-1 | Google | 2022-12 | 35M | EfficientNet + Transformer | 离散 token 分箱,3 Hz | 开放(代码) |
| RT-2 | Google DeepMind | 2023-07 | 12B / 55B | PaLM-E / PaLI-X | 动作作为文本 token | 闭源 |
| RT-2-X / Open X-Embodiment | 21+ 家实验室 | 2023-10 | 55B | PaLI-X | 离散 token | 数据集开放 |
| Octo | UC Berkeley 等 | 2024-05 | 27M / 93M | 自研 transformer | 扩散头 | 开放(Apache-2.0) |
| OpenVLA | Stanford/Berkeley 等 | 2024-06 | 7B | Prismatic(Llama-2-7B + DINOv2 + SigLIP) | 离散 token 分箱 | 开放(MIT) |
| RDT-1B | 清华 | 2024-10 | 1.2B | 自研 | 扩散 transformer(双臂) | 开放 |
| π0 | Physical Intelligence | 2024-10 | ~3.3B | PaliGemma 3B + 300M 动作专家 | 流匹配,50 Hz 动作块 | 开放(2025-02,Apache-2.0) |
| π0-FAST | Physical Intelligence | 2025-01 | ~3B | π0 架构 | 自回归 FAST token | 开放 |
| Helix | Figure | 2025-02 | 7B(S2)+ 80M(S1) | 开源 VLM(S2) | 隐变量条件化的 200 Hz 视觉运动策略 | 闭源 |
| GR00T N1 | NVIDIA | 2025-03 | ~2B | Eagle-2 VLM | 扩散-transformer(流匹配)头 | 开放权重 |
| Gemini Robotics | Google DeepMind | 2025-03 | 未公开 | Gemini 2.0 | 连续动作(细节未公开) | 闭源 |
| GO-1 | AgiBot(中国) | 2025-03 | 2B VLM + 规划器 + 专家 | InternVL2.5-2B | ViLLA:隐式规划器 + 扩散动作专家 | 开放(CC BY-NC-SA 4.0) |
| π0.5 | Physical Intelligence | 2025-04 | ~3.3B | π0 架构 + 联合训练 | 分层:子任务 token → 流匹配 | 开放(2025-09) |
| GR00T N1.5 | NVIDIA | 2025-05 | ~3B | Eagle 2.5(冻结 VLM)+ FLARE | 流匹配 DiT 头 | 开放权重 |
| SmolVLA | Hugging Face | 2025-06 | 450M | SmolVLM-2 | 流匹配 | 开放 |
| Gemini Robotics On-Device | Google DeepMind | 2025-06 | 未公开(机上运行) | Gemini Robotics 蒸馏版 | 连续动作 | 闭源,可通过 SDK 微调 |
| GR-3 | ByteDance Seed(中国) | 2025-07 | 4B | Qwen2.5-VL-3B | 流匹配 DiT 头 | 闭源 |
| WALL-OSS | X Square Robot(中国) | 2025-09 | 4B | 3B VLM | 混合式 | 开放 |
| Gemini Robotics 1.5 / ER 1.5 | Google DeepMind | 2025-09 | 未公开 | Gemini | "思考型" VLA + 推理编排器 | 闭源(ER 1.5 可经 API 使用) |
| π0.6 / π*0.6 | Physical Intelligence | 2025-11 | 5B + 动作专家 | 升级版 π0.5 | 流匹配 + RECAP 强化学习(优势条件化) | 截至 2026-07 闭源 |
| GR00T N1.6 | NVIDIA | 2025-09 宣布(CoRL),2026-01 发布(CES) | ~3B | Cosmos Reason | 流匹配 DiT 头,全身控制 | 开放权重 |
| Helix 02 | Figure | 2026-01 | S0 10M + S1 + S2 | Helix 架构 + 1 kHz 反射层 | 三层层级架构 | 闭源 |
| UnifoLM-VLA-0 | Unitree(中国) | 2026-01 | 未公开 | — | — | 开放 |
| LingBot-VLA | Ant Group / Robbyant(中国) | 论文 + 权重 2026-01 | 未公开 | — | — | 开放 |
| π0.7 | Physical Intelligence | 2026-04 | 未公开 | π0.6 谱系 | 可引导的通才模型:通过语言指导、元数据、视觉子目标提示 | 截至 2026-07 闭源 |
| GR00T N1.7 | NVIDIA | 2026-04(早期访问) | 3B | Cosmos-Reason2-2B(Qwen3-VL 架构) | 32 层扩散-transformer 头 | 开放权重(NVIDIA Open Model License) |
| GR00T N2 | NVIDIA | 2026-03 预览,2026 年底发布 | 未公开 | DreamZero 世界-动作模型 | 基于世界模型 | 已宣布开放 |

## 动作解码:核心设计维度

- **离散分箱 token**(RT-1、RT-2、OpenVLA):每个动作维度量化为约 256 个分箱,自回归预测。简单、可复用语言模型头,但速度慢(OpenVLA 在 RTX 4090 上仅 3–5 Hz),不适合高频灵巧控制。
- **压缩动作 token——FAST**(π0-FAST,2025-01):DCT + 字节对编码的"频域动作序列 token 化"(Frequency-space Action Sequence Tokenization)将 50 Hz 动作块压缩为短 token 序列;Physical Intelligence 称在相近质量下训练成本比扩散/流匹配解码低最高约 5 倍;FAST+ 是在 100 万条真实轨迹上训练的通用 tokenizer。
- **扩散头**(Octo、RDT-1B、GR00T N 系列):扩散 transformer 以 VLM 嵌入为条件对连续动作块去噪;可处理多模态动作分布。
- **流匹配(flow matching)**(π0、π0.5、SmolVLA):扩散的连续时间变体;π0 的 3 亿参数"动作专家"生成 50 Hz 动作块,该设计在 2025–26 年被广泛效仿,是新模型的当前默认选择。
- **朴素回归**(OpenVLA-OFT,2025):并行解码 + 动作分块 + L1 回归带来比自回归 OpenVLA 高约 26 倍的动作生成吞吐量,在 LIBERO 上平均成功率约 97.1%(原为 76.5%)——证明解码配方与规模同等重要。
- **双系统隐变量条件化**(Helix;GR00T N1 也是明确的双系统设计):慢速 VLM(7–9 Hz)输出隐式目标向量,由一个小而快的策略(200 Hz)消费——牺牲端到端纯粹性换取反应速度。Helix 02 将其扩展为三层,加入 1 kHz 反射层。
- **分层"先文本后动作"**(π0.5、Gemini Robotics 1.5、GR00T N1.7):同一模型先以文本预测高层子任务("拿起枕头"),再解码运动动作——"先思考再行动"。
- **世界-动作模型**(GR00T N2/DreamZero,2026):联合预测未来视频和动作,而不是给 VLM 外挂动作头——VLA 与[世界模型](world-models.md)两条研究线正在合流。

## Physical Intelligence(π 系列)

- **π0**(2024-10):PaliGemma-3B VLM + 300M 动作专家,流匹配,在 7–8 种机器人本体(单臂、双臂、移动)上约 1 万小时遥操作数据训练。演示了叠衣服、收拾餐桌、组装纸箱。权重 + 代码于 2025-02 在 `openpi` 开源(Apache-2.0)。
- **π0.5**(2025-04-22):目标是开放世界泛化——在训练中从未见过的住宅里清理厨房和卧室。联合训练网络多模态数据、口头指令、子任务标注、跨本体机器人数据;分层推理(以 FAST token 做离散自回归子任务推理 + 流匹配运动控制)。规模研究:约 100 个不同训练环境后,性能逼近在目标环境内训练的基线。权重于 2025-09 发布(含"知识隔离"训练与 PyTorch 支持);检查点包括 π0.5-base、π0.5-DROID、π0.5-LIBERO。
- **π*0.6 + RECAP**(2025-11-17):π0.6 是一个 5B 参数 VLM 外加动作专家(据模型卡)。RECAP = "RL with Experience & Corrections via Advantage-conditioned Policies":三阶段——演示 → 实时遥操作纠正("指导")→ 基于自主经验的优势条件化强化学习,用学得的价值函数为下游成功分配信用。报告结果(截至 2025-11,公司口径):做浓缩咖啡成功率约 40%→90%+,吞吐量约翻倍;纸箱组装约 60%→95%+;一台浓缩咖啡工作站自主运行约 18 小时,在新住宅中叠完 50 件未见过的衣物,组装并贴标 59 个工厂纸箱。π*0.6 权重截至 2026-07 未发布(开放请求见 openpi issue #789;openpi 仍仅提供 π0/π0-FAST/π0.5)。
- **π0.7**(2026-04-16 宣布):"可引导的"通才模型——公司报告单一检查点在多样灵巧任务上匹敌微调专家模型,具备组合泛化(重组已学技能解决新问题)、通过逐步语言指导执行未见任务,并可通过元数据(速度/质量)、视觉子目标和控制规格进行提示;在无该平台任何训练数据的情况下于双臂 UR5e 上演示叠衣服(公司口径)。权重截至 2026-07 未发布。
- 融资:**2025-11 以 $5.6B 估值融资 $600M**,由 Alphabet 旗下 CapitalG 领投,Jeff Bezos、Thrive、Lux、Index、Emergence 和 T. Rowe Price 参投;截至 2025-11 累计融资约 $1.1B(上一轮:2024-11 以 $2.4B 估值融资 $400M,投资方包括 Jeff Bezos、OpenAI、Thrive、Lux、Bond)。2026-03 Bloomberg 报道该公司正洽谈以超过 $11B 的估值再融资约 $1B(Founders Fund、Lightspeed 在谈;截至 2026-07 交易未确认完成)。见[投资](investment.md)与[关键人物](key-people.md)(Hausman、Levine、Finn)。

## NVIDIA Isaac GR00T N 系列

- **N1**(2025-03,GTC):NVIDIA 称之为首个面向通用人形机器人的开放基础模型。约 2B 参数;双系统设计——Eagle-2 VLM(System 2)+ 扩散-transformer 动作头(System 1);在由真实遥操作、合成数据(Omniverse/Cosmos、GR00T-Dreams)和人类视频组成的"数据金字塔"上训练。已在 Fourier GR-1、1X NEO 等平台上验证。
- **N1.5**(2025-05):冻结并升级为 Eagle 2.5 VLM 以改善 grounding;新增 FLARE(Future LAtent Representation Alignment),可从人类视频学习;NVIDIA 称 DreamGen/GR00T-Dreams 合成流水线将约 3 个月的人工数据采集压缩到 36 小时(公司口径)。面向 Jetson Thor 机上算力([硬件](hardware.md))。
- **N1.6**(2025-09-29 CoRL 宣布,2026-01-05 CES 前后发布):集成 **Cosmos Reason** 作为推理 VLM"深度思考大脑";扩展到人形全身控制——移动与操作同时进行,例如推开重门;可在 NVIDIA 开放的 Physical AI Dataset 上后训练(截至 2025-10 下载量 480 万+);通过 Hugging Face LeRobot 集成分发。
- **N1.7**(2026-04-17 早期访问):3B 参数;骨干换为 Cosmos-Reason2-2B(Qwen3-VL 架构)+ 32 层 DiT 动作头;预训练新增 **EgoScale**——20,854 小时、覆盖 20+ 任务类别的第一人称人类视频(N1.6 仅有数千小时遥操作数据),采用人类与机器人本体共享的相对末端执行器动作空间。NVIDIA 宣称发现"首个机器人灵巧性的 scaling law":视频时长从 1k 扩展到 20k 小时可使平均灵巧任务完成率翻倍以上(公司口径,未证实)。支持本体包括 Unitree G1(含全身 SONIC 控制器)、LIBERO Panda、OXE WidowX、双臂 YAM、AGIBot Genie 1。代码 Apache-2.0;权重采用 NVIDIA Open Model License(允许商用)。
- **N2**(2026-03-16 GTC 预览):基于 **DreamZero** 世界-动作模型架构;NVIDIA 称机器人"在新环境中完成新任务的成功率是领先 VLA 模型的两倍以上",并在 MolmoSpaces 和 RoboArena 通才策略榜单排名第一(截至 2026-03,公司口径);计划 2026 年底正式发布。NVIDIA 在 GTC 上的表述:用世界模型把机器人领域的数据问题换成算力问题。见[世界模型](world-models.md)。
- 战略姿态:NVIDIA 把 GR00T 定位为"机器人界的 Android"——通过开放(偏开放)模型带动其 Jetson Thor / Jetson T4000 机上算力需求(见[硬件](hardware.md)、[组织机构](organizations.md))。

## Google DeepMind Gemini Robotics

- **Gemini Robotics + Gemini Robotics-ER**(2025-03-12):基于 Gemini 2.0 的 VLA,加上一个独立的具身推理(ER)模型负责空间理解、指点与规划;与包括 Apptronik(Apollo 人形机器人)在内的伙伴共同开发。
- **Gemini Robotics On-Device**(2025-06-24):首个完全在机器人本地运行(无需云端)的 Gemini VLA,面向低延迟和离线场景;也是 DeepMind 首个开放微调的 VLA——只需 50–100 条演示即可适配;配套 Gemini Robotics SDK,含 MuJoCo 仿真评估。
- **Gemini Robotics 1.5 + ER 1.5**(2025-09-25):智能体式技术栈——ER 1.5 是编排器(规划、调用网页搜索等数字工具、下发自然语言子指令),Robotics 1.5 是"思考型 VLA",行动前输出可解释的推理轨迹。演示了**运动迁移(motion transfer)**:仅在 ALOHA-2 上训练的技能可零样本迁移到 Apptronik Apollo 和双臂 Franka,反之亦然。ER 1.5 声称在 15 个具身推理基准(ERQA、Point-Bench、RefSpatial)加 ASIMOV 安全基准上达到 SOTA。ER 1.5 已通过 Gemini API 正式开放;1.5 VLA 仍限定合作伙伴使用(截至 2026-06)。
- **Gemini Robotics-ER 1.6**(2026-04-14 经 Gemini API / AI Studio 发布):改进空间与多视角推理;新增读取模拟仪表和视镜的能力,与 Boston Dynamics 合作开发,后者正将该模型集成到其 Spot 巡检平台;DeepMind 称其在对抗性空间推理安全评估中是其迄今最安全的机器人模型。

## Figure Helix

- **Helix**(2025-02-20):面向人形机器人上半身控制的"System 1、System 2" VLA——S2 是运行在 7–9 Hz 的 7B 开源 VLM;S1 是 8000 万参数、200 Hz 的视觉运动 transformer,在 35 自由度动作空间(手腕、手指、躯干、头部注视)上输出连续指令。用约 500 小时遥操作数据训练;完全在机上双嵌入式 GPU 运行;同一套权重驱动两台机器人协作完成共享任务。Figure 声称多项"第一":首个高频全上半身人形 VLA、首个多机器人 VLA、首个完全机上运行的商用 VLA(公司口径)。Figure 于 2025-02 终止与 OpenAI 的合作,转而自研 Helix。权重闭源。
- **物流规模化**(2025):演示数据从约 10 小时扩展到约 60 小时后,单包裹处理时间从约 6.84 秒降至约 4.31 秒,条码扫描成功率从 88.2% 升至 94.4%;新增有状态视觉记忆、力觉输入和"Sport Mode"(执行速度 +50%)(公司口径,截至 2025-06)。
- **Helix 02**(2026-01-27):新增 **System 0**——位于 S1/S2 之下、1 kHz 运行的 1000 万参数全身反射/平衡控制器,在 20 万+ 个域随机化并行仿真环境中用 1,000+ 小时人类运动数据训练;新增触觉感知(可检测约 3 克的力)和掌心相机以获取手内视觉反馈。招牌演示:连续约 4 分钟的厨房序列——61 个连贯移动-操作动作完成洗碗机取放,全程无复位、无干预;Figure 称之为迄今最长时程的自主人形任务(公司口径,无第三方基准)。另演示了药片分拣、精准注射器分液。
- Helix 驱动 Figure 02/03 机器人开展物流试点和家庭测试;Figure 03(2025-10)围绕 Helix 设计——见[人形机器人](humanoid-robots.md)。

## 开放学术/社区模型与基准

- **Open X-Embodiment / RT-X**(2023-10):汇集来自 21 家机构、22 种机器人本体的 100 万+ 条 episode;RT-1-X 比各实验室原模型平均高约 50%;成为 Octo 和 OpenVLA 的标准预训练语料。
- **Octo**(2024-05):27M/93M 参数 transformer 加扩散头,在 80 万条 OXE 轨迹上训练;首个被广泛使用的完全开放通才策略,可在消费级 GPU 上运行。
- **OpenVLA**(2024-06):7B,在 97 万条 OXE episode 上训练;在 29 个评估任务上比 55B 的 RT-2-X 绝对成功率高约 16.5%——这是"开放的小模型能击败闭源巨型模型"的标志性结果。
- **OpenVLA-OFT**(2025):优化的微调配方在 LIBERO 四个套件上平均达 97.1%,在该基准上击败 π0、Octo 和扩散策略基线。
- **SmolVLA**(2025-06):450M 流匹配 VLA,主要在社区贡献的 LeRobot 数据集上训练;参数量约为 OpenVLA 的 1/15,却在 LIBERO 和 Meta-World 上超越 Octo/OpenVLA(单一实验室的说法);可在消费级硬件上运行;是经 LeRobot 框架入门的爱好者/研究者默认选择。
- **在用基准**(截至 2026-06):LIBERO(130 个仿真任务;已在约 97% 处饱和,如今只是健全性检查)与 SimplerEnv(仿真操作)、DROID(真实世界 Franka 语料/评测)、RoboArena(众包真机对决评测)、MolmoSpaces(2026,空间/通才策略基准)、GM-100(Ant Group,3 个平台上 100 个真机任务——最佳平均成功率仍仅约 17%,是对演示视频的清醒对照)。真实世界评估与自报数字仍是该领域最薄弱的一环(ICLR 2026 社区反复批评的问题)——见[开放问题](open-problems.md)。

## 中国的 VLA 生态(简述)

- 中国实验室在 2025–26 年密集发布 VLA,并明显倾向以开放权重作为分发策略:ByteDance Seed 的 **GR-3** 和 AgiBot 的 **GO-1**(均在下文详述);Unitree 开源的 **UnifoLM-VLA-0**(权重 + 代码 2026-01-29 发布)驱动 G1 完成家务任务;X Square Robot 的开放 4B 模型 **WALL-OSS**(2025-09),其 WALL-OSS-0.5 技术报告(2026)新增在 9000 万样本多模态语料上的单阶段训练,以及 **WALL-B**(2026-04)——一个横跨感知、语言、动作与物理预测的统一基础模型;该公司连续完成四轮融资,最终 Series C 估值超 $2.8B(200 亿元人民币),并声称不同阶段分别获得 Alibaba、ByteDance、Meituan、Xiaomi 领投(公司通稿,截至 2026-06)。
- **GR-3**(ByteDance Seed;技术报告 2025-07-21,arXiv:2507.15493):4B 参数 VLA——Qwen2.5-VL-3B-Instruct 骨干 + 流匹配扩散-transformer(DiT)动作头——通过网络规模视觉-语言数据联合训练、VR 设备采集的人类轨迹微调、机器人遥操作模仿学习训练而成;控制 ByteDance 的双臂移动机器人 **ByteMini**。报告在其三个评测套件上全面胜过 π0(如长时程餐桌收拾指令跟随成功率 97.5%;灵巧布料操作平均进度 86.7%)(自报)。截至 2026-07 无公开权重。注意勿与 Fourier 的 GR-3 混淆——后者是面向照护的人形机器人*硬件*平台(见[产业图景:中国](landscape-china.md))。
- **GO-1**(AgiBot,2025-03;arXiv:2503.06669):**ViLLA** 架构(vision-language-latent-action)——InternVL2.5-2B VLM + 预测离散隐式动作 token 的 24 层隐式规划器 + 用于连续控制的扩散动作专家;在 **AgiBot World**(100 万+ 条轨迹、2,976 小时、217 个任务,由 100 台双臂人形机器人采集)上预训练。论文报告比 Open X-Embodiment 预训练平均高 30%,在复杂真实任务上成功率超 60%(比 RDT 高 32%)。数据集、代码与权重(GO-1 及去掉隐式规划器的轻量版 GO-1-Air)以 CC BY-NC-SA 4.0 在 Hugging Face 开放;IROS 2025 最佳论文奖入围。
- **LingBot-VLA**(Ant Group / Robbyant;论文、权重与代码库 2026-01-27 发布):Ant 的首个开放具身 AI 模型;在 9 种双臂本体(AgileX、Galaxea R1Pro、AgiBot G1 等)约 20,000 小时遥操作双臂数据上训练;在 GM-100 上带深度输入取得 17.30% 平均成功率 / 35.41% 进度——在同一后训练协议下高于 π0.5、GR00T N1.6 和 WALL-OSS(自报)。
- 广为流传的"100+ 中国 VLA"数字源自 ResearchInChina 的《VLA Large Model Applications in Automotive and Robotics Research Report, 2025》(2025-09 发布)。其原始表述比传播版本窄:"机器人领域超过 100 个 VLA 模型**及相关数据集**"——这是把模型与数据集混在一起的全行业统计,且不限于中国实验室(方法学未公开;市场研究估计)。该报告另统计了 40+ 大模型框架/解决方案,并综述了中国车企(XPeng、Li Auto、Chery、Geely、Xiaomi Auto)的 VLA 式驾驶技术栈。详见[产业图景:中国](landscape-china.md)。

## 训练数据:根本约束

- 典型现代配比(π0.5、GR00T N1.7、Gemini Robotics):网络规模图文数据(语义)+ 跨本体机器人遥操作(前沿模型 1 万–2 万小时:π0 约 1 万小时,LingBot-VLA 约 2 万小时)+ 合成/仿真 rollout + 第一人称人类视频(GR00T N1.7 约 2 万小时的 EgoScale 语料;辅以 FLARE 和运动迁移技术加以利用)。
- 跨本体迁移已在产品层面得到验证(Gemini Robotics 1.5 的运动迁移;π0.5 的多机器人联合训练),意味着在任何一台机器人上采集的演示原则上可以改进所有机器人。
- 从部署经验中做强化学习(π*0.6/RECAP)是最新的数据来源,把机队运行时间转化为训练信号,而非只依赖人工遥操作;世界模型则是另一条摆脱遥操作数据稀缺的路径(NVIDIA GTC 2026:把数据问题变成算力问题)。见[数据](data.md)。

## 2026 年中局势

- 生产部署已存在但范围狭窄:Helix 用于物流包裹处理,基于 π 的模型进入商业试点(浓缩咖啡、叠衣、工厂配套),基于 GR00T 的技术栈遍布 NVIDIA 的人形机器人合作伙伴(截至 2026-06)——见[技术现状](state-of-the-art.md)。
- 开放权重前沿:openpi(π0、π0-FAST、π0.5)和 GR00T N1–N1.7 是当前可下载的最强开放 VLA;中国的开放发布(LingBot-VLA、WALL-OSS、UnifoLM-VLA)正在缩小差距;Gemini Robotics 各 VLA、Helix 以及 π0.6/π*0.6/π0.7 仍闭源(截至 2026-07)。规律:美国前沿实验室把最好的部署模型留在闭源,而 NVIDIA 和中国玩家激进开放权重以培育硬件/平台生态。
- 架构走向:层级化(推理器 + 快策略,Helix 02 已到三层)正胜过单体解码;世界-动作模型(GR00T N2/DreamZero)和基于经验的强化学习("RL 回归",π*0.6)是被寄望突破模仿学习天花板的两条主要路径。
- 关键开放问题:可靠评估、长时程错误恢复、无护栏部署的安全论证,以及人类视频能否替代稀缺的遥操作数据——追踪见[开放问题](open-problems.md)与[技术树](tech-tree.md)。

## 来源

- https://www.pi.website/blog/pi05 — π0.5 发布(2025-04-22),架构、联合训练、未见住宅清洁结果
- https://github.com/Physical-Intelligence/openpi — π0、π0-FAST、π0.5 的开放权重/许可;检查点列表;π0.6 未发布(issue #789)
- https://www.pi.website/blog/pistar06 — π*0.6 + RECAP 方法及吞吐量/成功率数据(2025-11-17)
- https://www.pi.website/blog/pi07 — π0.7 "可引导模型"公告(2026-04-16):专家级通用性、语言指导、跨本体迁移
- https://arxiv.org/abs/2511.14759 — π*0.6 论文("a VLA That Learns From Experience")
- https://website.pi-asset.com/pi06star/PI06_model_card.pdf — π0.6 模型卡:5B VLM + 动作专家、训练任务
- https://www.pi.website/research/fast — FAST 动作 tokenizer、FAST+ 通用 tokenizer、约 5 倍训练成本优势的说法
- https://www.bloomberg.com/news/articles/2025-11-20/robotics-startup-physical-intelligence-valued-at-5-6-billion-in-new-funding — $5.6B 估值融资 $600M,CapitalG 领投(2025-11)
- https://www.cnbc.com/2024/11/04/jeff-bezos-and-openai-invest-in-robot-startup-physical-intelligence.html — 上一轮:$2.4B 估值融资 $400M(2024-11),Bezos/OpenAI/Thrive/Lux/Bond
- https://techcrunch.com/2026/03/27/physical-intelligence-is-reportedly-in-talks-to-raise-1-billion-again/ — 据报道洽谈以 >$11B 估值融资约 $1B(2026-03,据 Bloomberg)
- https://github.com/NVIDIA/Isaac-GR00T — GR00T N1.7 规格(3B、Cosmos-Reason2-2B 骨干、EgoScale 数据、许可)
- https://huggingface.co/blog/nvidia/gr00t-n1-7 — GR00T N1.7 深度解析:20,854 小时 EgoScale、32 层 DiT、灵巧性 scaling law、支持本体(2026-04-17)
- https://nvidianews.nvidia.com/news/nvidia-isaac-gr00t-n1-open-humanoid-robot-foundation-model-simulation-frameworks — GR00T N1 发布(2025-03)
- https://research.nvidia.com/labs/gear/gr00t-n1_5/ — GR00T N1.5 改进(Eagle 2.5、FLARE)
- https://nvidianews.nvidia.com/news/nvidia-releases-new-physical-ai-models-as-global-partners-unveil-next-generation-robots — GR00T N1.6 + Cosmos Reason 公告(CoRL,2025-09-29)
- https://nvidianews.nvidia.com/news/nvidia-and-global-robotics-leaders-take-physical-ai-to-the-real-world — GTC 2026-03:GR00T N2 预览、DreamZero、MolmoSpaces/RoboArena 第一名说法、2026 年底可用性
- https://the-decoder.com/gtc-2026-nvidia-wants-to-swap-robotics-data-problem-for-a-compute-problem/ — GTC 2026 世界模型/数据叙事
- https://deepmind.google/blog/gemini-robotics-15-brings-ai-agents-into-the-physical-world/ — Gemini Robotics 1.5 / ER 1.5(2025-09-25),思考型 VLA、运动迁移、基准说法、可用性
- https://deepmind.google/blog/gemini-robotics-on-device-brings-ai-to-local-robotic-devices/ — Gemini Robotics On-Device(2025-06),50–100 条演示微调、SDK
- https://deepmind.google/blog/gemini-robotics-er-1-6/ — Gemini Robotics-ER 1.6 发布(2026-04-14),仪表读取、安全性说法
- https://roboticsandautomationnews.com/2026/04/15/boston-dynamics-integrates-google-deepminds-gemini-robotics-model-into-spot-inspection-platform/100585/ — Boston Dynamics Spot + Gemini Robotics-ER 1.6 集成
- https://www.figure.ai/news/helix — Helix 架构(S2 7B @ 7–9 Hz,S1 80M @ 200 Hz)、500 小时遥操作、35 自由度、宣称的多项"第一"(2025-02-20)
- https://www.figure.ai/news/helix-02 — Helix 02:System 0 10M @ 1 kHz、1,000 小时人类运动数据、61 个动作的洗碗机演示(2026-01-27)
- https://www.humanoidsdaily.com/news/from-pixels-to-torque-figure-unveils-helix-02-and-the-era-of-whole-body-autonomy — 独立报道确认 Helix 02 日期、System 0 规格、61 动作 / 约 4 分钟洗碗机演示及最长时程说法
- https://www.figure.ai/news/scaling-helix-logistics — Helix 物流规模化指标(处理时间、条码成功率)
- https://arxiv.org/abs/2406.09246 — OpenVLA 论文:7B、97 万条 OXE episode、在 29 个任务上比 55B RT-2-X 绝对高 16.5%
- https://openvla-oft.github.io/ — OpenVLA-OFT 配方:LIBERO 平均 76.5%→97.1%、动作生成吞吐量 26 倍(arXiv:2502.19645)
- https://arxiv.org/html/2506.01844v1 — SmolVLA(450M、流匹配、LeRobot 社区数据)
- https://arxiv.org/abs/2507.15493 — ByteDance Seed GR-3 技术报告(2025-07-21):4B 参数、Qwen2.5-VL-3B 骨干 + 流匹配 DiT 头、VR 采集的人类轨迹、ByteMini 机器人、与 π0 的比较
- https://arxiv.org/abs/2503.06669 — AgiBot World Colosseo 论文:100 万+ 轨迹 / 2,976 小时 / 217 任务、100 台机器人;GO-1 ViLLA 架构(InternVL2.5-2B + 隐式规划器 + 扩散动作专家);比 OXE 预训练高 30%
- https://huggingface.co/agibot-world/GO-1 — GO-1 开放权重(CC BY-NC-SA 4.0);轻量版 GO-1-Air 亦已发布
- https://www.globenewswire.com/news-release/2025/09/11/3148371/28124/en/China-VLA-Large-Model-Applications-in-Automotive-and-Robotics-Research-Report-2025-Robots-on-the-Rise-Over-100-VLA-Models-Poised-to-Transform-Industries.html — ResearchInChina 报告(2025-09-11):"机器人领域超过 100 个 VLA 模型及相关数据集"统计的来源
- https://arxiv.org/html/2601.18692v1 — LingBot-VLA 论文:9 种本体 2 万小时双臂遥操作数据、GM-100 结果
- https://www.businesswire.com/news/home/20260127455032/en/Robbyant-Open-Sources-LingBot-VLA-as-a-Universal-Brain-for-Robots — Robbyant 新闻稿:LingBot-VLA 于 2026-01-27 开源(权重 + 代码库)
- https://www.marktechpost.com/2026/01/29/ant-group-releases-lingbot-vla-a-vision-language-action-foundation-model-for-real-world-robot-manipulation/ — 独立确认 LingBot-VLA 权重发布及 GM-100 分数(17.30% SR / 35.41% PS;胜过 π0.5、GR00T N1.6、WALL-OSS)
- https://arxiv.org/html/2605.30877 — WALL-OSS-0.5 技术报告(4B 开放 VLA、数据配比)
- https://github.com/unitreerobotics/unifolm-vla — UnifoLM-VLA-0 权重/代码发布(2026-01-29)
- https://mbreuss.github.io/blog_post_iclr_26_vla.html — ICLR 2026 VLA 研究综述(社区趋势、基准批评)
- https://en.wikipedia.org/wiki/Vision-language-action_model — VLA 定义、RT-2 提出该术语的出处
- https://www.therobotreport.com/x-square-robot-secures-140m-in-funding-for-ai-foundation-models/ — X Square Robot 的 WALL-OSS 与 $140M 融资
- https://www.prnewswire.com/apac/news-releases/x-square-robot-secures-four-consecutive-financing-rounds-surpasses-us2-8-billion-valuation-in-push-for-physical-ai-foundation-models-302813098.html — X Square Robot 公司通稿(2026-06-29):连续四轮融资至 Series C、>$2.8B 估值、WALL-B/WALL-OSS-0.5/WALL-WM 模型
- https://techcrunch.com/2026/01/05/nvidia-wants-to-be-the-android-of-generalist-robotics/ — NVIDIA 在 CES 2026 上的开放模型战略叙事
