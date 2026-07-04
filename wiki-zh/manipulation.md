---
title: 灵巧操作
slug: manipulation
updated: 2026-07-03
confidence: verified
lang: zh
source: ../wiki/manipulation.md
---
> 灵巧操作(dexterous manipulation)——用末端执行器抓取、重新调整姿态并控制物体,包括可形变物体与工具——是 Physical AI 的核心瓶颈:运动控制基本已被解决,操作还没有。2023–2026 年间,该领域的主流路线从任务专用控制转向大规模模仿学习(ALOHA/ACT、Diffusion Policy、UMI),并被吸收进[视觉-语言-动作基础模型(VLA)](vla-models.md);而基于真实世界经验的强化学习微调(π*0.6/RECAP,2025-11)重新兴起,用于提升可靠性。硬件呈两极分化:廉价的平行夹爪(parallel-jaw gripper)仍支撑着大多数已部署系统和大部分训练数据,而多指灵巧手(dexterous hand)(20+ 自由度、触觉皮肤)于 2025 年在中国进入量产(出货量超 3 万只)。截至 2026-07,旗舰能力——叠衣服、组装纸盒、装洗碗机、全天制作意式浓缩咖啡——相比人类仍然缓慢且易出错;任意物体的手内重定向、有力的工具使用以及标准化评测仍是未解问题。

## 为什么操作是最难的部分

- Moravec 悖论的现实体现:富接触物理(摩擦、柔顺性、间歇接触)比自由空间运动或[运动控制](locomotion.md)更难建模、仿真和学习。
- 接触动力学不连续且混沌——微小的位姿误差就能颠覆抓取结果;仿真器对刚体接触的处理已经不佳,对可形变物体(布料、线缆、食物)更差,限制了曾解决行走问题的模拟到现实(sim2real)路线(见[仿真](simulation.md))。
- 感知恰恰在最关键处被遮挡:接触瞬间手会挡住物体,这正是触觉传感的动机。
- 数据稀缺:不存在操作领域的互联网级语料;下文的每一种范式,本质上都是低成本获取带动作标注的接触数据的策略(见[数据](data.md))。
- 长程误差累积:家庭/工业任务串联数十个接触事件;即使单步成功率达 95%,整体任务仍会频繁失败,这也是吞吐量(每小时成功次数)正在取代单次尝试成功率成为关键指标的原因(π0.6 模型卡,2025-11)。

## 末端执行器:夹爪 vs 灵巧手

| 类型 | 自由度(典型) | 成本(典型,截至 2026) | 优势 | 劣势 | 示例 |
|---|---|---|---|---|---|
| 平行夹爪 | 1 | 数百至 $5k | 便宜、皮实、易建模,在数据集中占主导 | 无法手内重定向;对小件/扁平/需精度的可形变任务乏力 | Robotiq 2F-85、WSG-50、UMI 夹爪、Franka 手 |
| 吸盘/混合式 | 1–2 | 数百至 $5k | 平整表面、物流拣选 | 多孔/不规则物体失效;无灵巧性 | 仓储拣选机(见[技术现状](state-of-the-art.md)) |
| 欠驱动 2–3 指 | 3–11 | $5k–$20k | 自适应力量抓取,容错性好 | 精细操作能力有限 | Robotiq 3F、Shadow DEX-EE(3 指,与 DeepMind 合作) |
| 拟人多指手 | 16–24+ | 约 $3k(中国量产)至 $100k+(Shadow) | 手内重定向、工具使用、与人类工具兼容、便于遥操作 | 脆弱,高端昂贵,控制/数据饥渴 | Shadow Hand(24 关节)、Tesla Optimus Gen-3(22 自由度)、Unitree Dex5-1(20 自由度)、Inspire RH56、DexRobot DexHand021 |

- 实用派观点(双臂平行夹爪足以完成大多数任务;人类工具可以用力量抓取握持,不需要五根手指)在《The Case Against Human Hands》一文中被明确论证,并在实践中得到体现:ALOHA、UMI、π0 的叠衣服演示以及大多数仓储部署都使用简单夹爪。
- 极致派观点:小物体的捏取、手内换握、装配以及书写级精度都需要多指手;各大[人形机器人项目](humanoid-robots.md)(Tesla、Figure、Sanctuary、Apptronik、中国整机厂)现在都押注于此。
- Tesla Optimus Gen-3 手:22 自由度手 + 3 自由度腕,由前臂内置执行器经腱驱动(基于专利的分析统计每条前臂约 25 个执行器,而非完全按自由度配置执行器(二手来源,未证实)),指尖带触觉;2025 年演示中展示了接球和拿鸡蛋——多次被媒体指出为遥操作(teleoperation)。
- Shadow Hand 仍是自由度标杆(24 关节,约 20 个主动驱动,腱驱动,曾用于 OpenAI 2018–2019 年 Dactyl 的手内魔方/立方体工作);其 DEX-EE 3 指手(2023,与 Google DeepMind 合作)以牺牲拟人化换取在强化学习级磨损下的耐用性。
- 中国量产浪潮(据 Gasgoo 行业报道,单一来源):2025 年已知灵巧手出货量 >30,000 只——Gasgoo 按每台机器人两只手推算得出该数字;Inspire Robots 2025 年交付约 10,000 只手(2024 年约 2,000 只);Unitree 人形机器人出货量突破 5,500 台,但未单独披露灵巧手数据;LinkerBot 目标 2026 年出货 50,000–100,000 只(未证实)。见[产业格局:中国](landscape-china.md)。
- DexRobot DexHand021 Pro(2026-01 在 CES 亮相;完整灵巧手系列 + DexTele 遥操作系统于 2026-06 在 Automate 发布):22 自由度(腕手一体,双腱驱动),50 N 负载,全掌多模态感知,>30 万次耐久循环,约 $14k–28k——号称约为同类灵巧手成本的 1/5(公司 PR,未证实)。
- TESOLLO DG-5F(韩国):面向人形机器人市场的 20 自由度五指手(截至 2025)。
- 跨本体问题:在一种手上训练的策略难以迁移到另一种手;夹爪与灵巧手之分也割裂了数据生态(大多数开放数据集是平行夹爪)。见[未解问题](open-problems.md)。

## 触觉传感

- 为什么需要触觉:解决接触时的遮挡、实现打滑检测、限力抓取(鸡蛋、玻璃)、纹理/材质识别,以及纯视觉无法完成的富接触插装。
- 基于视觉的触觉(摄像头观察可形变凝胶):GelSight 系列主导研究界——微米级表面分辨率;2024–2025 年的变体包括 GelBelt(大面积表面)、ThinTact(无透镜)、DTactive(主动表面)以及模块化开源设计(Yuan 实验室,IJRR 2025)。
- Meta AI × GelSight Digit 360(2024-10 发布):指尖形传感器,约 830 万触觉单元(taxel),全向触觉,可检测低至约 1 mN 的力,18+ 种感知模态,端上处理;定位为开放的研究标准。
- 磁式/压电阵列皮肤正在灵巧手上胜出,因为它们又薄又便宜:Unitree Dex5-1 每只手配备 94 个触觉点(截至 2025);Tesla 在 Optimus Gen-3 上加入了指尖力传感。
- Tacta(CES 2026,公司口径,未证实):4.5 mm 模块内实现 361 传感单元/cm²、1 kHz;首个全手覆盖演示,指尖、指腹和手掌共 1,956 个传感单元。
- 策略层的整合尚早但在加速:触觉条件扩散策略(PolyTouch,2025)、触觉-语言-动作模型(TLA,2025)、VLA-Touch(为 VLA 提供双层触觉反馈,2025)、AnyTouch(跨视触觉传感器的统一表征,2025)。截至 2026-07,尚无前沿 VLA 将触觉作为一等模态输入——这一缺口被反复提及,因为人类视频和大多数遥操作数据集中都没有触觉数据。

## 模仿学习脉络:ALOHA/ACT → Diffusion Policy → UMI → VLA

2023–2024 年的模仿学习浪潮是今天 [VLA 模型](vla-models.md)的直系祖先;另见[历史](history.md)。

| 年份 | 系统 | 贡献 |
|---|---|---|
| 2023-04 | **ALOHA + ACT**(Zhao、Finn 等,斯坦福) | 约 $20k 的开源双臂遥操作平台;Action Chunking with Transformers(CVAE,预测动作序列而非单步)仅用约 50 条演示在精细任务上达到 80–90% |
| 2023(RSS) | **Diffusion Policy**(Chi、Song 等,哥伦比亚大学/TRI) | 对动作轨迹做去噪扩散;能处理多模态演示;相比此前 BC 基线平均提升约 47%;成为默认策略类 |
| 2024-01 | **Mobile ALOHA**(Fu、Zhao、Finn) | 全身双臂移动遥操作(约 $32k);与静态 ALOHA 数据联合训练提升 ACT/Diffusion/VINN——早期的跨任务数据汇集证据 |
| 2024-02 | **UMI**(Chi、Song 等) | 手持夹爪 + GoPro + 鱼眼 + 镜面:无需机器人即可在真实环境采集人类数据;策略可迁移到机械臂完成动态和双臂任务 |
| 2024 | **ALOHA 2**(DeepMind) | 更皮实、更强的 ALOHA 平台(附 MuJoCo 仿真模型);成为 DeepMind 的双臂数据采集主力 |
| 2024-10 | **ALOHA Unleashed**(DeepMind) | "简单配方"——5 个任务 >26,000 条遥操作演示 + 扩散策略——掌握挂衬衫、系鞋带、齿轮插装;证明灵巧性受限于数据而非算法 |
| 2024-10 | **π0**(Physical Intelligence) | 流匹配 VLA;将模仿学习脉络吸收进基础模型;跨本体完成叠衣服、收拾餐桌 |
| 2025 | **UMI 衍生系统** | FastUMI(FastUMI-100K:>10 万条 episode、54 个任务)、DexUMI(CoRL 2025:手部外骨骼 + 机器手图像修补 → 在 XHand/Inspire 上平均成功率 86%)、ActiveUMI、UMI-on-Legs/Air |
| 2025-11 | **π*0.6 / RECAP**(Physical Intelligence) | 在模仿学习之上叠加真实世界经验强化学习:优势条件化策略 + 遥操作纠正;最难任务上吞吐量约 2 倍、失败率约减半 |

- 关键概念性进展:(1) 动作分块在平滑的富接触控制上优于单步预测;(2) 生成式策略(扩散/流)能刻画多模态的人类演示;(3) 数据采集接口(ALOHA 遥操作、UMI 手持设备、外骨骼)与架构同等重要;(4) 人类视频和手持设备让数据采集与昂贵的机器人解耦。
- 这一脉络汇入了 VLA:Gemini Robotics(2025-03,基于 Gemini 2.0)在 ALOHA 2 平台上完成折纸和 Ziploc 袋封装,并迁移到 Franka 双臂和 Apptronik Apollo;Figure 的 Helix 用同一主干同时跑物流和叠衣服。见 [VLA 模型](vla-models.md)、[关键人物](key-people.md)(Zhao、Chi、Song、Finn、Levine、Hausman)。
- 强化学习的回归:OpenAI 的 Dactyl(2018–19,sim-to-real 手内立方体强化学习)之后,真实世界强化学习一度沉寂;2025 年重新兴起——π*0.6/RECAP、Honda 的灵巧性强化学习专利申请(2025-02),以及混合专家手内重定向(DexReMoE)加触觉 sim-to-real 蒸馏(PTLD,2026)(各为单一来源)。

## 双臂系统

- 两条手臂是家务任务的实际下限:抚平布料、组装纸盒、"工具 + 工件"类任务都需要一只稳定手加一只操作手(研究方向:VoxAct-B、EquiBim、从视频单样本学习双臂操作)。
- 研究平台:ALOHA 2(ViperX 臂)、双臂 Franka FR3、UR5e 对(π0)、SO-ARM101(低成本,用于 LeHome 2026 挑战赛)。
- 人形机器人里程碑(截至 2026-07):Figure Helix 用多指灵巧手自主完成叠衣服(2025-08,首个声称端到端神经网络驱动的人形叠衣);Figure 的 Helix 02 完成约 4 分钟、61 个动作的洗碗机装卸,无重置、无遥操作,整合了行走 + 操作(未剪辑视频发布于 2026-01-28;Figure 声称这是迄今最长时程的自主人形任务);Apptronik Apollo 运行 Gemini Robotics 检查点。见[人形机器人](humanoid-robots.md)。
- π*0.6 部署(2025-11,公司口径):意式浓缩咖啡机操作,从早 5:30 运行到晚 11:30;在新环境中折叠 50 件不同的新衣物;在工厂环境中组装并贴标 59 个巧克力盒。
- 数据备注:双臂 + 多指数据是[数据金字塔](data.md)中最稀缺的一层;遥操作成本随自由度增长,这正是 UMI 式手持设备和外骨骼(DexUMI、DexTele)大量涌现的原因。

## 能力前沿与基准(截至 2026-07)

**已展示(至少在一个实验室/公司环境中可靠实现):**
- 从篮子里折叠衣物——π0.6 开箱即用(无任务微调),成功率约 60%+,约 19 次成功/小时(模型卡,2025-11);Helix 完成毛巾/衣物折叠。
- 收拾餐桌、装碗碟、挂衬衫、系鞋带、齿轮插装、组装纸盒(π0.6 开箱即用的纸盒组装成功率仅约 20%——难任务仍需微调)。
- 实验室环境中对多种刚性物体的手内重定向(强化学习,如 DexReMoE 混合专家,sim-to-real)。
- 强化学习微调的 VLA 实现连续数小时无人值守运行(π*0.6 意式浓缩咖啡),吞吐量远低于人类基线。

**基准及其问题:**

| 基准 | 类型 | 状态 |
|---|---|---|
| LIBERO(+ LIBERO-Plus) | 仿真,4 个泛化套件 | 事实上的 VLA 标准;接近饱和,LIBERO-Plus 加入 7 因子扰动以恢复区分度 |
| SIMPLER | 真实机器人策略的 real-to-sim 评测 | RT/π 系策略对比的标准 |
| RobotArena ∞ / RoboArena | Real-to-sim + 人类偏好 | 迄今规模最大的跨实验室 VLA 对比(2025–26) |
| ICRA Cloth Competition(2024) | 真实环境,布料展开抓取点选择 | 可形变物体参考数据集 |
| LeHome Challenge(2026) | 仿真,SO-ARM101 上的双臂叠衣 | 社区可形变物体基准 |

- 评测危机:真实世界结果大多是公司自报的演示,配置互不可比;单次尝试成功率掩盖了速度和恢复能力,因此指标正转向吞吐量(每小时成功次数)和长时自主运行。独立复现(如宾夕法尼亚大学的 "π0 in the wild" 研究)发现通用策略在训练分布之外明显更弱。

## 仍然困难的问题及原因

- **任意物体的手内操作**:换握、指间步态(finger-gaiting)和工具重定向在训练物体集之外泛化很差;接触仿真误差和触觉数据稀缺是硬约束。
- **有力且精细的工具使用**:高力量与高精度耦合的任务(削皮、切割、紧固、规模化的连接器插装)不在当前演示范围内。
- **超越平面折叠的可形变物体**:线缆布线、穿衣辅助、食物操作——高自由度可形变物体的状态估计仍未解决。
- **可靠性,而非存在性证明**:前沿演示的单次成功率为 60–90%,速度比人类慢 3–10 倍;工业落地需要 99%+ 并具备优雅的失败恢复。基于经验的强化学习(RECAP)是当前最好的抓手。
- **触觉与策略的整合**:传感器已经存在(Digit 360、凝胶皮肤),但前沿 VLA 仍只用视觉 + 本体感觉;截至 2026-07,尚无大规模带触觉标注的数据集。
- **向灵巧手的跨本体迁移**:以夹爪为中心的数据集(Open X-Embodiment、DROID)无法迁移到 20 自由度灵巧手;外骨骼/图像修补管线(DexUMI)是早期的变通方案。
- **灵巧手硬件经济学**:高自由度灵巧手仍是人形机器人中最不耐用、最昂贵的子系统;中国的规模化制造(2025–26)正在压低成本,但持续接触下的耐久性(>30 万次循环的宣称)基本未经独立审计(未证实)。见[硬件](hardware.md)、[投资](investment.md)。
- **接触的模拟到现实**:[世界模型(world model)](world-models.md)和 GPU 仿真器对摩擦、柔顺性和可形变物体的建模仍有偏差;2023 年以来大多数操作进展来自真实数据而非仿真——与运动控制正好相反。

## 来源

- https://arxiv.org/abs/2410.13126 — ALOHA Unleashed:规模 + 扩散配方,5 个灵巧双臂任务(DeepMind,2024-10)。
- https://mobile-aloha.github.io/resources/mobile-aloha.pdf — Mobile ALOHA 论文:全身遥操作,对 ACT/Diffusion/VINN 的联合训练增益。
- https://arxiv.org/abs/2402.10329 — Universal Manipulation Interface(UMI):真实环境中的手持夹爪数据采集。
- https://dex-umi.github.io/ — DexUMI(CoRL 2025):手部外骨骼 + 图像修补,在 XHand/Inspire 灵巧手上平均成功率 86%。
- https://arxiv.org/html/2606.04708 — VISTA:面向 VLA 训练的 UMI 数据适配;综述了 FastUMI-100K(>10 万条 episode、54 个任务)及 UMI 变体生态。
- https://website.pi-asset.com/pi06star/PI06_model_card.pdf — π0.6 模型卡(2025-11-17):架构、开箱即用的叠衣/纸盒组装结果、吞吐量指标。
- https://www.pi.website/blog/pistar06 和 https://arxiv.org/abs/2511.14759 — π*0.6/RECAP:基于经验的强化学习,咖啡/叠衣/纸盒工厂运行,2 倍吞吐量宣称。
- https://deepmind.google/blog/gemini-robotics-brings-ai-into-the-physical-world/ — Gemini Robotics(2025-03):折纸级灵巧性,ALOHA 2 → Apollo 迁移。
- https://www.figure.ai/news/helix-learns-to-fold-laundry — Figure Helix 用多指灵巧手叠衣服(2025-08-12)。
- https://www.figure.ai/news/helix-loads-the-dishwasher — Figure 官方帖子:Helix 02 洗碗机装卸,61 个动作,无重置(2026-01)。
- https://the-decoder.com/figure-ai-shows-robot-that-really-puts-its-hip-into-dishwasher-duty/ — 独立报道,证实约 4 分钟未剪辑的 Helix 02 洗碗机视频。
- https://www.basenor.com/blogs/news/tesla-optimus-gen-3-hands-22-dof-50-actuators-explained — Optimus Gen-3 手:22 自由度 + 3 腕自由度,腱驱动,指尖触觉(二手来源)。
- https://www.teslarati.com/tesla-optimus-v3-hand-arm-details-revealed-new-patents/ — Optimus V3 手/臂专利:前臂内置执行器,腱驱动(二手来源)。
- https://vedder.io/misc/the_case_against_human_hands.html — 灵巧手 vs 夹爪之争中"夹爪足够"一方的论证。
- https://www.therobotreport.com/tesollo-unveils-dexterous-robot-hand-for-humanoids/ — TESOLLO DG-5F 20 自由度灵巧手。
- https://www.prnewswire.com/news-releases/dexrobot-unveils-full-dexterous-hand-series-and-new-dextele-teleoperation-system-at-automate-2026-302808579.html — DexHand021 Pro 规格(22 自由度、50 N、30 万次循环)与 DexTele 遥操作(公司 PR)。
- https://autonews.gasgoo.com/articles/news/from-prototypes-to-production-dexterous-hands-kick-off-a-mass-production-race-2016425582734970881 — 2025 年中国灵巧手出货量(按每台机器人两只手推算 >3 万只;Inspire 约 1 万只 vs 2024 年约 2 千只;LinkerBot 2026 年目标;文中 Unitree 数字为人形机器人整机而非灵巧手)。
- https://www.unitree.com/mobile/Dex5-1/ — Unitree Dex5-1:20 自由度(16 主动),94 个触觉点。
- https://www.businesswire.com/news/home/20241031980322/en/GelSight-and-Meta-AI-Introduce-Digit-360-Tactile-Sensor — Digit 360:约 830 万触觉单元、约 1 mN 灵敏度、18+ 种感知特性。
- https://finance.yahoo.com/news/fingertips-full-body-coverage-ensuring-090900110.html — Tacta 在 CES 2026 的全手触觉覆盖(公司口径)。
- https://github.com/linchangyi1/Awesome-Touch — 触觉传感器与触觉-策略论文的精选索引(PolyTouch、TLA、AnyTouch、VLA-Touch)。
- https://arxiv.org/pdf/2508.01695 — DexReMoE:面向通用手内重定向的混合专家强化学习。
- https://arxiv.org/abs/1808.00177 — OpenAI Dactyl:强化学习手内立方体重定向的源头。
- https://openreview.net/attachment?id=OutljIofvS&name=pdf — RobotArena ∞:可扩展的 real-to-sim VLA 基准评测。
- https://arxiv.org/pdf/2508.16749 — ICRA 2024 布料竞赛:布料展开的数据集/基准。
- https://arxiv.org/pdf/2606.27163 — LeHome Challenge 2026:SO-ARM101 上的双臂叠衣基准。
- https://penn-pal-lab.github.io/Pi0-Experiment-in-the-Wild/ — π0 泛化差距的独立评测。
