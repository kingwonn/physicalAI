---
title: 术语表
slug: glossary
updated: 2026-07-04
confidence: verified
lang: zh
source: ../wiki/glossary.md
---
> Physical AI 约 35 个核心术语的释义词典 —— 涵盖模型与架构(VLA、世界模型(world model)、双系统(dual-system))、学习方法(模仿学习 vs 强化学习、diffusion policy、flow matching)、数据机制(遥操作(teleoperation)、UMI、数据飞轮(data flywheel)、Open X-Embodiment)、硬件(QDD、谐波减速器(harmonic drive)、滚柱丝杠(roller screw)、触觉传感(tactile sensing))、控制理论(ZMP、MPC、全身控制(whole-body control))以及商业简称(RaaS、BOM)。每个词条 1–3 句话,并附有链接到深入介绍该主题的 wiki 页面。按字母顺序排列,分区间小节。

## A–C

- **ACT(Action Chunking with Transformers)** —— 一种模仿学习(imitation learning)策略(Zhao et al., 2023, arXiv:2304.13705),将 transformer 训练为条件 VAE 的解码器,用于预测未来动作的"分块"(chunk)而非单步动作,从而减少复合误差(compounding error);配合 ALOHA 遥操作平台,仅用约 10 分钟的示范数据就在精细双臂任务上达到 80%–90% 的成功率。它是现代[操作(manipulation)](manipulation.md)学习及大多数 [VLA](vla-models.md) 动作头(action head)背后的基础方案。
- **动作分词(Action tokenization)** —— 将连续的机器人动作转换为离散 token,使语言模型主干能够像生成文本一样输出它们。方法从朴素的逐维分箱(RT-2)到基于压缩的分词器,例如 Physical Intelligence 的 FAST,它对动作分块做离散余弦变换(DCT)并量化系数,得到大幅缩短的序列(训练速度提升约 5 倍,公司口径)。参见 [VLA 模型](vla-models.md)。
- **ALOHA** —— "A Low-cost Open-source Hardware" 的缩写,一套低成本(约 2 万美元)的双臂遥操作平台(主从臂结构;Zhao et al., 2023),使高质量双手示范数据的采集变得平价;后续版本包括 ALOHA 2 和 Mobile ALOHA。事实上的学术界标准遥操作平台 —— 参见[操作](manipulation.md)和[数据](data.md)。
- **BOM(物料清单,bill of materials)** —— 机器人每个部件成本的总和;是论证人形机器人价格下限与利润率的关键输入。执行器(见下文 QDD、谐波减速器、行星滚柱丝杠)与灵巧手(dexterous hand)在人形机器人 BOM 中占大头;中国供应链是压低这一成本的主要力量 —— 参见[硬件](hardware.md)和[投资](investment.md)。
- **运输成本(Cost of transport, CoT)** —— 无量纲的移动效率指标:CoT = P / (m·g·v)(功率除以体重与速度之积);数值越低越好,它使机器人可以与动物、车辆直接比较。人类步行的 CoT 约为 0.2 —— 这是机器人学中的经典参考值(Collins et al., Science 2005),而按总代谢估算则更接近约 0.3 —— 而 ASIMO 时代的电驱人形机器人测得约 3.2,差了一个数量级。此后,学习得到的步态在效率上已超过基于模型的控制:Hwangbo et al.(Science Robotics 2019)报告,一个 RL 训练的 ANYmal 策略在相同速度下比基于模型的基线消耗更少机械功率(78.1 对 97.3 瓦)、扭矩减少 23%–36%;2025 年一篇 FITEE 论文报告,一个学习得到的多步态四足策略在可行速度指令范围内平均 CoT 约为 0.43 —— 详情及 CoT 报告口径不一致的注意事项参见[移动](locomotion.md)。
- **跨本体(Cross-embodiment)** —— 在多种不同机器人本体(机械臂、双臂平台、四足、人形)的数据上训练单一策略,和/或在不同本体之间迁移技能。标志性证据:Open X-Embodiment 的 RT-1-X 在数据较少的领域中平均比各机器人专用模型在其自身数据上高出约 50% 的表现,RT-2-X 在涌现技能(emergent-skill)评测中的成功率是 RT-2 的三倍。参见 [VLA 模型](vla-models.md)和[数据](data.md)。

## D–F

- **数据飞轮(Data flywheel)** —— 一种自我强化的循环:部署的机器人产生交互数据 → 数据改进模型 → 更好的模型赢得更多部署 → 产生更多数据。由特斯拉 FSD 项目推广;如今是大多数人形机器人和 VLA 公司的明确战略。参见[数据](data.md)。
- **数据代工厂(Data foundry)** —— 将机器人训练数据作为产品来生产的组织或业务:遥操作农场、搭建的真实环境、第一人称人类视频采集,以及合成数据(synthetic data)流水线(截至 2026 年的供应商包括 Scale AI、micro1 及众多中国采集中心;NVIDIA 的"Physical AI Data Factory"蓝图是以仿真为主的变体)。参见[数据](data.md)。
- **灵巧手自由度(Dexterous hand DoF)** —— 自由度(degrees of freedom):机器人手中独立关节的数量(人手约有 21+ 个)。截至 2026 年的参考值:Shadow Hand 24 个关节(约 20 个主动驱动)、特斯拉 Optimus Gen-3 手 22 个自由度、中国量产手 16–22 个自由度、价格约 3000–28000 美元;注意关节自由度不等于主动驱动自由度 —— 许多手是欠驱动的(腱绳耦合)。参见[操作](manipulation.md)。
- **Diffusion policy** —— 将视觉运动策略(visuomotor policy)表示为对动作序列的条件去噪扩散过程(Chi et al., RSS 2023):模型以观测为条件,迭代地将噪声还原为动作轨迹,能优雅地捕捉多模态的示范数据。被广泛用作 VLA 的动作头 —— 参见[操作](manipulation.md)和 [VLA 模型](vla-models.md)。
- **域随机化(Domain randomization)** —— 在训练过程中随机化模拟器参数(纹理、光照、摩擦、质量、延迟等),使真实世界看起来只是训练分布中的又一个样本(Tobin et al., 2017, arXiv:1703.06907)。这是应对模拟到现实(sim2real)差距的标准低成本手段 —— 参见[仿真](simulation.md)。
- **双系统 VLA(System 1 / System 2)** —— 一种 VLA 架构,将缓慢、庞大的视觉-语言推理器("System 2",约 7–10 Hz:场景理解、任务规划)与快速、小型的视觉运动策略("System 1",约 100–200 Hz:反应式运动控制)分离开来,借用了 Kahneman 的快思考/慢思考术语。典型案例:Figure Helix(7–9 Hz VLM / 200 Hz 策略)和 NVIDIA GR00T N1(10 Hz VLM / 120 Hz 扩散动作头)。参见 [VLA 模型](vla-models.md)。
- **具身 AI(Embodied AI)** —— 一个较早的学术术语(源自 1990 年代具身认知的脉络),指代拥有并依赖物理身体的智能;在当前用法中几乎是 Physical AI 的同义词,"embodied" 是研究界的表述,而"Physical AI"是产业界的表述。参见[历史](history.md)。
- **具身缩放定律(Embodied scaling laws)** —— (部分得到证实的)假说:机器人策略性能随训练规模呈幂律提升,其中真正重要的维度是环境/物体的*多样性*以及*本体*数量,而非单纯的训练时长:模仿学习中的数据缩放研究发现了接近幂律的泛化提升(arXiv:2410.18647),在约 1000 种程序化生成的躯体上训练的移动策略能泛化到未见过的躯体(arXiv:2505.05753)。Generalist 的 GEN-0 宣称在 27 万+ 小时的操作数据上实现平滑缩放(公司口径,未证实)。参见[开放问题](open-problems.md)和[数据](data.md)。
- **Flow matching** —— 一种连续时间的生成建模技术(学习将噪声输运到数据的速度场),用于替代扩散模型来生成动作;更少的积分步数使其足够快,可用于实时控制。π0 的 flow-matching "动作专家"(action expert)以高达 50 Hz 的频率输出动作分块。参见 [VLA 模型](vla-models.md)。

## G–I

- **GPU 并行仿真(GPU-parallel simulation)** —— 将物理计算完全放在 GPU 上运行,使数千个环境实例能在单张显卡上并行步进(NVIDIA Isaac Gym 2021 → Isaac Lab;还有 MJX、Genesis),相较 CPU 集群实现 2–3 个数量级的实际速度提升。正是这一点使大规模并行 RL 用于足式移动训练变得常规化 —— 参见[仿真](simulation.md)。
- **谐波减速器(Harmonic drive,应变波齿轮)** —— 一种紧凑型齿轮,利用可弯曲的"柔轮"(flexspline)在单级中实现极高减速比(通常 30:1–320:1),且几乎零背隙;是工业机械臂和人形机器人旋转关节的标准减速器,但难以反向驱动(backdrivable),扭矩通常需要传感而非从电流推断。与 QDD 相对。参见[硬件](hardware.md)。
- **模仿学习(Imitation learning, IL)** —— 从示范数据中学习策略(最简单形式:行为克隆,即在观测→动作对上做监督学习)。自 2023 年以来是操作任务学习的主流方案(ACT、diffusion policy、VLA 预训练);与之相对的是强化学习,后者从奖励而非示范中学习。参见[操作](manipulation.md)。

## M–P

- **MPC(模型预测控制,model predictive control)** —— 一种控制方式,在每个时间步在线反复求解有限时域最优控制问题,并只执行第一个动作("滚动时域")。是动态足式控制的主力方法(波士顿动力跑酷时代的 Atlas),并越来越多地与学习策略混合使用。参见[移动](locomotion.md)。
- **Open X-Embodiment(OXE)** —— 具有里程碑意义的跨本体数据集与合作项目(由 Google DeepMind 主导、涵盖 21 家机构,2023 年):汇集来自 34 个实验室的 60 个数据集、22 种机器人本体、100 万+条统一格式的真实轨迹,并配套 RT-X 系列模型,展示了跨机器人的正向迁移。是开源 VLA 的默认预训练语料库 —— 参见[数据](data.md)。
- **Physical AI** —— 涵盖性的产业术语,指通过传感器与执行器在物理世界中感知、理解并行动的 AI 系统 —— 机器人、自动驾驶车辆、智能空间;自 2024 年起由 NVIDIA/黄仁勋推广,被称为生成式 AI 之后的"下一波浪潮"。实质上是具身 AI 的商业化重新包装 —— 参见[历史](history.md)和[技术前沿](state-of-the-art.md)。
- **行星滚柱丝杠(Planetary roller screw)** —— 一种旋转转直线的传动机构,螺纹滚柱在丝杠轴与螺母之间公转,将载荷分散到多条接触线上;相比滚珠丝杠,在相同直径下承载能力约提升 2–3 倍,寿命也长得多。特斯拉 Optimus 在其线性执行器中使用了 14 个(倒装布局),使滚柱丝杠成为截至 2026 年人形机器人供应链与成本方面的头条话题。参见[硬件](hardware.md)。

## Q–S

- **QDD(准直驱,quasi-direct-drive)执行器** —— 大直径、高扭矩密度的电机,配以刻意选择的低减速比(约 3:1–10:1),从而具备反向驱动能力、低反射惯量、抗冲击性,并可直接从电机电流估算扭矩("本体感知驱动",源自 MIT Cheetah 系谱)。是动态足式机器人的默认选择;与谐波减速器相对。参见[硬件](hardware.md)。
- **RaaS(机器人即服务,Robots-as-a-Service)** —— 一种商业模式,客户按订阅或按任务付费,而非直接购买机器人,从而将资本支出转化为运营支出,同时让厂商保留车队数据和升级权;截至 2026 年,这是人形机器人及仓储机器人试点项目中的主流商业结构。参见[投资](investment.md)。
- **强化学习(Reinforcement learning, RL)** —— 通过试错并根据奖励信号来学习策略,而非从示范中学习。在 Physical AI 中,它主导了移动领域(大规模并行仿真训练 + 模拟到现实),并正重新在操作领域中以真实世界微调的形式出现,以提升可靠性(例如 Physical Intelligence 的 RECAP/π*0.6)。参见[移动](locomotion.md)和[操作](manipulation.md)。
- **模拟到现实(Sim2real)** —— 将在仿真中训练的策略迁移到物理硬件上;"模拟到现实差距(sim-to-real gap)"指动力学、接触、传感与视觉方面的不匹配,使得朴素迁移失败。通常用域随机化、更好的物理/渲染,以及真实世界适应来应对。参见[仿真](simulation.md)。
- **System 1 / System 2** —— 见上文"**双系统 VLA**"。

## T–Z

- **触觉传感(Tactile sensing)** —— 赋予机器人触觉。两大主流方案:*基于视觉的*传感器(GelSight 及其后继者:摄像头拍摄受光照的弹性体垫片的形变,得到高分辨率的接触几何与力信息)以及 *taxel 阵列*(离散压力/磁力传感元件组成的网格,是应用于指尖和掌心的"机器人皮肤"方案)。参见[硬件](hardware.md)和[操作](manipulation.md)。
- **Taxel** —— "触觉像素"(tactile pixel):触觉阵列中的一个离散传感元件;阵列分辨率以 taxel 数量表示,就像图像分辨率以像素数量表示一样。
- **遥操作(Teleoperation)** —— 人类实时远程控制机器人 —— 方式包括主从臂(如 ALOHA)、VR 头显、动作捕捉服或外骨骼。在 Physical AI 中,它主要是一种*数据采集*方法:是模仿学习中高质量示范数据的主要来源,成本随操作员工时线性增长。参见[数据](data.md)。
- **UMI(通用操作接口,Universal Manipulation Interface)** —— 一种手持、无动力的 3D 打印夹爪,唯一的传感器是一个 GoPro 相机(Chi et al., 2024, arXiv:2402.10329);人类无需任何机器人即可采集"野外"示范数据,夹爪位姿通过单目 SLAM 恢复,策略可迁移到真实机械臂上。衍生出庞大的变体家族(DexUMI、FastUMI、UMI-on-Legs)。参见[数据](data.md)。
- **VLA(视觉-语言-动作模型,vision-language-action model)** —— 一种基础模型,通常从视觉-语言模型初始化,将摄像头图像与语言指令直接映射为机器人动作;该术语由 Google DeepMind 的 RT-2(2023)首次提出。截至 2026 年,是 Physical AI 中的主导架构类别(π0.x、Gemini Robotics、GR00T、Helix)—— 参见 [VLA 模型](vla-models.md)。
- **全身控制(Whole-body control, WBC)** —— 一种控制框架,同时协调机器人的*所有*关节,以满足一组带优先级的任务(例如:保持平衡 ≻ 跟踪手部位姿 ≻ 保持姿态),通常在每个时间步被求解为一个二次规划问题;是人形机器人实现移动-操作(loco-manipulation)一体化的经典使能技术。参见[移动](locomotion.md)。
- **世界模型(World model)** —— 一种学习得到的模型,用于预测环境如何演化 —— 即在给定动作条件下预测未来的观测或状态。在 Physical AI 中有三种用法:作为神经模拟器/训练场(Genie 3)、作为合成数据引擎(NVIDIA Cosmos),以及越来越多地直接作为策略主干本身("世界-动作模型",例如 GR00T N2)。参见[世界模型](world-models.md)。
- **ZMP(零力矩点,zero moment point)** —— 地面上的一点,在该点处重力与惯性力的合力矩没有水平分量;将 ZMP 保持在脚部支撑多边形内,是判断动态稳定行走的经典准则(Vukobratović,1960 年代末至 70 年代)。它是 ASIMO 时代人形机器人的基础,即使在 RL/MPC 控制器逐渐接管的今天,仍作为一种稳定性检验手段留存下来。参见[移动](locomotion.md)。

## 来源
- https://www.nvidia.com/en-us/glossary/generative-physical-ai/ —— NVIDIA 对 Physical AI 的定义
- https://www.nvidia.com/en-us/glossary/embodied-ai/ —— NVIDIA 对具身 AI 的定义;术语对比
- https://arxiv.org/abs/2304.13705 —— ACT/ALOHA 论文:动作分块、2 万美元遥操作平台、10 分钟示范达到 80%–90% 成功率
- https://arxiv.org/abs/2402.10329 —— UMI 论文:手持 GoPro 夹爪、SLAM 恢复的轨迹
- https://diffusion-policy.cs.columbia.edu/ —— Diffusion Policy(Chi et al., RSS 2023)定义
- https://www.pi.website/blog/pi0 —— π0 flow-matching 动作专家,最高 50 Hz 控制频率
- https://www.pi.website/research/fast —— FAST 动作分词器(基于 DCT 的压缩方法)
- https://robotics-transformer-x.github.io/ —— Open X-Embodiment:100 万+条轨迹、22 种本体、60 个数据集、RT-X 迁移能力
- https://arxiv.org/abs/2108.10470 —— Isaac Gym:GPU 并行物理仿真,2–3 个数量级的速度提升
- https://arxiv.org/abs/1703.06907 —— 域随机化(Tobin et al., 2017)
- https://arxiv.org/abs/2503.14734 —— GR00T N1 白皮书:双系统架构,10 Hz VLM / 120 Hz 扩散动作模块
- https://www.figure.ai/news/helix —— Figure Helix 双系统架构:7–9 Hz System 2 / 200 Hz System 1
- https://arxiv.org/abs/2307.15818 —— RT-2 论文,提出"视觉-语言-动作(VLA)模型"这一术语
- https://en.wikipedia.org/wiki/Zero_moment_point —— ZMP 定义及 Vukobratović 归属
- https://en.wikipedia.org/wiki/Cost_of_transport —— 无量纲 CoT 公式 P/(m·g·v);给出总代谢人类步行 CoT 约 0.3
- https://www.science.org/doi/10.1126/science.1107799 —— Collins et al. 2005:人类步行 CoT ≈0.2 参考值,ASIMO ≈3.2
- https://arxiv.org/abs/1901.08652 —— Hwangbo et al.(Science Robotics 2019):学习得到的 ANYmal 策略在功率(78.1 对 97.3 瓦)和扭矩上优于基于模型的基线
- https://doi.org/10.1631/FITEE.2401070 —— Wang et al., FITEE 2025 26(9):1679–1691:学习得到的多步态策略,平均 CoT 0.4306
- https://pmc.ncbi.nlm.nih.gov/articles/PMC5751610/ —— GelSight 基于视觉的触觉传感机制
- https://www.fastcompany.com/91314612/this-tiny-screw-is-powering-the-humanoid-robot-revolution —— 行星滚柱丝杠相较滚珠丝杠在人形机器人中的应用
- https://www.kggfa.com/news/humanoid-robot-dexterous-hand-structure-to-high-load-bearing-development-the-number-of-roller-screws-may-be-doubled/ —— Optimus 的 14 个倒装行星滚柱丝杠(2 个肘部、4 个腕部、8 个腿部)
- https://arxiv.org/abs/2004.00467 —— QDD 定义:高扭矩密度电机 + 低(<10:1)减速比,以实现反向驱动能力/带宽
- https://en.wikipedia.org/wiki/Strain_wave_gearing —— 谐波减速器 30:1–320:1 单级减速比,无背隙
- https://arxiv.org/abs/2410.18647 —— 模仿学习中的数据缩放定律
- https://arxiv.org/abs/2505.05753 —— 移动任务中的本体缩放定律
- https://generalistai.com/blog/nov-04-2025-GEN-0 —— GEN-0 27 万+ 小时缩放主张(公司口径)
