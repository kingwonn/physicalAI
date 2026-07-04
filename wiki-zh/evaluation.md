---
title: 评测与基准
slug: evaluation
updated: 2026-07-04
confidence: verified
lang: zh
source: ../wiki/evaluation.md
---
> Physical AI 没有自己的 ImageNet:截至 2026-07,这个领域的头条成绩大多是在自选任务上自报的成功率,跑在不同的机器人上,每项只有 10–20 次试验且没有统计检验,这使得各论文之间的[视觉-语言-动作模型(VLA)](vla-models.md)基本无法互相比较。占主导地位的仿真基准(LIBERO、CALVIN、SimplerEnv)已经饱和——顶级模型都聚集在 97–99%,而 LIBERO-Plus 之类的鲁棒性探针显示,同样的模型在适度的相机或位姿扰动下会跌破 30%。2025–26 年的应对是一波共享的真机评测基础设施(基于 DROID 的 RoboArena、RoboChallenge Table30、GM-100、AutoEval、VLA-REPLICA)、更难的仿真套件(BEHAVIOR-1K、RoboCasa365、MolmoSpaces-Bench)、具身推理考卷(ERQA),以及一个有官方背景的中国基准(EIbench)——但尚无任何单一标准胜出;与此同时,工业界给机器人打分用的是吞吐量、干预率和"几个 9",而不是基准成功率。

## 一页看懂评测危机

- **数字不可迁移。** 真机评测缓慢、依赖特定硬件、跨实验室不可复现:OpenVLA 的头条成绩是在 WidowX/BridgeData 装置上的 29 项任务;π0 的成绩来自 Physical Intelligence 自家机队上的专有任务套件;Figure 的 Helix 从未出现在任何公开基准上。不同的机器人、相机、物体集合、任务定义、初始状态分布和随机种子,使得跨论文比较基本没有意义(见[开放问题](open-problems.md) §6)。
- **样本小、无统计。** PhAIL 对 13 篇真机 VLA 论文(2023–2025)的调查发现,每个实验条件的典型样本量是 10–20 次试验,而且**13 篇中没有一篇报告置信区间或配对显著性检验**(截至 2026-05)。它指出的唯一严谨例外——TRI 的 LBM 研究(每条件真机 N=50 / 仿真 N=200,配对精确检验)——不在这 13 篇"标准做法"论文之列。
- **饱和掩盖了停滞。** ICLR 2026 的 VLA 研究综述(Reuss)发现 LIBERO/SIMPLER/CALVIN 主导了论文评测且"基本已被解决"——"展示 99% 对 98% 没有太大意义";有意思的失败(零样本、开放世界)恰恰发生在论文很少去评测的地方。
- **分数掩盖了坏行为。** LIBERO-Plus(2025-10)显示 SOTA VLA 在适度扰动下从约 95% 跌到 30% 以下,对相机视角和机器人初始状态最为敏感——并发现许多模型**完全无视语言指令**,靠轨迹记忆取得成功。
- **连评测框架本身都互相矛盾。** vla-eval 审计(2026-03)发现,即便是文档完善的基准也把关键细节留在暗处——语义过载的终止标志、隐藏的动作归一化统计量——每一项都是重实现之间悄悄扭曲分数的来源(单一论文)。
- **仿真与真机的相关性只是部分成立。** SimplerEnv 证实(仿真和真机各约 1,500 个评测回合),精心"视觉匹配"的仿真分数与 Google Robot 和 WidowX 装置上的真机表现强相关——但仅限这些装置;真实到仿真(real-to-sim)的泛化基准(RobotArena ∞、REALM)正试图扩展这一结论。
- **这场危机已进入主流视野(截至 2026-07)。** Stephen Witt 在《纽约客》的文章("Are Humanoid Robots Ready to Be Deployed?",2026-07-06 期)转述工业机器人从业者的看法:该领域"没有衡量进展的标准化基准",那些惊人特技的视频"往往是从几百条素材里挑出来的"。Witt 的现场见闻与之吻合:1X 流畅的 Neo 厨房演示是 VR 遥操作(teleoperation)的("一个提线木偶"),1X 干脆拒绝展示任何自主运行,而一台由 Skild 驱动的 Unitree 能处理直立的杯子,杯子一放倒就手足无措——在演示者自选构型上测出的成功率,对扰动情形几乎说明不了什么。

## 主要基准对比

| 基准 | 衡量什么 | 具身形态 | 仿真/真机 | 状态(截至 2026-07) |
|---|---|---|---|---|
| **LIBERO**(UT Austin,2023) | 130 项桌面操作任务;标准评测 = 4 个 10 任务套件(Spatial/Object/Goal/Long) | Franka(仿真) | 仿真(robosuite/MuJoCo) | **已饱和**:OpenVLA-OFT 平均 97.1%;π0.5-LIBERO 接近天花板;现在只是个健全性检查 |
| **LIBERO-Plus**(OpenMOSS/复旦,2025-10) | 鲁棒性:7 个扰动维度(布局、相机、机器人初始状态、语言、光照、背景、噪声),21 个子因素 | Franka(仿真) | 仿真 | 活跃;最佳报告平均约 81%(VLA-GSE,2026-05),对比原版 LIBERO 上的约 95% |
| **CALVIN**(2022) | 语言条件的长时程任务链(ABCD→D) | Franka(仿真) | 仿真 | 接近饱和(ICLR 2026 综述) |
| **SimplerEnv / SIMPLER**(UCSD Hao Su 实验室 + Google,2024) | Google Robot 和 WidowX/Bridge 评测的真实到仿真复刻;视觉匹配 + 变体聚合 | Google Robot、WidowX | 仿真(真机代理) | 广泛使用;顶级模型分数聚集在高位;主要价值是便宜的回归测试 |
| **RoboCasa365**(UT Austin/NVIDIA,ICLR 2026;arXiv 2026-03) | 365 项家务任务,2,500 个厨房,3,200+ 物体;多任务、预训练、终身学习;2,200+ 小时演示,500k+ 条轨迹 | 移动操作机器人(仿真) | 仿真(RoboCasa/robosuite) | 新基准,远未饱和;已集成 LeRobot |
| **BEHAVIOR-1K**(Stanford SVL,2024→) | 1,000 项长时程家庭活动(平均 6.6 分钟),双臂 + 移动;BDDL 目标谓词 | 移动双臂(仿真) | 仿真(基于 Isaac Sim 的 OmniGibson) | 很难:NeurIPS 2025 挑战赛(50 任务、10k 演示、18 支队伍)冠军 q-score 仅约 26%;2026 挑战赛扩到 100 任务 / 20k 演示(结果 2026-11 揭晓) |
| **MolmoSpaces-Bench**(Ai2,2026-02) | 通用策略在受控单因素变化下的泛化;230k+ 场景、130k+ 物体、42M 抓取;模拟器无关(MuJoCo/Isaac/ManiSkill) | 机械臂 + 导航(仿真) | 仿真(+ 真实世界验证研究) | 新;NVIDIA 宣称 GR00T N2 排名第一(2026-03,公司口径) |
| **RoboArena**(DROID 联盟,2025-06) | 众包的双盲成对 A/B 比较通用策略;评测者自由选择任务/场景;偏好聚合排名 | Franka(DROID 装置) | **真机**,7+ 家机构 | 实时排行榜;发布论文含 600+ 成对回合;最接近机器人版 Chatbot Arena 的东西 |
| **AutoEval**(UC Berkeley,2025) | 全天候自主真机评测:学习得到的成功分类器 + 复位策略;公开任务队列 | WidowX(Bridge 装置) | **真机** | 在线运行;站点/任务少,但几乎零人力 |
| **RoboChallenge Table30**(Dexmal + Hugging Face 等,2025-10) | 30 项桌面任务(插装、备餐、工具使用),在运营方托管的真机上执行 | UR5、Franka、ARX5、ALOHA | **真机**(远程、集中式) | 80,000+ 次真机执行,20+ 个模型排名;Table30 于 2026-05-27 退役,已宣布 Table30 v2 |
| **GM-100 /"Great March 100"**(RHOS:上海交大/SII + 蚂蚁集团,2026-01) | 由人-物交互原语构成的 100 项注重细节的任务;成功率 + 部分成功 + 动作误差;每任务每平台 130+ 条演示 | Agilex Cobot Magic、Dobot Xtrainer(计划扩展更多) | **真机** | 极其残酷:最佳平均成功率约 17%(LingBot-VLA,自报);是演示视频的解毒剂 |
| **VLA-REPLICA**(2026-05) | 用现成零件搭建的低成本物理基准,专为跨实验室复制设计 | 小型机械臂套件 | **真机**(可复制) | 新(采用情况未证实) |
| **ERQA**(Google DeepMind,2025-03) | 400 道多选 VQA 题:空间/轨迹/动作/任务推理、状态估计、指点、多视角 | 无(VLM 考卷) | 都不是(图像+文本) | "具身推理"的活跃标准;后续诊断版 ERQA-Plus 于 2026-06 发布 |
| **EIbench"求索"**(中国电子技术标准化研究院 CESI,2025-11) | 有官方背景的具身智能评测,纳入中国 HEIS 2026 标准框架 | 多种 | 混合 | v1 已发布;配套的 CAICT 行业基准测试标准 2026-06-01 生效 |

## 仿真基准:饱和与鲁棒性纠偏

- **LIBERO** 之所以成为该领域的默认记分卡,是因为它便宜、脚本化、可比较——恰恰是真机机器人学缺乏的属性。到 2025 年,那些"配方论文"(OpenVLA-OFT 仅靠解码方式的改动就从 76.5% 提到 97.1%)表明 LIBERO 分数衡量的更多是微调配方而非能力;前沿实验室仍把它(π0.5-LIBERO 检查点)当健全性检查来引用。
- **鲁棒性浪潮**(2025-10→):LIBERO-Plus、LIBERO-PRO 和 LIBERO-Para(改写鲁棒性,2026-03)都对这个已饱和的基准施加扰动并报告大幅下跌——由此确立:在固定场景上的聚合成功率不只是粗糙,而是一个具有误导性的统计量。
- **改为扩大难度**:RoboCasa365(365 任务/2,500 个厨房)和 BEHAVIOR-1K(1,000 项活动,NeurIPS 2025 冠军 q-score 约 26%)通过任务数量、时程和移动性重新引入提升空间;MolmoSpaces-Bench 通过控制变量的泛化扫描重新引入难度。the-decoder 把 BEHAVIOR-1K 说成机器人学未来的 ImageNet 只是愿景而非事实——纯仿真的长时程分数仍缺乏经证明的真实世界相关性(见[仿真](simulation.md))。
- **真实到仿真评测**是折中路线:SimplerEnv(在两套装置上验证了相关性)、RobotArena ∞(把真实视频转换到仿真中做 OOD 测试,2025-10)、REALM(2025-12)。悬而未决的问题是,这种相关性在富接触和长时程任务上是否成立——而这正是仿真物理最薄弱的地方。

## 真机评测:三种相互竞争的模式

- **联邦式竞技场(RoboArena)。** 分布在 7+ 家学术机构的评测者在 DROID Franka 装置上进行双盲成对比较,自由选择任务;偏好聚合产生的排名,按发布论文(CoRL 2025)所示,比集中式单实验室评测更准确、更抗操纵。弱点:单一具身形态类别,学术级吞吐量。
- **集中式评测即服务(RoboChallenge)。** 上传一个策略,由专职实验室按固定协议在真实的 UR5/Franka/ARX5/ALOHA 硬件上执行——2025-10 以来已执行 80,000+ 次。还催生了一起值得注意的透明化事件:Spirit AI 的 **Spirit v1.5** 登顶排行榜后开源了权重 + 评测代码(2026-01-12),明确为了让结果可被独立验证。弱点:对单一站点的信任、成本、基准更迭(Table30 → v2,2026-05)。
- **自主评测站(AutoEval)。** Berkeley 针对评测人力问题的答案:基础模型成功分类器加上学习得到的复位策略,让 WidowX 工作站全天候持续评测;结果与人工评测的真值高度吻合(论文声称)。弱点:只适用于可复位的桌面任务。
- **硬核任务集(GM-100)。** RHOS(上海交大/SII 联合蚂蚁集团 xbench 团队)策划了 100 项注重细节的任务,配固定演示和受控协议(一次部署动用 25 台机器人、约 22,500 次试验);2026 年最好的通用 VLA 平均成功率约 17% / 部分成功率约 35%——这是对抗演示视频通胀时被引用最多的清醒数字(模型厂商在第三方协议上自报)。
- **以竞赛为评测:** AGIBOT World Challenge 2026(ICRA,来自 27 个国家的 526 支队伍)把最终计分从仿真改为闭环真机测试——一次具有象征意义的文化转变(见[版图:中国](landscape-china.md))。

## 具身推理基准(无需机器人)

- **ERQA**(随 Gemini Robotics 发布,2025-03):400 道图文交错的多选题,覆盖空间/轨迹/动作/任务推理、状态估计、指点、多视角——测试的是技术栈中的 VLM 层,而非运动控制。Gemini Robotics-ER 1.5 宣称在含 ERQA、Point-Bench、RefSpatial 在内的 15 个具身推理基准上综合领先(公司口径)。
- **ERQA-Plus**(2026-06):对具身推理失败模式的诊断性分解(单一论文,采用情况未证实)。
- **RoboBench**(2025-10):评估多模态大模型充当"具身大脑"的能力——规划、可供性、故障诊断(单一论文)。
- 注意:具身推理高分明显不会迁移到控制能力——那些鼓吹 ERQA 夺冠的报告同时承认精细操作仍未解决;应把这些基准当作先修课考试,而非能力证书。

## 工业指标:吞吐量、干预、几个 9

已部署机器人的运营方基本无视学术成功率,他们跟踪的是:

- **吞吐量**:每小时拣选/周转箱/包裹数或节拍时间。Figure 报告在物流场景中,随着训练数据增多,单包裹节拍时间从 6.84 s 降到 4.31 s(公司,2025);Agility 的 Digit 在 GXO Flowery Branch 用约 16 个月完成了**搬运 100,000 个周转箱**(2025-11)——这是已披露的最大人形机器人工作量。厂商不公布相对于人类基线(约)的每小时拣选数;分析师估计当前人形机器人的吞吐量远低于人类(未证实)。
- **干预率 / 自主性**:每小时(或每任务)干预次数乘以人力成本是 ROI 杀手——例如在 5% 干预率、每次修复 30 s 的情况下,一名 $30/h 的监督员在维护成本之前就给每台机器人增加约 $1.50/h(分析师推算,未证实)。Physical Intelligence 的 π*0.6 评测就倚重这种框架:多小时不间断运行(浓缩咖啡服务 5:30am–11:30pm,约 18 小时),按真实时钟跟踪吞吐量与成功率,而不是按试验批次(公司口径)。
- **可靠性"几个 9"**:实验室基准止步于 95–99%;客户把 99% 定价为失败——无人值守运行隐含要求 99.9%+(见[开放问题](open-problems.md) §4)。截至 2026-06,没有任何人形机器人厂商公布 MTBF、正常运行时间或干预率数据;运行时间披露仅限于充电比(Digit 约 2:1 工作:充电,目标 4:1+)。
- 这些运营指标与学术基准之间的鸿沟本身就是危机的一部分:尚无任何公开基准对长时自主、干预或数小时内的性能衰减打分——而这些正是采购方真正购买的维度(RoboChallenge 的长时程任务和 PI 的马拉松运行是最接近的近似)。
- **遥操作是未披露的干预通道(截至 2026-07)。** Witt 在《纽约客》的报道记录了全行业名义上自主的系统背后都有远程人类——Waymo 在菲律宾的职业"飞行员"、日本 7-Eleven 的 VR 远程补货、1X 让遥操作员坐在其 AI 团队旁边(Neo 耳机上的光环变色以提示远程控制;1X 在遭到客户反弹后在营销中淡化了遥操作,但并未放弃)。Jim Fan(NVIDIA,2025 年末,文中引述):"照看这些机器人需要一整个运营团队。错误是不可逆且不可原谅的。"没有任何厂商报告每自主小时对应的遥操作小时数——这一披露缺口叠加在上述缺失的 MTBF/干预率数据之上。

## 谁在运营什么(截至 2026-07)

| 排行榜 / 基准 | 主理方 | 类型 |
|---|---|---|
| LIBERO(+ 社区变体) | UT Austin(原版);LIBERO-Plus 由 OpenMOSS/复旦维护 | 学术,各论文自行运行 |
| SimplerEnv | UCSD(Hao Su 实验室)+ Google 合作者 | 学术,自行运行 |
| RoboCasa365 | UT Austin + NVIDIA(Yuke Zhu);Hugging Face LeRobot 分发 | 学术/企业混合 |
| BEHAVIOR-1K + 年度挑战赛 | Stanford SVL(李飞飞、Jiajun Wu) | 学术,NeurIPS 挑战赛 |
| MolmoSpaces-Bench | Ai2(Allen Institute) | 非营利实验室,开放生态 |
| RoboArena 排行榜 | DROID 学术联盟(Berkeley/Stanford 牵头,7+ 所大学) | 联邦式学术,在线站点 |
| AutoEval 评测站 | UC Berkeley RAIL | 学术,公开队列 |
| RoboChallenge(Table30 → v2) | Dexmal + Hugging Face 等 | 创业公司 + 社区,在线站点 |
| GM-100 | RHOS(上海交大/SII)+ 蚂蚁集团 xbench | 学术 + 企业(中国) |
| ERQA | Google DeepMind | 企业,开放 GitHub |
| EIbench"求索" | 工信部下属 CESI(中国) | 国家标准机构 |

## 2026 年会收敛吗?

- **推动收敛的力量:** RoboArena 的联邦在扩大且获得厂商引用(NVIDIA 在 2026-03 为 GR00T N2 引用了 RoboArena 和 MolmoSpaces 排名——这是前沿厂商第一次拿第三方机器人基准名次做营销);Hugging Face 正把 LeRobot 接入 RoboCasa365 和 RoboChallenge,给开源模型一个默认记分板;中国在自上而下地标准化(EIbench v1 于 2025-11 发布;CAICT 牵头的具身智能基准测试行业标准,40+ 家起草单位,2026-06-01 生效),这可能让一个国家级基准成为全球最大机器人市场事实上的准入门槛(见[安全与监管](safety-regulation.md))。
- **反对收敛的力量:** 具身形态碎片化(Franka 竞技场的名次对[人形机器人](humanoid-robots.md)几乎说明不了什么);前沿实验室最好的模型是闭源的且缺席公开排行榜(截至 2026-07 的 Helix、Gemini Robotics VLA、π0.6/0.7);基准更迭(Table30 约 7 个月后退役);以及只报告自己能赢的基准这一结构性激励。
- **2026 年的现实终局:** 一个组合,而非一个标准——饱和的仿真套件充当回归测试,一两个在线真机竞技场负责通用模型排名,硬核任务集(GM-100、BEHAVIOR)提供提升空间,而运营指标(吞吐量/干预/几个 9)是商业上的最终真值。"ImageNet 时刻"尚未到来(此处作为共识观点写下;没有任何一手来源作相反主张)。

## 来源

- https://arxiv.org/abs/2510.13626 — LIBERO-Plus:7 个扰动维度,95%→<30% 的跌幅,无视语言指令的发现
- https://mbreuss.github.io/blog_post_iclr_26_vla.html — ICLR 2026 VLA 综述:LIBERO/SIMPLER/CALVIN 的主导地位与饱和论断
- https://openvla-oft.github.io/ — OpenVLA-OFT 在 LIBERO 上 76.5%→97.1%;配方对能力的证据
- https://arxiv.org/pdf/2405.05941 — SIMPLER/SimplerEnv:仿真和真机各约 1,500 个评测回合,视觉匹配相关性
- https://arxiv.org/abs/2506.18123 — RoboArena 论文(CoRL 2025):DROID,7 家机构,600+ 双盲成对回合
- https://robo-arena.github.io/ — RoboArena 实时排行榜网站
- https://arxiv.org/abs/2503.24278 — AutoEval:自主全天候真机评测,WidowX 工作站,公开队列
- https://arxiv.org/abs/2510.17950 — RoboChallenge 技术报告:Table30,UR5/Franka/ARX5/ALOHA,集中式真机评测
- https://robochallenge.ai/news — 80,000+ 次执行,20+ 个模型,Table30 于 2026-05-27 退役,Table30 v2
- https://www.prnewswire.com/news-releases/robochallenges-top-ranked-embodied-ai-model-goes-open-source-challenging-clean-data-collection-paradigm-302658247.html — Spirit AI 的 Spirit v1.5 在 RoboChallenge 排名第一,2026-01-12 开源
- https://arxiv.org/html/2601.11421v1 — GM-100 论文:100 项任务,RHOS/上海交大/SII/蚂蚁集团,平台,SR/PSR 指标
- https://www.rhos.ai/research/gm-100 — GM-100 网站:每任务 130+ 条演示、排行榜、平台路线图
- https://www.marktechpost.com/2026/01/29/ant-group-releases-lingbot-vla-a-vision-language-action-foundation-model-for-real-world-robot-manipulation/ — LingBot-VLA 的 GM-100 成绩(约 17.30% SR / 35.41% PSR),3 个平台各 130 条演示/任务
- https://arxiv.org/abs/2601.18692 — LingBot-VLA 论文:4 个商业平台共 25 台机器人,22,500 次试验的受控协议,对比 π0.5/GR00T N1.6/WALL-OSS
- https://arxiv.org/abs/2605.06175 — VLA-GSE:LIBERO-Plus 零样本平均 81.2%(截至 2026-05 的最佳报告)
- https://arxiv.org/abs/2603.04356 — RoboCasa365(ICLR 2026):365 项任务,2,500 个厨房,2,200+ 小时演示
- https://arxiv.org/abs/2403.09227 — BEHAVIOR-1K:1,000 项活动,OmniGibson
- https://behavior.stanford.edu/challenge/index.html — BEHAVIOR 挑战赛页面(现已显示 2026 届:100 任务、20k 演示;2025 届见存档)
- https://robot-learning-collective.github.io/winning-behavior-1k-challenge.html — 冠军方案 q-score 约 26%,18 支队伍
- https://the-decoder.com/behavior-1k-is-set-to-become-for-robotics-what-imagenet-was-for-computer-vision/ — "机器人学的 ImageNet"之说(愿景性质)
- https://allenai.org/blog/molmospaces — MolmoSpaces 生态:230k 场景、130k 物体、42M 抓取,MolmoSpaces-Bench
- https://arxiv.org/html/2602.11337v2 — MolmoSpaces 论文:模拟器无关的基准,受控变量
- https://github.com/embodiedreasoning/ERQA — ERQA:400 道多选题、类别划分、DeepMind 发布
- https://arxiv.org/html/2606.17639v1 — ERQA-Plus 诊断基准(2026-06)
- https://deepmind.google/blog/gemini-robotics-15-brings-ai-agents-into-the-physical-world/ — ER 1.5 宣称在 15 个具身推理基准上达到 SOTA
- https://arxiv.org/abs/2605.20774 — VLA-REPLICA:低成本可复制的真实世界基准
- https://arxiv.org/pdf/2605.29710 — PhAIL:13 篇论文的调查(典型 n=10–20,零置信区间),分布式方法学
- https://arxiv.org/html/2603.13966v1 — vla-eval 评测框架:隐藏的归一化/终止陷阱,配置锁定的可复现性
- https://arxiv.org/html/2510.23571v1 — RobotArena ∞:真实到仿真的转换基准测试
- https://nvidianews.nvidia.com/news/nvidia-and-global-robotics-leaders-take-physical-ai-to-the-real-world — NVIDIA 宣称 GR00T N2 在 MolmoSpaces + RoboArena 排名第一(2026-03,公司口径)
- https://sesec.eu/2026/04/01/chinas-first-standards-system-for-humanoid-robots-and-embodied-intelligence/ — EIbench"求索"(CESI,2025-11)纳入 HEIS 2026 框架
- https://news.cgtn.com/news/2026-03-27/China-releases-first-industry-standard-for-embodied-intelligence-1LQAZmMXmtW/p.html — CAICT 牵头的具身智能基准测试行业标准,2026-06-01 生效
- https://roboticsandautomationnews.com/2025/11/24/agility-robotics-digit-humanoid-passes-100000-tote-milestone-in-live-gxo-implementation/96877/ — Digit 在 GXO 达成 100,000 周转箱里程碑(2025-11)
- https://www.figure.ai/news/scaling-helix-logistics — Figure 物流节拍时间指标(6.84→4.31 s/包裹)
- https://blog.robozaps.com/b/roi-of-humanoid-robots — 干预率成本推算、与人类吞吐量对比的估算(分析师,未证实)
- https://www.pi.website/blog/pistar06 — π*0.6 的马拉松式评测风格(多小时吞吐量/成功率跟踪)
- https://www.globenewswire.com/news-release/2026/05/13/3293715/0/en/Global-Showdown-526-Teams-from-27-Countries-Compete-in-the-AGIBOT-WORLD-CHALLENGE-ICRA-2026-Online-Round.html — AGIBOT World Challenge 规模;最终计分转向真机
- https://www.newyorker.com/magazine/2026/07/06/are-humanoid-robots-ready-to-be-deployed — Stephen Witt(2026-07-06 期):"没有标准化基准"/演示视频出自数百条素材、遥操作的 1X Neo 演示、自主外衣下的遥操作模式、Jim Fan 的"照看"引语(有付费墙;经 2026-07-03 的 Wayback 快照完整阅读)
