---
title: 关键人物
slug: key-people
updated: 2026-07-04
confidence: verified
lang: zh
source: ../wiki/key-people.md
---
> Physical AI 领域由一小群联系紧密的人推动:既有联合创立基础模型初创公司的学术研究者(Sergey Levine、Chelsea Finn、Deepak Pathak),也有企业实验室负责人(NVIDIA GEAR 的 Jim Fan 和 Yuke Zhu、Google DeepMind 的 Carolina Parada、Amazon 的 Pieter Abbeel),以及争相将人形机器人商业化的创始人型高管(Brett Adcock/Figure、Bernt Børnich/1X、王兴兴/Unitree、彭志辉/AgiBot)。2024–2026 年人事变动频繁:Google 机器人"离散潮"孕育了美国大多数机器人基础模型初创公司,Amazon 吸纳了 Covariant 的创始团队,Tesla 和 Boston Dynamics 更换了项目负责人,随着领域从研究转向部署,多位高知名度高管(Robert Playter、Caitlin Kalinowski、Eric Jang、Milan Kovac)相继离任。

## 研究者与 AI 实验室负责人

| 人物 | 所属机构(截至 2026-07) | 以何闻名 | 2024–2026 重要动向 |
|---|---|---|---|
| **Sergey Levine** | UC Berkeley(BAIR/RAIL)+ Physical Intelligence 联合创始人 | 机器人深度强化学习(Soft Actor-Critic、离线 RL)、Open X-Embodiment/RT-X、π 系列[视觉-语言-动作模型(VLA)](vla-models.md) | 联合创立 Physical Intelligence(2024-03 宣布);合著 π0(2024-10)、π0.5(2025-04)、π0.7(2026-04),他称后者显示一旦出现技能重组,能力随数据"超线性"扩展 |
| **Chelsea Finn** | Stanford(IRIS 实验室)+ Physical Intelligence 联合创始人 | MAML 元学习;其实验室产出 ALOHA / Mobile ALOHA 低成本遥操作(teleoperation)硬件和 DROID 数据集([数据](data.md)) | 2024 年联合创立 Physical Intelligence;π 模型系列直至 π0.7(2026-04)的核心作者 |
| **Karol Hausman** | Physical Intelligence CEO 兼联合创始人 | 曾领导 Google Brain 机器人操作攻坚项目(SayCan/RT 时代);Stanford 兼职教授 | 离开 Google DeepMind 创立 Pi(2024);估值升至 $5.6B(截至 2025-11);据报道正洽谈以 $11B+ 估值融资约 $1B(截至 2026-01,(未证实)) |
| **Pieter Abbeel** | Amazon(Frontier AI & Robotics;AGI 部门)+ UC Berkeley 教授 | 面向操作任务的深度 RL 与模仿学习先驱;联合创立 Covariant(2017) | Amazon 招入 Covariant 创始人(Abbeel、Peter Chen、Rocky Duan)及约 25% 员工,并获其基础模型授权(2024-08);被任命为 Amazon AGI 部门 LLM 工作负责人(截至 2025-12),同时继续机器人方向 |
| **Jim Fan (Linxi Fan)** | NVIDIA — AI 总监兼杰出科学家;GEAR 实验室 + Project GR00T 联合负责人 | "Physical AI/具身 AGI"布道者;Stanford 博士(师从李飞飞);OpenAI 首位实习生;Voyager/Eureka | 在 GTC 2024-03 宣布 Project GR00T 人形机器人基础模型;发布 GR00T N1(2025-03)至 N1.6(2026),在 Unitree G1、AgiBot Genie-1、YAM 机械臂上测试 |
| **Yuke Zhu** | UT Austin(RPL 实验室,副教授)+ NVIDIA — 总监兼杰出研究科学家,GEAR 联合负责人 | 机器人感知与学习;仿真框架(robosuite);GR00T 模型系列([仿真](simulation.md)) | 与 Jim Fan 共同创建 NVIDIA GEAR(2024-02);获 IEEE 具身 AI 早期职业奖(2025) |
| **Carolina Parada** | Google DeepMind — 副总裁、机器人负责人 | 领导 Gemini Robotics 项目:Gemini Robotics + Robotics-ER(2025-03)、On-Device(2025-06)、Robotics 1.5(2025-09) | 2025–2026 年领衔 DeepMind 的机器人攻势;发起面向欧洲初创企业的 Google DeepMind Robotics Accelerator(2026);合作将 Gemini 模型部署到 Agile Robots 的人形机器人上 |
| **Russ Tedrake** | MIT 教授 + Toyota Research Institute 大型行为模型(Large Behavior Models)高级副总裁 | 欠驱动机器人学;扩散策略研究;面向灵巧操作的大型行为模型(LBM) | 与 Scott Kuindersma 共同主导 Boston Dynamics–TRI 演示,用 LBM 驱动 Atlas 完成长时程操作 + 移动序列(2025-08) |
| **Deepak Pathak** | Skild AI CEO 兼联合创始人;CMU 教职 | 好奇心驱动 RL、自适应运动控制;"全形态(omni-bodied)"机器人大脑理念 | 与 Abhinav Gupta 联合创立 Skild(2023);$300M A 轮(2024-07);SoftBank 领投 $1.4B 融资,估值 >$14B(2026-01),NVentures 和 Bezos Expeditions 参投 |
| **李飞飞** | Stanford HAI + World Labs CEO 兼联合创始人 | ImageNet;"空间智能"宣言;将[世界模型(world model)](world-models.md)视为 AI 的下一个前沿 | 创立 World Labs(2024,$230M);推出首个商用生成式 3D 世界模型 Marble(2025-11);完成 Autodesk 领投的 $1B 融资(2026-02-18;投后约 $5.4B,(据报道)) |
| **Marc Raibert** | Boston Dynamics 创始人;RAI Institute 执行主任 | 足式运动先驱(MIT Leg Lab、BigDog、Atlas);1992 年创立 Boston Dynamics | 执掌现代汽车支持的 RAI Institute(2022 年成立);与 Boston Dynamics 达成电动 Atlas 的 RL 训练合作(2025-02);RAI 框架造就了 Atlas 在 CES 2026 的体操表演和自然步态 |
| **Vincent Vanhoucke** | Waymo — 杰出工程师 | 用约 8 年时间建立起 Google 机器人研究团队(RT-1/RT-2 时代);前 Google DeepMind 机器人负责人 | 以健康优先为由离开 DeepMind 机器人团队;转投 Waymo,从事自动驾驶的 ML/机器人工作(2024) |
| **Corey Lynch** | Figure AI — AI 总监 | 语言条件模仿学习(前 Google Brain);领导 Figure 的 Helix VLA | 从 Google Brain 加入 Figure(2023-06);发布 Helix,首个具备双机器人协作能力的人形机器人 VLA(2025-02) |
| **Eric Jang** | 独立(截至 2026-01) | 2022–2026 任 1X AI 副总裁;"条条大路通机器人";主导 NEO 的 Redwood AI 模型和 1X World Model | 从 1X 卸任(2026-01);由 Mohi Khansari(Redwood 首席架构师)接任机器人学习负责人 |

Physical Intelligence 的其他联合创始人:Brian Ichter(前 Google Brain)、Quan Vuong、Adnan Esmail,以及 Stripe 老将投资人 Lachy Groom("Jasmine Hsu"出现在部分名单上,但大多数名单——包括 2026-01 的 TechCrunch 深度报道——都没有她,(未证实);见 [PI 深度解析](company-pi.md));π0.7 署名约 90 位作者,包括 Danny Driess。

## 创始人与高管 — 美国与欧洲

| 人物 | 公司与职位 | 背景 | 2024–2026 重要动向 |
|---|---|---|---|
| **Brett Adcock** | Figure AI — 创始人兼 CEO(2022 年创立) | 连续创业者(Vettery、Archer Aviation);持有 Figure 约 50% 股份(未证实) | 终止与 OpenAI 的合作,转向垂直整合(2025-02,Helix 发布);完成投后估值 **$39B** 的 >$1B C 轮(2025-09)——18 个月内估值跃升 15 倍;总融资 >$1.9B(截至 2026-01);BotQ 工厂 + BMW 部署([人形机器人](humanoid-robots.md)) |
| **Bernt Børnich** | 1X Technologies — 创始人兼 CEO(2014 年在挪威创立,原名 Halodi Robotics) | 面向家庭的低扭矩执行器人形机器人;先有 EVE,后有 NEO | 开放 NEO 预订——$20k 或 $499/月(2025-10-28);首年产量(10,000+ 台)5 天售罄(公司口径,据 Forbes/1X);在加州 Hayward 启动 NEO 全面量产,目标到 2027 年底达到 100k 台/年产能(2026-04);承诺 2026 年底前首批家庭交付 |
| **Peggy Johnson** | Agility Robotics — CEO(2024-03 起) | 前 Magic Leap CEO;在 Nadella 麾下任 Microsoft 业务发展执行副总裁 6 年;Qualcomm 资深人士 | 接替联合创始人 Damion Shelton(现任总裁);扩大 Digit 在仓库场景的 RaaS 业务;正与 Churchill Capital Corp XI 商讨拟议的 SPAC 业务合并(截至 2026-06,进行中);估值约 $2.1B(截至 2026,据二级市场数据,(未证实)) |
| **Jeff Cardenas** | Apptronik — 联合创始人兼 CEO(Austin,2016 年从 UT HCRL 分拆) | Apollo 人形机器人;Mercedes-Benz、GXO、Jabil 试点;与 Google DeepMind 的 AI 合作 | $350M A 轮(2025-02,B Capital/Capital Factory、Google)扩至 $403M;$520M A-X 轮延展(2026-02)→ A 轮总额 >$935M,投后约 $5.3B;新投资方包括 John Deere、AT&T Ventures、卡塔尔投资局 |
| **Robert Playter** | Boston Dynamics — 2020–2026 年 CEO | 在 BD 工作 30 年;主导 Spot 商业化和电动 Atlas 发布 | 2026-02 卸任(最后工作日 2026-02-27),称因退休;CFO Amanda McMaster 出任临时 CEO;离任恰逢现代汽车的商业化推进(据报道目标:到 2028 年最高 3 万台人形机器人/年);现代汽车以 $325M 收购 SoftBank 剩余 9.65% 股份,实现 100% 控股(2026-06,据 Reuters/KED Global) |
| **Kyle Vogt** | The Bot Company — 创始人兼 CEO(2024 年创立) | 联合创立 Cruise(2023 年末被逐出);Twitch 联合创始人 | 打造非人形家用机器人;$150M 种子轮(2024-05,估值 $550M);Greenoaks 领投 $150M,估值 $2B(2025-03);据报道正以 >$4B 估值融资 $250M(2025-10,尚未确认完成) |
| **Caitlin Kalinowski** | 前 OpenAI — 硬件/机器人负责人 2024-11 → 2026-03 | 曾领导 Meta AR 眼镜硬件;Apple 产品设计 | 加入 OpenAI 从零打造机器人/硬件(2024-11);2026-03-07 辞职,称对 OpenAI 五角大楼合同的治理问题存在担忧("无人授权的致命自主");OpenAI 确认其离职,并称该合同不涉及国内监控与自主武器;开源人形机器人初创公司 K-Scale Labs(已倒闭)创始人 Benjamin Bolte 同周加入 OpenAI;OpenAI 机器人部门现由 Aditya Ramesh 以机器人副总裁身份领衔([版图:美国](landscape-usa.md)) |
| **Ashok Elluswamy** | Tesla — AI 软件副总裁;Optimus 负责人 | Autopilot 首位工程师;FSD AI 负责人 | 在 Milan Kovac(Optimus 工程负责人)于 2025-06 离职后接管 Optimus 项目;统一 FSD 与 Optimus 的 AI 技术栈;发表演讲 "Building Foundational Models for Robotics at Tesla"(2026-02) |
| **Marc Raibert** | RAI Institute — 执行主任 | 见上方研究者表格 | — |

## 创始人与高管 — 中国

完整的公司版图见[版图:中国](landscape-china.md)。

| 人物 | 公司与职位 | 背景 | 2024–2026 重要动向 |
|---|---|---|---|
| **王兴兴** | Unitree Robotics(宇树科技)— 创始人兼 CEO(杭州,2016 年创立) | 低成本四足机器人(Go/B 系列)后转人形(H1、G1、R1);2025 年全球人形机器人出货份额 >32%(据报道) | 在习近平的民营企业座谈会上坐在前排(2025-02);提交 ¥4.2B(约 $608M)科创板 IPO 申请(2026-03)——首个纯人形机器人上市案例;直接持股 23.8%、表决权 68.78%;2025 年营收据报约 ¥1.7B(Caixin 称 ¥1.69B,较 2024 年的 ¥393M 增长),人形机器人占比过半;约一半 IPO 募资拟投入 AI 模型训练;CSRC 于 2026-07-03 批准注册,据报道 IPO 估值最高约 ¥40B(约 $5.9B) |
| **彭志辉("稚晖君")** | AgiBot / 智元机器人 — 联合创始人兼 CTO(上海,2023 年创立) | 前华为"天才少年";Bilibili 硬核创客网红;主导 AgiBot 的机器人 + GO-1/Genie 基础模型和 AgiBot World 数据集([数据](data.md)) | 第 10,000 台 AgiBot 人形机器人下线(2026-03);宣布 2026 年为"部署之年"——四台人形机器人直播完成 8 小时工厂班次(2026-04);在 AgiBot 借壳上市操作后出任科创板上市公司 Swancor/上纬新材董事长(2025,据报道);获中国青年五四奖章(2026-05) |
| **邓泰华** | AgiBot — 联合创始人兼董事长/CEO | 前华为副总裁(计算产品线) | 与彭志辉联合创立 AgiBot(2023);将其做成中国两大主导人形机器人厂商之一 |
| **王鹤** | Galbot(银河通用)— 创始人兼 CTO(北京,2023 年创立) | 北京大学助理教授;BAAI 具身智能中心主任;面向零售的轮式底盘双臂 G1 | 2025 年底/2026 年初多轮融资合计约 ¥5B(约 $700M),含与国家"大基金"的 ¥2.5B 轮(2026-03);估值 >¥20B(约 $2.8B)(截至 2025-12);已为 2026 年港股 IPO 选定投行(2025-12,据 Bloomberg) |
| **何小鹏** | XPeng(小鹏)— 董事长兼 CEO | 进军人形机器人的电动车厂商([硬件](hardware.md)) | 发布采用固态电池设计的新一代 IRON 人形机器人,并宣称 2026 年底前量产(截至 2025-11) |
| **周剑** | UBTech(优必选)— 创始人兼 CEO(深圳,2023 年港股上市) | Walker 人形机器人系列;最早上市的中国人形机器人厂商 | Walker S1/S2 在 BYD、Foxconn、Zeekr 工厂试点;Walker S2 引入可热插拔电池实现 24/7 运行(2025) |

## 2024–2026 重要动向时间线

- **2024-02/03** — Jim Fan 与 Yuke Zhu 创建 NVIDIA GEAR 实验室;GTC 上宣布 Project GR00T。Hausman、Levine、Finn、Ichter、Hsu 创立 Physical Intelligence。Peggy Johnson 出任 Agility Robotics CEO。
- **2024-08** — Amazon 招入 Covariant 创始人(Abbeel、Chen、Duan)及约 25% 员工;获得 Covariant 机器人基础模型的非独占授权。
- **2024-H2** — Vincent Vanhoucke 离开 Google DeepMind 机器人团队赴 Waymo;Caitlin Kalinowski 从 Meta 加入 OpenAI(2024-11)领导硬件/机器人。
- **2025-02** — Figure 终止与 OpenAI 的合作;Corey Lynch 团队发布 Helix。Boston Dynamics 与 Raibert 的 RAI Institute 就 Atlas 的 RL 达成合作。Apptronik 完成 $350M A 轮。
- **2025-06** — Milan Kovac 离开 Tesla;Ashok Elluswamy 将 Optimus 纳入其 FSD 职责范围。
- **2025-08** — Boston Dynamics + TRI(Tedrake/Kuindersma)在 Atlas 上演示大型行为模型。
- **2025-09** — Figure 完成投后 $39B 的 >$1B C 轮。
- **2025-10/11** — 1X 开放 NEO 预订;World Labs(李飞飞)发布 Marble;Physical Intelligence 估值 $5.6B。
- **2025-12** — Abbeel 被任命为 Amazon LLM 工作负责人(AGI 部门);Galbot 为港股 IPO 选定投行。
- **2026-01** — Skild AI 完成 $1.4B 融资,估值 >$14B(SoftBank 领投);Eric Jang 从 1X 卸任。
- **2026-02** — Robert Playter 从 Boston Dynamics 卸任;Apptronik 将 A 轮扩至 >$935M(估值约 $5.3B)。
- **2026-03** — Unitree 提交 $608M 科创板 IPO;Kalinowski 因五角大楼合同从 OpenAI 辞职,Benjamin Bolte(前 K-Scale)加入;AgiBot 第 10,000 台人形机器人下线。
- **2026-04** — Physical Intelligence 发布 π0.7;1X 在 Hayward 启动 NEO 全面量产。
- **2026-06** — Agility Robotics 与 Churchill Capital Corp XI 商讨 SPAC 合并;现代汽车以 $325M 收购 SoftBank 剩余 9.65% 股份,100% 控股 Boston Dynamics。
- **2026-07** — Unitree 的 ¥4.2B 科创板 IPO 获 CSRC 注册批准(2026-07-03)。

## 值得了解的规律

- **Google 机器人离散潮孕育了美国的行业格局。** Physical Intelligence(Hausman、Ichter)、Figure 的 Helix 团队(Lynch)、1X 的 AI 团队(Jang)以及 Skild 的竞争对手们都可追溯到 Google Brain/DeepMind 机器人团队;建立起该团队的 Vanhoucke 现在 Waymo。Google DeepMind 则围绕 Parada 的 Gemini Robotics 团队重建([组织机构](organizations.md))。
- **"双重身份"学者主导模型层。** Levine(Berkeley/Pi)、Finn(Stanford/Pi)、Zhu(UT Austin/NVIDIA)、Pathak(CMU/Skild)、Tedrake(MIT/TRI)、王鹤(北大/Galbot)都在运营工业项目的同时保留教职——人才池就是这么薄。
- **自动驾驶老兵迁移到机器人。** Kyle Vogt(Cruise → Bot Company)、Elluswamy(Autopilot → Optimus)、Vanhoucke(机器人 → Waymo,反向流动)反映了 FSD 与机器人技术栈的融合。
- **2026 年高管更迭映射商业化压力。** Playter(Boston Dynamics)、Kovac(Tesla)、Kalinowski(OpenAI)、Jang(1X)在约 9 个月内相继离场,背后是股东从研发转向生产经济性的推动([投资](investment.md))。
- **中国的创始人画像不同:** 硬件出身的创始人(王兴兴、彭志辉)搭配国家队资本和 IPO 路径,对照美国以模型为先、依赖风险投资巨额融资的创始人([最新进展](state-of-the-art.md)、[版图:美国](landscape-usa.md))。

## 来源

- https://www.pi.website/blog/pi07 — π0.7 发布公告(2026-04-16),能力介绍,作者名单含 Levine/Finn/Driess
- https://techcrunch.com/2026/04/16/physical-intelligence-a-hot-robotics-startup-says-its-new-robot-brain-can-figure-out-tasks-it-was-never-taught/ — π0.7 报道;Pi 累计融资 >$1B、估值 $5.6B;Levine 引语
- https://x.com/svlevine/status/1767636367717310708 — Levine 宣布创立 Physical Intelligence(2024-03)
- https://techcrunch.com/2026/01/30/physical-intelligence-stripe-veteran-lachy-grooms-latest-bet-is-building-silicon-valleys-buzziest-robot-brains/ — Pi 深度报道,Lachy Groom 的角色
- https://techfundingnews.com/physical-intelligence-1b-raise-11b-valuation-founders-fund-lightspeed/ — 据报道以 $11B+ 估值融资约 $1B(未确认)
- https://research.nvidia.com/labs/gear/ — GEAR 实验室使命;Fan 与 Zhu 联合负责
- https://research.nvidia.com/labs/gear/gr00t-n1_6/ — GR00T N1.6 模型页面
- https://www.cs.utexas.edu/news/2025/yuke-zhu-earns-ieee-early-career-award-groundbreaking-contributions-ai-and-robotics — Zhu 的 IEEE 奖项、双重任职
- https://deepmind.google/blog/gemini-robotics-brings-ai-into-the-physical-world/ — Gemini Robotics 发布(2025-03)
- https://blog.google/topics/google-europe/powering-the-future-of-robotics-in-europe/ — Parada 任机器人副总裁;欧洲机器人加速器
- https://www.aboutamazon.com/news/company-news/amazon-covariant-ai-robots — Amazon–Covariant 人才招募加授权交易(2024-08)
- https://techcrunch.com/2024/08/31/amazon-hires-the-founders-of-robotics-ai-startup-covariant/ — Covariant 创始人/员工细节
- https://en.wikipedia.org/wiki/Pieter_Abbeel — Abbeel 履历;Amazon AGI LLM 职务(2025-12)
- https://www.intelcapital.com/figure-exceeds-1b-in-series-c-funding-at-39b-post-money-valuation/ — Figure C 轮 >$1B、投后 $39B(2025-09),投资方名单
- https://en.wikipedia.org/wiki/Brett_Adcock — Adcock 背景(Vettery、Archer)
- https://newatlas.com/robotics/helix-vla-figure-02-robot/ — Helix VLA 发布;Figure–OpenAI 分道扬镳(2025-02);Corey Lynch 的角色
- https://www.linkedin.com/in/corey-lynch-391a56ba/ — Lynch:Figure AI 总监,2023-06 从 Google Brain 加入
- https://en.wikipedia.org/wiki/1X_Technologies — 1X/Halodi 历史;Børnich;NEO 预订条款(2025-10-28)
- https://www.forbes.com/sites/johnkoetsier/2026/04/30/1x-kicks-off-full-scale-production-of-humanoid-robot-neo/ — NEO 全面量产、Hayward 工厂、预订数量
- https://www.humanoidsdaily.com/news/eric-jang-steps-down-as-vp-of-ai-at-1x-technologies — Jang 离任(2026-01);Khansari 接任
- https://www.therobotreport.com/1xs-neo-humanoid-gains-autonomy-with-new-redwood-ai-model/ — Redwood AI 模型,Jang 引语
- https://www.agilityrobotics.com/content/agility-robotics-appoints-peggy-johnson-as-chief-executive-officer — Johnson 任命(2024-03)、背景
- https://www.stocktitan.net/sec-filings/CCXI/425-churchill-capital-corp-xi-business-combination-communication-47967fc2936a.html — Agility–Churchill Capital XI SPAC 业务合并公告(2026-06)
- https://apptronik.com/news-collection/apptronik-closes-over-935-million-series-a — Apptronik A 轮总额 >$935M(2026-02)
- https://www.cnbc.com/2026/02/11/apptronik-raises-520-million-at-5-billion-valuation-for-apollo-robot.html — Apptronik 约 $5B+ 估值,Cardenas
- https://techcrunch.com/2026/02/10/boston-dynamics-ceo-robert-playter-steps-down-after-30-years-at-the-company/ — Playter 离任;McMaster 任临时 CEO
- https://www.kedglobal.com/robotics/newsView/ked202606210001 — 现代汽车以 $325M 收购 SoftBank 剩余 9.65% Boston Dynamics 股份(2026-06)
- https://rai-inst.com/resources/press-release/boston-dynamics-atlas-partnership/ — Boston Dynamics–RAI Institute RL 合作(2025-02)
- https://rai-inst.com/about/leadership/marc-raibert/ — Raibert 在 RAI Institute 的职务
- https://fortune.com/2025/06/06/departure-milan-kovac-tesla-optimus-humanoid-robot-elon-musk/ — Kovac 离职;Elluswamy 接管 Optimus(2025-06)
- https://www.caixinglobal.com/2026-03-21/unitree-robotics-files-for-608-million-star-market-ipo-102425491.html — Unitree ¥4.2B 科创板 IPO 申报
- https://www.caixinglobal.com/2026-07-03/unitree-robotics-wins-approval-for-618-million-star-market-ipo-102460136.html — CSRC 注册批准(2026-07-03);2025 年营收 ¥1.69B;约 ¥40B 估值预估
- https://www.scmp.com/tech/article/3347611/inside-unitrees-landmark-ipo-what-know-about-chinas-humanoid-giant — 王兴兴持股/表决权,Unitree 指标
- https://en.people.cn/n3/2026/0602/c90000-20462845.html — Unitree 通过上交所上市审核;王兴兴 68.78% 表决权
- https://english.news.cn/20260503/3616ad8aae584ea6a5501dbb0fd78111/c.html — 新华社彭志辉人物报道;第 10,000 台机器人;部署里程碑
- https://technode.com/2026/03/02/humanoid-robot-maker-galbot-raises-rmb-2-5-billion/ — Galbot ¥2.5B 融资(2026-03)
- https://www.bloomberg.com/news/articles/2025-12-12/humanoid-robot-maker-galbot-said-to-pick-banks-for-2026-hk-ipo — Galbot 港股 IPO 筹备
- https://www.businesswire.com/news/home/20260114335623/en/Skild-AI-Raises-$1.4B-Now-Valued-Over-$14B — Skild $1.4B 融资、估值 >$14B(2026-01)
- https://techcrunch.com/2025/03/23/former-cruise-ceo-kyle-vogts-new-robotics-startup-reportedly-raises-another-150m/ — Bot Company $150M、估值 $2B(2025-03)
- https://www.bloomberg.com/news/articles/2025-10-28/cruise-founder-kyle-vogt-s-robotics-startup-eyes-4-billion-valuation — Bot Company 据报道洽谈 $4B+ 估值融资
- https://www.humanoidsdaily.com/news/openai-hardware-leader-caitlin-kalinowski-resigns-over-pentagon-deal-as-benjamin-bolte-joins — Kalinowski 辞职(2026-03-07);Bolte 加入
- https://finance.yahoo.com/news/openai-robotics-leader-resigns-over-171328055.html — Fortune(经 Yahoo):OpenAI 确认 Kalinowski 离职;其担忧的原话;公司声明的合同保障条款
- https://www.tri.global/about-us/dr-russ-tedrake — Tedrake 任 TRI 大型行为模型高级副总裁
- https://pressroom.toyota.com/ai-powered-robot-by-boston-dynamics-and-toyota-research-institute-takes-a-key-step-towards-general-purpose-humanoids/ — Atlas LBM 演示(2025-08),Tedrake/Kuindersma
- https://techcrunch.com/2025/11/12/fei-fei-lis-world-labs-speeds-up-the-world-model-race-with-marble-its-first-commercial-product/ — World Labs Marble 发布(2025-11)
- https://drfeifei.substack.com/p/from-words-to-worlds-spatial-intelligence — 李飞飞的空间智能宣言
- https://vanhoucke.medium.com/whymo-6926a65928f4 — Vanhoucke 讲述离开 Google DeepMind 机器人团队赴 Waymo 的经过
