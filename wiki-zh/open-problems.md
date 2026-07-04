---
title: 开放问题与争论
slug: open-problems
updated: 2026-07-04
confidence: verified
lang: zh
source: ../wiki/open-problems.md
---
> Physical AI 领域截至 2026-07 的核心争议:机器人学习能否弥合 Ken Goldberg 所估算的
> "10 万年"人类经验数据缺口;在移动/步态领域已成熟的模拟到现实(sim2real)迁移能否
> 覆盖接触密集型的操作(manipulation)任务;灵巧度差距(人类手部约有 1.7 万个
> 机械感受器,而机器人触觉感知远远落后)是否会如 Rodney Brooks 所说,注定让
> 依赖视频训练的人形机器人失败;如何从约 99% 的演示成功率跨越到商业部署所需的
> 多个"9"的可靠度;一场安全标准的抢跑(ISO 10218:2025 已发布,面向动态平衡机器人的
> ISO 25785-1 仍在草案阶段,中国的 HEIS 2026 框架已于 2026-02 发布);
> [VLA 模型](vla-models.md)领域缺乏可信共享基准的评测危机;以及从 Elon Musk 的
> "2026 年实现 AGI"到 Brooks 的"数十年内都是纯粹幻想"横跨整个光谱的时间线争论。

## 1. 数据稀缺——核心瓶颈

- **差距有多大。** Ken Goldberg(UC Berkeley)在两篇 *Science Robotics* 论文
  (2025-08-27)中指出:LLM 的训练数据相当于约 10 万年的人类阅读量,而机器人学
  在物理交互数据上完全没有可比拟的规模——而且机器人技能大概率比语言需要*更多*
  数据,而不是更少。他称近期的人形机器人宣传为"炒作……远远超出该领域研究者所熟悉
  的机器人能力水平"。
- **两大阵营。** Goldberg 的配套论文(合著者来自 MIT、Georgia Tech、ETH Zürich)
  勾勒出该领域的核心分歧:*规模化数据*("数据就是我们所需要的一切") vs.
  *老派扎实工程*(模型、物理、控制)。Goldberg 本人的立场是一种自举策略:先把
  机器人工程做到足够好可以卖出去,再从部署中收集数据——参见[数据](data.md)。
- **哪种数据?** 截至 2026 年,各方押注大致如下:

| 数据来源 | 代表方 | 优点 | 缺点 |
|---|---|---|---|
| 真实机器人遥操作(teleoperation) | Physical Intelligence、AgiBot | 动作真值可靠,具备力感知 | 成本高、速度慢、覆盖窄;随操作员数量线性扩展 |
| 第一人称人类视频 | Tesla、Figure | 可利用互联网+可穿戴设备规模 | 缺乏力/触觉通道;有效精度约 1-3 厘米(Brooks) |
| 模拟/合成数据 | NVIDIA(Isaac/GR00T)、多家实验室 | 无限、廉价、安全 | 模拟到现实(sim2real)差距,尤其在接触与可变形物体上——参见[模拟](simulation.md) |
| 跨本体聚合(OXE、DROID、AgiBot World) | Google DeepMind、Levine 等 | 复用一切已有数据 | 本体不匹配;数据整理胜过单纯数量 |

- **质量 vs. 数量。** 2025 年的一项工作("Is Diversity All You Need for Scalable
  Robotic Manipulation?", arXiv 2507.06219)对"越多越好"的聚合思路提出反驳,
  认为数据的*构成*和多样性类型比原始轨迹数量更重要(未证实)。
- **反方观点:约束正在缓解。** 2025-26 年投资者/从业者的写作认为,瓶颈正通过
  可规模化的遥操作、以模拟为先的流水线、第一人称视频以及[世界模型(world
  model)](world-models.md)而逐步缓解——这正是当前融资热潮背后的支撑性假设
  (参见[投资](investment.md))。
- Sergey Levine(Physical Intelligence / Berkeley)认为,真实世界的跨本体
  机器人数据——而非模拟——才是通往机器人基础模型的道路;模拟"只是对传统
  基于模型方法的重新包装",其保真度最终总会与现实产生偏差
  (CoRL 2024 演讲,该立场持续保持至 2025-26 年)。
- **实地报道印证了这一差距(截至 2026-07)。** Stephen Witt 的《纽约客》文章
  ("Are Humanoid Robots Ready to Be Deployed?", 2026-07-06 期):目前不存在
  "无论合法与否"的关节运动轨迹数据库,即便是行星级规模的动作捕捉也需要数十年
  才能匹配 ChatGPT 级别的训练数据量。文章记录的数据采集押注包括:Neura(德国)
  已让 1000 多名产业工人穿戴动捕服(CEO David Reger:"我们正在获得,呃,大量
  数据");1X 保留付费遥操作员,部分原因正是*作为*数据渠道("这对我们来说也是
  有用的数据"——CEO Bernt Børnich),Børnich 还强调了车队级学习效应("一台机器人
  学到的东西,其他所有机器人同时都能学到";"这里确实存在数据飞轮效应")——
  Witt 推断这种网络效应"或许可以解释"1X 为何急于提前推出家用机器人。

## 2. 模拟到现实(sim2real)的局限

- **对移动/步态基本已解决。** 通过域随机化(domain randomization)实现零样本
  sim2real 已是[移动](locomotion.md)领域的标配(Humanoid-Gym 系列工作);
  2025-26 年的论文进一步拓展:PolySim(多模拟器动力学随机化,2025-10)、
  关节力矩空间扰动注入(2025-04)、用于自适应人形机器人移动的对比表征学习
  (2025-09)。
- **操作(manipulation)领域仍是开放问题。** 接触密集型、可变形物体相关、
  依赖触觉的任务仍难以被良好模拟;这正是操作数据争论(见第 1 节)存在的根本
  原因——参见[操作](manipulation.md)。
- **即便是"修复方案"本身也有局限。** 2026-06 的一篇论文《Too Much of a Good
  Thing: When sim2real Efforts Impede Policy Learning》(arXiv 2606.02636)
  指出,过度的 sim2real 努力——域随机化导致策略过于保守、模拟器锁定——本身
  也可能损害策略学习;这一纠偏措施自身也存在失效模式(单篇论文,
  Apptronik/UT Austin)。
- **诊断手段尚不成熟。** "Robot Policy Evaluation for Sim-to-Real Transfer"
  (arXiv 2508.11117)指出,该领域甚至缺乏公认的方法来*衡量*迁移质量,这与
  第 6 节的评测危机直接相关。

## 3. 灵巧度差距

- **生物学基线。** 人类无毛(光滑)手部皮肤携带约 1.7 万个低阈值机械感受器,
  每个指尖约 1000 个,分布在约 15 个专门的神经元家族中(压力、振动、滑动、
  温度)。目前没有任何机器人手能接近这一水平(Brooks,2025-09)。
- **Brooks 的核心技术论点。** 每一个实现了"端到端"的机器学习领域(语音、
  视觉、LLM)此前都经历了数十年针对该领域的专门输入编码方案(声谱图、卷积、
  分词)。触觉尚无对应的预处理体系,因此仅靠视频训练灵巧度"没有采集到正确的
  数据"——这一批评直指 Tesla 和 Figure 的人类视频数据流水线。
- **硬件在进步,但仍远远落后。** F-TAC Hand(*Nature Machine Intelligence*,
  2025,北京大学主导)通过 17 个基于视觉的触觉传感器,在约 70% 的手部表面
  实现了 0.1 毫米空间分辨率的触觉覆盖;来自人类示范的视觉-触觉预训练可提升
  样本效率和 sim2real 鲁棒性(2026 年报告)。参见[硬件](hardware.md)。
- **为何这在经济上至关重要。** Brooks 认为灵巧操作是通用人形机器人能否算得过
  经济账的*决定性*要求;若不具备灵巧操作能力,它们就只是造价高昂、干着搬箱子
  这类轮式机器人能更便宜完成的工作的移动平台。
- **主流框架(截至 2026-07)。** Witt(《纽约客》,2026-07-06 期)认为手部
  可能是人形机器人的"缺失一环":人类的手能执行 27 种独立动作,而"我们距离
  一台既能系鞋带又能洗牌的机器人还有好几年";机械工程本身(例如 1X 的
  肌腱驱动手指,经受住 286 万次循环的耐久测试)"远远领先于驱动它的人工智能"。

## 4. 可靠性——"多个 9"的问题

- **演示 ≠ 部署。** VLA 论文中 70-95% 的实验室/基准成功率司空见惯;而物流和
  制造业客户将 99% 视为*失败*,因为 1% 的错误率意味着需要持续人工介入,
  摧毁投资回报率。多个"9"(99.9% 以上)才是无人值守运行的隐含门槛。
- **公开报道的部署数据(均为公司口径,需谨慎对待):**
  - Figure 02 在 BMW Spartanburg 工厂:支持了超过 3 万辆 BMW X3 的钣金装载
    部署,历时 11 个月,已于**2025-11 结束**(机器人已退役,并未扩大规模);
    共装载超过 9 万个零件,累计运行超过 1250 小时,单班次声称精度超过 99%
    (公司公布的数据,被广泛转载但未经独立审计)。
  - BMW Leipzig 试点:在为期 90 天的评估中,车身白车身分总成任务成功率达
    94.3%(未证实,单一二手信源)。
  - Agility Digit:商用部署量最大的人形机器人,截至 2026-06 全球约 75 台
    (未证实的跟踪估算);参见[人形机器人](humanoid-robots.md)。
  - 截至 2026-01,全球商业场景中约有 3000 台人形机器人,只有约 40% 的试点
    项目能在 24 个月内进入量产(未证实的市场研究)。
- **结构性问题。** 自回归学习策略的失败方式不可预测且非局部性,目前尚无公认
  的工程学科(如 FMEA 式方法)来为一套学习策略的失效边界进行认证——这与
  第 5、第 6 节直接相关。
- **演示与现实的第一手对比(《纽约客》,截至 2026-07)。** Stephen Witt 的
  实地报道("Are Humanoid Robots Ready to Be Deployed?", 2026-07-06 期):
  1X 那段流畅的 Neo 厨房演示实际上是由一名戴 VR 头显的遥操作员操控的
  ("我看到的机器人其实是个木偶");1X 拒绝展示 Neo 的自主 AI 能力;1X
  产品负责人 Dar Sleeper 谈及跌倒问题时说:"说它不会摔倒,这话说得,有点
  夸张了。"CEO Bernt Børnich 正明确地在测试消费者对"机器人瑕疵"
  (robotics slop,笨拙执行的任务)的容忍度——已有超过 1 万份定金,
  定价为 2 万美元,承诺 2026 年交付到家。就在风投人 Modar Alaoui 对 Witt
  说"移动能力问题已经解决"的第二天,一台 Xpeng Iron 在深圳一家商场的演示中
  突然僵住并摔倒,需要三名工作人员才能把它拖走;Unitree 春节功夫表演
  被认为是预先编排的脚本(据 Witt 分析,很可能源自动作捕捉)。
- **对可靠性发表明确立场者(同一篇文章):** Aaron Ames(Caltech)——无论
  工程多么精巧,自主机器人的可靠 AI 都还要等好多年。Carolina Parada
  (Google DeepMind 机器人负责人)——家庭部署的瓶颈在于安全性,而非兴趣
  或能力:"能完成后空翻的同一台机器人,可能连一段楼梯都爬不上去。"
  Deepu Talla(NVIDIA 机器人业务)——"这个世界目前还没有机器人版的
  ChatGPT"(相比 Huang 那种"即将到来"的措辞明显更为谨慎,见第 8 节)。
- **遥操作作为隐藏的介入层。** 文章记录了遥操作在全行业范围内支撑着所谓
  "自主"系统:Waymo 在菲律宾雇用的专业远程"飞行员"、日本 7-Eleven 门店中
  的 VR 远程理货、以及 1X 计划让操作员坐在其 AI 团队旁边(Neo 的耳机指示灯
  会变色以披露远程控制状态)。1X 此前曾以遥操作作为卖点进行营销,后来在
  客户反弹之后转而围绕 AI 重新包装——但并未放弃遥操作本身。

## 5. 安全与认证

- **ISO 10218-1/-2:2025**(2025 年初发布,自 2011 年以来的首次重大修订):
  功能安全要求被明确化,网络安全问题得到处理,**ISO/TS 15066**(协作机器人
  力/压力限值)被并入 10218 系列——协作运行如今被界定为一组*应用场景*,
  而非某一类机器人。美国通过 ANSI/A3 R15.06-2025 采纳该标准。
- **人形机器人留下的空白。** 上述标准均假定机器人为固定基座或静态稳定型。
  一台动态平衡的双足机器人*永远*不可能是被动安全的——紧急停止有可能意味着
  摔倒。目前有两种应对:
  - **ISO 25785-1**——针对动态稳定(主动平衡)工业移动机器人的安全要求,
    由 ISO/TC 299 制定:截至 2026-01 仍处于工作草案(Working Draft)阶段,
    已于 2026-05-12 启动委员会草案(Committee Draft)投票;预计 2026-27
    年发布(时间未证实)。
  - **IEEE 人形机器人研究组报告**("A Pathway Study for Future Humanoid
    Standards",发布于 2025-09-25,由 ASTM International 的 Aaron Prather
    牵头,60 余位贡献者参与):这是一份路线图,而非正式标准,指出了三个
    差距领域——分类/分类法、稳定性指标与跌倒响应、以及人机交互。估计
    **首批正式人形机器人标准需要 18-36 个月**,而在人类周围安全大规模部署
    最早也要到约 2027 年。
- **中国率先在国家层面推进。** 由工信部/TC08 于 2026-02-28 发布的《人形机器人
  与具身智能标准体系(2026 版)》,有 120 余家参与机构:六大部分框架(基础
  共性;类脑与智能计算;肢体与部件;整机;应用;安全与伦理),已发布首批
  52 项标准清单,12 项国家/行业标准项目正在推进(由中国电子技术标准化研究院
  CESI 牵头管理),此外还发布了具身智能评测基准首个版本(EIbench,由 CESI
  发布)。这使中国有望事实上主导全球规则的制定——参见
  [中国全景](landscape-china.md)。
- **Brooks 的实用法则:** 与行走中的全尺寸人形机器人保持约 3 米距离;
  跌倒能量的增长很不利(体型翻倍→质量增至 8 倍),而基于零力矩点(ZMP)
  的平衡方式本身就在主动向系统中注入动能。
- **《纽约客》文章中从业者的警示(截至 2026-07):** Apptronik CEO
  Jeff Cardenas——"在小型宠物、小孩子周围,还有很多工作要做";Apptronik
  在 Mercedes-Benz 工厂的 Apollo 机器人仍被围栏与人类工人隔开。Aaron Ames
  (Caltech)谈及 1X 计划于 2026 年将 Neo 送入家庭:"如果这些机器人中有一台
  摔到人身上,我会担心其中的法律后果。"文章还提到安全研究员 Andreas Makris
  和 Kevin Finisterre 发现的 Unitree G1 蓝牙漏洞(可自我传播的"机器人僵尸网络",
  2025 年),以及一台 G1 在中国某游乐场踢到一名幼儿的事件——攻击面与摔倒/
  击打风险已成为部署的首要障碍。

## 6. 评测危机

- **问题所在。** 真实机器人评测速度慢、难以规模化、存在安全隐患,且在不同
  实验室之间难以复现;论文往往自行挑选任务、以小样本量运行且不做统计检验,
  结果无法在不同装置间迁移。VLA 模型在分布外(OOD)环境中表现出明显的性能
  骤降,因此实验室内的数字系统性地高估了真实能力。
- **《10 Open Challenges》(arXiv 2511.05936,AAAI 2026)** 将评测列为该
  领域十大核心开放问题之一(与数据、安全、跨机器人泛化、全身协调并列)。
- **2025-26 年的应对措施:**

| 举措 | 日期 | 方法 |
|---|---|---|
| RobotArena ∞(arXiv 2510.23571) | 2025-10 | 将视频进行真实到模拟的转译;分布外泛化测试 |
| AutoEval | 2025 | 对通用策略进行自主的真实世界评测,最大限度减少人工投入 |
| REALM(arXiv 2512.19562) | 2025-12 | 经真实到模拟验证的泛化能力基准 |
| RoboChallenge | 2025-26 | 标准化的大规模真实机器人评测平台 |
| VLA-REPLICA(arXiv 2605.20774) | 2026-05 | 低成本、可用现成器材、可在实验室复现的物理基准 |
| 中国 EIbench | 2026-02 | 国家背书的具身智能基准(见第 5 节) |

- **统计严谨性的推动。** 2025-26 年关于策略比较的近最优停止规则以及可重复
  性能测量方法的论文,正在攻克小样本量、缺乏显著性检验这一普遍问题
  (单个结果未经证实)。目前尚无任何基准能扮演 ImageNet 或 MMLU 那样的角色——
  [最新进展(state of the art)](state-of-the-art.md)中的 SOTA 声明应当据此
  审慎看待。

## 7. 人形机器人形态之争

- **支持人形形态的理由:** 现有建成环境是为人类身体设计的(楼梯、货架、
  工具、车辆);单一通用型号可将研发成本摊薄到每一项任务上;人类视频
  (可以说)可以直接作为训练数据使用。支持方包括 Tesla、Figure、1X、
  Agility,以及大多数中国生态系统企业——参见[人形机器人](humanoid-robots.md)。
- **反对意见(Brooks,2025-09):** 双足机器人在人类周围本质上具有危险性
  (见第 5 节);灵巧度不会来自视频(见第 3 节);而且经济性更偏向任务
  形态定制的机器。他对 15 年后的预测是:届时的机器仍然会被*称为*"人形
  机器人",但会带轮子、配备任务专用夹爪和非人类传感器——随着泡沫破裂,
  定义本身会被悄悄改变("挪动球门柱")。
- **中间立场:** Goldberg 并不否定人形这一形态,只是质疑其时间表;Agility
  已经在出售一种实用主义的半人形机器人(Digit 采用板簧式腿部,2025 年前
  都没有五指手);多家仓储运营商认为,轮式底盘+人形躯干在成本和正常运行
  时间上更胜一筹(许多中国厂商已在销售这种配置)。
- 这场争论正是 2025-12 硅谷人形机器人峰会的公开背景,尽管 Brooks 本人缺席,
  他的文章却被反复引用(据 AP 报道)。
- **新出现的"反对"声音(《纽约客》,截至 2026-07):** Autodesk 高级研究员
  Mike Haley(拥有工厂机器人领域的从业生涯)表示他"从未见过人形机器人在
  工业场景中做过任何有用的事"——任务形态定制的机器(独立式喷涂手臂、
  自主叉车)在成本、运动部件数量和维护性上都更胜一筹:"我们回头看这场人形
  机器人的热潮,会说:'天啊,那真是蠢透了。'"Skild AI 联合创始人 Deepak
  Pathak(CMU)拒绝在自己家里放一台人形机器人,并认为这种形态本身具有
  误导性:"人们正在利用外观来误导公众。如果你把机器人做得像人,人们就会
  期待它具备人类般的能力。但技术水平远远达不到。"(Skild 自身的押注——
  一个可用于任何身体、无论是否人形的跨本体"大脑"——正是对这一形态之争的
  一种对冲。)
- **各地区的接受态度存在明显分化(截至 2026-07)。** Witt(同一篇文章)
  援引了一项覆盖约三十多个国家的斯坦福意见调查分析:**中国、韩国、泰国、
  印度尼西亚**的受访者对 AI 消费级应用**最为兴奋**;**美国和加拿大**受访者
  兴奋程度**最低**。这与斯坦福 HAI 的《AI Index》公众舆论章节相符:
  2025 版(Ipsos 2024 年调查,32 个国家)显示,中国(83%)、印度尼西亚
  (80%)、泰国(77%)的受访者中有大量多数认为 AI 产品利大于弊,相比之下
  加拿大为 40%、美国为 39%,并将中国、韩国、印度尼西亚列为高度兴奋的
  聚类;2026 版(Ipsos 2025 年调查,30 个国家)延续了同样的模式——中国、
  马来西亚、泰国、印度尼西亚均有超过 80% 的受访者预期 AI 将深刻改变他们的
  生活,而美国/加拿大则处于低兴奋度、高紧张感的一端。Witt 原文的措辞是
  "AI 消费级应用"——机器人只是文章的语境,并非调查问题本身。Witt 的文化
  解读是:从卡佩克(Čapek)到《终结者》的叙事传统玷污了西方的观感,而
  Neura 的 CEO 则表示,韩国记者们只是单纯"等得不耐烦了"。这是一个态度层面
  的数据点,而非需求预测——但它与 NEO 等家用人形机器人"美国优先"的
  上市策略相悖,提示东亚/东南亚或许才是更愿意接受的早期消费市场。

## 8. 时间线话语——谁在主张什么

| 发言人 | 立场(附日期) |
|---|---|
| Elon Musk(Tesla) | 约 2026 年实现 AGI,Optimus 在 2026 年底前完成"复杂任务";年化 Gen-3
产量目标据报道从约 5 万台上调至约 7 万台(2026 年,供应链报道,未证实)。
过往记录:自 2022 年以来 Optimus 的每一次重大时间表都未能兑现;2025 年
约 5000 台的目标最终只交付了数百台(超过 90% 落空,Musk 在 2025 年二季度
财报电话会上证实);在 2026-01 的 2025 年四季度财报电话会上,Musk 表示
尚无 Optimus 正在从事有用的工厂工作;Gen-3/V3 发布再次推迟至 2026 年中
(Electrek,2026-04)。 |
| Jensen Huang(NVIDIA) | "机器人领域的 ChatGPT 时刻近在眼前"(2024-25);
人形机器人是一个"40 万亿美元市场"(2026-05,被广泛报道);据称在 2026-03
Lex Fridman 节目中说"我认为我们已经实现了 AGI"(未证实)。 |
| Brett Adcock(Figure) | 家用级人形机器人即将到来;Helix 是突破性进展;
Figure 估值达 390 亿美元(2025-09)。怀疑者对实际部署台数和演示条件提出
质疑;Adcock 公开否认 Figure 家用机器人测试中存在遥操作(Bloomberg,
2026-05)。 |
| Rodney Brooks(MIT/iRobot) | 数十年内实现人类水平的手部技能是"纯粹幻想";
*在灵巧度最低要求下*首个盈利的人形机器人部署至少需要 10 年以上;预测资金
崩溃以及定义层面的"挪动球门柱"(2025-09)。 |
| Ken Goldberg(UC Berkeley) | 无论"2 年、5 年,甚至 10 年"内都不会出现机器人
外科医生/管家;存在 10 万年的数据差距;通过工程+部署数据实现自举
(2025-08)。 |
| Sergey Levine(Physical Intelligence) | 对机器人基础模型持乐观态度,但前提
是依靠大规模的真实世界跨本体数据,而非单纯依赖模拟或视频;时间表取决于
数据飞轮能否真正转动起来。 |
| Bernt Børnich(1X) | 人形机器人"几乎什么都能做";Neo 将于 2026 年交付到家——
"这是我们必须兑现的承诺"(据产品负责人 Dar Sleeper 转述);押注消费者会
在车队学习不断提升自主性的同时,接受"机器人瑕疵"及经过披露的遥操作
(《纽约客》,2026-07)。 |
| Aaron Ames(Caltech) | 无论工程多么精巧,自主机器人的可靠 AI 都还要等好多年;
"我不知道 1X 到底打算怎么应对"——指出家用人形机器人跌倒事故的法律风险
(《纽约客》,2026-07)。 |
| IEEE/ASTM 标准社区 | 人形机器人在人类周围安全大规模部署最早约 2027 年;
首批正式标准需要 18-36 个月(2025-09)。 |
| 专家调查 | AGI 的中位数预期时间已从(约 2010 年时的)50-100 年,推进到
2026 年时的约 5-15 年(未证实的汇总数据)。 |

- **元观察。** 主张短时间表的声音最响亮的,往往是机器人或算力的卖方;
  主张长时间表的声音最响亮的,往往是没有损益表压力的学界人士——双方
  都各有其利益驱动。值得关注的实证试金石是:在标准落地(见第 5 节)之前,
  是否有任何人形机器人部署,在具备真实劳动经济价值的任务上,达到了无人
  值守的多个"9"级可靠度(见第 4 节)。关于"谁是谁",参见
  [关键人物](key-people.md)与[组织机构](organizations.md)。

## 来源

- https://rodneybrooks.com/why-todays-humanoids-wont-learn-dexterity/ — Brooks 文章(2025-09):机械感受器数量、视频数据批判、双足安全性、10 年以上/15 年预测、3 米法则。
- https://techcrunch.com/2025/09/26/famed-roboticist-says-humanoid-robot-bubble-is-doomed-to-burst/ — TechCrunch 对 Brooks 文章的报道,泡沫论框架,Figure 390 亿美元估值。
- https://news.berkeley.edu/2025/08/27/are-we-truly-on-the-verge-of-the-humanoid-robot-revolution/ — Goldberg 的 10 万年数据差距计算,Science Robotics 论文(2025-08-27),数据 vs. 工程之争。
- https://techxplore.com/news/2025-08-year-gap-robots-lag-ai.html — 对 Goldberg 数据差距计算的二手报道。
- https://arxiv.org/abs/2511.05936 — "10 Open Challenges Steering the Future of VLA Models"(AAAI 2026):涵盖数据、评测、安全在内的权威开放问题清单。
- https://arxiv.org/pdf/2507.06219 — "Is Diversity All You Need for Scalable Robotic Manipulation?" ——数据质量 vs. 数量之争。
- https://arxiv.org/pdf/2508.17449 — 模仿学习综述:领域内数据稀缺是根本瓶颈。
- https://medium.com/@jianming.wang07/robotic-foundation-models-corl-2024-sergey-levines-talk-notes-e42bb3eb618e — Levine 关于真实世界跨本体数据立场的演讲笔记(二手来源)。
- https://arxiv.org/pdf/2404.05695 — Humanoid-Gym:人形机器人移动零样本 sim2real 基线工作。
- https://arxiv.org/pdf/2606.02636 — "Too Much of a Good Thing":域随机化可能阻碍策略学习。
- https://arxiv.org/pdf/2508.11117 — sim-to-real 迁移的机器人策略评估:尚无公认的迁移度量指标。
- https://github.com/YanjieZe/awesome-humanoid-robot-learning — 2025-26 年 sim2real 论文索引(PolySim、力矩扰动注入)。
- https://www.nature.com/articles/s42256-025-01053-3 — F-TAC Hand:高分辨率触觉覆盖(Nature Machine Intelligence 2025)。
- https://arxiv.org/html/2507.11840v1 — 灵巧/具身操作综述:灵巧度差距框架,遥操作力反馈局限。
- https://www.automate.org/robotics/news/updated-iso-10218-major-advancements-in-industrial-robot-safety-standards-now-available — A3 关于 ISO 10218:2025 的公告;TS 15066 并入情况。
- https://www.wideautomation.com/en/robotic-safety-what-changes-with-the-new-iso-102182025-standards/ — ISO 10218:2025 生效及变化内容。
- https://www.therobotreport.com/ieee-study-group-publishes-framework-for-humanoid-standards/ — IEEE 人形机器人标准框架:Prather、60 余位贡献者、18-36 个月、约 2027 年。
- https://spectrum.ieee.org/domestic-humanoid-robot-safety-standards — IEEE Spectrum 关于家用人形机器人安全标准转变的报道。
- https://theresarobotforthat.com/blog/humanoid-robot-safety-standards-2026/ — ISO 25785-1 工作草案状态,ANSI/A3 R15.06-2025(二手来源)。
- https://sesec.eu/2026/04/01/chinas-first-standards-system-for-humanoid-robots-and-embodied-intelligence/ — 中国 HEIS 2026 标准体系详情。
- https://govt.chinadaily.com.cn/s/202603/02/WS69a5171c498e23165e06dc3c/china-introduces-a-standard-framework-for-humanoid-and-embodied-intelligence.html — 官方中文报道:2026-02-28 发布,六大部分,工信部/TC08,EIbench。
- https://arxiv.org/html/2510.23571v1 — RobotArena ∞:真实到模拟的 VLA 基准测试,分布外泛化下降情况。
- https://arxiv.org/pdf/2605.20774 — VLA-REPLICA:低成本可复现的真实世界 VLA 基准(2026-05)。
- https://arxiv.org/pdf/2512.19562 — REALM 真实到模拟验证的操作泛化基准。
- https://abcnews.go.com/Technology/wireStory/humanoid-robots-center-stage-silicon-valley-summit-skepticism-128353889 — AP 对 2025-12 人形机器人峰会的报道;Brooks 文章在业内的广泛回响。
- https://www.iiot-world.com/artificial-intelligence-ml/robotics/physical-ai-deployment-roi-humanoid-robots/ — BMW/Figure 3 万辆汽车和 99% 精度声明(二手来源,公司口径)。
- https://www.figure.ai/news/production-at-bmw — Figure 官方文章:超 3 万辆 X3、超 9 万个零件、超 1250 小时、单班次超 99% 装载精度。
- https://www.repairerdrivennews.com/2025/11/25/humanoid-robots-complete-11-month-project-at-bmw-plant/ — BMW Spartanburg 部署历时 11 个月后结束(2025-11);机器人已退役。
- https://www.iso.org/standard/91469.html — ISO/CD 25785-1 目录条目:委员会草案阶段(30.20 CD 投票,2026-05)。
- https://www.automate.org/robotics/news/new-ansi-a3-r15-06-2025-american-national-standard-for-industrial-robot-safety-now-available-for-purchase — ANSI/A3 R15.06-2025 第 1-2 部分作为美国对 ISO 10218:2025 的采纳;第 3 部分为美国自行制定。
- https://electrek.co/2026/04/22/tesla-optimus-production-fremont-model-sx-line/ — Optimus V3 发布再次推迟至 2026 年中;Fremont 产线改造。
- https://finance.biggo.com/news/e77c6e9b-d703-45fc-906d-1ea3d1272482 — 据报道 Optimus Gen-3 年化目标从约 5 万台调整为约 7 万台(供应链报道,未证实)。
- https://axis-intelligence.com/humanoid-robots-deployment-2026-case-studies/ — 截至 2026-01 全球商业场景约 3000 台人形机器人;试点到量产比例(未证实的市场研究)。
- https://finance.yahoo.com/markets/stocks/articles/why-teslas-optimus-story-more-153200371.html — Optimus 目标落空情况核算(二手来源)。
- https://www.bloomberg.com/news/videos/2026-05-15/figure-ceo-says-humanoid-robot-test-had-no-outside-aid-video — Adcock 否认 Figure 家用测试中存在遥操作。
- https://247wallst.com/investing/2026/05/31/jensen-huang-just-called-humanoid-robots-a-40-trillion-market-heres-why-wall-street-is-loading-up-on-physical-ai-stocks/ — Huang 40 万亿美元市场声明(2026-05,二手来源)。
- https://www.newyorker.com/magazine/2026/07/06/are-humanoid-robots-ready-to-be-deployed — Stephen Witt,"Are Humanoid Robots Ready to Be Deployed?"(2026-07-06 期):1X Neo 遥操作演示与"机器人瑕疵"、Ames/Parada/Talla/Cardenas/Pathak/Haley 各方立场、Xpeng Iron 摔倒事件、Neura 动捕项目、遥操作经济、斯坦福跨国态度调查(付费墙内容;通过 Wayback 2026-07-03 快照全文阅读)。
- https://hai.stanford.edu/ai-index/2025-ai-index-report/public-opinion — 斯坦福 HAI《AI Index》2025 公众舆论章节(Ipsos 2024 年调查,32 个国家):Witt 所引用的中国 83% / 印度尼西亚 80% / 泰国 77% vs. 加拿大 40% / 美国 39% 的利弊评价分化,以及中国/韩国/印度尼西亚高兴奋度聚类的数据来源。
- https://hai.stanford.edu/ai-index/2026-ai-index-report/public-opinion — 斯坦福 HAI《AI Index》2026 公众舆论章节(Ipsos 2025 年调查,30 个国家):同样的模式延续(中国/马来西亚/泰国/印度尼西亚均超过 80% 的乐观度;美国/加拿大兴奋度最低、紧张感最高)。
