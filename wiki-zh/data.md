---
title: 机器人数据难题
slug: data
updated: 2026-07-04
confidence: verified
lang: zh
source: ../wiki/data.md
---
> 机器人领域没有互联网规模的语料库:LLM 用数万亿网络 token 训练,而机器人动作必须被人为制造出来——通过遥操作(teleoperation)、手持采集设备、第一人称人类视频或仿真。截至 2026-07,领域内最大的开放真实机器人数据集约为 100–200 万条轨迹(Open X-Embodiment、AgiBot World),而已披露的最大专有语料库是 Generalist AI 的 270,000+ 小时(截至 2025-11 以每周约 1 万小时的速度增长)。2025–2026 年首次出现了可信的机器人数据缩放定律(scaling law)证据——环境/物体多样性上的幂律(ICLR 2025)、原始预训练小时数上的幂律(GEN-0)、第一人称人类视频上的幂律(NVIDIA EgoScale)——由此引发了建设"数据工厂"的资本竞赛:Figure×Brookfield、Apptronik 的 Robot Park、Scale AI 的 Physical AI Data Engine,以及中国 40 多个政府支持的采集中心。

## 为什么数据是瓶颈

- 语言和视觉模型可以从免费、被动积累的互联网语料库中起步;但不存在等价的"机器人动作互联网"。机器人轨迹(同步的视频 + 本体感知 + 动作)必须刻意生产,每小时都有边际成本。
- 全球约有 400 万台工业机器人在运行(IFR 存量估计),但几乎没有一台在记录可用于训练的数据——硬件存在,数据却不存在。
- 共识框架(由 NVIDIA 的 GR00T"数据金字塔"推广)是三层混合:**网络与人类视频**(海量、无动作标签)→ **合成/仿真数据**(廉价,存在模拟到现实(sim2real)差距)→ **真实机器人遥操作**(金标准动作标签,昂贵且缓慢)。前沿实验室现在在三层上联合训练;参见 [VLA 模型](vla-models.md)与[世界模型](world-models.md)。
- 成本锚点:据报道高质量遥操作数据成本从约 $340/小时(2024 年初)降至约 $136/小时(2025 年 Q4),得益于设备与流程的成熟(未证实,单一行业报告来源)。
- 数据策略如今是实验室之间的首要竞争轴——可以说比架构更重要;参见[最新进展](state-of-the-art.md)与[投资](investment.md)。

## 采集方式的权衡

| 方式 | 动作标签 | 吞吐量 / 成本 | 弱点 | 代表案例 |
|---|---|---|---|---|
| 机器人遥操作(主从式、VR) | 精确的机器人动作 | 每位操作员约 35 条演示/小时;设备 $20–30k(ALOHA 级) | 慢、受操作员限制、绑定具体机身 | ALOHA/ALOHA 2、Mobile ALOHA、DROID(Quest 2)、AgiBot World |
| 手持/便携采集 | 末端执行器位姿 + 夹爪(SLAM 恢复) | 约 111 条演示/小时(约为遥操作的 3 倍,UMI) | 无力觉感知;需重定向到机械臂 | UMI、FastUMI、DexUMI、ActiveUMI |
| 第一人称人类视频(带仪器) | 仅手部位姿(经重定向) | 被动、可穿戴;随人力规模扩展 | 具身差距(人手 ≠ 夹爪),无动作标签 | EgoDex(Vision Pro)、EgoMimic(Aria)、Tesla 相机装备、Figure Go-Big |
| 网络/人类视频(无仪器) | 无(伪标注) | 几乎免费,互联网规模 | 监督信号最弱;视角/具身不匹配 | Ego4D、GR00T/Helix 流程中的 YouTube 预训练 |
| 仿真 / 合成 | 完美的真值 | 11 小时生成 78 万条轨迹(Isaac 上的 DexMimicGen) | 模拟到现实差距、资产/场景多样性受限 | MimicGen、DexMimicGen、Isaac Lab;参见[仿真](simulation.md) |
| 神经生成("梦境") | 来自视频模型的伪动作 | 受 GPU 限制,完全无需物理设备 | 物理幻觉,需要过滤 | NVIDIA DreamGen、GigaBrain-0;参见[世界模型](world-models.md) |

## 遥操作与手持采集

- **ALOHA / ALOHA 2 / Mobile ALOHA**(Stanford/Google DeepMind,2023–2024):开源双臂主从式设备,每工位约 $20–30k;成为事实上的学术标准,也是中国数据中心设备的模板。Mobile ALOHA 显示,将移动操作数据与静态 ALOHA 数据集联合训练,可在某些任务上把成功率提升多达约 90 个百分点(论文口径)。
- **UMI(Universal Manipulation Interface)**(Stanford/Columbia,2024):手持夹爪 + 腕部 GoPro 鱼眼相机;SLAM 恢复末端执行器轨迹,因此采集时不需要机器人。每条演示约 30 秒(约 111 条/小时,对比遥操作约 35 条/小时);策略可在 UR5e 和 Franka 机械臂间零样本迁移。到 2025–2026 年衍生出庞大的后续家族(FastUMI、面向灵巧手(dexterous hand)的 DexUMI、ActiveUMI)。
- **VR 遥操作**是全身人形机器人的标配:Quest/Vision Pro 头显加动作重定向(DROID、AgiBot、中国训练中心以及大多数[人形机器人](humanoid-robots.md)公司在用)。Apple Vision Pro 的设备端手部追踪也支撑了 EgoDex 式的纯人类采集。
- 人体工学/经济学经验法则(截至 2026):一名熟练遥操作员每小时产出约 20–50 条可用轨迹;国家级项目因此雇佣数百名全职"数据采集员",每天将同一任务重复数百次(中国中心已有记录;Rest of World,2026)。
- **自动驾驶先例——遥操作即训练数据**:Waymo 在其 2025 年缩放定律研究中使用了**超过 500,000 小时的真实驾驶数据**(Waymo 官方博客,2025-06;Witt 的《纽约客》文章引用了同一个"至少 50 万小时"驱动其驾驶模型的数字),其远程人类"驾驶员"(在菲律宾工作的遥操作员)同时也是训练数据来源。1X 在家庭中运行同样的飞轮:遥操作"Expert Mode"会话反哺模型训练——"这对我们来说也是有用的数据"(CEO Bernt Børnich,据 Witt)——参见[数据铸造厂](data-foundry.md)与[开放问题](open-problems.md)。

## 第一人称人类视频

- 论点:人类是最便宜的"机器人"——录制人们做任务的第一人称视频,然后用重定向或联合训练弥合具身差距。2025–2026 年,这一思路从研究想法变成了多家实验室的主要策略。
- **EgoDex**(Apple,2025-05):829 小时的 Vision Pro 第一人称视频,配有成对的 3D 手部/手指关节追踪,194 个桌面任务——发布时最大的灵巧操作数据集(论文口径)。
- **Ego4D**(Meta):约 3,670 小时的通用第一人称日常活动;是感知骨干网络的常用素材,但没有操作标注。**EgoMimic**(Georgia Tech,2024)使用 Project Aria 眼镜联合训练人类 + 机器人数据,报告相对纯机器人数据获得 34–228% 的任务性能提升。
- **NVIDIA EgoScale / GR00T N1.7**(早期访问 2026-04):在 20,854 小时、覆盖 20+ 任务类别的第一人称人类视频上预训练;NVIDIA 报告了灵巧性的对数线性缩放定律——从 1 千小时扩展到 2 万小时使平均任务完成率翻倍以上——灵巧手任务(注射器操作、卡片分类、叠衬衫)主要从人类视频学得,训练环节中没有机器人(公司口径)。
- **Figure "Project Go-Big"**(2025-09 宣布):与 Brookfield 合作(100,000+ 住宅单元、5 亿平方英尺办公楼、1.6 亿平方英尺物流设施),在真实家庭中被动采集第一人称人类视频;Figure 报告 Helix 在 100% 第一人称人类视频训练后,能根据语言指令在杂乱家庭环境中导航——人类到机器人的零样本迁移(公司口径);参见[人形机器人](humanoid-robots.md)。
- **Tesla Optimus** 于 2025 年年中从动捕服/遥操作转向纯视觉策略:工人佩戴带五个摄像头的头盔加背包装备,记录日常任务,复刻 FSD 的相机优先打法(据报道发生在 Ashok Elluswamy 接管该项目之后,2025-06)。
- **Neura Robotics(德国)**以工业规模运行动捕服变体:**1,000 多名穿动作捕捉服的产业工人**生成人形机器人训练数据(据 Witt,《纽约客》2026-07-06 期;为公司项目,规模未经独立核实)。CEO David Reger 将其定位为数据采集而非取代工作:"我们正在获得,呃,大量数据。"Witt 对整个路线的上限估计:"即使地球上所有人都穿上动作捕捉服,也需要几十年才能生成训练 ChatGPT 所用的数据量"——全人类动捕仍达不到 LLM 语料库规模,这正是各实验室将其与视频和仿真叠加使用的原因。
- 开放问题:人类视频缺乏机器人动作标签和力信号;相互竞争的桥接方案包括潜在动作模型(GO-1、GR00T)、手到夹爪重定向,以及联合训练。有一项报告结果:在联合训练设置中,1 小时的 Aria 人类数据贡献超过额外 1 小时的遥操作数据(未证实,单一来源)。

## 仿真与神经生成数据

- **MimicGen / DexMimicGen**(NVIDIA):自动将少量人类演示扩展为大规模仿真数据集;DexMimicGen 在 Isaac Sim 上用 11 小时生成 780,000 条轨迹(约合 6,500 小时人类当量),用于 GR00T N1 训练。
- **DreamGen / GR00T-Dreams**(2025):视频世界模型(world model)生成"神经轨迹"——机器人从未执行过的任务的逼真推演——再对动作进行伪标注;NVIDIA 报告与真实数据混合时约有 40% 的性能提升(未证实的公司/博客口径)。参见[世界模型](world-models.md)。
- 仿真数据在[运动控制](locomotion.md)领域占主导(Isaac Gym 级模拟器中的 RL 不需要演示),但对富接触操作而言仍是联合训练的补充而非替代——模拟到现实差距在[仿真](simulation.md)与[开放问题](open-problems.md)中有专门讨论。

## 开放数据集

| 数据集 | 规模 | 具身形态 | 备注 |
|---|---|---|---|
| **Open X-Embodiment (OXE)**(2023,持续增长) | 100 万+ 真实轨迹、500+ 技能、16 万+ 任务变体 | 22 种机器人类型 | 由 21 家机构合作从 60 个已有数据集汇集;RLDS 格式;是默认的 VLA 预训练语料库,但质量/格式高度不均 |
| **DROID**(2024) | 7.6 万条遥操作轨迹、350 小时、564 个场景、86 个任务 | Franka Panda(单一标准化设备) | 13 家机构、50 名采集员、12 个月;标定立体相机、1,417 个视角;单集多样性基准 |
| **AgiBot World**(2024-12 α,2025 β) | >100 万条轨迹、2,976.4 小时、217 个任务、3,000+ 物体 | 100 台同构双臂 AgiBot G1 人形机器人 | 在 AgiBot 位于临港(上海)约 4,000 m² 的设施采集(数据见 arXiv:2503.06669 + Hugging Face 数据集卡);论文报告在其上预训练的策略在分布内与分布外均比 OXE 预训练高约 30%;是 GO-1 潜在动作模型的基础;IROS 2025 最佳论文入围 |
| **RoboMIND**(2024-12) | 10.7 万条轨迹、479 个任务、96 个物体类别 | 4 种具身形态,含天工(Tien Kung)人形机器人 | 北京 X-Humanoid 中心;统一平台,包含失败轨迹 |
| **RoboMIND 2.0**(2025-12) | 31 万条双臂轨迹、1,000+ 小时、1.2 万条触觉增强、2 万条移动操作 | 6 种异构具身形态 | 新增触觉与移动操作模态(论文口径) |
| **EgoDex**(Apple,2025-05) | 829 小时第一人称视频 + 3D 手部追踪、194 个任务 | 人手(Vision Pro) | 发布时最大的人类灵巧操作数据集 |
| **AIRoA 发布**(日本,2026-02 宣布) | 约 10,000 小时真实机器人多模态数据(RGB-D、力/力矩、语言) | 移动操作机器人(Toyota HSR 评测) | 以 LeRobot 格式发布,并在 ICRA 2026-06 举办全球 VLA 流水线竞赛 |
- Hugging Face 的 **LeRobot** 已成为社区标准的数据格式/工具层(截至 2026);NVIDIA 在 HF 上的 Physical AI 开放数据集报告 480 万+ 次下载(未证实)。
- 中国的生态(AgiBot World、RoboMIND、麒麟训练场产出)在原始轨迹数量上已与美国开放数据集持平甚至超越——参见[版图:中国](landscape-china.md)。

## 商业数据工厂

- **Generalist AI**(截至 2025-11):270,000+ 小时的真实世界操作数据,通过遍布数千个家庭/仓库的多家签约"数据铸造厂"合作伙伴以每周约 10,000 小时增长;以约 $2B 估值融资 $400M(2026-06 宣布;Radical Ventures 领投,累计融资 >$500M),用于扩展其 GEN-0 模型和数据引擎;参见[组织机构](organizations.md)。
- **Scale AI Physical AI Data Engine**(2025-09 扩展):其旧金山机器人实验室已记录 100,000+ 生产小时,外加全球贡献者;公开客户包括 Physical Intelligence、Generalist AI 和 Cobot;2026-03 的合作(在 GTC 宣布)将该引擎嵌入 Universal Robots 的 UR AI Trainer 主从套件(10 万+ 已安装工业机械臂构成采集机队)。
- **Apptronik Robot Park**(2026-06-30 宣布):位于 Austin 的 90,000 平方英尺人形机器人数据工厂——Apollo 2 机队在混合遥操作 + 自主模式下执行物流/制造/零售工作,为 Google DeepMind 的 Gemini Robotics 模型供数;在 Mercedes-Benz 和 GXO 设有卫星采集点。
- **Figure × Brookfield**(2025-09):把房地产组合当作数据集——在 10 万+ 住宅单元中被动采集第一人称人类视频(见上文)。
- **中国的政府支持中心**:到 2025-12 已宣布 40 多个政府背景的数据采集中心,2026 年初约二十来个投入运营(Rest of World)。旗舰项目:上海麒麟训练场(国家地方共建人形机器人创新中心 + 张江集团;据官方媒体约 4,600–5,000 m²,100+ 台异构人形机器人同时训练,2025-01 开放)和北京石景山中心(10,000+ m²,与乐聚机器人(Leju Robotics)共建;4 大类 16 个搭建场景)。UBTech 向三个省级数据中心售出 ¥566M(约 $80M)的人形机器人(截至 2025);工人每天将单一动作重复多达约 600 次。
- **Tesla**:完全自建;规模化的相机装备人类视频采集加 Optimus 机队数据(截至 2025-06 的策略转向)。
- 理念对比:美国实验室越来越押注人类视频 + 客户现场机队数据;中国押注补贴的集中式遥操作大厅。双方都在向混合金字塔收敛。

## 跨具身迁移

- **RT-X**(2023)是概念验证:在 OXE 的 22 种具身形态上训练一个模型产生了正迁移——RT-1-X 在代表性不足的实验室基准上比专用模型高约 50%,RT-2-X 在涌现技能评测上的成功率约为 RT-2 的三倍(论文口径)。
- **π0 / π0.5**(Physical Intelligence):π0.5 的混合数据结合了约 400 小时移动操作演示、多环境静态机器人数据、多样的跨具身实验室数据、高层语言子任务数据以及网络 VQA/图像描述——为在未见过的家庭中实现开放世界泛化设计的显式"课程"(截至 2025-04)。参见 [VLA 模型](vla-models.md)。
- **GR00T N1/N1.5/N1.7** 与 **GEN-0** 在异构具身形态上训练(GEN-0 在 6 自由度、7 自由度和 16+ 自由度半人形平台上评测)。
- 注意事项:简单地混合数据可能产生负迁移——OXE 不一致的视角、动作空间和质量是公认的拖累,而 AgiBot 相对 OXE 预训练约 30% 的优势表明,精心策划的同构数据可以胜过更大的异构语料库(单一团队口径)。动作空间统一化(潜在动作、末端执行器规范化、OXE-AugE 等增强工作)是 2026 年的活跃研究前沿。

## 缩放定律证据

| 研究 | 缩放的轴 | 报告的规律 | 注意事项 |
|---|---|---|---|
| **Data Scaling Laws in Imitation Learning**(清华等,ICLR 2025 口头报告;4 万+ 演示、1.5 万+ 次执行) | 环境与物体数量 | 环境/物体多样性上的幂律;每环境演示数会饱和(达到阈值后持平);4 名采集员一个下午的数据即可在新环境任务上达到约 90% 成功率 | 单任务策略、2 台机器人、仅限操作任务 |
| **GEN-0**(Generalist AI,2025-11) | 预训练小时数(27 万小时) | 下游误差满足 L(D) = (D_c/D)^α 幂律;约 7B 参数以下出现"骨化"——更大的模型更能吸收数据 | 公司技术博客,未经同行评审 |
| **NVIDIA EgoScale / GR00T N1.7**(2026-04) | 第一人称人类视频小时数(20,854 小时) | 灵巧性的对数线性缩放;1 千→2 万小时使平均任务完成率翻倍以上 | 公司口径,早期访问模型 |
| **Mobile ALOHA 联合训练**(2024) | 跨任务联合训练 | 与现有静态数据联合训练带来最多 +90 个百分点的成功率 | 小规模、特定任务 |
- 解读(截至 2026-07):现有证据支持"更多且更多样的数据可预测地有帮助",其中在小规模下**环境/物体多样性比原始轨迹数量更重要**,而在基础模型规模下原始小时数起主导作用。目前仍没有公认的计算最优"机器人版 Chinchilla"——数据配比(真实 : 人类视频 : 仿真)仍是各实验室的经验秘方;参见[开放问题](open-problems.md)。

## 开放问题

- 真实遥操作 : 人类视频 : 合成数据的什么比例在算力/资金上最优?每家实验室报告的配比都不同;没有一家发布完整的消融实验。
- 第一人称视频缩放定律(EgoScale、Go-Big)在富接触、依赖力觉的任务上是否成立?视频不携带触觉信号;触觉增强数据集(RoboMIND 2.0)是早期回应。
- 开放语料库能否跟上?专有与开放的差距在 2025–2026 年拉大:Generalist 的 27 万小时超过所有开放数据集之和;开放发布(AgiBot World、AIRoA)是对冲力量。
- 评测落后于采集:多数数据集论文只在自家任务上自报成功率;标准化的跨实验室基准仍很薄弱(参见[最新进展](state-of-the-art.md))。

## 来源
- https://arxiv.org/abs/2410.18647 — Data Scaling Laws in Imitation Learning(ICLR 2025 口头报告):环境/物体幂律、4 万条演示、约 90% 新环境成功率。
- https://generalistai.com/blog/nov-04-2025-GEN-0 — GEN-0:27 万+ 小时语料库、每周 +1 万小时、L(D) 幂律、7B 骨化阈值、数据铸造厂合作伙伴。
- https://www.therobotreport.com/generalist-raises-400m-to-scale-its-general-purpose-ai-models/ — Generalist 融资 $400M(2026-06 宣布)。
- https://www.bloomberg.com/news/articles/2026-06-04/nvidia-backed-robotics-startup-generalist-ai-valued-at-2-billion — Generalist $400M 轮次、约 $2B 估值,2026-06-04,Radical Ventures 领投,累计 >$500M。
- https://iclr.cc/virtual/2025/oral/31769 — ICLR 2025 对 Data Scaling Laws in Imitation Learning 的口头报告条目(确认口头报告身份)。
- https://umi-gripper.github.io/ — UMI:手持夹爪、每条演示约 30 秒(约 111 条/小时对比遥操作 35 条/小时)、跨平台零样本部署。
- https://proceedings.mlr.press/v270/fu25b — Mobile ALOHA:全身遥操作设备,联合训练最多带来 90 个百分点的提升。
- https://droid-dataset.github.io/ — DROID:7.6 万条轨迹、350 小时、564 个场景、86 个任务、13 家机构、Franka Panda + Quest 2。
- https://arxiv.org/html/2503.06669v4 — AgiBot World Colosseo:>100 万条轨迹、217 个任务、100 台双臂人形机器人、约 4,000 m² 临港设施、相对 OXE 预训练 +30%、GO-1。
- https://huggingface.co/datasets/agibot-world/AgiBotWorld-Beta — AgiBot World Beta 数据集卡:2,976.4 小时、>100 万条轨迹。
- https://arxiv.org/abs/2412.13877 — RoboMIND:10.7 万条轨迹、479 个任务、96 个物体类别、多具身遥操作基准。
- https://arxiv.org/abs/2512.24653 — RoboMIND 2.0:31 万条双臂轨迹、6 种具身形态、1,000+ 小时、触觉 + 移动操作。
- https://machinelearning.apple.com/research/egodex-learning-dexterous-manipulation — EgoDex:829 小时 Vision Pro 第一人称视频、194 个任务。
- https://ai.meta.com/blog/egomimic-project-aria-georgia-tech-ego4d-robotics-embodied-ai/ — EgoMimic/Project Aria 人类-机器人联合训练;Ego4D 背景。
- https://www.figure.ai/news/project-go-big — Project Go-Big:Brookfield 合作规模(10 万+ 家庭)、Helix 依靠 100% 人类视频的零样本导航(2025-09)。
- https://huggingface.co/blog/nvidia/gr00t-n1-7 — GR00T N1.7:20,854 小时第一人称预训练(EgoScale)、对数线性灵巧性缩放、1 千→2 万小时使完成率翻倍(2026-04)。
- https://arxiv.org/pdf/2503.14734 — GR00T N1:数据金字塔训练语料、MimicGen/DexMimicGen 合成数据、神经轨迹。
- https://developer.nvidia.com/blog/building-a-synthetic-motion-generation-pipeline-for-humanoid-robot-learning/ — Isaac/DexMimicGen:11 小时生成 78 万条仿真轨迹(约合 6,500 小时)。
- https://www.eweek.com/news/tesla-optimus-robot-training/ — Tesla 2025 年转向纯视觉相机装备人类数据采集;Optimus 领导层变动。
- https://scale.com/blog/physical-ai — Scale AI Physical AI Data Engine:10 万+ 生产小时,采集 + 标注技术栈。
- https://www.universal-robots.com/news-and-media/news-center/universal-robots-scale-ai-launch-imitation-learning-system-accelerate-ai-training-lab-to-factory/ — Scale × Universal Robots UR AI Trainer 合作。
- https://www.forbes.com/sites/johnkoetsier/2026/06/30/apptronik-announces-robot-park-a-90000-square-foot-humanoid-data-factory-teases-new-robot/ — Apptronik Robot Park:90,000 平方英尺 Austin 数据工厂、Apollo 3(2027)、DeepMind/Mercedes/GXO 站点。
- https://restofworld.org/2026/china-robots-training-centers-workers/ — 中国:已宣布 40+ 个政府数据中心、约二十来个运营、工人工作方式、UBTech ¥566M 销售额。
- https://www.chinadaily.com.cn/a/202501/23/WS67919d43a310a2ab06ea8c2e.html — 上海麒麟人形机器人训练场开放(2025-01)、4,600 m²、100+ 台机器人同时训练。
- https://english.news.cn/20250122/8da44371af8342ca84ee505914fd5fa6/c.html — 新华社关于麒麟:5,000+ m²、初期 100+ 台人形机器人、2025-01-21 启动。
- https://english.beijing.gov.cn/latest/news/202510/t20251009_4216190.html — 北京石景山中心:10,000+ m²、全国最大、4 大类 16 个场景、与乐聚机器人共建。
- https://www.airoa.org/updates/20260210/208/ — AIRoA 约 10,000 小时移动操作机器人数据发布(RGB-D、力/力矩、语言;LeRobot 格式)+ ICRA 2026 VLA 流水线竞赛、Toyota HSR 评测。
- https://www.pi.website/blog/pi05 — π0.5 训练配比:约 400 小时移动操作 + 多环境 + 跨具身 + 网络数据。
- https://robotics-transformer-x.github.io/ — Open X-Embodiment/RT-X:100 万+ 条轨迹、22 种具身形态、正迁移结果。
- https://www.roboticscenter.ai/state-of-robotics-2026 — 行业报告数据:遥操作成本下降($340→$136/小时)、LeRobot/NVIDIA 数据集采用情况(二手来源;引用处均标注未证实)。
- https://www.newyorker.com/magazine/2026/07/06/are-humanoid-robots-ready-to-be-deployed — Witt:Neura 1,000+ 名穿动捕服的工人(Reger 引语)、全人类动捕上限的框架、Waymo 遥操作驾驶员作为数据来源、1X Expert-Mode 即数据的引语(经 Wayback 快照阅读)。
- https://waymo.com/blog/2025/06/scaling-laws-in-autonomous-driving/ — Waymo 基于 500,000 小时真实驾驶数据的缩放定律研究(一手来源;佐证 Witt 的"至少 50 万小时")。
