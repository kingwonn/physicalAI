---
title: 数据工厂经济学
slug: data-foundry
updated: 2026-07-04
confidence: verified
lang: zh
source: ../wiki/data-foundry.md
---
> 机器人训练数据如今已成为一种人工制造的商品,拥有自己的供应链、工厂、劳动力市场和价格曲线——一个位于模型实验室之下的"数据工厂(data foundry)"产业。截至 2026-07,该赛道涵盖美国的中介商(Scale AI 的 Physical AI Data Engine)、垂直整合的采集方(Generalist AI 的 500,000+ 小时可穿戴设备语料库)、中国由政府补贴的遥操作(teleoperation)大厅(40+ 中心;仅京东就计划两年内采集 1000 万小时)、[Physical Intelligence](company-pi.md)/[Figure](company-figure.md)/[Tesla](company-optimus.md) 的自建团队,以及第一波数据交易市场。单位经济性是核心故事:据报道,美国遥操作数据的全口径成本从约 $340/小时(2024 年初)降至约 $118/小时(2026-03),美国操作员时薪 $20–50,而中国为 $3–20,第一人称人类视频的成本又比遥操作低约一个数量级——这正是各大实验室纷纷转向可穿戴设备的原因。本页讨论商业层面;技术层面的数据问题见[数据](data.md)。

## 为什么会出现数据工厂产业

- 机器人动作没有免费的互联网语料库;每一小时训练数据都有边际生产成本(操作员人工 + 设备摊销 + 质检 + 标注)。方法权衡见[数据](data.md)。
- 缩放定律结果(ICLR 2025 多样性幂律;GEN-0 的预训练小时数定律)把数据从"锦上添花"变成了首要的资本消耗项——实验室现在像预算算力一样预算数据采购。见[投资](investment.md)。
- 已经出现三种商业模式:**中介/服务商**(Scale AI、标注 BPO)出售采集即服务;**垂直整合的实验室**(Generalist、AgiBot、Tesla)自建采集并自留数据;**政府补贴的基础设施**(中国的市级训练中心)把成本分摊到政府、硬件厂商和廉价劳动力上。
- 结构性张力:拥有最好模型的实验室越来越拒绝共享或出售数据(数据即护城河),因此开放生态依赖政府支持的开源发布(AgiBot World、RoboMIND)和学术联盟——见下文"专有与开放的差距"一节。

## Scale AI Physical AI Data Engine

- **产品**(2025-09 发布/扩展):面向机器人的端到端采集 + 标注——在旧金山一处机器人原型实验室已记录 100,000+ 生产小时,外加全球贡献者网络;覆盖遥操作、人类视频和评测数据(公司口径)。
- **公开客户**(截至 2025-09):[Physical Intelligence](company-pi.md)、Generalist AI、Cobot——也就是说,Scale 向那些同时自建数据引擎的实验室卖"铲子和镐"。
- **Universal Robots 合作**(GTC 2026-03 宣布):"UR AI Trainer" 主从式模仿学习套件把 Scale 的引擎嵌入 UR 约 10 万台的工业机械臂存量——意在把已部署的协作机器人变成分布式采集车队。
- **Meta 交易之后的状态**:Meta 以 $14.3B 收购 49% 股份(2025-06,估值约 $29B);创始人 Alexandr Wang 离职去执掌 Meta Superintelligence Labs;随后 Google、OpenAI 和 xAI 因保密顾虑削减或暂停了 LLM 数据标注业务,Scale 裁减约 200 名数据标注员工(2025-07)。Physical AI 是新任 CEO Jason Droege 治下的增长押注之一——上述机器人客户名单是在 Meta 交易*之后*宣布的,说明机器人实验室不像 LLM 实验室那么忌惮(机器人数据是客户特定的,不会泄露模型机密)。另于 2026-03 成立 "Scale Labs",专注智能体/多模态系统可靠性研究。Forbes 报道其整体业务面临利润率压力(2026-05)(单一来源)。

## Generalist AI:垂直整合的数据工厂

- **创始人**(已核实):Pete Florence(CEO,前 Google DeepMind;PaLM-E/RT-2 系脉络)、Andy Zeng(首席科学家,前 Google Brain)、Andy Barry(CTO,前 Boston Dynamics)。注意:Eric Jang 并非 Generalist 创始人——这是一个常见误传;他曾任 1X Technologies 的 AI 副总裁,2026-01 离职(截至 2026 年中处于休假状态)。
- **数据引擎**:腕戴式 "data hands" 可穿戴设备,让人手充当夹爪式机器人末端执行器,同时记录视觉与感知数据流;Generalist 已"向新的地区运送了数千只机器人手",交给一个签约的**数据工厂合作伙伴**网络,在数千个家庭、仓库和工作场所运营(公司说法;合作伙伴身份、地域和薪酬未披露)。这是人体化采集,而非机器人遥操作——采集时无需机器人(UMI 式经济性)。
- **语料库**:270,000+ 小时(2025-11,GEN-0)→ GEN-1 时 **500,000+ 小时**(2026-04),最后一次披露时以约 10,000 小时/周的速度增长——这是全球已披露的最大物理交互语料库,是所有开放数据集总和的数倍。
- **GEN-1**(2026-04-02):宣称在 GEN-0 级模型只达到 64% 的任务上平均成功率 99%,任务执行速度快约 3 倍,预训练之后每个任务只需约 1 小时机器人特定数据(相比从头训练成功率 19%)——其商业卖点是,足够大的预训练语料库能把单客户数据成本压缩约 10 倍(公司口径,无第三方评测)。
- **资本**:$400M,估值约 $2B(2026-06,Radical Ventures 领投;NVIDIA、Bezos Expeditions 参投;累计融资 >$500M)——这轮融资实质上就是数据工厂的资本开支。此前:截至 2025 年累计融资约 $140M,估值约 $440M(Forbes)。
- 与 PI 的对比:Forbes 报道 Physical Intelligence 依赖遥操作,搭建场景甚至租用 Airbnb 做家庭采集,而 Generalist 押注廉价可穿戴设备——两者是每小时成本谱系的两个极端。

## 中国的政府支持数据工厂

中国以政策方式将数据采集工业化;政策时间线见[格局:中国](landscape-china.md)——本节聚焦设施与经济性。

- **AgiBot(上海临港)**:自称最大的具身数据采集设施——AgiBot World 论文称 4,000 m²(kr-asia 报道为 3,000 m²),约 100 台机器人在五个模拟场景域(家居、零售、服务、餐饮、工业)中持续采集,配备 3,000+ 真实物体,通过 VR 遥操作每天产生约 30,000–50,000 条 episode(公司口径)。开放的 AgiBot World 语料库(100 万+ 轨迹)及后续开源版本 **AgiBot World 2026** 均出自这里;还在 G2 上演示了超视距遥操作用于远程采集。
- **X-Humanoid / 北京具身智能机器人创新中心(亦庄)**:"具身智能数据与训练基地",**120+ 种不同机器人型号**在 6 大行业(家庭、零售、办公、工业、医药、医疗)的 30+ 场景中训练,并设有高精度动作捕捉场馆用于制定采集质量标准;产出了 RoboMIND/RoboMIND 2.0(新华社称下载量 600 万+);首轮市场化融资募得人民币 7 亿+(约 $100M)(2026-02,财新;百度参投)(设施数据:新华社,截至 2026-06)。
- **市级训练场**:上海麒麟(约 5,000 m²,100+ 异构人形机器人,2025-01 开业);北京石景山(10,000+ m²,16 个搭建场景);截至 2025-12 已宣布 40+ 国有中心,约二十余家在运营(Interact Analysis 统计,经 Rest of World,2026 年初)。深圳/广东有厂商运营的项目嵌入数十家电子和包装工厂(工人在真实产线上佩戴头部相机 + 腕部传感器)。
- **京东(宿迁)**:计划两年内产出 **1000 万小时**机器人训练数据——一个专门建造的"数据采集社区",居民拍摄家务,最终涉及约 10 万名员工加约 50 万名外部人员(Rest of World;公司计划,执行情况未证实)。若兑现,将令所有已披露的西方语料库相形见绌。
- **需求驱动**:工信部+国资委的**实景训练专项行动**(2026-06-09)要求到 2026 年底在 10 个省份和中央国企落地 100+ 应用场景并具备"万台级"部署能力——每个部署场景同时也是数据采集点,实质上是国家对数据工厂产能的采购订单。优必选(UBTech)自贡数据采集中心 1.59 亿元人民币订单展示了收入闭环:政府买机器人来配备中心,中心生产数据来改进机器人。
- **劳动模式**:全职"数据采集员"戴着 VR 头显和手臂外骨骼,单个动作每天重复多达约 600 次;时薪 $5–20,视地区而定(Rest of World)。副业式第一人称拍摄报酬低得多——有记录的案例:在山东每天拍 6 小时家务,时薪 ¥20(约 $3)。上门机器人服务则把补贴反向运作:一位北京客户为一次 3 小时的机器人上门服务*支付*了 ¥149(约 $22),而这次服务的真正产品是在他公寓里采集的训练数据——数据价值在补贴一个低于市场价的服务。

## 美国实验室的自建数据运营

| 实验室 | 采集模式 | 已披露规模 | 备注 |
|---|---|---|---|
| [Physical Intelligence](company-pi.md) | 自建遥操作;搭建场景 + 租用 Airbnb;同时也是 Scale AI 的公开客户 | π0 时代语料库据报道约 1 万小时(未证实);π0.5 新增约 400 小时移动操作演示 | 不出售数据或遥操作服务;采集是服务于自家模型的成本中心 |
| [Figure](company-figure.md) | 自建多操作员遥操作车队 + Brookfield 第一人称人类视频("Go-Big") | Helix 用约 500 小时高质量遥操作数据训练(2025-02);Go-Big 覆盖 10 万+ 住宅单元 | 用 VLM 生成事后语言指令自动标注遥操作片段——把标注成本转嫁给 GPU |
| [Tesla Optimus](company-optimus.md) | 帕洛阿尔托的受薪"数据采集操作员"——时薪上限 $48,动捕服 + VR,身高要求 5'7"–5'11",每天步行 7+ 小时;截至 2024-08 已有 >50 人担任该岗位(Business Insider 的 LinkedIn 分析) | 未披露 | 2025-06 转向纯相机的头盔/背包装备(五个相机)拍摄日常任务——放弃动捕服,保留雇佣模式 |
| Apptronik | "Robot Park"(奥斯汀,90,000 平方英尺,2026-06-30 宣布):Apollo 车队在遥操作 + 自主混合模式下做真实的物流/制造/零售工作 | 未披露 | 数据供给 Google DeepMind 的 Gemini Robotics;在 Mercedes-Benz 和 GXO 设卫星站点——以工作即采集,收入抵消采集成本 |

- 欧洲对照:**Neura Robotics**(德国)已让 **1,000+ 工业工人穿上动作捕捉服**来生成人形机器人训练数据——CEO David Reger:"我们拿到了,嗯,非常多的数据"(据 Witt,《纽约客》2026-07-06 期;公司项目,规模未证实)——穿动捕服的*工人做本职工作*作为一条工厂化渠道,既不同于专门的遥操作大厅,也不同于被动的第一人称拍摄。Witt 给出的上限:即便全球规模的动捕也要几十年才能追上 ChatGPT 级训练语料库;见[数据](data.md)。
- 来自自动驾驶的先例:**Waymo** 在其 2025 年缩放定律研究中使用了 **500,000+ 小时**真实驾驶数据(一手来源:Waymo 博客),其远程遥操作"领航员"(据 Witt 位于菲律宾)同时也是数据生产者——这正是 1X 把遥操作 Expert Mode 当作数据渠道的经济学模板("这对我们来说也是有用的数据"——Børnich)。
- Tesla 的工资锚点(时薪 $48,即全职约 $100k/年)是美国第一方采集劳动力最清晰的公开价格——是中国中心工资的 5–15 倍。
- 共同模式:美国实验室把采集劳动当作有技能的内部岗位(质量控制、统一装备),然后把规模化交给更便宜的渠道——人类视频(Tesla、Figure)、客户现场车队数据(Apptronik)或签约的工厂网络(Generalist)。

## 遥操作小时的单位经济性

现有最佳数字,大多来自单一行业分析来源(SVRC / roboticscenter.ai)——仅作方向性参考(多数行为单一来源):

| 指标 | 美国(截至 2026) | 中国(截至 2026) |
|---|---|---|
| 操作员基础工资 | 中等成本城市 $20–35/小时;旧金山/纽约 $30–50/小时;居家远程 VR $20–30/小时 | 训练中心 $5–20/小时(Rest of World);零工式第一人称拍摄约 $3/小时 |
| 全口径操作员成本 | $28/小时的操作员全口径 $36–40/小时(+30–40% 福利/税费) | 未披露;中心由市级项目补贴 + 厂商硬件合作 |
| 每交付遥操作数据小时的全口径成本 | 约 $340/小时(2024 年初)→ 约 $136/小时(2025 年 Q4)→ **约 $118/小时**(2026-03,标准抓放任务,腕部相机 + 外部 RGBD) | 无公开数字;按劳动力占比推断低数倍(未证实推断) |
| 每条演示轨迹成本 | 简单抓放 $6–11;多样抓取 $11–23;工具使用 $20–42;富接触装配 $31–79;双臂/可形变物体 $54–157 | 未公布 |
| 单操作员吞吐量 | 简单任务 80–120 条演示/天;中等 20–70;复杂 5–25(≈ [数据](data.md)中约 35 条演示/小时的遥操作上限) | 单个动作每人每天最多约 600 次重复 |
| 第一人称人类视频(全口径) | 参与者报酬 $10–30/小时 + 设备摊销,对比遥操作操作员时间 $50–200/小时(厂商口径,Claru) | 有记录的零工价约 $3/小时 |

- 含义:按约 $118/小时计,用美国遥操作复制 Generalist 的 50 万小时语料库需约 $59M——但可穿戴人类采集的实际成本很可能只是其零头,这正是其全部命题所在。按中国中心工资计,同样的语料库劳动力成本仅为个位数百万美元(粗略估算,未证实)。
- 成本下降驱动因素:更便宜的装备(ALOHA 级 $20–30k → 消费级 VR)、远程操作省去场地成本、VLM 自动标注(Figure 的事后标注),以及策略辅助遥操作(部分策略处理简单子片段)。
- 没有任何厂商公布真正的"每小时、已交付、质量保证"价目表——定价都是定制/企业级,这本身就说明市场尚不成熟。

## 第一人称人类视频:廉价替代品

- 驱动可穿戴转向的不只是科学论证,更是经济论证:人不需要机器人、不需要装备、不需要专门场地——采集成本逼近当地工资底线。缩放证据(NVIDIA EgoScale 对数线性灵巧度定律)交叉参见[数据](data.md)。
- **Meta Aria Gen 2**:面向合格研究者的大范围推广目标为 2026 年 Q2;27 个国家近 300 个学术实验室已使用 1,000+ 台 Aria Gen 1 设备;与 NVIDIA 合作将 Aria Gen 2 与 FoundationStereo 结合实现可穿戴深度感知。EgoMimic 的标志性经济数据:90 分钟 Aria 录像在联合训练时带来最高 400% 的任务性能提升(Meta/Georgia Tech 口径)。
- Meta 还收购了机器人 AI 初创公司 ARI(Assured Robot Intelligence;团队于 2026-05 加入 Meta Superintelligence Labs),作为其物理 AI 布局的一部分——把 Aria 式第一人称采集定位为战略基础设施,而不只是研究项目。
- 初创层(均截至 2026,多为 YC 系,全部为公司口径):**Claru**(YC W26;10,000+ 佩戴相机的贡献者,遍及 100+ 城市,交付预先计算好的深度/姿态/分割/动作标签)、**Cortex AI**(交易市场,工作场所有偿承接采集/评测;来自真实产业环境的第一人称 + 机器人轨迹数据)、**Sensei**(2024 年成立;宣称人类演示采集成本约为遥操作的 1/10、速度 2 倍;定位"机器人数据界的 Scale AI"),外加做离岸采集/标注的 BPO 类厂商(Objectways、Unidata、Macgence、Labellerr)。
- 中国用零工劳动力跑同一个剧本:京东宿迁社区、工厂头部相机项目,以及约 $3/小时的家务拍摄——第一人称采集是美中成本差距绝对值最大、但护城河意义最小的领域(谁都能买相机)。
- 未决问题:第一人称视频不携带力/触觉信号,也没有机器人动作标签——如果富接触任务无法只靠视频学会,那么在恰恰最值得自动化的任务上,成本优势就会消失。见[开放问题](open-problems.md)和[世界模型](world-models.md)中的神经数据替代方案。

## 交易市场与授权

- 一个虽薄但真实存在的机器人数据*出售*市场在 2025–2026 年出现(所有数字均为公司口径,未证实):
  - **SVRC / Robotics Center 市场**:已编目 20,000+ 小时,索引 1100 万+ episode,来自 30+ 国家的采集方;卖家可选择商用/仅限研究/独家授权,按 episode 或按数据集定价——首个可见的机器人数据标准化授权条款尝试。
  - **Cortex Marketplace**:双边市场——场地(仓库、厨房)有偿承接采集;实验室购买真实场景数据。
  - **Scale AI** 出售采集即服务(不是交易市场——买家拥有自己的数据)。
  - Hugging Face 的 **LeRobot** 格式正成为事实上的交换标准,而任何真正的交易市场都需要这个。
- 什么*不*出售:前沿语料库。Generalist、PI、Figure、Tesla 以及 AgiBot 的专有层严格内部使用;AgiBot 开源精选切片(AgiBot World 2026),但保留实时数据流。仿真数据几乎可以零成本复制,因而难以货币化——见[仿真](simulation.md)。
- 授权方面的开放问题(截至 2026-07):在家庭和工作场所拍摄的第一人称视频(Brookfield 租户、中国工厂工人)尚无成熟的同意/隐私规范,没有标准质量保证条款,也没有关于演示轨迹是否内嵌演示者知识产权的判例。可以预期这会重演 2023–2024 年 LLM 文本授权的乱局,只是晚了几年。

## 专有与开放的差距

- 走势(已披露语料库规模,单位小时,截至 2026-07):Generalist 50 万+(专有),对比 AgiBot World 约 3 千开放 + 更大的内部数据、RoboMIND 2.0 约 1 千、DROID 350、AIRoA 约 1 万——最大的专有语料库已是最大开放真实机器人数据集的约 50 倍,且以约 1 万小时/周增长。尽管开放发布规模变大,差距在 2025–2026 年仍在拉大。
- 中国是主要的制衡力量:政府支持的中心把开源发布(AgiBot World 2026、RoboMIND、麒麟产出)当作生态补贴,与中国 LLM 实验室的开源权重策略如出一辙——见[格局:中国](landscape-china.md)。
- 第一人称数据集可能重新打开局面:人类视频采集足够便宜,学术联盟(Aria 合作伙伴)和初创公司有望追平实验室规模,这与机器人车队数据不同。
- 战略解读:如果缩放定律成立,数据会像资本开支一样复利——2026 年的融资潮(Generalist $400M、Apptronik Robot Park、京东的 1000 万小时计划)都是在赌今天的小时数差距会变成明天的能力差距。见[投资](investment.md)和[最新进展](state-of-the-art.md)。

## 质量对数量:审计与数据整理

- **Traceplane 审计**(2026,对 10 个热门开放数据集的自动化检查):Open X-Embodiment 子数据集 `utokyo_saytap` 只包含黑帧;所列 55 个 OXE 子数据集中有 28 个无法下载;一个拼写错误的数据集名("manpulation")破坏了程序化访问;`berkeley_rpt` 文档标注 3 个相机视角但实际只有 1 个(单一来源审计,但结论可机械复核)。
- 数据整理研究正在专业化:**Re-Mix**(为模仿学习优化数据集混合权重)、基于影响函数的演示筛选("Quality over Quantity",2026),以及研究表明仅看动作的质量评分器会漏掉真正损害策略的结构性缺陷(2026)。一致结论:经过整理的同质数据胜过更大的异质堆料(AgiBot World 相对 OXE 预训练约 30% 的优势——见[数据](data.md))。
- 对数据工厂的启示:质检正在成为利润所在。厂商宣传"可直接训练"的标签和质量基准(X-Humanoid 的动捕校准采集标准;Scale 的评测产品);买家正在意识到一小时便宜的坏数据价值为负。目前尚无第三方认证或标准质量指标(截至 2026-07)——工信部的标准化项目可能会率先在中国填补这一空白。

## 开放问题

- 市场会向中介(Scale 模式)还是垂直方(Generalist 模式)集中?LLM 的历史表明,一旦数据成为护城河,实验室就会将其内化——这对纯数据工厂公司是坏消息。
- 补贴退坡后中国中心的经济性会怎样?工信部专项行动执行到 2026 年底;持续需求取决于部署能否产生真实收入。
- 在前沿实验室不再需要外部数据(已部署机器人的车队学习闭环)之前,有人能建成一个流动性充足的数据市场吗?
- 价格底部在哪里?遥操作 $/小时两年内下降约 65%;第一人称采集已接近工资底线;*仿真*和世界模型(world model)"神经数据"的边际成本是 GPU 时间——见[世界模型](world-models.md)。

## 来源
- https://scale.com/physical-ai — Scale Physical AI Data Engine 产品:100k+ 生产小时、旧金山机器人实验室、采集 + 标注体系。
- https://www.universal-robots.com/news-and-media/news-center/universal-robots-scale-ai-launch-imitation-learning-system-accelerate-ai-training-lab-to-factory/ — UR AI Trainer 合作(GTC 2026-03 宣布),UR 装机量作为采集车队。
- https://techcrunch.com/2025/08/29/cracks-are-forming-in-metas-partnership-with-scale-ai/ — Meta 交易后客户流失(Google/OpenAI/xAI)、约 200 名标注员工裁员(2025-07)、Meta 研究人员更偏好 Surge/Mercor。
- https://www.forbes.com/sites/richardnieva/2026/05/14/scale-meta-deal/ — Meta 交易后 Scale 业务承压(2026-05)。
- https://scale.com/blog/scale-ai-announces-next-phase-of-company-evolution — Alexandr Wang 赴 Meta;Jason Droege 出任 CEO。
- https://generalistai.com/blog/apr-02-2026-GEN-1 — GEN-1(2026-04-02):500k+ 小时预训练语料库、可穿戴设备人类数据、99% 对 64% 成功率、每任务约 1 小时机器人数据、3 倍速度。
- https://www.forbes.com/sites/annatong/2026/04/02/generalist-is-betting-its-robot-training-gloves-will-usher-in-robotics-chatgpt-moment/ — Generalist "data hands" 腕戴设备、数千只已发往多地、创始人(Florence/Zeng/Barry)、PI 遥操作/Airbnb 对比、此前 $140M 融资估值 $440M。
- https://www.bloomberg.com/news/articles/2026-06-04/nvidia-backed-robotics-startup-generalist-ai-valued-at-2-billion — Generalist $400M,估值约 $2B(2026-06),Radical Ventures 领投,累计 >$500M。
- https://generalistai.com/blog/nov-04-2025-GEN-0 — GEN-0:270k+ 小时、每周 +10k 小时、"数据工厂合作伙伴"网络。
- https://restofworld.org/2026/china-ai-robotics-training-data/ — 中国采集经济性:¥20(约 $3)/小时家务拍摄、¥149/3 小时上门服务、京东宿迁 1000 万小时计划(10 万员工 + 50 万外部)、广东工厂头部相机项目。
- https://restofworld.org/2026/china-robots-training-centers-workers/ — 40+ 已宣布的国有中心、约二十余家在运营、$5–20/小时工资、每天约 600 次重复、湖北中心约 100 台遥操作人形机器人。
- https://english.news.cn/20260613/5d8906d63b2a4586a04fe160bd5d7a65/c.html — 新华社(2026-06):X-Humanoid 亦庄数据/训练基地——120+ 机器人型号、30+ 场景、6 大行业、动捕校准采集标准、RoboMIND 600 万+ 下载。
- https://www.caixinglobal.com/2026-02-04/beijing-humanoid-robotics-hub-raises-100-million-in-first-funding-round-102411145.html — X-Humanoid 首轮融资人民币 7 亿+(约 $100M)(2026-02),国资背景投资方 + 百度。
- https://kr-asia.com/inside-agibots-shanghai-center-robots-learn-to-master-tasks-in-human-like-ways — AgiBot 临港设施:约 100 台机器人、每天 3 万–5 万数据点、五大场景域(报道为 3,000 m²)。
- https://arxiv.org/html/2503.06669v4 — AgiBot World 论文:4,000 m² 设施、100 台机器人、3,000+ 不同物体(设施数据的一手来源)。
- https://www.therobotreport.com/agibot-world-2026-dataset-open-source-accelerate-embodied-ai-development/ — AgiBot World 2026 开源数据集发布。
- https://www.ncsti.gov.cn/kjdt/tzgg/202606/t20260609_249248.html — 工信部+国资委实景训练专项行动(2026-06-09):场景指标制造了对训练场的国家需求(一手来源)。
- https://www.roboticscenter.ai/research/robot-data-collection-cost-breakdown — 美国单位经济性:操作员工资 $20–50/小时、全口径 $36–40/小时、按任务复杂度每条演示 $6–157、每天 5–120 条演示吞吐量(单一行业来源)。
- https://www.roboticscenter.ai/state-of-robotics-2026 — 遥操作数据成本下降 $340/小时(2024 年初)→ $136/小时(2025 年 Q4)→ 约 $118/小时(2026-03)(单一行业来源;SVRC "State of Robotics 2026" 报告)。
- https://www.roboticscenter.ai/marketplace — SVRC 数据市场:编目 20k+ 小时、索引 1100 万+ episode、30+ 国家、按 episode 分级授权。
- https://fortune.com/2024/08/19/tesla-robot-hiring-workers-optimus-training-ai/ — Tesla 数据采集操作员:$25.25–$48/小时、动捕服 + VR、身高 5'7"–5'11"、每天步行 7+ 小时。
- https://www.heise.de/en/news/Tesla-hires-over-50-people-for-Optimus-training-in-motion-capture-suits-9841052.html — 截至 2024-08 已有 >50 人担任 DCO 岗位(Business Insider LinkedIn 梳理);帕洛阿尔托地点。
- https://www.eweek.com/news/tesla-optimus-robot-training/ — Tesla 2025 年转向五相机头盔/背包人类视频装备。
- https://www.figure.ai/news/helix — Helix:约 500 小时多机器人多操作员遥操作语料库;VLM 事后自动标注流水线。
- https://www.forbes.com/sites/johnkoetsier/2026/06/30/apptronik-announces-robot-park-a-90000-square-foot-humanoid-data-factory-teases-new-robot/ — Apptronik Robot Park:奥斯汀 90,000 平方英尺数据工厂;Mercedes/GXO 卫星站点;DeepMind 模型。
- https://www.meta.com/blog/aria-gen-2-updates/ — Aria Gen 2 开放申请、2026 年 Q2 大范围推广、200+ 合作伙伴、NVIDIA FoundationStereo 结合。
- https://ai.meta.com/blog/egomimic-project-aria-georgia-tech-ego4d-robotics-embodied-ai/ — EgoMimic:90 分钟 Aria 数据 → 最高 400% 任务性能提升(联合训练口径)。
- https://www.eweek.com/news/meta-acquires-ari-humanoid-robotics-ai/ — Meta 收购机器人 AI 初创公司 ARI(2026-05)。
- https://techcrunch.com/2026/05/01/meta-buys-robotics-startup-to-bolster-its-humanoid-ai-ambitions/ — 对 ARI(Assured Robot Intelligence)收购的独立确认;团队加入 Meta Superintelligence Labs。
- https://evjang.com/2026/01/21/leaving-1x.html — Eric Jang 本人宣布离开 1X(2026-01),佐证创始人误传的说明。
- https://claru.ai/guides/how-to-collect-egocentric-video-data — 第一人称 vs 遥操作成本对比($10–30/小时 vs $50–200/小时操作员时间)(厂商来源)。
- https://claru.ai/blog/best-egocentric-data-providers — Claru 贡献者网络(10,000+ 贡献者、100+ 城市)与预计算增强层;供应商版图(厂商来源)。
- https://www.ycombinator.com/companies/cortex-ai — Cortex AI 市场:有偿场地承接、来自产业环境的第一人称 + 机器人轨迹数据。
- https://www.ycombinator.com/companies/sensei — Sensei:宣称人类演示采集约为遥操作成本 1/10、速度 2 倍;操作员网络模式。
- https://traceplane.ai/blog/we-audited-10-robotics-datasets — 对 10 个开放数据集的审计:OXE 黑帧子集、28/55 子数据集不可用、元数据缺陷。
- https://arxiv.org/pdf/2408.14037 — Re-Mix:为大规模模仿学习优化数据混合权重。
- https://arxiv.org/pdf/2603.09056 — 基于影响函数的演示筛选("Quality over Quantity",2026)。
- https://www.pi.website/blog/pi05 — π0.5 数据配比(约 400 小时移动操作演示),作为 PI 自建采集的锚点。
- https://www.newyorker.com/magazine/2026/07/06/are-humanoid-robots-ready-to-be-deployed — Witt:Neura 1,000+ 穿动捕服工人、Waymo 菲律宾遥操作领航员、1X 遥操作即数据引语(经 Wayback 快照阅读)。
- https://waymo.com/blog/2025/06/scaling-laws-in-autonomous-driving/ — Waymo 500,000 小时真实驾驶缩放研究(一手来源)。
