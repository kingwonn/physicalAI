---
title: 技术现状(2026-07 快照)
slug: state-of-the-art
updated: 2026-07-04
confidence: verified
lang: zh
source: ../wiki/state-of-the-art.md
---
> 截至 2026 年 7 月,Physical AI 已从实验室演示走向首批商业部署:通用[视觉-语言-动作模型(VLA)](vla-models.md)(Physical Intelligence 的 π0.7、Google DeepMind 的 Gemini Robotics 1.5/ER 1.6、NVIDIA 的 GR00T 系列、Figure 的 Helix 02)能够零样本跨机器人本体执行数分钟级的家庭和工业任务;[人形机器人](humanoid-robots.md)已在 BMW 和 GXO 的工厂里承担付费工作(丰田 RAV4 产线的合同定于 2026 年落地),而中国出货了全球约 80–90% 的人形机器人;[世界模型(world model)](world-models.md)(Genie 3、NVIDIA Cosmos 3)既是仿真引擎,也日益成为策略本身的骨干;资本随之而来——Figure 估值 $39B,Skild AI 约 $14B,Physical Intelligence 据报道正以 $11B+ 估值融资。灵巧[操作](manipulation.md)仍是最明确的未解瓶颈。

## 高管速览:谁在各领域领先(截至 2026-07)

| 领域 | 前沿领先者 | 证据 |
|---|---|---|
| 通用 VLA 策略 | Physical Intelligence(π0.7)、Google DeepMind(Gemini Robotics 1.5) | π0.7 零样本即可匹敌专用微调模型;Gemini Robotics-ER 1.5 在 15 项学术具身推理基准上综合成绩 SOTA |
| 具身推理(高层"大脑") | Google DeepMind(Gemini Robotics-ER 1.6) | 仪表读数准确率 93%,ER 1.5 仅 23%(2026 年 4 月) |
| 开放机器人基础模型 | NVIDIA(GR00T N1.7 / N2 预览版)、Cosmos 3 | GR00T N2 在 MolmoSpaces 和 RoboArena 排行榜排名第一(2026 年 3 月) |
| 人形机器人商业部署 | Figure(BMW)、Agility(GXO/丰田)、UBTech(中国) | Figure 03 自 2026-06 起在 BMW Spartanburg 从事物流分拣;Digit 在 GXO 搬运超 10 万个料箱;UBTech 宣称部署 1,000+ 台工业人形机器人(未证实) |
| 人形机器人出货量 | AgiBot、Unitree(中国)——第一名归属存在争议 | 2025 年全球出货约 1.3 万台(Omdia)到约 1.8 万台(IDC);AgiBot 约 5,200 台(Omdia/IDC 口径),Unitree 按其招股书自称 >5,500 台;约 80–90% 为中国厂商——见下文出货量核对 |
| 动态运动控制 | Unitree、Boston Dynamics | 春晚直播的全自主功夫表演含空翻(春节联欢晚会,2026-02-16);量产版电动 Atlas 具备 56 个自由度 |
| 世界模型 | Google DeepMind(Genie 3)、NVIDIA(Cosmos 3) | 实时 720p/24fps 交互式世界;基于约 20T token 训练的开源全模态世界基础模型 |
| 消费级家用人形机器人 | 1X(NEO) | $20k 售价下 5 天获约 10,000 台预订(公司口径);首批美国交付计划在 2026 年 |

## VLA / 机器人基础模型

架构细节见[VLA 模型](vla-models.md),训练数据全景见[数据](data.md)。

- **Physical Intelligence π0.7**(2026-04-16 发布)是当前通用策略的参照标杆:一款"可引导"的 VLA,可接受语言、速度/质量元数据和视觉子目标作为提示。宣称具备组合泛化能力(重组技能以完成未见任务,如操作陌生的厨房电器),并在移动操作臂、双臂 UR5e 和 Franka 机械臂上无需微调即可匹敌专用微调模型。据称在新机器人平台上的叠衣成功率可与专家级遥操作(teleoperation)人员相当(公司口径,未证实)。
  - 演进脉络:π0(2024 年 10 月)→ π0.5 开放世界泛化(2025 年 4 月)→ π*0.6 从经验强化学习(2025 年 11 月)→ π0.7(2026 年 4 月)。支撑技术:FAST 动作分词器(训练提速约 5 倍)、实时动作分块、面向 10 分钟以上任务的多尺度具身记忆(2026 年 3 月)。
- **Google DeepMind Gemini Robotics 1.5**(2025 年 9 月):双模型智能体架构——Gemini Robotics-ER 作为统筹的"大脑",Gemini Robotics 作为 VLA 执行器。据报告,Gemini Robotics-ER 1.5 在 15 项学术*具身推理*基准(指点、图像/视频问答:Point-Bench、ERQA、RefSpatial 等——出自技术报告;并非端到端机器人基准)上综合得分最高,其 VLA 展示了跨本体的动作迁移(从双臂实验室机器人到人形机器人),无需针对每种机器人单独定制。**Gemini Robotics-ER 1.6**(2026-04-14)改进了空间推理、成功检测,并新增智能体式"仪表读数"能力(准确率 93%,ER 1.5 为 23%);已通过 Gemini API / AI Studio 提供。
- **NVIDIA GR00T**:GR00T N1.7 已进入带商业许可的抢先体验阶段(侧重灵巧控制);**GR00T N2** 在 GTC 2026-03-16 预览——基于 DreamZero 研究构建的"世界-动作模型",宣称在新环境新任务上的成功率是领先 VLA 的 2 倍以上,并在 MolmoSpaces 和 RoboArena 排名第一;计划 2026 年底交付。世界模型与策略的融合见[世界模型](world-models.md)。
- **Figure Helix 02**(2026-01-27):自研端到端"全身自主"VLA——输入像素与本体感知、输出力矩——驱动 Figure 03 完成 BMW 物流作业和家庭任务演示(装洗碗机、叠衣、整理房间)。
- **其他**:Skild AI("全本体"大脑;截至 2026-01 估值超 $14B);RLWRLD 的 RLDX-1,面向五指灵巧手(dexterous hand)的灵巧性优先基础模型(2026 年,单一来源,能力宣称未证实)。
- **研究领域**:ICLR 2026 收到 164 篇 VLA 投稿(是 ICLR 2025 的 9 篇的 18 倍)。主导趋势:离散扩散动作解码、具身思维链、更好的动作分词器(残差 VQ、样条)以及跨本体/跨动作空间迁移。值得关注的开放模型:FLOWER、X-VLA、OpenVLA 的后继者。

### 基准现实核查(截至 2026-07)

| 基准 | 状态 | 说明 |
|---|---|---|
| LIBERO | 已饱和 | 多数 ICLR 2026 投稿达 95–98%;鲁棒性变体(LIBERO-Plus/PRO/X)已取而代之 |
| CALVIN | 接近上限 | SOTA 在 ABC→D 上平均任务链长 >4.5 |
| SIMPLER | 使用中,噪声大 | 依设置不同为 40–99%;跨论文比较不可靠 |
| RoboArena / MolmoSpaces | 新兴标准 | 零样本、近真实机器人评测;闭源前沿模型与开放权重研究模型之间差距明显 |

要点:仿真基准已无法区分前沿系统;领域正转向零样本真实机器人评测,而闭源模型(Gemini Robotics、π 系列、GR00T N2)在此领先。评测问题见[开放问题](open-problems.md)。

## 人形机器人:从试点到首批商业机队

完整细节见[人形机器人](humanoid-robots.md);公司概况见[组织机构](organizations.md)。

| 公司 | 机器人 | 状态(截至 2026-07) |
|---|---|---|
| Figure | Figure 03(Helix 02) | Figure 03 已在 BMW Spartanburg 开始复杂物流分拣——BMW 于 2026-06-25 宣布该项目,Figure 于 2026-06-30 宣布部署——此前 Figure 02 已完成试点(约 10 个月支持 30,000+ 台 X3,约 1,250 小时);据报道首批机队合同为 40 台(单一聚合来源,未证实);与 Catalyst Brands 签订物流协议(2026-05-26,内华达州 Reno 配送中心);据报道按约 $25/机器人小时计费(未证实)。注意:BMW 莱比锡试点(2026 年夏)使用的是 Hexagon Robotics 的 AEON,而非 Figure |
| Tesla | Optimus V3 | 约 2026 年 7 月底/8 月在 Fremont 改造后的 Model S/X 产线启动生产,初期产量"非常缓慢";首条 Optimus 产线已运抵 Fremont 并开始安装(Tesla 副总裁 Lars Moravy 表示);Musk 于 2026-07-01 发布了走访产线的照片;第三代手部:每侧前臂/手约 25 个执行器(每手 22 个自由度,腱绳驱动,双手共 50 个执行器);高产量目标定在 2027 年;消费者销售目标为"2027 年底"(Musk,达沃斯,2026-01) |
| Boston Dynamics | 电动 Atlas | 量产版于 CES 2026-01-05 亮相;56 个自由度、2.3 m 臂展、50 kg 认证举重;2026 年机队配额已全部锁定(Hyundai RMAC、Google DeepMind 合作);Hyundai 正在美国建设年产 30,000 台机器人的工厂;据报道有 25,000 台内部承诺订单(未证实) |
| 1X | NEO | $20,000(或 $499/月)的消费级家用人形机器人;首 5 天约 10,000 台预订(2025 年 10 月,公司口径);自 2026-04-30 起在加州 Hayward 全面量产(宣称年产能 1 万台);承诺 2026 年底前完成首批家庭交付 |
| Agility Robotics | Digit | GXO 物流:在 Flowery Branch 累计搬运超 100,000 个料箱(截至 2025 年末);与丰田 RAV4 工厂(安大略省 Woodstock;2026-02 签约)签订 7 台 RaaS 合同,2026 年内部署 |
| Unitree | G1 / R1 / H2 | 按其 IPO 招股书,2025 年售出并交付人形机器人 >5,500 台(仅双足,不含轮式;Omdia/IDC 记为 4,200 台并列其为第二——见下文出货量核对);G1 约 $16k(Amazon 挂牌价 $17,990);R1 约 $5,900;上海科创板 IPO 于 2026-06-01 通过上市审核,2026-07-02 获 CSRC 注册批准(2026-07-03 据报道;募资约 ¥4.2B / 约 $618M);2025 年营收 ¥1.70B;GAAP 净利润约 ¥288M,扣非(excl. non-recurring)>¥600M(SCMP:"调整后" ¥591M)——见[公司:Unitree](company-unitree.md) |
| AgiBot(智元) | Expedition A3 等 | 第 10,000 台通用机器人于 2026 年 3 月末下线;按 Omdia 口径 2025 年出货人形机器人 5,168 台(IDC 口径 5,200 台),两家均列其为全球第一;正寻求借壳上市 |
| UBTech | Walker S2 | 宣称在汽车/电子/物流工厂部署 1,000+ 台工业人形机器人(公司口径,未证实);2026-06-30 推出 UWORLD U1 消费级陪伴产品线,起售价约 RMB 119,800,宣称订单 13k+(公司口径),约 2026-09 起交付 |
| Apptronik | Apollo / Apollo 2 | A 轮累计 $935M(2026-02-11 追加 $520M),据报道投后估值约 $5.3B;投资方包括 Mercedes-Benz、Google、John Deere;与 Google DeepMind 一起发布 Apollo 2 及 90,000 平方英尺的"Robot Park"训练园区(Austin,2026-06-30) |

- 市场规模:TrendForce 预测 2026 年全球人形机器人出货量 >50,000 台(同比约 +700%——注意此增速隐含约 6–7 千台的 2025 年基数,远低于下文核对的约 1.3–1.8 万台跟踪区间;各预测基线同样存在分歧);预计中国产量同比 +94%,Unitree 加 AgiBot 占中国出货量约 80%(截至 2026-04 的预测)。
- 区域格局:2025 年人形机器人出货量约 80–90% 来自中国——Omdia 前十榜单内约 87%,IDC 口径约 90%,Morgan Stanley 口径 ">80%"([图景:中国](landscape-china.md))——而价值最高的部署和前沿模型仍由美国主导([图景:美国](landscape-usa.md));欧洲/韩国/日本的态势见[图景:世界其他地区](landscape-row.md)。

### 核对 2025 年出货量统计(截至 2026-07)

已发布的 2025 年人形机器人总量在约 13,000 到约 18,000 台之间。分歧主要源于口径——各跟踪机构统计的对象不同:

| 跟踪机构(报告) | 2025 年数字 | 统计口径 |
|---|---|---|
| Omdia——*Market Radar: General-purpose Embodied Intelligent Robots*(2026-01) | 全球 13,317 台 | 厂商单位出货量,全球。前十:AgiBot 5,168(第一,份额约 39%)、Unitree 4,200、UBTech 1,000、Leju 500、EngineAI 400、Fourier 300、Figure/Agility/Tesla 各约 150、其他约 1,350 |
| IDC——*Global Humanoid Robot Market Analysis*(2026-01;这就是新华社/央视/环球时报引用的"约 18,000"数字) | 全球约 18,000 台,同比 +508% | 按公司和应用场景(娱乐、科研、制造、仓储等)统计出货;AgiBot 第一,5,200 台,Unitree 4,200 台,UBTech 1,000 台;约 90% 为中国厂商 |
| Unitree——科创板 IPO 招股书(2026-03 提交) | >5,500 台(仅自家) | "实际销售并交付给最终客户"的单位——订单更高,量产产出 >6,500 台;仅双足人形机器人,不含轮式;宣称全球第一份额(某招股书解读为约 32%——单一来源,未证实),据此推算全球市场约 1.7 万台 |
| Morgan Stanley(分析师 Sheng Zhong,2026-06) | 2025 年全球部署 >16,000 台;中国 >80% | 仅计对外销售——明确排除原型、试用机和内部使用机;是其中国 2026 年预测的基线,该预测在 2026 上半年从 1.4 万上调至 2.8 万再到 5 万台 |

分歧原因:

- **出货 ≠ 产量 ≠ 订单**:仅 Unitree 一家就报出三个数字(交付 >5,500、生产 >6,500、订单更高);各跟踪机构取样于该漏斗的不同环节。
- **形态口径**:轮式/双臂平台是否算"人形机器人"。Unitree 的数字明确排除轮式型号;此类范围差异很可能是 Omdia 约 1.3 万与 IDC 约 1.8 万之间的分歧所在,也是 AgiBot 与 Unitree 争夺第一的背景——两家都宣称 2025 年全球第一(此为推断,未证实)。
- **仅中国 vs 全球**:Morgan Stanley 被广泛引用的 2026 年 50,000 台预测仅覆盖中国;Omdia/IDC 总量为全球口径(无论哪种口径,约 80–90% 为中国厂商)。
- **厂商层面的分歧仍在**:Omdia 和 IDC 都记 Unitree 4,200 台,比 Unitree 自己招股书披露的数字低约 24%——这表明人形机器人市场跟踪仍很不成熟(媒体报道指出演示/测试机很难与销售区分)。

本 wiki 惯例:引用 2025 年全球人形机器人出货量时写为"约 13,000–18,000 台,视跟踪机构而定"并注明出处,任何单一公司的第一名宣称均视为有争议。

## 运动控制

深入阅读:[运动控制](locomotion.md)。

- 全身强化学习控制在平地行走上已基本解决,在杂技动作上也日益成熟:Unitree G1/H2 人形机器人在中国春节联欢晚会(2026-02-16,Unitree 第三次登上春晚)上表演了完全自主的集群功夫节目("WuBOT")——超过 3 m 的空中翻越、跨桌腾跃、借墙后空翻、集群速度达 4 m/s。
- 研究前沿转向**单策略多能**:一个学习策略同时处理行走/跳跃/站立/单脚跳,支持实时可调步态参数,并能容忍任意上身操作指令(如 HugWBC);还有可模仿任意人体动捕数据的通用运动跟踪策略。
- **感知型跑酷与技能串联**(2026 年论文:Deep Whole-body Parkour、基于运动匹配的技能链)将其扩展到视觉条件化的动态地形穿越。
- 关键使能技术:大规模并行 GPU 物理仿真([仿真](simulation.md))——每张 GPU 数千个环境——仍是标准训练配方;运动控制的模拟到现实(sim2real)如今已属常规,与操作形成对比。

## 操作

深入阅读:[操作](manipulation.md);手部与执行器见[硬件](hardware.md)。

- 灵巧五指操作被广泛认为是实用机器人领域**最大**的未解难题:柔性物体、人类工具、小件装配。
- 硬件竞赛:Tesla Optimus V3 每侧前臂/手搭载 25 个执行器(约为第二代的 4.5 倍);Figure 03 手部增加了指尖触觉传感和掌心摄像头;预计 2027 年出现售价低于 $25k 的商业可行灵巧手(分析师预测,未证实)。
- 模型竞赛:π0.7 宣称以专家级效率完成叠衣/做浓缩咖啡;RLWRLD RLDX-1 通过重定向技术栈直接从徒手人手视频训练;NVIDIA GR00T N1.7 主打"高级灵巧控制"。
- 触觉基准正在兴起(Daimon Robotics 与 Galbot 的 RobOmni,ICRA 2026),但尚无公认的社区级灵巧性基准——见[开放问题](open-problems.md)。

## 世界模型

深入阅读:[世界模型](world-models.md)。

- **Genie 3**(DeepMind,2025-08-05 发布):提示生成可交互世界,720p/24fps,可保持数分钟一致性;已产品化为面向 AI Ultra 订阅用户的"Project Genie"(2026-01-29)。仅提供闭源 API。
- **NVIDIA Cosmos 3**(2026-05-31 在 GTC Taipei 发布):开源"全模态"世界基础模型——混合 transformer 架构,将推理 transformer(Reasoner)与生成专家(Generator)配对——训练数据约 20T token,涵盖文本、图像、约 4 亿条视频、音频及机器人/人类动作轨迹;有 Super/Nano/Edge 三个版本;宣称在 Physics-IQ、PAI-Bench、RoboLab 上位居前列;采用方包括 Skild AI、Agile Robots、LG、Samsung、Doosan、理想汽车(Li Auto)。
- **与策略的融合**:GR00T N2 的"世界动作模型"(DreamZero)与 π0.7 用于视觉子目标的内部世界模型都表明,世界模型正成为策略的一部分,而不再只是仿真器。这可以说是 2026 年最具决定性的架构押注——见[技术树](tech-tree.md)。

## 算力、平台与生态

- NVIDIA 是事实上的平台层:Jetson Thor 机载计算、Isaac Sim/Lab、Cosmos 世界模型、GR00T 策略,外加面向学术界(Ai2、ETH Zurich、Stanford、UCSD)的开放 **Isaac GR00T 参考人形机器人**设计(与 Unitree 合作打造,2026 年底可用)。见[硬件](hardware.md)与[仿真](simulation.md)。
- 传统工业机器人厂商(FANUC、ABB、Yaskawa、KUKA——合计装机量 >200 万台)正将 NVIDIA Omniverse 库和 Isaac 仿真框架整合进虚拟调试工作流,而非自研基础模型(截至 GTC 2026-03)。
- 数据仍是护城河:遥操作机队、人类视频预训练、世界模型合成数据是三条相互竞争的路线——见[数据](data.md)。

## 投资快照(截至 2026-07)

细节与历史见[投资](investment.md)。

| 公司 | 最新一轮 | 估值 |
|---|---|---|
| Figure | $1B+ C 轮(2025-09) | 投后 $39B |
| Skild AI | $1.4B C 轮(2026-01-14,SoftBank 领投;Nvidia、Bezos 参投) | >$14B |
| Physical Intelligence | 约 $1B 融资进行中(2026-03 据报道) | 目标 >$11B(未完成前未证实) |
| Apptronik | $520M A 轮追加(2026-02-11) | 据报道投后约 $5.3B |
| Unitree | 上海科创板 IPO:2026-06-01 通过上市审核,2026-07-02 获 CSRC 注册批准(募资约 $618M);接下来是定价/申购,可能于 2026 年 7 月底挂牌(媒体报道,未证实) | 目标约 $6.2B(据 Caixin) |

- 仅 2026 年第一季度,Physical AI 初创公司就在 27 笔交易中融资超 $6.4B(单一跟踪来源,未证实);若上半年节奏延续,全年人形机器人专项投资预计超 $20B(预测,未证实)。

## 尚未达到的"技术现状"

交叉参考:[开放问题](open-problems.md)。

- 没有任何人形机器人能完成一整班经济上为正、无人看管的多任务工作;现有部署都是有人监督的窄任务机队。
- 灵巧操作、长时程错误恢复(>10 分钟任务是前沿,依据 π 的具身记忆工作)以及可信的真实世界评测仍是开放问题。
- 仿真基准(LIBERO/CALVIN)已饱和、不再有信息量;RoboArena 式零样本真实评测尚处早期。
- 面向未受训人群(家庭、公共空间)的人形机器人安全认证尚无成型标准;1X NEO 的 2026 年家庭交付将是第一次大规模检验。

## 来源

- https://www.pi.website/ — Physical Intelligence 模型时间线(π0 → π0.5 → π*0.6 → π0.7)及研究博客
- https://www.pi.website/blog/pi07 — π0.7 发布细节、可引导性、评测宣称(2026-04-16)
- https://deepmind.google/blog/gemini-robotics-er-1-6/ — Gemini Robotics-ER 1.6 能力与基准数据(2026-04-14)
- https://deepmind.google/blog/gemini-robotics-15-brings-ai-agents-into-the-physical-world/ — Gemini Robotics 1.5 智能体架构、动作迁移、15 项基准 SOTA 宣称
- https://arxiv.org/pdf/2510.03342 — Gemini Robotics 1.5 技术报告;ER 1.5 "15 项学术具身推理基准"综合 SOTA 宣称的出处
- https://nvidianews.nvidia.com/news/nvidia-launches-cosmos-3-the-open-frontier-foundation-model-for-physical-ai — Cosmos 3 发布、架构、开放性、合作伙伴(2026-05-31)
- https://nvidianews.nvidia.com/news/nvidia-and-global-robotics-leaders-take-physical-ai-to-the-real-world — GTC 2026 GR00T N2 预览、MolmoSpaces/RoboArena 第一的宣称、伙伴生态(2026-03-16)
- https://nvidianews.nvidia.com/news/nvidia-open-humanoid-robot-reference-design — Isaac GR00T 参考人形机器人(与 Unitree 合作)、学术合作伙伴
- https://mbreuss.github.io/blog_post_iclr_26_vla.html — ICLR 2026 VLA 领域综述:164 篇投稿、基准饱和、趋势
- https://www.figure.ai/news — Figure 时间线:Helix 02、Figure 03、BMW 部署、$39B C 轮
- https://www.press.bmwgroup.com/global/article/detail/T0455864EN/ — BMW 德国人形机器人试点(莱比锡,2026 年夏,使用 Hexagon Robotics 的 AEON);Spartanburg Figure 02 试点结果(2026-02-27)
- https://www.press.bmwgroup.com/global/article/detail/T0458778EN/ — BMW 新闻稿:Figure 03 在 Spartanburg 的物流分拣项目(2026-06-25)
- https://techcrunch.com/2026/04/16/physical-intelligence-a-hot-robotics-startup-says-its-new-robot-brain-can-figure-out-tasks-it-was-never-taught/ — π0.7 发布及宣称的独立确认(2026-04-16)
- https://www.bloomberg.com/news/articles/2026-03-27/ex-deepmind-staffers-robotics-startup-in-talks-for-11-billion-valuation — Physical Intelligence 洽谈约 $1B 融资、估值 >$11B(2026-03-27)
- https://techcrunch.com/2026/01/14/robotic-software-maker-skild-ai-hits-14b-valuation/ — Skild AI $1.4B C 轮、估值 >$14B、SoftBank 领投(2026-01-14)
- https://www.caixinglobal.com/2026-07-03/unitree-robotics-wins-approval-for-618-million-star-market-ipo-102460136.html — Unitree 获 CSRC 注册批准(2026-07-02 周四批准,2026-07-03 报道)、募资约 $618M、2025 年财务数据
- https://www.stcn.com/article/detail/3735182.html — 证券时报:Unitree 2025 年 GAAP 净利润约 ¥288M("近3亿");同系列申报阶段文章(stcn.com 3688950)指出 >¥600M 为扣非净利润(excl. non-recurring),+674.29%
- https://www.scmp.com/tech/tech-trends/article/3340446/chinas-unitree-ships-more-5500-humanoid-robots-2025-surpassing-us-peers — Unitree 2025 年出货 5,500+ / 生产 6,000+(经 36Kr/内部人士,仅双足、不含轮式;Unitree 拒绝置评);Omdia 对 Tesla/Figure/Agility 各约 150 台的统计
- https://technode.com/2026/01/09/chinas-agibot-leads-global-humanoid-robot-shipments-in-2025-omdia-says/ — Omdia Market Radar:2025 年全球出货约 1.3 万台;AgiBot 5,168(39%)、Unitree 4,200、UBTech 1,000
- https://www.forbes.com/sites/johnkoetsier/2026/01/09/top-10-humanoid-robot-companies-by-shipments-revealed/ — Omdia 完整前十榜单与 13,317 台全球总量;指出销售/演示/测试机的口径模糊
- https://www.globaltimes.cn/page/202601/1354054.shtml — IDC Global Humanoid Robot Market Analysis:2025 年约 18,000 台、同比 +508%、AgiBot 第一 5,200 台(即新华社/官方媒体引用的数字)
- https://www.humanoidsdaily.com/news/unitree-files-for-580m-ipo-humanoid-sales-surpass-robot-dogs-as-profits-soar — Unitree 招股书:2025 年人形机器人 5,500 台、不含轮式、人形机器人占营收 >51%
- https://roboticsandautomationnews.com/2026/03/31/unitree-robotics-files-for-610-million-ipo-as-humanoid-robot-sales-surge/100272/ — Unitree 招股书口径:>5,500 台"实际销售并交付给最终客户",订单更高,产出 >6,500 台
- https://www.scmp.com/tech/article/3358210/morgan-stanley-raises-china-humanoid-robot-shipment-forecast-50000-units — Morgan Stanley 将中国 2026 年预测上调至 50,000 台(此前 28,000;2030 年 446,000 台),2026-06-24
- https://www.cryptopolitan.com/morgan-stanley-doubles-chinas-humanoid-shipment-target-to-50000/ — Morgan Stanley 方法论(仅计对外销售,排除原型/试用/内部使用);2025 年全球部署 >16,000 台、中国 >80%;分析师 Sheng Zhong
- https://www.prnewswire.com/news-releases/kung-fu-meets-spring--unitree-spring-festival-gala-robots-present-cyber-real-kung-fu-in-the-year-of-the-horse-302689291.html — Unitree 在春节联欢晚会上的自主功夫表演(2026-02-16)
- https://www.eweek.com/news/tesla-optimus-robot-2027-sale/ — Musk:Optimus 消费者销售目标定于 2027 年底(达沃斯,2026-01)
- https://techcrunch.com/2026/02/19/toyota-hires-seven-agility-humanoid-robots-for-canadian-factory/ — 丰田 Woodstock 工厂 7 台 Digit 的 RaaS 合同(2026-02)
- https://www.agilityrobotics.com/content/digit-moves-over-100k-totes — Digit 在 GXO Flowery Branch 搬运超 100,000 个料箱
- https://blog.google/innovation-and-ai/models-and-research/google-deepmind/project-genie/ — Project Genie 面向 AI Ultra 订阅用户上线(2026-01-29)
- https://www.figure.ai/news/figure-signs-agreement-with-catalyst-brands — Figure 与 Catalyst Brands 的物流协议(2026-05-26)
- https://www.trendforce.com/presscenter/news/20260409-13007.html — 中国人形机器人产量 2026 年 +94% 预测、Unitree/AgiBot 份额
- https://restofworld.org/2026/unitree-china-humanoid-robot-shanghai-ipo/ — Unitree $608M 上海 IPO 申报
- https://www.techtimes.com/articles/317632/20260602/unitree-ipo-cleared-agibot-hits-10000-units-china-humanoid-robot-duopoly-takes-shape.htm — Unitree IPO 过会 2026-06-02;AgiBot 第 10,000 台下线
- https://electrek.co/2026/04/22/tesla-optimus-production-fremont-model-sx-line/ — Optimus V3 生产时间表、Fremont 产线改造
- https://www.automate.org/robotics/industry-insights/boston-dynamics-to-begin-production-on-redesigned-atlas-humanoid-in-2026 — Atlas 量产版 CES 2026 发布、规格、2026 年配额
- https://www.hyundainews.com/releases/4664 — Hyundai AI 机器人战略、美国机器人工厂
- https://www.therobotreport.com/1x-announces-pre-order-launch-neo-humanoid-robot/ — 1X NEO 定价与预订启动
- https://www.forbes.com/sites/johnkoetsier/2026/04/30/1x-kicks-off-full-scale-production-of-humanoid-robot-neo/ — NEO 全面量产、工厂产能
- https://techcrunch.com/2026/02/11/humanoid-robot-startup-apptronik-has-now-raised-935m-at-a-5b-valuation/ — Apptronik 融资
- https://news.crunchbase.com/venture/ai-humanoid-robot-funding-apptronik/ — 人形机器人融资背景、Skild $14B、PI $11B 洽谈
- https://www.therobotreport.com/rlwrld-releases-rldx-1-a-dexterity-first-foundation-model-for-robot-hands/ — RLDX-1 灵巧性优先基础模型
- https://deepmind.google/blog/genie-3-a-new-frontier-for-world-models/ — Genie 3 能力(720p/24fps 实时交互世界)
- https://arxiv.org/pdf/2510.13626 — LIBERO-Plus 鲁棒性分析(基准饱和的证据)
- https://www.benzinga.com/markets/tech/26/07/60209589/elon-musk-says-teslas-model-s-model-x-line-is-now-building-optimus-robots — Musk 发布 Fremont 首条 Optimus 产线照片(2026-07-01);Moravy:产线已到位、安装已开始
- https://www.prnewswire.com/news-releases/ubtech-launches-uworld-u1-the-worlds-first-full-size-mass-produced-ultra-bionic-humanoid-robot-302815272.html — UBTech UWORLD U1 消费级产品发布(2026-06-30)、定价、订单宣称
- https://apptronik.com/news-collection/welcome-to-robot-park-where-apptroniks-apollo-goes-to-work — Apptronik Apollo 2 与 Robot Park 发布(2026-06-30)
- https://news.futunn.com/en/post/75500836/robotics-sector-surges-unitree-technology-s-star-market-ipo-registration — Unitree IPO 注册生效;可能 2026 年 7 月底挂牌(媒体报道)
