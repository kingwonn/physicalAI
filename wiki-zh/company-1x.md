---
title: "公司深度剖析：1X Technologies"
slug: company-1x
updated: 2026-07-05
confidence: verified
lang: zh
source: ../wiki/company-1x.md
---
> 1X Technologies(2014年5月由Bernt Børnich于挪威莫斯创立,原名Halodi Robotics;自约2025年起总部设于加州帕罗奥图)是唯一一家押注**居家优先**的主要人形机器人厂商:其约30公斤、22分贝、腱驱动的NEO于2025-10-28开启消费者预订,定价**2万美元或每月499美元**,五天内预订量突破1万份(公司口径),并承诺2026年底前完成美国境内的居家交付。其技术栈是"安全优先"的硬件(低惯量腱驱动、软质点阵聚合物机身、HIC<250)+ 小型机载VLA(**Redwood**,1.6亿参数)+ **1X World Model**,再由人类远程操作("专家模式")为自主能力兜底——这既是数据飞轮,也是隐私争议的焦点。制造环节高度自建:位于加州海沃德(Hayward)、占地5.8万平方英尺的工厂(2026年4/5月开业)自行生产电机、电池、腱绳和结构件,目标是当下年产1万台、到2027年底年产超10万台(公司目标)。反面因素包括:据报道的约10亿美元融资(估值约100亿美元)截至2026年7月尚未确认完成,已披露的融资总额仅约1.365亿美元(至B轮),流畅的演示为远程操作(Witt,《纽约客》),而与[Figure](company-figure.md)和Agility相比,其工业化落地进展稀薄。背景资料参见:[人形机器人](humanoid-robots.md)、[世界模型](world-models.md)、[待解决的问题](open-problems.md)、[安全与监管](safety-regulation.md)。

## 公司概览(截至2026年7月)

| 项目 | 数值 |
|---|---|
| 成立 | 2014年5月,原名**Halodi Robotics**,挪威莫斯;2023年3月更名为**1X Technologies** |
| 创始人/CEO | **Bernt Øivind Børnich**(11岁时便决心要造人形机器人;毕业于奥斯陆大学机器人学/纳米电子学专业);联合创始人Phuong Nguyen(前CTO)、Jørgen Sundell、Pål Løken |
| 总部/布局 | 加州帕罗奥图(2025-07整合);工厂位于加州海沃德;第二基地加州圣卡洛斯即将于2026年投产;传统工程/制造仍在挪威莫斯 |
| 员工人数 | 663人(2025-09,Contrary Research数据);湾区总部+工厂综合体观察到约800人(Witt记者实地观察,2026-07) |
| 产品 | EVE(轮式人形机器人,2018)→ NEO Beta(2024-08-30)→ NEO Gamma(2025-02-21)→ **NEO消费级发布(2025-10-28)** |
| AI技术栈 | Redwood VLA(1.6亿参数,约5赫兹,机载于Jetson Thor)+ 1X World Model + 离线大语言模型语音;远程操作"专家模式"作为兜底 |
| 定价 | **2万美元**买断("早鸟通道",2026年优先交付)或**每月499美元**订阅(稍后发货);200美元可退定金 |
| 订单量 | 前5天预订超1万份;首年产能"已售罄"(公司口径);截至2026-06约2万份预订将于2026年发货(据Forbes) |
| 工业渠道 | 与EQT的合作(2025-12-11):意向性合作,计划2026–2030年在EQT旗下投资组合公司部署最多1万台NEO |
| 已披露融资 | 约1.365亿美元(至B轮):2023-03由OpenAI Startup Fund领投的2350万美元A2轮;2024-01由EQT Ventures领投的1亿美元B轮 |
| 估值 | 约8.2亿美元(2024-01,据报道);**自2025-09起寻求以约100亿美元以上估值融资最多10亿美元——尚未宣布完成交割(截至2026-07,未证实)** |
| 主要投资方 | OpenAI Startup Fund、EQT Ventures、Tiger Global、三星NEXT、ADT(战略投资,2021)、Sandwater、Alliance Ventures、Skagerak Capital、Nistad |

## 技术路线与架构

**硬件理念:安全是居家场景下的约束性条件,因此设计目标是低机械阻抗,而非工业级负载能力。**

- **腱驱动(Tendon-driven)执行机构**:关节通过腱绳传动而非高减速比直驱齿轮驱动——这是Halodi的原创创新(**Revo1**高转矩密度伺服电机+缆索传动,放弃谐波齿轮;据1X自己的时间线,研发于**2018年**,而安全执行器的研发自2014年创立起便已展开),如今NEO采用的是**Revo2**电机+"低惯量腱驱动"。高转矩密度电机配合低减速比→可反向驱动、反射惯量低、接触时柔顺。
- **规格表体现的结果**(官方数据,截至2026-07):**身高约1.68米(5英尺6),体重30公斤(66磅)**——相比之下Tesla Optimus约57公斤、Figure 03约61公斤——**行走噪音22分贝**("树叶沙沙声"级别;经Witt实地验证),可举起70公斤(154磅),可搬运25公斤(55磅),手臂负载18磅;双手各22自由度,双臂各7自由度;842瓦时电池,续航约4小时,支持5G/WiFi;**3D点阵聚合物软体机身**外覆针织物,无外露夹点,**HIC评分<250**(头部损伤指数,公司自行发布)。
- **机载算力**:"NEO Cortex"采用NVIDIA Jetson Thor,最高2070 FP4 TFLOPS(参见[美国概况](landscape-usa.md));双885万像素90赫兹立体鱼眼摄像头,4麦克风波束成形阵列。
- **Redwood**(发布于2025-06-10):刻意做得**小巧**的VLA——**1.6亿参数,约5赫兹**;融合预训练语言嵌入+ViT视觉token+本体感知(关节位置*及*施加力),通过扩散策略(diffusion policy)解码为NEO/EVE全身动作;基于EVE与NEO机队的远程操作及自主数据训练;完全机载运行。对话交互由离线大语言模型处理。对比:Figure的Helix 02是三层7B/80M/10M的层级结构,最高可达1千赫兹——详见[VLA模型](vla-models.md)。
- **1X World Model(1XWM)**(论文发布于2025-06-16;2026-01-12接入NEO):基于动作条件的视频预测,用于**离线策略评估**,在产品层面则通过视频预测+逆动力学使NEO尝试未经示范的任务;Børnich表示:"这标志着Neo开始具备自我学习、掌握几乎任何你能想到的任务的能力的起点"(发布新闻稿——1X自家发言人随后将此说法软化为"尝试任何任务",据TechCrunch报道)。专门的**1X World Model实验室**随后于2026-06-04成立(由前Luma AI的Sam Sinha领导)。完整内容参见[世界模型](world-models.md)。
- **远程操作是架构层,而非缺陷**:"专家模式"——1X操作员(与AI团队同坐;远程操控时耳机指示灯变色)在自主能力无法完成任务时接管操控NEO;这些会话数据用于模型训练("这对我们来说也是有用的数据"——Børnich,据Witt报道)。这是Waymo式飞轮模式在居家场景的应用——参见[数据](data.md)、[数据铸造厂](data-foundry.md)。
- **与竞争对手的差异**:Figure/Optimus/中国厂商优化的是工业级刚性、负载和节拍时间,再寄望于向居家场景降级;1X则反其道而行——自Halodi时代起,质量、力度、噪音和外壳柔软度就是首要设计变量,能力预期通过机队数据日后逐步获得。代价正是工业买家所看重的:负载、速度、精度。

## 愿景与押注

- **居家优先,创始人原话**:"家庭与消费者市场必须先于其他所有市场实现"(Børnich,据Contrary Research)——与Figure/Agility/Boston Dynamics的顺序恰恰相反。
- **为何选择家庭场景**:(1)**数据飞轮**——家庭场景提供了工业单元永远无法产生的多样化、长尾操作数据,且付费客户为数据采集买单;Børnich强调机队级学习("一台机器人学到的,所有机器人都能学到"的框架)——Witt推断这种网络效应"或可解释"1X急于发货的原因(参见[待解决的问题](open-problems.md));(2)消费市场是30公斤安全机器人具备结构性优势的领域,任何工业厂商靠给60-90公斤机器降级都无法与之匹敌。
- **对不完美的容忍**:Børnich明确在测试消费者是否能接受"**机器人瑕疵(robotics slop)**"——缓慢、偶尔失败、由远程操作兜底的服务——同时静待自主能力逐步改善(Børnich本人在发布会上的原创说法,据Gizmodo 2025-10-29报道;《纽约客》Witt在2026-07-06刊也有报道)。
- **将远程操作定位为特性而非缺陷**:Børnich为"专家模式"辩护称这是"比让人类清洁工进入你家更安全、更好的服务"(在NYT的*Hard Fork*播客上,2025-11,据Humanoids Daily报道)——提示灯、面部模糊处理、App设置的禁入房间、仅在业主许可下操作员才能访问(公司自述的缓解措施)。
- **承诺**:2026年美国境内居家交付——"这是我们对世界的承诺,也是我们必须兑现的承诺"(产品负责人Dar Sleeper,对Witt公开表态,2026-07)。
- **对AI能力的坦诚**:Børnich曾承认"我们目前所有的AI在大多数推理任务上都彻底失败"——其愿景明确依赖硬件安全+远程操作来弥合自主能力的差距,而非寄望于近期实现AGI。前AI副总裁Eric Jang的表述是:"条条大路通机器人"(参见[关键人物](key-people.md))。

## 产品与部署——真实数据

| 平台 | 首发 | 形态/成本 | 部署记录 |
|---|---|---|---|
| **EVE** | 原型机2017-07;发布于2018 | 轮式人形机器人,生产成本约10万美元,租赁约5万美元/年(Contrary数据) | **与ADT Commercial签订140台协议(2022-03,约7000万挪威克朗≈700万美元/年)**用于安保巡逻;试点项目:Sunnaas医院(挪威)、Altopack(意大利,包装业)、Strongpoint(零售物流)、I-Mens(比利时,老年护理);曾有"EVE Industrial"变体;NEO转型后该平台已被淡化 |
| **NEO Beta** | 2024-08-30 | 双足、软体机身 | 居家测试(有限规模,高度依赖远程操作) |
| **NEO Gamma** | 2025-02-21 | 改进迭代版 | 居家alpha测试;NVIDIA GTC 2025演示(远程操作) |
| **NEO(消费版)** | 预订始于2025-10-28 | 2万美元/每月499美元,3种配色 | **前5天预订超1万份;首年产能(超1万台)已售罄**(公司口径);截至2026-06约2万份预订(据Forbes);**截至2026-07尚无确认的第三方客户居家交付案例**——海沃德工厂首批量产单元用于内部测试/验证及研发(2026-05) |

- **EQT工业合作(2025-12-11)**:与EQT(其B轮领投方的母公司,旗下投资组合公司超300家)达成战略合作——"意向性"计划在2026–2030年间于制造、仓储、物流、设施运营、医疗领域**部署最多1万台NEO**;2026年美国试点,随后拓展至欧洲/亚洲。注意:此为意向性合作而非已确认订单;这也是对居家优先战略的一种隐性对冲(TechCrunch的解读框架是:把"居家"人形机器人送去工厂)。
- **自主能力现实检验(截至2026-07)**:Witt实地探访发现,流畅的NEO厨房演示实为**VR远程操控**("像提线木偶");1X**拒绝演示自主能力**;在2025-10-28的发布会上,发布窗口期媒体演示中的复杂任务全部为远程操作——"其动作100%由人远程操控"(MKBHD在WSJ的实测报道中如是说;Tom's Guide等媒体也指出了对专家模式的依赖)。1XWM驱动的自主任务仍停留在简单层面(空气炸锅取篮、面包放入烤面包机、击掌——TechCrunch及媒体共识,2026-01;1X自身已将Børnich"任意提示"的说法软化为"尝试任何任务",能力"仅限于基础任务")。参见[评估](evaluation.md)。
- 手部耐久性测试台观测到286万次手指弯曲循环;通过公主抱式测试确认NEO重量约66磅(Witt,2026-07)。

## 商业模式与单位经济学

- **消费者双轨制**:2万美元买断("早鸟通道",2026年优先交付,含充电器/去毛刷/手提箱)或**每月499美元**订阅(稍后发货);200美元可退定金。1万份×200美元≈仅约200万美元的定金流动资金——订单量本质上是一份期权账本,而非营收(定金可退;2万美元买断与每月499美元订阅客户的比例未披露)。
- **营收潜力**:若首年1万台全部为2万美元买断,营收上限约2亿美元(实际比例未知)。按每月499美元计算,与2万美元价格持平需约40个月——订阅模式对消费者而言是应对可靠性/过时风险的对冲,对1X而言则是经常性收入故事。
- **隐藏成本:远程操作人力。**每小时"专家模式"运行都意味着人力投入+数据采集成本;1X未披露每台机器人的远程操作工时或人员配比(这是行业普遍的信息缺口——参见[评估](evaluation.md))。Jim Fan曾说:"照看这些机器人需要一整个运营团队。"
- **物料成本(BOM)**:据称NEO的制造成本"与中端自动驾驶汽车的成本相当"(Contrary数据,表述模糊);未公布具体物料清单。对比商用级人形机器人物料成本:中国供应链约4.6万美元 vs 西方供应链约13万美元(参见[人形机器人](humanoid-robots.md))——2万美元的零售价意味着要么早期利润微薄甚至为负,要么通过自建电机等方式实现了激进的成本工程(未证实)。
- **Halodi时代的RaaS先例**:EVE以约5万美元/年的价格租赁,对应约10万美元的生产成本——约2年回本;该业务(约700万美元/年的ADT合同规模)是公司迄今唯一有实质意义的营收历史(截至最近一次披露;当前营收未披露)。
- **融资缺口是怀疑者的立论支点**:截至2024年已披露融资约1.365亿美元,相较Figure的约19亿美元差距悬殊;要在此基础上扩产至年产10万台,需要依赖那笔据报道的**估值约100亿美元、融资约10亿美元**的轮次——**截至2026-07仍未确认完成交割**;相较2024-01披露的8.2亿美元估值,约20个月内溢价超过12倍——参见[投资](investment.md)关于估值上涨速度的讨论。

## 优势/劣势对比同业

| | 评估 |
|---|---|
| **优势** | 唯一具备可信度的**居家品类领跑者**(Figure的居家布局滞后;Optimus尚未发货);真正差异化的**安全硬件**(30公斤/22分贝/HIC<250是竞争对手无法事后追加的);西方市场最低价位(2万美元/每月499美元);深度垂直整合,含自建电机;OpenAI/EQT/三星在列的股东名单;十年级别的执行器技术积累(安全执行器研发自2014年创立起持续至今;Revo1于2018年推出);EQT渠道降低了消费级押注的风险;若交付顺利落地,将形成居家数据飞轮 |
| **劣势** | **对远程操作的依赖**——招牌能力实为人力驱动;自主能力演示被拒绝展示(Witt);2026年底交付承诺存在**交付风险**(截至2026-07尚无确认的客户交付);相较Agility(客户现场工时超6.5万小时)和Figure(已获宝马确认合作),**工业化落地进展稀薄**;已披露资本约1.365亿美元,远低于10亿美元级别的同业,且新一轮融资尚未完成;续航仅4小时/842瓦时;搬运上限25公斤;隐私争议可能限制主流市场采纳;AI领导层动荡(Eric Jang于2026-01离职,由Mohi Khansari接任) |
| **机会** | 先发消费品牌+装机量网络效应;EQT旗下超300家投资组合公司;关税政治背景下的"美国制造"定位;订阅模式的客户终身价值(LTV) |
| **威胁** | 特斯拉/Figure携10-100倍资本进军家庭场景;中国低于1万美元的平台([Unitree](company-unitree.md));一起严重的居家伤害事件或隐私丑闻(Aaron Ames:"我不知道1X到底要怎么才能蒙混过关"——居家跌倒事故的法律风险敞口);UL 3300类认证缺口——1X**尚未为NEO发布任何第三方安全认证**(截至2026-07,未证实的缺失——参见[安全与监管](safety-regulation.md)) |

- **怀疑论的浓缩版**:1X实质上是在出售一台2万美元的远程操作终端,外加一份自主能力路线图;订单量由可退定金构成;估值诉求(约100亿美元)已提前计入飞轮效应生效的预期,而此时尚无任何客户交付案例。**持平而论**:硬件安全护城河是真实的,并已获独立实地报道验证;五天内的定金量证明了任何竞品都尚未展示过的真实消费需求;而"远程操作换数据"正是Waymo当年的自举打法——即便营销说法有所夸大,该战略本身仍是自洽的。

## 制造与供应链姿态

**姿态:最大化的垂直自建整合;截至2026-07,未披露任何ODM/EMS代工制造关系。**

- **加州海沃德工厂**:占地5.8万平方英尺,2026-01获得最终许可,2026-04-30/05-01开业("美国首个垂直整合的人形机器人工厂"——公司自我定位),员工超200人,初始产能**约年产1万台NEO**。
- **自建生产**:电机、电池包、结构件、腱传动装置、软体材料(点阵聚合物+织物)及传感器,并设有电机、手部组件、电池包及**腱绳生产**(专有精密编织及后处理工艺)的专用产线。
- **Revo2电机产线**:全自动化——自行绕制铜线圈,在1X自主设计的机器上用电工钢制造定子;自海沃德工厂投产以来**已生产1.7万台电机**(据2026-04-30工厂开业时公司披露);电机技术谱系可追溯至Halodi时代在莫斯的研发(Revo1于2018年研发完成)。自建电机被称为NEO实现低重量高转矩密度、以及达成2万美元零售价的关键推手。
- **外包组件**:对于非自建部件,1X表示会"直接进驻供应商工厂内部"以贯彻自身质量标准;供应商身份及部件来源(芯片除外:采用NVIDIA Jetson Thor)均未披露——在执行器级钢材、磁体或电池芯采购方面没有任何可见度(截至2026-07)。
- **扩产计划**:海沃德工厂自动化升级+2026年晚些时候投产的**第二基地(加州圣卡洛斯)**→到2027年底实现**年产10万台以上**(公司目标);官方表态计划在产线上采用工业自动化与NEO机器人本身相结合的混合模式。历史路线图(Contrary数据):数千台(2025)→数万台(2026)→数十万台(2027)→数百万台(2028)——此前每一家人形机器人厂商都未能兑现过类似的增长曲线。
- **布局历史**:挪威莫斯(执行器+EVE/NEO组装,与工程部门同址)→2021年扩展至蒙特利尔与奥克兰→2025-07总部整合至帕罗奥图→生产重心现已转移至加利福尼亚州;莫斯保留用于工程研发(在量产中的角色尚不明确,未证实)。
- **对ODM/EMS行业的启示**:1X在组装与执行器层面是一家**封闭工坊**——与系统级ODM机会恰恰相反;真正的开放空间在于**零部件层级**(电芯、磁体、精密钢材、半导体、聚合物点阵材料),且需在1X嵌入式质量管控体系下运作。其美国本土组装的姿态既是关税对冲,也是营销资产,同时也让1X成为检验西方自建制造能力能否在10万台/年规模下逼近中国物料成本经济性(商用级约4.6万美元——参见[中国概况](landscape-china.md))的最清晰试金石。对比[Figure的BotQ](company-figure.md)(同样信奉垂直整合、工业优先)与Agility(更依赖合作伙伴)。

## 来源

- https://en.wikipedia.org/wiki/1X_Technologies — Halodi创立背景(2014-05,莫斯)、创始人、EVE 2018、2023年更名、总部帕罗奥图
- https://research.contrary.com/company/1x — Contrary Research业务分析:创始人背景故事、Revo1传动机构、ADT单位经济学(约10万美元成本/约5万美元年租/约700万美元年营收)、A2轮后2.1亿美元估值、663人员工规模(2025-09)、生产路线图、Børnich关于居家优先与AI局限性的言论
- https://ipvm.com/reports/halodi-robotics — ADT Commercial 140台EVE协议分析(2022)
- https://www.securitysystemsnews.com/article/adt-commercial-introduces-humanoid-robotics-to-security-industry — ADT方对EVE部署的确认
- https://www.1x.tech/discover/1x-rasies-23-5m-in-series-a2-funding-led-by-open-ai — A2轮2350万美元融资,OpenAI Startup Fund领投,Tiger Global参投(官方,2023-03)
- https://www.1x.tech/discover/1x-secures-100m-in-series-b-funding — B轮1亿美元融资,EQT Ventures领投,三星NEXT参投(官方,2024-01)
- https://www.theinformation.com/articles/humanoid-robot-developer-1x-targets-1-billion-new-funding — 据报道寻求以100亿美元以上估值融资约10亿美元(2025-09;交割未确认)
- https://www.humanoidsdaily.com/news/report-humanoid-robotics-firm-1x-seeking-up-to-dollar1b-at-a-valuation-of-dollar10b-or-more — 此前8.2亿美元估值(2024-01,据报道);12倍溢价背景
- https://www.1x.tech/neo — 官方NEO规格表:身高5英尺6/体重66磅、22分贝、举重154磅/搬运55磅、842瓦时/4小时续航、HIC<250、点阵聚合物机身、Jetson Thor Cortex、专家模式
- https://www.therobotreport.com/1x-announces-pre-order-launch-neo-humanoid-robot/ — 预订发布条款(2025-10-28)、200美元定金、2026年美国/2027年国际交付
- https://www.forbes.com/sites/johnkoetsier/2026/04/30/1x-kicks-off-full-scale-production-of-humanoid-robot-neo/ — 5天内超1万份定金(公司口径)、全面量产启动、Redwood运行于Jetson Thor
- https://www.globenewswire.com/news-release/2026/04/30/3285118/0/en/1x-opens-neo-factory-in-hayward-ca-america-s-first-vertically-integrated-humanoid-robot-factory-with-consumer-shipments-planned-for-2026.html — 海沃德工厂开业新闻稿:5.8万平方英尺、员工200+、年产1万台、2027年底目标超10万台
- https://www.1x.tech/discover/neo-factory — 垂直整合细节:自建电机/电池/结构件/腱绳/软体材料/传感器、自动化Revo2产线、1.7万台电机、供应商嵌入式质量管控、圣卡洛斯基地
- https://thenextweb.com/news/1x-neo-humanoid-factory-hayward-10000-home-robots — 首批量产单元用于内部研发;圣卡洛斯基地;2027年前实现年产10万台的自动化计划
- https://www.travteks.com/blog/1x-neo-home-delivery/ — 首批量产单元用于内部测试人员,客户交付目标为2026年末
- https://www.therobotreport.com/1xs-neo-humanoid-gains-autonomy-with-new-redwood-ai-model/ — Redwood发布公告(2025-06-10)、Eric Jang言论、机载GPU部署
- https://www.1x.tech/discover/redwood-ai — Redwood架构:1.6亿参数、约5赫兹、视觉+语言+本体感知→扩散策略(官方)
- https://www.1x.tech/discover/world-model-self-learning — 1X World Model接入NEO(2026-01-12):视频预测+逆动力学
- https://www.globenewswire.com/news-release/2026/01/12/3217155/0/en/1x-unveils-paradigm-shift-in-humanoid-ai-neo-s-starting-to-learn-on-its-own.html — 1XWM产品新闻稿:Børnich"Neo开始自我学习的起点"言论(2026-01-12)
- https://techcrunch.com/2026/01/13/neo-humanoid-maker-1x-releases-world-model-to-help-bots-learn-what-they-see/ — 1XWM发布报道:空气炸锅/烤面包机/击掌任务示例;1X发言人软化"任意提示"的说法
- https://www.forbes.com/sites/johnkoetsier/2026/06/04/1x-launches-humanoid-robot-world-model-lab-you-cant-fine-tune-your-way-to-agi/ — 1X World Model实验室成立(2026-06-04,Sam Sinha);约2万份预订将于2026年发货
- https://www.1x.tech/about — 官方公司时间线:2014年创立、2018年研发出Revo1、2022年EVE工业部署、2023年转向NEO
- https://www.businesswire.com/news/home/20251211360340/en/1X-Announces-Strategic-Partnership-to-Make-up-to-10000-Humanoid-Robots-Available-to-EQTs-Global-Portfolio — EQT合作新闻稿:最多1万台人形机器人、2026–2030年、投资组合应用场景(官方,2025-12-11)
- https://techcrunch.com/2025/12/11/1x-struck-a-deal-to-send-its-home-humanoids-to-factories-and-warehouses/ — 将EQT合作解读为工业化转型/对冲策略;2026年美国试点
- https://www.newyorker.com/magazine/2026/07/06/are-humanoid-robots-ready-to-be-deployed — Stephen Witt:VR远程操控的厨房演示、拒绝演示自主能力、观察到约800名员工、实地验证66磅/22分贝、286万次手指循环测试台、Sleeper的"承诺"言论、Børnich的"有用数据"言论、Ames的法律风险言论(通过Wayback快照读取;原文付费墙——现场探访内容的唯一来源)
- https://www.humanoidsdaily.com/feed/1x-ceo-details-neo-s-two-modes-and-defends-teleoperation-as-more-secure-than-a-cleaner — Børnich为远程操作辩护("更安全、更好的服务")及双模式说明,发表于NYT的Hard Fork播客(2025-11)
- https://gizmodo.com/neo-wants-to-usher-in-the-era-of-robotics-slop-2000678755 — Børnich在发布会上提出的"机器人瑕疵"说法(2025-10-29);WSJ实测发现演示完全由远程操控完成
- https://www.tomsguide.com/home/smart-home/the-neo-home-robot-thats-breaking-the-internet-promises-to-change-the-world-but-theres-one-huge-problem — 发布视频因依赖专家模式引发争议;隐私缓解措施(模糊处理、禁入区域)
- https://www.humanoidsdaily.com/news/1x-neo-launch-sparks-debate-on-autonomy-and-teleoperation — 发布窗口期的争论;MKBHD:"其动作100%由人远程操控"(WSJ演示)
- https://www.therobotreport.com/teleop-not-autonomy-the-path-for-1x-neo-humanoid/ — 分析文章:远程操作优先的路径,自主能力路线图的注意事项
- https://www.humanoidsdaily.com/news/eric-jang-steps-down-as-vp-of-ai-at-1x-technologies — Jang离职(2026-01),Khansari接任
- https://evjang.com/2026/01/21/leaving-1x.html — Jang本人的离职文章(一手来源)
