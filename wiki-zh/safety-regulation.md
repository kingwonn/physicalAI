---
title: 安全与监管
slug: safety-regulation
updated: 2026-07-04
confidence: verified
lang: zh
source: ../wiki/safety-regulation.md
---
> 截至 2026 年年中,安全标准是人形机器人从演示走向规模化部署之间公认的瓶颈。专门针对平衡控制机器人的标准——ISO 25785-1(由 ISO/TC 299 WG 12 制定,美方代表团项目负责人来自 Agility Robotics、Boston Dynamics 和 A3)——于 2026-05-12 进入委员会草案(CD)阶段,预计 2027 年前后发布;在此之前,人形机器人只能依据 ISO 10218:2025(已吸收协作机器人技术规范 TS 15066)、ANSI/RIA R15.08(移动机器人)、ISO 12100/13849 风险评估,以及面向消费/服务机器人的 UL 3300(已于 2025-12-31 列入 OSHA 的 NRTL 测试标准清单)分别进行零散认证。欧盟在 AI Act 之上叠加了《机械设备条例》2023/1230(2027-01-20 起适用),而 AI Act 的高风险条款截止日期在 2026 年的"数字综合法案(Digital Omnibus)"中被推迟到 2027 年末/2028 年。中国在纸面标准上推进最快:工信部成立了国家级人形机器人标准化委员会(2025-12-26,宇树科技和智元机器人创始人担任副主任),并发布了 HEIS 2026——首个面向人形机器人与具身智能的国家标准体系(首批 52 项标准)。Agility 的 Digit 在一个实体运营的物流中心内获得了首个 OSHA 认可的人形机器人 NRTL 现场认证(2025-11);真正意义上无围栏的"协作安全"运行以及经认证的家庭部署(1X NEO 计划于 2026 年末交付)仍走在标准的前面,而非落后于标准。

## 标准体系一览(截至 2026-07)

| 文件 | 范围 | 状态 | 对人形机器人的意义 |
|---|---|---|---|
| ISO 10218-1/-2:2025 | 工业机器人 + 机器人应用/单元 | 2025 年发布(自 2011 年以来首次修订) | 任何工厂人形机器人的基线标准;现已纳入协作应用要求、功能安全、网络安全 |
| ISO/TS 15066:2016 | 协作机器人操作(功率/力限值、身体部位阈值) | 已基本并入 ISO 10218-2:2025 | 四种协作模式被逐字保留;"协作机器人"这一术语被"协作应用"取代 |
| ANSI/A3 R15.06-2025 | ISO 10218 的美国国内采纳版本(共 3 部分) | 历时约 8 年,于 2025-09 发布 | 美国工业机器人安全的法律参照;新增面向用户的第 3 部分 |
| ANSI/RIA R15.08 | 工业移动机器人(AMR) | 现行有效;第 3 部分面向用户 | Digit 2025 年 NRTL 现场检测的依据;是轮式移动操作臂机器人最贴近的适用标准 |
| **ISO 25785-1** | **动态稳定型工业移动机器人(腿式/轮式/其他形式)** | **委员会草案(CD)已于 2026-05-12 登记(ISO/TC 299 WG 12)** | 首个专为需要主动保持平衡的机器人制定的标准——双足、四足、轮式平衡机器人 |
| ISO 13482:2014 | 个人护理/服务机器人 | 2014 年发布,被广泛认为对动态稳定型人形机器人已显过时(未证实的表述) | 唯一现有的、面向在未受训人员周围工作的机器人的 ISO 安全标准 |
| ANSI/CAN/UL 3300:2024 | SCIEE 机器人(服务、通信、信息、教育、娱乐)含人形机器人 | 首版于 2024-05 发布;ANSI/SCC 批准版本于 2025-04-16;已于 2025-12-31 列入 OSHA NRTL"适用测试标准"清单 | 北美消费级/家用及商用服务型人形机器人最可能的认证路径 |
| ISO 12100 / ISO 13849 | 机械风险评估/安全相关控制系统 | 长期沿用的标准 | 当前所有人形机器人部署实际依据的横向标准 |
| 欧盟《机械设备条例》2023/1230 | 所有机械设备,含具备自我演化能力的机器学习安全功能 | 2027-01-20 起适用 | 使基于机器学习的安全行为在欧盟成为强制性第三方符合性评估路径 |
| 欧盟 AI Act | AI 系统,含产品的安全组件 | 2026-08-02 全面适用;高风险条款截止日期已推迟(见下文) | 具身智能系统可能在机械合规之上被认定为"高风险 AI" |
| 中国 HEIS 2026 | 面向人形机器人+具身智能的国家标准*体系* | 2026-02-28 发布;首批 52 项标准 | 首个综合性国家框架;将中国立场输入 ISO/IEC |

## ISO 25785-1——人形机器人的标准空白被填补

- 全称:《机器人学——动态稳定型工业移动机器人(腿式、轮式或其他运动形式)的安全要求——第 1 部分:机器人》。属于 **ISO/TC 299(机器人学)工作组 12** 下的 **C 类**(特定机型)安全标准。
- 覆盖需要主动保持平衡才能站立的机器人——双足/人形、四足、三足形式,以及轮式自平衡机器人。现有标准(10218、R15.08)默认机器人静态稳定;失衡、跌倒行为及平衡状态下的安全停止是新的危险类别。
- 时间线:工作组会议于 2025-10 在巴塞罗那召开;**CD(委员会草案)于 2026-05-12 登记**(ISO 目录中列为 ISO/CD 25785-1);多方预计 2027 年发布(部分报道称 2026 年末,较为乐观)——CD → DIS → FDIS 各阶段仍在进行中。
- 美方代表团负责人:**Kevin Reese(Agility Robotics,项目负责人)、Federico Vicentini(Boston Dynamics,安全负责人)、Carole Franklin(A3,机器人标准开发总监)**。
- 配套工作:**IEEE 人形机器人研究组**(由 Aaron Prather 领导,ASTM)发布了《未来人形机器人标准路径研究》(2025 年),在分类、稳定性、人机交互三个方面梳理了所需工作,并协调各标准制定机构;Prather 预计需 18-36 个月才能形成正式标准,并表示规模化人形机器人部署实际上要等到 2027 年前后。参见[开放问题](open-problems.md)。

## ISO 10218:2025 与"协作机器人"概念的终结

- 2025 年修订版(自 2011 年以来首次)是十多年来最大规模的工业机器人安全体系改造。主要变化:澄清了**功能安全**要求,新增**网络安全**要求(在其影响安全的范围内),更新了机器人分类、末端执行器及人工装卸相关内容,以及最重要的一点——将 **ISO/TS 15066 的大部分内容并入**第 2 部分。
- 术语变化:不再使用"协作机器人"/"协作操作",而只使用**"协作应用"**,因为安全只能在应用层面(机器人+末端执行器+工件+单元)设计和验证,而非仅针对机器人本身。TS 15066 的四种协作模式(含带身体部位阈值的功率与力限制)得以保留。
- 美国采纳情况:**ANSI/A3 R15.06-2025** 于 2025-09 发布(第 1-3 部分;第 3 部分是新增的、面向用户的指南)。A3 将其定位为"智能自动化时代安全"的路线图。

## 美国消费/服务领域路径:UL 3300

- **ANSI/CAN/UL 3300**(服务、通信、信息、教育、娱乐机器人标准,即 SCIEE 标准)明确将人形机器人、家用机器人、陪伴机器人、配送机器人、外骨骼及移动服务机器人纳入范围;其重点是保障普通人(包括残障用户)周围的安全运行。
- **2025-12-31,OSHA 将 UL 3300 加入 NRTL 项目的"适用测试标准清单"**,使其可用于在美国商业/企业环境中部署的 SCIEE 机器人的认证。
- UL Solutions 开设了首个专门的服务机器人测试实验室;UL 3300 涵盖多方向移动性、防火/防电击、外部操控、用户分类及使用环境等内容。

## 欧盟:双层监管体系(机械设备 + AI)

- **《机械设备条例》(EU) 2023/1230** 取代了原《机械设备指令》,**自 2027-01-20 起适用**。在**安全功能**中使用"完全或部分自我演化行为(基于机器学习)"的机械设备被列入高风险清单→须进行强制性(第三方)符合性评估。任何其学习型策略执行安全功能的人形机器人都完全落入该范围。
- **欧盟 AI Act**:2024-08-01 生效;通用人工智能(GPAI)义务自 2025-08 起适用;全面适用日期为 **2026-08-02**。**AI 数字综合法案**(2025-11-19 提出;2026-05-07 达成临时三方协议,2026-05-13 经 COREPER 确认;欧洲议会于 2026-06-16 批准;欧盟理事会于 2026-06-29 最终批准)推迟了高风险制度的实施:独立的(附件 III)高风险系统最迟于 **2027-12-02** 适用,**嵌入产品**的高风险 AI(即人形机器人的情形)最迟于 **2028-08-02** 适用。
- 该综合法案还将《机械设备条例》移入了**附件 I B 部分**,这意味着 AI Act 第三章的义务不再直接适用于嵌入机械设备的 AI;取而代之的是,欧盟委员会须通过授权法案,在 **2028-08-02 前**将 AI 相关的健康/安全要求纳入《机械设备条例》,而仅用于便利性/优化(非安全)目的的 AI 则被排除在"安全组件"之外。整体效果:欧盟人形机器人将在约 2027-28 年迎来一条以机械设备为核心的合并合规路径。

## 中国:HEIS 2026 与标准竞赛

- 工信部于 **2025-12-26** 正式成立了**人形机器人与具身智能标准化技术委员会(MIIT/TC08)**。副主任委员包括**王兴兴(宇树科技创始人)**和**彭志辉(智元机器人联合创始人/CTO)**——制造商代表坐上了主导席位。参见[中国格局](landscape-china.md)与[关键人物](key-people.md)。
- **2026-02-28**,工信部在北京亦庄发布了**人形机器人与具身智能标准体系(2026 版,即"HEIS 2026")**——全球首个面向人形机器人/具身智能的综合性国家标准体系。共分六大板块:基础共性;类脑智能与智能计算;肢体与部件;整机系统与集成;应用;以及**贯穿全生命周期的安全与伦理**。首批公布了 **52 项**标准,由 **120 余家**科研机构/企业起草,并获得中国电子技术标准化研究院(CESI)的结构性支持。
- 该体系明确旨在将中国立场输入 **ISO/IEC**——在 ISO 25785-1 仍处于 CD 阶段之际,这是一次刻意争夺国际人形机器人规则先发影响力的举动。西方媒体将此描述为一场"标准竞赛";但需注意 HEIS 2026 目前只是框架/路线图,尚非认证体系(这一区别在相关报道中常被忽视)。

## 实践中的认证关卡

**无围栏工厂作业**
- 目前的部署案例(Figure 在宝马工厂、Digit 在 GXO、Apollo 在梅赛德斯——参见[人形机器人](humanoid-robots.md))都在**限制区域或隔离区域**内运行;目前没有任何人形机器人获得在无保护工人周围自由移动、协作作业的认证。
- **Agility Robotics** 宣布(2025-11-25)在一个实体运营的电商物流中心内完成了首个 **OSHA 认可的人形机器人 NRTL 现场检验**——针对周转箱搬运工作流程,依据 **ANSI/RIA R15.08、ISO 13849、ISO 12100** 进行评估。该批准是**特定场地**的(该配置、该设施),但确立了一个可复制的模板。Agility 的安全团队还将 ANSI B11.0/B11.19 和 ISO 10218 列为其基础合规依据;其宣称的 TÜV 莱茵对其 ISO 12100 风险评估的验证未能独立核实(未证实)。
- Agility 将 Digit v5(基于 NVIDIA Halos 构建)宣传为首款"协作安全"人形机器人;其 CEO 关于实现协作安全的目标时间已从"18 个月内"(2024 年末提出)推迟到 **2027 年初**(未证实的单一来源时间线)。在 ISO 25785-1 发布之前,"无围栏"的说法尚无专门标准可供认证。

**家庭部署**
- **1X NEO**(计划于 2026 年末开始美国家庭配送,售价 2 万美元或每月 499 美元;Hayward 工厂已于 2026-05-01 开业,首批量产机型交付内部测试人员)以"安全内建设计"为卖点:约 30 公斤、腱驱动机身,柔软的 3D 网格聚合物外皮,关节全覆盖防夹伤设计,低力驱动——此外还有人类遥操作("专家模式")来处理复杂任务,这也把部分安全问题转移到了操作员审查和隐私层面。截至 2026-07,1X **尚未公布 NEO 的任何特定第三方安全认证**(未证实的缺失情况)。
- UL 3300 是北美家用人形机器人自然的认证路径;欧盟路径(《机械设备条例》+ AI Act)将在 2027-28 年落实。法律评论人士指出,在此之前家用人形机器人是产品责任领域的一个雷区。
- **护栏被绕过的风险(截至 2026-07)**:家用人形机器人继承了大语言模型的"越狱"问题,但带来了实体后果。Witt 在《纽约客》(2026-07-06 期)中描述的一个示例场景:一个持续纠缠、富有创意的孩子,把 NEO 哄骗绕过 AI 护栏去执行有害指令(例如让机器人用头撞桌子)——"研究表明,这类护栏是可以被绕过的"。值得注意的是,1X 自己的 CEO 也认同 NEO"不应在幼儿周围使用"(据 Witt 报道),但上述标准中没有一项针对大语言模型护栏的稳健性作为安全功能进行测试。
- **家庭内遥操作隐私问题**:1X 的"专家模式"意味着人类操作员可以通过 NEO 的眼部摄像头看到客户家中的情况;目前的缓解措施仅限于信息披露——操作员坐在 1X 园区内、与 AI 团队相邻的地方办公,且 NEO 的耳机指示灯在远程操作期间会变色(据 Witt 报道)。Børnich 承认这些会话同时也被用作训练数据("这对我们来说也是有用的数据"),这将家庭隐私问题与[数据工厂](data-foundry.md)中尚未解决的同意问题联系了起来;截至 2026-07,尚无任何认证或法规专门规范家庭内机器人遥操作。

## 事故、责任与保险

- **Unitree H1"抽搐"事件(2025-05,病毒式传播)**:一台吊装在工厂测试中的 H1 在工人附近剧烈抽动,拖拽着支架;操作人员将其归因于在双脚未承重的情况下运行了全身控制策略。未造成严重伤害,但成为人形机器人安全讨论中的经典案例。
- **Unitree G1 在公开演示中踢中一名儿童**,事件发生在中国的一次公开演示上(视频于 2026-06-04 传播,受到广泛报道——一台戴假发的 G1 一记回旋踢击中了一名儿童的腹部;中国媒体报道未造成严重伤害)。
- **Unitree G1 蓝牙"机器人僵尸网络"漏洞**:安全研究人员 Andreas Makris 与 Kevin Finisterre 披露(2025-09)一项 BLE 漏洞,攻击者可借此控制 G1 机群,"制造出一个无需用户干预即可自我传播的机器人僵尸网络"——该漏洞后经 Witt 在《纽约客》(2026-07-06 期)的报道再度进入大众视野。完整技术细节(UniPwn、CVE-2025-60017/-60250/-60251、披露时间线)见[宇树深度报告](company-unitree.md);此处相关的原因在于 ISO 10218:2025 现已将网络安全纳入安全标准要求,而这一可蠕虫传播的漏洞恰恰发生在全球部署量最大的研究型人形机器人上,是该要求的一个具体案例。
- **特斯拉 Fremont 工厂机械臂诉讼**:一名机器人技术人员在拆卸特斯拉 Fremont 工厂的一台 FANUC 工业机械臂时(2023-07-22)被击昏并被压住,原因是机械臂意外释放、其约 8000 磅的配重落到了他身上;他对特斯拉和 FANUC 提起的约 5100 万美元诉讼(2025 年提起,已产生约 100 万美元医疗费用+预计约 600 万美元)被媒体称为首起重大机器人工伤诉讼。该事件常被误引为人形机器人事故——实际上它是一起典型的工业机械臂事故。
- 仓储自动化背景:有报道称亚马逊的机器人化仓库设施的工伤率比非机器人化设施高约 54%(存在争议,单一调查性来源,未证实)。
- **责任**问题尚未厘清:工伤赔偿覆盖雇员,但不包括痛苦与折磨赔偿;针对机器人制造商的第三方产品责任诉讼预计将成为主要的压力出口;针对系统集成商/运营商的过失部署理论在人形机器人领域尚未经过检验。遥操作型家用机器人还带来了一层新的操作员责任问题。
- **保险**在中国发展最快:两台 60 公斤级人形机器人的保单以每台约人民币 5000 元(约合 707 美元)保费投保,提供为期一年、最高 50 万元人民币的保障(湖北首份具身智能保单,由一家华中科技大学孵化企业购买,2025-11);中国太平洋保险于 2025-09 推出了中国首款专门的商用人形机器人保险产品,人保财险和平安随后跟进。美国经纪商报告称,在有机器人运行的场所,一般责任险保费上涨了 10%-20%(二手信息来源,未证实)。可以预期,在法规跟上之前,保险公司将实际上扮演"事实监管者"的角色——对经认证与未经认证的部署分别定价。

## 关键议事桌上的人(截至 2026-07)

| 机构 | 关键人物/构成 |
|---|---|
| ISO/TC 299 WG 12(ISO 25785-1) | Kevin Reese(Agility,项目负责人);Federico Vicentini(Boston Dynamics);Carole Franklin(A3)领导美方代表团 |
| A3(ANSI/A3 R15.06、R15.08) | Carole Franklin,机器人标准开发总监 |
| IEEE 人形机器人研究组 | Aaron Prather(ASTM),组长;负责跨标准制定机构的协调工作 |
| MIIT/TC08(中国) | 副主任委员包括王兴兴(宇树科技)、彭志辉(智元机器人);CESI 提供秘书处支持;120 余家起草机构 |
| UL Standards & Engagement | UL 3300 技术委员会(消费/服务机器人,含无障碍相关意见) |

值得注意的一个模式:无论是在美方主导的 ISO 轨道,还是在中国的国家级委员会中,**都是制造商自己在执笔**——Agility、Boston Dynamics、宇树、智元。这样做速度快、信息充分——但批评"自设安全门槛"做法的人士也指出,这构成了一种结构性的利益冲突。参见[组织机构](organizations.md)与[开放问题](open-problems.md)。

## 来源

- https://www.iso.org/standard/91469.html — ISO/CD 25785-1 标题及 CD 阶段(2026-05-12),ISO/TC 299
- https://www.techbriefs.com/component/content/article/53111-safety-in-motion-setting-the-standard-for-humanoid-robots — ISO 25785-1 C 类标准范围,美方代表团负责人(Reese/Vicentini/Franklin)
- https://www.fortrobotics.com/news/shaping-the-robot-safety-standards-of-the-future — TC 299 WG 12 范围,2025-10 巴塞罗那会议
- https://www.automate.org/robotics/blogs/updated-iso-10218-faq — ISO 10218:2025 变化内容,"协作应用"术语,TS 15066 并入情况
- https://www.therobotreport.com/iso-10218-industrial-robot-safety-standard-receives-major-overhaul/ — 10218:2025 改造细节(功能安全、网络安全)
- https://www.businesswire.com/news/home/20250910605228/en/New-ANSIA3-R15.06-2025-American-National-Standard-for-Industrial-Robot-Safety-Now-Available-for-Purchase — ANSI/A3 R15.06-2025 发布,Franklin 相关表态
- https://www.ul.com/news/ul-3300-outline-investigation-helps-advance-safety-consumer-service-and-education-robots — UL 3300 范围(含人形机器人)
- https://www.federalregister.gov/documents/2025/12/31/2025-24076/ul-llc-grant-of-expansion-of-recognition-and-modification-to-the-nrtl-programs-list-of-appropriate — 联邦公报公告,将 UL 3300 加入 NRTL 适用测试标准清单,自 2025-12-31 生效(一手来源)
- https://webstore.ansi.org/standards/ul/ansiul33002024 — ANSI/CAN/UL 3300:2024 标准编号;ANSI 批准版本于 2025-04-16 发布(首版为 2024-05)
- https://www.humanoidsdaily.com/feed/agility-robotics-secures-osha-recognized-safety-approval-widening-the-gap-between-demo-and-deployment — Digit NRTL 现场检验(2025-11-25),R15.08/13849/12100,特定场地
- https://inkog.io/labs/eu-machinery-regulation-ai-agents — 《机械设备条例》2023/1230 适用日期,自我演化型机器学习安全功能
- https://www.gibsondunn.com/eu-ai-act-omnibus-agreement-postponed-high-risk-deadlines-and-other-key-changes/ — 数字综合法案推迟高风险截止日期(2027-12-02 / 2028-08-02)
- https://www.insideglobaltech.com/2026/05/28/eu-ai-act-update-timeline-relief-targeted-simplification-and-new-prohibitions/ — 《机械设备条例》移至附件 I B 部分;授权法案截止 2028-08
- https://www.consilium.europa.eu/en/press/press-releases/2026/06/29/artificial-intelligence-council-gives-final-green-light-to-simplify-and-streamline-rules/ — 欧盟理事会最终批准 AI 综合法案,2026-06-29(一手来源)
- https://www.consilium.europa.eu/en/press/press-releases/2026/05/07/artificial-intelligence-council-and-parliament-agree-to-simplify-and-streamline-rules/ — 临时三方协议,2026-05-07(一手来源)
- https://www.addleshawgoddard.com/en/insights/insights-briefings/2026/technology/ai-omnibus-provisional-agreement-changes-eu-ai-act-delayed-deadlines/ — 综合法案协议时间线(2026 年 5-6 月批准过程)
- https://sesec.eu/2026/04/01/chinas-first-standards-system-for-humanoid-robots-and-embodied-intelligence/ — HEIS 2026 发布(2026-02-28),六大板块,52 项标准,MIIT/TC08,CESI
- https://robottoday.com/article/china-s-humanoid-robot-and-embodied-intelligence-standard-system-heis-2026 — MIIT/TC08 成立(2025-12-26),副主任王兴兴与彭志辉,ISO/IEC 参与情况
- https://www.globaltimes.cn/page/202512/1351625.shtml — 工信部标准化委员会成立(2025-12),65 名成员,全球竞争力框架
- https://www.therobotreport.com/ieee-study-group-publishes-framework-for-humanoid-standards/ — IEEE 人形机器人研究组框架,Aaron Prather,18-36 个月时间线
- https://www.therobotreport.com/1x-announces-pre-order-launch-neo-humanoid-robot/ — NEO 预售,2026 年美国家庭配送,安全内建设计特性
- https://roboticsandautomationnews.com/2025/05/08/ai-robot-attacks-worker-viral-video-shows-unitree-humanoid-going-berserk/90524/ — Unitree H1 工厂事件及原因
- https://interestingengineering.com/ai-robotics/viral-humanoid-robot-kicks-child-in-stomach — Unitree G1 踢中儿童事件(2026-06)
- https://www.chinadaily.com.cn/a/202512/12/WS693b6d05a310d6866eb2e404.html — 中国人形机器人保险保单条款(保费、保障范围)
- https://www.automotivedive.com/news/former-factory-worker-sues-tesla-fanuc-robotic-arm-unconscious-51-million/761146/ — 特斯拉 Fremont FANUC 机械臂诉讼细节(5100 万美元,2023-07-22 事件,拆卸期间配重意外释放)
- https://humanoidliability.com/industries/humanoid-robots/ — 责任框架,保险保费趋势
- https://www.travteks.com/blog/1x-neo-home-delivery/ — 1X Hayward 工厂于 2026-05-01 开业,首批交付内部团队,客户配送目标为 2026 年末
- https://www.agilityrobotics.com/content/beyond-the-hype — Agility 自述的 NRTL 批准情况及合规标准清单
- https://www.newyorker.com/magazine/2026/07/06/are-humanoid-robots-ready-to-be-deployed — Witt:G1 蓝牙僵尸网络漏洞(Makris/Finisterre)、儿童越狱场景、1X 遥操作隐私/披露模式(通过 Wayback 快照阅读)
- https://spectrum.ieee.org/unitree-robot-exploit — UniPwn 技术细节及披露时间线(主要技术报道;完整内容见宇树公司深度报告)
