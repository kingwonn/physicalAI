---
title: 仿真与模拟到现实
slug: simulation
updated: 2026-07-03
confidence: verified
lang: zh
source: ../wiki/simulation.md
---
> 仿真(simulation)是将机器人学习数据规模扩展到真实硬件产能之外的首要杠杆:GPU 并行物理引擎(Isaac Sim/Lab、MuJoCo Warp/MJX、Genesis、ManiSkill3/SAPIEN)可在单块 GPU 上运行数千个环境,把运动控制训练从数周压缩到数分钟;而域随机化(domain randomization)、系统辨识(system identification)和 real2sim 流水线则在不断缩小模拟到现实(sim2real)差距。2025–26 年,该领域向两大 GPU 物理栈收敛——NVIDIA 的 Newton(与 Google DeepMind、Disney Research 联合开发,自 2025-09 起由 Linux Foundation 治理,2026 年 GTC 发布 1.0 GA)和 MuJoCo Warp——同时仿真的角色也从强化学习训练场扩展为工业级合成数据工厂(MimicGen/SkillGen 轨迹倍增、Cosmos/GR00T-Dreams 神经世界模型数据),日益与[世界模型](world-models.md)融合,成为[数据战略](data.md)中的"神经仿真"层。

## 为什么仿真对 Physical AI 至关重要

- 真实机器人数据是机器人基础模型的核心瓶颈:遥操作(teleoperation)每台机器人每天只能采集数小时数据,而单块 GPU 每天可模拟数年的经验。完整的数据金字塔(网络数据 → 合成/仿真 → 真实遥操作)见[数据](data.md)。
- 对运动控制而言,仿真已是**事实上解决了的基础设施**:大规模并行强化学习 + 域随机化可得到零样本迁移的行走/奔跑控制器——这几乎是所有现代[人形机器人](humanoid-robots.md)和四足步态背后的训练配方(见[运动控制](locomotion.md))。Rudin 等(2021)展示了在单块工作站 GPU 上用 4,096 个并行 Isaac Gym 环境约 20 分钟训练出 ANYmal 运动策略。
- **操作任务仍高度依赖真实数据**:接触动力学、可变形体和感知差距意味着大多数[视觉-语言-动作模型(VLA)](vla-models.md)(π0、Helix、RT-2 系列)主要在真实遥操作数据上训练,仿真用于增强、评估和预训练。弥合这一不对称性是首要的[开放问题](open-problems.md)。
- 仿真同时充当**评估工具**(ManiSkill、RoboCasa、LIBERO、Isaac Lab Arena 等可复现基准)——在 VLA 宣称领先于标准化测试的当下愈发重要(见[技术现状](state-of-the-art.md))。

## 主要平台(截至 2026-07)

| 平台 | 维护方 | 物理 / 渲染 | 特色 | 状态 |
|---|---|---|---|---|
| **Isaac Sim 5.0 + Isaac Lab** | NVIDIA | PhysX 5 → 正迁移到 Newton;RTX 光线追踪传感器 | 基于 Omniverse/OpenUSD 的全栈机器人仿真;SDG 流水线;神经(NuRec)渲染;2025 年 SIGGRAPH 在 GitHub 开源 | GA;Isaac Lab 2.3(2025-09)新增 ADR、PBT、灵巧遥操作 |
| **MuJoCo / MJX / MuJoCo Warp** | Google DeepMind | MuJoCo 接触模型;MJX(JAX)、MJWarp(NVIDIA Warp) | 接触密集型强化学习的研究标准;MJWarp 为 DeepMind–NVIDIA 联合项目,供给 Newton | MuJoCo 成熟;MJWarp 作为 Newton 1.0 的求解器发布("MuJoCo 3.5",2026-03);面向吞吐优化(据文档,单步延迟劣于 CPU 版 MuJoCo) |
| **Newton** | Linux Foundation(NVIDIA + Google DeepMind + Disney Research) | 多求解器(MJWarp、Warp 求解器、MPM),可微分,OpenUSD | 意在成为通用 GPU 物理基座;Isaac Lab 后端;采用者包括 ETH RSL、TUM、北京大学、Lightwheel、Style3D | 2025-09-29 Beta;2026 年 GTC(2026-03)1.0 GA,含 VBD + iMPM 可变形体、Disney Kamino 求解器 |
| **Genesis** | Genesis AI + 约 20 个实验室的学术联盟 | 自研 GPU 物理(刚体、MPM、SPH、FEM)+ 生成式场景引擎 | 纯 Python;宣称在 RTX 4090 上达 43M FPS(简单场景);速度宣称存在争议(见下文) | 2024-12 起开源 |
| **SAPIEN / ManiSkill3** | UCSD 苏昊(Hao Su)实验室 / Hillbot | 基于 PhysX 的 GPU 仿真 + 并行渲染 | 以操作为中心的基准套件(12 个领域);视觉数据采集比同类快 10–1000 倍,含渲染约 30k+ FPS;RSS 2025 论文 | 活跃 |
| **Habitat 3.0** | Meta FAIR | 运动学/抽象物理,快速 CPU 渲染 | 人机协作(虚拟人)、社交导航/重排;导航时代的旗舰 | 维护中;在领域转向 GPU 物理 + 操作后地位下降 |
| **Genie Sim 3.0** | 智元机器人(AgiBot) | — | 与 AgiBot World 数据集配套的开源全栈评估工具链;用于 2026 年 ICRA 的 AGIBOT World Challenge(526 支队伍、27 个国家) | 活跃;见[中国格局](landscape-china.md) |

- 其他值得关注的项目:Gazebo/ROS 2(经典机器人学)、Webots、CoppeliaSim(传统);基于 Unreal/Unity 的照片级仿真(AirSim 后继者、UnrealZoo);mjlab(2026-01,Kevin Zakka 等)——在 MuJoCo Warp 物理上实现 Isaac Lab 的 manager-based API,定位为轻量替代;MuJoCo Playground(DeepMind,2025-01)——开箱即用的 MJX/Warp sim2real 套件,已用于四足和人形迁移。

## GPU 并行强化学习范式

- **核心配方**(由 Isaac Gym 2021 确立,现已成标准):单块 GPU 上数千个向量化环境,PPO 系列在线策略强化学习,奖励/观测以批量张量计算、无 CPU 往返;在消费级硬件上以分钟到小时级完成端到端策略训练。
- 吞吐量基准(厂商口径,时间为 2025-09 至 2026-06):
  - MuJoCo Warp:在 2025 年 GTC Newton 发布会上,相比此前 MuJoCo 基线,人形任务提速 >70 倍、手内操作约 100 倍;Newton 1.0 GA(2026 年 GTC,2026-03)报告在 RTX PRO 6000 Blackwell 上相比 MJX 达 252 倍(运动控制)和 475 倍(操作)(厂商数据,无独立复现)。
  - ManiSkill3:含渲染 30,000+ FPS;比同类平台快 10–1000 倍、GPU 显存少 2–3 倍(论文宣称)。
  - Genesis:宣称 Franka 机械臂在 RTX 4090 上达 43M FPS / 430,000 倍实时。独立分析(SAPIEN/ManiSkill 作者 Stone Tao)表明头条数字来自近乎空场景;在典型接触密集场景下,其他 GPU 仿真器可持平或胜出。所有厂商的头条 FPS 营销数字都应视为高度依赖场景。
- **趋势——物理与框架解耦**:Isaac Lab API 正成为事实上的接口标准(mjlab 将其套在 MuJoCo Warp 上),而 Newton 志在成为可插拔求解器的基座;可以预期训练代码将可跨物理后端移植。
- **趋势——大规模 RL 回归**:Isaac Lab 2.3 内置自动域随机化(ADR)和基于种群的训练(PBT),灵巧操作训练可达 40,960 个并行环境,以平民化成本重现 OpenAI 2019 年的 ADR 配方。

## Sim2real:差距与工具箱

差距来源:刚性接触近似、执行器/传动动力学、传感噪声与延迟、视觉外观,以及未建模物理(线缆、可变形体、摩擦变异)。

| 技术 | 思路 | 典型案例 |
|---|---|---|
| 域随机化(DR) | 随机化视觉/动力学,使现实成为训练分布中的一个样本 | Tobin 等 2017(视觉);Peng 等 2018(动力学) |
| 自动 DR / 课程学习 | 随策略提升自动扩大随机化范围 | OpenAI 魔方 2019;Isaac Lab 2.3 ADR(2025) |
| 系统辨识 | 用真实日志拟合仿真参数(尤其是执行器);学习式执行器网络 | Hwangbo 等 2019(ANYmal) |
| 师生蒸馏 | 仿真中的特权状态教师 → 仅依赖观测的学生部署 | Lee 等 2020;人形全身控制的标准做法 |
| LLM 引导的奖励 + DR 设计 | 用 LLM 编写奖励函数和 DR 配置 | Eureka(2023)、DrEureka(2024) |
| 多仿真器随机化 | 跨异构仿真器训练以抵消单引擎偏差 | PolySim(2025-10)——零样本迁移到 Unitree G1 |
| Real2sim / 数字孪生 | 将真实场景重建(摄影测量、3D 高斯泼溅、神经渲染)为仿真资产 | Isaac Sim 5.0 NuRec;数字孪生工厂工作流 |
| 残差 / 在线修正 | 用少量真实数据或人工干预微调/修正仿真策略 | TRANSIC(2024);simDP(2026-06)对齐动作/观测空间 |
| 硬件在环与联合训练 | 训练同一策略时混合仿真与真实批次 | 在 VLA 训练中常见(sim-and-real 联合训练报告) |

- 2026 年的共识:差距是一项工程预算,而非不可逾越的墙——运动控制已可常规零样本跨越;接触密集操作仍需真实世界微调。2025 年 Annual Reviews 综述("The Reality Gap in Robotics")将最佳实践归纳为保真度、随机化与自适应的组合,而非押注单一手段。

## 合成数据生成(SDG)流水线

- **轨迹倍增**:MimicGen(2023)通过重组以物体为中心的片段,从约 200 条人类示范生成约 5 万条示范;后继 SkillGen(Isaac Lab 2.3)加入无碰撞运动规划;DexMimicGen 扩展到双臂/灵巧场景。这是低成本扩展模仿数据的主力工具。
- **感知 SDG**:Isaac Sim/Omniverse Replicator 渲染带随机化场景的光线追踪 RGB、深度、激光雷达、雷达数据,用于训练检测/分割模型——成熟,已在工业视觉中广泛应用。
- **神经 / 世界模型 SDG**(2025–26 年的转变):NVIDIA Cosmos 世界基础模型可基于一张图像 + 语言条件生成照片级机器人视频;**GR00T-Dreams**(基于 DreamGen 研究)从这些"梦境"中提取伪动作轨迹,用于训练 GR00T-N 人形模型,任务无需专门遥操作数据。NVIDIA 称开发时间"从数月降到数小时"(厂商宣称)。截至 2025-09,Cosmos WFM 下载量超过 300 万,NVIDIA Physical AI Dataset 下载量达 480 万。这一层与[世界模型](world-models.md)高度重叠。
- **Cosmos Transfer** 类模型做 sim2real 外观转换——将仿真回放渲染成多样的照片级变体,从生成侧攻克视觉差距(截至 2025-09,Cosmos Transfer 2.5 比前代小 3.5 倍)。
- **数据战略定位**:NVIDIA 公开的"数据金字塔"= 网络级视频/文本(基底)→ 合成仿真 + 神经数据(中层)→ 真实遥操作(稀缺塔尖)。Genesis AI 的主张反其道而行:以专有物理引擎作为通用机器人基础模型的主数据源。Tesla/Figure 则强调真实车队/遥操作数据;仿真与真实数据的配比是各[组织](organizations.md)之间的开放战略赌注——见[数据](data.md)与[投资](investment.md)。

## 生态与商业层(截至 2026-07)

- **NVIDIA** 是引力中心:Isaac Sim/Lab 开源(SIGGRAPH 2025),Newton Beta(2025-09)→ 1.0 GA(2026 年 GTC),由 Linux Foundation 治理——GA 采用者包括 Skild AI(GPU 机架装配强化学习)和 Samsung/Lightwheel(可变形线缆仿真)——再加上 GR00T 模型 + Cosmos WFM + OSMO 编排,构成"三台计算机"(训练 / 仿真 / 部署)的整体叙事。Isaac GR00T 参考人形机器人(2026-06-01 在 GTC Taipei/COMPUTEX 发布)组合了 Unitree H2 Plus 本体、Sharpa Wave 触觉灵巧手(dexterous hand)和 Jetson Thor T5000,搭配开放的 Isaac GR00T 软件栈,面向学术实验室(Ai2、ETH Zurich、Stanford、UCSD);预计 2026-10 供货。
- **Google DeepMind** 维持 MuJoCo 免费开源并共同开发 MuJoCo Warp;MuJoCo Playground + mjlab 构成研究优先的轻量栈。
- **Genesis AI**:1.05 亿美元种子轮由 Eclipse 与 Khosla 领投(2025-07,创机器人领域种子轮纪录之一;投资方包括 Eric Schmidt、Bpifrance、HSG);创始人为 Zhou Xian(CMU)和 Théophile Gervet(前 Mistral);约 60 名员工分布美欧两地(截至 2025-07)。2026-05 随 GENE-26.5 转向"全栈":在与 Wuji Tech 联合设计的人形灵巧手上演示灵巧操作(打鸡蛋、切菜、魔方、弹钢琴);仅有厂商演示,尚无第三方评估。
- **Lightwheel**(仿真资产/评估初创)与 NVIDIA 共同开发 Isaac Lab Arena 策略评估框架;**Hillbot** 商业化 SAPIEN/ManiSkill 产品线;**Antioch**(2025-05 成立)以 6,000 万美元估值完成 850 万美元种子轮(2026-04,A* + Category Ventures),自我定位为"Physical AI 领域的 Cursor"——将云端仿真实例接入机器人真实软件栈。
- **中国**:智元机器人的 Genie Sim 3.0 + AgiBot World 数据集构成开放 sim2real 工具链的支柱;AGIBOT World Challenge 2026(ICRA,维也纳,2026-06;2026-05 线上赛有来自 27 个国家的 526 支队伍,vivo 的 PrismBot 获 Reasoning-to-Action 赛道冠军)将决赛评分从仿真基准改为闭环真实机器人测试——一次值得注意的评估文化转变。见[中国格局](landscape-china.md)。

## 时间线要点,2024-12 → 2026-06

| 日期 | 事件 |
|---|---|
| 2024-12 | Genesis 开源;430,000 倍实时的宣称走红,随后引发基准方法论争议 |
| 2025-01 | MuJoCo Playground 发布(基于 MJX 的 GPU sim2real 套件) |
| 2025-03(GTC) | MuJoCo Warp 公布;Newton(NVIDIA + DeepMind + Disney)亮相 |
| 2025-06 | Isaac Sim 5.0 / Isaac Lab 2.2 在 GitHub 开放早期开发者预览 |
| 2025-07 | Genesis AI 携 1.05 亿美元种子轮走出隐身模式 |
| 2025-08(SIGGRAPH) | Isaac Sim 5.0 + Isaac Lab 2.2 GA 并开源 |
| 2025-09 | Newton Beta 纳入 Linux Foundation;Isaac Lab 2.3(ADR、PBT、与 Lightwheel 合作的 Arena);GR00T N1.6 + Cosmos Reason |
| 2025-10 | PolySim 多仿真器随机化 → 零样本迁移到 Unitree G1 |
| 2026-01 | mjlab 预印本(MuJoCo Warp 上的 Isaac Lab API) |
| 2026-03(GTC) | Newton 1.0 GA——MJWarp("MuJoCo 3.5")相比 MJX 252 倍/475 倍(厂商宣称);VBD + iMPM 可变形体求解器;Disney Kamino 刚体求解器;SDF 碰撞、水弹性接触 |
| 2026-04 | Antioch 850 万美元种子轮("Physical AI 领域的 Cursor") |
| 2026-05 | Genesis AI 全栈演示(GENE-26.5) |
| 2026-06 | AGIBOT World Challenge @ ICRA 改为真实机器人闭环评估;Genie Sim 3.0 开放工具链;NVIDIA Isaac GR00T 参考人形机器人(2026-06-01);Cosmos 3 全模态 WFM 发布(2026-06) |

## 开放问题

- **操作能否复制运动控制的仿真优先路径?** 接触密集、可变形体和工具使用任务仍缺乏可信的仿真物理;Newton 的多求解器(MPM + 刚体)耦合是主要押注。
- **经典仿真 vs. 神经世界模型**:学习式视频/世界模型会取代物理引擎做数据生成,还是收敛为混合形态(物理引擎提供动力学真值,生成模型提供外观/多样性)——见[世界模型](world-models.md)。
- **基准诚信**:厂商 FPS 数字依赖场景且易被营销化(Genesis 事件);策略层面的评估(Isaac Lab Arena、AgiBot 式真实机器人挑战赛)正取代原始吞吐量,成为真正重要的指标。
- **碎片化 vs. 整合**:Newton/MJWarp 的融合预示共享 GPU 物理基座,但 Genesis、SAPIEN 以及各家自研仿真器(Tesla、Figure、Boston Dynamics)使格局保持多元。

## 来源
- https://developer.nvidia.com/blog/announcing-newton-an-open-source-physics-engine-for-robotics-simulation/ — Newton 架构、Warp/OpenUSD 基础、MJWarp 70 倍/100 倍提速
- https://nvidianews.nvidia.com/news/nvidia-accelerates-robotics-research-and-development-with-new-open-models-and-simulation-libraries — Newton Beta + Linux Foundation(2025-09)、GR00T N1.6、Cosmos 下载量、采用者名单
- https://www.linuxfoundation.org/press/linux-foundation-announces-contribution-of-newton-by-disney-research-google-deepmind-and-nvidia-to-accelerate-open-robot-learning — Newton 治理结构
- https://developer.nvidia.com/blog/streamline-robot-learning-with-whole-body-control-and-enhanced-teleoperation-in-nvidia-isaac-lab-2-3/ — Isaac Lab 2.3(2025-09):ADR、PBT、SkillGen、Arena/Lightwheel、40,960 环境训练
- https://developer.nvidia.com/blog/isaac-sim-and-isaac-lab-are-now-available-for-early-developer-preview/ — Isaac Sim 5.0 / Isaac Lab 2.2 GitHub 发布,SIGGRAPH 2025 GA
- https://developer.nvidia.com/blog/newton-adds-contact-rich-manipulation-and-locomotion-capabilities-for-industrial-robotics/ — Newton 1.0 GA(2026 年 GTC,2026-03-16):MJWarp 在 Blackwell 上相比 MJX 252 倍/475 倍、VBD/iMPM 可变形体、Kamino 求解器、Skild AI + Samsung/Lightwheel 采用
- https://mujoco.readthedocs.io/en/latest/mjwarp/ — MJWarp 状态、特性、与 MJX 的扩展性对比、Isaac Lab/mjlab 集成
- https://github.com/google-deepmind/mujoco_warp — MJWarp 仓库(NVIDIA + DeepMind 联合项目)
- https://github.com/google-deepmind/mujoco_playground — MuJoCo Playground sim2real 套件
- https://arxiv.org/abs/2601.22074 — mjlab:MuJoCo Warp 上的 Isaac Lab manager-based API(2026-01)
- https://arxiv.org/abs/2410.00425 — ManiSkill3:GPU 并行仿真+渲染、30k+ FPS、RSS 2025
- https://arxiv.org/abs/2310.13724 — Habitat 3.0:人、虚拟人与机器人共处
- https://stoneztao.substack.com/p/the-new-hyped-genesis-simulator-is — 对 Genesis 速度基准的独立批评
- https://techcrunch.com/2025/07/01/genesis-ai-launches-with-105m-seed-funding-from-eclipse-khosla-to-build-ai-models-for-robots/ — Genesis AI 1.05 亿美元种子轮、创始人、团队规模
- https://techcrunch.com/2026/05/06/khosla-backed-robotics-startup-genesis-ai-has-gone-full-stack-demo-shows/ — Genesis AI 全栈演示(2026-05)
- https://developer.nvidia.com/blog/enhance-robot-learning-with-synthetic-trajectory-data-generated-by-world-foundation-models/ — GR00T-Dreams / DreamGen 世界基础模型轨迹生成
- https://developer.nvidia.com/blog/scale-synthetic-data-and-physical-ai-reasoning-with-nvidia-cosmos-world-foundation-models/ — Cosmos WFM 的 SDG 角色
- https://arxiv.org/abs/2510.01708 — PolySim 多仿真器动力学随机化、Unitree G1 零样本迁移
- https://arxiv.org/abs/2606.03551 — Isaac Sim 综述(2026-06):架构、SDG、使用模式
- https://arxiv.org/abs/2511.04831 — Isaac Lab 框架论文(2025-11)
- https://www.annualreviews.org/content/journals/10.1146/annurev-control-031924-100130 — "The Reality Gap in Robotics" 综述:差距分类与最佳实践
- https://arxiv.org/abs/2109.11978 — Rudin 等:大规模并行强化学习,分钟级运动控制训练
- https://arxiv.org/abs/1703.06907 — Tobin 等 2017:域随机化起源
- https://arxiv.org/abs/1910.07113 — OpenAI 2019:自动域随机化(魔方)
- https://arxiv.org/abs/2310.17596 — MimicGen:200 条示范 → 5 万条合成示范
- https://techcrunch.com/2026/04/16/this-simulation-startup-wants-to-be-the-cursor-for-physical-ai/ — Antioch 以 6,000 万美元估值完成 850 万美元种子轮(2026-04)
- https://www.tradingview.com/news/eqs:09f22872d094b:0-agibot-world-challenge-2026-advances-embodied-ai-competition-from-simulation-to-real-robot-testing-at-icra-2026/ — AGIBOT World Challenge 2026、Genie Sim 3.0、转向真实机器人评估
- https://www.globenewswire.com/news-release/2026/05/13/3293715/0/en/Global-Showdown-526-Teams-from-27-Countries-Compete-in-the-AGIBOT-WORLD-CHALLENGE-ICRA-2026-Online-Round.html — 2026-05 线上赛 526 支队伍 / 27 个国家
- https://nvidianews.nvidia.com/news/nvidia-open-humanoid-robot-reference-design — Isaac GR00T 参考人形机器人(Unitree H2 Plus + Sharpa Wave 灵巧手 + Jetson Thor T5000,2026-06-01,2026-10 供货)
- https://www.prnewswire.com/news-releases/genesis-ai-unveils-gene-26-5--the-first-ai-brain-to-enable-robots-with-human-level-physical-manipulation-capabilities-302763638.html — GENE-26.5 发布详情、与 Wuji Tech 的灵巧手合作
- https://nvidianews.nvidia.com/news/nvidia-launches-cosmos-3-the-open-frontier-foundation-model-for-physical-ai — Cosmos 3 全模态 WFM 发布(2026-06)
