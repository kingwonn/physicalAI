---
title: 学术实验室版图
slug: academic-labs
updated: 2026-07-04
confidence: verified
lang: zh
source: ../wiki/academic-labs.md
---
> 几十个大学实验室贡献了 Physical AI 领域绝大多数的思想、数据集、基准和创始人。美国的人才管线贯穿斯坦福(IRIS/Finn、SVL/李飞飞、REAL/Shuran Song)、伯克利(RAIL/Levine、BAIR)、CMU(Pathak 与 Gupta → Skild AI)、MIT(Tedrake ↔ 丰田研究院 TRI)、UT Austin(Zhu ↔ NVIDIA GEAR;Sentis → Apptronik)和华盛顿大学(Fox → NVIDIA → Ai2);中国的管线贯穿清华交叉信息研究院(IIIS)——到 2026 年已孵化三家机器人独角兽(Robotera、Galaxea、Spirit AI)——北京大学(Galbot、PsiBot)、上海人工智能实验室、哈工大(乐聚)与浙江大学(云深处 DEEP Robotics);欧洲的旗舰是 ETH Zurich 的 RSL(Hutter),其衍生公司从 ANYbotics 到被 Amazon 收购的 RIVR;韩国的 KAIST 孕育了 Rainbow Robotics(现由 Samsung 控股)和 Raion;日本东京大学 JSK 实验室诞生了 SCHAFT(2013 年被 Google 收购)。这个领域几乎每一件奠基性成果——ALOHA、Diffusion Policy、UMI、DROID、Open X-Embodiment、LIBERO、BEHAVIOR、legged_gym——都源自学术界,而主导的用人模式是"双重身份"教授:一边经营初创公司或企业实验室,一边保留教职。

## 为什么学术版图重要

- **学术界是 Google 人才大流散的上游。** 后来孕育了 Physical Intelligence、Figure 的 Helix 团队和 1X AI 团队的 Google Brain/DeepMind 机器人团队([关键人物](key-people.md)),本身就是由伯克利、斯坦福和 CMU 的博士项目输送的——下文这些实验室是该领域人才树不断再生的源头。
- **数据集和基准是学术界的主要杠杆。** 公司囤积机器人数据([数据](data.md));大学则公开发布。每一个被广泛使用的开放语料库(OXE、DROID)、遥操作(teleoperation)装置(ALOHA、UMI)、仿真基准(LIBERO、BEHAVIOR-1K、RoboCasa)和运动控制工具链(legged_gym/rsl_rl、RaiSim)都有一所起源大学。
- **"双重身份"教授是这个领域标志性的雇佣结构**(截至 2026-07):Levine(伯克利 + Pi)、Finn(斯坦福 + Pi)、Zhu(UT Austin + NVIDIA)、Pathak 与 Gupta(CMU + Skild)、Tedrake(MIT + TRI)、王鹤(北大 + Galbot)、陈建宇(清华 + Robotera)、朱秋国(浙大 + DEEP Robotics)、Hwangbo(KAIST + Raion)。人才池足够稀薄,以至于双方都不强迫做出选择。
- **企业对学术谱系的收编正在加速**:Google–SCHAFT(2013)、现代–Boston Dynamics(2021)、Samsung–Rainbow Robotics(2025-03 获批控股)、Amazon–Covariant 团队(2024-08)、Amazon–RIVR(2026-03)。

## 美国

| 实验室(机构) | 负责人(PI) | 标志性贡献 | 产业管线 |
|---|---|---|---|
| **IRIS,斯坦福** | Chelsea Finn | MAML;ALOHA/ACT + Mobile ALOHA 遥操作装置;DROID(13 家机构联合语料库);OpenVLA(与伯克利/TRI 合作) | Finn 联合创立 **Physical Intelligence**(2024);学生 Tony Zhao 与(REAL 实验室的)Cheng Chi 创立 **Sunday Robotics**;校友遍布 Pi 和 Google DeepMind |
| **SVL / HAI,斯坦福** | 李飞飞、吴佳俊 | ImageNet 遗产;**BEHAVIOR-1K** 基准 + OmniGibson(1,000 项家务活动;NeurIPS 挑战赛系列,2026 届:100 项任务/2 万条演示) | 李飞飞创立 **World Labs**(2024,Marble 世界模型(world model));博士谱系包括 Jim Fan(NVIDIA GEAR 联合负责人)和 Yuke Zhu |
| **REAL,斯坦福(原哥伦比亚大学)** | Shuran Song | **Diffusion Policy**(与 TRI 合作,RSS 2023)、**UMI** 手持夹爪——两者均为领域标准 | Song 于 2023 年从哥伦比亚大学转到斯坦福,学生 Cheng Chi 随行;Chi 联合创立 **Sunday Robotics**(CTO);与 TRI 深度合作 |
| **RAIL / BAIR,UC 伯克利** | Sergey Levine(RAIL);Pieter Abbeel;Ken Goldberg | SAC、离线强化学习、Open X-Embodiment/RT-X 联合牵头、OpenVLA;Dex-Net 抓取(Goldberg) | Levine 联合创立 **Pi**;Abbeel 联合创立 **Covariant**(→ Amazon,2024-08);Goldberg 联合创立 **Ambi Robotics** + **Jacobi Robotics**;博士/博士后大流散在各地任教(Finn→斯坦福、Pathak→CMU、A. Gupta→华盛顿大学、Kumar→CMU、高阳→清华) |
| **机器人研究所(RI),CMU** | Deepak Pathak、Abhinav Gupta(均为休假/双重身份) | 好奇心驱动强化学习、腿式机器人快速运动适应、自监督机器人学习;RI 是美国最古老的机器人系(1979)+ NREC 合同实验室 | Pathak 与 Gupta 创立 **Skild AI**(2023,匹兹堡)——估值超 $14B(2026-01);DARPA 城市挑战赛(Boss,2007)谱系哺育了自动驾驶产业([历史](history.md)) |
| **CSAIL / Leg Lab 遗产,MIT** | Russ Tedrake;Pulkit Agrawal;Sangbae Kim(仿生学);Daniela Rus(CSAIL 主任) | 欠驱动机器人学课程/经典教材;TRI **Large Behavior Models**;Mini Cheetah(第一台后空翻四足机器人);Improbable AI 的灵巧操作 + 运动控制强化学习 | Tedrake 是 **丰田研究院(TRI)** 高级副总裁(MIT–TRI 是美国最深度的实验室–企业联姻);Marc Raibert 的 Leg Lab → **Boston Dynamics**(1992);Sangbae Kim 加入 **Meta** 任其人形机器人("Metabot")项目的 Robotics Architect(2025-03;从 MIT 休假);Rus 联合创立 Liquid AI |
| **RSE / WEIRD,华盛顿大学** | Dieter Fox;Abhishek Gupta | 状态估计 → 机器人学习;Fox 在校园旁建立了 **NVIDIA 西雅图机器人实验室**(2017–2025) | Fox 于 2025-07 离开 NVIDIA 加入 **Ai2**,领导其机器人基础模型计划(MolmoAct 开放具身模型);Ai2 是 2026 年 NVIDIA GR00T 参考机器人合作伙伴 |
| **RPL / LARG / HCRL,UT Austin** | Yuke Zhu;Peter Stone;Luis Sentis | robosuite、**LIBERO**(与 Stone 合作)、**RoboCasa** 厨房级仿真;RoboCup 传统;全身控制 | Zhu 联合领导 **NVIDIA GEAR**(GR00T 产品线,[NVIDIA](company-nvidia.md));Stone 是 Sony AI 首席科学家;Sentis 的 HCRL 衍生出 **Apptronik**(2016,约 $5.3B,截至 2026-02) |
| **USC(RESL/ICAROS)** | Gaurav Sukhatme;Stefanos Nikolaidis;Erdem Bıyık;Maja Matarić(社交辅助机器人传统) | 多机器人系统、人机交互、面向机器人的 RLHF 等方向 | 稳定向 NVIDIA/Amazon 输送博士;暂无标志性衍生公司(截至 2026-07) |

- 佐治亚理工(Danfei Xu,斯坦福 SVL 校友)贡献了 **EgoMimic** 人类视频协同训练;UCSD 的 ARC Lab 是 GR00T 参考机器人合作伙伴——版图的第二梯队密集且仍在扩张。
- NVIDIA 于 2026-06-01 正式建立学术渠道:**Isaac GR00T 参考人形机器人**(Unitree H2 Plus 底盘、Sharpa Wave 触觉手、Jetson Thor)首批交付 Ai2、ETH Zurich、斯坦福机器人中心和 UCSD ARCLab,2026 年底起可从 [Unitree](company-unitree.md) 购买。

## 中国

| 实验室(机构) | 负责人(PI) | 标志性贡献 | 产业管线 |
|---|---|---|---|
| **交叉信息研究院(IIIS),清华**(姚期智创办) | 陈建宇;高阳;赵行(MARS Lab);许华哲(TEA Lab) | 模仿学习中的数据缩放定律(ICLR 2025 口头报告);强化学习 + 视觉-语言-动作模型(VLA)研究;IIIS 采用明确的孵化模式 | **Robotera**(陈建宇,2023,清华持股——公司口径);**Galaxea AI**(赵行联合创始人/首席科学家,前 Waymo);**Spirit AI**(高阳联合创始人/首席科学家,伯克利博士)——到 2026 年一个研究院孵化出三家独角兽 |
| **EPIC Lab,北京大学** | 王鹤 | 类别级位姿估计、GAPartNet 系列感知工作;兼任 BAAI 具身智能中心主任 | **Galbot**(2023):轮式双臂 G1,估值超 $2.8B,累计融资约 ¥5B(截至 2026-03),筹备港股 IPO([格局:中国](landscape-china.md)) |
| **人工智能研究院,北京大学** | 杨耀东 | 多智能体强化学习;NeurIPS 2022 灵巧操作挑战赛冠军;北大–PsiBot 联合实验室 | **PsiBot**(灵初智能):首席科学家杨耀东;天使轮/Pre-A 累计融资 ¥2B(截至 2025);Psi R0/R1 号称首个端到端基于强化学习的具身模型(公司口径) |
| **上海人工智能实验室——具身智能中心 / OpenRobotLab** | 庞江淼(研究负责人) | InternRobotics 技术栈、GRUtopia 城市级仿真、学习式运动控制(Hybrid Internal Model);国家背景的 EIbench 评测([评测](evaluation.md)) | 是国家实验室而非衍生公司工厂;向中国生态输出开放模型/基准;与 OpenDriveLab(港大)合作 |
| **上海期智研究院** | 姚期智创办(2020) | 桥梁型研究院,汇聚清华系具身智能研究者(高阳、许华哲等圈子) | 向同一个清华初创集群(Spirit AI 等)输送人才 |
| **哈尔滨工业大学(HIT)** | 机器人技术与系统国家重点实验室(1986 年建立) | 中国最早的机器人实验室之一;空间机械臂(天宫计划);2020 年起被列入美国实体清单 | **乐聚机器人**(2016,冷晓琨):Kuavo——首款 HarmonyOS 开源人形机器人(2023-12);$207M pre-IPO 轮(景林领投);共建北京石景山数据采集中心([数据](data.md)) |
| **浙江大学** | 朱秋国(控制学院) | 绝影(Jueying)四足机器人、悟空(Wukong)人形机器人;ZJUDancer 学生机器人足球队作为人才漏斗 | **DEEP Robotics(云深处)**(2017,朱秋国仍任副教授)——中国四足机器人第二,仅次于 Unitree;浙大宣称培育了杭州"六小龙"集群(DeepSeek、Unitree、DEEP Robotics……),不过 Unitree 的王兴兴并非浙大校友 |

- 中国模式与美国存在结构性差异:教授创始人保留教职**且**大学/国家基金持股(清华持股 Robotera;"大基金"投资 Galbot;国开资本投资 PsiBot),走 IPO 路径(科创板、港股)而非无限期的风险融资轮([投资](investment.md))。
- BAAI(北京)充当跨高校具身智能协调者(王鹤在经营 Galbot 的同时兼任其具身中心主任)。

## 欧洲

| 实验室(机构) | 负责人(PI) | 标志性贡献 | 产业管线 |
|---|---|---|---|
| **RSL,ETH Zurich** | Marco Hutter | ANYmal 四足机器人;执行器网络(Hwangbo,Science Robotics 2019);师生蒸馏式模拟到现实(sim2real);**legged_gym + rsl_rl**(社区标准的强化学习运动控制栈);与 NVIDIA 共同开发 Isaac Lab;DARPA SubT 夺冠机器人([运动控制](locomotion.md)) | **ANYbotics**(2016,累计融资超 $150M,截至 2024-12);**RIVR**/前 Swiss-Mile(Bjelonic,2023;Bezos 投资;**2026-03 被 Amazon 收购**);**Ascento**;**Flexion Robotics**;博士校友:Hwangbo(KAIST)、Mittal(ETH/NVIDIA 双聘);NVIDIA 在苏黎世附近设有机器人研究点 |
| **LASA / BioRob,EPFL** | Aude Billard;Auke Ijspeert | 示教学习经典(Billard);基于 CPG 的运动控制、蝾螈机器人(Ijspeert) | 更多是人才输出者而非衍生公司工厂;校友遍布欧洲高校和 DeepMind |
| **IAS,达姆施塔特工业大学(TU Darmstadt)** | Jan Peters | 策略搜索、运动基元;兼任 DFKI SAIROL 机器人学习部门负责人(2022 年起) | 欧洲机器人学习博士的"师范学院"——校友在全欧洲执掌教席(如 KIT 的 Gerhard Neumann) |
| **H2T,KIT** | Tamim Asfour | ARMAR 人形机器人家族(自约 1998 年持续开发,ARMAR-6/7)——欧洲历史最长的人形机器人平台 | 研究平台谱系;哺育德国工业机器人生态 |
| **帝国理工 / 牛津** | Edward Johns(Robot Learning Lab);牛津机器人研究所(ORI,Posner、Newman 等) | 少样本模仿学习(帝国理工);野外机器人 + 自动驾驶(ORI) | ORI 衍生出 **Oxa**(原 Oxbotica,自动驾驶软件);Google DeepMind 伦敦机器人团队是英国机器人学习人才的引力汇 |

- 欧洲的结构性难题(截至 2026-07):它产出世界级的运动控制/硬件人才,但其衍生公司要么停留在小众领域(ANYbotics = 工业巡检),要么卖给美国收购方(Amazon–RIVR);没有任何一家欧洲机器人基础模型实验室以美国/中国的规模完成融资。Google DeepMind 于 2026 年推出欧洲机器人加速器,部分即为回应此局面([格局:世界其他地区](landscape-row.md))。

## 韩国与日本

| 实验室(机构) | 负责人(PI) | 标志性贡献 | 产业管线 |
|---|---|---|---|
| **Hubo Lab,KAIST** | Jun Ho Oh(荣休)→ 实验室延续 | HUBO(2005,韩国首台双足机器人);**DRC-HUBO 夺得 DARPA 机器人挑战赛决赛冠军(2015,$2M)**([历史](history.md)) | **Rainbow Robotics**(2011 年衍生);Samsung 将持股从 14.7% 提升到 35%(2024-12 宣布,2025-03 获批)成为控股股东;Oh 现任 Samsung 未来机器人办公室负责人 |
| **RaiLab,KAIST** | Jemin Hwangbo(ETH RSL 博士) | RaiSim 物理引擎;执行器网络模拟到现实;Raibo 四足机器人(首台跑完全程马拉松的机器人,2024-11) | **Raion Robotics**(2023,Hwangbo 任 CEO):商业化 Raibo 系列四足机器人 |
| **JSK Lab,东京大学** | Masayuki Inaba(承 Hirochika Inoue 谱系,实验室约建于 1970 年代) | 肌肉骨骼人形机器人(Kotaro、Kojiro、Kenshiro)、JAXON;对 ROS 的深度贡献 | **SCHAFT**(2012,Nakanishi 与 Urata):为接受 DARPA 资助离开大学,赢得 2013 年 DRC 预选赛,2013 年被 Google 收购,SoftBank 出售交易破裂后于 2018 年关闭——企业收编的警世故事 |
| **早稻田大学(高西研究室传统)** | Atsuo Takanishi 谱系 | **WABOT-1(1973)**——第一台全尺寸拟人机器人;WABIAN 双足系列 | 所有人形机器人项目的历史源头(本田 P2/ASIMO 时代深受这一环境影响);如今更多是遗产而非管线 |

- 日本 2026 年的学术-产业载体是 **AIRoA**(约 10,000 小时开放移动操作数据集 + ICRA 2026 竞赛,丰田 HSR 平台——见[数据](data.md));韩国的载体是 Samsung–Rainbow 加上 KAIST 持续的运动控制优势。

## 实验室 → 初创公司管线

| 实验室(PI) | 公司 | 创立 | 方向 | 状态(截至 2026-07) |
|---|---|---|---|---|
| MIT Leg Lab(Raibert) | Boston Dynamics | 1992 | 腿式机器人 | 现代 100% 持股(2026-06) |
| KAIST Hubo Lab(Oh) | Rainbow Robotics | 2011 | 人形机器人/协作机器人 | Samsung 控股(35%) |
| 东京大学 JSK(Inaba 门下) | SCHAFT | 2012 | DRC 人形机器人 | 2013 被 Google 收购 → 2018 关闭 |
| ETH RSL(Hutter) | ANYbotics | 2016 | ANYmal 巡检 | 累计融资超 $150M(2024-12) |
| UT Austin HCRL(Sentis) | Apptronik | 2016 | Apollo 人形机器人 | 约 $5.3B(2026-02) |
| 伯克利(Abbeel/Chen/Duan) | Covariant | 2017 | 仓储操作基础模型 | 团队+授权被 Amazon 吸收(2024-08) |
| 浙大(朱秋国) | DEEP Robotics | 2017 | 四足、人形机器人 | 中国四足第二 |
| 伯克利 Dex-Net(Goldberg/Mahler) | Ambi Robotics | 2018 | 包裹分拣 | 运营中;Goldberg 另联合创立 Jacobi(2022) |
| 哈工大(校友,冷晓琨) | 乐聚机器人 | 2016 | Kuavo 人形机器人 | $207M pre-IPO |
| CMU(Pathak 与 A. Gupta) | **Skild AI** | 2023 | 全形态机器人基础模型 | **>$14B**(2026-01;SoftBank、NVentures、Bezos、Samsung、LG) |
| 清华 IIIS(陈建宇) | Robotera | 2023 | STAR/L7 人形机器人 | 估值超 ¥10B(2026-03);超 $200M 融资(2026-05);千台级交付 + 顺丰物流(2026-Q2,据报道) |
| 清华 MARS(赵行联合创立) | Galaxea AI | 2023 | R1 机器人 + VLA | 约 $291M B+ 轮,估值超 ¥20B(约 $2.8B)(2026-04) |
| 清华(高阳) | Spirit AI | 2024 | "脏数据"具身基础模型 | 融资 $280M(2026-02),独角兽;20 万+ 小时交互数据(公司口径) |
| 北大 EPIC(王鹤) | Galbot | 2023 | 零售轮式人形机器人 | >$2.8B;筹备港股 IPO |
| ETH RSL(Bjelonic) | RIVR(前 Swiss-Mile) | 2023 | 轮腿式配送 | **被 Amazon 收购(2026-03)** |
| KAIST RaiLab(Hwangbo) | Raion Robotics | 2023 | Raibo 四足机器人 | 种子期 |
| 斯坦福 IRIS(Finn)+ 伯克利 RAIL(Levine) | **Physical Intelligence** | 2024 | π 系列 VLA 模型 | $5.6B(2025-11);见 [Pi](company-pi.md) |
| 斯坦福 SVL(李飞飞) | World Labs | 2024 | 生成式世界模型 | Marble 于 2025-11 发布;$1B 融资于 2026-02-18 完成(Autodesk 领投,投后约 $5.4B,据报道) |
| 北大(杨耀东,首席科学家) | PsiBot | 2024(未证实) | 灵巧强化学习 VLA | 融资 ¥2B(国资背景投资方) |
| 斯坦福 IRIS/REAL 校友(Zhao 与 Chi) | Sunday Robotics | 2024 | Memo 家用机器人、Skill Capture Glove | 2025-11 结束隐身($35M,Benchmark/Conviction);据报道约 $165M 后续融资,估值约 $1.15B(2026,据报道) |

## 源自学术界的数据集、基准与工具

| 成果 | 起源实验室 | 意义 |
|---|---|---|
| **ALOHA / ACT / Mobile ALOHA**(2023–24) | 斯坦福 IRIS(Tony Zhao、Zipeng Fu;ALOHA 2 与 Google DeepMind 合作) | $20–30k 开源遥操作装置——全球数据采集的模板,包括中国的数据中心([数据](data.md)) |
| **Diffusion Policy**(RSS 2023) | 哥伦比亚 REAL(Cheng Chi、Song)+ TRI | 在 VLA 之前/并行时期默认的视觉运动策略类型([操作](manipulation.md)) |
| **UMI**(2024) | 斯坦福/哥伦比亚 REAL | 手持式无机器人数据采集,吞吐量约为遥操作的 3 倍 |
| **DROID**(2024) | 斯坦福牵头,13 家机构 | 标准化装置的多样性语料库;RoboArena 评测的底座 |
| **Open X-Embodiment / RT-X**(2023) | 21 家机构与 Google DeepMind 协作 | 默认的 VLA 预训练语料库;跨具身迁移的证明 |
| **OpenVLA**(2024) | 斯坦福 + 伯克利 + TRI 等 | 被引最多的开放 VLA 基线([VLA 模型](vla-models.md)) |
| **LIBERO**(2023) | UT Austin(Liu、Zhu、Stone) | 事实上的(现已饱和的)VLA 记分牌([评测](evaluation.md)) |
| **RoboCasa / robosuite** | UT Austin RPL(Zhu) | 厨房级仿真 + 大量操作研究的底层框架 |
| **BEHAVIOR-1K + OmniGibson**(2024→) | 斯坦福 SVL(李飞飞、吴佳俊) | 1,000 项活动的长时程基准;年度 NeurIPS 挑战赛;"机器人领域的 ImageNet"愿景 |
| **Dex-Net**(2017–19) | 伯克利(Goldberg、Mahler) | 规模化抓取谱系 → Ambi Robotics |
| **legged_gym / rsl_rl / RaiSim** | ETH RSL(Rudin;Hwangbo) | 让强化学习运动控制成为行业默认做法的"配方栈"([运动控制](locomotion.md)、[仿真](simulation.md)) |
| **EgoMimic**(2024) | 佐治亚理工(Danfei Xu) | 人类视频协同训练的证据,助推第一视角数据浪潮 |

## 人才流动模式

- **学术界 → Google → 初创公司 →(有时)回流。** 伯克利/斯坦福博士充实了 Google Brain 机器人团队;其 2023–24 年大流散创立了 Pi 并充实了 Figure/1X;这些创始人的学术合作者和学生如今直接流向那些初创公司,跳过了 Google 这一步(Tony Zhao:斯坦福 → Sunday;Karl Pertsch:伯克利/斯坦福博士后,DROID/OpenVLA/RoboArena → Physical Intelligence,据其个人网站为技术团队成员)。
- **NVIDIA 是这张版图的结缔组织**(截至 2026-07):GEAR 由一位 UT Austin 教授联合领导,Isaac Lab 与 ETH RSL 共同开发,西雅图实验室由一位华盛顿大学教授建立(直到 Fox 2025 年转投 Ai2),NVentures 投资 Skild,GR00T 参考人形机器人于 2026 年交付四个学术实验室。没有任何其他公司嵌入这么多大学([NVIDIA](company-nvidia.md))。
- **中国压缩了这条管线。** 美国模式:博士(5 年)→ 产业实验室 → 初创公司。清华/北大模式:助理教授直接创办公司,大学持股,国家基金跟进,创立约 3 年内 IPO(Robotera、Galbot)。结果:中国的学术实验室与其[人形机器人产业](humanoid-robots.md)实际上是同一张组织架构图。
- **运动控制人才在谱系上高度集中**:Raibert(MIT)→ Boston Dynamics;Hutter(ETH)→ ANYbotics/RIVR + legged_gym 配方;Hwangbo(ETH 博士)→ KAIST → Raion。世界上大多数学习式运动控制栈都可追溯到两个实验室(ETH RSL 及其后裔;MIT 的 Cheetah 系列)——见[运动控制](locomotion.md)。
- **对企业来说,收购胜过竞争**:Google(SCHAFT)、Amazon(Covariant 团队、RIVR)、Samsung(Rainbow)、现代(Boston Dynamics)都是买下学术谱系而非自行培养;OpenAI 和 Meta 则改为招募个人(OpenAI 的 Kalinowski 时代;Meta 已确认的 Sangbae Kim 招募),效果好坏参半([组织机构](organizations.md))。
- **基准权力是软实力**:谁维护记分牌(斯坦福的 BEHAVIOR 挑战赛、UT Austin 的 LIBERO、复旦的 LIBERO-Plus、上海人工智能实验室的 EIbench),谁就定义什么叫"最先进水平"——见[最先进水平](state-of-the-art.md)和[评测](evaluation.md)。

## 悬而未决的问题

- 当训练规模超出学术算力预算时,大学还能做前沿工作吗?2026 年的对冲手段是基础设施捐赠(NVIDIA GR00T 参考机器人、云算力额度)——但这也加深了供应商锁定。
- 双重身份模式能否在规模化的利益冲突下存续(教授创始人评审竞争对手的论文,学生成为事实上的初创公司员工)?尚无机构发布明确政策(截至 2026-07)。
- 欧洲/日本会把研究卓越转化为本土公司,还是继续把实验室成果输出给美中收购方(RIVR、SCHAFT 的先例)?
- 实体清单动态:哈工大和其他与国防相关的中国大学被切断了与美国的合作,但其衍生公司(乐聚)却能自由商业化——这一不对称尚无美国政策上的应对([安全与监管](safety-regulation.md))。

## 来源
- https://www.businesswire.com/news/home/20260114335623/en/Skild-AI-Raises-$1.4B-Now-Valued-Over-$14B — Skild 融资 $1.4B,估值超 $14B(2026-01);CMU 创始人 Pathak 与 Gupta
- https://www.therobotreport.com/skild-ai-raises-1-4b-building-omni-bodied-robot-skild-brain/ — Skild 投资方名单(SoftBank、NVentures、Bezos、Samsung、LG)、全形态论点
- https://shurans.github.io/ — Shuran Song:斯坦福 REAL 实验室,哥伦比亚 → 斯坦福的迁移
- https://github.com/real-stanford/diffusion_policy — Diffusion Policy 起源(哥伦比亚/REAL + TRI)
- https://umi-gripper.github.io/ — UMI 手持采集,相对遥操作的吞吐量
- https://behavior.stanford.edu/challenge/index.html — BEHAVIOR-1K 2025/2026 挑战赛规模(斯坦福 SVL)
- https://the-decoder.com/behavior-1k-is-set-to-become-for-robotics-what-imagenet-was-for-computer-vision/ — "机器人领域的 ImageNet"提法(愿景性)
- https://rpl.cs.utexas.edu/ — UT Austin RPL:Zhu 与 NVIDIA GEAR 的双重身份;RoboCasa、robosuite
- https://rpl.cs.utexas.edu/publications/2024/07/15/nasiriany-rss24-robocasa/ — RoboCasa(RSS 2024)
- https://goldberg.berkeley.edu/bio.html — Goldberg:Ambi + Jacobi 联合创始人、BAIR 联合创始人
- https://ipira.berkeley.edu/ambi-robotics — Ambi Robotics 源自 Dex-Net(Mahler,2018 年博士)
- https://rail.eecs.berkeley.edu/people.html — RAIL 实验室(Levine)隶属 BAIR
- https://rsl.ethz.ch/partnership/spinoff.html — ETH RSL 衍生公司名录(ANYbotics、RIVR、Ascento、Flexion)
- https://www.swissinfo.ch/eng/workplace/amazon-acquires-swiss-delivery-robot-start-up-rivr/91144826 — Amazon 收购 RIVR(2026-03-19 确认)
- https://deeptechnation.ch/dtn-news/amazon-acquires-rivr-how-an-eth-zurich-lab-built-the-robot-that-delivers-your-packages/ — RIVR/Swiss-Mile 创立(2023)、Bezos 领投种子轮、RSL 起源
- https://ethz.ch/en/news-and-events/eth-news/news/2025/12/getting-a-grip-ai-and-robotic.html — RSL–NVIDIA 关系;ANYbotics 谱系
- https://news.samsung.com/global/samsung-electronics-to-become-largest-shareholder-in-rainbow-robotics-accelerating-future-robot-development — Samsung 持股 14.7%→35%;Jun Ho Oh 出任未来机器人办公室负责人
- https://www.koreatimes.co.kr/business/companies/20250305/south-koreas-regulator-approves-samsungs-purchase-of-robotics-startup — 监管机构批准(2025-03)
- https://en.wowtale.net/2024/04/03/74664/ — Raion Robotics 由 Hwangbo(KAIST)于 2023 年创立,基于 Raibo 技术
- https://www.koreatimes.co.kr/business/tech-science/20241118/kaists-4-legged-robot-becomes-1st-in-the-world-to-finish-full-marathon — Raibo 跑完全程马拉松(2024-11)
- https://spectrum.ieee.org/schaft-robot-company-bought-by-google-darpa-robotics-challenge-winner — SCHAFT:JSK 起源、DARPA 资助约束、Google 收购
- https://www.caixinglobal.com/2026-03-05/chinas-robot-era-valued-at-over-10-billion-yuan-102419832.html — Robotera 估值超 ¥10B;清华 IIIS 孵化
- https://pandaily.com/star-dynasty-humanoid-robot-sf-express-20260622 — Robotera 累计融资超 ¥4B、顺丰物流部署(2026-06)
- https://www.forbes.com/sites/ywang/2025/08/25/the-700-million-chinese-robot-startup-that-wants-to-take-on-tesla/ — Galaxea AI:清华/斯坦福创始团队,赵行(前 Waymo)任首席科学职位
- https://www.caixinglobal.com/2026-04-02/robot-startup-galaxea-ai-raises-291-million-102430297.html — Galaxea 融资 ¥2B(约 $291M),估值超 ¥20B(2026-04)
- https://www.prnewswire.com/news-releases/spirit-ai-lands-280m-to-scale-embodied-ai-through-dirty-data-302697085.html — Spirit AI 融资 $280M(2026-02);高阳(清华助理教授,伯克利博士);20 万+ 小时数据主张
- https://baike.baidu.com/en/item/Spirit%20AI%20(Hangzhou)%20Technology%20Co.,%20Ltd./33601 — Spirit AI 于 2024-01 创立(杭州);韩峰涛与高阳联合创立
- https://www.psibot.ai/en/about-us/ — PsiBot:杨耀东任首席科学家、北大联合实验室、Psi R0/R1
- https://autonews.gasgoo.com/articles/icv/seeds-psibot-announces-completion-of-2-billion-yuan-financing-2031589417448222721 — PsiBot ¥2B 融资、国资背景投资方
- https://en.wikipedia.org/wiki/Leju_Robot — 乐聚:哈工大衍生(2016)、冷晓琨、Kuavo/HarmonyOS
- https://www.therobotreport.com/leju-raises-200m-humanoid-production-unitree-unveils-h2-robot/ — 乐聚 $207M pre-IPO 轮
- https://www.thewirechina.com/whos_who/zhu-qiuguo-%E6%9C%B1%E7%A7%8B%E5%9B%BD/ — 朱秋国:浙大副教授 + DEEP Robotics 创始人/CEO
- https://www.zju.edu.cn/english/2025/0313/c75270a3026836/page.htm — 浙大"六小龙"培育叙事、ZJUDancer 起源
- https://github.com/InternRobotics — 上海人工智能实验室 OpenRobotLab/InternRobotics 开放技术栈
- https://oceanpang.github.io/ — 庞江淼:上海人工智能实验室具身智能中心负责人
- https://www.geekwire.com/2025/nvidia-leader-uw-prof-dieter-fox-joins-allen-institute-for-ai-to-lead-new-robotics-initiative/ — Fox:NVIDIA 西雅图实验室 → Ai2 机器人计划(2025-07)
- https://nvidianews.nvidia.com/news/nvidia-open-humanoid-robot-reference-design — GR00T 参考人形机器人(2026-06-01):Unitree H2 Plus + Sharpa 灵巧手;合作方 Ai2、ETH、斯坦福机器人中心、UCSD ARCLab
- https://theaiinsider.tech/2025/11/20/sunday-emerges-from-stealth-with-35m-for-household-robot-called-memo/ — Sunday Robotics:Zhao(CEO)与 Chi(CTO),$35M(Benchmark/Conviction),Memo + Skill Capture Glove
- https://www.founded.com/sunday-memo-robot-chores-founders/ — Sunday 创立于 2024,估值据报道约 $1.15B,创始人的 ALOHA/Diffusion Policy 谱系
- https://h2t.iar.kit.edu/tamim-asfour.php — Asfour:自 1998 年起的 ARMAR 家族,KIT H2T
- https://www.ias.informatik.tu-darmstadt.de/Team/JanPeters — Peters:TU Darmstadt IAS + DFKI SAIROL(2022 年起)
- https://www.tri.global/about-us/dr-russ-tedrake — Tedrake 的 MIT + TRI 高级副总裁双重角色
- https://droid-dataset.github.io/ — DROID:13 家机构,斯坦福牵头
- https://robotics-transformer-x.github.io/ — Open X-Embodiment:21 家机构协作
- https://meche.mit.edu/people/faculty/SANGBAE@MIT.EDU — MIT 将 Sangbae Kim 列为"机械工程教授(休假中)"(截至 2026-07)
- https://www.linkedin.com/pulse/meta-hires-mits-sangbae-kim-robotics-architect-brian-heater-mf7ge — Kim 于 2025-03 以"Robotics Architect"身份加入 Meta 机器人工作室(Heater,2025-04-16);Kim 本人的 LinkedIn 资料/公告可佐证
- https://kpertsch.github.io/ — Pertsch 自述为 Physical Intelligence 技术团队成员;DROID/OpenVLA/RoboArena 项目页面
