---
title: "公司深度剖析:NVIDIA 机器人技术栈"
slug: company-nvidia
updated: 2026-07-04
confidence: verified
lang: zh
source: ../wiki/company-nvidia.md
---
> NVIDIA 是 Physical AI 的平台供应商——"向每一家机器人制造商卖铲子"的打法,执行方式是一套**三台计算机理论**:在 DGX 上训练,在 Omniverse/Cosmos(OVX/RTX PRO 服务器)上模拟,在 Jetson 上执行。围绕这一骨架,它构建了该领域最深厚的技术栈:Isaac Sim/Lab 仿真(2025 年开源)、Newton 物理引擎(Linux Foundation 托管,2026 年 GTC 上 1.0 正式发布)、开放的 GR00T 机器人基础模型系列(N1 2025-03 → N1.7 早期访问 2026-04 → N2/DreamZero 计划于 2026 年末正式发布)、Cosmos 世界模型(world model)系列(1 → 3,2025-01 至 2026-06)、Jetson Thor 车载计算(2025-08 正式发布),以及从自动驾驶(AV)延伸到人形机器人的 Halos 安全平台(2026-06)。NVIDIA 还投资于自己的客户(Figure、Skild、Neura),CEO 黄仁勋(Jensen Huang)将人形机器人描述为约 40 万亿美元的劳动力自动化总目标市场(TAM)。矛盾之处在于:NVIDIA 披露的汽车与机器人业务收入在 2026 财年 2,159 亿美元总收入中仅约 23 亿美元(约 1%),机器人专项收入完全未单独披露,而其最大的机器人制造客户(Tesla、Figure)正在积极开发非 NVIDIA 的车载芯片。相关背景:[仿真](simulation.md)、[世界模型](world-models.md)、[硬件](hardware.md)、[VLA 模型](vla-models.md)、[格局:美国](landscape-usa.md)、[投资](investment.md)。

## 平台理论:三台计算机,卖铲子的生意

- **三台计算机架构**(NVIDIA 自己的表述,自 2024 年末以来已成为标准说法):(1)**DGX/HGX** AI 超级计算机,用于*训练*机器人基础模型;(2)**Omniverse + Cosmos,运行于 OVX / RTX PRO 服务器**,用于*仿真、测试并生成合成数据*(Isaac Sim、Isaac Lab、数字孪生);(3)**Jetson AGX Thor**(机器人)/ DRIVE AGX Thor(车辆),用于*执行*——机器人本体上的推理。三者均运行 Blackwell 世代芯片,因此客户机器人项目的每一层都在为 NVIDIA 硬件创收。
- 战略逻辑:NVIDIA 不卖机器人;它志在成为**"机器人领域的 CUDA"**——每一家机器人制造商都标准化使用的底层基础设施,无论哪家机器人公司胜出都能从中获利。媒体的简称是"通用机器人领域的 Android"(TechCrunch,2026-01)——用(半)开放的模型来培育对闭源、高利润率算力的需求。
- 模型层刻意保持**开放权重(open-weight)**(GR00T 采用 NVIDIA 自有开放模型许可证,Cosmos 采用宽松许可),而变现层(GPU、Jetson)保持专有——这与 [Figure](company-figure.md)(闭源模型、自研机器人)等垂直整合型厂商恰好相反。
- 配套的连接层:**OSMO**(跨三台计算机的工作流编排)、**Metropolis**(面向工厂的视觉 AI)、**Mega** Omniverse Blueprint(与西门子合作的工厂级数字孪生)、**Isaac ROS**(GPU 加速的 ROS 2 软件包)。
- 规模数据(NVIDIA,2026 年 3 月 GTC):平台上约有 **200 万机器人开发者**;4 万余家 Inception 初创企业;与 Hugging Face 的合作触达 1,300 万 AI 开发者——机器人是 Hugging Face 上增长最快的类别,NVIDIA 的模型下载量领先(截至 2026-01)。
- **独立方对护城河的印证(截至 2026-07)**:Stephen Witt 为《纽约客》(New Yorker)走访 1X、Skild、Caltech 等机构后写道(2026-07-06 期):"我在报道本文过程中接触到的每一台机器人都运行在英伟达芯片上,每一台都是在英伟达的数字健身房里训练出来的。"同一篇文章还引用了一位前员工的说法,称 NVIDIA 是刻意打造了"供应商锁定"——让机器人制造商依赖其技术栈——这是目前关于 NVIDIA 无处不在的最强的第三方(非厂商)表态,不过其覆盖范围仅限于这位记者恰好看到的那些机器人。

## 仿真层:Isaac Sim、Isaac Lab、Newton、Arena

详细内容见 [仿真](simulation.md);以下是 NVIDIA 特有的脉络:

- **Isaac Sim 5.0 + Isaac Lab 2.2** 在 GitHub 上开源(2025-08 SIGGRAPH 正式发布)——基于 Omniverse/OpenUSD 的完整机器人仿真,配备 RTX 传感器仿真与合成数据流水线(Replicator、MimicGen→SkillGen 轨迹倍增)。
- **Isaac Lab 2.3**(2025-09):自动域随机化(domain randomization)、基于种群的训练(可运行至 40,960 个并行环境)、灵巧遥操作(dexterous teleoperation);**Isaac Lab Arena** 策略评估框架,与 Lightwheel 联合开发。**Isaac Lab 3.0** 在 2026-03 GTC 上早期访问——定位为基于 DGX 基础设施的大规模机器人学习。
- **Newton 物理引擎**:与 Google DeepMind 和 Disney Research 联合开发,已捐赠给 Linux Foundation(2025-09),**1.0 正式版于 2026-03 GTC 发布**,内置 MuJoCo-Warp 求解器、可变形体仿真,以及用于训练迪士尼 BDX 机器人的 Disney Kamino 求解器。这是在物理层面对"锁定"批评的一种治理层面妥协。
- **GR00T Blueprint / GR00T-Dreams**:合成数据生成——NVIDIA 宣称在 N1 发布时(公司口径,2025-03)11 小时内生成了 78 万条轨迹(约相当于 9 个月的人类演示数据);DreamGen "神经轨迹"是通往[世界模型](world-models.md)数据引擎的桥梁。

## 模型层:GR00T 系列

完整谱系与架构见 [VLA 模型](vla-models.md)。"Project GR00T" 于 2024-03 GTC 上与 Jetson Thor 一同宣布;截至 2026-07 的状态如下:

| 模型 | 日期 | 状态 | 要点 |
|---|---|---|---|
| GR00T N1 | 2025-03-18(GTC) | 开放权重 | 号称首个开放的人形机器人基础模型;约 20 亿参数,双系统架构(Eagle-2 VLM + DiT 动作头);早期合作伙伴包括 1X、Agility、Boston Dynamics、Mentee、NEURA |
| GR00T N1.5 | 2025-05 | 开放权重 | 冻结的 Eagle 2.5 VLM;从人类视频中学习的 FLARE;面向 Jetson Thor |
| GR00T N1.6 | 2025-09-29 CoRL 宣布,2026-01 CES 发布 | 开放权重 | 以 Cosmos Reason 作为推理大脑;全身移动-操作(loco-manipulation);通过 LeRobot 分发 |
| GR00T N1.7 | 2026-04-17 | **早期访问**,开放权重(NVIDIA 开放模型许可证) | 30 亿参数;Cosmos-Reason2-2B 骨干网络;EgoScale 20,854 小时第一人称人类视频;宣称"首个机器人灵巧度扩展定律(scaling law)"(公司口径) |
| GR00T N2 | 2026-03-16 GTC 预览 | **预览版;正式发布计划于 2026 年末**(截至 2026-07 尚未正式发布) | 基于**DreamZero** 世界-动作模型构建;宣称在新任务/新环境上成功率约为领先 VLA 的两倍,在 MolmoSpaces 与 RoboArena 上排名第一(公司口径) |

- GR00T 的这套打法呼应了行业整体的架构收敛趋势:双系统 VLA → 推理型 VLA → 世界-动作模型(VLA 与世界模型两条脉络正在融合)。
- **Isaac GR00T 参考人形机器人**(在 2026-05-31 GTC Taipei/COMPUTEX 上宣布):一款开放参考设计——Unitree H2 Plus 机身 + Sharpa Wave 触觉灵巧手(dexterous hand) + Jetson Thor T5000 + Isaac GR00T 技术栈——面向学术实验室(Ai2、苏黎世联邦理工学院、斯坦福机器人中心、加州大学圣地亚哥分校);据 NVIDIA 发布会所述,将于 2026 年末通过 Unitree 提供(未给出具体月份)。值得注意的是:NVIDIA 面向美国市场的参考平台采用的是一具中国机器人机身([Unitree](company-unitree.md))。

## 世界模型层:Cosmos

完整内容见 [世界模型](world-models.md);以下是平台战略视角:

- **Cosmos 1**(2025-01-06 CES):开放的世界基础模型,训练数据约 9,000T tokens / 2,000 万小时视频;首批采用方包括 1X、Agility、Figure、Fourier、Galbot、Skild、Waabi、XPENG、Uber。**Cosmos Reason**(2025-03 GTC)增加了物理推理(physical-reasoning)VLM——现已成为 GR00T N1.6/N1.7 的骨干网络。**Predict 2.5 / Transfer 2.5**(2025-10):30 秒推演(rollout);模拟到现实(sim2real)风格迁移。**Cosmos 3**(2026-03 GTC 上发布,2026-05-31 GTC Taipei 完全开源发布):被称为"首个完全开放的全模态模型(omnimodel)"——支持文本/图像/视频/声音/**动作**生成;推出 Super/Nano/Edge 三种变体;并成立了一个"Cosmos 联盟"(Agile Robots、Black Forest Labs、Generalist、LTX、Runway、Skild AI)。CMR Surgical 使用一款 **Cosmos-H** 变体来验证其手术系统(据 2026 年 GTC 发布会)。
- **Cosmos Policy**(2026-01):将 Cosmos 进行后训练(post-train)转化为控制模型——在 LIBERO 上达到 98.5%(据报道)——将世界模型定位为*策略骨干网络*,而不仅仅是数据引擎。
- 下载量:Cosmos 世界基础模型下载量突破 **300 万次**,开放的 NVIDIA Physical AI 数据集下载量突破 **480 万次**(截至 2025-09,NVIDIA 数据,来自 2025-09-29 CoRL 发布会)。
- 战略意图:Cosmos 把机器人领域的数据稀缺问题转化为 GPU 需求——NVIDIA 在 2026 年 GTC 上的表述直接就是要"把数据问题换成算力问题"。

## 执行层:Jetson,以及 Halos 安全平台

细节见 [硬件](hardware.md)。Jetson 产品线脉络:TK1(2014)→ TX1/TX2 → AGX Xavier(2018)→ AGX Orin(2022,275 TOPS,2023-25 年间人形机器人的主力芯片)→ **Thor**:

| 型号 | AI 算力 | 内存 | 价格 | 状态 |
|---|---|---|---|---|
| Jetson AGX Thor(T5000) | 2,070 TFLOPS(FP4 稀疏) | 128 GB | 3,499 美元开发者套件 | **2025-08-25 正式发布**;算力为 Orin 的 7.5 倍 |
| Jetson T4000 | 1,200 TFLOPS(FP4 稀疏) | 64 GB | 1,999 美元(千片起订价) | 2026-01 CES 上宣布(中端型号) |

- Thor 的 128 GB 内存足以在机器人本体上装载数十亿参数的 VLA 模型;早期采用者包括 Agility、Amazon Robotics、Boston Dynamics、Figure、Caterpillar、Meta;1X NEO 搭载 Thor 出货;OpenAI 和 Physical Intelligence 正在评估中(截至 2025-08,NVIDIA 名单)。
- **机载 NVIDIA 算力的功耗代价**:据 Witt 在《纽约客》上的报道(2026-07-06 期),一枚 NVIDIA 边缘芯片"可能耗尽机器人多达六成的电力供应"——相比之下,人脑消耗的身体能量约为 20%;Apptronik CEO Jeff Cardenas 在同一篇文章中说:"占用电池最多的不是电机,而是算力。"这为下文以及 [硬件](hardware.md) 中提及的价格/功耗敏感性风险提供了一个具体数字。
- **Halos**:于 2025-03 GTC 上作为自动驾驶(AV)全栈安全系统推出;**2026-06-22(Automate 2026)宣布 Halos for Robotics**——号称是业内首个面向 Physical AI 的全栈安全系统。四层架构:**IGX Thor** 工业级计算、**Holoscan Sensor Bridge**、**Halos OS** 安全软件,以及 **Halos AI Systems Inspection Lab**(为 IEC 61508、ISO 13849、ISO/IEC TR 5469 认证做准备)。NVIDIA 宣称该平台把超过 18,600 个工程师-年的自动驾驶安全工作经验迁移到了机器人领域(公司口径)。**Agility Robotics 是首个采用方**,应用于 Digit——安全能力成为平台化售卖的功能,这在该领域尚属新鲜事;参见 [安全与监管](safety-regulation.md)。

## 垂直领域

- **Isaac for Healthcare**(2025-03 GTC 推出):医疗机器人开发平台(数字孪生、合成数据生成(SDG)、IGX/Holoscan 边缘部署)。截至 2026 年 GTC:**强生医疗科技(Johnson & Johnson MedTech)** 正使用 Isaac Sim + Cosmos 训练其 Monarch 平台(计划 2026 年在美国推出泌尿科应用);**美敦力(Medtronic)** 正在评估用于手术系统的 IGX Thor;**CMR Surgical** 正用 Cosmos-H 验证 Versius。
- **面向 AMR(自主移动机器人)/ 工业领域的 Isaac**:Isaac Perceptor/Nova 传感器技术栈;Isaac AMR 路径规划 + Metropolis 视觉智能体已部署于富士康休斯顿工厂;2026 年 GTC 上宣布了与 **FANUC、ABB、KUKA、安川(Yaskawa)**(合计安装基数超 200 万台机器人)的虚拟调试集成——这是从人形机器人切入现有工业机械臂存量市场的楔子。
- **工厂作为客户与展示样板**:富士康位于休斯顿、占地 242,287 平方英尺的 AI 服务器工厂在 Omniverse 中设计,计划成为最早运行**由 GR00T 驱动的人形机器人**的产线之一(2025-10 宣布;部署目标为 2026 年第一季度,与 GB300 服务器生产同步;截至 2026-07,尚无独立证据确认人形机器人已投入生产运行——应视为进行中)。TSMC(凤凰城晶圆厂)、丰田(乔治敦)、Caterpillar、Lucid、纬创(Wistron)、Belden 均被列为 Omniverse/Isaac 用户(GTC DC,2025-10-28)。

## 合作与投资图谱(截至 2026-07)

| 关系类型 | 对象 | 实质内容 |
|---|---|---|
| 股权投资 | [Figure](company-figure.md)(2024-02 B 轮 + 2025-09 C 轮)、Skild AI(NVentures,2025 年 + 2026-01 C 轮)、Neura Robotics(2026-06 轮) | NVIDIA 在投资自己未来的平台客户——一种"造王者(kingmaker)"动态(参见 [投资](investment.md)) |
| 模型/基础设施客户 | Figure(据 NVIDIA 2025-10-28 公关稿,"使用 NVIDIA 加速计算"构建 Helix,并用 Isaac 做仿真/训练)、Skild、Boston Dynamics、Agility、1X(NEO 搭载 Thor)、AGIBOT、Hexagon | 即使是拥有自研模型的实验室也在 NVIDIA GPU 上训练;Figure 的 Helix 是闭源的,但由 NVIDIA 训练 |
| GR00T 生态 | 1X、Agility、Boston Dynamics、Mentee、NEURA(N1 发布时);Fourier、Franka、AGIBOT、Unitree(参考人形机器人)后续加入 | 开放模型的分发渠道;验证深度参差不齐(许多仍是试点/评估阶段) |
| 制造业 | 富士康(休斯顿人形机器人 + 得州/威斯康星州/加州的 AI 服务器产能;也主导了 Agility 的 SPAC PIPE 融资)、TSMC、丰田、宝马(自 2021-23 年起用于工厂数字孪生的 Omniverse)、梅赛德斯、现代(通过 Boston Dynamics 母公司涉足自动驾驶与机器人) | 工厂数字孪生是切入点;宝马的人形机器人供应商是 Figure,而非 NVIDIA 直接供应 |
| 仿真/物理层盟友 | Google DeepMind + Disney Research(Newton)、Lightwheel(Arena)、Hugging Face/LeRobot | 竞合关系:DeepMind 在模型层是竞争对手,但在物理层是合作伙伴 |
| 云服务 | 微软 Azure(Physical AI Data Factory 蓝图)、CoreWeave(Isaac Lab 流水线)、阿里云(全栈) | 三台计算机可以租用,不必只能购买 |

## 机器人收入与话术的落差

叙事与已披露数字之间的鸿沟,是怀疑论者最核心的论据:

| 指标(截至 2026-05 报道) | 数值 |
|---|---|
| 2026 财年总收入(截至 2026-01-25 的财年) | **2,159 亿美元** |
| 2026 财年数据中心业务 | 1,937 亿美元(约 90%) |
| 2026 财年汽车业务线(含机器人;DRIVE + Jetson) | **23 亿美元(约 1.1%)**;第四季度:6.04 亿美元,对比数据中心业务的 623 亿美元 |
| 2027 财年第一季度(截至 2026-04-26,2026-05-20 发布) | 总收入 816 亿美元;**新的业务分类**:数据中心 752 亿美元;**边缘计算(Edge Computing)64 亿美元**(同比增长 29%) |
| 机器人专项收入 | **从未单独披露** |

- 从 2027 财年第一季度起,NVIDIA 将财报口径合并为两大板块——数据中心与**边缘计算**,其中机器人业务与**个人电脑、游戏主机、工作站、AI-RAN 及汽车业务**混在一起——恰恰在话术达到顶峰之际,让机器人收入变得*更难*被看清。
- 相对靠谱的乐观论点是:机器人业务今天的收入贡献主要是*间接*的——每一家机器人实验室的训练集群都算作数据中心收入(Figure、Skild、PI、OpenAI 都在 NVIDIA 上训练),因此机器人技术栈相当于为核心业务提供了一种需求保险。
- **黄仁勋的 TAM 话术**:"通用机器人的 ChatGPT 时刻即将到来"(2025 CES);"通用机器人的时代已经到来"(2025-03 GTC);"Physical AI 已经到来——每一家工业公司都将成为机器人公司"(2026-03 GTC)。财经媒体(2026-05)多次报道他将人形机器人描述为约 **40 万亿美元**的劳动力自动化 TAM(二手转述;他与马斯克也曾提出过约 50 万亿美元的"physical AI"数字)——这一数字比该行业任何已披露的机器人收入都高出约四个数量级。

## 竞争格局

| 挑战者 | 打法 | 状态(截至 2026-07) |
|---|---|---|
| **高通(Qualcomm)** | 在 2026-01 CES 上推出全套机器人方案:Dragonwing IQ10(面向人形机器人/AMR 的 18 核高端 SoC)、明确对标 Jetson 功耗/成本优势的 Dragonwing Robotics Development Platform;收购 Arduino(2025-10,拥有 3,300 万用户社区;Uno Q / Ventuno Q 开发板) | 生态伙伴包括 Advantech、Booster、KUKA、VinMotion——以及 **Figure**,后者正与高通"合作定义下一代计算架构"(高通公关稿)——这是 NVIDIA 旗舰客户叙事上的一道明显裂缝 |
| **Tesla(自研)** | AI5 定制芯片已于 2026-04-15 流片(三星 + 台积电代工),量产计划在 2027 年中后期,面向 Optimus 与推理集群 | 垂直整合的退出路径:目前仍在 NVIDIA 上训练,但计划最终不再需要 Jetson |
| **华为** | CloudRobo 具身智能(embodied AI)平台("端-边-云"重云架构) + 昇腾(Ascend)芯片;明确对标 NVIDIA 的打法(Digitimes) | 随着美国出口管制收紧,已成为中国厂商的默认选项;截至 2026 年年中,尚无确认的主导性人形机器人设计中标案例(见 [格局:中国](landscape-china.md)) |
| **Google DeepMind** | Gemini Robotics 模型系列(闭源),在策略层与 GR00T 竞争 | 同时也是 NVIDIA 在 Newton/MuJoCo-Warp 上的合作伙伴——竞合关系 |
| **中国边缘芯片厂商** | 地平线机器人(Horizon Robotics)、黑芝麻(Black Sesame) | 被定位为国产 Jetson 替代方案;截至 2026 年年中未见广泛采用的人形机器人中标案例(未证实的缺席) |

- NVIDIA 的结构性优势:CUDA 开发者生态的引力(超过 400 万注册 CUDA 开发者)、Isaac Lab API 正在成为事实上的训练框架标准(甚至基于 MuJoCo 的 mjlab 也采用了它),以及唯一一套端到端的训练/仿真/执行方案。
- 结构性风险:中国市场准入(出口管制正推动这个最大的机器人制造大国转向国产技术栈);机载推理的价格/功耗敏感性(在约 2 万美元的机器人里,一台 3,499 美元级别的计算机是实打实的物料成本(BOM)项——见 [硬件](hardware.md));以及最大的机器人机队(Tesla,或许还有 Figure)正在走向垂直整合、脱离 NVIDIA。

## 怀疑论者的观点

- **发布密度不等于采用率**:合作伙伴名单在各类新闻稿中反复出现(CES、GTC、CoRL、Automate 上翻来覆去大约是同样那十几个名字);其中许多仍处于试点、评估或"正在探索"阶段。上文图谱所暗示的、经独立证实的全栈部署级应用要稀少得多。厂商的基准测试宣称(N2 的"比领先 VLA 高出两倍"、N1.7 的"灵巧度扩展定律"、Newton 的 252 倍/475 倍加速)都缺乏第三方复现——见 [评测](evaluation.md)。
- **"开源包装"批评**:GR00T 权重是在 NVIDIA 自有许可证下发布的(而非 Apache/MIT),Cosmos/Isaac 都针对——且实际上默认假设——NVIDIA 硬件进行了优化;所谓"开放的 Android"其实是通向封闭芯片的导流漏斗。反驳观点是:Newton 的 Linux Foundation 治理模式和货真价实的 Isaac Sim 开源,比大多数竞争对手所提供的要多。
- **生态锁定的担忧来自开发者本身的声音**:VLA 时代的工作负载是异构的(视觉、语言、动作、世界模型推理),而全盘采用 NVIDIA 的假设会妨碍针对每种工作负载混用最优加速器的做法——有观点认为,机器人业务反而可能*稀释*而非扩展 CUDA 的护城河(投资人/分析师评论,2026 年)。
- **客户集中度的讽刺之处**:美国资金最充足的人形机器人项目,恰恰是最有能力"出走"的那些——Tesla(AI5)、Figure(尽管 NVIDIA 持有其股权,仍与高通展开合作)。NVIDIA 投资自己的客户,也让"采用率"作为一个自然信号变得模糊不清。
- **收入不透明**:将机器人业务并入以游戏为主导的边缘计算板块(2026-05)意味着市场无法追踪机器人业务是否真的在增长——那个 40 万亿美元的故事,从 NVIDIA 自己的财报披露中根本无法被证伪。
- 持平而论:以上怀疑论点都没有触及核心的不对称优势——无论最终是哪家的机器人、哪家的机载芯片胜出,NVIDIA 都能从机器人 AI 的*训练*环节获利,而且没有任何竞争对手能提供集成的三台计算机全流程方案。"卖铲子"式定位对个别机器人厂商的失败具有很强的抗风险能力;它主要暴露的风险在于整个行业层面的[泡沫情景](investment.md)。

## 来源

- https://blogs.nvidia.com/blog/three-computers-robotics/ —— 三台计算机理论(DGX 训练 / Omniverse+Cosmos 仿真 / Jetson 执行),官方表述
- https://nvidianews.nvidia.com/news/nvidia-isaac-gr00t-n1-open-humanoid-robot-foundation-model-simulation-frameworks —— GR00T N1 发布(2025-03-18),早期合作伙伴(1X、Agility、Boston Dynamics、Mentee、NEURA)、Blueprint 78 万轨迹宣称、Newton 宣布
- https://research.nvidia.com/labs/gear/gr00t-n1_5/ —— GR00T N1.5(Eagle 2.5、FLARE)
- https://nvidianews.nvidia.com/news/nvidia-releases-new-physical-ai-models-as-global-partners-unveil-next-generation-robots —— N1.6 随 Cosmos Reason 集成发布 + LeRobot 分发(CES,2026-01-05)
- https://nvidianews.nvidia.com/news/nvidia-accelerates-robotics-research-and-development-with-new-open-models-and-simulation-libraries —— N1.6 宣布(CoRL,2025-09-29);Cosmos 300 万 / Cosmos Reason 100 万 / Physical AI 数据集 480 万下载量数据
- https://huggingface.co/blog/nvidia/gr00t-n1-7 —— GR00T N1.7 早期访问(2026-04-17):Cosmos-Reason2-2B 骨干网络、EgoScale 20,854 小时、许可信息
- https://nvidianews.nvidia.com/news/nvidia-and-global-robotics-leaders-take-physical-ai-to-the-real-world —— 2026-03-16 GTC:GR00T N2/DreamZero 预览及厂商宣称、Isaac Lab 3.0、Newton 1.0、Cosmos 3 发布、完整合作伙伴名单、200 万机器人开发者、Hugging Face 合作、黄仁勋"每一家工业公司"语录
- https://nvidianews.nvidia.com/news/nvidia-launches-cosmos-world-foundation-model-platform-to-accelerate-physical-ai-development —— Cosmos 1 发布(2025-01-06 CES),训练规模,采用方
- https://nvidianews.nvidia.com/news/nvidia-launches-cosmos-3-the-open-frontier-foundation-model-for-physical-ai —— Cosmos 3 开放发布(2026-06-01),全模态模型,各变体,联盟
- https://nvidianews.nvidia.com/news/nvidia-open-humanoid-robot-reference-design —— Isaac GR00T 参考人形机器人(Unitree H2 Plus + Sharpa Wave + Thor T5000,2026-06-01,学术界首批用户,Unitree 2026-10 起提供)
- https://nvidianews.nvidia.com/news/nvidia-blackwell-powered-jetson-thor-now-available-accelerating-the-age-of-general-robotics —— Jetson Thor 正式发布(2025-08-25),规格,3,499 美元开发者套件,采用方名单
- https://developer.nvidia.com/blog/accelerate-ai-inference-for-edge-and-robotics-with-nvidia-jetson-t4000-and-nvidia-jetpack-7-1/ —— Jetson T4000 规格与定价(2026-01 CES)
- https://nvidianews.nvidia.com/news/nvidia-announces-halos-for-robotics-the-industrys-first-full-stack-safety-system-for-physical-ai —— Halos for Robotics:四层架构,Agility 为首个采用方,目标认证标准
- https://www.robotics247.com/article/automate-2026-nvidia-announces-halos-for-robotics —— Halos for Robotics 发布日期/地点(Automate 2026,2026-06-22),18,600 工程师-年的表述
- https://developer.nvidia.com/blog/introducing-nvidia-isaac-for-healthcare-an-ai-powered-medical-robotics-development-platform/ —— Isaac for Healthcare 平台介绍(2025-03 GTC)
- https://www.jnj.com/media-center/press-releases/johnson-johnson-to-advance-robotics-development-with-nvidia-isaac-for-healthcare —— 强生医疗科技采用 Isaac for Healthcare;Monarch 训练
- https://nvidianews.nvidia.com/news/nvidia-us-manufacturing-robotics-physical-ai —— GTC DC(2025-10-28):Figure 在 NVIDIA 加速计算 + Isaac 上构建 Helix;富士康休斯顿工厂 242,287 平方英尺;Amazon BlueJay;TSMC/丰田/Caterpillar/Lucid 数字孪生;1.2 万亿美元美国产能框架
- https://www.investing.com/news/stock-market-news/foxconn-to-deploy-humanoid-robots-at-houston-ai-server-plant-4315135 —— 路透社:富士康在休斯顿 GB300 工厂部署 GR00T 驱动的人形机器人,目标 2026 年第一季度部署
- https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-fourth-quarter-and-fiscal-2026 —— 2026 财年业绩:总收入 2,159 亿美元,数据中心 1,937 亿美元,汽车业务 23 亿美元(第四季度:6.04 亿美元)
- https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-first-quarter-fiscal-2027 —— 2027 财年第一季度(截至 2026-04-26):总收入 816 亿美元;新的业务分类,数据中心(752 亿美元)/ 边缘计算(64 亿美元);边缘计算包含机器人 + 汽车 + 个人电脑/游戏主机
- https://www.cnbc.com/2026/05/20/nvidia-nvda-earnings-report-q1-2027.html —— 2027 财年第一季度财报发布日期与报道
- https://techcrunch.com/2026/01/05/nvidia-wants-to-be-the-android-of-generalist-robotics/ —— "机器人领域的 Android"表述;机器人是 Hugging Face 上增长最快的类别
- https://247wallst.com/investing/2026/05/31/jensen-huang-just-called-humanoid-robots-a-40-trillion-market-heres-why-wall-street-is-loading-up-on-physical-ai-stocks/ —— 40 万亿美元人形机器人 TAM 归于黄仁勋的表述(二手转述;财经媒体)
- https://www.qualcomm.com/news/releases/2026/01/qualcomm-introduces-a-full-suite-of-robotics-technologies-power —— 高通机器人套件(2026 CES):Dragonwing IQ10,生态包括与 Figure 的合作
- https://www.automate.org/robotics/news/ces-2026-qualcomm-targets-nvidia-jetson-with-new-robotics-developer-platform —— 高通 Dragonwing 平台对标 Jetson
- https://spectrum.ieee.org/qualcomm-arduino-acquisition-open-source —— 高通收购 Arduino(2025-10)及开源社区争议
- https://electrek.co/2026/04/15/tesla-ai5-chip-taped-out-musk-ai6-dojo3/ —— Tesla AI5 流片(2026-04-15),2027 年量产目标,面向 Optimus
- https://www.digitimes.com/news/a20250103PD214/huawei-nvidia-robotics-llm-robot.html —— 华为按照 NVIDIA 的平台模式进入人形机器人领域
- https://www.huaweicloud.com/intl/en-us/news/20250919133255709.html —— 华为 CloudRobo 具身智能平台介绍
- https://builtin.com/articles/nvidias-cuda-future-ai-infrastructure —— CUDA 锁定批评;认为异构机器人工作负载会削弱护城河的论点
- https://www.newyorker.com/magazine/2026/07/06/are-humanoid-robots-ready-to-be-deployed —— Witt:"我遇到的每一台机器人……都运行在英伟达芯片上/是在英伟达的数字健身房里训练出来的";边缘芯片消耗机器人多达 60% 的电池电量(Cardenas 引述);前员工对"供应商锁定"的表述(通过 Wayback 快照读取)
