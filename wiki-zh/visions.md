---
title: "愿景与论点：领军者如何构建物理AI(Physical AI)的叙事框架"
slug: visions
updated: 2026-07-05
confidence: verified
lang: zh
source: ../wiki/visions.md
---
> 物理AI(Physical AI)领域最具影响力的十余位人物,除了都认同"这个市场规模巨大"之外,几乎没有其他共识。Jensen Huang 兜售一个 40-50 万亿美元的劳动力自动化总目标市场(TAM),其 CES 2026 主题演讲宣称"物理AI的 ChatGPT 时刻"已近在眼前;Elon Musk 声称"特斯拉约 80% 的价值将来自 Optimus"(X 平台,2025-09),而这与该行业最糟糕的交付记录形成对照;Demis Hassabis 将具身智能(embodied intelligence)定位为通用人工智能(AGI)的核心支柱,并预计机器人领域将在"未来约18个月内"(2026-02)迎来突破;Fei-Fei Li 和 Yann LeCun 都认为大语言模型(LLM)是错误的底层架构,世界模型(world model)才是正确方向——Li 的路径是"空间智能(spatial intelligence)",LeCun 则通过反生成式的 JEPA 架构与一家估值十亿美元级的初创公司(AMI Labs);Masayoshi Son(孙正义)斥资 54 亿美元收购 ABB Robotics,意图"融合超级人工智能(Artificial Super Intelligence)与机器人技术";Jeff Bezos 几乎为美国每一个机器人"大脑"实验室都提供了个人投资,却坚称自己的物理AI初创公司"与机器人技术毫无关系";Brett Adcock 与王兴兴分别押注于成本曲线两端的人形机器人;Karol Hausman 和 Sergey Levine 则认定"大脑"比任何"身体"都更重要。而反对的声音——Rodney Brooks、Gary Marcus、Ken Goldberg——则强力反击;Brooks 将依靠视频训练获得人形机器人灵巧操作能力的想法称为"纯粹的幻想"。这些论点在世界模型以及"软件而非硬件才是瓶颈"这一点上趋于一致;但在形态(form factor)、时间线,以及市场规模究竟是 380 亿美元还是 50 万亿美元的问题上则严重分歧。背景资料:[关键人物](key-people.md)、[投资](investment.md)、[待解决的问题](open-problems.md)、[技术前沿](state-of-the-art.md)。

## 如何阅读本页

- 以下引语均标注日期,并尽可能采用一手来源(主题演讲、财报电话会、X 帖子、官方发布、发表的文章)。二手引述已作标注。
- 有三类修辞需要区分:**投资人话术型框架(investor-pitch framing)**(TAM 数字、"史上最大产品"等说法)、**运营指引(operational guidance)**(生产日期、产量数字——法律风险更高的一类),以及**研究论点(research theses)**(可证伪的架构性判断)。同一个人常常在同一句话中混杂这三类表达;本页对此做了区分。
- "宣称 vs 实际交付"的对照记录见于各公司深度报告([Optimus](company-optimus.md)、[Figure](company-figure.md));本页只覆盖叠加在其上的"叙事框架"层面。

## TAM 阶梯——谁在宣称什么(截至 2026-07)

| 主张 | 主张者、场合、日期 | 类别 |
|---|---|---|
| 覆盖工厂、交通运输和人形机器人的 50 万亿美元市场机遇 | Jensen Huang,GTC 巴黎主题演讲,2025-06(媒体转述,非逐字引语) | 投资人话术 |
| 人形机器人是一个"约 40 万亿美元"的劳动力自动化市场 | Huang,据财经媒体多次引述(截至 2026-05,二手来源) | 投资人话术 |
| 体力劳动约占全球 GDP 的 50%,"约 42 万亿美元/年" | Figure《总体规划(Master Plan)》(官方公司文件) | 投资人话术 |
| "特斯拉约 80% 的价值将来自 Optimus" | Elon Musk,X 帖子,2025-09-01 | 投资人话术 |
| Optimus 可能使特斯拉成为"一家 25 万亿美元的公司" | Musk,特斯拉年度股东大会,2024-06(广泛报道) | 投资人话术 |
| 机器人技术作为万亿美元级的软银下一前沿领域;¥1000 万亿(约 6.2 万亿美元)净资产价值(NAV)目标 | Masayoshi Son(孙正义),软银年度股东大会,2026-06-24 | 投资人话术 |
| 到 2050 年约 5 万亿美元的人形机器人生态系统 | 摩根士丹利(Morgan Stanley)(2025) | 分析师预测 |
| 到 2035 年 380 亿美元人形机器人 TAM,约 140 万台 | 高盛(Goldman Sachs)(2024-02 修订) | 分析师预测 |

- 上表最高与最低数字之间相差约**三个数量级**;每一个万亿美元级数字都假定[操作/抓取(manipulation)](manipulation.md)、廉价[硬件](hardware.md)以及数据方面的突破均已解决,而这些至今仍是[待解决的问题](open-problems.md)。该细分领域披露营收规模最大的公司(Unitree)2025 年全年披露营收约为 2.35 亿美元([投资](investment.md))。

## Jensen Huang(NVIDIA)——物理AI作为下一波浪潮

- **论点**:AI 按浪潮演进——感知AI(perception AI)→ 生成式AI(generative AI)→ 智能体AI(agentic AI)→ **物理AI(physical AI)**("理解物理定律的AI,能与我们共同工作的AI");无论哪家机器人厂商胜出,NVIDIA 都为这最后一波浪潮销售底层平台。参见 [NVIDIA 深度报告](company-nvidia.md)。
- **"ChatGPT 时刻"叙事时钟**(一台持续滴答作响的营销时钟):"通用机器人的 ChatGPT 时刻即将到来"(CES 主题演讲,2025-01-06)→"通用机器人时代已经到来"(GTC,2025-03)→"物理AI的 ChatGPT 时刻已近在眼前,但挑战显而易见。物理世界是多样且不可预测的"(CES 主题演讲,2026-01,据 Rev 转录稿——该句是在主题演讲的 Cosmos 视频片段中被旁白念出,并非 Huang 本人直接说出;部分媒体报道将其表述为"已经到来")→"物理AI已经到来——每一家工业公司都将成为机器人公司"(GTC,2026-03)。
- **"三台计算机"论**(自 2024 年末以来的经典表述):"打造自动驾驶汽车,和打造所有机器人一样,需要三台计算机:用于训练AI模型的 NVIDIA DGX、用于试驾和生成合成数据的 Omniverse,以及车内的超级计算机 DRIVE AGX"(CES 2025)——训练(DGX)/仿真(Omniverse+Cosmos)/执行(Jetson),全部运行在 NVIDIA 芯片上。
- **TAM 叙事框架**:覆盖工厂、交通运输、人形机器人的 50 万亿美元(GTC 巴黎,2025-06,二手来源);约 40 万亿美元的人形机器人劳动力市场(财经媒体,2026-05,二手来源)。他将物理AI定义为需要"对世界运作方式的常识。物体恒存性……因果关系……摩擦力和重力"(CES 2026)。
- **修辞与实际披露的对比**:NVIDIA 的汽车与机器人业务板块在 2160 亿美元的 2026 财年总营收中约占 23 亿美元(约 1%),机器人业务并未单独披露——TAM 话术实质上是在为算力创造需求,而 Cosmos 明确表示"把数据问题换成了算力问题"(GTC 2026 的叙事框架)。

## Elon Musk(特斯拉)——Optimus 作为史上最大产品

- **价值主张**:"特斯拉约 80% 的价值将来自 Optimus"(X,2025-09-01——恰好是特斯拉发布《总体规划第四部分(Master Plan Part 4)》"可持续富足"宣言的同一天);更早前:Optimus 可能使特斯拉成为"一家 25 万亿美元的公司"(年度股东大会,2024-06,经 CNBC 广泛转述报道)。他约 1 万亿美元的薪酬方案(2025-11-06 批准)将**"交付 100 万台机器人"**嵌入为一项里程碑指标——这一主张如今已成为资本配置框架的一部分,而不仅仅是口头表态。
- **产品主张**:"我认为 Optimus 将是我们最大的产品,不仅是特斯拉史上最大的产品,可能也是史上最大的产品……我仍然坚信这一结论"(2026年第一季度财报电话会,2026-04-22,据电话会记录)。
- **运营指引远比愿景谦逊得多**:在 2025 年第四季度财报电话会(2026-01-28)上,Musk 承认"我们在 Optimus 上仍处于非常早期的阶段。它仍处于研发阶段",且"尚未在我们的工厂中实质性地投入使用";在 2026-07-02,他警告"生产初期将极其缓慢……这不像造汽车"。
- **时间线记录**:自 2021 年以来每一个重大量产目标均未达成(承诺 2025 年交付 1 万台 → 实际造出"数百台")——完整的宣称与交付对照记录见于 [Optimus 深度报告](company-optimus.md)。Musk 的叙事是该领域中投资人话术与运营指引在同一位发言人身上分裂最纯粹的案例。
- **架构论点**:汽车是"装了轮子的机器人"(AI Day,2021-08)——FSD 的纯视觉端到端技术栈、车队数据、神经网络世界模拟器和定制芯片可直接迁移到人形机器人上;这是一个投射到不同具身形态上的单一基础模型(Elluswamy,CVPR 2026,聚合媒体来源)。

## Demis Hassabis(谷歌 DeepMind)——通往AGI之路上的具身智能

- **论点**:真正的通用智能需要理解时空维度上的物理世界;"智能体物理能动性(intelligent physical agency)"是AGI的核心支柱,而非事后附加的一项应用。关于AGI本身:"未来五到十年内"(谷歌 I/O 与 Sergey Brin 的炉边谈话,2025-05)。
- **瓶颈论**:"机器人技术的瓶颈与其说在硬件……不如说其实一直是软件智能拖了机器人的后腿"(采访,2025,二手引述)——与 Brooks 的硬件/传感论点直接相反,而与 Hausman 和王兴兴的立场一致。
- **时间线**:AI驱动的机器人技术"将在未来几年内迎来突破时刻"(接受 WIRED 采访,约2025-11,经 Semafor 转载);后收紧为"未来约18个月内,我们将在机器人领域看到突破时刻"(《财富》,2026-02-11)。
- **战略**:将 Gemini 作为机器人技术的"操作系统"(Semafor,2025-11)——跨具身形态的闭源模型(Gemini Robotics 2025-03 → On-Device 2025-06 → 搭载ER推理器的 Robotics 1.5,2025-09)被授权用于合作伙伴的硬件(对 Apptronik 的投资与合作;部署于 Atlas 和 Apollo),而非自行制造机器人。这是一种资本轻量化、与具身形态无关的路径;与[Figure](company-figure.md)的垂直整合形成对照。参见 [VLA模型](vla-models.md)。

## Fei-Fei Li(World Labs / 斯坦福大学)——空间智能宣言

- **宣言**:《从词语到世界:空间智能是AI的下一前沿》("From Words to Worlds: Spatial Intelligence is AI's Next Frontier")(Substack,2025-11-10)。对LLM的核心批评:"它们仍是黑暗中的文字工匠;能言善辩却缺乏经验,博学却不接地气。"

  > 原文:"they remain wordsmiths in the dark; eloquent but inexperienced, knowledgeable but ungrounded."

- **正面论点**:下一个前沿是**世界模型(world models)**——能"生成具有感知、几何和物理一致性的世界"并"根据输入的动作输出下一状态"的生成式、多模态、交互式系统——这需要植根于几何/物理的全新训练目标,以及超越一维标记化(1D tokenization)的架构。参见[世界模型](world-models.md)。
- **机器人是下游应用,而非产品本身**:"从昆虫到人类的动物都依赖空间智能来理解、导航并与世界互动。机器人也不例外。"

  > 原文:"Animals from insects to humans depend on spatial intelligence to understand, navigate and interact with their worlds. Robots will be no different."

  World Labs 销售的是世界模型(Marble,首个商用生成式3D世界模型,2025-11;由 Autodesk 领投的 10 亿美元融资轮,2026-02-18),而非机器人本身——机器人只是与创意工具、科学研究并列的几个应用市场之一。

## Yann LeCun(AMI Labs)——以世界模型对抗LLM共识

- **否定性论点**(自约2022年起公开持有,2024-26年间观点更加尖锐):扩展LLM的规模无法达到人类水平的智能;自回归的标记预测(autoregressive token prediction)缺乏持久记忆、世界建模和规划能力。在达沃斯论坛(2025-01-23)他预测三到五年内将出现"AI架构的新范式",并宣布未来数年为**"机器人的十年"**。
- **正面论点**:反生成式的**JEPA系列世界模型**,在表征空间(representation space)而非像素空间中进行预测——这正是机器人预测行动后果所需的架构(V-JEPA 2,2025-06;参见[世界模型](world-models.md))。他更倾向使用"高级机器智能(Advanced Machine Intelligence,AMI)"这一说法而非"AGI"。
- **付诸行动**:2025-11 离开 Meta,结束长达12年的任职;共同创立**AMI Labs**(总部巴黎;CEO 为 Alexandre LeBrun),该公司以**35亿美元投前估值完成了10.3亿美元种子轮融资(2026-03-09)**——欧洲史上最大的种子轮——由 Bezos Expeditions 联合领投(与 Cathay Innovation、Greycroft、Hiro Capital、HV Capital 共同领投),NVIDIA、三星(Samsung)、淡马锡(Temasek)、丰田风投(Toyota Ventures)参与其中。首个公布的应用领域是医疗健康(与 Nabla 合作),世界模型被定位为解锁一切的关键——从"真正实用的家用机器人"到 L5 级自动驾驶(《麻省理工科技评论》,2026-01-22,该文将这一项目称为"一次对抗大语言模型的反主流投资")。
- 值得注意的讽刺之处:该领域最响亮的LLM怀疑者(LeCun)与最响亮的人形机器人怀疑者(Brooks)在诊断上达成一致(当前的技术栈无法在物理世界中实现自我"接地"),但在处方上并不一致(LeCun:新架构将解决问题;Brooks:触觉/力觉数据以及形态本身才是难以逾越的墙)。

## Masayoshi Son(孙正义,软银)——超级人工智能与机器人技术的融合

- **论点原话**:"软银的下一个前沿是物理AI。我们将与ABB Robotics携手,在共同愿景下融合世界级的技术与人才,以融合超级人工智能与机器人技术——推动一场将推进人类前进的突破性演进"(官方发布,2025-10-08)。孙正义长期将超级人工智能(ASI)描述为"比人类聪明1万倍",目标时间点约为2035年(软银年度股东大会,2024-06)。
- **实际出手记录(截至2026-07)**:以**53.75亿美元收购ABB机器人业务**(2025-10-08;预计于2026年年中至年末完成交割)——收购一家排名第二的老牌工业机器人厂商,作为其AI论点的"身体";**领投Skild AI的14亿美元融资轮,估值超过140亿美元**(2026-01);据报道机器人相关资产被整合到一家名为"Robo HD"的控股公司之下;此外还有OpenAI一方的**Stargate**项目敞口。据报道:一家名为"Roze"的美国AI+机器人公司,目标估值约1000亿美元,最快于2026年下半年上市(仅有聚合媒体来源,未证实)。
- **2026年股东大会言论**(2026-06-24):在超级人工智能论点下设定16年内达到¥1000万亿(约6.2万亿美元)净资产价值目标(约14倍增长);"如果你说这是泡沫,我认为这是对AI的亵渎",AI革命"才刚刚开始";宣称是"全球首家实现机器人规模化制造机器人"的公司,在一座"物理AI工厂"内(公司口径,未证实);驳斥Musk的轨道数据中心构想没有太大意义——AI竞赛将由地球上的算力在"未来几年内"赢得(彭博社/《日本时报》)。
- 独特立场:孙正义是唯一一位收购**工业机器人老牌企业**(ABB的装机基础)而非仅仅投资人形机器人初创公司的超级资本配置者——这是一个物理AI将首先通过现有工厂自动化实现变现的判断。参见[投资](investment.md)、[公司:Skild](company-skild.md)。

## Jeff Bezos——组合投资论点(以及一个引人注目的例外)

- 没有宣言;论点体现在他的支票簿里。个人/Bezos Expeditions的投资跨越**每一个层面**:机器人"大脑"([Physical Intelligence](company-pi.md) A轮+B轮;[Skild](company-skild.md))、一家垂直整合的人形机器人公司([Figure](company-figure.md) B轮,2024-02)、腿式配送硬件(RIVR种子轮;2026-03被亚马逊收购),以及世界模型(**联合领投**LeCun的AMI Labs种子轮,2026-03)——也就是说,在*相互竞争*的架构论点上,他同时做多模型这一层。
- **Prometheus项目**(与Vik Bajaj共同担任联合CEO;以62亿美元启动,2025-11;以410亿美元估值获得120亿美元融资,2026-06-11):打造一个用于计算、航空航天、汽车领域设计与制造的"通用工程师式AI(artificial general engineer)"——一种"从真实世界的试错中学习",而非仅从数字数据中学习的AI。Bezos明确表示该公司"与机器人技术毫无关系"(CNBC,2026-06-11)——这是关于**物理AI ≠ 机器人**这一观点最清晰的公开表态:即便没有具身形态,"为实体世界赋予智能"这一层本身就是一个市场。
- 背景评论:AI是"某种工业泡沫",但其带来的好处"是巨大的"且真实存在(意大利科技周,2025-10,广泛报道)——一边承认泡沫,一边加大投资敞口。

## Brett Adcock(Figure)——以人形机器人为先的垂直整合

- **《总体规划》叙事框架**(官方):体力劳动报酬约占全球GDP的50%("约42万亿美元/年");随着人形机器人"加入劳动力大军",劳动力成本将趋向于租用一台机器人的价格;终局是劳动力不再是稀缺资源的富足状态。Adcock将这一机遇的规模定为"大约40万亿美元"(二手来源),并宣称:"如果机器人运行良好,我们将有能力在商业劳动力中交付数十亿台机器人";"我们认为劳动力中将有数十亿台机器人……最终随着时间推移,它们也会进入太空"(《时代》杂志,2025-10)。
- **垂直整合论点**:一家公司必须同时拥有模型、硬件、工厂和车队数据——在放弃OpenAI合作时表态:"我们无法外包AI,理由与我们无法外包硬件是一样的"(2025-02-04);Helix被定位为"软件2.0(Software 2.0)",取代此前约10.9万行手写的机器人C++代码(2026-01,公司主张)。
- **形态论点**:世界是为人类而建造的,因此一台能够泛化的人形机器人胜过许多专用机器——这与下文Brooks的观点、以及与具身形态无关的Pi/Skild路径直接对立。
- 象征性里程碑:"Figure内部,机器人数量首次超过了人类员工数量"(X,2026-06-20——公司内部车队数据,公司口径)。宣称与交付的对照记录见于[Figure深度报告](company-figure.md)。

## Karol Hausman 与 Sergey Levine(Physical Intelligence)——与具身形态无关的机器人大脑

- **论点**:瓶颈在于智能,而非硬件或机械设计;打造**一个通才型模型**("一个机器人大脑"),在来自多种机器人类型的异构数据上训练,并将这一智能出售给每一种"身体"——π0 → π0.5 → π*0.6 → π0.7,覆盖机械臂、移动底盘、人形机器人等([公司:PI](company-pi.md)、[VLA模型](vla-models.md))。预计LLM式的规模化(scaling)动力学也会同样适用:"曾经改变语言模型的那种规模化动力学,或许也能解锁机器人智能"(Generalist采访叙事框架,2026-03-17)。
- **Levine的规模化主张**:借助π0.7,一旦跨任务的"技能重组(skill remixing)"能力涌现,能力就会"以超线性的速度随数据增长而增长"(TechCrunch,2026-04)——这是该领域关于机器人技术中出现"能力涌现体制"最有力的公开主张。他长期坚持的立场是:通往目标的路径要经过**大规模的真实世界跨具身形态机器人数据**,而非仅靠仿真或人类视频(CoRL演讲,2024-25)。
- **物理智能作为通往AGI的路径**:Hausman认为,解决物理智能问题就是解决智能问题——物理世界"比起被描述,要难以被模拟得多",因此一个掌握了物理世界的AI也就囊括了其余一切(采访叙事框架,2026-03)。
- 同样是"大脑优先"的论点,但风格不同:**Deepak Pathak的Skild**主打一个横跨四足机器人到人形机器人的"全具身(omni-bodied)"大脑([公司:Skild](company-skild.md));NVIDIA的GR00T则是这一思路的平台化版本([公司:NVIDIA](company-nvidia.md))。

## 王兴兴(Unitree)——成本下探的大众市场,模型瓶颈论的逆势派

- **成本论点(已付诸实践,而非仅停留在口头)**:将价格下限一路压低,直到机器人变成消费电子产品——四足机器人从4.5万美元降至1600美元(2017→2023);人形机器人H1约9万美元(2023)→ G1约1.35万美元(2024)→ **R1 ¥39900(约5900美元,2025-07)**——凭借极致的垂直整合实现约60%的毛利率([Unitree深度报告](company-unitree.md))。硬件先行,智能在已有装机量基础上逐步追赶。
- **"ChatGPT时刻"定义**(2026中国网络媒体论坛,2026-03-29):如果一台机器人被投放到陌生场景中,能够根据语音/语言指令,在约80%的场景中完成约80%的任务——这是他反复提及的"双80%"表述,也曾于2025-11向新华社表述过;部分对该论坛的报道将其表述为"80-90%的任务"——具身AI就已经迎来了它的ChatGPT时刻。他预计这将在**约2-3年内**发生(2026-03-29);在其世界机器人大会(WRC)主题演讲(2025-08-09)中,他将区间定为快则1-3年、慢则3-5年,并表示整个具身AI浪潮的实现不会超过约10年。他将该领域描述为处于"临界点前夜"的状态:方向已经找到,但阈值尚未跨越(2025-26年间的表态)。
- **逆势派瓶颈主张**(世界机器人大会主题演讲,2025-08-09):制约因素在于**模型,而非数据**——"对机器人数据的关注度有点过高了,最大的问题在模型"(对"数据关注度太高,最大问题在模型"的转述);当前的VLA模型是一种"傻瓜式"架构;他预计**视频生成/世界模型驱动的控制**将更快取得进展。这与Pi/Figure/NVIDIA所持的数据瓶颈共识直接相悖([数据](data.md))。
- **产量预判**:全球人形机器人出货量可以保持每年翻倍增长;若在2-3年内出现重大AI突破,单年出货量可能跃升至数十万台——"甚至上百万台以上"(2025-26年间采访,公司立场趋于乐观)。

## 反对方——有据可查的公开怀疑者

- **Rodney Brooks**(iRobot/Rethink联合创始人;包容架构subsumption architecture的先驱人物——见[历史](history.md))。文章《为何今天的人形机器人学不会灵巧操作》("Why Today's Humanoids Won't Learn Dexterity")(rodneybrooks.com,2025-09-26):认为相信今天的人形机器人能在"未来数十年内的任何时候"学会人类水平的灵巧操作"纯属幻想",因为视频不携带触觉/力觉信号,而人类手掌拥有约17000个低阈值机械感受器;全尺寸双足机器人在靠近人类时本质上是不安全的(他所谓的约3米规则);"十五年后"真正成功的机器人"既不会长得像今天的人形机器人,也不会长得像人类"(轮式、多机械臂);预计这股热潮将以类似Gartner曲线的"幻灭低谷"收场,并伴随目标不断被重新定义。他与之配套、标注了日期的预测(2025-09/10,并在其2026-01-01的"预测记分卡"中重申):可部署的"灵巧操作能力相比人类手掌将持续表现糟糕,时间点将**超过2036年**"。他针对Musk再次重申:人形通才助手是"纯属幻想"(《财富》,2026-02-25)。完整技术层面的论述见[待解决的问题](open-problems.md)。
- **Gary Marcus**(纽约大学荣休教授;深度学习的老牌怀疑者)。就机器人技术而言:曾称Optimus的发布"多少有点令人失望",没有清晰的市场推进路径(IEEE Spectrum综述,2022-10;Substack专栏"Sub-Optimal");针对Musk关于2040年人形机器人数量将超过人类的预测:"Elon在AI预测上一贯过度乐观,这次也不例外",并以目前全球仅约15亿辆汽车存量作为采纳上限的类比(Decrypt,2024-10);多次在人形机器人演示中放大对遥操作(teleoperation)问题的关注。机器人技术对Marcus而言是次要战场(他的主要靶子是LLM的推理能力),因此他在机器人方面的公开记录比Brooks单薄(分析判断)。
- **Ken Goldberg**(加州大学伯克利分校):机器人所需数据与现有数据之间存在"10万年的数据鸿沟";未来"2年、5年,甚至10年内"都不会出现管家机器人/外科医生机器人(2025-08)——这是Brooks数据论点的学术版本,不过Goldberg支持通过工程手段加上部署数据来实现自举式发展。
- 元观察(引自[待解决的问题](open-problems.md)第8节):时间线最短的预测来自机器人或算力的卖方,最长的预测来自没有损益表(P&L)压力的学者。二者都带有各自的利益驱动;应关注"经济性下的可靠性"这类里程碑,而非单纯的时间预测。

## 一致与分歧矩阵

各方论点**一致**之处(截至2026-07):

- **软件/智能才是瓶颈,而非执行器**——Huang、Hassabis、Hausman/Levine、Adcock、王兴兴、孙正义都以各自的方式表达了这一观点;即便是Brooks也承认硬件已经足够,他只是在"缺失清单"中额外加上了传感(触觉/力觉)。
- **世界模型是下一层架构**——这一点在Li(宣言)、LeCun(JEPA/AMI)、Huang(Cosmos/DreamZero)、王兴兴(视频生成驱动的控制)、特斯拉(神经网络世界模拟器)、1X身上都有明确体现;VLA与世界模型这两条线索正明显走向融合([世界模型](world-models.md)、[VLA模型](vla-models.md))。
- **数据稀缺决定了这场竞赛的胜负**——这是近乎共识的观点(Pi、Figure×Brookfield、NVIDIA的合成数据、Goldberg的数据鸿沟论、Brooks的触觉数据批评),王兴兴是其中声音最响亮的异议者(主张模型架构优先)。
- **奖励是劳动力市场,即数十万亿美元规模**——每一位卖方的TAM本质上都是对全球劳动力份额的一种计算(Huang的40-50万亿美元、Figure的42万亿美元/年框架、Musk的"占特斯拉价值80%"),而非自下而上的单位量预测。

各方论点**分歧**之处:

| 维度 | 立场 |
|---|---|
| 形态 | 人形优先:Musk、Adcock、王兴兴、(孙正义通过ABB+人形机器人投资) ↔ 与具身形态无关的大脑路径:Hausman/Levine、Pathak、NVIDIA、Hassabis ↔ 反人形:Brooks(轮式+任务专用形态才会胜出) |
| 瓶颈 | 数据:Pi、Figure、NVIDIA、Goldberg ↔ 模型架构:王兴兴、LeCun、Li ↔ 触觉/力觉传感与接触物理学:Brooks |
| 与LLM的血缘关系 | 基于VLM底座构建的VLA(Pi、DeepMind、Figure、NVIDIA) ↔ LLM从根本上就是错误的底层架构(LeCun、Li;王兴兴称VLA为"傻瓜式架构") |
| "ChatGPT时刻"的时间线 | 已经到来/近在眼前:Huang(CES/GTC 2026)、Adcock ↔ 18个月至3年:Hassabis、王兴兴 ↔ 5-10年以上:Goldberg ↔ 灵巧操作要到2036年以后:Brooks |
| TAM | 40-50万亿美元(Huang、Adcock、与Musk相关的估计) ↔ 到2050年5万亿美元(摩根士丹利) ↔ 到2035年380亿美元(高盛)——一个1000倍的差距 |
| 谁将攫取价值 | 平台/算力(Huang) ↔ 垂直整合者(Musk、Adcock) ↔ 出售给所有"身体"的模型层(Hausman、Pathak、Hassabis) ↔ 规模化的低成本硬件(王兴兴) ↔ 老牌装机基础+资本(孙正义) |
| 机器人技术与AGI的关系 | 具身形态是AGI的必需/核心要素:Hassabis、Hausman、LeCun(接地问题) ↔ 物理AI即便没有机器人也有价值:Bezos-Prometheus("与机器人技术毫无关系")、Li(机器人只是空间智能的一种应用) |
| 这是否是泡沫? | 说是泡沫就是"亵渎":孙正义 ↔ 是泡沫但值得投入:Bezos ↔ 泡沫终将破裂:Brooks;中国国家发展改革委(NDRC)也曾发出过警告([投资](investment.md)) |

- **高管视角的解读**:这些看多的论点并非同一个论点。一个敞口于"物理AI"的投资组合,实际上同时做多了一系列互不兼容的判断——人形与非人形、数据规模化与新架构、平台化与垂直整合。唯一一个各方普遍认同且可证伪的近期主张,是Hassabis/王兴兴式的判断:到约2028年将出现一次可见的泛化能力突破。Brooks关于灵巧操作的论断(数十年内不会出现人类水平的手部操作技能)是用来检验所有人主张的最清晰的对照基准。

## 来源

- https://blogs.nvidia.com/blog/ces-2025-jensen-huang/ —— CES 2025主题演讲:"通用机器人的ChatGPT时刻即将到来";三台计算机的原话(官方)
- https://www.rev.com/transcripts/nvidia-at-ces-2026 —— CES 2026转录稿:"物理AI的ChatGPT时刻已近在眼前"(在Cosmos视频片段中被旁白念出);Huang对物理AI/常识的定义(一手转录稿)
- https://www.manufacturingdive.com/news/industrial-robotics-companies-everywhere-says-nvidia-ceo-gtc-2026-abb-fanuc-ai/815042/ —— GTC 2026(2026-03-16):Huang:"每一家工业公司都将成为机器人公司";"物理AI已经到来"的叙事框架
- https://gamesbeat.com/nvidia-believes-physical-ai-systems-are-a-50-trillion-market-opportunity/ —— Huang在GTC巴黎提出的50万亿美元物理AI叙事框架(2025-06,二手来源;媒体转述,无逐字引语)
- https://247wallst.com/investing/2026/05/31/jensen-huang-just-called-humanoid-robots-a-40-trillion-market-heres-why-wall-street-is-loading-up-on-physical-ai-stocks/ —— 40万亿美元人形机器人TAM的归因引述(2026-05,二手来源)
- https://x.com/elonmusk/status/1962618811141812475 —— Musk一手帖子:"特斯拉约80%的价值将来自Optimus"(2025-09-01)
- https://www.cnbc.com/2025/09/02/musk-tesla-value-optimus-robot.html —— 背景:与总体规划第四部分同日发布的时机;此前25万亿美元公司说法的回顾
- https://www.npr.org/2026/04/22/nx-s1-5791653/tesla-earnings-first-quarter-2026 —— 2026年第一季度财报电话会报道:最大产品叙事框架;2026年夏季量产,明年"在特斯拉之外"实现实用化
- https://www.investing.com/news/transcripts/earnings-call-transcript-tesla-beats-q1-2026-eps-forecasts-stock-rises-93CH-4631008 —— 2026年第一季度电话会转录稿:"我认为Optimus将是我们最大的产品,不仅是特斯拉史上最大的产品,可能也是史上最大的产品";"我仍然坚信这一结论"(逐字引述)
- https://www.semafor.com/article/11/23/2025/deepmind-deepens-push-into-robotics —— Hassabis对WIRED表态:机器人"未来几年内的突破时刻";Gemini作为操作系统的战略(2025-11)
- https://fortune.com/article/fortune-500-titans-and-disruptors-of-industry-google-deepmind-demis-hassabis-isomorphic-artificial-intelligence/ —— Hassabis:"未来约18个月内,我们将在机器人领域看到突破时刻"(2026-02-11)
- https://kantrowitz.medium.com/demis-hassabis-and-sergey-brin-on-ai-scaling-agi-timeline-robotics-simulation-theory-ef3f7a740eeb —— I/O 2025炉边谈话:AGI"未来五到十年"(2025-05)
- https://www.digit.in/features/general/demis-hassabis-says-ai-led-robot-revolution-is-unfolding-right-now-heres-why.html/amp/ —— Hassabis"瓶颈……软件智能"引语(二手来源)
- https://drfeifei.substack.com/p/from-words-to-worlds-spatial-intelligence —— Fei-Fei Li宣言(2025-11-10):"黑暗中的文字工匠"、世界模型定义、机器人"也不例外"(一手来源)
- https://techcrunch.com/2025/01/23/metas-yann-lecun-predicts-a-new-ai-architectures-paradigm-within-5-years-and-decade-of-robotics/ —— LeCun在2025年达沃斯的表态:新范式预测,"机器人的十年"
- https://www.technologyreview.com/2026/01/22/1131661/yann-lecuns-new-venture-ami-labs/ —— AMI Labs被称为"一次对抗大语言模型的反主流投资"(2026-01)
- https://techcrunch.com/2026/03/09/yann-lecuns-ami-labs-raises-1-03-billion-to-build-world-models/ —— AMI Labs以35亿美元投前估值完成10.3亿美元种子轮融资(2026-03-09);LeBrun的表态;Bezos Expeditions联合领投
- https://group.softbank/en/news/press/20251008 —— 孙正义一手引语:"软银的下一个前沿是物理AI……融合超级人工智能与机器人技术";ABB交易53.75亿美元(2025-10-08)
- https://www.forbes.com/sites/iansayson/2025/10/08/billionaire-masayoshi-sons-softbank-deepens-ai-push-with-54-billion-abb-robotics-deal/ —— ABB机器人交易报道,交割时间线
- https://www.thestandard.com.hk/innovation/article/335487/Talk-of-a-bubble-is-blasphemy-against-AI-says-SoftBanks-Son —— 孙正义2026年股东大会(2026-06-24):"如果你说这是泡沫,我认为这是对AI的亵渎";机器人制造机器人的主张
- https://www.japantimes.co.jp/business/2026/06/23/companies/softbank-dismissal-musk-idea-data-centers/ —— 孙正义驳斥Musk的轨道数据中心构想(意义不大;地球算力将在"未来几年内"取胜)
- https://finance.biggo.com/news/bdc0a37f-28fe-453d-b8e6-ba8af661a224 —— 孙正义股东大会:¥1000万亿NAV目标,ASI 1万倍智能的叙事框架(二手来源)
- https://www.outlookbusiness.com/deeptech/masayoshi-son-rejects-ai-bubble-fears-outlines-softbanks-plans-of-robots-manufacturing-robots —— "机器人规模化制造机器人";Roze目标估值1000亿美元IPO(有报道,未证实)
- https://www.businesswire.com/news/home/20260114335623/en/Skild-AI-Raises-$1.4B-Now-Valued-Over-$14B —— 软银领投Skild融资轮(2026-01)
- https://www.cnbc.com/2026/06/11/project-prometheus-bezos-bajaj-live-updates.html —— Bezos谈Prometheus:"通用工程师式AI","与机器人技术毫无关系"(2026-06-11)
- https://techcrunch.com/2026/06/11/jeff-bezoss-prometheus-raises-12b-to-build-an-artificial-general-engineer-for-the-physical-world/ —— Prometheus以410亿美元估值获得120亿美元融资;真实世界试错的叙事框架
- https://www.figure.ai/master-plan —— Figure《总体规划》:劳动力约占全球GDP的50%(约42万亿美元/年),租用机器人的成本逻辑(官方来源)
- https://time.com/7324233/figure-03-robot-humanoid-reveal/ —— Adcock:"数十亿台机器人加入劳动力大军……也会进入太空"(2025-10)
- https://techcrunch.com/2025/02/04/figure-drops-openai-in-favor-of-in-house-models/ —— Adcock的垂直整合逻辑("我们无法外包AI")
- https://techcrunch.com/2026/01/30/physical-intelligence-stripe-veteran-lachy-grooms-latest-bet-is-building-silicon-valleys-buzziest-robot-brains/ —— Pi的论点:瓶颈是智能而非硬件;一个模型对应多种具身形态
- https://www.generalist.com/p/karol-hausman-physical-intelligence —— Hausman采访(2026-03-17):规模化动力学的叙事框架;"比起被描述,更难以被模拟"
- https://techcrunch.com/2026/04/16/physical-intelligence-a-hot-robotics-startup-says-its-new-robot-brain-can-figure-out-tasks-it-was-never-taught/ —— Levine:能力"以超线性的速度随数据增长而增长"(π0.7)
- https://www.chinanews.com.cn/cj/2026/03-29/10594954.shtml —— 王兴兴2026-03-29论坛:具身AI"GPT时刻"的定义(该媒体将其表述为陌生场景中"80-90%的任务"),约2-3年(中文一手报道)
- http://www.news.cn/energy/20251106/0ee9e5e4f67a482884b7ee537912895d/c.html —— 新华社2025-11-06:王兴兴"两个80%"的临界点定义,1-3年窗口期
- https://zhidx.com/p/496440.html —— 王兴兴世界机器人大会2025-08-09主题演讲:瓶颈在模型而非数据;VLA"傻瓜式";世界模型/视频生成路径;快则1-3年/慢则3-5年(中文)
- https://finance.ifeng.com/c/8lgDwnjxZgX —— 王兴兴采访:全球人形机器人出货量将保持每年翻倍增长;若出现AI突破,产量可能跃升至数十万台(甚至上百万台)/年(中文)
- https://www.21jingji.com/article/20250809/herald/fecc404938f03df050143f46e4922853.html —— 王兴兴:"机器人数据关注度太高;最大的问题在模型"(2025-08-09,中文)
- https://rodneybrooks.com/why-todays-humanoids-wont-learn-dexterity/ —— Brooks文章(2025-09-26):"纯属幻想",约17000个机械感受器,3米规则,15年后形态预测,"幻灭低谷"(一手来源;2036年这一表述**不在**此文中)
- https://rodneybrooks.com/predictions-scorecard-2026-january-01/ —— Brooks的日期化预测(一手来源):"灵巧操作能力相比人类手掌将持续表现糟糕,时间点将超过2036年";行走人形机器人"过于不安全,不适合与真人近距离共处"
- https://techcrunch.com/2025/09/26/famed-roboticist-says-humanoid-robot-bubble-is-doomed-to-burst/ —— Brooks:泡沫叙事框架;非人形形态将在约15年内胜出
- https://fortune.com/2026/02/25/mit-roboticist-irobot-cofounder-roomba-robot-vacuum-elon-musk-tesla-optimus-pure-fantasy-thinking/ —— Brooks针对Musk的愿景再次重申"纯属幻想"(2026-02-25)
- https://spectrum.ieee.org/robotics-experts-tesla-bot-optimus/gary-marcus —— Marcus谈Optimus:"多少有点令人失望",没有清晰的市场推进路径(2022)
- https://garymarcus.substack.com/p/sub-optimal —— Marcus专栏"Sub-Optimal":对Optimus的怀疑,遥操作方面的质疑(一手来源)
- https://decrypt.co/289058 —— Marcus对Decrypt表态(2024-10,针对Musk关于2040年机器人数量将超过人类的预测):"一贯有过度乐观预测AI的记录";约15亿辆汽车的类比
- https://news.berkeley.edu/2025/08/27/are-we-truly-on-the-verge-of-the-humanoid-robot-revolution/ —— Goldberg:10万年的数据鸿沟;2年、5年甚至10年内都不会出现管家机器人(2025-08)
