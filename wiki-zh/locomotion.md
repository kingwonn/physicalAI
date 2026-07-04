---
title: 足式运动
slug: locomotion
updated: 2026-07-04
confidence: verified
lang: zh
source: ../wiki/locomotion.md
---
> 足式运动(legged locomotion)在大约 2018 到 2022 年间经历了一次范式转变:从基于模型的控制(ZMP 行走、全身 MPC)转向在大规模并行 GPU 仿真中训练、零样本迁移到硬件的强化学习(RL)策略。如今的标准配方——PPO 加数千个并行环境(Isaac Gym/Lab 一脉)、地形课程、域随机化(domain randomization)、以及特权观测的师生蒸馏(teacher–student distillation)——先让四足机器人在野外变得鲁棒(ANYmal 登山、DARPA SubT),再变得敏捷(2023–24 基于第一视角视觉的跑酷),到 2024–26 年更把人形机器人从实验室行走推进到跑酷、10 m/s 冲刺和通用全身运动跟踪。截至 2026-07,几乎所有认真做四足和人形的项目(包括 Boston Dynamics)都在用学习式运动控制;前沿已转向感知型全身敏捷性,以及把运动与[操作](manipulation.md)统一起来。

## 为什么运动控制是 Physical AI 中"基本解决"的那一层

- 运动控制是第一个让模拟到现实(sim2real)强化学习成为*默认*工业方法而非研究猎奇的机器人能力——比[操作](manipulation.md)早了好几年;后者的富接触动力学和感知多样性更难仿真。
- 它率先被攻克的原因:动作空间低维(12–29 个关节)、动力学以刚体物理+接触为主(可仿真)、奖励可自监督(速度跟踪)、仿真中重置成本极低。
- 运动策略是现代[人形机器人](humanoid-robots.md)技术栈中位于[视觉-语言-动作模型(VLA)](vla-models.md)和全身控制器之下的"脊髓"层:高层模型输出速度或姿态目标,学习得到的低层策略以约 50 Hz 保持机器人直立。
- 领域整体时间线见[历史](history.md),当前总体快照见[技术现状](state-of-the-art.md)。

## 时代 1 —— 基于模型的控制:从 ZMP 到 MPC(1968–约 2019)

- **ZMP(零力矩点)**:由 Miomir Vukobratović 提出的判据(1968–72)。稳定性 = 让净惯性+重力力矩为零的点保持在支撑多边形内。它催生了 Honda P2(1996)和 **ASIMO**(2000,首秀行走速度 1.6 km/h),以及一整代平地、准静态的行走机器人。
- **预观控制 / 捕获点**:Kajita 的 ZMP 预观控制(2003)和捕获点 / 发散运动分量方法,使行走从准静态变为动态。
- **Raibert 动力学**:MIT Leg Lab 的弹跳机器人(1980 年代)证明可用简单启发式实现动态平衡——这是 Boston Dynamics 的思想源头(BigDog 2005、Spot、液压 Atlas)。
- **凸 MPC 时代(约 2013–2021)**:全身 MPC + 轨迹优化支撑了 DRC 时代的人形机器人以及 MIT Cheetah 3 / Mini Cheetah 的步态;Boston Dynamics 著名的 Atlas 跑酷和后空翻视频(2017–2021)是基于模型的(离线优化的行为库 + 在线 MPC),*不是* RL。
- 后来被 RL 利用的结构性弱点:手工设计的接触时序、对未建模地形(泥地、植被、瓦砾)的脆弱性、每个行为都需要大量工程、以及大扰动下恢复能力差。

## 时代 2 —— RL 转向(2018–2021)

- **Hwangbo 等,Science Robotics 2019**(ETH Zurich):在 RaiSim 中训练的 RL 策略配合学习得到的**执行器网络**(建模真实串联弹性执行器动力学),零样本迁移到 ANYmal——比此前基于模型的控制器跑得更快,还能摔倒恢复。确立了 sim2real 差距在很大程度上是*执行器/接触建模*问题。
- **Lee 等,Science Robotics 2020**("Learning quadrupedal locomotion over challenging terrain"):盲走(仅本体感受)的 ANYmal 控制器;将**特权师生**范式引入运动控制——教师在仿真中用地形/接触真值训练,学生蒸馏为只用可部署传感器历史的策略。在训练中从未见过的泥地、雪地、瓦砾、植被上实现零样本鲁棒性。
- **RMA(Kumar、Fu、Pathak、Malik —— RSS 2021)**:快速运动自适应;自适应模块从本体感受历史在线估计环境隐变量——低成本四足(Unitree A1)版的师生方案。
- **Siekmann 等 2021**(Oregon State):通过 sim2real RL 实现 Cassie 盲走上下楼梯——同一工具箱产出的第一个有说服力的双足鲁棒性结果。
- **DARPA SubT 决赛 2021**:CERBERUS 队(由 University of Nevada Reno / NTNU 领衔的联合体,ETH Zurich 提供机器人和控制器)使用四台运行学习式运动控制器的 ANYmal C 四足机器人在矿井/洞穴/城市废墟中夺冠——RL 运动控制的首次高风险实地验证。

## 时代 3 —— 大规模并行仿真(2021–)

- **Isaac Gym(NVIDIA,2021,arXiv:2108.10470)**:端到端 GPU 物理 + RL,单块 GPU 上跑数千个环境,消除了 CPU 仿真瓶颈。
- **"Learning to Walk in Minutes"(Rudin 等,CoRL 2021,arXiv:2109.11978)**:配方论文。4096 个并行 ANYmal 环境、PPO、游戏式地形课程;单 GPU 上平地策略**不到 4 分钟**训成,复杂地形约 20 分钟——比此前工作快几个数量级。开源为 `legged_gym` + `rsl_rl`,成为事实上的社区标准(扩展到 A1/Go1/Go2、G1、H1、Cassie、Digit、Spot、ANYmal-B/C/D 等;RSL-RL 库论文 arXiv:2509.10771,2025)。
- 截至 2026-07 的仿真器格局(详见[仿真](simulation.md)):

| 技术栈 | 出处 | 备注 |
|---|---|---|
| Isaac Gym → Orbit → **Isaac Lab** | NVIDIA | 运动 RL 的主导一脉;Isaac Lab 是持续维护的继任者(框架论文 arXiv:2511.04831) |
| **MuJoCo MJX / MuJoCo Playground** | Google DeepMind | GPU 版 MuJoCo;Playground(2025)在单 GPU 上数分钟内训出运动策略 |
| **Genesis** | 开源联合体 | 生成式/通用物理引擎,2024 年 12 月 |
| **Newton** | NVIDIA + Google DeepMind + Disney Research | 开源,基于 Warp+OpenUSD,2025-09 起进入 beta,Linux Foundation 治理;与 Isaac Lab 和 MuJoCo Playground 互操作;NVIDIA 称 MuJoCo-Warp 在运动负载上比 MJX 快最高约 152 倍(RTX 4090,厂商基准,未证实) |

## 标准训练配方(截至 2026)

社区共识流水线,自约 2022 年起保持稳定并逐步升级:

1. **算法**:PPO,约 4096 个并行环境,单 GPU 上数分钟到数小时的墙钟时间。
2. **观测**:本体感受历史(关节位置/速度、IMU、上一帧动作);感知型策略可选加高度图扫描或深度。
3. **动作**:输出目标关节位置,交给 50 Hz 的 PD 控制器(力矩策略存在,但迁移更难)。
4. **奖励**:速度指令跟踪 + 存活,减去惩罚项(力矩、动作变化率、打滑、姿态);可选风格项。
5. **地形课程**:程序化生成的坡道/楼梯/沟壑/瓦砾,按每台机器人的成功率提升难度("游戏式课程")。
6. **域随机化**:摩擦、连杆质量、电机强度/延迟、推搡扰动、传感器噪声——sim2real 的核心工具。
7. **执行器建模**:学习式执行器网络或辨识出的电机模型,弥合剩余的动力学差距。
8. **师生 / 非对称 actor-critic**:教师(或 critic)可见特权仿真状态(真实高度、接触、摩擦);可部署的学生通过 DAgger 式监督在观测历史上蒸馏,或由 scandots 教师蒸馏出深度视觉学生。
9. **需要自然度时加风格先验**:对抗性运动先验(AMP,Peng 等 2021)或来自人类/动物动作捕捉的运动跟踪目标。
10. **部署**:ONNX/TensorRT 策略跑在嵌入式计算上,置于安全层之下;零样本,标准配方不做机上微调。

仍需工程手段处理的失败模式:奖励欺骗(脚部打滑、不自然步态)、仿真未建模的柔性(软地面需专门的颗粒介质模型)、以及视觉策略的相机延迟不匹配。

## 跑酷与敏捷性里程碑

| 年份 | 系统 | 结果 |
|---|---|---|
| 2021 | Atlas 跑酷(Boston Dynamics) | 基于模型的行为库 + MPC;非学习式 |
| 2022 | Mini Cheetah 快速奔跑(MIT,Margolis 等,RSS 2022) | RL 控制器在草地、冰面、碎石上持续冲刺至 3.9 m/s |
| 2022-09 | **Cassie 100 米吉尼斯纪录**(Oregon State) | 24.73 秒,RL 控制器,站立式起止 |
| 2023 | Robot Parkour Learning(Zhuang 等,CoRL 2023)+ **Extreme Parkour**(CMU,arXiv:2309.14341) | 低成本四足、单深度相机、端到端:跳远 2 倍体长、跳高 2 倍体高、倒立行走 |
| 2024-03 | **ANYmal Parkour**(Hoeller 等,Science Robotics) | 感知 + 技能库 + 导航模块;以最高 2 m/s 通过障碍赛道,跳跃、攀爬、匍匐 |
| 2024 | **Humanoid Parkour Learning**(Zhuang 等,CoRL 2024) | 端到端视觉全身策略,无运动先验:跳上 0.42 m 平台、跨越 0.8 m 沟壑、户外奔跑 1.8 m/s |
| 2024-04 | DeepMind 1v1 机器人足球(Science Robotics) | 在迷你 OP3 人形上做 RL:踢球、摔倒再爬起、动态对抗 |
| 2025 | ASAP(LeCAR Lab,RSS 2025) | 现实到仿真的 delta-action 模型对齐,用于 G1 敏捷全身技能 |
| 2026-01 | **Deep Whole-Body Parkour**(Zhuang 等,arXiv:2601.07701) | 将外部感知融入全身运动跟踪:单一策略在不平地形上完成撑越和前滚翻 |

## 双足与人形:从 Cassie 到全身控制

- **Cassie/Digit 一脉**:Xie 等(2019)首次在 Cassie 上实现 RL 行走;2021 盲走楼梯;2022 打破 100 米吉尼斯纪录。Agility 的 Digit 在仓储部署中使用学习式运动控制(见[人形机器人](humanoid-robots.md))。
- **Radosavovic 等,Science Robotics 2024**("Real-world humanoid locomotion with reinforcement learning",Berkeley):在仿真中训练的因果 Transformer 策略,在 Digit 上零样本户外行走——证明运动策略可以用与 [VLA](vla-models.md) 相同的序列模型机制来扩展。
- **全身运动跟踪成为人形领域的主导框架(2024–2026)**:不再训练"行走控制器",而是训练一个策略去跟踪重定向后的人类动作(行走只是特例)。脉络:H2O/OmniH2O 与 Expressive Whole-Body Control(2024)→ **ASAP**(RSS 2025;通过学习的 delta-action 模型把仿真物理对齐到现实)→ **HOVER**(NVIDIA,ICRA 2025;单个神经控制器多路复用指令模式)→ BeyondMimic / GMT / UniTracker(2025)→ **SONIC**(NVIDIA,arXiv:2511.07820,2025-11;运动跟踪"超大规模化"——报告在 Unitree G1 上对 50 条多样真实轨迹达到 100% 成功率,实时机上运行)。
- **Unitree 的演示节奏**(见[中国格局](landscape-china.md)):H1 无液压站立后空翻(2024,宣称首例);G1 功夫/侧空翻演示贯穿 2025;2026-02 春晚节目——自主功夫、3 米蹦床空翻、7.5 圈 airflare、借墙后空翻——约 6.79 亿观众收看(Unitree 公关数字,未证实)。
- **速度纪录**(截至 2026-04):Unitree H1 于 2026-04-11 冲刺达 **10 m/s(约 22.4 mph;通过计时门时峰值 10.1 m/s)**,追平 **MirrorMe 的 "Bolt"** 在 2026-02-02 宣称的 10 m/s。MirrorMe Technology 是一家真实存在的上海初创公司(2024-05 成立,浙江大学系创业团队;此前造出四足机器人 **Black Panther II**——约 0.63 m、约 38 kg、弹簧储能膝关节——在电视直播中以 13.17 秒跑完 100 米,并在 MrBeast 视频中与奥运会 100 米冠军 Noah Lyles 赛跑,2025-11;它还持有宣称的四足峰值速度纪录:2025-11-26 公司稿件称 13.2 m/s,较一个月前的 10.3 m/s 提升,2025-12-25 的公司视频进一步把宣称推到 **13.4 m/s**——全部来自公司自供素材,无第三方计时,峰值数字仍未证实);Bolt 是身高 175 cm / 体重 75 kg 的人形机器人,其 10 m/s 是在一场**宣传性跑步机演示**中展示的(创始人在旁并排竞跑),*不是*户外跑道或独立计时。两项纪录均为公司自供素材的公司口径——被 CGTN、Interesting Engineering、CnEVPost 等媒体广泛转载,但无第三方计时(数字宣称仍未证实)。H1 自己此前的纪录是 3.3 m/s(2024-03)。提升归功于软件/控制,而非新硬件。
- **Boston Dynamics 也转向了**:与 Robotics & AI Institute 达成合作(2025-02,新闻稿),为电动 Atlas 共建 RL 训练流水线;RAI 的开源 Spot 流水线(Isaac Lab,ICRA 2025)通过分布匹配(Wasserstein/MMD + CMA-ES)调优仿真参数,零样本达到 **5.2 m/s——约为 Spot 默认最高速度的 3 倍**。第五代电动 Atlas(2026-07 发布)延续 sim+RL 流水线,硬件"简化一个数量级"(Forbes,截至 2026-07)。

## 野外鲁棒性

- **Miki 等,Science Robotics 2022**("robust perceptive locomotion in the wild"):基于注意力的循环网络融合本体感受与不确定高程图;ANYmal 徒步 Mount Etzel(2.2 km、120 m 爬升):31 分钟登顶,而人类路标估时约 35 分钟,零摔倒——野外鲁棒性的经典结果。
- 盲走策略(Lee 2020)能在从未仿真过的地形类别上存活:泥地、雪地、湍流水、密集植被——鲁棒性来自随机化动力学训练,而非地形真实感。
- 可变形/颗粒地形:在仿真中专门建模颗粒介质,把鲁棒性扩展到沙地和软地面(Choi 等,Science Robotics 2023)。
- 商业化验证:数千台 Spot 和 ANYmal 在工业巡检中运行学习式或混合控制器;Unitree 自报 2025 年出货人形机器人 5,500 台以上(IPO 招股书数字;Omdia 的独立统计约 4,200 台——差距源于"什么算人形"的口径之争),全部以 RL 运动控制为标准固件(截至 2026,见[投融资](investment.md)和[组织机构](organizations.md))。
- 领域综述:Ha、Lee、van de Panne、Xie、Yu、Khadiv——"Learning-based legged locomotion: state of the art and future perspectives"(IJRR 2025,arXiv:2406.01152);MDPI 系统性 DRL 运动控制综述(2025,覆盖 2018–2025 的 27 项研究)。

## 开放问题(截至 2026-07)

- **感知型全身通用性**:跑酷级敏捷性 + 运动跟踪 + 操作合入单一策略才刚出现(Deep Whole-Body Parkour,2026-01);尚无系统能同时处理任意地形 + 任意任务。
- **力矩级、感知硬件极限的策略**:多数策略仍架在 PD 位置控制之上;直接力矩策略迁移效果差。
- **长时程自主**:运动控制可在数分钟到数小时内保持鲁棒,但对 50+ kg 的人形机器人来说摔倒代价依然高昂;负载下的摔倒恢复与摔倒规避是活跃研究方向。
- **能量效率**:不含能量项的标准速度跟踪 RL 策略往往低效——表现为高频跺脚/打滑(Fu 等在消融实验中直接展示了这一点)——但把能量写进奖励的学习式策略能*击败*基于模型的基线。Hwangbo 等 2019 报告学习式 ANYmal 控制器在匹配速度下机械功率降低约 20%(78.1 vs 97.3 W)、力矩降低 23–36%;Fu 等(CoRL 2021)报告能量最小化的 A1 策略在行走时比凸 MPC 节能约 50%(每米能耗 30.7 vs 87.0 J/m;trot 步态 41.2 vs 77.2;bounce 步态 90.7 vs 93.9)。运输成本(cost of transport)的报告口径仍不统一——各论文的单位和基线各异(有的报 J/m,有的报 W,有的报无量纲 CoT),跨系统比较困难。一个罕见的无量纲数据点:Wang 等(FITEE 2025,26(9):1679–1691)在小型 12 自由度四足(Jueying Lite3、Unitree A1)上训练 walk/trot/gallop 策略加学习式步态选择器,报告其多步态策略在可行速度指令范围内平均 **CoT = 0.4306**——优于 FSM 步态切换基线(0.4531)和所有单步态策略(0.45–0.72),同时在分形、坡面、离散地形上保持 100% 通过率(仿真评估;策略面向 sim2real 迁移设计)。
- **基准不透明**:敏捷性宣称由公司视频驱动(速度纪录、晚会演示),缺乏标准化评测——见[开放问题](open-problems.md)。

## 来源

- https://arxiv.org/abs/2109.11978 — Rudin 等,"Learning to Walk in Minutes":4096 环境,平地 <4 分钟 / 复杂地形约 20 分钟,地形课程,legged_gym。
- https://ar5iv.labs.arxiv.org/html/2108.10470 — Isaac Gym 论文:基于 GPU 的大规模并行物理仿真用于 RL。
- https://www.science.org/doi/10.1126/scirobotics.abc5986 — Lee 等 2020:盲走四足运动、特权师生方案、泥地/雪地/瓦砾零样本鲁棒性。
- https://www.science.org/doi/10.1126/scirobotics.abk2822 — Miki 等 2022:野外感知型运动控制;Mount Etzel 徒步数据。
- https://ethz.ch/en/news-and-events/eth-news/news/2022/01/how-robots-learn-to-hike.html — ETH 新闻:Etzel 徒步 31 分钟登顶 vs 人类估时 35 分钟。
- https://www.science.org/doi/10.1126/scirobotics.adi7566 — Hoeller 等,ANYmal Parkour(Science Robotics 2024):感知/运动/导航模块,最高 2 m/s。
- https://arxiv.org/pdf/2309.14341 — Cheng 等,Extreme Parkour with Legged Robots:2 倍体长跳远、2 倍体高攀爬、倒立、单深度相机。
- https://humanoid4parkour.github.io/ — Zhuang 等,Humanoid Parkour Learning(CoRL 2024):0.42 m 平台、0.8 m 沟壑、1.8 m/s、无运动先验。
- https://arxiv.org/abs/2601.07701 — Deep Whole-Body Parkour(2026-01):感知型通用运动控制,撑越与前滚翻。
- https://news.oregonstate.edu/news/bipedal-robot-developed-oregon-state-achieves-guinness-world-record-100-meters — Cassie 100 米吉尼斯纪录,24.73 秒(2022)。
- https://www.guinnessworldrecords.com/world-records/629600-fastest-100-m-by-a-bipedal-robot — 吉尼斯官方条目:双足机器人最快 100 米。
- https://arxiv.org/abs/2205.02824 — Margolis 等,Rapid Locomotion via RL(RSS 2022):Mini Cheetah 持续速度最高 3.9 m/s。
- https://global.honda/en/newsroom/news/2000/c001120b-eng.html — Honda ASIMO 首发公告(2000):行走速度 1.6 km/h。
- https://www.science.org/doi/full/10.1126/scirobotics.adi9579 — Radosavovic 等:Digit 上的 Transformer RL 人形运动控制(Science Robotics 2024)。
- https://github.com/LeCAR-Lab/ASAP — ASAP(RSS 2025):通过 delta-action 模型对齐仿真/现实物理,Unitree G1。
- https://arxiv.org/pdf/2511.07820 — SONIC(NVIDIA,2025):大规模人形运动跟踪,50 条真实 G1 轨迹 100% 成功。
- https://rai-inst.com/resources/press-release/boston-dynamics-atlas-partnership/ — BD 与 RAI Institute 就 Atlas 的 RL 合作(2025-02)。
- https://rai-inst.com/resources/papers/high-performance-reinforcement-learning-on-spot/ — RAI Institute:Spot RL 达 5.2 m/s,用分布度量优化仿真参数(ICRA 2025)。
- https://www.humanoidsdaily.com/news/unitree-h1-reclaims-speed-record-with-blistering-10-m-s-sprint — Unitree H1 10 m/s 冲刺(2026-04-11),过计时门峰值 10.1 m/s;此前纪录 3.3 m/s;MirrorMe Bolt 背景。
- https://cnevpost.com/2026/02/03/mirrorme-unveils-worlds-fastest-humanoid-robot-bolt/ — MirrorMe Technology(上海,2024-05 成立,浙江大学团队);Bolt 于 2026-02-02/03 发布,175 cm / 75 kg,公司素材中达 10 m/s;Black Panther II 四足背景。
- https://interestingengineering.com/ai-robotics/fastest-humanoid-robot-bolt-unveiled — 独立报道确认 Bolt 的 10 m/s 是宣传性跑步机演示(创始人并排竞跑),公司自供素材,无第三方计时。
- https://markets.financialcontent.com/wral/article/getnews-2025-11-26-black-panther-ii-the-worlds-fastest-robot-dog-racing-a-world-champion-in-mrbeasts-latest-video-from-chinas-mirrorme-technology — MirrorMe 新闻稿(2025-11-26):Black Panther II 峰值 13.2 m/s(30 天内从 10.3 m/s 提升),MrBeast 视频中与 Noah Lyles 竞速("惜败");宣传性来源。
- https://www.aparobot.com/robots/black-panther-ii — Black Panther II 规格页(厂商核实数据):100 米 13.17 秒;演示 9.7 m/s,内部测试据报 10–13 m/s。
- https://x.com/XRoboHub/status/2004194422817542449 — 对 MirrorMe 2025-12-25 公司视频宣称 13.4 m/s 峰值的转述(仅公司素材,未证实)。
- https://doi.org/10.1631/FITEE.2401070 — Wang 等,"Efficient learning of robust multigait quadruped locomotion for minimizing the cost of transport"(FITEE 2025,26(9):1679–1691):CoTavg 0.4306 vs FSM 0.4531 与单步态 0.45–0.72(表 6);Jueying Lite3 + Unitree A1;Isaac Gym 训练。
- https://arxiv.org/abs/1901.08652 — Hwangbo 等,"Learning Agile and Dynamic Motor Skills"(Science Robotics 2019):学习式 ANYmal 力矩(8.23 vs 11.7 N·m)和机械功率(78.1 vs 97.3 W)低于基于模型的控制器,按速度分档力矩低 23–36%,ANYmal 速度纪录提升 25%。
- https://proceedings.mlr.press/v164/fu22a/fu22a.pdf — Fu 等,"Minimizing Energy Consumption Leads to the Emergence of Gaits"(CoRL 2021):A1 每米能耗对比凸 MPC(表 2),行走节能约 50%;消融实验显示未做能量优化的策略高频跺脚。
- https://www.prnewswire.com/news-releases/kung-fu-meets-spring--unitree-spring-festival-gala-robots-present-cyber-real-kung-fu-in-the-year-of-the-horse-302689291.html — Unitree 2026 春晚演示宣称(airflare、蹦床空翻、收视数据)。
- https://developer.nvidia.com/blog/announcing-newton-an-open-source-physics-engine-for-robotics-simulation/ — Newton 物理引擎:NVIDIA+DeepMind+Disney,Warp/OpenUSD,与 Isaac Lab、MuJoCo Playground 互操作。
- https://www.linuxfoundation.org/press/linux-foundation-announces-contribution-of-newton-by-disney-research-google-deepmind-and-nvidia-to-accelerate-open-robot-learning — Linux Foundation 新闻稿(2025-09-29):Newton 捐赠、beta 状态、厂商中立治理。
- https://spectrum.ieee.org/ai-institute — IEEE Spectrum:独立确认 RAI 的 RL 使 Spot 奔跑速度提升三倍(1.7 到 5.2 m/s)。
- https://arxiv.org/abs/2207.04914 — CERBERUS 队 SubT 技术综述:UNR/NTNU 领衔的联合体,决赛使用四台 ANYmal C。
- https://arxiv.org/pdf/2511.04831 — Isaac Lab 框架论文(2025):GPU 加速多模态机器人学习;legged_gym 一脉的形态覆盖。
- https://arxiv.org/abs/2406.01152 — Ha 等,学习式足式运动综述(IJRR 2025):领域现状与展望。
- https://www.mdpi.com/2410-390X/10/1/8 — 系统性 DRL 足式运动综述(2025):27 项研究,域随机化/奖励塑形结论。
- https://arxiv.org/html/2509.10771v1 — RSL-RL 库论文(2025):运动控制研究的标准 PPO 工具。
- https://www.forbes.com/sites/johnkoetsier/2026/07/02/boston-dynamics-new-atlas-humanoid-robot-order-of-magnitude-simpler/ — 第五代电动 Atlas 简化设计(2026-07)。
- https://autonews.gasgoo.com/articles/market-industry/annual-champion-changes-hands-unitree-announces-over-5500-humanoid-robot-shipments-2014711162140991489 — Unitree 招股书自报 2025 年出货 5,500+ 人形 vs Omdia 独立统计约 4,200;机器人分类口径之争。
