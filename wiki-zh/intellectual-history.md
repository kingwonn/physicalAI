---
title: 具身智能学术思想史 (The Intellectual History of Embodied Intelligence)
slug: intellectual-history
updated: 2026-07-12
confidence: verified
lang: zh
source: ../wiki/intellectual-history.md
---
<!-- 对抗性核验 2026-07-12(引文/归属专项):全部带引号原文对一手文本(scratchpad/lineage1 dossier + elephants/representation/schaal1999 全文提取)或已核 lineage 页回源,存疑者对网上一手/权威源复核。已纠 8 处:① PSSH 补回原文 "general"(CACM 19(3) p.116,Nilsson 2007 转引漏词);② Ashby "only variety can absorb variety"→"only variety can destroy variety"(1956),absorb 版系 Stafford Beer 转述;③ Searle 公理句全文补齐并改归 1990《Scientific American》公理 3(1980 BBS 无此句);④ "world is its own best model" 从 1986 包容架构行移正至 1990《Elephants》;⑤ Grey Walter "two functioning neurones" 降格为二手转述(原文措辞未一手核到);⑥ Schaal 1999 引文补 "the study of";⑦ Sutskever 引文补 "My bet is that";⑧ Ha&Schmidhuber 2018 补 Schmidhuber 1990/Dyna 1991 优先权注。另:Shakey "开环执行"改为慢速重规划闭环(有 PLANEX 执行监控);钟摆二/三/四补史学脚注(控制论与感知机在符号时代延续至 1969、行为机器人摆是机器人学局部、统计转向始于 1990s 统计 NLP)。已复核为真:Wiener 1943/副标题、Dartmouth、Lighthill 两句、Harnad、Gibson 两句、Moravec pp.15–16、Pinker 1994 转述纠误、Brooks 1990 物理接地/35 亿年/"(H)"、Braitenberg、Varela、McGeer、Smith&Gasser 2005、Sutton TD/苦涩教训两句、Better Lesson 2500W vs 20W 与 6 天间隔、RT-2 命名句、DAgger、Levine 9.2 万参数、Tobin、Raibert "controlled falling" 转述标记;62h V-JEPA、RT-2 翻倍、locomotion 零示范、X1–X8 映射均与源页一致。 -->

> 「说人话」:今天机器人行业的每条技术路线,都是一场打了七十年的学术论战里某个学派的转世。这一页讲清:哪三条思想血脉汇成了今天的具身智能、"智能需不需要身体"这个钟摆怎么摆了三个来回、几场关键论战谁说了什么(带原文),以及学术史视角下这门技术的本质到底是什么——它和我们从产业语料挖出的 X-pattern([physical-ai-essence](physical-ai-essence.md))如何互相印证。这一页讲**思想**的历史;工业事件的时间线不在这里,在 [history](history.md);今天各领袖的论点是这场老论战的最新一轮,在 [visions](visions.md)。

---

## 0. 一句话地图

先给最忙的读者一张地图:**这门技术不是新发明,是一个七十年悬案第一次要被真机实验裁决。** 悬案叫"智能需不需要身体"。1943 年控制论说"需要,且身体就是反馈回路";1956 年符号 AI 说"不需要,智能是符号计算";1986 年起 Brooks 一派反扑说"当然需要,世界就是自己最好的模型"(此句语出其 1990 论文);2012 年后统计学习又把智能抽离身体、2022 年 LLM 把"去身"推到史上极致;而 2024 年起的 Physical AI 又要把这些最没有身体的造物(互联网预训练的视觉语言模型)塞进机器人身体里。**中心悖论:一个花了四十年论证"智能离不开身体"的领域,如今正被人类造过的最"离身"的产物殖民。** 这到底是具身认知学派的胜利还是它的反证?这是本页要诚实对待的开放问题。

---

## 1. 三条血脉 (the three lineages)

今天的具身智能不是一条线进化来的,是三条各自独立的思想血脉在 2022–2026 年撞在一起。三条各有各的"身体观",今天的路线之争其实是它们互不相让的续集。

### 血脉一:控制论 → 符号 AI → 批评者(1943–1990)

「说人话」:这条线是"智能的定义之争"。它先说智能是**反馈**(控制论),再说智能是**符号计算**(符号 AI),然后被一批哲学家和工程师围攻说"你们都漏了身体"。

| 年份 | 人物/工作 | 核心主张(带原文) | 它赌什么 |
|---|---|---|---|
| 1943 | Rosenblueth, Wiener, Bigelow《Behavior, Purpose and Teleology》 | "All purposeful behavior may be considered to require negative feed-back."(一切有目的的行为都需要负反馈) | 赌:智能=有目的的行为=负反馈回路;身体和机器无本质区别 |
| 1948 | Wiener《Cybernetics》 | 副标题即主张:"control and communication in the animal and the machine"(动物与机器中的控制与通信) | 赌:一套数学统一生物、机器、社会的控制 |
| 1948/1956 | Ashby 稳态机(Homeostat, 1948)+ 必要多样性定律(1956) | "only variety can destroy variety"(唯有多样性能消灭多样性,《An Introduction to Cybernetics》1956;流传更广的 "only variety can absorb variety" 是 Stafford Beer 的转述,非 Ashby 原话) | 赌:控制器的行为库必须和它面对的扰动一样丰富——"身体给你免费的多样性"的祖先 |
| 1948–50 | Grey Walter 电子龟(Elmer/Elsie) | 两个真空管电路≈"两个神经元"的等价物(二手转述措辞,原文确切用词 unverified);无世界模型、无规划,行为直接从传感-马达耦合涌现 | 赌:复杂行为不需要符号,只需要简单反射×真实环境——**第一台行为机器人** |
| **1956** | **Dartmouth 提案**(McCarthy, Minsky, Rochester, Shannon) | "every aspect of learning or any other feature of intelligence can in principle be so precisely described that a machine can be made to simulate it."(智能的每个方面原则上都能精确到让机器模拟) | 赌:智能=可形式化的东西;身体是可选的外设。**"人工智能"一词诞生** |
| 1966–72 | Shakey + STRIPS(SRI) | 第一台完整"感知-规划-行动"机器人;世界=一阶逻辑谓词集,行动=前提/增删表,规划=搜索 | 赌:机器人=把世界读成符号→在符号上规划→执行。**sense-plan-act 范式的原型** |
| 1976 | Newell & Simon 物理符号系统假说(PSSH,图灵讲座) | "A physical symbol system has the necessary and sufficient means for general intelligent action."(物理符号系统具备**一般**智能行为的必要且充分手段;原文含 "general",*CACM* 19(3) p.116,常见转引漏掉此词) | 赌:符号操作**充分**产生智能;身体只是符号接地的通道 |
| 1972 | Dreyfus《What Computers Can't Do》 | 人的专长是"know-how 先于且不可还原为 know-that";智能是"(human-like) being in the world"、需要"bodies more or less like ours"(引号措辞出自 Dreyfus 2000 年代重述、经 Nilsson 2007 转引;1972 原书主张一致,原书原文未一手核到) | 赌(反方):符号 AI 撞墙,因为常识和技能无法形式化——最早、最强的具身派哲学家 |
| 1973 | Lighthill 报告 | 病根是"failure to recognise the implications of the 'combinatorial explosion'"(组合爆炸);"pronounced feeling of disappointment" | 判(反方):搜索式 AI 无法规模化——直接触发第一次 AI 寒冬 |
| 1980 | Searle 中文屋 | 1980《Minds, Brains, and Programs》以思想实验立论;公理化的名句 "Syntax by itself is neither constitutive of nor sufficient for semantics."(句法本身既不构成语义、也不足以产生语义)出自其 1990《Scientific American》"Is the Brain's Mind a Computer Program?"(公理 3) | 赌(反方):对的符号操作不足以产生理解——攻击 PSSH 的"充分性" |
| 1990 | Harnad 符号接地问题 | "How can the meanings of the meaningless symbol tokens ... be grounded in anything but other meaningless symbols?"(无意义符号的意义如何接地于符号之外?) | 赌(反方):符号必须自底向上接地于感官(iconic/categorical 表征)——今天"LLM 缺接地"批评的直系祖先 |

**白话叙事:** 这条线是一部"智能定义的三段剧"。第一幕(1943–48),控制论说智能是**反馈回路**——一个自动瞄准的鱼雷(Wiener 的原例)和一只追光的电子龟已经算"有目的";身体不神秘,它就是回路的一部分。第二幕(1956–76),符号 AI 掀桌子:智能不是回路,是**符号计算**;Shakey 把世界读成逻辑谓词、在谓词上规划、靠缓慢的感知-规划-行动串行循环执行(有执行监控与重规划,但慢而脆),PSSH 把这升格为"符号系统充分产生智能"的科学假说。第三幕(1972–90),四位批评者从四个方向围攻:Dreyfus 说你漏了不可形式化的身体常识,Lighthill 说你算不动(组合爆炸),Searle 说句法不等于语义,Harnad 说你的符号悬空——这四刀合起来就是"符号 AI 缺身体/缺接地"的完整控诉状。第一次 AI 寒冬(1974–80)是这场围攻的战果。

**这对理解今天意味着什么:** 今天所有"LLM 到底懂不懂物理世界"的争论,是 1980 年中文屋和 1990 年符号接地问题的**逐字重演**。Brooks 自己在 2023 年直接承认"GPT **是**中文屋"([lineage-embodied-cognition](lineage-embodied-cognition.md) §1)——他没有说 Searle 赢了,他说的是"现在真的造出一个中文屋了,老论证必须正面重打一遍"。我们的 X2 具身税(信息在人体最便宜、动作必须在机体执行)就是符号接地问题**被货币化**的版本:接地不再是哲学难题,而是一笔按小时付工资的账单。

### 血脉二:具身认知学派(1980s–2010s)

「说人话」:这条线不是问"智能是什么定义",而是造真东西+提哲学主张来证明"没有身体就没有认知"。它是血脉一里"批评者"的建设性续集。

| 年份 | 人物/工作 | 核心主张(带原文) | 它赌什么 |
|---|---|---|---|
| 1979 | Gibson 生态心理学/可供性(affordance) | "The affordances of the environment are what it offers the animal";可供性"cuts across the dichotomy of subjective–objective" | 赌:知觉是对环境信息的**直接**拾取,不是从贫乏视网膜输入计算重建;被动视频是categorically更弱的信号 |
| 1984 | Braitenberg《Vehicles》 | "law of uphill analysis and downhill invention":造一个产生某行为的机制容易,反推一个黑箱的内部机制难 | 赌:观察者会系统性高估简单机制的内在复杂度——对"从行为推断理解"的方法论警告 |
| 1986 | Brooks 包容架构(subsumption) | 分层反应行为,高层可抑制低层,无中央世界模型 | 赌:智能自下而上从传感-马达耦合涌现,符号规划是弯路 |
| 1990/91 | Brooks《Elephants Don't Play Chess》/《Intelligence Without Representation》 | "physical grounding hypothesis";"the world is its own best model"(语出 1990《Elephants》,常被误引至 1986 或 1991);"(H) Representation is the wrong unit of abstraction" | 赌:要智能必须把表征接地于物理世界;表征本身是错的抽象单位 |
| 1972/80 | Maturana & Varela 自创生(autopoiesis) | 生命=持续自我生产自身组分与组织的网络 | 赌:认知是自我维持系统所做的事,不是外部施加的信息处理 |
| 1991 | Varela, Thompson, Rosch 生成认知(enactivism) | "cognition is not the representation of a pregiven world by a pregiven mind but ... the enactment of a world" | 赌(最强/构成性):身体不是效率问题,是认知**定义**的一部分——去身系统在做另一件事,只是输出相似 |
| 1990 | McGeer 被动动态行走 | 双腿机构在斜坡上零驱动、零控制、零计算settle into类人步态 | 赌:身体设计能替代控制/计算复杂度——形态计算的物理存在证明 |
| 2005 | Smith & Gasser 具身假说 | "The embodiment hypothesis is the idea that intelligence emerges in the interaction of an agent with an environment and as a result of sensorimotor activity." | 赌:把具身当**可证伪的科学假说**命名;从婴儿发育推 AI 原则 |

**白话叙事:** 如果血脉一是哲学法庭,血脉二就是把主张搬进实验室。Brooks 是核心人物:他造真机器人,发现"一旦承诺把表征接地于物理世界,对传统符号表征的需求就完全消失了"——他最出名的那句"世界就是它自己最好的模型",完整意思是"世界永远最新、永远含有全部细节,诀窍是恰当且足够频繁地感知它"([lineage-embodied-cognition](lineage-embodied-cognition.md) §1)。这一派内部有软硬之分(这个区分对今天极其关键):**弱/架构版**(Brooks、形态计算)说身体改变的是"什么高效/实际必要"——McGeer 的零计算行走机就是铁证,一个真实物理系统用**零比特**控制器走出了类人步态;**强/构成性版**(生成认知、Gibson 直接知觉、Lakoff 隐喻接地)说身体是认知**定义本身**的一部分,去身系统不是做得差,是根本在做另一件事。

**这对理解今天意味着什么:** 今天把"embodiment""grounding""affordance"这些词随手扔进 LLM/VLA 辩论的人,九成没意识到自己在调用的是**弱版还是强版**——两者可证伪性天差地别。我们的 X4 时钟分层律(五家前沿系统全长成"慢层管语义/快层管运动/反射层管安全")其实是 Brooks 1986 包容架构的**转世**:分层反应、高层抑制低层、每层各自完整——只是当年用真空管的地方,今天换成了 VLM。McGeer 的零计算行走机则直接预言了我们语料里"locomotion 已被仿真 RL 零示范解决"([locomotion](locomotion.md))这一事实:行走这件事,身体和物理承担了大部分"计算"。

### 血脉三:学习与控制的工程汇流(1960s–2026)

「说人话」:这条线不吵哲学,只管"怎么让一台真机器人把一件真事做好"。它是今天机器人**实际**跑的代码的祖先——控制论→强化学习→模仿学习→深度 RL→VLA→世界模型。

| 年份 | 人物/工作 | 核心主张(带原文) | 它赌什么 |
|---|---|---|---|
| 1960 | Kalman 滤波 | 状态空间递归最优估计器 | 赌:实时状态估计可递归、可计算——今天每个机器人控制栈的祖先 |
| 1984/86 | Raibert 动态平衡 | "active dynamic balance":机器人从不静态稳定,靠快速反馈边倒边接 | 赌:动态平衡比静态稳定强——Boston Dynamics 的技术源头("controlled falling"是后人转述,非其原话) |
| 1988 | Sutton 时序差分(TD)学习 | 从"相邻预测之差"更新价值,不必等最终结果 | 赌:价值可从经验自举——现代 RL 的信用分配机制 |
| 1997–99 | Schaal, Atkeson 模仿学习 | "the study of imitation learning offers a promising route ... [that] could ultimately lead to the creation of autonomous humanoid robots"(Schaal 1999 摘要);硬件必要不充分,缺的是**算法** | 赌:技能从少数示范自举,不必逐条手编——今天数据问题的直系祖先 |
| 2011 | Ross et al. DAgger | 行为克隆有复合误差;迭代让专家标注策略自己走到的状态 | 赌:分布漂移可用在线学习修——今天 VLA 谈鲁棒性必引 |
| 2016 | Levine, Finn, Darrell, Abbeel 端到端视觉运动策略 | 像素进、力矩出,单个 CNN 联合训练(~9.2 万参数) | 赌:感知与控制不该分阶段——今天所有"像素到动作"的祖先 |
| 2017 | Tobin et al. 域随机化 | 随机化仿真参数,让真实世界"看起来只是又一种变体" | 赌:仿真+随机化=免费数据——sim2real 支柱 |
| 2018 | Ha & Schmidhuber《World Models》 | "train our agent entirely inside of its own hallucinated dream"(在自己幻想的梦里训练) | 赌:在学到的生成模型里训练策略——今天 Cosmos/Genie/GR00T 的直接祖先;思想优先权更早:Schmidhuber 1990《Making the World Differentiable》的控制器/世界模型拆分、Sutton Dyna 1991([lineage-learning-control](lineage-learning-control.md) §6,优先权是 Schmidhuber–LeCun 间在世论战) |
| 2019 | Sutton《The Bitter Lesson》 | "general methods that leverage computation are ultimately the most effective, and by a large margin";"building in how we think we think does not work" | 赌:规模+通用打败人类精工结构 |
| 2019 | Brooks《A Better Lesson》(6 天后) | 反驳:人类知识没消失,只是搬进了架构设计;还有能耗不对称(2500W vs 20W)、摩尔定律在放缓 | 赌(反方):"纯规模"不是免费午餐,是把人类巧思藏进网络结构 |
| 2023 | RT-2 命名 VLA | "We refer to such category of models as vision-language-action models (VLA)" | 赌:互联网视觉语言知识**零具身**获得,能迁进机器人身体 |
| 2005/2022 | Smith & Gasser vs Sutskever | 具身假说 ↔ "My bet is that physical embodiment is not necessary, though there is some chance that it will make things a lot easier." | 赌:身体必要 ↔ 身体不必要(互联网文本可替代)——今天路线之争的最纯对撞(两者非直接交锋,是独立到达的对立立场) |

**白话叙事:** 这条线的性格和前两条相反——它**对哲学不表态**。一个 Kalman 滤波器或一个 DAgger 策略,不管你信不信"智能需要身体",工作方式都一样。前四段(控制、RL、模仿、深度 RL/sim2real)是纯工程,只解"这台机器怎么把这件事做好"。真正撞上哲学是在第五、六段:RT-2 的整个前提——把**零具身**获得的网络视觉语言知识,靠一个薄薄的动作解码头塞进机器人——就是 Sutskever 那句"具身非必要"的直接工程下注,而它恰好对撞 Smith & Gasser 命名的"具身假说"。这条线里还藏着一对最干净的"辩论档案":Sutton 2019 年《苦涩教训》说"规模打败精工",Brooks 六天后《A Better Lesson》逐条反驳——不是事后追认的分歧,是白纸黑字、带日期、点名的对打。

**这对理解今天意味着什么:** 这条线是我们语料里"scaling 竞赛撞上数据墙"([physical-ai-essence](physical-ai-essence.md) 主线一)的思想史。Schaal 1999 年那句"缺的不是硬件是算法"直接长成了今天 X1 技能资本化的经济学问题:技能怎么从劳务变资本。而苦涩教训 vs A Better Lesson 这对,正是我们 X2 里"苦涩教训第一次遇到不服从摩尔定律的成本项——工资"这句判词的思想史源头。

---

## 2. 钟摆:具身 → 去身 → 具身(the embodiment pendulum)

「说人话」:"智能需不需要身体"这个问题,七十年里像钟摆一样来回摆了三个来回。看清这个钟摆,就看清了整门技术的节律。

**第一摆·具身(1943–1955):** 控制论时代,智能=反馈回路,身体天然在场。Wiener 的鱼雷、Ashby 的稳态机、Grey Walter 的电子龟——都是"身体×环境"直接产生行为,没有中央大脑。

**第二摆·去身(1956–1985):** 符号 AI 把智能抽离身体。Dartmouth 说智能是可形式化的符号操作,PSSH 说符号系统"充分"产生智能,Shakey 把世界压成谓词、靠慢速重规划闭环。身体降格为"符号接地的外设"。这一摆撞墙:组合爆炸(Lighthill)、Shakey 的脆弱与慢(规划一个简单任务要算数小时,secondary)、四位批评者的围攻,合力砸出第一次 AI 寒冬。*史学脚注:切换不是一夜之间——控制论与神经网络研究在"去身"时代内部延续(Ashby《Introduction to Cybernetics》1956、Rosenblatt 感知机 1958),直到 1969《Perceptrons》与经费转向才被边缘化;"摆"描述的是重心迁移,不是学派消失。*

**第三摆·回具身(1986–2011):** Brooks 反扑。"世界是它自己最好的模型",包容架构扔掉中央世界模型,机器人行为从传感-马达耦合涌现。Roomba(2002)是这一摆的商业变现——用行为主义、无符号规划,把机器人送进千万家庭。同期具身认知学派(Gibson、生成认知、形态计算)在哲学侧建墙:身体不是可选项。*史学脚注:这一摆主要发生在机器人学内部;同一时期主流 AI 的重心其实在走向统计方法(专家系统退潮后的概率图模型、统计 NLP、机器学习自立门户)——钟摆是分学科局部的,不是全领域齐步走。*

**第四摆·再去身(1990s 起势,2012–2023 加速):** 统计学习把智能又一次抽离身体,而且抽得比符号 AI 更彻底。去身的统计转向 1990 年代就已开始(统计 NLP 用语料库替代语言学规则,是"用数据替代身体/知识"的先声);2012 年 AlexNet 后深度学习→深度 RL→LLM,一路把"从数据里学"推到极致;2022 年 ChatGPT 是史上最去身的智能造物——它没有任何身体,只有互联网文本,却表现出通用能力。Sutskever 2022 年那句"具身非必要"是这一摆的宣言。

**第五摆·Physical AI(2024–):** 钟摆正在往回摆,但方式极其反讽——不是造具身认知学派想要的"从婴儿发育起长出身体的智能",而是**把第四摆里最去身的产物(互联网预训练的 VLM)直接塞进机器人身体**。RT-2、π0、Helix、GR00T 全是这个形状:一个网络预训练的大脑 + 一个动作解码头 + 一具身体。

**中心悖论(诚实展开):** 一个花了四十年论证"智能需要身体"的领域(血脉二整条),如今正被人类造过的最离身的造物殖民。**这到底是具身认知的胜利还是它的反证?** 两种读法都有语料证据,而且现在正被真机实验裁决:

- **读作胜利**:V-JEPA(LeCun 反 VLA 的旗舰)最终还是内嵌了 62 小时机器人动作微调才能干活([lecun-worldmodels-rethink](lecun-worldmodels-rethink.md))——纯去身的世界模型不够,还是要具身数据接地。视频里"没有一牛顿的力"([data-scaling-strategy](data-scaling-strategy.md)),接触任务上离身预训练顶不上真机语料。这些都是"身体必要"的证据。
- **读作反证**:RT-2 证明了互联网视觉语言知识**能**零具身迁进机器人、未见任务成功率翻倍([history](history.md));locomotion 被仿真里、无真实身体地解决了([locomotion](locomotion.md))。这些是"离身预训练+薄接地"路线奏效的证据。

**这对理解今天意味着什么:** 钟摆这次不同——**它第一次能做实验**。前四摆都是靠哲学论证和有限 demo 摆来摆去,谁也没真正裁决过。这一摆,V-JEPA 需要多少小时真机数据、RT-2 的网络知识迁移率、接触任务的 sim-to-real 复现——都是可测的数字。所以本页第 4 节的裁决是**条件性的、带到期日的**:钟摆的落点会在 2027–2029 年由几个具体实验读出来,而不是由谁的哲学更漂亮。

---

## 3. 五场关键论战 (the great debates, with receipts)

| # | 论战 | 双方 | 当年怎么判 | 今天的证据 | 还没判的 |
|---|---|---|---|---|---|
| D1 | PSSH vs 符号接地 | Newell&Simon(符号充分)↔ Searle/Harnad(句法≠语义) | 悬而未决;寒冬中批评者占上风 | LLM 逼所有人重打:"GPT 是中文屋"(Brooks 2023) | 大规模统计接地算不算"真接地" |
| D2 | Dreyfus vs GOFAI | Dreyfus(智能是具身应对)↔ 符号 AI | 1970s 停滞被读作 Dreyfus 部分获胜 | LLM 学会语法却无普遍语法(Brooks 承认priors被打脸) | 常识/技能能否被统计规模逼近 |
| D3 | Brooks vs 表征 | Brooks("世界是自己最好的模型")↔ 中央世界模型派 | 行为机器人赢了昆虫级,输了高层认知 | VLA 全是分层(X4);但顶层用大世界模型(LeCun) | 表征该多"厚";离线模型 vs 持续再感知 |
| D4 | 苦涩教训 vs 精工结构 | Sutton(规模打败精工)↔ Brooks(结构没消失只是搬家) | 语料里 locomotion/架构由 scale 赢两次 | scale 赢在数据免费处(仿真/视频);输在数据要工资处(灵巧) | 数据墙能否被合成数据/世界模型绕过 |
| D5 | LeCun 世界模型 vs 自回归 | LeCun(JEPA 潜空间预测)↔ VLM 自回归 token | 未判;今天这一轮的核心 | JEPA 旗舰内嵌 62h 动作微调;VLA 与世界模型正合流 | 哪种架构是主导设计;见 [lecun-worldmodels-rethink](lecun-worldmodels-rethink.md) |

**D1 — PSSH vs 符号接地。** 1976 年 Newell & Simon 立下"物理符号系统具备智能行为的必要且充分手段";1980 年 Searle 中文屋攻其"充分"(句法不构成语义),1990 年 Harnad 精确化为"符号如何接地于符号之外"。当年没判——寒冬里批评者气势占优,但没人能证伪 PSSH。**今天的证据:** LLM 把这场论战逼到墙角。Brooks 2023 年承认"GPT 是中文屋——它真的存在了,老论证必须正面重打一遍"。**还没判的:** 大规模统计学习(把整个互联网压进权重)算不算解决了接地?我们的 X2 具身税给了一个经济学裁决角度:接地在自由空间近零税、在接触处最重税——也就是说 Harnad 的问题不是全有全无,是有一张税率地图。

**D2 — Dreyfus vs GOFAI(老式符号 AI)。** Dreyfus 1972 年说人的专长是不可形式化的具身应对("know-how 先于 know-that"),需要"more or less像我们的身体"。当年被主流嘲笑,但 1970s 的停滞被后世读作他部分获胜。**今天的证据反转了一半:** Brooks 2023 年惊讶承认 LLM 学会了语法"却没有 Chomsky 说必须内建的普遍语法知识"——一个纯统计、非内建、非具身的学习器做到了他先验认为需要内建结构的事。这对 Dreyfus 是喜忧参半:符号 AI 确实撞墙了(他对),但撞墙的原因可能不是"缺身体",而是"缺规模"(他没料到)。

**D3 — Brooks vs 表征("世界是自己最好的模型")。** 1986–91 年 Brooks 主张扔掉中央世界模型,让行为从传感-马达耦合涌现。当年结论清楚:行为机器人赢了昆虫级智能(避障、觅食、Roomba),输了高层认知(没造出通用智能)。**今天的证据两面下注:** 我们语料里五家前沿 VLA 全长成分层形状(X4)——这是 Brooks 包容架构的胜利;但每家的**顶层**都是一个大世界模型/VLM(这是他反对的东西)。Brooks 自己的可证伪预言仍然开着:任何"先建模型再行动"的架构,在世界变化处会脆——这直接可测于今天的离线训练 VLA 分布外是否崩。

**D4 — 苦涩教训 vs 精工结构。** 2019 年 Sutton:"利用计算的通用方法最终最有效,且优势巨大";Brooks 六天后逐条反驳:人类知识没消失,只是从"手编规则"搬进了"网络架构设计",而且还有能耗不对称和摩尔定律放缓。**今天的证据是分裂判决:** 苦涩教训在语料里赢了两次(locomotion、操作架构),但**都赢在数据免费的基质上**(仿真、网络视频);它没赢的地方(灵巧、可靠性)恰是数据要付工资的地方。这就是我们 X2 的核心判词:**苦涩教训第一次遇到一个不服从摩尔定律的成本项——工资**。**还没判的:** 合成数据/世界模型能否把"要工资的数据"变回"免费的数据",从而让苦涩教训在灵巧上也赢。

**D5 — LeCun 世界模型 vs 自回归(今天这一轮)。** LeCun 主张世界模型应预测**表征**(JEPA)而非像素/token,因为生成式像素预测浪费容量在无关细节上;对手是 VLM 自回归 token 派(RT-2/π0/Figure)。这是老论战的最新一轮,还没判。**今天的证据:** LeCun 反 VLA 的旗舰结果里都内嵌 62h 动作微调这个"缩小版敌军"([lecun-worldmodels-rethink](lecun-worldmodels-rethink.md));VLA 与世界模型正在合流(GR00T N2 "world-action model")。**还没判的:** 哪种架构会成为主导设计。我们 X4 的动力学版本给了一个预测:每场路线战争都不以全胜告终,而以**各阵营被收编进其数据占优的那一层**告终——LeCun 会赢慢层(世界模型),VLA 会赢中层(动作策略)。

---

## 4. 学术史裁决:这门技术的本质 (the essence, per academic history)

**问题:** 七十年思想史说这门技术**本质上是什么**?权衡四个候选:

- **(a) 具身问题的经验裁决**:钟摆终于拿到了一个实验。这是最诚实的元层描述——整门技术本质上是"智能需不需要身体"这个七十年悬案第一次被真机数据裁决的现场。它不是一个"是什么"的答案,是一个"正在被回答"的状态。
- **(b) Moravec 悖论作为本领域的守恒律**:我们的 X2 具身税 = Moravec 1988 被货币化。这是最精确的映射(下面展开)。
- **(c) 技能获取的工业化**:X1 技能资本化 = Schaal 1999 那个问题("模仿学习是否通向人形机器人")的经济形态。Schaal 问的是"技能怎么从少数示范自举",X1 答的是"自举出来的技能怎么从劳务变成可无限摊销的资本"。
- **(d) 包容架构的平反**:X4 时钟分层 = Brooks 1986 穿上 VLA 外衣。五家前沿系统全长成分层反应形状,因为三个不可通约的时钟被物理钉死。

**X-pattern 与学术祖先的映射表:**

| X-pattern | 学术祖先 | 年份 | 当年的表述 | 今天的表述 |
|---|---|---|---|---|
| **X1 技能资本化** | Schaal 模仿学习问题 | 1999 | 标题之问 "Is imitation learning the route to humanoid robots?";答:模仿学习是 "a promising route" | 技能从劳务变资本:一次训练、$0 复制、全机队摊销 |
| **X2 具身税·接触梯度** | Moravec 悖论 | 1988 | "prodigious olympians in perceptual and motor areas";感官运动是十亿年进化的深层,推理是薄薄的表层 | 关于世界的信息在人体最便宜、动作必须在机体执行,差价是中央税;税按接触梯度分布 |
| **X3 原子三不可逆** | 控制论实时反馈 + Ashby | 1943/56 | 负反馈必须在墙钟时间内闭环;"only variety can destroy variety"(Ashby 1956) | 动作有串行时间地板、错误不可逆、1kHz 安全环禁云 |
| **X4 时钟分层律** | Brooks 包容架构 | 1986 | 分层反应行为,高层抑制低层,无中央世界模型 | 慢层管语义/快层管运动/反射层管安全;三个时钟被物理钉死 |
| **X5 双时钟相位差** | (无直接祖先;Kuhn 范式弧 + 苦涩教训的时间维) | — | 苦涩教训的"long run"是隐含的时间尺度 | 能力按研究钟(月级)、部署按工业钟(年级),相位差 2–4 年 |
| **X6 计量-柠檬统一律** | Lighthill 报告(可验证性危机的祖先)+ PSSH 的"empirical inquiry" | 1973/76 | Newell&Simon:"one can attack or defend it only by bringing forth empirical evidence" | 瓶颈只在有计量单位+第三方尺子时才成市场;度量被私有化 |
| **X7 要素禀赋镜像** | (无学术祖先;纯产业地理经济) | — | — | 中美各自套利本地最便宜要素;一个模式的两半 |
| **X8 定价权拓扑** | (无学术祖先;产业组织理论) | — | — | 定价权只在物理卡点/生态锁定/一体化成本领先三处 |

**两处最锐利的映射,展开:**

**X2 = Moravec 1988 被货币化。** Moravec 1988 年的原话(《Mind Children》pp.15–16):"我们在感知和运动领域都是了不起的奥林匹克选手,好到让难事看起来容易";抽象思维"是个新把戏,也许不到十万年,我们还没掌握"。Brooks 1990 年给出进化经济学解释:感官运动能力用了近 35 亿年进化 R&D 在硬生存选择下打磨,符号推理只有几千年——所以 AI 先到棋类后到灵巧是**注定的**。而 Pinker 1994 年的名句"难的问题是容易的,容易的问题是难的"——**这句最常被当作 Moravec 原话的,其实是 Pinker 的转述,不是 Moravec 说的**(语料外事实核查,已标)。X2 做的,是把这个四十年"悖论"从一句观察升格为一条**会计恒等式**:感官运动信息为什么难?因为它便宜地存在于人体、昂贵地必须在机体执行,差价就是税。Moravec 说"感知难",X2 说"感知的数据要付工资,而工资不服从摩尔定律"——**悖论第一次变成一个成本项,可以入账、可以对冲、可以证伪**(video-only 接触突破若成立,税崩)。

**X4 = Brooks 1986 穿 VLA 外衣。** Brooks 1986 年包容架构:分层反应、高层抑制低层、每层各自完整、无中央世界模型。当年被符号 AI 视为倒退(没有规划、没有表征)。四十年后,五家互不通气的前沿系统(Figure Helix 三层、NVIDIA GR00T 双层、PI 双流、DeepMind 云-端拆分、连要推翻这一切的 LeCun 的模块栈)全部长成"慢层管语义/快层管运动/反射层管安全"的**同一形状**([on-device-brain](on-device-brain.md))。**区别在一处:** Brooks 反对中央世界模型,而今天每家的**顶层**恰恰是一个大世界模型/VLM。所以 X4 不是纯粹的 Brooks 胜利,是"Brooks 的**架构形状**赢了(分层反应),Brooks 的**反表征教条**输了(顶层是大模型)"——包容架构平反,但戴着它当年反对的帽子。

**诚实裁决:哪个学派 2026-07 正在赢,凭什么,什么会翻盘。**

以 2026 年 7 月的语料证据,**弱版具身认知(Brooks/形态计算)正在赢,强版具身认知(生成认知/构成性)既没赢也没被证伪,而符号接地问题以经济学而非哲学形式复活。** 具体:

- **弱版赢的证据:** locomotion 被仿真里无身体地解决(形态+物理承担计算,McGeer 平反);五家 VLA 全是分层反应(包容架构平反);"世界是自己最好的模型"在闭环再感知 vs 离线模型的对比里持续可测。
- **去身派也赢了一半:** RT-2 证明零具身互联网知识**能**迁进身体,Sutskever"具身非必要"没被证伪——离身预训练+薄接地这条路确实奏效在自由空间和语义层。
- **强版具身认知悬空:** 生成认知的"去身系统在做另一件事"是构成性主张,今天无法用基准证伪(一个 VLA 分数再高,enactivist 也会说它没有真正 enact 一个世界)——这不是证据不足,是主张本身设计成难证伪的([lineage-embodied-cognition](lineage-embodied-cognition.md) §3)。
- **符号接地以经济学复活:** Harnad 的"符号如何接地"在今天变成"接地要付多少工资"——X2 具身税。哲学难题降格为会计科目。

**什么结果会翻盘(dethrone 条款,带到期日):**

- 若到 **2027-12**,video-only(V-JEPA 类)在**接触任务**上以 <100h 动作数据追平 10× 遥操语料并被第三方复现([physical-ai-essence](physical-ai-essence.md) X2 哨点)——则**去身派大胜、弱版具身认知的"接触必须真身体"崩**,Moravec 悖论的接触半边被规模攻破。
- 若到 **2028-12**,接触富任务出现第三方复现的 sim-to-real、无需真机修正——则 X3"不可 Ctrl-C"从物理降级为工程,**苦涩教训在灵巧上也赢**,强版具身认知失去最后的经验庇护所。
- 反过来,若到 **2029-12** 前五 VLA 无一家能把新增训练数据过半转成部署机队自采、且部署仍呈 AV 式逐站点工程——则**去身路线的"薄接地"被证伪**,X1 技能资本化降格为营销叙事,X2 登基,本质从"技能变资本"退回"永远在缴具身税的自动化"。

---

## 5. 对我们的含义 (so what)

学术史给我们的设计栈([physical-ai-essence](physical-ai-essence.md)/[data-engine-v2](data-engine-v2.md))添了产业分析给不了的三样东西:

1. **区分"70 年未决悬案"和"已定科学"。** 产业分析把所有 X-pattern 平铺成"当前约束";学术史告诉我们哪些是**七十年反复摆动、这次才第一次能实验裁决的开放问题**(X2 具身税=Moravec 悖论的接触半边,D4/D5 未判),哪些是**已经收敛的工程事实**(X4 分层=控制论实时约束+包容架构,基本已定)。含义:凡挂在"未决悬案"上的收入线(器械溢价、力通道)必须按**期权**定价并绑到期日;凡挂在"已定科学"上的(端侧大脑、分层数据目录)可按稳态定价。

2. **钟摆的下一摆落点是可预判的。** 学术史的节律说:每一摆都在**上一摆最自信的地方**撞墙(符号 AI 撞在常识、深度 RL 撞在数据、LLM 可能撞在接触物理)。所以下一个瓶颈大概率不在今天喊得最响的地方(算力、模型),而在今天被系统性忽略的地方——**力/触觉**(前沿 VLA 无一把触觉当一等输入,[open-problems](open-problems.md)/[tactile-hands](tactile-hands.md))。这直接支持我们 CORE-R design-in(传感头长进部署 BOM)从选项升格为战略主线。

3. **给我们的策略一个七十年的压力测试。** 我们把 X1 技能资本化放在本质王座上;学术史提供了它的**替代世界**:若资本化不发生(去身接地失败),本质退回 X2"永远缴具身税的自动化"——而那个世界里,卖税务工具的(器械商、一体化本体厂)反而是终局赢家。**两个世界都利好我们的器械生意**,但理由相反:资本化世界里器械是过渡期(相位差)的生意,缴税世界里器械是永久生意。学术史逼我们把这两种未来都写进 watchlist,而不是押单边。

---

## 6. 观察哨 — 正在运行、将裁决世纪悬案的实验(带日期)

| 到期 | 实验 | 裁决哪个世纪悬案 | 学派含义 |
|---|---|---|---|
| 2027-12 | video-only 接触任务以 <100h 动作数据追平 10× 遥操语料(第三方复现) | Moravec 悖论的接触半边能否被规模攻破 | 成立→去身派大胜、Moravec 1988 的接触半边失守;不成立→弱版具身认知续命 |
| 2027-12 | 同技能权重跨 ≥2 本体类 OTA + 第三方验证 | Schaal 1999"技能能否自举成通用"的资本化版 | 成立→X1 技能资本化坐实;不成立→资本化降格营销、X2 登基 |
| 2027-06 | 登顶 RoboArena/GM-100 的新架构是否仍 ≥2 时钟层 | Brooks 1986 包容架构 vs 单一大模型 | 仍分层→X4/包容架构续命;单时钟单模型直出 ≥50Hz→X4 被击穿、Brooks 形状也输 |
| 2028-12 | 接触富任务第三方复现 sim-to-real、零真机修正 | 苦涩教训能否在灵巧上也赢(D4) | 成立→X3 降级、强版具身认知失去经验庇护;不成立→"接触要真身体"续命 |
| 2028-2029 | VLA 与世界模型是否合流为单一 world-action 架构(D5) | LeCun JEPA vs 自回归谁成主导设计 | 合流→X4 收编律成立(各赢一层);单方全胜→路线战争有全胜先例 |
| 2029-12 | 前五 VLA 任一家新增训练数据过半来自部署机队自采 | 去身"薄接地"路线的终局 | 过半→资本化闭环、去身路线胜;仍靠新采示范→接地税永续、X2 本质坐实 |

---

## Sources

**血脉一(控制论·符号 AI·批评者)——本页所用为独立研究dossier的一手核查(存于 scratchpad/lineage1/),主要一手作品:**
- Rosenblueth, Wiener, Bigelow, "Behavior, Purpose and Teleology," *Philosophy of Science* 10(1), 1943, pp.18–24 — 一手全文提取(JSTOR 扫描)。
- Wiener, *Cybernetics: or Control and Communication in the Animal and the Machine*, MIT/Wiley, 1948 — 副标题为一手;书内页码措辞标 (unverified)。
- Ashby, *An Introduction to Cybernetics*, 1956 / "Requisite Variety and its Implications," 1958 — 必要多样性定律一手 PDF;Ashby 原话为 "only variety can destroy variety"(1956);"only variety can absorb variety" 系 Stafford Beer 转述,本页已纠。
- W. Grey Walter, *The Living Brain*, Norton, 1953;"An Imitation of Life," *Scientific American*, 1950-05;电子龟 1948–50 — 建造与论文日期 (secondary);"两个神经元等价物"表述见于多个二手转述("the equivalent of two functioning neurons"),原文确切措辞未一手核到,本页已降格为转述。
- McCarthy, Minsky, Rochester, Shannon, Dartmouth 提案(1955-08-31)— 一手,coined "AI"。
- Newell & Simon, "Computer Science as Empirical Inquiry: Symbols and Search," *CACM* 19(3), 1976, pp.113–126(PSSH,图灵讲座)— 原文为 "general intelligent action"(p.116),本页表格已用全词;Nilsson 2007 转引漏 "general",该漂移已纠。
- SRI Technical Note 323, *Shakey the Robot*(1984,编录 1966–72 报告)— 一手全文提取;规划耗时"数小时"为 (secondary)。
- Dreyfus, *What Computers Can't Do*, Harper & Row, 1972 — 1972 原文 Monoskop 403 不可及,主张经 Nilsson 引 Dreyfus 2006 重述核对 (secondary/high-confidence)。
- Lighthill, *Artificial Intelligence: A General Survey*, UK SRC, 1973 — 部分一手(aitopics.org)。
- Searle, "Minds, Brains, and Programs," *Behavioral and Brain Sciences* 3(3), 1980, pp.417–457 — 中文屋原文;公理句 "Syntax by itself is neither constitutive of nor sufficient for semantics" 出自 Searle, "Is the Brain's Mind a Computer Program?" *Scientific American* 262, 1990(公理 3),本页已纠归属年份与全文措辞。
- Harnad, "The Symbol Grounding Problem," *Physica D* 42, 1990, pp.335–346 — 问题陈述双源核对。
- Moravec, *Mind Children*, Harvard UP, 1988, pp.15–16 — "prodigious olympians" 一手带页码;根源更早见 Moravec 1984 "Locomotion, Vision and Intelligence"(Brooks 1990 引为 [26])。
- **Pinker, *The Language Instinct*, 1994** — "the hard problems are easy and the easy problems are hard" 属 Pinker 转述,**非 Moravec 原话**(本页显式纠误)。
- Minsky, *The Society of Mind*, 1986 — "we're least aware of what our minds do best" (secondary)。
- Brooks, "Elephants Don't Play Chess," *Robotics and Autonomous Systems* 6, 1990, pp.3–15 — 一手全文提取(物理接地假说、进化时间线、"world is its own best model")。

**血脉二·三——本 wiki 已核页面(一手核查见各页 Sources):**
- [lineage-embodied-cognition](lineage-embodied-cognition.md) — Brooks 1986/90/91、Gibson 1979、Varela/Thompson/Rosch 1991、Maturana&Varela 1972/80、McGeer 1990、Braitenberg 1984、Thelen&Smith 1994、Friston 2010、Lakoff&Johnson 1980/99;Brooks 2019/2023 博文("A Better Lesson"、"GPT is the Chinese Room")。
- [lineage-learning-control](lineage-learning-control.md) — Kalman 1960、Raibert 1984/86、Sutton TD 1988 / Bitter Lesson 2019 / Dyna 1991、Schaal 1999、DAgger 2011、Levine et al. 2016、Tobin et al. 2017、RT-2 2023(VLA 命名)、Ha&Schmidhuber 2018、Smith&Gasser 2005、Sutskever 2022。

**本 wiki 交叉引用页(X-pattern 映射与今日证据):**
- [physical-ai-essence](physical-ai-essence.md)(X1–X8 本质 pattern,本页映射其学术祖先)、[history](history.md)(工业时间线,本页不重复)、[visions](visions.md)(今日领袖论点=老论战最新一轮)、[lecun-worldmodels-rethink](lecun-worldmodels-rethink.md)(D5)、[locomotion](locomotion.md)、[manipulation](manipulation.md)、[open-problems](open-problems.md)、[tactile-hands](tactile-hands.md)、[on-device-brain](on-device-brain.md)、[data-scaling-strategy](data-scaling-strategy.md)、[data-engine-v2](data-engine-v2.md)。
</content>
