---
title: "ODM机会图谱:合同制造商在Physical AI中的定位"
slug: odm-opportunity
updated: 2026-07-05
confidence: verified
lang: zh
source: ../wiki/odm-opportunity.md
---
> 电子ODM/EMS到底在Physical AI中处于什么位置?截至2026-07,诚实的答案是:制造业营收池仍然很小(全球2026年预测约5万台人形机器人 ≈ 按混合ASP计约20亿美元硬件规模——不及一个中型手机项目),但**设计中标窗口正在打开且正在收窄**:Apptronik任命Jabil为其全球制造伙伴(2025-02),AgiBot将合资公司加上其2025年全系列的组装工作交给了蓝思科技(Lens Technology),Foxconn(富士康)正在主导Agility 25亿美元SPAC交易中约2亿美元的PIPE投资(2026-06),同时在自家休斯顿AI服务器工厂筹备部署GR00T驱动的人形机器人,Boston Dynamics将电动版Atlas设计为"与汽车供应链兼容",并将执行器采购给现代摩比斯(Hyundai Mobis)——而两个规模最大的量产计划(Tesla、Figure)则坚定地保持自研自产。这一机会分为三块:整机组装(小体量池,高战略价值)、零部件(体量更大的池,面临中国残酷的价格通缩)、以及"卖水人"式的辅助设备(测试台架、换电、遥操作/数据采集硬件——无论最终哪个机器人品牌胜出都能卖出去)。2026-27年的需求信号是真实的,但属于机构性质,而非消费端:国家电网约68亿元人民币的分阶段机器人采购、工信部/国资委的"实景训练"专项行动、以及IPO资本正流入机器人厂商的资产负债表。相关背景参见:[Investment](../wiki/investment.md)、[Humanoid robots](../wiki/humanoid-robots.md)、[Hardware](../wiki/hardware.md)、[Landscape: China](../wiki/landscape-china.md)。

范围说明:本文面向正在构建高管投资决策案例的ODM行业分析师撰写;客户具体的能力画像未知,因此第5节的判断以条件式表述。以下事实在标注处经过了对抗性复核;一条被广泛转述的说法(立讯精密的中国移动订单)未通过核实,已相应标注。

## 1. 市场规模,诚实地划定边界(截至2026-07)

每一份人形机器人推介材料都会混淆两个不同的量:**台数 × 硬件ASP**(制造商可触达的市场)与**被替代的工资**(即黄仁勋所说的40-50万亿美元)。ODM的营收只跟随前者,与后者无关。

### 出货量的现实

| 指标 | 数字 | 追踪机构/来源 | 备注 |
|---|---|---|---|
| 2025年全球人形机器人出货量 | **13,317台** | Omdia(2026-01) | AgiBot以5,168台居首,Unitree(宇树)4,200台,UBTech(优必选)1,000台;Tesla/Figure/Agility各约150台 |
| 2025年全球人形机器人出货量 | **约18,000台**(同比+508%) | IDC(2026-01) | 形态口径更宽;该数字被中国官方媒体引用 |
| 2025年已部署(仅对外销售) | **>16,000台**,中国占比>80% | Morgan Stanley(2026-06) | 不含原型机/试用/内部使用台数 |
| 2026年预测,仅中国 | **50,000台** | Morgan Stanley——2026年上半年从1.4万上调至2.8万再到5万 | 被引用最多的2026年数字;仅限中国 |
| 2026年预测,全球 | **>50,000台**(+约700%) | TrendForce(2025-11-26) | 注意与2025年13-18万的口径基线不一致 |
| 2025年披露的最大纯人形机器人营收 | Unitree(宇树)**16.9亿元人民币(约2.35亿美元)** | IPO招股书 | 人形机器人占其51.5%;是整个赛道营收现实的一个校准点 |

维基惯例(源自[State of the art](../wiki/state-of-the-art.md)):将2025年出货量引用为"约1.3万至1.8万台,取决于统计口径",所有"第一"的说法均视为存在争议。

### 预测阶梯——为不同表述打上话语性质标签

| 数字 | 来源、日期 | 时间范围 | 类别(参见[Visions](../wiki/visions.md)) |
|---|---|---|---|
| 60-100亿美元人形机器人市场 | MarketsandMarkets等 | 2030年 | 分析师预测,保守区间 |
| **380亿美元TAM,约140万台** | Goldman Sachs(高盛,2024-02修订版) | 2035年 | 分析师预测 |
| **5万亿美元"人形机器人生态"** | Morgan Stanley(2025);一个7.5万亿美元的更新版本在流传(未证实) | 2050年 | 分析师预测,生态口径被夸大 |
| 40-50万亿美元劳动力自动化 | Jensen Huang(黄仁勋,GTC Paris 2025-06,二手转述);Figure的"每年42万亿美元" Master Plan | 无明确期限 | **投资者推介话术**——是工资规模,不是硬件规模 |

- 2030年与2050年的数字相差约500倍;每一个万亿级数字都假设[操作/灵巧操控](../wiki/manipulation.md)与可靠性问题已被解决,而这些恰恰是[尚未解决的问题](../wiki/open-problems.md)。
- **ODM算术题(示意性,本维基自行推算)**:2026年约5万台,按约4万美元的混合ASP计算 ≈ **全球硬件总营收约20亿美元**——经交叉验证:Morgan Stanley自己将中国2026年人形机器人市场规模测算为约20亿美元(2026-06,CNBC),IDC则将2025年全球市场营收仅测为约4.4亿美元。按典型EMS经济模型(占产品价值约6-10%)计算,整机组装的增值部分 ≈ **全球1.2亿至2亿美元,由所有合同制造商分摊**。即便按高盛2035年的情形(380亿美元)测算,组装环节的体量池也约为20-40亿美元,零部件环节的体量池约为130-150亿美元(执行器约占BOM的35-40%,参见[Humanoid robots](../wiki/humanoid-robots.md),行业估算)。
- BOM锚点:Morgan Stanley的模型显示,采用中国供应链约为每台4.6万美元,不采用则约为13.1万美元(相当于Optimus Gen 2级别);中国零部件成本每年通缩约15-20%(据报道估算)——无论谁来制造,量产之后利润压力都会到来。参见[Hardware](../wiki/hardware.md)。

## 2. 面向ODM/EMS的价值链开放地图

以下按外包意愿的证据强度排序。宏观信号:Boston Dynamics称电动版Atlas"大幅减少了独特零件的数量",并且**"每个部件的设计都考虑到了与汽车供应链的兼容性"**(官方博客,2024);其Atlas项目负责人将与现代摩比斯的执行器交易描述为可获取"汽车行业成熟的成本结构和规模潜力"——也就是说,至少有一家顶级OEM正在*为外部供应链而设计*。反向信号是:Tesla(弗里蒙特产线,约1万个独特零件)与Figure(BotQ产线,年产能1.2万台)将自研自产奉为教条。

| 子系统 | 约占BOM比例 | 现有厂商(截至2026-07) | 外包意愿的证据 | ODM进入难度 |
|---|---|---|---|---|
| **整机组装与集成** | ——(按费用计) | 大多自研自产:Tesla弗里蒙特产线、Figure BotQ、Unitree(宇树)、AgiBot、Agility RoboFab(年产能1万台,约75%美国零件) | Apptronik→Jabil全球制造伙伴(2025-02);AgiBot→蓝思全系列组装(2025-08);UBTech(优必选)↔富士康云智汇合作(2025-27);中国移动2025年招标标题直接写明为"代工服务"采购 | **中等**——对手机/服务器ODM能力而言毫无难度;门槛在于信任和体量太小,而非工艺本身 |
| **执行器模组与减速器** | 约35-40%(执行器;减速器约15%,滚珠丝杠约18%,流传数字,未证实) | Harmonic Drive Systems、Nabtesco(高端);格陵(Green Harmonic)、FORE(中端);滚珠丝杠:Rollvis、GSA、Ewellix、NSK及中国新进入者贝特(Beite)、五洲新春(Wuzhou New Spring);组装:兆威(Top Group)、三花(Sanhua) | Tesla据称外包了执行器组装/零部件——三花约6.85亿美元订单(单一信源,未证实,对方拒绝置评);BD→现代摩比斯执行器供应(官方) | **高**——精密螺纹磨削机床是护城河;贝特18.5亿元人民币的工厂目标是2026年实现年产260万套滚珠丝杠 |
| **灵巧手** | 约5-10%(估算) | 因时机器人(Inspire,2025年约1万只手)、LinkerBot、Unitree Dex5-1、Shadow、维卡(Wonik);Tesla/Figure自研自产 | AgiBot将其手部单元拆分为独立供应商(2026年);2025年累计出货量超3万只手(推算,单一信源);立讯精密宣称其自研的肌腱驱动手接近行业领先水平(公司口径) | **中等**——微电机加肌腱组装与手机触觉/摄像头技术脉络相通;易损件(凝胶、肌腱、皮肤在2000-4000次循环后磨损)意味着可持续复购的营收。参见[Tactile & hands](../wiki/tactile-hands.md) |
| **线束与高柔性走线** | 低个位数百分比 | 汽车线束巨头是显而易见的相邻赛道(推断);目前未识别出人形机器人专属的领先厂商 | 目前无公开信息(证据缺失,截至2026-07);手部信号线疲劳(ORCA研究中在4500-7000次循环后断裂)暗示存在尚未解决的需求 | **低**——属于商品化能力,体量池小 |
| **传感器与摄像头** | 约20%,含"其他"(未证实的拆分) | 摄像头模组:手机供应链厂商;触觉:GelSight、Meta/维卡Digit 360;力/力矩传感器:ATI、Schunk以及汉威盛(Hypersen)、坤维(Kunwei)、科力(Keli)正在扩产 | Figure 03搭载了掌部摄像头和指尖阵列(自研设计,但属于可外包的零件类别);歌尔股份明确将其扬声器/传感器/光学产品定位面向人形机器人,但同时否认涉足整机组装(2026-06,公司声明) | **低-中等**——与光学/声学ODM能力的直接复用度最高 |
| **电池包与电源** | 约15-20% | 电芯:宁德时代级别厂商;电池包多为自产(Figure 2.3千瓦时定制BMS;UBTech双电池包换电) | UN38.3认证已被作为营销卖点(2025年);UBTech三分钟自主换电已成为一个可对外采购而非自研的产品化子系统 | **中等**——电池包加BMS组装是标准的EMS业务;换电基础设施是一个全新的细分市场 |
| **热管理** | 占比很小 | 自研自产为主;驱动因素是Jetson Thor 40-130瓦的功耗包络加上执行器发热 | 间接信号:服务器ODM的液冷技术(富士康、广达GB300产线)可迁移应用 | **低-中等** |
| **测试/校准台架与产线终检(EOL)设备** | 属于资本开支,非BOM | 尚无成熟供应商——每家OEM各自摸索(1X的手部台架286万次循环测试;Figure的BotQ产线) | Flex↔Teradyne:20年测试设备制造传承延伸至机器人领域(2026-04-22);立讯精密的"制造2.0"全组件到组装自动化产线(2026年初,公司口径) | **中等**——"卖水人"生意:面向所有品牌销售,能在任何行业洗牌中存活 |
| **遥操作与数据采集硬件** | 属于运营支出,非BOM | VR台架组件、动作捕捉服;Neura×Bosch让博世产线工人穿戴传感器服以采集动作/工作流数据(2026-01宣布合作);1X运营付费操作员工位作为数据渠道 | [数据工厂](../wiki/data-foundry.md)的扩建(如AgiBot World式的数据工厂)需要大规模配套的采集设施和台架 | **低**——消费电子的技术脉络可直接迁移;体量虽小但随[Data](../wiki/data.md)中每一个数据论点而增长 |

- **护城河不在哪里**:组装一台价值2-4万美元的机器人,比现代智能手机的要求更低(公差更宽松,扭矩要求更高)。稀缺资产是:(a)精密减速齿轮加工,(b)在设计定型阶段获得OEM的信任,(c)尚无人建立标准的测试/可靠性工程([Open problems](../wiki/open-problems.md)第4节)。
- **毒药在哪里**:任何中国已经掌控的零部件层级——据报道,即使是Optimus约70%的零部件也可追溯至中国供应商(单一中国信源,未证实——参见[Hardware](../wiki/hardware.md));中国掌握约40%的精密轴承、约35%的电机、约90%的稀土磁体加工能力(McKinsey,截至2025年)。在这些领域竞争,意味着要与每年15-20%的价格通缩较量。

## 3. 友商记分牌

按承诺程度排序:**合资/量产线 > 投资(PIPE/股权) > 内部试点 > 仅零部件 > 无动作**。所有条目均标注日期;来源见[来源](#来源)。

| # | 公司 | 层级 | 具体动作(日期) | 注意事项 |
|---|---|---|---|---|
| 1 | **Jabil**(美国) | 生产合作 | 被任命为**Apptronik Apollo全球制造伙伴**(2025-02-25联合公告;项目将持续运行至2026年);新造Apollo在交付客户前先在Jabil自家产线上完成质检、配套包装、临线交付——"Apollo制造Apollo" | 锚点风险=Apptronik的执行能力;商用Apollo交付从2027年起 |
| 2 | **蓝思科技**(中国) | 合资+生产 | 与AgiBot成立合资公司**湖南智启未来科技**,2025-04注册,注册资本1000万元人民币,长沙(持股比例未披露);披露承接**AgiBot全部2025年人形机器人系列产品的制造/组装**(2025-08);对AgiBot旗下清洁机器人子公司知的(Zhiding)进行战略持股 | 1000万元人民币注册资本是期权而非工厂;未披露产能/台数数据 |
| 3 | **立讯精密**(中国) | 自建产线+零部件(超出ODM范畴) | 引导市场预期**2025年出货约3,000台人形机器人,全部面向外部客户**(公司口径,2025-11);"制造2.0"柔性产线于2026年初落地;目标到2026年中期实现约80%核心零部件(减速器、肌腱驱动手)自研自产,并推出通用型机器人原型(公司口径)。**核实提示**:市面流传的"约1.24亿元人民币中国移动订单给立讯精密"(2025-07)一说存在争议——一手招标报道显示,该笔1.2405亿元人民币的中国移动代工采购,实际中标方为**AgiBot(7,800万元)和Unitree/宇树(4,605万元)**;二手报道(乐橡机器人网leaderobot.com,被转载至其他中国行业网站)则将同等金额、同月份的"整机+联合模组"订单归于立讯精密。应视为未证实/可能存在信息混淆 | 3,000台的客户是谁?客户名称未披露;数据均为公司单方面口径 |
| 4 | **富士康/鸿海**(台湾) | 部署+投资(无自有品牌) | (a)正在其**休斯顿GB300 AI服务器产线**部署搭载NVIDIA Isaac GR00T的人形机器人,目标于2026年第一季度启动(在NVIDIA GTC华盛顿特区大会上宣布,2025-10;路透社此前已在2025年报道过该计划);(b)**主导Agility Robotics 25亿美元SPAC交易中约2亿美元以上的PIPE投资**(2026-06-24)——属于财务/战略持股,*不是*制造合资;(c)富士康关联企业云智汇×UBTech(优必选)全球战略合作协议签署(2025-09-21,2025-27:云智汇负责UBTech人形机器人的全球销售/营销/售后服务;部署覆盖富士康生态体系工厂);(d)与Nvidia在高雄联合开发服务型人形机器人(董事长刘扬伟于2025-01首次宣布,2026-01/02再次重申) | 截至2026-07尚无自有品牌通用型人形机器人;该PIPE买到的是信息知情权,而非制造权 |
| 5 | **广达**(台湾) | 通过子公司自研机器人 | 广达集团子公司**达明机器人(Techman Robot)**发布"TM Xplore I"——一款**轮式底座人形机器人**(上半身安装于移动底座之上),号称首款在台湾研发和制造的人形机器人——原型于2025-08展示,正式发布于NVIDIA GTC 2026(2026-03-18),搭载广达云端科技(Quanta Cloud Technology)+Nvidia(搭载Jetson Thor);量产目标为2026年(公司及多家媒体报道);广达还是"人形机器人组装服务器"这一供应链故事中被点名的GB300服务器ODM之一(中文行业媒体,2025-07,未证实) | 协作机器人厂商出身;人形机器人尚处于量产前阶段 |
| 6 | **和硕**(台湾) | 内部事业部/零部件优先 | 机器人事业部按5年计划推进,以零部件为先;在COMPUTEX/投资者活动上展示了"Aria"服务机器人及机器狗(2025-26);董事长童子贤称Nvidia将和硕列为人形机器人供应链受益者之一 | 截至2026-07尚无量产人形机器人,也未有具名的外部OEM客户 |
| 7 | **Flex**(美国) | 相邻领域(协作机器人/AMR),无人形机器人 | 扩大与Teradyne长达20年的合作(2026-04-22):在Flex自有工厂部署Universal Robots协作机器人+MiR自主移动机器人,**并制造UR的关键零部件** | 明确不涉及人形机器人项目 |
| 8 | **英业达**(台湾) | 相邻基础设施 | COMPUTEX 2026:基于NVIDIA IGX Thor的"Atlas Edge"AI服务器、双臂协作机器人iTwin、巡检无人车UGV;Omniverse/Isaac仿真到现实工具链(公司材料) | 未发现人形机器人制造/组装相关动作 |
| 9 | **歌尔股份**(中国) | 仅零部件 | 投资者问答(2026-06):"机器人相关业务有一些布局";扬声器/传感器/光学/精密结构件可用于人形机器人硬件;**明确未披露进入整机组装或具名OEM合作伙伴**(2024年声明:"尚未涉足人形机器人相关业务") | 市场将其视为主题受益标的,而非组装商 |
| 10 | **比亚迪电子**(中国) | 仅受益概念 | 人形机器人项目(含据报道到2026年在比亚迪产线部署2万台机器人的目标,未证实的愿景)属于**比亚迪集团层面,而非上市主体比亚迪电子**;比亚迪电子自身披露仅描述"有一些业务布局"涉及该主题;UBTech(优必选)Walker S1在比亚迪车厂试点属于客户关系,而非比亚迪电子的制造业务 | 截至2026-06未披露对外的人形机器人制造合同 |
| 11 | **纬创资通**(台湾) | 无公开动作 | 截至2026-07未发现任何动作。**实体警示**:有报道将纬创与上纬新材(Swancor,科创板688585)混淆——后者是AgiBot创始人彭志辉2025年取得控制权作为上市壳资源的材料公司(见[Investment](../wiki/investment.md)),已于2025-12-31推出0.8米迷你人形机器人**"启元Q1"(品牌上纬启元)**,并在CES 2026展出。这不是PC/服务器ODM纬创 | 行业渠道中流传的资料库存在这一错标;引用前请先核实实体身份 |

模式解读:**美国EMS通过具名合作(如Jabil)介入,台湾ODM通过子公司/自有机器人+Nvidia生态对齐介入,中国A股"ODM"通过合资加组装的方式服务于国内人形机器人冠军企业**——同一个问题下呈现出三种不同的风险姿态。

## 4. 时机:2026-27年是入场窗口期吗?

### 需求信号(看多论据)

- **订单簿正在夯实(截至2026-07)**:Agility签订的**Digit v5订单合计3亿美元**(SPAC文件);UBTech(优必选)Walker累计订单**超过8亿元人民币**;现代计划从2028年起在美国工厂部署**超过25,000台Atlas**,并新建一座年产能3万台的机器人工厂;Figure BotQ产线爬坡至约每小时1台的速度(累计已造350多台,公司口径)。参见[Humanoid robots](../wiki/humanoid-robots.md)。
- **中国国家层面采购**:国家电网2026年具身智能机器人项目总额**约68亿元人民币(约9.5亿美元)**——500台人形带电作业机器人(25亿元)、3,000台双臂巡检机器人(18亿元)、5,000台四足机器人(15亿元)——分阶段贯穿2026年:第一季度试点、第三季度规模采购、第四季度补充采购(拆分数据来自中国行业媒体36氪的报道,并被多家西方二手媒体转引;南华早报独立佐证了这一数十亿规模的计划;季度分阶段细节仍为单一信源,未证实)。Morgan Stanley将国家电网订单视为其2026-06预测上调的关键驱动因素。中国移动1.24亿元人民币的双足机器人招标(2025-07)是此类采购的范本。
- **中国政策端需求**:工信部与国资委联合推出了**2026年人形机器人与具身智能"实景训练"专项行动**(2026-06-09,工信部一手通知):目标到2026年底前打造100个以上高价值应用场景,并在制造、物流、巡检、医疗、应急等领域形成"万台级"部署能力。这是国家层面的需求承诺机制,而不仅是口号。韩国财阀协同推进的physical AI主线是相应的对照信号([Investment](../wiki/investment.md))。
- **IPO/SPAC资本正流向机器人厂商**:Unitree/宇树约6.18亿美元的科创板IPO(注册于2026-07-02获批)、Agility通过SPAC获得约6.2亿美元毛募资(预计于2026年底前完成交割,由富士康主导PIPE)、AgiBot的上市运作——这些新近获得充裕资金的OEM必须在2026-27年将现金转化为产能,而产能决策正是自研与外包的抉择点。
- **设计中标节奏正在加快**(见第6节清单):截至2026-06的12个月内,出现了六项对ODM/EMS具有实质意义的新承诺(蓝思全系列组装、云智汇×UBTech、富士康休斯顿项目、立讯精密的3,000台指引、Flex×Teradyne、富士康-Agility的PIPE投资),而前一个12个月只有三项(Jabil×Apptronik、蓝思合资、富士康高雄公告)——数量翻了一倍。

### 怀疑论(为什么2026-27年可能为时过早)

- **可靠性问题尚未解决**:西方旗舰试点项目(宝马斯帕坦堡工厂的Figure 02)在运行约11个月、执行单一任务(约1,250个运营小时)后于2025-11结束——机器人退役时明显有磨损痕迹,并未扩展为一个机队规模;宝马此后确认了Figure 03在斯帕坦堡的新用例(2026-06),但将其首个德国试点项目给了Hexagon的AEON,而非Figure;只有约40%的试点项目能在24个月内进入量产阶段(未证实的市场研究);业内的MTBF(平均无故障时间)数据基本处于未公开状态([Open problems](../wiki/open-problems.md)第4节)。为需求未经试点验证的产能进行制造布局,是搁浅资本开支的风险。
- **形态风险**:Rodney Brooks公开预测——在未来约15年内,胜出的机器将采用轮式底座、任务专用夹爪、非人类式传感器;他认为灵巧度"在2036年之后仍远逊于人手"。如果他判断正确,那么人形机器人专属的组装线就是错误的资产配置——不过上文地图中的大部分零部件环节(执行器、传感器、电池、测试)在形态转变后依然存续。应据此对冲配置([Open problems](../wiki/open-problems.md)第7节)。
- **最大的量产计划都不外包**:Tesla(弗里蒙特,年产100万台的愿景)和Figure(BotQ)在理念上都坚持垂直整合;Unitree/宇树能达到约60%的毛利率,*正是因为*其极端的垂直整合。外包意愿集中在资金受限的初创企业身上——而这些恰恰是最有可能在中国国家发改委已警示的行业洗牌中倒下的一批(2025-11警示:超150个近乎雷同的项目)。选择合作对象比总市场规模(TAM)更重要。
- **量级测算**:即便2026年一切顺利(全球约5万台),相对于ODM的规模而言仍是舍入误差——任何专用产线都面临产能利用率风险。马斯克本人的表态:"Optimus的产量初期会非常慢,因为一切都是全新的。这不像造一辆车。"(X平台帖子,2026-07-01)。
- **时间表延迟是行业常态**:自2021年以来,Optimus的每一个重大目标都未能按期实现;Agility的SPAC文件显示巨额亏损;所有2026年量产日期都应视为愿景性质,而非承诺。

### 综合判断

2026-27年不是*量产*窗口期——而是**锚定客户窗口期**。将服务于2028-30年量产爬坡(如果它真的到来)的制造关系,正在以低成本被现在就确定下来(Jabil的协议、蓝思1000万元人民币的合资、富士康的PIPE,相对于ODM的资产负债表而言都很便宜)。理性的姿态是进行体量小、与自身能力相匹配的投入,以换取设计导入地位和信息优势,并将风险敞口控制在即使Brooks式的悲观情形成真也不会造成伤害的程度。

## 5. 面向通用ODM的战略选项(自建/合作/投资/观望)

客户能力画像未知;以下判断均为条件式。

| 选项 | 具名先例 | 资本投入 | 主要风险 | 适用情形 |
|---|---|---|---|---|
| **自建自有品牌机器人** | 立讯精密(2025年引导出货3,000台,公司口径);广达/达明TM Xplore I | 高 | 渠道冲突——你会变成每一个潜在组装客户的竞争对手;而护城河是你所不具备的软件能力([VLA models](../wiki/vla-models.md)) | ……你已经掌握核心零部件和渠道,并接受为他人组装这条路已被封死 |
| **锚定合同制造伙伴关系** | Jabil↔Apptronik(2025-02) | 低-中 | 锚点客户存活风险(初创企业合作方);量产规模可能多年停留在试点阶段 | ……你希望以有限的资本开支实现"边学边造",并能选定一个资金充裕的锚定伙伴(Apptronik级别:已募资超9.35亿美元,有Google/奔驰背书) | 
| **与机器人OEM合资建厂** | 蓝思↔AgiBot(2025-04) | 中等 | 治理/知识产权泄露风险;小规模注册的合资公司只是期权而非承诺——不要过度解读(1000万元人民币) | ……一个具备量产可信度的OEM(AgiBot 2025年出货超5000台)希望共建产能,而你也希望共享上行收益 |
| **战略投资/PIPE** | 富士康→Agility约2亿美元PIPE主导方(2026-06) | 中等(财务性) | 有资本但无制造权——富士康的PIPE明确不是建厂合同;在估值过热的情形下存在按市值计价的风险([Investment](../wiki/investment.md)泡沫观察) | ……你希望在动用产能之前获得董事会级别的信息与可选择权,并能接受风险投资式的估值波动 |
| **零部件切入点** | 歌尔股份(传感器/声学定位);现代摩比斯(Atlas执行器);三花(Optimus执行器零部件,据报道/未证实) | 中等 | 中国每年15-20%的价格通缩;在中国已占据的任何层级中都只有商品化利润 | ……你在精密机械、光学、声学或电池包方面拥有差异化技术,能对应第2节中难度为"低/中"的品类 |
| **"卖水人":测试台架、EOL产线、换电/充电、遥操作与数据采集硬件** | Flex↔Teradyne(2026-04);目前尚无人主导人形机器人EOL测试市场 | 低 | 短期体量池较小 | ……你希望获得能同时经受住行业洗牌*和*形态之争两方面考验的敞口——每一个存活下来的品牌都需要测试与数据基础设施([Data foundry](../wiki/data-foundry.md)) |
| **观望** | 纬创资通、英业达(事实上的选择) | 无 | 错失2028-30年量产窗口的锚定客户名额;类似汽车行业的设计中标粘性意味着晚入场只能捡剩下的份额 | ……你对Brooks/可靠性方面的怀疑持较重权重,或者你的产能已经被AI服务器需求充分变现(截至2026年这是真实存在的机会成本:GB300产线现在就能赚钱) |

- 交叉判断:**组合式打法胜过单一押注**——例如一个锚定合同制造关系+一个零部件切入点+一项"卖水人"业务,总敞口在几十到低几百百万美元区间,即可复制富士康姿态的大部分上行空间,而无需自建品牌项目。
- Nvidia生态实际上是事实上的协调层(GR00T/Isaac/Thor贯穿富士康、广达/达明、和硕、Agility、Boston Dynamics——参见[Company: NVIDIA](../wiki/company-nvidia.md));对于任何已经身处Nvidia服务器供应链中的ODM而言,与该生态对齐几乎是零成本的可选权。

## 6. 什么会让这件事变得紧迫(诚实呈现的FOMO证据)

### 按日期排列的承诺清单

| 日期 | 友商动作 |
|---|---|
| 2025-01 | 富士康董事长宣布与Nvidia在高雄联合开发服务型人形机器人(2026-01/02再次重申) |
| 2025-02-25 | Jabil被任命为Apptronik全球制造伙伴;Apollo部署于Jabil自有运营场地 |
| 2025-04 | 蓝思×AgiBot合资公司(湖南智启未来)在长沙注册 |
| 2025-08 | 蓝思披露承接AgiBot全部2025年系列产品的组装 |
| 2025-09-21 | 富士康关联企业云智汇×UBTech(优必选)签署全球战略合作协议(2025-27) |
| 2025-10 | 富士康在NVIDIA GTC DC大会上宣布将在休斯顿GB300产线部署人形机器人(目标2026年第一季度启动) |
| 2025-11 | 立讯精密引导2025年人形机器人出货量为3,000台(公司口径) |
| 2026-04-22 | Flex×Teradyne合作扩大(协作机器人/AMR+UR零部件制造) |
| 2026-06-09 | 工信部/国资委专项行动启动(100个以上应用场景,2026年底前达成"万台级"能力) |
| 2026-06-24 | Agility宣布SPAC交易,富士康主导约2亿美元以上PIPE |

节奏正在加快,而且每一步动作都会让下一步更容易被证成——这是典型的设计中标竞赛动态。

### 产能与名额正在被锁定(截至2026-07)

- **组装名额**:Jabil拥有Apollo的独家权;蓝思拥有AgiBot的独家权;现代的年产3万台机器人工厂加上摩比斯执行器供应,使Atlas供应链内部化;Figure和Tesla是封闭体系。在具有可信度的美国平台中,尚未被分配的制造名额已经所剩无几。
- **零部件产能**:贝特昆山工厂(年产260万套滚珠丝杠,2026年量产);Xynova手部工厂(年产1万只,2026年第二季度);AgiBot手部业务拆分;LinkerBot目标2026年产能5-10万只手(公司声明,未证实)。滚珠丝杠磨削仍是最常被提及的实物瓶颈([Hardware](../wiki/hardware.md))——稀缺产能正被抢先锁定。
- **设计中标粘性**:人形机器人的BOM仍处于不断变动之中(Figure 03相对02更换了执行器、手部、充电方案;Atlas为适配汽车零部件而重新设计)。在这个阶段就参与共同开发DFM(面向制造的设计)的一方,将把产品塑造成符合自身工艺流程的形态——这正是让早期iPhone和电动车供应商成为长久在位者的同一机制。

### 诚实的反方权重

- 清单中的每一笔交易金额都在**几千万到低几百百万美元**区间——目前尚无一份人形机器人制造合同的价值能接近单个手机项目的规模。FOMO关乎的是*站位*,而非当下的营收。
- 地球上两个规模最大的量产计划(Tesla、Figure)明确不对外开放争取。
- 清单中的多个条目本质上是以承诺面目出现的期权(1000万元人民币的合资公司;一笔PIPE投资;董事长在论坛上的一句表态)。若按"是否真金白银落地"来给友商打分,那么按此标准,只有Jabil、蓝思和立讯精密真正做出了与制造相关的人形机器人实际动作——富士康的休斯顿部署原定于2026年第一季度启动,但截至2026-07其实际状态尚未得到确认。
- 如果2026年的预测像之前历次人形机器人时间表那样出现延迟,"紧迫"会在毫无预警的情况下转化为"过早"。紧迫性的论据建立在成本不对称之上——入场成本相对ODM的资产负债表而言很低,而错失真正量产窗口的代价却不低——而非建立在近期损益表现之上。

## 来源

- https://investors.jabil.com/news/news-details/2025/Apptronik-and-Jabil-Collaborate-to-Scale-Production-of-Apollo-Humanoid-Robots-and-Deploy-in-Manufacturing-Operations/default.aspx — Jabil×Apptronik一手公告(2025-02-25):全球制造伙伴,Apollo部署于Jabil运营场地。
- https://www.therobotreport.com/apptronik-collaborates-with-jabil-to-produce-apollo-humanoid-robots/ — 关于Jabil-Apptronik量产扩张及"Apollo制造Apollo"框架的独立报道。
- https://www.businesswire.com/news/home/20250225753929/en/Apptronik-and-Jabil-Collaborate-to-Scale-Production-of-Apollo-Humanoid-Robots-and-Deploy-in-Manufacturing-Operations — 同一公告的通讯社版本。
- https://stcn.com/article/detail/1636518.html — 蓝思×AgiBot合资公司(湖南智启未来科技)注册信息,注册资本1000万元人民币,长沙,股东名单。
- https://www.thepaper.cn/newsDetail_forward_31296583 — 合资公司业务范围:人形机器人研发+精密制造产线。
- https://www.nbd.com.cn/articles/2025-08-04/4000682.html — 蓝思披露(2025-08):承接AgiBot全部2025年人形机器人系列产品的制造/组装;对知的(Zhiding)的投资。
- https://www.leaderobot.com/news/6770 — 立讯精密:2025年3,000台出货指引,制造2.0产线,自研减速器/肌腱驱动手(公司口径);**也是将1.24亿元人民币中国移动订单归于立讯精密这一说法的唯一信源——存在争议,见下条**。
- https://www.guancha.cn/economy/2025_07_12_782708.shtml — 一手招标报道(2025-07):中国移动1.2405亿元人民币人形双足机器人代工采购,中标方为AgiBot(7,800万元)+Unitree/宇树(4,605万元)——与立讯精密的归属说法相矛盾。
- https://finance.sina.com.cn/tech/roll/2025-11-27/doc-infyvtha0077094.shtml — 立讯精密人形机器人出货指引及三大战略支柱(2025-11,公司表态)。
- https://m.ofweek.com/im/2025-11/ART-201900-8100-30674854.html — 立讯精密到2026年中期约80%核心零部件自研自产的目标;原型发布计划(公司口径)。
- https://www.assemblymag.com/articles/99628-foxconn-to-deploy-humanoid-robots-on-production-line-at-houston-ai-server-plant — 富士康休斯顿GB300工厂人形机器人部署,目标2026年第一季度,Isaac GR00T/Jetson Thor技术栈。
- https://www.therobotreport.com/humanoid-maker-agility-robotics-go-public-through-spac-merger/ — Agility 25亿美元SPAC交易条款;3亿美元Digit v5合同订单;PIPE结构。
- https://www.techtimes.com/articles/319099/20260625/humanoid-robot-ipo-agility-robotics-signs-spac-deal-us-nasdaq-debut.htm — 富士康主导超2亿美元PIPE投资(2026-06-24/25报道)。
- https://www.agilityrobotics.com/content/agility-robotics-to-go-public-through-merger-with-churchill-capital-corp-xi — Agility一手公告:毛募资超6.2亿美元,投资者名单含富士康。
- https://www.geekwire.com/2026/digit-maker-agility-robotics-to-go-public-in-2-5b-deal-heres-what-the-filings-say-about-its-finances/ — Agility SPAC文件中的财务状况(巨额亏损;订单簿背景)。
- https://www.stcn.com/article/detail/3349413.html — UBTech(优必选)×云智汇全球战略合作协议签署于2025-09-21(证券时报):2025-27年业务范围,云智汇负责全球销售/营销/售后。
- https://caifuhao.eastmoney.com/news/20251118194548969453820 — 云智汇×UBTech 2025-2027年产业化人形机器人合作的后续报道(2025-11)。
- https://www.cna.com.tw/news/afe/202501030226.aspx — 中央社(2025-01-03):刘扬伟首次宣布富士康×Nvidia服务型人形机器人高雄计划。
- https://www.21jingji.com/article/20260210/herald/c7e320646a87f919e869c3f343841278.html — 刘扬伟重申(2026-01/02):富士康与Nvidia在高雄联合开发服务型人形机器人。
- https://www.tm-robot.com/en/company/news/Techman-Robot-at-GTC-2026_Unveils-New-AI-Strategy-and-Humanoid-Robot-TM-Xplore-I — 达明机器人一手信息:TM Xplore I在NVIDIA GTC 2026发布(2026-03-18),携手广达云端科技;轮式底座人形机器人,搭载Jetson Thor。
- https://roboticsandautomationnews.com/2025/08/27/techman-robot-unveils-humanoid-prototype-aims-for-2026-launch/93937/ — TM Xplore I原型发布(2025-08-27),目标2026年量产。
- https://money.udn.com/money/story/11162/8952450 — 达明机器人(广达集团)"TM Xplore I"人形机器人,携手Nvidia,产品化目标2026年(台湾媒体)。
- https://www.ctee.com.tw/news/20250726700012-430502 — 据报道GB300 NVL72台湾供应链正引入人形机器人辅助组装(2025-07,中文行业媒体,未证实)。
- https://www.technice.com.tw/issues/ai/158236/ — 和硕机器人事业部,零部件优先的5年计划,童子贤的表述框架。
- https://udn.com/news/story/7240/8470291 — 和硕"Aria"服务机器人展示细节。
- https://news.cnyes.com/news/id/4329179 — 童子贤:Nvidia将台湾供应链厂商(含和硕)列为人形机器人受益者。
- https://ai.inventec.com/%E8%8B%B1%E6%A5%AD%E9%81%94%E6%96%BCcomputex-2026%E5%B1%95%E7%8F%BEai%E8%90%BD%E5%9C%B0%E5%AF%A6%E5%8A%9B/ — 英业达COMPUTEX 2026:Atlas Edge AI服务器(IGX Thor)、iTwin协作机器人、iUGV(公司材料)。
- https://investors.flex.com/news/news-details/2026/Flex-and-Teradyne-Robotics-Expand-Partnership-to-Scale-Intelligent-Automation-Across-Global-Manufacturing/default.aspx — Flex×Teradyne合作扩大(2026-04-22):部署UR/MiR+制造UR关键零部件(一手信息)。
- https://www.therobotreport.com/flex-teradyne-expand-partnership-scale-physical-ai/ — 对Flex-Teradyne physical AI框架的独立确认报道。
- https://finance.sina.com.cn/stock/bxjj/2026-06-23/doc-iniekqut6549406.shtml — 歌尔股份投资者问答(2026-06):机器人相关布局,零部件定位,未披露整机组装。
- https://view.inews.qq.com/a/20260623A06YPI00 — 歌尔股份:同一表态的二手确认。
- https://www.stcn.com/article/detail/1353689.html — 比亚迪电子面向投资者的智能产品/人形机器人表述框架(上市主体范围)。
- https://www.qbitai.com/2024/12/238878.html — 比亚迪集团层面的人形机器人项目及2026年2万台部署目标(据报道,未证实的愿景)。
- https://finance.sina.com.cn/stock/t/2026-06-03/doc-iniactaq0858417.shtml — "短期看手机/汽车,长期看AI"的比亚迪电子市场定位框架(2026-06)。
- https://www.stcn.com/article/detail/3568326.html — 证券时报(2025-12-31):彭志辉以上纬/Swancor董事长身份发布公开信,推出力控迷你人形机器人启元Q1(品牌上纬启元)。
- https://techorange.com/2026/01/02/china-primebot-q1-humanoid-robot/ — 上纬"启元Q1"迷你人形机器人发布报道——即引发纬创名称混淆警示的实体。
- https://bostondynamics.com/blog/boston-dynamics-unveils-new-atlas-robot-to-revolutionize-industry/ — 电动版Atlas:更少的独特零件,"设计上与汽车供应链兼容"(官方)。
- https://www.hyundai.com/worldwide/en/newsroom/detail/hyundai-motor-group-announces-ai-robotics-strategy-to-lead-human-centered-robotics-era-at-ces-2026-0000001100 — 现代CES 2026:摩比斯为Atlas供应执行器,年产3万台机器人工厂,2028年起在Metaplant部署(官方)。
- https://eu.36kr.com/en/p/3780742359243776 — 国家电网约68亿元人民币具身智能机器人采购:500台人形(25亿元)/3,000台双臂(18亿元)/5,000台四足(15亿元);2026年第一季度试点/第三季度规模化/第四季度补充的分阶段安排(拆分数据的原始来源;分阶段信息未证实)。
- https://interestingengineering.com/ai-robotics/china-8500-robots-power-grid — 西方媒体对8,500台/68亿元人民币国家电网拆分数据的二手转引。
- https://www.scmp.com/economy/china-economy/article/3351323/china-plans-invest-billions-robot-army-run-its-power-grid — 南华早报对国家电网数十亿规模机器人计划的佐证报道。
- https://www.miit.gov.cn/zwgk/zcwj/wjfb/tz/art/2026/art_f291ccd3da4c47ce95741de63cc088e6.html — 工信部/国资委联合通知(一手信息):2026年人形机器人与具身智能"实景训练"专项行动。
- https://www.news.cn/tech/20260612/a069b3a9948b4e0aaaa94cf3d618e545/c.html — 新华社(2026-06-12):专项行动启动;100个以上高价值场景,2026年底前实现"万台级"部署能力目标。
- https://technode.com/2026/01/09/chinas-agibot-leads-global-humanoid-robot-shipments-in-2025-omdia-says/ — Omdia 2025年数据:全球出货13,317台,厂商列表。
- https://www.globaltimes.cn/page/202601/1354054.shtml — IDC 2025年数据:约18,000台,同比+508%。
- https://www.scmp.com/tech/article/3358210/morgan-stanley-raises-china-humanoid-robot-shipment-forecast-50000-units — Morgan Stanley将2026年中国预测上调至5万台(2026-06-24)。
- https://www.cnbc.com/2026/06/24/morgan-stanley-china-humanoid-robot-market-forecast.html — Morgan Stanley预测阶梯(2026年内从1.4万→2.8万→5万台),2026年中国人形机器人市场约20亿美元,国家电网订单被引为驱动因素。
- https://www.prnewswire.com/news-releases/ai-to-reshape-the-global-technology-landscape-in-2026-says-trendforce-302626789.html — TrendForce(2025-11-26):2026年全球人形机器人出货量将超过5万台(+约700%)。
- https://m.jiemian.com/article/13925066.html — IDC:2025年约18,000台,全球人形机器人市场营收约4.4亿美元。
- https://www.press.bmwgroup.com/global/article/detail/T0455864EN/bmw-group-to-deploy-humanoid-robots-in-production-in-germany-for-the-first-time?language=en — 宝马一手信息(2026-02-27):Figure 02斯帕坦堡试点完成(约1,250小时,生产3万余辆X3);首个德国试点(莱比锡)给了Hexagon AEON而非Figure;Figure 03用例正在评估中。
- https://www.press.bmwgroup.com/global/article/detail/T0458778EN/bmw-group-advances-the-use-of-physical-ai-in-production-with-figure-03-project-in-spartanburg?language=en — 宝马一手信息(2026-06-25):斯帕坦堡的Figure 03排序物流项目——该合作关系在02退役后仍在延续。
- https://interestingengineering.com/ai-robotics/figure-humanoid-robots-retires-bmw — Figure 02机器人在宝马为期11个月的部署后明显磨损并退役(2025-11)。
- https://neura-robotics.com/neura-robotics-bosch-partnership/ — Neura×Bosch合作(2026-01宣布):博世产线工人穿戴传感器服以生成动作/工作流训练数据。
- https://electrek.co/2026/07/02/musk-shuts-down-optimus-4d-chess-theory/ — 马斯克X平台帖子(2026-07-01):"Optimus的产量初期会非常慢……这不像造一辆车。"
- https://www.goldmansachs.com/insights/articles/the-global-market-for-robots-could-reach-38-billion-by-2035 — 高盛预测:到2035年市场规模380亿美元/140万台。
- https://www.morganstanley.com/insights/articles/humanoid-robot-market-5-trillion-by-2050 — Morgan Stanley到2050年5万亿美元生态预测。
- https://www.scmp.com/tech/article/3337151/china-packs-patent-punch-race-build-humanoid-robots — Morgan Stanley的BOM测算:采用中国供应链4.6万美元 vs 不采用13.1万美元。
- https://eu.36kr.com/en/p/3780414717129481 — Optimus的BOM拆分、中国供应商图谱、据报道三花约6.85亿美元执行器订单(单一信源,未证实)。
- https://www.mckinsey.com/industries/industrials/our-insights/turning-humanoid-supply-chain-constraints-into-billion-dollar-wins — 中国零部件占比(轴承约40%、电机约35%、磁体加工约90%)。
- https://autonews.gasgoo.com/articles/news/from-prototypes-to-production-dexterous-hands-kick-off-a-mass-production-race-2016425582734970881 — 灵巧手产能竞赛:2025年出货超3万只(推算),因时机器人约1万只,Xynova工厂,产能扩建情况。
