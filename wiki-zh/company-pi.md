---
title: "公司深度剖析:Physical Intelligence"
slug: company-pi
updated: 2026-07-04
confidence: verified
lang: zh
source: ../wiki/company-pi.md
---
> Physical Intelligence("PI",标志为 π;总部在旧金山)是"机器人大脑、不造机器人本体"路线的旗舰代表:这是一家约 80 人的实验室,由 Google 机器人团队出走的核心成员(Karol Hausman、Sergey Levine、Chelsea Finn、Brian Ichter、Quan Vuong)以及 Stripe 老兵、投资人 Lachy Groom 于 2024-03 共同创立,致力于打造与本体无关(embodiment-agnostic)的基础模型——π0(2024-10,flow matching)→ π0.5(2025-04,开放世界泛化)→ π*0.6(2025-11,基于经验的 RECAP 强化学习)→ π0.7(2026-04,带世界模型视觉子目标的可引导通才模型)。PI 已开源 π0/π0.5(openpi,GitHub 星标 1.26 万),但前沿模型保持闭源;截至目前已累计融资约 10.7 亿美元(2025-11 由 CapitalG 领投,6 亿美元、估值 56 亿美元);据报道的一轮约 10 亿美元、估值超 110 亿美元的融资截至 2026-07-04 尚未确认完成。公司刻意选择零营收路线——Groom 拒绝向投资人给出商业化的答案——这使 PI 成为前沿 Physical AI 实验室中最"纯粹的研究押注"。相关背景参见:[VLA 模型](vla-models.md)、[美国格局](landscape-usa.md)、[投资](investment.md)、[关键人物](key-people.md)。

## 创立与理念

- **2024-03 宣布成立**(种子轮日期为 2024-03-12;部分资料将注册成立时间追溯到 2023 年底)。Lachy Groom——Stripe 早期员工,Figma/Notion/Ramp 的天使投资人——"花了五年时间寻找 Stripe 之后要创办的公司",他先通过学术工作找到 Levine 和 Finn,再找到 Hausman;"那种走出会议室就觉得——就是它了的感觉"。
- **联合创始人**(不同来源列出的名单略有差异):**Karol Hausman**(CEO;曾主导 Google Brain 的机器人操作登月计划——SayCan/RT 时代)、**Sergey Levine**(加州大学伯克利分校 RAIL 实验室;深度强化学习经典之作的作者——SAC、离线强化学习、Open X-Embodiment)、**Chelsea Finn**(斯坦福 IRIS 实验室;MAML、ALOHA/Mobile ALOHA、DROID)、**Brian Ichter**(前 Google Brain)、**Lachy Groom**(负责运营/融资/市场拓展)、**Quan Vuong**(前 Google DeepMind)、**Adnan Esmail**(前 Anduril 工程高级副总裁,曾任职特斯拉),另有部分资料提及 **Jasmine Hsu**(未证实——她不在大多数名单中,包括 2026-01 TechCrunch 的专访)。Levine 和 Finn 仍保留各自的教职(参见[关键人物](key-people.md))。
- **核心理念**:打造一个通才型"机器人大脑"——Levine 的说法是"把它想象成 ChatGPT,只不过是给机器人用的"——在大量廉价、异构的机器人本体上训练,使智能能够迁移到任何新平台。Vuong:"把自主能力移植到一个新机器人平台上的边际成本……会低得多。" PI **不自研任何硬件**,将机器人本体视为商品(其实验室机械臂成本约 3,500 美元;Levine 估计若自研生产,物料成本可低于 1,000 美元)。
- 明确反人形机器人炒作的定位:不是打造一台昂贵的人形机器人,而是在单臂、双臂系统和移动操作平台上广泛训练——押注跨本体数据的广度胜过垂直整合(与之相对的押注方是 [Figure](company-figure.md))。

## 团队与人才密度

- **截至 2026-01 约有 80 名员工**(TechCrunch 专访)——按估值折算的人均员工数大约只有典型硬件同行的十分之一;Groom 希望"尽可能缓慢地"扩张团队;大部分支出用于算力,而非人力成本。
- 可以说是全行业机器人学习作者密度最高的团队之一:π0.7 论文列出了约 90 位作者,包括 Danny Driess;创始团队共同撰写了该领域大量的经典成果(RT-1/RT-2、SayCan、Open X-Embodiment、ALOHA、DROID)。
- Groom 声称,原定 5 到 10 年的研究路线图在约 18 个月内就已完成(公司口径,未证实)。
- 总部位于旧金山,配有一个用于数据采集与评估的办公室内"测试厨房"(含意式咖啡机、洗衣设备)。

## 融资历程(截至 2026-07)

| 轮次 | 日期 | 金额 | 投后估值 | 领投方/主要投资人 |
|---|---|---|---|---|
| 种子轮 | 2024-03 | 7000 万美元 | 约 4 亿美元(据报道) | Thrive Capital;Khosla、Lux、Sequoia、OpenAI |
| A 轮 | 2024-11 | 4 亿美元 | 24 亿美元 | Jeff Bezos、OpenAI、Thrive、Lux、Bond |
| B 轮 | 2025-11 | 6 亿美元 | 56 亿美元 | CapitalG(Alphabet 旗下);Bezos、Thrive、Lux、Index、Emergence、T. Rowe Price |
| 据报道的下一轮 | 首次报道于 2026-03-27 | 约 10 亿美元 | 超 110 亿美元 | Founders Fund"计划参与",Lightspeed 正在洽谈(彭博社) |

- **观察要点——截至 2026-07-04 核实:估值超 110 亿美元、约 10 亿美元的这一轮融资尚未宣布完成。** 目前所有相关报道仍全部溯源自彭博社 2026-03-27 关于"洽谈中"的报道,此后 PI 或投资人均未给出一手确认。若该轮完成,估值将在约 4 个月内翻一倍,累计融资总额将达到约 21 亿美元。在正式宣布之前,110 亿美元这一估值应视为(未证实)。
- 已确认的累计融资总额约为 **10.7 亿美元**,共三轮。值得注意投资人构成:OpenAI 在种子轮和 A 轮均有投资;Alphabet 旗下的成长期基金领投了 B 轮——两大 AI 巨头都持有这家领先的独立机器人大脑实验室的股份(行业背景参见[投资](investment.md)中关于估值飙升速度的担忧)。
- 上述任何一轮估值背后都没有披露的营收支撑(参见下文的质疑观点)。

## 模型谱系:π0 → π0.7

完整的架构细节及跨实验室对比见[VLA 模型](vla-models.md);此表补充公司发展轨迹的背景信息。

| 模型 | 日期 | 核心进展 | 权重 |
|---|---|---|---|
| π0 | 2024-10 | 首个通才策略:PaliGemma-3B 视觉-语言模型 + 3 亿参数动作专家模块,flow matching,50 Hz 分块;约 1 万小时跨 7-8 种本体的遥操作(teleoperation)数据 | 2025-02 开源(Apache-2.0) |
| π0-FAST | 2025-01 | FAST 动作分词器(DCT + BPE):相较扩散/flow 解码,训练成本降低约 5 倍(公司口径) | 开源 |
| π0.5 | 2025-04-22 | 开放世界泛化——能清扫从未见过的房屋;分层的"先子任务、后动作"推理;约 100 个环境的规模化研究 | 2025-09 开源 |
| π*0.6 | 2025-11-17 | RECAP("基于优势条件策略的经验与纠错强化学习"):演示 → 遥操作纠正 → 基于自主经验的优势条件强化学习;50 亿参数视觉-语言模型 + 动作专家模块;意式咖啡/洗衣/装箱任务成功率超 90%,吞吐量约提升 2 倍 | 闭源 |
| π0.7 | 2026-04-16 | "具备涌现能力的可引导通才模型"(arXiv:2604.15483):单一权重检查点即可媲美经强化学习专项调优的 π*0.6 专家模型(吞吐比 0.9–2.0 倍);通过语言指导、速度/质量元数据、控制模态标签,以及**测试时由轻量级世界模型(world model)生成的视觉子目标**进行提示引导 | 闭源 |

- 这一谱系讲述了一条清晰的战略路线:2024 年验证架构(flow-matching VLA);2025 年先验证泛化能力(π0.5),再验证可靠性(π*0.6 的强化学习);2026 年验证一个模型能否可引导地"全都会"(π0.7)。前沿模型恰好在具备商业价值的那一刻转为闭源。
- π0.7 的世界模型子目标机制("展示当前子步骤结束时应呈现的画面……由世界模型在测试时生成")使 PI 加入了 2026 年 VLA 与世界模型融合的阵营,与 NVIDIA 的 DreamZero 并列——参见[世界模型](world-models.md)。
- Levine 对 π0.7 的规模化论断:一旦模型跨过"技能重组"的门槛,"能力的提升幅度会超过与数据量的线性关系"——这是该领域迄今为止最清晰的"GPT-3 时刻"式表述(公司相关人士的说法;PI 自己在论文中用"早期迹象"这样的措辞留有余地)。
- 各版本发布之间的配套研究节奏包括:FAST+ 通用分词器(100 万条轨迹)、知识隔离训练(随 π0.5 发布)、实时动作分块、Hi Robot 分层指令跟随(2025 年)以及支持 10 分钟以上任务的多尺度具身记忆(2026-03)(后两项来自公司研究页面,细节未证实)。

## 开源:openpi 与生态影响

- **openpi**(github.com/Physical-Intelligence/openpi,Apache-2.0 协议,**截至 2026-07 星标 1.26 万**):发布了 π0 与 π0-FAST 基础权重(2025-02)以及 π0.5(2025-09,支持 PyTorch),还有若干微调版本——π0-DROID / π0-FAST-DROID(适配 Franka)、π0-ALOHA(叠毛巾、收纳保鲜盒、笔帽盖合)、π0.5-LIBERO、π0.5-DROID。文档支持 DROID、ALOHA、LIBERO、UR5 平台。
- Hugging Face 的 **LeRobot** 将 π0(2025 年)与 π0.5 纳入一级策略模型——使 π 系列模型成为学术界和爱好者默认的"正经"开源 VLA 选择,与 SmolVLA、GR00T 并列(参见[数据](data.md)、[VLA 模型](vla-models.md))。
- 生态影响:π0 的 flow-matching 动作专家设计已成为 2025-26 年新 VLA 模型事实上的模板(SmolVLA 以及许多中国模型都沿用了这一设计),openpi 的权重检查点也成为 VLA 论文中的标准基线(例如 GM-100、LingBot-VLA 的对比研究)。
- 开源/闭源的界线是战略性的:**截至 2026-07,π*0.6 和 π0.7 仍然闭源**(openpi issue #789 中有开源诉求的跟踪记录)。PI 开源约 12 到 18 个月前的旧模型以培育生态系统,同时对具备部署级能力的新模型保密——这与[VLA 模型](vla-models.md)中描述的美国前沿实验室的普遍模式相呼应。

## 演示及其证明的内容

| 演示 | 模型/日期 | 证明了什么(以及没能证明什么) |
|---|---|---|
| 叠衣服、清理餐桌、装箱 | π0,2024-10 | 对可变形物体(deformables)的多分钟灵巧操作——历来是机器人学的一大难题——对 flow-matching VLA 而言是可行的。但并未证明超出训练场景的泛化能力。 |
| 在从未见过的房屋中清扫厨房/卧室 | π0.5,2025-04 | 开放世界泛化能力;规模化研究显示约 100 个训练环境即可接近域内性能。但成功率远未达到产品级水准。 |
| **18 小时意式咖啡马拉松**(早 5:30 至晚 11:30 连续运行)、在新家中处理 50 件从未见过的洗衣物品、组装并贴标 59 个工厂包裹 | π*0.6,2025-11 | 商业上具决定性的维度:马拉松时长下的可靠性与吞吐量,而非一次性成功率。基于自主经验的强化学习(RECAP)使吞吐量大约翻倍,失败率降低约 2 倍(公司口径)。 |
| 空气炸锅烤红薯:仅凭 2 段零散训练片段加网络知识,即可操作从未见过的家电;通过逐步语言指导完成新任务;在未训练过的双臂 UR5e 上零样本叠衣 | π0.7,2026-04 | 组合式泛化能力与本体无关性——这正是核心理念所主张的。但所有基准测试都是与 PI *自身*此前的模型对比,目前不存在标准化的外部基准(公司自己也承认这一点)。 |
| 现场媒体演示的失败案例:机器人能顺利叠好精心准备的 T 恤,但对来宾提供的衬衫、马甲、毛衣束手无策 | 《华盛顿邮报》探访,2026-06-08 发布 | 精心准备的演示分布与真实世界之间的差距依然存在;PI 自己的招牌任务对"对抗性"衣物并不稳健。 |

- 值得注意的模式:PI 的演示类型经历了从"能不能做到 X"(2024 年)到"能不能全天候做 X"(2025 年)再到"能不能做从未被教过的 X"(2026 年)的转变——恰好对应每一轮融资需要说服投资人相信的内容。
- 全文数据均为公司自行披露,没有第三方审计(参见[评测](evaluation.md))。

## 本体与合作伙伴

- **训练用本体**(π0 论文:8 种不同机器人):单臂及双臂 UR5e、Franka、双臂 Trossen(ALOHA 类)、双臂 ARX、双臂 AgileX,以及移动操作平台——刻意选用廉价、以商品化机械臂为主而非人形机器人。
- **评测用本体**(π0.7):移动操作平台、配备 Robotiq 夹爪的双臂 UR5e、Franka(通过 DROID)。微调后的权重检查点面向 DROID/Franka 和 ALOHA 平台。
- **截至 2026-07 尚未宣布任何人形机器人合作**——考虑到公司的核心理念,这一点颇为显眼;PI 的模型运行在机械臂和移动底盘上,而人形机器人厂商(Figure、Tesla、1X)都自研内部大脑(是否存在私下的人形机器人评测尚不确定)。
- **数据合作伙伴**:是 Scale AI"Physical AI 数据引擎"的具名客户(已记录超 10 万小时的生产数据;参见[数据](data.md))。
- **测试合作伙伴**(据 2026-01 TechCrunch 报道):物流、生鲜零售、巧克力制造等领域的未具名企业——这些试点尚未产生营收。此前 π*0.6 的相关材料中出现的工厂装箱和咖啡吧场景与此类试点相符。
- 投资人形成的战略网络:OpenAI(种子轮+A 轮)、Alphabet/CapitalG(B 轮领投)、Bezos(A 轮+B 轮)——除 NVIDIA 之外,PI 几乎与所有主要 AI 资本阵营都有关联(参见[组织机构](organizations.md))。

## 商业模式:刻意留白

- PI **主动选择零营收**(截至 2026-01,据 TechCrunch 专访:未披露营收、产品、定价或付费客户;合作被定位为测试而非商业化部署):Groom 说——"我不会向投资人给出商业化方面的答案。人们能容忍这一点,其实挺奇怪的。"绝大部分支出用于算力;Groom:"我们能投入使用的资金其实没有上限。"
- 隐含的终局设想:将"大脑"授权给碎片化的机器人硬件世界——即成为"Android 层"的定位——通过模型授权/API 而非出售机器人本体来实现。第三方分析勾勒出订阅制/按设备授权分级的可能路径,但**截至 2026-07,PI 尚未公布任何定价、产品或具名付费客户**。
- 行业内反差最鲜明的对比:**Skild AI**(另一家美国机器人大脑实验室,估值超 140 亿美元)声称在安防/仓储/制造业部署中实现约 3000 万美元的 2025 年营收(据 TechCrunch 报道;公司口径);而 PI 在估值 56 亿美元(或据报道的 110 亿美元)之下营收为零,并将此视为一种"自律"。[Figure](company-figure.md) 则走硬件+大脑垂直整合变现的路线。三种互不相容的路线,却都获得了数十亿美元级别的估值——参见[美国格局](landscape-usa.md)。
- 乐观解读:避免过早产品化,保住了专注度,才使 π0.5→π0.7 得以在 24 个月内接连问世,而 openpi 也培育了可能使行业统一采用 π 接口的生态系统。悲观解读见下文。

## 质疑观点

- **零营收下的高估值**:已完成的 56 亿美元估值 / 据报道的 110 亿美元估值,对应的披露营收为零;若该轮融资完成,相当于约 4 个月内估值翻倍——这种速度让人联想到 2021 年式的泡沫化融资节奏(参见[投资](investment.md)中的"泡沫观察")。
- **自我参照式评测**:每一项头条级别的成果(18 小时意式咖啡马拉松、成功率超 90%、媲美专项模型)都是与 PI 自身此前的模型、在 PI 自选的任务上进行对比;公司自己也承认目前不存在标准化的机器人基准测试。截至 2026-07,π*0.6/π0.7 都没有 RoboArena/GM-100 那样的第三方数据。
- **演示的脆弱性**:《华盛顿邮报》2026-06 的现场测试——在来宾提供的马甲和毛衣上失败——表明这一招牌任务一旦稍微超出精心准备的分布范围就会失效;Rodney Brooks 更广泛的批评("靠视频训练出的灵巧操作纯属幻想")在此完全适用。
- **本体无关不等于本体已被验证**:π 系列模型运行在实验室和试点场景中的廉价机械臂上;尚未宣布任何人形机器人合作、任何机队部署、任何 OEM 设计中标。这种授权路线尚未在硬件厂商强烈的"自研大脑"动机面前得到检验(Figure 正是因为这一点解约了 OpenAI)。
- **开源的慷慨是有限度的**:真正具备商业价值的模型(π*0.6、π0.7)是闭源的;成就了 PI 声誉的开放性比前沿进展滞后约一年,在商业化压力下这一差距还可能进一步拉大。
- **关键人物集中度**:这场押注与少数身兼多职的学者(Levine、Finn)以及 Hausman 密不可分;竞争对手(Skild、NVIDIA GEAR、DeepMind)都在从同一小片人才池中挖人(参见[关键人物](key-people.md))。
- 持平之论:PI 的论文异常详尽且可复现(openpi 让外部人士得以验证其架构层面的主张),其 2024→2026 年的能力提升曲线是真实的、并可通过开源权重检查点从外部观察到,而且它一再率先做出后来被业界效仿的技术(flow-matching 动作专家模块、FAST、基于经验的强化学习、可引导性)。

## 来源

- https://www.pi.website/ — 公司官网:模型时间线(π0 → π0.7)、投资人名单、研究文章
- https://x.com/svlevine/status/1767636367717310708 — Levine 的创立宣布(2024-03)
- https://www.crunchbase.com/funding_round/physical-intelligence-834b-seed--0936ae55 — 种子轮日期为 2024-03-12
- https://www.maginative.com/article/physical-intelligence-raises-70m-to-build-ai-powered-robots-for-any-application/ — 种子轮 7000 万美元,估值约 4 亿美元,投资人包括 Thrive/Khosla/Lux/Sequoia/OpenAI
- https://www.cnbc.com/2024/11/04/jeff-bezos-and-openai-invest-in-robot-startup-physical-intelligence.html — A 轮 4 亿美元,估值 24 亿美元(2024-11),投资人 Bezos/OpenAI/Thrive/Lux/Bond
- https://www.bloomberg.com/news/articles/2025-11-20/robotics-startup-physical-intelligence-valued-at-5-6-billion-in-new-funding — 6 亿美元,估值 56 亿美元,CapitalG 领投(2025-11)
- https://www.therobotreport.com/physical-intelligence-raises-600m-advance-robot-foundation-models/ — B 轮融资的佐证报道及投资人名单
- https://www.bloomberg.com/news/articles/2026-03-27/ex-deepmind-staffers-robotics-startup-in-talks-for-11-billion-valuation — 约 10 亿美元、估值超 110 亿美元"洽谈中"(2026-03-27);Founders Fund、Lightspeed
- https://techcrunch.com/2026/03/27/physical-intelligence-is-reportedly-in-talks-to-raise-1-billion-again/ — 佐证报道:截至报道时,110 亿美元估值一轮仍处于未完成的洽谈阶段
- https://techcrunch.com/2026/01/30/physical-intelligence-stripe-veteran-lachy-grooms-latest-bet-is-building-silicon-valleys-buzziest-robot-brains/ — 内部专访:约 80 名员工、Groom 拒绝商业化表态的立场、3,500 美元机械臂、测试合作伙伴(物流/生鲜/巧克力)、包括 Quan Vuong 在内的联合创始人名单、与 Skild 的对比
- https://www.pi.website/blog/pi0 — π0 发布公告(2024-10-31):架构(30 亿参数视觉-语言模型、flow matching、50 Hz)、8 种不同机器人、叠衣/清桌/装箱演示(文章未提及具体小时数)
- https://www.pi.website/research/fast — FAST 分词器,约 5 倍训练成本降低的说法,FAST+ 通用分词器
- https://www.pi.website/blog/pi05 — π0.5(2025-04-22):清扫从未见过的房屋、约 100 个环境的规模化研究、训练数据组合
- https://www.pi.website/blog/pistar06 — π*0.6 与 RECAP(2025-11-17):意式咖啡任务早 5:30 至晚 11:30(共 18 小时)、三项任务成功率均超 90%、吞吐量约提升 2 倍
- https://arxiv.org/abs/2511.14759 — π*0.6 论文("一个从经验中学习的 VLA")
- https://website.pi-asset.com/pi06star/PI06_model_card.pdf — π0.6 模型卡:50 亿参数视觉-语言模型 + 动作专家模块
- https://www.pi.website/blog/pi07 — π0.7(2026-04-16):可引导性输入、世界模型生成的视觉子目标、0.9-2.0 倍的专家模型吞吐比、UR5e/Robotiq 及移动操作平台评测
- https://arxiv.org/abs/2604.15483 — π0.7 论文("一个具备涌现能力的可引导通才机器人基础模型"),约 90 位作者
- https://techcrunch.com/2026/04/16/physical-intelligence-a-hot-robotics-startup-says-its-new-robot-brain-can-figure-out-tasks-it-was-never-taught/ — π0.7 相关报道:Levine 的"超线性"表述、空气炸锅示例、承认标准化基准尚不存在
- https://www.humanoidsdaily.com/news/physical-intelligence-unveils-0-7-the-rise-of-compositional-generalization-in-robotics — π0.7 的独立报道:组合式泛化能力、两段式空气炸锅细节
- https://github.com/Physical-Intelligence/openpi — openpi 代码仓库:1.26 万星标,Apache-2.0 协议,权重检查点列表(π0/π0-FAST/π0.5 及 DROID/ALOHA/LIBERO 变体)、2025-09 支持 PyTorch;不含 π0.6/π0.7
- https://www.therobotreport.com/physical-intelligence-open-sources-pi0-robotics-foundation-model/ — π0 开源(2025-02)
- https://huggingface.co/blog/pi0 — π0/π0-FAST 集成进 Hugging Face LeRobot;佐证超 1 万小时预训练数据这一数字
- https://huggingface.co/docs/lerobot/pi05 — π0.5 作为 LeRobot 策略模型(生态采用情况)
- https://www.washingtonpost.com/opinions/interactive/2026/06/08/this-ai-robot-promises-fold-your-laundry-would-you-buy-it/ — 现场演示:精心准备的 T 恤能叠好,来宾提供的衣物则失败;"贩卖一个承诺"的表述(质疑观点的重要来源)
- https://arxiv.org/html/2410.24164v1 — π0 论文:8 种不同机器人(UR5e、Franka、Trossen、ARX、AgileX;单臂/双臂/移动配置)
