---
title: "公司深度剖析:Agility Robotics"
slug: company-agility
updated: 2026-07-05
confidence: verified
lang: zh
source: ../wiki/company-agility.md
---
> Agility Robotics(成立于2015年,总部位于俄勒冈州塞勒姆;由Jonathan Hurst在俄勒冈州立大学的Dynamic Robotics Lab通过ATRIAS→Cassie这条谱系分拆而来)是人形机器人领域的"反炒作"代表:双足运动科学优先、"枯燥"的仓库工作优先、安全认证优先——如今即将成为**唯一一家美股上市的纯人形机器人公司**(官方口径;媒体将其宣传为首家上市的美国人形机器人制造商——中国同行如UBTech此前已在香港上市),通过**与Churchill Capital Corp XI于2026-06-24宣布的25亿美元pre-money SPAC合并**(预计毛募集资金超过6.2亿美元:4.2亿美元信托账户+由富士康(Foxconn)牵头的约2亿美元PIPE私募;股票代码**AGLT**;预计2026年完成)。其护城河在于同行无人能及的部署记录:Digit已在**9个客户设施中累计运行超过65,000小时**(GXO——业内首个人形机器人RaaS合同,2024-06;Schaeffler;丰田汽车加拿大制造公司(Toyota Motor Manufacturing Canada);Mercado Libre)、在GXO单一站点**搬运超过100,000个料箱(tote)**、**首个获OSHA认可的NRTL现场认证**人形机器人(2025-11,公司自称首创)、以及**超过3亿美元的Digit v5多年期合同订单**(以里程碑为条件)。质疑者的论点是:2025年运营支出约1.11亿美元,而营收未披露且规模较小;刻意收窄的料箱搬运与配套(kitting)使用场景;相较于灵巧型对手,该平台自由度(DoF)受限;以及在该行业历史表现不佳的SPAC结构。背景延伸阅读:[人形机器人](humanoid-robots.md)、[格局:美国](landscape-usa.md)、[投资](investment.md)、[安全与监管](safety-regulation.md)。

## 公司概览(截至2026-07)

| 字段 | 详情 |
|---|---|
| 成立时间 | 2015年,分拆自俄勒冈州立大学Dynamic Robotics Lab |
| 创始人 | **Jonathan Hurst**(首席机器人官)、**Damion Shelton**(CEO,任至2024-03)、**Mikhail Jones** |
| CEO | **Peggy Johnson**(自2024-03起;曾任Magic Leap CEO,在纳德拉(Nadella)麾下担任微软EVP BD 6年,曾在高通任职24年) |
| CTO | Pras Velagapudi(Melonee Wise曾于2023年任CTO→2024-05任CPO,2025-08离职加入KUKA) |
| 总部/布局 | 俄勒冈州塞勒姆(RoboFab工厂+总部);另有匹兹堡、湾区办公室 |
| 产品 | **Digit**双足机器人(v4已在现场部署;**v5**于2026-06-24发布,预计2027年初更广泛供货) |
| 商业模式 | RaaS(机器人+Agility Arc云平台+服务订阅);部分直接销售 |
| 部署记录 | 65,000+小时,9个客户设施,GXO Flowery Branch站点超过10万个料箱(2025-11) |
| 客户 | GXO Logistics、Schaeffler、丰田汽车加拿大制造公司、Mercado Libre;亚马逊(Amazon)试点;超过30个客户的储备管道(公司口径) |
| 订单储备 | 超过3亿美元的Digit v5多年期订单,以里程碑为条件(公司口径,2026-06) |
| 私募融资 | 约1.5亿美元B轮(2022年,DCVC/Playground、亚马逊工业创新基金);约4亿美元C轮,估值约21亿美元(2025年,WP Global Partners;SoftBank、亚马逊、Schaeffler参投)——参见[投资](investment.md) |
| 上市方式 | 与Churchill Capital Corp XI(Michael Klein)进行SPAC合并:25亿美元pre-money估值,4.2亿美元信托账户+约2亿美元由富士康牵头的PIPE(每股10美元),毛募集资金超过6.2亿美元,股票代码AGLT,180天锁定期,预计2026年完成;上市交易所为"北美主要交易所之一",尚未具名(Churchill XI目前以CCXI代码在纳斯达克交易) |
| 财务状况 | 2025财年运营支出约1.11亿美元(2024年约7100万美元),现金消耗约1亿美元(初步/未经审计数据,据GeekWire援引的申报文件);营收未披露,待S-4文件公布 |
| 制造 | RoboFab,俄勒冈州塞勒姆:占地7万平方英尺,首个专为人形机器人建造的工厂(2023年);设计产能约每年1万台;约75%零部件在美国采购(公司口径) |

## 技术路线与架构

**运动科学起步 → 定制化物流机器 → 学习型全身控制 → 安全认证驱动的自主性。** Agility的技术栈与Figure/特斯拉(Tesla)"通用VLA(视觉-语言-动作模型)+ 五指灵巧手"路线截然相反:

- **弹簧-质量(spring-mass)谱系,而非人形模仿。** Hurst的学术项目(卡内基梅隆大学(CMU)博士→俄勒冈州立大学)打造了ATRIAS(DARPA资助,首个机械化实现奔跑弹簧-质量模型的机器)以及**Cassie**(2017年)——这款"鸟腿"双足机器人后来因创下双足机器人100米吉尼斯世界纪录而闻名。Digit"反向"的膝关节、叶片弹簧腿和低惯量肢体源自动物运动物理学,而非对人体解剖结构的复制。参见[运动控制](locomotion.md)。
- **学习型全身控制基础模型**(据NVIDIA案例研究称为"软件运动皮层"):在Isaac Sim(基于OpenUSD)中构建数字孪生,在Isaac Lab中进行数百万次并行强化学习(RL)训练,并在容器化的MuJoCo环境中进行交叉验证后再部署到硬件上。CTO Pras Velagapudi表示:**"运行在NVIDIA GPU上的Isaac Sim让我们能够在几小时内为Digit模拟出数年的真实世界学习经验。"**("Isaac Sim running on NVIDIA GPUs lets us simulate years of real-world learning for Digit in just hours.")参见[仿真](simulation.md)。
- **任务自主性优先于开放式通用性。** Digit运行结构化的仓库工作流(料箱搬运、机床上下料、排序),由Agility的云端车队管理平台**Agility Arc**进行编排(任务分配、仓库管理系统(WMS)集成、监控)。公司并未公开押注自研通用VLA;Agility是Google DeepMind Gemini Robotics的可信测试方,也是NVIDIA的深度合作伙伴,而非前沿模型实验室(参见[格局:美国](landscape-usa.md)、[公司:NVIDIA](company-nvidia.md))。
- **刻意限制自由度的操作能力。** Digit v4采用简单的夹爪式末端执行器(手臂约4自由度;不同聚合信息源对具体数字说法不一——DoF数字应视为未证实);v5新增**可更换的手部/末端执行器**,而非五指灵巧手。其理念是:料箱与箱体物流并不需要20自由度的手,自由度更少意味着更便宜、更可靠、更易于认证。代价是相较于[Figure](company-figure.md) 03的触觉手或[Boston Dynamics](company-bostondynamics.md)的Atlas,其任务覆盖面存在上限。参见[触觉与灵巧手](tactile-hands.md)。
- **安全作为差异化层。** Digit v5被定位为首个**"协作安全"("cooperatively safe")**的AI赋能人形机器人——能够与人类共享无护栏空间——其基础是一个可独立于AI主控系统紧急停止机器人的专用安全处理器、**NVIDIA IGX Thor**计算平台、**Halos OS**,以及用于转角感知的外部设施摄像头。Agility是首个Halos合作伙伴——NVIDIA表示:**"Agility是首家与NVIDIA合作,将Halos for Robotics相关要素纳入自有专有安全系统的公司。"**("Agility is the first company to team with NVIDIA to incorporate elements of Halos for Robotics into its proprietary safety system.")(Halos for Robotics于2026-06-22在Automate展会发布);NVIDIA经ANAB认可的**Halos AI系统检测实验室**依据IEC 61508、ISO 13849和ISO/IEC TR 5469对系统进行评估,为第三方认证做准备(Digit是否正式经过该实验室评估尚未披露——未证实)。Agility的Kevin Reese(杰出机器人安全工程师)是ISO/TC 299 WG 12中ISO 25785-1标准的项目负责人,这是首个专门针对动态稳定移动机器人(含人形机器人)的安全标准——该公司实际上正在亲自参与撰写它计划率先通过的规则。参见[安全与监管](safety-regulation.md)。

## 愿景与押注

- Hurst的创始理念是增强稀缺劳动力以应对枯燥工作,而非为通用性本身而追求机器人通用性:机器人应当承担**"枯燥、肮脏、危险"("dull, dirty, dangerous")**的重复性任务(他反复使用的表述),而人类则保留创造性、多样化和社交性的工作;其既定使命是**"让人类更像人类"("to enable humans to be more human")**。他将Digit定位为一种轻量级自动化方案,能够进入现有设施直接开始工作而无需改造(据播客/访谈陈述,经转述)。
- 关于SPAC:Hurst表示——**"我们相信协作安全是规模化人形机器人应用的关键突破口,我们下一代Digit代表着迈向机器人成为工作场所可信赖伙伴这一未来的重要里程碑。"**("We believe cooperative safety is the critical unlock for scaled humanoid adoption, and our next generation Digit represents an important milestone toward a future where robots become trusted partners in the workplace.")(官方新闻稿)v5的宣传重点在于:相较于增加手指灵巧性,消除护栏/隔离区对客户而言价值更高。
- Peggy Johnson自2024-03起的定位明确反"登月计划":**"专注当下"("focused on the here and now")**(TechCrunch,2024-03)——先推出能创造营收的仓库机器人,再逐步扩展应用范围;即"先学走路,再学后空翻"。在SPAC宣布时她表示:**"人形机器人是美国技术领导力和全球产业未来的关键驱动力。"**("Humanoid robots are a critical driver of American technology leadership and the future of global industry.")并将美国制造/配送/物流市场机会规模估算为"约1万亿美元"——明确注明为"管理层估算"(官方新闻稿)。
- 战略对比:Figure和特斯拉出售的是通用未来愿景(家用机器人、2万美元价位),而Agility出售的是**已有付费客户记录的近期劳动力产品**——并利用公开市场而非私募巨额融资来为规模化扩张提供资金。其赌注是:枯燥、经认证、具备单位经济效益的部署,其复利增长速度快于能力演示。

## 产品与部署

### 平台代际演进

| 代际 | 时间 | 关键信息 |
|---|---|---|
| ATRIAS | 2010年代(俄勒冈州立大学/DARPA) | 学术性弹簧-质量双足机器人;前身 |
| Cassie | 2017年 | 仅腿部的双足机器人,销售给研究实验室(密歇根大学、伯克利等);创吉尼斯100米纪录(2022年,俄勒冈州立大学) |
| Digit v1–v3 | 2019–2022年 | 在Cassie腿部基础上加装躯干与手臂;与福特(Ford)开展最后一公里配送合作(2019–20年,首个客户)——后转向仓库物流时放弃 |
| Digit v4 | 2023年 | 身高约175厘米,体重约65公斤,负载约16公斤(35磅),夹爪式手部,续航约8小时并支持自主对接充电(聚合信息源数据,未证实);目前在现场部署的机型 |
| **Digit v5** | 2026-06-24发布 | **50磅(约22.7公斤)负载(较v4提升40%),每日可运行长达22小时,约7.2英尺(2.1米)臂展,可更换手部,NVIDIA IGX Thor + Halos安全技术栈,"协作安全"设计**;预计2027年初更广泛供货(公司口径) |

### 部署记录(截至2026-06,业内记录最完整)

- **GXO Logistics**——业内首个多年期人形机器人**RaaS协议(2024-06)**;Digit在乔治亚州Flowery Branch的Spanx工厂搬运料箱;截至2025-11已**搬运超过10万个料箱**;Agility还宣称在一家正在运营的客户履约站点获得所谓**首个获OSHA认可的NRTL现场认证**(2025-11,依据ANSI/RIA R15.08、ISO 13849、ISO 12100——具体针对该站点;被认证的站点被普遍认为就是GXO工厂,但官方未具名——未证实)。
- **Schaeffler**——战略投资方(2024-11)兼客户;Digit在南卡罗来纳州Cheraw工厂负责部件装卸;Schaeffler已表示计划到2030年在其全球工厂网络中推广使用(公司声明)。
- **丰田汽车加拿大制造公司(Toyota Motor Manufacturing Canada)**——商业协议签订于2026-02-19;位于安大略省伍德斯托克(Woodstock)的RAV4工厂;试点规模从3台扩展至接近10台,在2026年商业化推广中约为7台(不同报道对7台还是10台说法不一——具体数字应视为尚未确定)。
- **Mercado Libre**——商业协议宣布于2025-12-10;Digit已部署于Mercado Libre位于德克萨斯州圣安东尼奥的履约中心,并正在探索拉美地区的扩展(2025-12起)。
- **亚马逊(Amazon)**——在西雅图地区一处设施测试Digit(2023年起);亚马逊工业创新基金是投资方之一;截至2026-06尚未宣布规模化部署。
- 汇总数据:**9个客户设施累计运行超过65,000小时**(新闻稿原文表述:"通过在九个客户设施的部署承诺,Digit已累计运行超过65,000小时"——即这九个设施为部署*承诺*而非全部已投产设施);Agility是唯一一家公开车队运行小时数的人形机器人制造商(参见[评估](evaluation.md))。以上数字均为公司口径,但部分已获客户方(GXO、Schaeffler、丰田加拿大制造)公告佐证。

## 商业模式与单位经济效益

- **RaaS是核心模式**:Agility保留机器人所有权,客户支付订阅/使用费,涵盖机器人本体、Agility Arc软件、更新及维护。据广泛报道的公司/Johnson口径,定价基准约为**每机器人工时30美元,对标满载人工成本**,并设定**客户投资回收期少于2年**的目标(公司口径,经媒体报道;Johnson在Atoms & Bits访谈中仅给出RaaS"每月数千美元"的说法——具体的每小时30美元数字应视为公司口径,尚未经申报文件证实)。
- 聚合信息源估算RaaS费用大致为**每月每台机器人1万至1.5万美元**,直接购买价格接近**每台25万美元**(两者均未证实;Agility未公开定价)。有分析师估算Digit当前运营成本约为每机器人工时10至12美元,并有望降至2至3美元(单一信息源,未证实)。
- 经济学逻辑:按每小时30美元 × 每日20小时以上工作时长(v5目标为22小时)计算,一台机器人约相当于2至3个人力班次的产出;随着车队软件附加值提升及单位物料清单(BOM)成本下降,利润率有望扩大(行业BOM成本曲线参见[硬件](hardware.md))。
- **订单储备**:超过3亿美元的Digit v5多年期合同,明确**以合同里程碑为前提条件**(即取决于v5的交付进度);客户管道超过30家(公司口径,2026-06)。
- **成本现实**:2025财年运营支出约1.11亿美元,现金消耗约1亿美元(初步/未经审计数据);营收在S-4文件公布前未披露——放眼整个行业,营收充其量只有3000万美元规模,相较于数十亿美元的估值明显不成比例(参见[投资](investment.md))。若赎回比例较低,SPAC募集资金(超过6.2亿美元)将成为通向规模化生产的桥梁资金。

## 与同行相比的优势/劣势

| | Agility的定位 |
|---|---|
| **优势** | 行业内最长的真实客户现场记录(65,000+小时,9个站点,10万+料箱);在RaaS合同(GXO,2024年)和安全认证(NRTL,2025年;Halos合作,2026年;ISO 25785-1标准执笔方)方面均属先行者;拥有公开市场融资渠道以及预计超过6.2亿美元现金储备,而对手仍依赖私募巨额融资;自有工厂(RoboFab)加上富士康作为投资方/规模化伙伴;与营收挂钩的订单储备(3亿美元)而非纯粹的叙事 |
| **劣势** | 应用场景狭窄:料箱/箱体搬运几乎等同于其全部已验证业务——Melonee Wise(Agility前CPO,现就职于KUKA)表示:**"我认为没有人找到过一个需要每个设施部署数千台人形机器人的应用场景。"**("I don't think anyone has found an application for humanoids that would require several thousand robots per facility.")(IEEE Spectrum,2025-09);相较于Figure 03/Atlas的灵巧性,该平台自由度受限——一旦通用操作能力成熟,Digit的硬件上限便会显现;巨额亏损(每年约消耗1亿美元现金)而营收较小;SPAC路线带有逆向选择污名(Churchill旗下项目案例:Lucid、MultiPlan——二者交易价格均远低于合并价格),且面临4.2亿美元信托账户的赎回风险;3亿美元订单属于以里程碑为条件,而非已确认营收;"2027年初实现协作安全"这一时间表此前已跳票一次——Johnson在2024年末(Web Summit)曾表示商业化协作安全将在"未来18至24个月内"实现,即约2026年中至年末 |
| **质疑者论点** | 双足机器人必须在同样的料箱搬运工作流上胜过更廉价的固定自动化设备和自主移动机器人(AMR);大规模人形机器人需求仍属假设(参见IEEE Spectrum文章《现实正在毁掉人形机器人的炒作》"Reality Is Ruining the Humanoid Robot Hype");若仓库料箱搬运走向商品化(类Unitree的定价水平,参见[公司:Unitree](company-unitree.md)),Agility这款美国制造的高端机器仅能凭借安全认证和运行可靠性来竞争 |
| **看多论点** | 是唯一一家其宣称内容大部分获得客户佐证的厂商;安全认证护城河对手难以快速复制;公开上市迫使其接受审计披露——这是对抗自我披露型对手([Figure](company-figure.md)、[Optimus](company-optimus.md))的可信度利器 |

## 制造与供应链定位

本节内容对ODM/EMS读者最具参考价值:

- **优先自建产能**:**RoboFab**(俄勒冈州塞勒姆)——占地7万平方英尺,于2023-09宣布为全球首个专为人形机器人建造的工厂;初期年产数百台,**设计产能约为每年1万台**,满负荷运转时提供500个以上就业岗位。v4的量产原计划于2024年底前启动(Salem Reporter,2024-09)。
- **Digit约75%的零部件在美国境内采购**(公司口径,SPAC相关材料)——这是一个刻意的回岸(reshoring)/地缘政治宣传角度("美国技术领导力"),与以中国为中心的人形机器人物料清单(BOM)形成对比(参见[格局:中国](landscape-china.md))。
- **富士康(Foxconn)是形似ODM的退路安排**:这家全球最大的电子制造服务(EMS)企业牵头了约2亿美元的PIPE私募,且此前已是投资方。围绕该交易的报道将富士康定位为**若v5需求超出RoboFab产能**时的天然合同制造商(报道口径,并非已披露的制造协议——未证实)。战略解读:富士康借此对冲进入人形机器人组装领域(其正另外与NVIDIA合作,在其休斯顿AI服务器工厂部署人形机器人),Agility则无需资本支出即可获得可信的规模化扩产能力。需关注S-4文件中是否有任何正式化的富士康制造条款。
- **Schaeffler的双重角色**:既是投资方也是客户,同时作为精密运动部件(轴承、执行器部件)制造商,有可能成为Digit传动系统的供应商——媒体报道中曾暗示这种供应关系,但未正式披露(未证实)。
- **对NVIDIA的依赖**:IGX Thor + Halos OS如今已成为v5安全架构的核心支撑,加上训练环节的Isaac Sim/Lab——依赖程度很深,但这种单一供应商集中风险为行业内大多数厂商所共有(参见[公司:NVIDIA](company-nvidia.md))。
- 总体定位:**垂直整合的最终组装 + 以美国为主的供应链 + 资本结构中有EMS巨头参与**——最接近的同行对照是Figure的BotQ(完全自建、无EMS合作伙伴)以及Apptronik与Jabil的合作(EMS优先模式)。Agility介于两者之间:它拥有自己的工厂,但在规模化需求尚未出现之前就已预先布局了合同制造关系。

## 来源

- https://www.agilityrobotics.com/content/agility-robotics-to-go-public-through-merger-with-churchill-capital-corp-xi —— 官方SPAC新闻稿:25亿美元pre-money估值,4.2亿美元信托账户+约2亿美元由富士康牵头的PIPE,毛募集资金超6.2亿美元,股票代码AGLT,180天锁定期,3亿美元v5订单,65,000+小时,9个设施,RoboFab年产1万台,约75%美国零部件,Johnson与Hurst的引述
- https://www.businesswire.com/news/home/20260624555633/en/Agility-Robotics-to-Go-Public-Through-$2.5-Billion-Merger-with-Churchill-Capital-Corp-XI —— 交易条款通稿(2026-06-24)
- https://www.therobotreport.com/humanoid-maker-agility-robotics-go-public-through-spac-merger/ —— 对SPAC条款和部署数据的独立确认
- https://www.geekwire.com/2026/digit-maker-agility-robotics-to-go-public-in-2-5b-deal-heres-what-the-filings-say-about-its-finances/ —— 2025财年运营支出约1.11亿美元(2024年约7100万美元),现金消耗约1亿美元(初步/未经审计数据,据SPAC申报文件);亚马逊测试情况
- https://www.sec.gov/Archives/edgar/data/0002074973/000121390026071287/ea029548401ex99-1.htm —— Churchill Capital Corp XI 8-K附件(2026-06):随SEC申报的交易新闻稿
- https://www.forbes.com/sites/johnkoetsier/2026/06/24/first-humanoid-robot-maker-goes-public-in-us-25-billion-deal-new-robot-300-million-in-pre-orders/ —— "首家上市的美国人形机器人厂商"定位口径;v5于同日发布
- https://www.techtimes.com/articles/319099/20260625/humanoid-robot-ipo-agility-robotics-signs-spac-deal-us-nasdaq-debut.htm —— Digit v5:50磅负载,每日22小时,可更换手部,Halos集成,2027年初供货
- https://nvidianews.nvidia.com/news/nvidia-announces-halos-for-robotics-the-industrys-first-full-stack-safety-system-for-physical-ai —— NVIDIA Halos for Robotics发布(2026-06-22,Automate展会):IGX Thor、Halos OS、ANAB认可的检测实验室;"Agility是首家与NVIDIA合作将Halos for Robotics相关要素纳入自有专有安全系统的公司";IEC 61508/ISO 13849/ISO/IEC TR 5469
- https://www.nvidia.com/en-us/case-studies/agility-robotics-digit-humanoid-robot/ —— 全身控制基础模型:Isaac Sim数字孪生、Isaac Lab强化学习、MuJoCo验证;Velagapudi引述
- https://www.agilityrobotics.com/content/gxo-signs-industry-first-multi-year-agreement-with-agility-robotics —— 首个商业化人形机器人RaaS协议(2024-06,官方)
- https://www.agilityrobotics.com/content/digit-moves-over-100k-totes —— GXO Flowery Branch超过10万个料箱(官方,2025-11-20;该文本身未提及NRTL认证)
- https://www.humanoidsdaily.com/news/agility-robotics-secures-osha-recognized-safety-approval-widening-the-gap-between-demo-and-deployment —— 获OSHA认可的NRTL现场检测批准(2025-11):具体针对该站点,依据ANSI/RIA R15.08、ISO 13849、ISO 12100;客户站点未具名
- https://www.agilityrobotics.com/content/agility-robotics-announces-strategic-investment-and-agreement-with-motion-technology-company-schaeffler-group —— Schaeffler投资及部署协议(2024-11,官方)
- https://www.therobotreport.com/schaeffler-plans-global-use-agility-robotics-digit-humanoid/ —— Schaeffler在南卡Cheraw的使用情况及全球推广计划
- https://www.agilityrobotics.com/content/agility-robotics-announces-commercial-agreement-with-toyota-motor-manufacturing-canada —— 丰田加拿大制造协议(2026-02,官方)
- https://techcrunch.com/2026/02/19/toyota-hires-seven-agility-humanoid-robots-for-canadian-factory/ —— 伍德斯托克RAV4工厂部署7台Digit
- https://www.therobotreport.com/toyota-motor-manufacturing-canada-deploys-agility-robotics-digit-humanoids/ —— 丰田加拿大制造试点从3台扩展至10台
- https://www.agilityrobotics.com/content/opening-robofab-worlds-first-factory-for-humanoid-robots —— RoboFab:占地7万平方英尺,首年数百台,年产能1万台,500+就业岗位(官方,2023-09)
- https://www.salemreporter.com/2024/09/03/salem-factory-will-start-mass-producing-humanoid-robots-by-the-end-of-the-year/ —— RoboFab量产启动时间
- https://www.axios.com/2023/12/05/humanoid-robot-factory-agility-bipedal-amazon —— 亚马逊在西雅图附近测试Digit
- https://techcrunch.com/2024/03/05/agility-robotics-new-ceo-is-focused-on-the-here-and-now/ —— Johnson就任,"专注当下"定位
- https://www.agilityrobotics.com/content/agility-robotics-appoints-peggy-johnson-as-chief-executive-officer —— Johnson背景介绍(官方,2024-03)
- https://www.agilityrobotics.com/content/agility-welcomes-robotics-pioneer-melonee-wise-as-new-cto-establishes-new-chief-robot-officer-role-and-celebrates-year-of-outstanding-leadership-growth —— Wise加入担任CTO,Hurst转任首席机器人官(官方,2023年)
- https://www.therobotreport.com/melonee-wise-leads-kuka-new-software-ai-organization/ —— Wise离职(2025-08)加入KUKA
- https://spectrum.ieee.org/humanoid-robot-scaling —— IEEE Spectrum文章《现实正在毁掉人形机器人的炒作》(2025-09-11,Ackerman撰文);Wise原话:"我认为没有人找到过一个需要每个设施部署数千台人形机器人的应用场景。"
- https://techinformed.com/web-summit-2024-humanoid-robots-has-the-hardware-caught-up-with-the-software/ —— Johnson在2024年Web Summit的发言:协作安全商业化将在"未来18至24个月内"实现(该时间表后来跳票至2027年初)
- https://www.agilityrobotics.com/content/mercado-libre-and-agility-robotics-announce-commercial-agreement —— Mercado Libre商业协议,德克萨斯州圣安东尼奥(官方,2025-12-10)
- https://spectrum.ieee.org/agility-robotics-introduces-cassie-a-dynamic-and-talented-robot-delivery-ostrich —— Cassie发布(2017年),弹簧-质量谱系
- https://oregonbusiness.com/17736-i-robot/ —— 创业故事:Hurst、Shelton、Jones;俄勒冈州立大学分拆;ATRIAS/DARPA
- https://atomsbitsnewsletter.substack.com/p/qa8-peggy-johnson-ceo-of-agility —— Johnson谈RaaS经济学("每月数千美元"),反"后空翻"式定位
- https://robots4therestofus.substack.com/p/jonathan-hurst-of-agility-robotics —— Hurst理念播客(节目页面;增强框架——无公开文字稿,引述为转述)
- https://tsginvest.com/agility-robotics/ —— 每机器人工时30美元的RaaS基准+投资回收期低于2年的目标,运营成本估算(聚合信息源;数字为公司口径,未经申报文件证实)
- https://blog.robozaps.com/b/agility-robotics-digit-review —— Digit v4聚合信息源规格(约175厘米,65公斤,16公斤负载——未证实)
- https://robotsandstartups.substack.com/p/why-a-spac-for-agility-makes-sense —— Andra Keay为SPAC选择做的辩护性分析
- https://www.thescenarionist.com/p/the-humanoid-spac-test-deep-tech —— SPAC结构质疑者论点
