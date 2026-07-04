---
title: Physical AI 发展史
slug: history
updated: 2026-07-03
confidence: verified
lang: zh
source: ../wiki/history.md
---
> Physical AI(物理 AI)——通过机器人在物理世界中感知、推理和行动的 AI——经历了四个大的时代:(1)经典时代(1950s–2011),以手工设计的工业机械臂和符号规划研究机器人为代表,如 Unimate 和 Shakey;(2)深度学习/深度强化学习时代(2012–2021),学习得到的策略、模拟到现实(sim2real)迁移和腿足机器人的突破取代了手工编码的控制,但仍然狭窄且缺乏数据;(3)基础模型转折(2022–2023),Google 的 RT-1/RT-2 和 Open X-Embodiment 项目把"规模 + transformer + 网络知识"的 LLM 配方引入机器人领域;以及(4)当前的机器人基础模型与人形机器人浪潮(2024–2026),其标志是通用视觉-语言-动作模型(VLA)(π0、Helix、Gemini Robotics、GR00T)、创纪录的资本(Figure 估值 $39B、Physical Intelligence 估值 $5.6B、据 Dealroom 2025 年约 $26.5B 流入机器人初创公司)、中国的人形机器人量产,以及 NVIDIA 在 CES 2026 宣告"物理 AI 的 ChatGPT 时刻"已经到来。

## 关键拐点时间线

| 年份 | 里程碑 | 为何是拐点 |
|---|---|---|
| 1954/1961 | Devol 申请可编程机械臂专利(1954);第一台 **Unimate** 在 GM 安装(1961) | 工业机器人诞生;机器人成为一个产业 |
| 1966–72 | **Shakey**(SRI International) | 第一台能对自身行动进行推理的移动机器人;A*、STRIPS、感知-规划-行动范式的发源地 |
| 1986 | Brooks 的**包容式架构(subsumption architecture)**;Honda 启动人形机器人研发 | 与符号 AI 对立的"具身优先"范式;通往 ASIMO 之路 |
| 2000 | Honda **ASIMO** | 人形机器人作为工程化旗舰演示,而非产品 |
| 2002 | iRobot **Roomba** | 第一款大众消费级机器人(销量数千万台) |
| 2004–07 | **DARPA Grand/Urban Challenges**(2005:Stanley;2007:Boss) | 播下自动驾驶产业及其人才谱系的种子 |
| 2005 | Boston Dynamics **BigDog** | 动态腿足运动进入公众视野 |
| 2012 | AlexNet;Amazon 收购 **Kiva**(约 $775M);Rethink **Baxter** | 学习式感知到来;仓储机器人商业价值得到验证 |
| 2013–15 | DQN(2013/2015);**DARPA Robotics Challenge** 决赛(2015 年 6 月,KAIST 夺冠) | 深度强化学习时代开启;人形机器人的现实检验(Atlas 摔倒集锦) |
| 2016 | **AlphaGo**;Levine 等人的端到端抓取;Google "arm farm" | 深度强化学习达到超人水平;机器人学习被定义为数据问题 |
| 2017–18 | 域随机化;PPO;OpenAI **Dactyl**(2018 年 7 月) | 模拟到现实成为标准配方 |
| 2019–20 | ANYmal 强化学习控制器(Science Robotics 2019);Dactyl 还原魔方(2019 年 10 月);Spot 开售;Waymo 无人驾驶服务 | 学习在运动控制上击败经典控制;物理 AI 触达付费客户 |
| 2021 | OpenAI 解散机器人团队(7 月);Tesla 宣布 **Optimus**(8 月) | 按任务的强化学习被宣告数据匮乏;人形机器人的赌注下定 |
| 2022 | **SayCan**(4 月);ChatGPT(11 月);**RT-1**(12 月) | LLM 规划 + transformer 控制;机器人领域采纳 scaling 配方 |
| 2023 年 7 月 | **RT-2**,第一个被命名的 VLA | 网络知识 → 机器人动作;未见任务成功率约 62%,而 RT-1 约 32% |
| 2023 年 10 月 | **Open X-Embodiment / RT-X**(21 家机构,100 万+ 回合,22 种本体) | 跨本体数据汇聚被证明有效;整个领域的共享数据集时刻 |
| 2024 | Mobile ALOHA(1 月);电动 Atlas(4 月);OpenVLA(6 月);**π0**(10 月);Unitree G1 约 $16k(5 月);Project GR00T(3 月) | 机器人基础模型成为一个创业赛道;人形机器人硬件价格底线崩塌 |
| 2025 | Huang 推广"Physical AI"+ Cosmos(CES,1 月);**Helix**(2 月);**Gemini Robotics** 与 **GR00T N1**(3 月);π0.5(4 月);Figure Series C 估值 $39B(9 月);机器人初创融资创纪录约 $26.5B(Dealroom) | 各大实验室悉数发布 VLA;融资创纪录;工厂试点启动 |
| 2026 | CES:物理 AI 的 ChatGPT 时刻"已经到来";Unitree 科创板 IPO;Hyundai 承诺部署 25,000+ 台 Atlas;中国产量同比 +94%(TrendForce 预测) | 商业化部署之年;中国主导出货量 |

## 时代 1 —— 经典机器人学与符号具身 AI(1950s–2011)

- **1954/1961 —— Unimate,第一台工业机器人。** George Devol 于 1954 年 12 月提交"programmed article transfer"专利(1961 年授权);他与 Joseph Engelberger 共同创立了 Unimation,1961 年,重约 4,000 磅的 Unimate 机械臂开始在新泽西州 Ewing Township 的 General Motors 生产线上卸载滚烫的压铸件——由此催生的工业机器人产业,其保有量至今仍远超人形机器人。
- **1966–1972 —— Shakey(SRI)。** 第一台能对自身行动进行推理的移动机器人:电视摄像头 + 测距仪 + 轮式底盘,由运行 STRIPS 规划和 A\* 搜索(两者都是为该项目发明的)的远程计算机驱动。Shakey 确立了感知-规划-行动范式——同时也展示了它在受控环境之外的脆弱性。
- **1969–1978 —— Stanford Arm → PUMA**:Victor Scheinman 的电动、计算机控制机械臂谱系成为此后数十年工业操作臂的模板。
- **1973 —— WABOT-1(早稻田大学)**,通常被认为是第一台全尺寸拟人机器人——今天各人形机器人项目的深层根源。
- **1986 —— Rodney Brooks 的包容式架构**摒弃中心化世界模型,转而采用分层的反应式行为("世界就是它自己最好的模型")。Brooks 联合创立了 iRobot(1990),其 **Roomba**(2002)把机器人送进了数百万个家庭。同年,Honda 启动秘密双足项目,最终产出 **P2(1996)** 和 **ASIMO(2000)**——工程化而非学习式控制的奇迹。参见[关键人物](key-people.md)。
- **2004–2007 —— DARPA Grand Challenges**(2004:无人完赛;2005:Stanford 的 Stanley;2007 Urban Challenge:CMU 的 Boss)证明了自动驾驶的可行性;参赛校友组建了 Google 的自动驾驶项目(2009 年,后来的 Waymo)以及大半个自动驾驶行业——这是第一个吸引数十亿美元资本的物理 AI 领域。
- **2005 —— Boston Dynamics BigDog** 以及液压 **Atlas**(2013,为 DARPA Robotics Challenge 打造)用手工设计的基于模型的控制、不依赖深度学习,树立了动态运动控制的标杆。
- **2007–2010 —— ROS 与 Willow Garage PR2** 标准化了机器人软件基础设施,培养了一代机器人研究者。
- **2012 —— Amazon 收购 Kiva Systems(约 $775M)**——那个时代最清晰的信号:移动仓储机器人在商业上是真实的;Rethink Robotics 的 Baxter 让协作机械臂广为人知(但商业化失败)。
- 整个这一时代,自主性意味着工程化流水线:感知、状态估计、规划和控制是彼此独立的手工搭建模块。学习在已部署系统中几乎不发挥作用。

## 时代 2 —— 深度学习与深度强化学习进入机器人领域(2012–2021)

- **2012 —— AlexNet** 让学习式感知成为主流;机器人领域几乎立刻继承了深度视觉。
- **2015 年 6 月 —— DARPA Robotics Challenge 决赛**:KAIST 的 DRC-HUBO 赢得 $2M 奖金;机器人摔倒的花絮集锦成为当时人形机器人距离实用有多远的经典画面——也是评判 2024–2026 这波浪潮的有用基线。
- **2015–2016 —— DQN(Nature)、TRPO、AlphaGo**;Levine 等人展示了端到端视觉运动策略,Google 的 "arm farm" 并行采集抓取数据——这是"机器人学习本质上是数据问题"这一押注的早期版本。
- **2017 —— 域随机化**(Tobin 等)与 PPO 让**模拟到现实(sim2real)**成为该时代的核心方法论:在随机化的[模拟](simulation.md)中训练,零样本部署到硬件。
- **2018 年 7 月 —— OpenAI Dactyl**:一只 24 自由度的 Shadow Hand 完全在模拟中(PPO + 动力学随机化)学会手内立方体重定向,迁移到物理手上并涌现出类人的手指步态;**2019 年 10 月**,同一条技术线利用自动域随机化单手还原了魔方(约 10,000 年的模拟经验)。
- **2019–2020 —— 学习式腿足运动走向成熟**:Hwangbo 等(Science Robotics, 2019)在模拟中训练出超越基于模型控制的 ANYmal 控制器;Lee 等(2020)实现了盲视崎岖地形四足行走。强化学习成为[运动控制](locomotion.md)的默认方案——学习决定性击败经典控制的第一个子领域。Boston Dynamics 的 Spot 开始全面商业销售(2020);Waymo 在 Phoenix 开放完全无人驾驶的 robotaxi 服务(2020)。
- **2021 —— 这个时代的天花板显现。** OpenAI 解散其机器人团队(2021 年 7 月),理由是真实世界数据不足——这被广泛引用为"按任务的强化学习无法扩展到通用[操作](manipulation.md)"的标志。同年 8 月,Tesla 在 AI Day 上宣布 Optimus 人形机器人项目。
- 时代 2 的净结果:在狭窄范畴(运动控制、手内灵巧性)里看似超人的演示,但每个任务都需要自己的奖励函数、训练过程和工程投入。泛化是缺失的那味原料。

## 时代 3 —— 基础模型转折(2022–2023)

- **2022 年 4 月 —— SayCan(Google)** 用 LLM 规划机器人任务序列——第一个重要的"LLM 当机器人大脑"成果。**2022 年 5 月 —— DeepMind Gato** 展示了一个 transformer 横跨 Atari、图像描述和真实机器人堆叠。
- **2022 年 11 月 —— ChatGPT。** 对机器人领域的外溢效应是直接的:它验证了 scaling 配方,把人才和资本引向"机器人版 GPT",并奠定了此后每个主要实验室都在用的叙事框架("机器人基础模型"、"机器人的 ChatGPT 时刻")。
- **2022 年 12 月 —— RT-1(Google)**:在约 130,000 个真实回合、700+ 任务上训练的机器人 transformer;被广泛视为第一个 VLA 式的通用控制模型。
- **2023 年 7 月 —— RT-2(Google DeepMind)**:第一个被命名的视觉-语言-**动作**模型,通过联合微调经网络预训练的 VLM(PaLI-X / PaLM-E)以 token 形式输出机器人动作。在 6,000+ 次试验中,未见任务成功率相比 RT-1 大约翻倍(约 62% vs 约 32%)——[VLA 模型](vla-models.md)范式的奠基性成果。(5620 亿参数的具身多模态语言模型 PaLM-E 在 2023 年 3 月先于它发布。)
- **2023 年 10 月 —— Open X-Embodiment / RT-X**(arXiv 2310.08864;ICRA 2024):21 家机构汇聚来自 22 种机器人本体、527 项技能的 100 万+ 轨迹;RT-1-X 在合作方机器人上成功率提升约 50%,RT-2-X 在涌现技能上性能大约提升三倍——证明了**跨本体数据汇聚有效**,并成为后来开放[数据](data.md)项目的模板。
- **2023 —— 模仿学习复兴**:Stanford 的 ALOHA/ACT 让双臂遥操作(teleoperation)数据采集变得廉价(Mobile ALOHA,2024 年 1 月,约 $32k),扩散策略成为灵巧操作中主导的动作生成架构。

## 时代 4 —— 机器人基础模型与人形机器人浪潮(2024–2026)

### 2024:"机器人界 OpenAI"竞赛的创始之年
- **Figure AI**:$675M Series B,估值 $2.6B(2024 年 2 月),并与 OpenAI 合作;2024 年 1 月宣布 BMW Spartanburg 合作。(2025 年 2 月,Figure 全面转向自研模型,OpenAI 合作终止。)
- **NVIDIA** 在 GTC(2024 年 3 月)宣布 **Project GR00T** 与 Jetson Thor,将自己定位为物理 AI 的"卖铲人"([硬件](hardware.md))。
- **Physical Intelligence** 由 Hausman、Levine、Finn 等人创立(初始融资约 $70M);2024-10-31 发布 **π0**——3B 参数 VLM 骨干加流匹配动作头,在 8 个机器人平台上以最高 50 Hz 输出连续控制,训练数据是当时最大的机器人交互数据集;端到端完成叠衣服和收拾餐桌。完成 $400M Series A,估值 $2.4B(2024 年 11 月;Bezos、OpenAI、Thrive)。
- **OpenVLA**(2024 年 6 月)给学术界提供了开放的 7B VLA 基线。**Unitree G1** 以约 $16k 发布(2024 年 5 月,以发布时为准),击穿了人形机器人硬件的价格底线。Boston Dynamics 让液压 Atlas 退役,推出全电动重新设计版本(2024 年 4 月)。
- Tesla Optimus 的 "We, Robot" 演示(2024 年 10 月)因未披露的遥操作而受到质疑——这正是该时代"演示 vs 自主性"可信度鸿沟的缩影。

### 2025:每个主要实验室都发布了机器人基础模型
- **2025 年 1 月 —— CES**:Jensen Huang 把 "**Physical AI**" 推广为总括术语,发布 **Cosmos** 世界基础模型(在约 2,000 万小时视频上训练;参见[世界模型](world-models.md)),并宣称机器人的 ChatGPT 时刻"即将到来"。
- **2025-02-20 —— Figure Helix**:第一个以高频率控制人形机器人整个上半身(手腕、躯干、头部、每根手指)的 VLA;第一个用同一套权重驱动两台协作机器人的模型;完全运行在机载低功耗 GPU 上。
- **2025 年 2 月 —— π0 开源**(权重 + 代码)。**2025 年 4 月 —— π0.5** 展示了移动操作能力泛化到训练中从未见过的家庭中的清洁任务。
- **2025-03-12 —— Gemini Robotics + Gemini Robotics-ER**(Google DeepMind):基于 Gemini 2.0、带动作输出的 VLA;ER 变体面向具身空间推理;合作伙伴包括 Apptronik、Agility、Boston Dynamics。**2025 年 6 月 —— Gemini Robotics On-Device**(DeepMind 第一个可供微调的 VLA;在双臂机器人上本地运行);**2025 年 9 月 —— Gemini Robotics 1.5** 增加了智能体式多步推理。
- **2025-03-18 —— NVIDIA Isaac GR00T N1**:第一个开放、可定制的人形机器人基础模型,采用双系统架构(System 2 VLM 规划器 + System 1 扩散动作模块),与开源 **Newton** 物理引擎(NVIDIA + Google DeepMind + Disney Research)同期发布。NVIDIA 宣称在 11 小时内生成 78 万条合成轨迹(约相当于 9 个月的人类演示),比仅用真实数据提升 40%(厂商说法)。
- **资金与扩张(截至 2025-12)**:Figure Series C 超 $1B,投后估值 **$39B**(2025-09-16;由 Parkway Venture Capital 领投,NVIDIA、Intel Capital、Brookfield 参与——19 个月内估值跳涨 15 倍);Physical Intelligence $600M Series B,估值 **$5.6B**(2025 年 11 月,CapitalG 领投);1X 开放消费级 NEO 预订,售价 $20k 或 $499/月(2025 年 10 月);Unitree 达到独角兽地位(约 $1.3B,2025 年 6 月),2025 年出货约 5,500 台人形机器人;AgiBot 出货约 5,100 台(TrendForce)。2025 年中国约占全球人形机器人出货量的 85–90%(据 IDC 全球约 18,000 台——由新华社转载;已核实的追踪机构区间为约 13.3K(Omdia)到约 18K(IDC);参见[最新进展](state-of-the-art.md)中的口径核对表)。机器人初创公司 2025 年融资创纪录达 **$26.5B**(Dealroom 数据,经由 CNBC——该确切数字为单一来源;各追踪机构因口径不同而分歧:PitchBook 约 $27.6B,Crunchbase 仅风险投资约 $14B)。

### 2026(上半年):"ChatGPT 时刻"被宣告;部署与量产
- **2026 年 1 月 —— CES**:NVIDIA 宣告"物理 AI 的 ChatGPT 时刻已经到来"(据 Fortune,Huang 的主题演讲收敛为"几乎到来");GTC 2026 以物理 AI 为中心(Alpamayo 端到端自动驾驶模型、Rubin 平台)。Huang 反复把人形机器人劳动自动化描述为 **$40T 可及市场**——这是宣传性数字,不是预测。
- **部署(截至 2026-07)**:Figure 03 机器人经过约 11 个月、据报道涉及 30,000+ 辆汽车的试点后,已在 BMW Spartanburg 产线上工作;约 40 台,按约 $25/机器人运行小时计费(未证实——来源为聚合媒体)。Hyundai 宣布计划(2026 年 5 月)在其工厂部署 25,000+ 台 Atlas,约从 2028 年起规模化。据报道 Tesla 终止了 Model S/X 生产,正把 Fremont 产线转向 Optimus,Gen 3 量产推迟到 2026 年中/晚期(未证实)。Counterpoint 估计 2026 年商业运行的人形机器人超过 50,000 台,高于 2025 年底的约 16,000 台。
- **中国把这个品类工业化**([landscape-china](landscape-china.md)):AgiBot 下线第 10,000 台通用机器人(2026 年 3 月);Unitree 科创板 IPO 申请获受理(2026 年 3 月递交,2026 年 6 月过会;拟募资约 ¥4.2B,目标估值约 $6.2B)——2025 年其人形机器人营收首次超过四足机器人营收;TrendForce 预测 2026 年中国人形机器人产量同比 +94%,Unitree + AgiBot 占出货量约 80%;中国有 140+ 家人形机器人厂商、330+ 款已发布机型;2026 年上半年中国具身智能融资超 ¥46B、共 288 笔(截至 2026-06);政府政策将具身智能列为战略优先事项,并为 2026 年底设定部署配额("工作模式")。
- **模型迭代持续(截至 2026-07)**:Gemini Robotics-ER 1.6(2026-04-14);NVIDIA GR00T N1.7 早期访问(2026-04-17),基于 Cosmos-Reason2 骨干、在约 20,854 小时第一人称人类视频上预训练的 3B 开放 VLA,NVIDIA 宣称首次发现"机器人灵巧性的 scaling law"(未证实——厂商说法);Ant Group 的 LingBot-VLA(2026 年 1 月)以及拥挤的开放模型阵营(SmolVLA、X-VLA、Wall-OSS)。据报道 Physical Intelligence 正洽谈以约 $11B 估值融资约 $1B(2026-03 由 Bloomberg/TechCrunch 首先报道;截至 2026-07 未确认完成)。当前能力见:[最新进展](state-of-the-art.md)。

## 反复出现的模式

- **Moravec 悖论持续了 40 年**:抽象推理(国际象棋、围棋、语言)早在叠衣服之前就被 AI 攻克。2023–2026 的 VLA 时代是对它的第一次可信进攻——但灵巧[操作](manipulation.md)仍然大幅落后于语言能力(参见[开放问题](open-problems.md))。
- **数据是反复出现的瓶颈**:Shakey 的世界模型是手工编码的;深度强化学习用模拟替代数据;VLA 则用网络规模预训练 + 遥操作 + 第一人称人类视频。每个时代的赢家都找到了更便宜的数据来源(参见[数据](data.md))。
- **每个时代都过度承诺通用性,然后被具身现实检验纠正**:Shakey 的符号推理、ASIMO 的编排式动作、深度强化学习的模拟冠军。演示历来领先部署 5–10 年——不过付费部署(BMW、Hyundai、中国工厂)是本轮周期真正的新特征。
- **炒作周期就是资本周期**:DARPA 资金(1960s–70s、2004–15)、企业实验室(2012–21)、创纪录规模的风险资本(2023–;参见[投资](investment.md))。Figure 在 19 个月内估值跳涨 15 倍(截至 2025-09),对硬件公司而言在历史上是异常的。
- **模拟持续复利**:从 Dactyl 的域随机化到 Isaac/Newton 和世界模型,模拟技术栈是深度强化学习时代最持久的遗产(参见[模拟](simulation.md)、[世界模型](world-models.md))。贯穿四个时代的关键机构角色:[组织](organizations.md)。

## 来源
- https://ai.stanford.edu/~nilsson/OnlinePubs-Nils/General%20Essays/Shakey-aimag-17.pdf — Nilsson 关于 Shakey(1966–72)、STRIPS/A* 的一手记述。
- https://en.wikipedia.org/wiki/Unimate — Unimate/Devol/Engelberger 相关日期;1961 年 GM 安装。
- https://spectrum.ieee.org/unimation-robot — IEEE Spectrum 关于第一台工业机械臂的报道。
- https://en.wikipedia.org/wiki/DARPA_Grand_Challenge — 2004 年无人完赛,2005/2007 年冠军。
- https://openai.com/index/learning-dexterity/ — OpenAI Dactyl(2018 年 7 月),通过域随机化实现模拟到现实。
- https://openai.com/index/solving-rubiks-cube/ — Dactyl 还原魔方(2019 年 10 月),自动域随机化。
- https://journals.sagepub.com/doi/10.1177/02783649241312698 — 基于学习的腿足运动综述(2019–20 年 ANYmal 强化学习里程碑)。
- https://deepmind.google/blog/rt-2-new-model-translates-vision-and-language-into-action/ — RT-2 作为第一个 VLA;未见任务 62% vs 32% 的结果。
- https://arxiv.org/abs/2310.08864 — Open X-Embodiment / RT-X:22 种本体、100 万+ 轨迹、RT-1-X 提升 50%。
- https://deepmind.google/blog/scaling-up-learning-across-many-different-robot-types/ — DeepMind RT-X 博客。
- https://arxiv.org/abs/2401.02117 — Mobile ALOHA 论文(成本、联合训练结果)。
- https://www.pi.website/blog/pi0 — π0 一手来源:2024-10-31,3B VLM + 流匹配,8 个平台。
- https://www.therobotreport.com/physical-intelligence-raises-600m-advance-robot-foundation-models/ — PI $600M Series B,估值 $5.6B(2025 年 11 月)。
- https://techcrunch.com/2026/03/27/physical-intelligence-is-reportedly-in-talks-to-raise-1-billion-again/ — PI 洽谈约 $11B 估值融资(2026 年 3 月,据报道)。
- https://www.bloomberg.com/news/articles/2026-03-27/ex-deepmind-staffers-robotics-startup-in-talks-for-11-billion-valuation — Bloomberg 对 PI $1B/$11B 融资洽谈的确认(2026 年 3 月)。
- https://www.figure.ai/news/helix — Helix 一手来源:第一个全上半身、多机器人 VLA(2025-02-20)。
- https://www.figure.ai/news/series-c — Figure Series C 超 $1B、投后 $39B(2025-09-16),投资人名单。
- https://techcrunch.com/2025/09/16/figure-reaches-39b-valuation-in-latest-funding-round/ — Figure 估值的独立确认。
- https://deepmind.google/blog/gemini-robotics-brings-ai-into-the-physical-world/ — Gemini Robotics + ER 发布公告(2025-03-12)。
- https://www.infoq.com/news/2025/07/google-gemini-robotics/ — Gemini Robotics On-Device(2025 年 6 月)。
- https://blog.google/innovation-and-ai/models-and-research/google-deepmind/gemini-robotics-er-1-6/ — Gemini Robotics-ER 1.6(2026 年 4 月)。
- https://nvidianews.nvidia.com/news/nvidia-isaac-gr00t-n1-open-humanoid-robot-foundation-model-simulation-frameworks — GR00T N1 + Newton 引擎一手来源(2025-03-18)。
- https://blogs.nvidia.com/blog/ces-2025-jensen-huang/ — CES 2025:"Physical AI" 叙事框架,Cosmos 发布。
- https://www.axios.com/2026/01/05/nvidia-ces-2026-jensen-huang-speech-ai — CES 2026 "物理 AI 的 ChatGPT 时刻已经到来";Alpamayo、Rubin。
- https://fortune.com/2026/01/06/nvidia-jensen-huang-chatgpt-moment-for-robotics/ — Fortune 关于 CES 2026 "已到来" vs "几乎到来"措辞收敛的报道。
- https://www.cnbc.com/2026/01/21/nvidia-jensen-huang-robotics-opportunity-europe-.html — 2025 年机器人融资创纪录 $26.5B(Dealroom);该确切数字为单一来源。
- https://news.crunchbase.com/robotics/startup-venture-funding-surges-2026-data/ — Crunchbase:2025 年机器人风险投资约 $14B(口径与 Dealroom/PitchBook 不同)。
- https://247wallst.com/investing/2026/05/31/jensen-huang-just-called-humanoid-robots-a-40-trillion-market-heres-why-wall-street-is-loading-up-on-physical-ai-stocks/ — Huang 反复提出的 $40T 人形机器人劳动 TAM 叙事(2026 年 5 月报道)。
- https://bostondynamics.com/blog/electric-new-era-for-atlas/ — 液压 Atlas 退役;电动 Atlas(2024 年 4 月)。
- https://www.foxnews.com/tech/hyundai-send-25000-atlas-robots — Hyundai 25,000+ 台 Atlas 部署计划(2026 年 5 月)。
- https://www.trendforce.com/presscenter/news/20260409-13007.html — TrendForce:2026 年中国人形机器人产量同比 +94%;Unitree/AgiBot 约 80% 份额。
- https://www.techtimes.com/articles/317632/20260602/unitree-ipo-cleared-agibot-hits-10000-units-china-humanoid-robot-duopoly-takes-shape.htm — Unitree 科创板 IPO 过会;AgiBot 第 10,000 台下线。
- https://www.news.cn/tech/20260108/46b1220e159d4f80bc6a4240eb3b47b5/c.html — 新华社:2025 年中国人形机器人出货约 18,000 台。
- https://www.scmp.com/tech/tech-trends/article/3340446/chinas-unitree-ships-more-5500-humanoid-robots-2025-surpassing-us-peers — SCMP:Unitree 2025 年出货 >5,500 台人形机器人(据其 IPO 招股书);AgiBot 约 5,168 台(据 Omdia)。
- https://caifuhao.eastmoney.com/news/20260627181443427425560 — 2026 年上半年中国具身智能融资 >¥46B、288 笔。
- https://merics.org/en/report/embodied-ai-chinas-ambitious-path-transform-its-robotics-industry — 中国具身 AI 政策框架。
- https://www.ctco.blog/posts/humanoid-robots-state-of-the-art-2026/ — 2026 年部署细节(Figure 03/BMW、Optimus 状态);单一博客来源,谨慎标注。
- https://www.marktechpost.com/2026/04/28/top-10-physical-ai-models-powering-real-world-robots-in-2026/ — 2026 年模型格局,含 GR00T N1.7(细节为单一来源)。
