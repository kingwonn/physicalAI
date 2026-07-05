---
title: "公司深度分析:Skild AI"
slug: company-skild
updated: 2026-07-05
confidence: verified
lang: zh
source: ../wiki/company-skild.md
---
> Skild AI(总部匹兹堡,2023-05 由 CMU 教授 Deepak Pathak 与 Abhinav Gupta 创立)是估值最高的独立机器人大脑实验室:2026-01-14 宣布完成 14 亿美元 C 轮融资,投后估值超过 140 亿美元(SoftBank 领投;NVentures、Bezos Expeditions、Macquarie 参与)——约为其 2025 年年中估值的三倍,仅用了约 7 个月。其押注方向是"全身通用"(omni-bodied)的 **Skild Brain**:一个基础模型,宣称可以控制任何身体形态——四足机器人、人形机器人、桌面机械臂、移动操作平台——训练方式以仿真为先("一个拥有 10 万台不同机器人的宇宙"),辅以互联网人类视频数据,真实机器人数据仅用于训练后微调。与刻意选择"暂不追求营收"的 [Physical Intelligence](company-pi.md) 不同,Skild 走的是营收优先路线:据称 2025 年营收从 0 增长至约 3000 万美元(公司口径),来自安防/巡检、建筑、配送、数据中心、仓储与制造业部署,并在 2026 年积极向下游拓展——富士康 Blackwell 产线部署(2026-03)、与 ABB/Universal Robots 建立合作,以及收购 Zebra 旗下机器人业务(原 Fetch)AMR 部门(2026-04)。问题在于:技术层面近乎完全不透明——没有论文、没有开放权重、没有外部基准测试、客户身份不公开,且融资披露文件与第三方追踪数据对不上账。相关背景参见:[美国格局](landscape-usa.md)、[投资](investment.md)、[评估](evaluation.md)、[关键人物](key-people.md)。

## 公司概览

| 字段 | 状态(截至 2026-07) |
|---|---|
| 成立 | 2023-05;2024-07-09 走出隐身模式 |
| 总部/办公地点 | 匹兹堡,宾夕法尼亚州(CMU 圈子);旧金山湾区办公室(2025 年初);印度班加罗尔 |
| 创始人 | Deepak Pathak(首席执行官;CMU 教职人员,前 FAIR,伯克利博士——研究方向为好奇心驱动的强化学习与快速运动适应)与 Abhinav Gupta(总裁;自 2009 年起任 CMU RI 教授,前 FAIR 创始成员,引用量超 7.5 万次)——二人均在 CMU 兼任双重身份([学术实验室](academic-labs.md)) |
| 产品 | **Skild Brain**——"业界首个统一的机器人基础模型"(公司自述);闭源权重,无论文 |
| 理念 | "全身通用":一个大脑适配任意身体形态——四足、人形、机械臂、AMR——区别于按具体形态单独建模的路线 |
| 估值 | **投后估值超过 140 亿美元**(C 轮,2026-01-14)——所有机器人大脑实验室中最高;约为 PI 已公开的 56 亿美元估值的 2.5 倍 |
| 已披露融资总额 | 追踪到约 18.3 亿美元(A 轮 3 亿美元 + B 轮约 1–1.35 亿美元 + C 轮 14 亿美元;Crunchbase:超 18.3 亿美元);Pathak 本人(经 Bloomberg/TechCrunch)称"超过 20 亿美元"——两方记录对不上账(见质疑观点部分) |
| 主要投资方 | SoftBank(领投 B 轮 + C 轮)、Lightspeed、Coatue、Sequoia、Felicis、NVentures(NVIDIA)、Bezos Expeditions、Amazon(工业创新基金 + Alexa 基金)、Macquarie、1789 Capital、IQT(In-Q-Tel)、CMU;战略投资方包括 LG、Schneider Electric、CommonSpirit、Salesforce Ventures(三星参与了 2025 年那轮融资,约 1000 万美元——但未出现在公司自己公布的 C 轮投资方名单中) |
| 营收 | 2025 年内从 0 增长至约 3000 万美元(公司口径,无具名客户);"快速增长" |
| 部署领域 | 安防与设施巡检、建筑、最后一公里/点对点配送、数据中心、仓储、工厂装配(公司自述列表) |
| 已披露合作方/并购 | 富士康(NVIDIA Blackwell 产线,休斯顿)、ABB Robotics、Universal Robots(均于 2026 年 3 月 GTC 大会公布);2026-04-15 收购 Zebra Technologies 旗下机器人业务(原 Fetch Robotics) |
| 员工人数 | 未披露;24 人(2024-11)、25+ 人(2025-07)——即便按机器人大脑实验室的一贯标准衡量,人均估值也极为夸张 |

## 技术路线 Tech route & architecture

以下是目前公开的信息(没有论文、没有模型卡——以下全部来自公司博客、NVIDIA 案例研究与媒体报道):

- **分层双层策略架构**:(1)高层策略,发出低频率的操作/导航/任务意图指令;(2)低层策略,将其转化为高频率的关节角度与电机扭矩,以适配任意连接的身体形态。参数量、骨干网络结构、动作解码方案均未披露——相比之下,[PI](company-pi.md) 的流匹配(flow-matching)VLA 谱系是完全公开的([VLA 模型](vla-models.md))。
- **形态尺度上的仿真优先预训练**:"我们创造了一个拥有 10 万台不同机器人的宇宙,并训练我们的 AI 去控制它们所有"("We created a universe with 100,000 different robots and trained our AI to control them all");"经过'千年'的模拟时间(原文如此)"("[a]fter a millenia of simulated time"(sic))后,一个具有韧性的全身通用大脑涌现出来(公司博客,2025-09)。数千个机器人实例覆盖人形/四足/机械臂,形态随机化——其论点是,形态多样性会*迫使*模型进行上下文内适应,而非记忆单一身体的控制器。这是 Pathak 在 CMU 期间快速运动适应研究路线的直接延续([运动能力](locomotion.md))。
- **互联网人类视频作为预训练数据**——人类被视为"生物机器人",其互联网视频可作为示范数据(Pathak 的表述);真实机器人数据仅用于针对性的训练后微调与部署优化。Pathak 在达沃斯访谈(2026-01)中表明立场:整个行业在数据问题上方向错了;高度依赖遥操作的车队,乃至"特斯拉的自动驾驶数据集也无法帮助 Optimus 实现泛化"("Tesla's self-driving dataset won't help Optimus generalize")。
- **宣称的涌现式适应能力**(公司演示,针对训练集之外机器人的零样本测试):从失去肢体中恢复(约 7–8 秒的上下文内适应后即可有效行走)、断腿后恢复(约 2–3 秒内重新行走);检测到车轮卡死后切换为腿式步态;踩高跷行走(公司博客,2025-09);可承载高达自身体重 1.5 倍的负载,并在"数小时的数据采集内达到 60%–80% 的任务表现"(NVIDIA 案例研究数据——由供应商发布,未经独立验证)。
- **原生适配 NVIDIA 技术栈**:使用 Isaac Lab(强化学习)、Cosmos Transfer(文本提示驱动的环境增强)以及 NVIDIA 算力进行训练;是 Cosmos 联盟成员,并已采用 Newton 1.0 正式版(用于 GPU 机架装配的强化学习)——参见 [仿真](simulation.md)、[NVIDIA 公司](company-nvidia.md)。Witt(《纽约客》,2026-07)发现 Skild 的每一台机器人都运行在 NVIDIA 芯片上,并在 NVIDIA 仿真环境中训练。
- **与竞争对手路线的区别**:相比 PI——Skild 走仿真+视频优先路线而非遥操作优先路线,追求运动能力+操作能力的广度而非操作能力的深度,闭源而非开源,营收导向而非研究纯粹性导向。相比 NVIDIA GR00T——Skild 把"大脑"当作产品出售;NVIDIA 则免费提供模型以推动平台销售(同时 NVIDIA 又是 Skild 的投资方兼基础设施供应商)。相比 [Figure](company-figure.md)/[特斯拉](company-optimus.md)——(在收购 Fetch AMR 之前)自身没有机器人本体,以形态覆盖广度作为护城河。
- 公司在发布之初宣称其训练数据"至少是竞品模型的 1000 倍"("at least 1,000 times more data points than competing models")(2024 年,公司自述,无法验证——未披露数据集详情)。

## 押注方向/愿景

- **"全身通用"是产品本身,而非训练技巧**:"Skild Brain 能够控制其从未接受过训练的机器人,并针对形态或环境的极端变化实时适应"("The Skild Brain can control robots it has never trained on, adapting in real time to extreme changes in form or environments",Pathak,C 轮融资时表述)。"这个模型被迫去适应而不是去记忆——就像自然界中的智能一样"("The model is forced to adapt rather than memorize — much like intelligence in nature",Pathak)。Gupta 认为机器人必须"在复杂环境中动态运作,而无需预先编程的指令"("operate dynamically in complex environments, without requiring preprogrammed instructions")。
- **物理智能是通往通用人工智能(AGI)的道路**:Pathak 认为物理智能——而非语言——才是 AGI 真正的基础(达沃斯,2026-01);"通过经验学习,而非预编程,才是机器人学领域已经发生的那次质变"("Learning by experience, and not pre-programming, is the step change that has happened in robotics",NVIDIA 案例研究)。
- **反人形炒作,支持任意形态**:Pathak 拒绝在自己家中放置人形机器人——"人们利用外观来误导公众。如果你把机器人做得像人,人们就会期待它具备类人的能力。但技术远远达不到那个水平"("People are using appearance as a way to misguide the public. If you make a robot humanlike, you expect it to have humanlike capabilities. But technology is far behind that",《纽约客》,2026-07)。"全身通用"的押注实质上是对机器人形态因素的一种明确对冲([愿景](visions.md)、[人形机器人](humanoid-robots.md))。
- **与 PI 同属"一个大脑,任意身体"的信条,但奉行不同的教义**:PI 把商业化视为分心之事,并公开一切;Skild 则把部署本身当作数据引擎("从编程具体任务,转向构建能够持续学习和改进的系统,即使在部署过程中也是如此"——Pathak 谈富士康合作,"shifting from programming tasks to building systems that continuously learn and improve, even during deployment"),且不发表任何论文。来自 A 轮投资方的表述:"机器人领域的 GPT-3 时刻即将到来"("A GPT-3 moment is coming to the world of robotics",Stephanie Zhan,Sequoia)。
- 优先面向企业客户,消费级家庭场景留待以后(公司在 C 轮阐述的既定优先级)。

## 产品与部署情况(附有真实数据之处)

| 部署/产品 | 日期 | 宣称内容(以及可验证的部分) |
|---|---|---|
| Skild Brain 首次公开亮相 | 2025-07-29 | 演示对抗性条件下的爬楼梯、精细装配、洗碗动作;宣称"可安全地在人类身边使用"(训练模型施加低作用力——由 technical.ly 转述公司说法);没有基准测试,没有第三方评估 |
| 产生营收的部署:安防与设施巡检、建筑、配送、数据中心、仓储、工厂装配 | 2025 年内 | **2025 年"仅几个月内"营收从 0 增至约 3000 万美元**(公司口径);部署"包括安防与设施巡检、最后一公里及点对点配送、仓储、制造业、数据中心与建筑任务"(Crunchbase News,转述公司列表);无具名客户;technical.ly 另外报道称该公司在 2025 年"实现盈利"(单一信源,未经验证——若不加限定条件,与前沿模型的算力烧钱速度相比显得不太可信) |
| **富士康:NVIDIA Blackwell GPU 服务器装配产线,休斯顿** | 2026 年 3 月 16 日 GTC 大会宣布 | Skild Brain 部署在富士康的机器人产线上(双臂机械手,高精度装配);"经过数年测试后的首次公开大规模部署"(technical.ly 的表述);明确的"数据飞轮"叙事;机器人数量与产线范围均未披露 |
| ABB Robotics + Universal Robots 合作 | 2026 年 3 月 16 日 GTC 大会 | 将 Skild 的"共享智能层"嵌入广泛部署的工业机器人及协作机器人(cobot)机队——通过改造现有装机基础实现路径;商业条款未披露 |
| **收购:Zebra Technologies 旗下机器人自动化部门(原 Fetch Robotics)+ Symmetry Fulfillment 编排平台** | 2026-04-15 | 交易条款未披露;Zebra 表示获得了现金以及 Skild 的股权;Zebra 曾于 2021 年斥资 2.9 亿美元收购其未持有的 Fetch 剩余 95% 股权(该交易对 Fetch 的估值约为 3.05 亿美元)。这笔收购为 Skild 带来了 AMR 产品线、仓储编排平台以及真实客户基础;其宣传口径为:人形机器人负责拣选,四足机器人负责巡检,机械臂负责打包,AMR 负责运输——由一个大脑统一编排 |
| 演示用机器人本体 | 持续进行中 | 媒体演示中使用宇树科技(Unitree)四足/人形机器人以及商用机械臂(据《纽约客》及演示视频)(完整机队构成未经验证);匹兹堡街道/公园/防火梯导航、桌面清理、AirPod 盒插入等演示 |

- 独立第三方的实证依据稀少且好坏参半:Witt 在《纽约客》(2026-07 期)中的第一手演示报道显示——由 Skild 驱动的一台宇树机器人成功处理了直立摆放的水杯,但**在水杯被平放侧倒时手忙脚乱**——这与 [评估](evaluation.md) 页面记录的整个行业普遍存在的"扰动脆弱性"模式一致。
- 若属实,这个 3000 万美元的数字将是所有机器人大脑实验室中已披露营收最高的(PI:出于策略选择营收为 0;[宇树科技](company-unitree.md)作为硬件厂商,营收约为 2.35 亿美元,但两者不可直接类比)。目前没有任何备案文件、审计或客户名单支撑这一数字(截至 2026-07)。

## 商业模式与单位经济效益

- **模式**:授权"大脑",让其他厂商拥有"身体"——包括 API 访问/按使用量计费的授权模式、微调服务以及 OEM 集成授权(根据 Contrary Research 在其营收产生之前所做的业务拆解),此外还有由 Skild 提供全套部署的完整解决方案(其安防/巡检业务;以及并购完成后的 Fetch AMR + Symmetry 编排平台业务)。营收优先的立场是对 PI 路线的明确反向定位([公司:PI](company-pi.md)——Groom 拒绝谈论商业化;而 Pathak 在每次融资公告中都会披露营收数字)。
- **部署即数据**:每一笔付费部署都会反哺数据飞轮;客户实际上在为训练数据采集提供资金支持([数据](data.md)、[数据铸造厂](data-foundry.md))。
- **宣称的单位经济效益**(NVIDIA 案例研究,由供应商发布):由 Skild 驱动的商用机器人成本为"每套系统 4000–15000 美元,而传统自动化方案则需 25 万美元以上"("$4,000–$15,000 per system vs $250,000+ conventional automation"),总体拥有成本(TCO)降低约 10 倍——其宣传口径是:廉价的中国制造机器人本体 + 授权的"大脑"能够压制定制化系统集成商。目前没有经客户验证的公开 TCO 数据。
- **营收构成不透明**:约 3000 万美元的营收中,没有任何公开信息区分经常性的"大脑"授权收入与一次性的集成/试点项目收入;收购 Zebra 之后,AMR 硬件与编排软件收入将进一步模糊"纯粹大脑授权方"这一叙事(需持续关注)。
- **资本状况**:追踪到的累计融资总额约为 18.4 亿美元;仅 C 轮(14 亿美元)一轮的规模就超过了美国所有机器人大脑实验室竞争对手的融资总额(Figure 一类的硬件厂商除外)([投资](investment.md))。烧钱速度未披露。

## 相对同行的优势/劣势

**优势**
- **是唯一拥有营收叙事的机器人大脑实验室**(据称 2025 年约 3000 万美元)——化解了笼罩在 PI 头上的"大脑永远无法变现"的质疑;SoftBank/NVIDIA/Bezos 均加倍下注。
- **形态覆盖广度是真实的差异化优势**:运动能力 + 操作能力 + 导航能力横跨四足/人形/机械臂/AMR,根植于 Pathak/Gupta 数十年的仿真到现实(sim2real)与适应性研究积累——相比之下,PI 以机械臂/操作能力为中心;Figure/特斯拉则专注单一身体形态。
- **资本与战略关系网络**:是资金最充裕的纯"大脑"实验室;SoftBank(同时也在以 53.75 亿美元收购 ABB Robotics——为其提供了一条未来的专属分销渠道,参见 [愿景](visions.md))、NVIDIA(算力 + GR00T 生态席位)、Amazon(仓储渠道)、韩国财阀集群(LG、三星、Mirae、KIC——消费级机器人的邻近领域)、In-Q-Tel(安防/政府需求信号)、Schneider(工业分销)、CommonSpirit(医疗健康领域)。
- **既有装机基础策略**:ABB/UR 改造 + Fetch AMR 机队 + 富士康产线,直接从已存在的机器人身上变现,而不是坐等人形机器人技术成熟([悬而未决的问题](open-problems.md))。

**劣势/质疑观点**
- **不透明程度是全方位的**:没有论文、没有开放权重、没有模型卡、没有外部基准测试、没有具名客户、没有经审计的营收数据。每一个能力数字都可追溯到公司博客或其兼具投资方身份的供应商 NVIDIA。PI 会发表论文并开源;NVIDIA 会发表论文;而 Skild 只是要求外界信任它([评估](evaluation.md))。
- **融资记录对不上账**:媒体报道称有一轮约 5 亿美元的 B 轮融资,估值为 45–47 亿美元(2025-04/05);但追踪机构仅记录到约 1–1.35 亿美元已完成交割(Crunchbase 记录为 1.35 亿美元;The Robot Report 在 2025-07 报道的累计总额为"两轮共 4.35 亿美元",与之相互印证);technical.ly 找到的唯一一份 Skild Form D 备案文件显示金额仅约 100 万美元,通过一个特殊目的实体(SPV)完成(以"cgf2021-llc"名义提交;而 PitchBook 记录的总额当时约为 8.14 亿美元);已披露的各轮融资加总约为 18.3 亿美元,而 Pathak 本人却说"超过 20 亿美元"。这些都不构成欺诈证据——但对于一家估值 140 亿美元的公司来说,这种程度的混乱记录并不寻常(截至 2026-07)。
- **估值与实证之间存在巨大落差**:以公司自报的约 3000 万美元营收计算,140 亿美元以上的估值相当于约 470 倍的远期(且前景不明的)销售额,而这一估值是在 45 亿美元估值仅仅过去 7 个月后给出的——这种重新定价的速度正是 [投资](investment.md) 页面标记为"泡沫模式"的特征。
- **独立演示证据反而不利于其"鲁棒性"叙事**:《纽约客》记录的水杯失败案例,是目前唯一有记录的第三方第一手测试,而 Skild 在这次测试中失败了。
- **未来存在渠道冲突**:拥有 Fetch AMR 业务使 Skild 与其希望争取为被授权方的 AMR 制造商形成竞争关系;NVIDIA 同时身兼投资方、供应商与竞争对手(通过 GR00T)三重身份;SoftBank 旗下的 ABB 可能会对 Skild 给予优待——或直接将其吸纳合并。
- **同样面临人才储备单薄的问题**,这与其他所有竞争对手一致:整个押注集中在两位身兼双重身份的教授身上;CMU 的学术传承虽深厚,但在大规模部署的机队工程能力(相对于研究声望而言)尚未得到验证([关键人物](key-people.md))。
- 持平而论(steel-man 观点):营收优先的纪律性,恰好能产生仿真优先路线所欠缺的、杂乱但真实的现实世界数据;如果"全身通用"的说法哪怕只有一半属实,Skild 就拥有业内最广的形态覆盖范围,以及唯一能在融资寒冬中存活下来的机器人大脑实验室损益表。

## 制造与供应链定位(ODM/EMS 视角)

- **按设计不生产任何机器人本体**(2026 年之前):纯粹的软件/模型公司;其演示与部署机队均搭载第三方商用硬件——宇树科技级别的四足/人形机器人、商用协作机械臂(机队构成部分未经验证)。"大脑授权"这一理念,从结构上就决定了硬件合作方——OEM、ODM、EMS——将成为身体的供应商:Skild 的总体拥有成本(TCO)宣传口径明确依赖于 4000–15000 美元的商用机器人,也就是依赖于中国成本水平的硬件供应链([硬件](hardware.md)、[中国格局](landscape-china.md))。
- **富士康是其最引人瞩目的 EMS(电子制造服务)合作关系**(截至 2026-03):Skild 的"大脑"驱动着富士康位于休斯顿、用于装配 NVIDIA Blackwell GPU 机架的双臂装配机器人。这对 ODM 领域的读者具有双重意义:(a)EMS 产线本身就是客户——"AI 驱动的制造"正被出售给合同制造商;(b)富士康自身也有生产机器人的雄心,这使其有可能成为 Skild "大脑"的一条高产量身体渠道。基于 Newton 的 GPU 机架装配强化学习工作(据 NVIDIA,[仿真](simulation.md))表明,仿真训练出的单元正在被搬运到真实的 EMS 产线上。
- **以改造现有装机基础为先的市场进入策略**:与 ABB Robotics 及 Universal Robots 的合作,瞄准的是现有工业机械臂与协作机器人的既有装机基础——无需新增制造产能,收入来自软件层面的附加销售。SoftBank 待完成的对 ABB Robotics 的收购(预计于 2026 年年中至年末完成)有可能将其转变为在共同所有权之下的专属 OEM 渠道。
- **收购 Zebra 之后,Skild 首次拥有了硬件产品**:即原 Fetch 系列 AMR 产品组合,加上 Symmetry Fulfillment 编排平台。Fetch 的 AMR 产品历来是以适中的产量由合同制造商生产/在美国组装完成的(当前具体安排未经验证);目前没有公开信息表明 Skild 想要拥有自己的工厂——这笔收购看起来更像是在购买一支机队、一层编排软件以及仓储数据,而非一项制造业务。
- **算力供应链**:单一供应商模式,全部依赖 NVIDIA——不仅用于训练(Isaac Lab、Cosmos、DGX 级别的基础设施),据 Witt 的报道,连车载推理芯片也是如此。NVentures 的股权投资使双方利益一致,但也进一步集中了这种依赖关系([NVIDIA](company-nvidia.md))。
- **ODM 厂商应从中得到的启示**(截至 2026-07):Skild 是"物理 AI"(Physical AI)领域中最清晰的"Android 式授权方"类比对象——它需要在每一种形态因素上寻找身体合作伙伴,拥有为集成合作提供资金的资本实力,并且(除了在收购 Fetch 之后进入的仓储 AMR 领域)不与硬件制造商构成竞争。对身体合作伙伴而言仍待解决的问题包括:没有公开发布的集成 SDK/API 规范,没有认证项目,也没有披露具体的按机器人计费的授权经济模式。

## 来源

- https://www.skild.ai/blogs/series-c —— C 轮融资官方公告原始来源(2026-01-14):14 亿美元、超过 140 亿美元估值、完整投资方名单(不含三星)、3000 万美元营收说法、部署领域
- https://techcrunch.com/2026/01/14/robotic-software-maker-skild-ai-hits-14b-valuation/ —— C 轮融资的佐证报道;Pathak 通过 Bloomberg 称"已融资超过 20 亿美元";此前 45 亿美元估值
- https://www.bloomberg.com/news/articles/2026-01-14/robotics-startup-skild-valued-above-14-billion-after-softbank-led-funding-round —— SoftBank 领投轮次,估值超过 140 亿美元
- https://www.therobotreport.com/skild-ai-raises-1-4b-building-omni-bodied-robot-skild-brain/ —— 更完整的投资方名单(包括 IQT、KIC、Mirae)、办公地点(匹兹堡/旧金山/班加罗尔)、Pathak/Gupta 相关引述、部署领域
- https://news.crunchbase.com/venture/robotics-startup-skild-ai-triples-valuation/ —— 约 7 个月内估值增至三倍;累计融资总额超过 18.3 亿美元;B 轮记录为 1.35 亿美元/45 亿美元估值;部署环境列表
- https://www.businesswire.com/news/home/20240709306400/en/Skild-AI-Raises-%24300M-Series-A-To-Build-A-Scalable-AI-Foundation-Model-For-Robotics —— A 轮融资(2024-07-09):3 亿美元,估值 15 亿美元;Lightspeed/Coatue/SoftBank/Bezos 领投;Amazon、CMU、Sequoia 参投
- https://techcrunch.com/2025/12/08/softbank-and-nvidia-reportedly-in-talks-to-fund-skildai-at-14b-nearly-tripling-its-value/ —— C 轮前的洽谈情况;"5 月份估值为 47 亿美元"、彼时所融的 5 亿美元;LG Technology Ventures/三星/NVIDIA 参与 B 轮
- https://finance.yahoo.com/news/nvidia-samsung-back-4-5b-203049332.html —— NVIDIA 投入约 2500 万美元 + 三星投入约 1000 万美元,进入 2025 年那轮约 45 亿美元估值的融资
- https://www.therobotreport.com/skild-ai-is-giving-robots-a-brain/ —— Skild Brain 首次亮相报道(2025-07-30);"两轮共 4.35 亿美元"的累计总额说法;25+ 名员工;Pathak 关于爬楼梯/装配的引述
- https://technical.ly/entrepreneurship/skild-brain-unveiled-ai-human-robot/ —— SEC Form D 备案调查:仅找到约 100 万美元的 SPV 备案,而 PitchBook 记录的总额为 8.14 亿美元;招聘足迹情况
- https://technical.ly/entrepreneurship/skild-ai-1-4-billion-raise/ —— "已实现盈利,2025 年营收约 3000 万美元"的表述来源(单一信源);Form D 备案缺失的提示
- https://www.skild.ai/blogs/omni-bodied —— "全身通用"理念的原始出处:10 万台机器人的仿真宇宙、失去肢体/切换步态/踩高跷的零样本能力宣称
- https://www.skild.ai/blogs/building-the-general-purpose-robotic-brain —— 数据金字塔(仿真 + 互联网视频预训练,真实世界训练后微调);高层/低层双层策略架构
- https://www.nvidia.com/en-us/case-studies/skild-ai/ —— NVIDIA 案例研究:Isaac Lab + Cosmos Transfer 的使用情况、"数天内积累千年经验"的说法、数小时内达到 60–80% 表现、4000–15000 美元对比 25 万美元以上的 TCO 说法、Pathak 引述
- https://nvidianews.nvidia.com/news/nvidia-and-global-robotics-leaders-take-physical-ai-to-the-real-world —— 2026 年 3 月 16 日 GTC 大会:Skild 与 ABB Robotics、Universal Robots、富士康 Blackwell 产线的合作
- https://technical.ly/entrepreneurship/pittsburgh-skild-ai-nvidia-foxconn-robotics-deployment/ —— 富士康休斯顿部署细节:"首次公开大规模部署"、数据飞轮叙事、Pathak 引述(2026-03-18)
- https://www.skild.ai/blogs/skild-zebra —— 收购 Zebra 机器人业务的官方公告原始来源(2026-04-15):Fetch 的产品渊源、Symmetry Fulfillment、端到端仓储解决方案宣传
- https://www.therobotreport.com/skild-acquires-fetch-robotics-assets-from-zebra-automation/ —— Zebra 收购 Fetch 的价格(2021 年);Skild 对 Fetch 既有装机基础的规划
- https://www.dcvelocity.com/material-handling/robotics/zebra-sells-off-its-fetch-amr-division —— 交易对价:"除获得现金对价外,还获得了 Skild AI 的股权"("in addition to receiving cash consideration, it also took on an equity stake in Skild AI",Zebra 声明);印证 Zebra 新闻稿内容
- https://www.zebra.com/us/en/about-zebra/newsroom/press-releases/2021/zebra-technologies-to-acquire-fetch-robotics.html —— Zebra 于 2021 年收购 Fetch 的交易:以现金 2.9 亿美元收购剩余 95% 股权,隐含估值约 3.05 亿美元
- https://research.contrary.com/company/skild-ai —— 创立故事、创始人背景、A 轮融资细节、2024 年 11 月时的 24 人团队规模、预计的授权/API 业务模式、"数据量为竞品 1000 倍"的说法
- https://sources.news/p/skild-ai-ceo-robotics-brain-davos —— Pathak 达沃斯访谈(2026-01):对数据策略的批评、对特斯拉/Optimus 的质疑观点、"物理智能即通往 AGI 之路"的论述
- https://www.newyorker.com/magazine/2026/07/06/are-humanoid-robots-ready-to-be-deployed —— Witt 第一手报道:Skild 驱动的宇树机器人水杯失败案例;Pathak 的反人形机器人相关引述;Skild 内部 NVIDIA 芯片的普遍使用情况(付费墙内容;文章的存在、标题与核心论点已通过二手引用来源印证,但截至 2026-07-05,引语原文措辞尚无法通过公开检索独立复核)
- https://lsvp.com/stories/skild-is-bringing-generative-ai-to-the-real-world/ —— Lightspeed 投资备忘录中的相关表述(A 轮领投方)
</content>
