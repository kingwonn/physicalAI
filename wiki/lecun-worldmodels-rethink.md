---
title: LeCun 世界模型论纲 vs 数据引擎方案 (LeCun World Models vs Our Data Engine)
slug: lecun-worldmodels-rethink
updated: 2026-07-07
confidence: verified
---
> Yann LeCun 于 2026-05-29 在 ETH Zürich「Robotics, Systems, and Control Seminar / Frontiers of Embodied AI」发表 **"World Models: Enabling the next AI revolution"**——活动、日期、视频链接均由 LeCun 本人社交帖直接确认(primary),但**本页未能取得逐字讲稿:内容重建自两篇独立二手评述 + 与会者帖 + 他 2026 年其他场合(Brown、Davos、播客)的同主题原话,凡属此类均已标注,ETH 讲内原话一律按 (secondary) 处理**。论纲的核心挑战直指本 wiki 的[数据引擎路线图](data-engine-roadmap.md):如果 JEPA 式潜空间世界模型用海量**被动视频**预训练、只需 <62 h 动作数据即可零样本操作,那么围绕「动作标签小时数 × 精度阶梯」组织的采集引擎是否在为一个将被跳过的范式建厂?**一行判词:LeCun 的论纲修正了我们的权重、没有击穿我们的骨架——他自己的旗舰结果(V-JEPA 2-AC 仍需 62 h 机器人动作数据、无力觉通道、65–80% 成功率)恰好落在我们 W/L/R 脊柱的下游收口处;最大的改动是把 W1e 被动视频从防御性副 SKU 升格为带自有保真度规格的第一产品线。**

## 1. 演讲核心思想 (the talk, faithfully)

**事件本体(primary,LeCun 本人帖):** 2026-05-29,ETH Zürich ML 楼 D28,「Frontiers of Embodied AI」四场特邀讲之一(同台:Koltun / Malik / Shuran Song);视频 youtube.com/watch?v=72Xj8k5WQX4,讲稿 PDF 由 LeCun 本人挂 Google Drive(链接见其帖)。注意:主办方是 ETH Future Computing Laboratory(EFCL),**并非**"ETH AI Center 主办";活动页(14:00–18:30, ML D28)与 LeCun 帖相互印证。以下论证链按二手评述(StartupHub.ai 2026-06-10;erogol substack 2026-06-12,最实质的一篇)重建:

- **① LLM 批判 / Moravec 悖论 (secondary)。** LLM 在语言任务上惊艳,但对物理世界无理解;自回归逐 token 预测没有内部世界模拟,无法评估行动的物理后果。标志性说法:四岁儿童经日常感官接触的数据量与习得的世界知识超过最大的语言模型(secondary,StartupHub 概述,**非逐字引语**;此为 LeCun 多场合惯用论点)。同一逻辑他在别处推到安全论:代理化 LLM「**intrinsically unsafe**」,因为无法预测行动的实际物理后果——此句出自 Unsupervised Learning 播客(2026-05-18 发布),**非 ETH 现场** (secondary)。
- **② 数据效率论 (secondary,内部有张力)。** 「17 岁少年十几个小时学会开车」(播客,secondary;erogol 记录的演讲版本为「~20 小时」);同时演讲重申其惯用的「感官带宽 ≫ 文本」换算(erogol 评述引 Koch et al. 2006 视网膜 ~10 Mbit/s 复核同一量级)——评述者(erogol)直指这两条互相打架:按原始感官量算,4 岁儿童已处理 ~1,500 亿视觉帧,诚实的表述是「更少的**标注**数据」而非「更少的数据」。听众 (LinkedIn) Jonathan Sandhu 独立给出同一反驳:人类一生感官数据与 LLM 文本训练量**同为 ~10¹⁴ 字节量级** (secondary)。
- **③ 目标驱动架构 (secondary,与其 2022 立场论文一致)。** 模块化:感知 + 记忆 + 世界模型 + actor + 目标/成本函数;世界模型在**潜空间**预测动作条件化的未来状态(JEPA 族:I-JEPA → V-JEPA → V-JEPA 2 → LeJEPA),刻意丢弃不可预测的像素细节,而非生成式逐像素预测。
- **④ 规划 = 潜空间 MPC (secondary,erogol 确认)。** 用学习到的世界模型做 model-predictive control(带 guardrail 目标/成本函数)/ 能量函数优化,替代自回归 token 生成——erogol 评述明确将「MPC + guardrail objectives」列为演讲主论点之一。
- **⑤ 实证弹药 (secondary)。** V-JEPA 对物理不可能视频表现出「violation-of-expectation」反应(物体恒存/固体性/重力),被引为无标签习得直觉物理的证据;**LeJEPA/SIGReg**(各向同性高斯正则)作为新技术贡献展示,评述者注明 LeCun 自曝其弱点(经验信息度量只是上界)——罕见的诚实,加分。
- **⑥ 机器人论断 (secondary,播客非 ETH)。** VLA 模型「basically now being seen as a failure」;现范式 scaling 是通往物理智能的「dead end」;范式转移的必要性将「completely obvious to people by early 2027」。**再次强调:这三句出自播客,不能当 ETH 现场引语使用。**
- **⑦ AMI Labs 语境。** 离开 Meta(2025-11-19 官宣,被置于 Alexandr Wang 之下;他形容 Meta 新组织「completely LLM-pilled」,并称「我离开 Meta 是因为他们也 LLM-pilled 了」)→ 创立 AMI Labs(巴黎;LeCun 任执行主席而非 CEO),**$1.03B 种子轮 @ $3.5B pre-money(2026-03-09 官宣)**,Cathay Innovation/Greycroft/Hiro/HV/Bezos Expeditions 共同领投,NVIDIA/Samsung/Temasek/丰田等跟投;CEO LeBrun 自陈「世界模型从理论到商用可能要数年」,报道口径 ~5 年无可售产品;首个落地方向是医疗(Nabla),而非机器人 (secondary,多源一致)。演讲即是这套融资论纲的学术版路演——这不构成反驳,但构成利益语境。

## 2. 论纲与我们证据链的对撞 (collision with our evidence chain)

| # | LeCun 论断 | 我们已验证的证据 ([data](data.md) / [world-models](world-models.md)) | 今天谁的证据硬 | 判定实验 |
|---|---|---|---|---|
| 1 | VLA/模仿 scaling 是 dead end,「已被视为失败」(播客, secondary) | GEN-0 幂律 **270k h 未饱和**(+10k h/周);EgoScale 对数线性(1k→20k h 灵巧度翻倍);清华 ICLR 2025 环境多样性幂律;π0.5 在**从未见过的家庭**完成长时程任务;GR00T N1 数据效率曲线(10% 数据 42.6% vs DP 10.2%) | **我们**——三条独立测得的 scaling 曲线 vs 一句修辞;但 RoboChallenge π0.5 均值仅 43.7%、任务间 0–100% 方差(两个任务 100%、多个任务 0%),说明"scaling 正在赢"≠"scaling 已够用" | GEN-0 曲线在 1M h 处是否弯折;π 系 2027 年可靠性是否过 95% |
| 2 | 人类数据效率证明架构缺陷 | 双重独立反驳(Sandhu 10¹⁴ 字节对等;erogol 1,500 亿帧)——人类优势在**无标签感官流**,不在总量 | **平局偏我们**——但注意:这条反驳**恰好支持被动视频 scaling**,即 EgoScale/Go-Big 路线,也支持 LeCun 的预训练主张 | 无需实验;两边在"被动视频有巨大价值"上其实同向 |
| 3 | JEPA 潜空间预训练 + 极少动作数据即可操作(V-JEPA 2-AC:>1M h 视频 + **<62 h** DROID → 零样本 65–80% 抓放,报告碾压 Cosmos 0–20% 与 Octo ~15%) | 我们页内已录:**Octo 是 2024 年弱基线**,严谨对照应是 π0.5/GR00T/Helix;65–80% 抓放 ≈ VLA 阵营 2024 年水平;无接触密集/插装结果;无力觉 | **各赢一半**——预训练数据效率 LeCun 赢;绝对操作能力与任务广度 VLA 阵营赢 | 同基准同任务 JEPA-AC vs π0.5 头对头(至今无人做,RoboChallenge 是现成擂台) |
| 4 | 世界模型应预测潜变量而非像素;「别做生成式世界模型」(erogol 转述并反驳;劝退式论断,非"没人在做") | 我们的四角色分类:**数据引擎角色必须出像素**(DreamGen 22 新行为/10 新环境、240k 神经轨迹对数线性;Cosmos Transfer 域倍增)——V-JEPA 无像素,当不了数据工厂;DreamerV3/Genie 3 是「别做生成式」劝退论的现成反例 | **我们**——潜空间 vs 像素是**分角色互补**,不是路线战争 | Cosmos Policy(LIBERO 98.5%)类 WAM 与 JEPA-AC 在同一操作套件对比 |
| 5 | 世界模型 MPC「intrinsically safe」,不可越狱 | erogol:成本函数照样可被博弈;我们的证据:可靠性来自**部署期修正数据**(π*0.6/RECAP 干预+结果标签),不来自架构先验;世界模型自身有幻觉→坏动作→更 OOD 的恶性循环(MiraBench) | **我们**——"架构即安全"无实证,RECAP 有部署曲线 | AMI 系统上线后的实际干预率/事故率数据 |
| 6 | 被动视频足以学到直觉物理 → 动作标签价值塌缩 | Helix S1 **200 Hz** 动作专家需 ≥200 Hz 标签(现语料 15–50 Hz 已是插值天花板);力/触觉信号**不在视频里**;V-JEPA 2-AC 自己也要 62 h 动作数据收口 | **分层各对**——见下 | 我们新增的 pretrain-vs-label 消融(§4) |

**「两边都对、只是不在同一层」的诚实读法:** 把 LeCun 架构映射到我们的 [S2/S1/S0 分层](on-device-brain.md)——**世界模型预训练吃 S2**(语义/物理常识,被动视频的主场,他基本对);**动作标签微调吃 S1**(50–200 Hz 视觉运动,视频给不了 200 Hz 力控标签,我们对);**RL 修正吃 S0/可靠性**(他的框架里干脆没有部署飞轮这一层,我们对)。2025–2026 每一个前沿系统——V-JEPA 2-AC(1M h 视频 + 62 h 动作)、1X NEO(900 h 人类视频 + 70 h 本体微调 + 400 h 逆动力学)、GR00T(数据金字塔)、π0.5(网络数据 + 400 h 移动操作)——都是**同一张三层配方**,差别只在预训练目标函数。LeCun 的「世界模型 vs VLA」二分法比技术现实更锋利;文献潮流(World-Env、DriveVLA-W0「世界模型**放大**而非替代 VLA 数据 scaling」、WMPO、VLAW)是融合而非替换。

## 3. 对 LeCun 的批判性评估 (critique of LeCun)

**先立钢人 (steelman)。** 他有三张真牌:(1) **潜空间预测在表征学习上实证胜出**——V-JEPA/I-JEPA/DINOv2 系确实优于像素重建系(MAE),erogol 这样的批评者也承认;(2) **样本效率差距是真的**——人类 ~20 h 学会驾驶 vs AV 系统百万小时,这是所有阵营都得解释的事实;(3) **JEPA 谱系在快速兑现**:V-JEPA 2-AC 零样本操作(2025-06)→ DINO-WM 零样本规划(LeCun 合著)→ LeWM 15M 参数单 GPU 数小时训练、规划提速 ~47×(2026-03, arXiv 编号 (unverified))——方向是**更小更快**,这反而说明他不是在讲"世界模型也要大力出奇迹"的故事。此外,他公开自曝 SIGReg 的理论弱点,以及「我没有发明世界模型,Jürgen 也没有;真问题是怎么让它在非平凡任务上工作」(secondary 转述其自辩原话,回应署名权争议)——比多数同级大佬诚实。

**预测记录(有日期的)。** 有利:2022–2024 持续断言纯文本 LLM 无法获得稳健物理/空间推理——2026 年前沿模型在此仍然偏弱,方向性正确 (secondary, synthesized)。不利:(a) 「GPT-5000 永远推不出推桌子会带动桌上的书」类论断被后来的多模态推理模型处理掉——**单一聚合源,(unverified)**;(b) 2024-06「读博别做 LLM」——此后两年恰是 LLM 骨架 VLA(π0/π0.5/Helix/GR00T)交付实体机器人能力最快的两年,时点错了;(c) Gary Marcus 2024-06 公开信指其立场(需要世界模型、LLM 常识肤浅、需要模块先验)是对 Marcus 2018–2019 论点的渐进收编——署名权层面有争议,但记录了其立场漂移;(d) erogol 四连击:「不可越狱」过度、「不在 token 空间推理」被 DeepSeek-R1 反例、「别做生成式世界模型」被 DreamerV3/Genie 反例、「学术界别做 LLM」被 DPO/FlashAttention/RLHF(皆出自学术界、皆在 scale 时代之后)反例——**模式:实证工作扎实,配套修辞系统性过度延伸**。

**利益语境。** 演讲发生在 $1.03B 种子轮官宣后 11 周;估值 $3.5B 在公司成立前就已被放风(Fortune 2025-12-19);承诺 ~5 年无产品;首个落地是医疗文书(Nabla)而非机器人——**一个正在按此论纲融资的人,其"VLA 已失败"的断言应打上折扣系数**。这不否证论纲,但意味着"对手范式已死"部分是路演修辞。

**他系统性低估的三件事(与我们引擎直接相关):**
- **力/触觉是视频伪造不了的信号。** >1M h 互联网视频里没有一牛顿的力标签;插装 0.1–1N 力控窗口、滑移预测、200 Hz 冲击瞬态——世界模型可以「想象」接触,但校准想象所需的 ground truth 恰是我们 Gen-2 力-振动数据「卖两次」的第二买家(sim 接触校准)。LeCun 框架里此通道为空白。
- **最后一公里可靠性数据。** 从 60–80% 到 99.9% 的爬坡历史上从不来自更好的预训练,而来自部署期干预/修正(RECAP 型);他的架构叙事终止在"会规划",没有飞轮层。
- **他自己配方的收口。** V-JEPA 2-AC 的 62 h DROID 数据就是**动作标签微调**——被他贬为失败的范式,以缩小版嵌在他的旗舰结果里。62 h 不是零;而且那 62 h 恰好得是高质量、同步干净的动作数据——**谁生产这 62 h?我们这种引擎。**

## 4. 方案再思考 (the rethink — what changes in OUR roadmap)

对照 [data-engine-roadmap](data-engine-roadmap.md) 逐层裁决:

### 4.1 原封不动的部分 (survives untouched)

- **力通道 Gen-1 上人手、触觉逐代加密。** LeCun 论纲不仅没触及,反而**抬价**:世界模型预训练把视觉-语义监督变便宜后,视频里没有的信号(力/振动/触觉)成为语料里最稀缺的维度;「力数据卖两次」新增第三买家——世界模型实验室需要真实接触瞬态校准其想象的物理。
- **单时钟公理、无软件时间戳、保真度 SLA 证书。** 范式无关:无论下游是 VLA 微调还是世界模型动作条件化,时间戳纪律都是标签质量的地板(世界模型的动作条件化保真度差,正是 MiraBench 抓出的病灶之一)。
- **R 系修正飞轮(月 3 启动)。** LeCun 框架的空白层;RECAP 证据未被挑战。若世界模型真把"会做"变便宜,可靠性数据在总价值中的占比只会**更高**——Gen-3 混合体向 R 系倾斜(30/25/45)的逻辑被加强而非削弱。
- **L 系计量职能 + 双源供应链 + 月 9 精度门禁的"先证伪后花钱"纪律。** 与范式之争正交。

### 4.2 重新加权的部分 (re-weighted)

- **W1e 被动头戴 SKU:从防御到主力。** 原案里 W1e 是对 $371 UMI 克隆的走量应答($350,"被动 6 h/天"副产品定位)。LeCun 论纲 + EgoScale + V-JEPA 2 的 1M h 视频胃口共同指向:**被动第一视角视频是世界模型时代涨价最快的资产**。改动 (设计目标):W 系内部拆出**被动:主动双轨配额**,Gen-1 从"副产品"改为明确目标(如 W 系小时数的 ~25% 为被动 ego 流,Gen-2 升至 ~40%);W1e 升级规格——加校准深度/双目、更高帧率、IMU 硬同步,使每帧带**度量尺度 ego-motion**(见 4.3 新产品)。混合体记法从 W/L/R 三元扩为 **W(主动)/W(被动)/L/R 四元**,Gen-2 参考配比 45/15/25/15 (设计目标)。
- **精度 capex 论点:2mm 门更重要而非更不重要。** 若世界模型吃掉 S2 和 S1 粗段,动作标签总需求量可能下降,但**单位动作标签的价值密度上升**(62 h 收口数据必须干净;插值伪影在小数据量微调里伤害更大)。原案的 6mm-vs-2mm 消融(数据科学评委钦点"最重要单个实验")地位不变,但其解读框架变了:它现在同时是"精度值不值钱"和"动作标签在新范式下值多少钱"的联合测试。月 9 门禁保留。
- **hours-ladder 叙事微调。** Gen-2 40 万 h 目标不变,但其中被动小时的边际成本(~$1/h 级,众包头戴)远低于主动采集,同预算下**总小时数可上修、动作标签小时数可下修**——精确配比交给 4.3 的新消融,不拍脑袋。

### 4.3 新增的部分 (added)

- **新门禁实验:世界模型预训练 vs 动作标签消融(与 6mm/2mm 消融并列)。** 固定下游任务集与预算:(a) V-JEPA 2 类潜空间预训练 + X h 我方 W1 动作数据微调,vs (b) 纯动作数据 3X h,vs (c) 像素世界模型(Cosmos 类)预训练 + X h。测下游成功率交叉点。**裁决规则:若 (a) 在 X ≤ 100 h 处追平 (b) 的 10× 数据量——原风险 3(b) 判据触发——被动双轨配额立即再上调一代,W 主动系退守接触密集任务专供。** 这把原来风险清单里的被动条款变成我们自己跑的主动实验。
- **新数据产品线:世界模型级 ego 语料规格 (设计目标)。** 世界模型训练对视频的要求 ≠ VLA 预训练:需要**度量尺度深度 + 帧级 ego-pose + 内参标定**(动作条件化的"动作"就是相机运动)、**长时程不剪切片段**(现役模型 rollout 一致性 ≤30 s–分钟级,长时程真值稀缺)、**同场景多结局覆盖**(反事实相邻:同一操作的成功/失败/异常分支,配我们 R 系的结果标签体系)、**物理密集事件**(碰撞/形变/流体,配接触麦克风与力通道 → sim/世界模型物理校准双卖)。我们的 per-episode 质量证书顺势扩展一项:**ego-pose ATE 证书 = 世界模型动作条件化保真度证书**——把 AMI Labs、NVIDIA(Cosmos 数据管线)、1X(世界模型实验室)登记为脊柱的新买家类别,而非竞争者。
- **新观察义务:** 每季度对 JEPA-AC 系与 π 系在公开基准(RoboChallenge 类)上的头对头保持跟踪,作为混合体季度调度(既有机制)的新输入信号。

### 4.4 修订后的底线 (revised bottom line)

三代路线图**成立**:Gen-1/2/3 的硬件阶梯、精度门禁、终局判据全部保留;W/L/R 脊柱的"可转向不陪葬"性质恰好是对范式不确定性的正确对冲——这正是当初选 C 案骨架的理由,LeCun 情景只是它要对冲的情景之一。**唯一的一句话最大改动:被动第一视角视频从防御性副 SKU 升格为带自有保真度规格(度量深度 + ego-pose 证书)的共同主力产品线,使同一条数据脊柱同时供货 VLA 阵营与世界模型阵营——范式之争打得越凶,中立军火商越贵。**

## 5. 观察哨 (watch items)

- **2027-03 前:** LeCun 的「early 2027 完全显然」预言到期——若届时 VLA 阵营(π/Figure/GR00T)商业部署继续扩张且无公开范式撤退,该预言证伪;记录在案 (secondary)。
- **2026-12 前:** AMI Labs 首个技术发布(LeWM 放大版?)——是否在**任何**操作基准上与 π0.5/GR00T 同台;若继续只发 Push-T 级玩具任务,"5 年无产品"折扣系数上调。
- **2026-12 前:** 我方两个门禁实验(6mm/2mm 精度消融 + 新增 pretrain-vs-label 消融)出数——这是本页 4.2/4.3 全部量化配比的裁决者。
- **2027-06 前:** 是否出现 video-only 预训练 + <100 h 动作标签追平 10k h 级动作语料的公开复现(原路线图风险 3(b),现为主动实验)——触发即被动配额再上调。
- **2027-06 前:** JEPA 潜空间系 vs 生成像素系(Cosmos 3 WAM / Cosmos Policy)在同一操作套件的头对头——决定世界模型阵营内部哪支需要我们的哪种数据(潜空间系要动作收口数据,像素系还要长时程视频)。
- **持续:** GEN-0 幂律是否在 500k–1M h 段弯折(Generalist 周更速率公开可推算)——弯折 = LeCun 的天花板论获得第一个真实证据点,我方 hours-ladder 需重排。
- **持续:** V-JEPA 2-AC 的 62 h 收口数据量在后继版本(V-JEPA 3?)是否趋零——若降到 <5 h 或纯自监督,动作标签价值论需二次重估;若不降反升(任务变难),我们的判断获证。
- **2027-12 前:** 是否有第三方开始为世界模型训练数据发布质量/标定规格(我们 4.3 产品线的竞品信号);无人做 = 我们的空窗期红利。

## Sources

- https://www.facebook.com/yann.lecun/posts/10162289117682143 — LeCun 本人确认 ETH 演讲日期/系列/视频链接 *(primary)*
- https://www.linkedin.com/posts/yann-lecun_yann-lecun-world-models-enabling-the-next-activity-7470235759082405888-hgXQ — LeCun LinkedIn 转发;评论区反驳(Sandhu 10¹⁴ 字节)*(primary 帖 / secondary 评论转述)*
- https://www.youtube.com/watch?v=72Xj8k5WQX4 — 演讲视频(本页未能解析音频,内容未直接核对)*(primary artifact, content unextracted)*
- https://efcl.ethz.ch/events/conferences---workshops/frontiers-of-embodied-ai.html — 活动页:2026-05-29,ML D28,四讲者 *(primary)*
- https://erogol.substack.com/p/lecuns-world-models-talk-what-holds — 最实质的技术评述(2026-06-12):LeJEPA/SIGReg、四点反驳、1,500 亿帧论证 *(secondary,单一但高质量)*
- https://www.startuphub.ai/ai-news/artificial-intelligence/2026/yann-lecun-on-world-models-and-the-ai-revolution — 演讲内容新闻转述(Moravec、四岁小孩)*(secondary)*
- https://www.humanoidsdaily.com/news/yann-lecun-predicts-paradigm-shift-in-robotics-by-2027-dismisses-llms-as-intrinsically-unsafe — 播客引语:VLA「failure」、「early 2027」、「intrinsically unsafe」——**非 ETH 现场** *(secondary)*
- https://fortune.com/2026/01/23/deepmind-demis-hassabis-anthropic-dario-amodei-yann-lecun-ai-davos/ — Davos 三方交锋(LeCun/Hassabis/Amodei)*(secondary)*
- https://www.brown.edu/news/2026-04-01/yann-lecun-artificial-intelligence-pioneer — Brown 讲座(同期同题材)*(primary-ish 校方)*
- https://garymarcus.substack.com/p/open-letter-responding-to-yann-lecun — Marcus 公开信:立场收编论 *(primary 信件本体/立场有偏)*
- https://www.edtechinnovationhub.com/news/6dsnebjgpjgww53zs5fyghm4mhxayb — 世界模型署名权争议 + LeCun 自辩原话 *(secondary)*
- https://x.com/ylecun/status/1796982509567180927 — 2024-06「别做 LLM」原帖 *(primary)*
- https://techcrunch.com/2026/03/09/yann-lecuns-ami-labs-raises-1-03-billion-to-build-world-models/ — AMI $1.03B @ $3.5B pre;五家共同领投 + NVIDIA/Samsung/Temasek/丰田跟投;CEO LeBrun 时间线引语;首个落地医疗(Nabla) *(secondary,多源一致)*
- https://fortune.com/2025/12/19/yann-lecun-ami-labs-ai-startup-valuation-meta-departure/ — 成立前 $3.5B 估值放风 *(secondary)*
- https://techcrunch.com/2025/11/11/metas-chief-ai-scientist-yann-lecun-reportedly-plans-to-leave-to-build-his-own-startup/ — 离职报道链起点;LeCun 2025-11-19 本人官宣 *(secondary + primary 帖)*
- https://arxiv.org/abs/2601.16163 — Cosmos Policy:LIBERO 98.5% 均值(Spatial 98.1 / Object 100 / Goal 98.2 / Long 97.6),超 π0.5 96.9% *(primary)*
- https://arxiv.org/abs/2506.09985 — V-JEPA 2/V-JEPA 2-AC:1M h 视频 + <62 h DROID、零样本 65–80%、vs Cosmos/Octo 对照 *(primary)*
- https://arxiv.org/abs/2411.04983 — DINO-WM(LeCun 合著,零样本规划)*(primary)*
- https://arxiv.org/html/2603.19312v1 — LeWM:15M 参数、~47× 规划提速(arXiv 编号 (unverified))*(primary-adjacent)*
- https://activemodels.ai/v-jepa-2-and-the-rise-of-world-models-a-practical-guide-for-robotics-and-agents/ — V-JEPA 2-AC vs Cosmos/Octo 量化对照转述 *(secondary)*
- https://arxiv.org/abs/2504.16054 — π0.5:未见家庭开放世界泛化 *(primary)*
- https://arxiv.org/pdf/2510.17950 — RoboChallenge:π0.5 43.7% 均值(progress 62.2%)、任务方差 0–100% *(secondary/第三方基准)*
- https://arxiv.org/abs/2503.14734 — GR00T N1:数据效率曲线 *(primary)*
- https://sergeylevine.substack.com/p/sporks-of-agi — Levine:瓶颈是数据获取而非架构;世界模型=候补数据倍增器 *(primary,温和派对位观点)*
- https://arxiv.org/pdf/2510.12796 — DriveVLA-W0:「世界模型放大 VLA 数据 scaling law」——融合派旗帜 *(primary)*
- https://techcrunch.com/2026/01/13/neo-humanoid-maker-1x-releases-world-model-to-help-bots-learn-what-they-see/ — 1X 三层配方(900 h 人视频 + 70 h 微调 + 400 h IDM)*(secondary)*
- 站内:[data-engine-roadmap](data-engine-roadmap.md) / [world-models](world-models.md) / [data](data.md) / [data-collection-devices](data-collection-devices.md) / [on-device-brain](on-device-brain.md) / [visions](visions.md)
