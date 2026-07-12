---
title: 公司档案:Generalist AI, Inc. (Company Dossier: Generalist)
slug: case-generalist
updated: 2026-07-12
confidence: verified
lang: zh
source: ../wiki/case-generalist.md
---
> **说人话:** 这家公司叫 Generalist AI,是美国加州一群前 Google DeepMind 顶级机器人研究员开的,目标是造出"什么活都能干"的机器人大脑。它现在不卖任何东西给普通客户——它自己造了一种戴在手腕上的采数据爪子,雇人在几千个家庭和仓库里干活攒数据,再用这些数据训练自己的 VLA 模型(看图听指令直接输出动作的机器人大脑模型),模型只对少数"早期合作伙伴"开放。跟我们的关系:它是全世界把"手持爪采数据→喂大模型"这条路砸钱砸得最狠的公司(融资超 5 亿美元),它的成功印证了我们数据引擎的核心公理,但它对设备精度、误差、同步方式**零披露**,恰好反向证明了我们"计量院"车道(卖带误差报告的尺子)是空着的。
> **身份解析:** 法律名 Generalist AI, Inc.(官网页脚 "© 2026 Generalist AI, Inc." 直接核验),品牌名 Generalist,官网 generalistai.com,GitHub/HuggingFace/X/LinkedIn 账号全部核对一致,无重名混淆(不像觅蜂/Maniformer 那次)——**身份确认度:高,主源核验**。总部加州 San Mateo(媒体口径,SiliconANGLE 等),招聘页岗位标注 SFO(旧金山湾区)与波士顿两地。

## 1. 愿景与论纲 (vision & thesis)

Generalist 的论纲可以用一句白话概括:**机器人智能不能光靠从互联网下载数据,必须靠真实世界里的物理交互数据大量喂出来,而且喂得越多、模型越大,能力就按可预测的规律涨**。逐字引语:

- CEO Pete Florence(2025-03 GTC 场合,TechCrunch 直引):*"We are dead set on making robots that can do absolutely anything"*(我们铁了心要造出什么都能干的机器人);*"imagine a world where the marginal cost of physical labor is driven to zero"*(想象一个体力劳动边际成本被压到零的世界)。**勘误:此前误标为 X 创办帖出处,实为 TechCrunch 2025-03-19 报道直引。**(次源直引,已逐字核验)
- 创办宣言帖(X,2025-06-17):开头 *"Last Spring I took off from Google DeepMind... It's felt to me for a couple years, since we started bringing multimodal LLMs into robotics, that a subset of the..."*(去年春天我从 Google DeepMind 离职……几年来我一直有种感觉,自从我们开始把多模态大模型引入机器人领域,其中一部分……;经搜索快照逐字证实到此);后文大意为"造真正通用机器人智能的一部分要素正在就位",需要在数据、模型、硬件的交叉点上重新聚焦,光靠从互联网下载数据造不出物理智能——**原帖在登录墙后(2026-07-12 复核返回 402),后半段引语为转述,逐字 (unverified)**。
- GEN-1 博客(2026-04-02):使命是 **"physical AGI"**(物理世界的通用人工智能)—— *"building towards physical AGI and making it useful to everyone."*(致力于构建物理 AGI,并让所有人都能用上它。)他们对智能的定义:*"the ability to reach the same goal by different means"*(用不同的办法达成同一个目标),靠 **"intelligence instead of restriction"**(靠智能而不是靠把环境管死)。(主源)
- GEN-0 博客(2025-11-04):具身基础模型的能力 **"predictably scale with physical interaction data — not just from text, images, or simulation — but the real world."**(能力随物理交互数据可预测地增长——不是靠文本、图像或仿真,而是靠真实世界。)(主源)
- 融资博客:*"Millions of robots are operating in the world today. Billions more are coming"*(如今全世界有数百万台机器人在运转,未来还会有数十亿台到来),收尾一句 *"General intelligence will be born from the physical world."*(通用智能将诞生于物理世界。)(主源)
- Florence 对 Forbes 谈"ChatGPT 时刻"类比:*"What's happening now with robotics parallels when people opened GPT-3 and asked it to write a completely new limerick. The limerick didn't exist before."*(机器人领域现在发生的事,就像当年人们打开 GPT-3、让它写一首前所未有的打油诗——那首诗此前根本不存在。)(次源,Forbes 2026-04-02)
- 36氪欧洲镜像转述过一句"Goals are more important than labels"(目标比标签重要)——单源转述,原话 (unverified)。

**这对我们意味着什么:** 他们的整个公司就是我们公理 7(能力随真实交互数据可预测地涨)的 5 亿美元级实盘下注,而且他们自己公布了 scaling 曲线当证据——这条公理在美国最强团队那里也是地基,不是我们的一厢情愿。

## 2. 创始人与团队 (founders & team)

- **Pete Florence,联合创始人、CEO。** 白话:他是 Google DeepMind 的资深研究科学家,牵头做过 PaLM-E(Boldstart 称其 "led PaLM-E research",即"主导 PaLM-E 研究")、是 RT-2 的合著者之一——这两篇是"机器人大脑"方向被引用最多的论文之二;MIT 博士,导师 Russ Tedrake。**为什么重要:** RT-2 就是 VLA 这个范式的开山作之一,等于说"发明这条路的人自己出来创业走这条路了",这本身是最强的路线背书。**2024 年春离开 DeepMind**(本人 X 帖自述 "Last Spring I took off from Google DeepMind"〔去年春天我从 Google DeepMind 离职〕,发于 2025-06;TechCrunch 2025-03 亦称"约一年前"离开——此前档案误写 2025-03,已勘误),2025-03-18 在 NVIDIA GTC 的一场 NVentures 座谈上首次以创始人身份公开亮相(注意:不是公司自己办的发布会)。(主源:个人主页、TechCrunch、RT-2 署名)
- **Andy Zeng,联合创始人、首席科学家。** 白话:伯克利本科、普林斯顿博士,Google Brain/DeepMind 做过 TossingBot、Transporter Nets、PaLM-SayCan,2024 年拿了 IEEE 机器人早期职业奖。**为什么重要:** 他是"让机器人从抓取数据里自己学"这个小方向的元老,采数据设备"data hands"(数据之手)的点子据 Forbes 说就是他在 Newport Beach 看人用夹物钳(grabber)时想出来的——采集设备的技术审美由他定调。注:他的维基百科页面还没更新 Generalist 职务,是信息滞后不是事实冲突。(主源:普林斯顿/Google 论文记录;次源:Wikipedia,滞后)
- **Andrew "Andy" Barry,联合创始人、CTO。** 白话:MIT 博士(CSAIL,2010–2016),之后在波士顿动力当了五年资深机器人工程师(2016–2021,做 Spot 机械臂功能),又在 Broad 研究所做了三年蛋白质工程的机器学习。是 Florence 的 MIT 博士同学。**为什么重要:** 他是三人里唯一有"把机器人硬件做成量产产品"经历的人——采集设备的工程化归他;而且他个人 GitHub 上的 ZCM fork 是我们能找到的关于他们技术栈的唯一面包屑(见 §4)。首笔投资(Boldstart)日期 2024-03-24。(主源:LinkedIn/The Org、Google Scholar)
- **Kamyar Ghasemipour,创始技术员工,** 前 DeepMind 学生研究员——唯一被点名的非创始人。(次源,TechCrunch)

**团队规模:** 72 人(2026-05-31,Tracxn 单源,只当方向参考)。招聘页 18 个在招岗位(2026-07-12 复核):绝大多数是研究/工程/运维/行政,**没有带 "Sales"(销售)头衔的岗位,但有 "Applied AI & Partnerships"(应用 AI 与合作伙伴)和 "Field Applications Engineer"(现场应用工程师)两个面向伙伴/客户的岗位**——此前"零销售 BD 岗"的说法过强,已收窄。公司 2024-03 成立(Boldstart 首笔 2024-03-24),**潜伏(stealth)到 2025-06-17 以 Research Preview(研究预览)博客 + Florence X 帖公开亮相**(此前档案误写"潜伏到 GEN-0 发布",已勘误;GEN-0 2025-11-04 是首个模型级披露)。

**这对我们意味着什么:** 这是一支"论文作者亲自下场"的顶配阵容,他们选了手持爪路线而不是遥操作(人远程操控机器人干活,像开体感遥控车)农场——路线选择本身与我们的公理推导同向。

## 3. 产品全览与规划 (products & roadmap)

| 产品 | 是什么(白话) | 格位 | 关键规格 | 价格 | 披露度 |
|---|---|---|---|---|---|
| **"Data hands"(数据之手)** 采集设备 | 戴在手腕上的可穿戴装置,把人手变成一个"平行夹爪的替身",人干活时录下视觉和传感数据 | **UMI 类手持爪**(不用机器人、人手拿着采数据的夹爪)+ 专职采集劳动;Forbes 明说它是 pincer 式(钳式),没有对生拇指级灵巧 | 硬件规格、传感器、成本**全部未披露**(Forbes:公司 "declined to detail",即"拒绝透露细节");公司自称 "shipped thousands of robot hands across new geographies"(已向多个新地区交付数千台机器人手,GEN-1 博客原句已逐字核验;数千台之说为自述,未独立证实) | 不卖 | **极低** |
| **GEN-0** 基础模型 | 第一个公开展示"数据越多能力按幂律涨"的具身基础模型 | 模型(不是设备) | 语料 27 万+ 小时、披露时每周 +1 万小时,采自"数千个家庭/仓库/工作场所";"Harmonic-Reasoning"(和谐推理)训练目标(感知与动作作为异步连续时间的 token 流,不切成快慢两个系统);**约 7B 参数处有相变**(以下会"僵化",以上继续涨),已扩到 10B+;每天训练消化"6.85 年"的操作经验 | 不卖 | 中(博客有量化曲线,无论文) |
| **GEN-1**(2026-04-02) | 号称达到商用可行性的通用操作模型 | 模型 | 语料 50 万+ 小时;**平均成功率 99%**(GEN-0 为 64%,从零训练 19%);执行速度约 3 倍;每个新任务只需约 1 小时机器人本体(机器人硬件身体)专属数据(比 GEN-0 少 10 倍);演示:12.1 秒折纸箱(此前最好 34 秒)、连续 86 次叠 T 恤、1800 次连续积木装箱等 | 无公开定价、无 SKU、无自助 API;只有 **"Early Access Partners"(早期访问合作伙伴)** 计划(发邮件申请) | 中(数字多,全部自评) |

**数据分级(新发现):** 外包"数据代工伙伴"的数据分 **Class 1 / 2 / 3**——GEN-0 博客原文(已逐字核验):*"Class 1 involves data on specific tasks, Class 3 involves do-anything type data, and Class 2 is everything in between"*(Class 1 是特定任务数据,Class 3 是"什么都能做"类型的数据,Class 2 介于两者之间),与 "multiple data foundry partners"(多个数据代工伙伴)一起用于对比不同预训练数据集。(主源逐字)

**路线图:** 除了融资通稿里的"造下一代模型、扩数据引擎、扩算力"没有任何带日期的公开路线图,没有 GEN-2 的名字或日期。

**这对我们意味着什么:** 他们只占了四格矩阵里"专职×recovered"一格,被动穿戴格与计量格(带实测误差的台架)完全空着,而且设备只自用不外卖——他们不是我们卖设备/卖证书生意的直接对手,而是这条路线可行性的免费证人。

## 4. 技术栈方案 (tech stack)

- **标签路径(动作数据是"算出来的"还是"传感器直接量出来的"——这是数据可信度的命门,因为"算出来的"轨迹会带算法误差,买家没法验货):** Generalist 属于 **recovered(算出来的)** 家族,和 UMI 类设备同宗。但他们**连用什么算法都没说**——没提 SLAM(用摄像头反推自己走过的轨迹)、没提 IMU(惯性测量单元,测加速度和转动的小芯片)、没提任何漂移/误差数字。对比:觅蜂至少还点名了"红外主动光+VSLAM"。Forbes 直接写公司"declined to detail"(拒绝透露)设备内部。这是真实的披露空洞,不是营销省略。(主源负发现,Forbes 直查确认)
- **力/触觉通道(机器人学抓握最缺的就是"手感"数据):** 设备上**没有任何触觉/力传感的证据**,大概率没有(钳式结构,Forbes 点明)。**对我们自己 wiki 的勘误:** `data-collection-devices.md` 里"Genesis/Generalist gloves add tactile"(Genesis/Generalist 的手套加了触觉)那行有把两家搞混的风险——有触觉手套(GENE-26.5)的是 **Genesis AI**,另一家公司;修订时应拆开写。
- **开源足迹(为什么重要:开源是外界唯一能审计他们技术的窗口):** 实测(GitHub/HF API 直查,非搜索):GitHub org `generalistai` 有且仅有 **3 个仓库、全是 fork、零原创代码**——`dinov3`、`dinov2`(Meta 视觉模型)和 **`zcm`**。`zcm` 这个 fork 经由 CTO Andy Barry 的个人 fork 转来(org fork 最近推送 2026-04-02,API 复查 2026-07-12)。**ZCM 是机器人圈用的轻量级发布/订阅消息库(LCM 家族),专门干"多个传感器数据低延迟传输"这件事**——这是我们能找到的关于他们内部采集同步/传输栈的唯一技术面包屑,纯旁证,任何官方材料都没确认过。HuggingFace org 存在但 **0 模型 0 数据集**。**专利:零**(USPTO/Google Patents 定向搜索无一条属于该公司)。
- **论文:** GEN-0/GEN-1 **没有 arXiv 论文**,全部技术细节只在博客里;PaLM-E、RT-2 是创始人在 DeepMind 时期的旧作。
- **传感器/时钟/同步(为什么重要:多路传感器不对表,数据就是废的——这是我们公理 3 的核心):** 帧率、相机型号、IMU 型号、对时方案,**零披露**。
- **数据格式:** 未披露。第三方(日本 note.com/npaka 评论)一针见血:*"the figures and evaluations shown are fundamentally from the company... external evaluation and reproducibility by third parties remain to be verified"*(所展示的数据和评估结果本质上都来自公司自身……第三方的外部评估和可复现性仍有待验证)——所有数字都是自评,无第三方复现。

**这对我们意味着什么:** 全球融资最多的采集玩家在"精度、同步、误差分布"上交了白卷,这等于替我们确认了车道 1(计量院:随货附实测误差报告、证书可审计)在美国市场同样是无人区。

## 5. GTM 与资金 (go-to-market & funding)

**GTM(怎么把东西卖出去):** 目前**没有任何东西在公开卖**。GEN-1 只通过 "Early Access Partners"(早期访问合作伙伴)计划开放(partnerships@generalistai.com),无价目表、无自助 API。**真付费客户:零个被点名**——连觅蜂那种"签约仪式"(拉客户拍照签字但看不到钱)都没有,就是彻底沉默。招聘页无 "Sales"(销售)头衔岗,但已有 "Applied AI & Partnerships"(应用 AI 与合作伙伴)岗(2026-07-12 复核)——伙伴通道在建人,带 quota(业绩指标)的外推销售仍不存在。**采集劳动模式:** 一部分"robot trainer"(机器人训练员)在 San Mateo 办公室内部干,另一部分外包给"数据代工伙伴"(data foundry partners)网络,在"数千个家庭/仓库/工作场所"作业——伙伴身份、地域、工钱全部未披露。社区声音:Cobot CEO Brad Porter 对 Forbes 公开泼冷水:*"Just brute forcing a huge amount of data against a not-perfect architecture is really expensive"*(单纯用海量数据去硬怼一个不完美的架构,代价非常高昂;逐字核验到此;"未必拿得到你要的结果"为同段转述);Reddit/HN 上**找不到一条专门讨论它的帖子**——热度全是媒体给的,不是社区给的。

**融资全史(多源对账,分歧已标):**

| 轮次 | 日期 | 金额 | 领投 | 备注 |
|---|---|---|---|---|
| 种子 | 首笔支票 **2024-03-24**(Boldstart 官方 2024 recap 确认,NVIDIA 同轮,2026-07-12 复核);Tracxn 把"种子轮"标在 2025-03-24,金额未披露 | (unverified);有单源 SERP 说"$12.5M 种子 + 2025 年初 $128M A 轮",无旁证 | Boldstart 首笔;Tracxn 称 NVentures(NVIDIA)领种子 | **日期分歧已标:** 可能是"首笔支票 vs 正式交割"的口径差,未能完全对账 |
| 至 Forbes 报道点 | 截至 2026-04-02 | 累计 $140M,估值 $440M | Spark Capital、NVIDIA NVentures、Bezos Expeditions、Boldstart | (次源,Forbes) |
| 最新一轮(Bloomberg/多数媒体标 B 轮,Tracxn 标 A 轮) | 2026-06-04 | **$400M** | **Radical Ventures** | 新进:8VC、USV、Hanabi、Norwest;跟投:NVIDIA、Boldstart、Spark、Bezos Expeditions、NFDG;官方博客天使名单(逐字核验):**林斌**(小米联创)、李飞飞、Naval Ravikant——袁征(Zoom)仅见媒体转述、官方名单未列 (unverified) |
| **累计** | — | **>$500M** | — | 投后估值约 **$2B**(Bloomberg 被 403 挡,经 Robot Report/SiliconANGLE 旁证) |

**这对我们意味着什么:** 资本市场愿意给"手持爪采数据+自训模型、零收入零客户"的垂直一体化故事开 20 亿美元估值——数据引擎这个品类的钱是真的,但他们把设备锁在自家院里,设备与证书的**外部市场**没人占。

## 6. 没搞清楚的 (explicit unknowns)

1. **设备 BOM(物料清单)/成本。** 查了:Forbes 专访、全部官方博客、招聘页。为什么查不到:公司对 Forbes 明确"declined"(拒绝透露)——主动保密,视为竞争壁垒。
2. **传感器栈**(相机/IMU 型号、分辨率、帧率)。查了:官方博客、GitHub、招聘 JD。为什么查不到:同上,零披露是策略;招聘 JD 也没漏。
3. **标签恢复机制**(SLAM 变体、漂移/误差数字)。查了:博客、访谈、专利库。为什么查不到:无论文无专利,博客只讲模型不讲设备。
4. **设备有无力/触觉。** 查了:Forbes、博客。为什么可能查不到:大概率是"没有"所以没得说(钳式结构旁证)。
5. **专利。** 查了:USPTO/Google Patents 定向检索。为什么查不到:可能真没申请(靠速度和数据护城河,不靠专利),也可能以个人/壳主体申请未挂公司名。
6. **GEN-1 参数量。** 查了:GEN-1 博客及报道。为什么查不到:GEN-0 披露过 7B 相变和 10B+,GEN-1 刻意不说——可能涉及推理成本敏感信息。
7. **点名客户/试点。** 查了:多组"customer/deployment/pilot"(客户/部署/试点)检索。为什么查不到:早期访问计划签保密是行业常态,也可能确实还没有付费客户。
8. **种子轮确切金额与交割日。** 查了:Boldstart、Tracxn、Crunchbase、SERP。为什么查不到:私募轮次无强制披露,三个源三个口径。
9. **中文圈认知。** 查了:36氪/机器之心/量子位/雷峰网三轮定向检索,零命中(噪音全是觅蜂内容)。为什么查不到:不是查不到,是真没有——截至 2026-07 中文具身媒体雷达上没有这家公司。
10. **数据代工伙伴的身份、地域、工价。** 查了:Forbes、招聘页、搜索。为什么查不到:劳务外包细节是成本结构机密,且可能涉及众包合规敏感。

## 7. 与我们设计的对撞要点 (collision highlights)

引用 [data-engine-first-principles](data-engine-first-principles.md)(公理与收敛核)与 [data-engine-v2](data-engine-v2.md)(三车道定位)的既有结论,不重新推导:

1. **公理 7 获最强验证。** GEN-0→GEN-1 的 27 万→50 万小时语料与公开 scaling 曲线(64%→99%,新任务数据需求降 10 倍),是"能力随真实交互数据可预测地涨"这条公理迄今最大规模的第三方实盘证据——虽然全部数字自评无复现,方向性仍成立。
2. **2×2 矩阵的"专职×recovered"格被 5 亿美元填满,其余格照旧空着。** 首原理页的四格分析(副产品/专职 × recovered/measured)在 Generalist 身上再次成立:他们与觅蜂一样只占专职手持爪一格;被动穿戴格(公理 8 的非工资地板姿态)与 measured 格他们都没碰。手持爪路线的劳动经济学(专职采集工+代工伙伴网络)被他们再次市场验证。
3. **车道 1(计量院)的空腔被美国头部玩家反向确认。** v2 页判定"误差分布随货、证书可审计"是全品类无人占的差异化;Generalist 连恢复算法名字都不说、零专利、零开源、零第三方评测——**空腔不仅在中国空着,在美国也空着**。而且他们是买方生态的塑造者:当他们的 Early Access 伙伴将来想审计数据质量时,市场上只有我们这类中立尺子。
4. **公理 11(标签路径无黑盒单源)被他们的反面示范凸显。** 我们要求原始流落盘+开源恢复算法,买家可换件可审计;Generalist 是彻底黑盒——第三方评论("figures... fundamentally from the company",即"数字本质上都来自公司自身")正是黑盒模式必然招致的信任折扣,这是我们"每句宣称可指向公开证书"纪律(v2 P9)的对照组。
5. **一处真挑战:垂直一体化可能根本不需要卖设备的市场。** Generalist 证明最强团队的选择是"设备自用、数据自吃、只卖模型访问权"——如果这成为具身头部共识,采集设备的外部买家就只剩二线模型厂和本体厂。这不推翻我们的车道,但支持 v2 的诚实排序:车道 1 的护城河必须落在"仪器+证书+中立审计"上,而不是幻想头部模型厂来买爪子。
6. **ZCM 面包屑与公理 3 同向(旁证级)。** CTO 亲手 fork 低延迟多传感器消息库,暗示他们同样把"传输与同步"当采集栈的脊梁——与我们时钟岛/单晶振架构的优先级判断一致,但证据强度仅为旁证。

## 8. 观察哨 (watch items)

| 触发事件 | 含义 | 检查节奏 |
|---|---|---|
| GEN-2 或新模型发布(留意语料小时数) | 若语料增速跳档(>2 万小时/周),说明采集舰队规模翻倍,手持爪路线经济学进一步坐实 | 每次 sweep |
| 任何设备规格/误差/同步方式披露,或 arXiv 论文出现 | 车道 1 空腔被头部玩家侵入的第一信号;对照 v2 的"披露战"响应预案(响应窗 ≤4 周) | 每次 sweep |
| Early Access 伙伴被点名 / 出现公开定价或 API | 从"沉默"转向真商业化,买方开始有审计需求——证书 SaaS 的销售窗口信号 | 每次 sweep |
| 招聘页出现带 quota 的销售岗(已有 "Applied AI & Partnerships" 岗,2026-07-12) | GTM 从伙伴内推转外推,商业化提速的领先指标 | 月度 |
| 专利公开(申请后 18 个月公开期) | 若 2024–2025 年申请过,2026-H2 起会陆续可见;届时重查 USPTO | 2026-Q4 |
| 中文媒体首次实质报道 | 中国市场认知启动;影响我们车道 3 出海叙事的对标话术 | 月度 |
| 觅蜂/国内玩家公开对标 Generalist | 两条手持爪路线正面对撞,披露战可能被迫升级——利好我们的中立横评位 | 每次 sweep |

## Sources

**一档(主源,直接核验;全部于 2026-07-12 复核):**
- https://generalistai.com/blog/gen-1 (2026-04-02) — GEN-1 全部指标(50 万小时、99%/64%/19%、~3x、~1 小时本体数据、12.1s/86 次/1800 次)、physical AGI 使命引语、"shipped thousands of robot hands" 原句,逐字复核通过
- https://generalistai.com/blog/gen-0 (2025-11-04) — 27 万小时、+1 万小时/周、Harmonic-Reasoning、7B 相变、10B+、6.85 年/天、Class 1/2/3 原文、scaling 引语,逐字复核通过
- https://generalistai.com/blog/accelerating-the-next-phase-of-physical-ai (2026-06-04) — $400M 轮、累计 >$500M、投资人全名单(天使仅林斌/李飞飞/Naval Ravikant)、"Millions of robots..."/"born from the physical world" 引语,逐字复核通过
- https://generalistai.com/careers — 18 岗位复核通过;岗位地标 SFO/BOS;含 "Applied AI & Partnerships" 岗
- https://generalistai.com 页脚 — 法律名 "© 2026 Generalist AI, Inc."
- https://x.com/peteflorence/status/1935021240802291901 (2025-06-17) — 创办宣言帖;**2026-07-12 复核:登录墙 402,仅开头经搜索快照逐字证实**
- https://github.com/generalistai — 3 fork(dinov3/dinov2/zcm)零原创(API 复核通过)
- https://huggingface.co/GeneralistAI — 0 模型(API 复核通过,返回空数组)
- https://peteflorence.com 及 RT-2 论文 https://arxiv.org/abs/2307.15818 — 创始人履历锚点

**二档(可靠次源):**
- Forbes(2026-04-02, annatong)— $140M/$440M 节点、设备"declined to detail"、钳式、Zeng 起源故事、GPT-3 limerick 引语、Brad Porter 引语(以上均于 2026-07-12 对原文复核通过)
- TechCrunch(2025-03-19)— GTC 亮相、"dead set" 与 "marginal cost of physical labor is driven to zero" 直引、Ghasemipour(复核通过)
- Bloomberg(2026-06-04,标题可见)/ SiliconANGLE / qz — $400M 轮、~$2B 估值、Series B 口径、San Mateo 总部
- Boldstart Ventures 官方(2024 recap + portfolio 页)— 首笔支票 2024-03-24、NVIDIA 同轮(复核通过)

**三档(单源/需谨慎):**
- Tracxn — 72 人团队、种子轮 2025-03-24 口径(与 Boldstart 冲突已标)
- note.com/npaka — 第三方"无外部复现"评论
- 36氪欧洲镜像 — "Goals are more important than labels" 转述 (unverified)
- 单源 SERP "$12.5M seed/$128M Series A" 说法 (unverified)

**站内:** [data-engine-first-principles](data-engine-first-principles.md) / [data-engine-v2](data-engine-v2.md) / [case-mifeng](case-mifeng.md) / [data-foundry.md](data-foundry.md) / [data-collection-devices](data-collection-devices.md)(含待修的 Genesis/Generalist 混淆行)
