---
title: Physical AI 技术树
slug: tech-tree
updated: 2026-07-04
confidence: verified
lang: zh
source: ../wiki/tech-tree.md
---
> Physical AI 以分层依赖栈的方式演进:**硬件**(执行器、灵巧手、传感器、算力、电池)支撑起**感知**,感知输入**控制**(运动、全身控制、操作原语),而控制正日益被**学习**(模仿 + 强化学习 + 模拟到现实)所吸收;学习在规模化之后产生**基础模型**(VLA、世界模型、具身推理器),后者最终决定**部署**(工厂、物流,最终进入家庭)。截至 2026 年中,这个栈的成熟度并不均衡:运动能力已基本被模拟到现实的强化学习解决,VLA 架构正在收敛,今年预计出货 50,000 台以上人形机器人(TrendForce)——但约束条件已经转移到:(1)规模化的真实世界操作数据,(2)具备人类级触觉感知的灵巧手,(3)可靠性/在线率经济学(电池、MTBF、安全标准),以及(4)评测——饱和的仿真基准掩盖了闭源前沿模型与开放权重模型之间巨大的开放世界泛化差距。

## 如何阅读这棵技术树

- 每一层**依赖**其下的各层,并**解锁**其上的各层。
- "瓶颈" = 截至 2026-06 最限制该分支进展的约束条件,不一定是长期最难的问题。
- 姊妹深度页面:[硬件](hardware.md)、[数据](data.md)、[VLA 模型](vla-models.md)、[世界模型](world-models.md)、[仿真](simulation.md)、[操作](manipulation.md)、[运动](locomotion.md)、[人形机器人](humanoid-robots.md)、[开放问题](open-problems.md)。

## 第 0 层 — 硬件:物理基座

- **执行器(actuator)**:在配备五指手的高配人形机器人中,关节执行器占 BOM 的 30% 以上,基础配置中占 50% 以上(Interact Analysis,截至 2025)。旋转/线性执行器采用谐波减速器或行星滚柱丝杠传动;高精度丝杠的低产能是被明确点名的规模化瓶颈。执行器在功率密度、速度和耐久性上如今已*超过*人类肌肉——原始力量不再是约束。
- **灵巧手(dexterous hand)**:硬件中最薄弱的分支,也是最大的单项成本——约占人形机器人 BOM 的 31%(Bank of America Institute,截至 2025-04)。前沿部件示例:Sharpa Wave 触觉五指手,22 个自由度,被 NVIDIA 选为其 2026 参考人形机器人的手部。人手在分辨率、鲁棒性和成本上仍遥遥领先。
- **触觉感知(tactile sensing)**:2026 年的实验室成果(剑桥的石墨烯/液态金属皮肤,约 200 µm 金字塔触觉单元,可检测沙粒级接触,支持法向力 + 剪切力 + 滑移)在灵敏度/尺寸上比此前的柔性传感器提升约 10 倍(截至 2026-03,单一来源,未证实)。商用产品(XELA、GelSight 式光学方案)已经存在,但脆弱且昂贵;当今几乎没有任何量产机器人配备密集触觉皮肤出货。
- **算力(边缘端)**:NVIDIA Jetson AGX Thor T5000 — Blackwell GPU、2,070 FP4 TFLOPS、128 GB 统一内存、40–130 W、算力为 Jetson Orin 的 7.5 倍 — 是 2026 年人形机器人事实上的机载推理标准,足以在本地运行数十亿参数的 VLA。2025-08-25 正式发售,开发套件 $3,499 起;首发采用者包括 Agility Robotics、Amazon Robotics、Boston Dynamics、Figure、Hexagon 和 Meta,1X、OpenAI 和 Physical Intelligence 处于评估阶段(截至 2025-08)。
- **能源**:约 250–350 Wh/kg 的锂离子电池包可提供 1–4 小时的人形机器人活跃续航(许多机型实际上每次充电间隔仅 30–90 分钟);参考数据:Unitree H1 搭载 0.864 kWh 电池包,Tesla Optimus Gen 2 约 2.3 kWh(高镍 NMC),可支撑约 2 小时的动态运行(TrendForce/CnEVPost,2026-01)。工业客户期望 95–99% 的在线率,因此热插拔电池(Agility Digit、Apptronik Apollo)和充电编排只是权宜之计。固态电池是实现整班次(8 小时)作业所等待的突破口;TrendForce 预测到 2035 年人形机器人对固态电池的需求将达 74 GWh(截至 2026-01)。
- **平台/成本**:Unitree 的人形机器人售价大约比美国竞争对手低一个数量级(入门机型约 $4,290–$16k 档,截至 2026),并自报 2025 年出货 5,500 台以上人形机器人(Unitree 招股书数据;Omdia 独立统计约 4,200 台);商品化硬件的到来速度快于能驾驭它的智能。
- **解锁**:其上的一切。廉价可靠的平台(第 0 层)正是让学习研究(第 3 层)从纯仿真走向机群规模的关键。

## 第 1 层 — 感知

- **现状:基本上在搭 VLM 的顺风车。** 现代技术栈使用预训练的视觉(-语言)骨干网络而非定制检测流水线;多视角 RGB + 深度 + 本体感知已成标配,例如参考设计的立体头部相机(140° 水平 / 102° 垂直)。
- **具身推理模型(embodied reasoning model)** 如今在原始视觉之上提供"感知即服务":Gemini Robotics-ER 1.5(2025-09,通过 Gemini API 预览)支持指点、基于可供性的 2D 输出和多步规划;ER 1.6(2026-04-14)新增多相机理解、成功检测和仪表读数(agentic vision 下成功率 93%),并宣称 1.5 代在 15 项具身推理基准上达到 SOTA。
- **仍存差距**:富接触感知(力、滑移、纹理——依赖第 0 层的触觉硬件)、面向自主数据采集的可靠成功检测,以及长时程空间记忆(Physical Intelligence 的 MEM,2026-03,面向 10 分钟以上的任务)。
- **解锁**:感知质量直接决定遮挡/杂乱环境下的操作能力(第 2/3 层),以及将非结构化视频自动标注为训练数据的能力(第 3 层)。

## 第 2 层 — 控制

- **运动:实际上已是被解决的研究问题。** 带大规模域随机化的模拟到现实(sim2real)强化学习是标准配方;FastTD3/FastSAC 式离策略强化学习如今可在一块 RTX 4090 上用数千个并行环境、约 15 分钟训练出可部署的人形行走(arXiv 2512.01996,在 Unitree G1 和 Booster T1 上演示,截至 2025 年末)。参见[运动](locomotion.md)。
- **全身控制(WBC)**:潜在指令接口让高层策略驱动完整的 30–75 自由度身体;LeVERB(2025)首次展示了从视觉-语言输入实现零样本模拟到现实全身控制。多仿真器动力学随机化(PolySim)进一步缩小了模拟到现实的差距。
- **操作控制**:已知刚性物体的抓取已经可用;灵巧手内操作、工具使用、可变形物体处理和滑移恢复仍停留在研究级——同时受制于手/触觉(第 0 层)和数据(第 3 层)。参见[操作](manipulation.md)。
- **解锁**:运动 + WBC 的解决让人形机器人厂商得以转向操作和自主性上的竞争;它也使移动操作(π0.5 式的"清理一间没见过的厨房")第一次成为可能。

## 第 3 层 — 学习:数据引擎与算法

- **整棵树的共识瓶颈就在这里:数据,而非算力。** 机器人策略需要成对的观测-动作流,而这种数据在互联网规模上并不存在。
- **遥操作(teleoperation)** 是金标准,但每操作员小时仅产出约 5–50 条演示;并行化站点可达每天约 200–500 条演示。前沿实验室(Physical Intelligence、NVIDIA GR00T、Google DeepMind)瞄准百万演示规模,此时约束转向后勤:标定、格式一致性、跨数十个工位的质检(截至 2026)。
- **聚合数据集**:Open X-Embodiment — 100 万+ 回合、22+ 种机器人、33 家机构 — 证明了跨具身迁移优于单机器人训练,但社区也承认 OXE 中大量是低质量演示数据,且没有公认的质量度量。DROID 约 76k 条轨迹;RH20T 110k+ 条富接触序列。
- **2026 年涌现的效率倍增器**:策略辅助遥操作(部分训练好的策略完成简单子任务,人类负责难点——号称每任务人类演示需求减少 5–10 倍)、带机器人辅助复位的自主采集、人类视频重定向,以及来自世界模型的合成数据(第 4 层反哺下层)。
- **合成数据杠杆,具体来说**:NVIDIA GR00T N1(2025-03,arXiv 2503.14734)在其数据金字塔"塔尖"仅使用了 88 小时自采人形遥操作数据(Fourier GR-1)——通过神经生成视频扩增约 10 倍至 827 小时——外加 11 小时内生成的 780k 条 DexMimicGen/Isaac Sim 仿真轨迹(约 6,500 小时);外部真实数据集(Open X-Embodiment 子集、140k 条 AgiBot-Alpha 轨迹)也在配比之中。NVIDIA 报告称合成数据与真实数据结合比仅用真实数据性能提升约 40%。近期共识认为模拟到现实的成功更多取决于训练数据的多样性,而非仿真物理的精确性(未证实)。
- **真实机器人上的强化学习回归**:π*0.6 + RECAP(2025-11-17,arXiv 2511.14759)用优势条件化强化学习在演示、遥操作纠正和自主执行数据上训练 VLA——在最难的任务上吞吐量翻倍以上、失败率约减半,实现了数小时不间断的意式咖啡服务、在没见过的家庭中叠衣服、在工厂装配纸箱;π 的"RL token"工作(2026-03-19)从 VLA 中提取快速在线强化学习接口;DexPIE 等 2026 年论文实现了基于真实世界经验的稳定灵巧策略改进。
- **立场论文批评**(arXiv 2606.06556,2026):该领域现在是"以策略扩展为中心",而本应"以落地(grounding)为中心"——缺失的机制是能把非结构化行为(互联网视频、可穿戴设备、部署失败案例)自动标注为机器人监督信号的数据引擎、保持任务语义的重定向、物理落地的世界模型,以及自我改进的部署闭环。
- **解锁**:第 4 层的每一项基础模型能力都是本层吞吐量的下游产物。

## 第 4 层 — 基础模型

### VLA(视觉-语言-动作)

- 领域增速:ICLR 的 VLA 投稿量从 1 篇(2024)→ 9 篇(2025)→ **164 篇(2026)** — 同比增长 18 倍。
- **模型系列示例**:π0(2024-10)→ π0.5 开放世界泛化(2025-04)→ π0.6 +RL(2025-11)→ π0.7 "可操控的基础模型,泛化能力的阶跃式提升"(2026-04-16)。Google:Gemini Robotics 1.5(VLA)+ Robotics-ER 1.5/1.6(推理器),把技术栈拆分为思考者/执行者。NVIDIA:Isaac GR00T 开放模型 + Cosmos 3 世界模型(2026-05-31)。中国:LingBot-VLA(蚂蚁集团,2026-01)、RDT-1B、ABot-M0。参见 [VLA 模型](vla-models.md)和[最新进展](state-of-the-art.md)。
- **架构趋势(截至 ICLR 2026)**:从自回归 token 解码转向**离散扩散(discrete diffusion)** 动作生成(并行解码长动作块);具身思维链(子任务、检测框、轨迹)提升可解释性;更好的动作分词器(FAST、RVQ/B-spline 的后继者如 FASTer、OMNISAT)。
- **基准饱和问题**:LIBERO 达到 95–98%,CALVIN >4.0 成为标准——仿真基准已无区分度。真实差距在于:开放权重 VLA 在仿真中可比肩闭源模型,但在新物体、没见过的场景和改述指令上明显落后于 Gemini Robotics / π0.5 级别的闭源模型。

### 世界模型

- Genie 3(DeepMind,2025-08):以 24 fps 实时生成可交互 3D 世界;在机器人领域的主要用途是生成多样化的第一人称训练环境和边缘案例;仍处于受限研究预览阶段(截至 2026 年初)。Waymo 将其改造为驾驶世界模型(2026-02)(未证实)。
- NVIDIA Cosmos 3(技术报告 2026-06,arXiv 2606.02800):全模态混合 Transformer(mixture-of-transformers),在单一架构中统一语言、图像、视频、音频和动作;开放权重/代码/数据集;发布时宣称是 RoboArena 上最强的策略模型。将视频世界模型定位为合成数据生成器与策略骨干的双重角色(面向视觉运动控制的 "Cosmos policy" 微调)。Cosmos WFM 到 2026-01 下载量超 200 万次,训练数据约为 2,000 万小时真实世界视频(NVIDIA,截至 2026-01)。
- 基于世界模型的策略优化(WMPO 及其后继)在学习到的模拟器内训练/评估 VLA——这是摆脱真实世界数据瓶颈的预期逃生通道,前提是物理保真度(接触、力)可以被信任。参见[世界模型](world-models.md)。
- **解锁**:廉价的策略评估(真实世界试验是最稀缺的资源——前沿实验室的部分优势正来自机群访问权),以及可能无限的合成经验。

## 第 5 层 — 部署

- NVIDIA 的 Jensen Huang 在 CES 2026 上宣告了 Physical AI 的 "ChatGPT 时刻"。Counterpoint Research 估计 **2025 年全球安装约 16,000 台人形机器人**(80% 以上在中国),并预测 **2027 年装机量超过 100,000 台**;TrendForce 另行预测 **2026 年人形机器人出货超 50,000 台**(同比增长 700% 以上)(截至 2026-01)。此前聚合媒体的"Counterpoint:2026 年 5 万台商用运行"说法混淆了这两个口径。
- **旗舰部署案例(截至 2026-06)**:Figure(02/03)+ Helix 自 2024 年起在 BMW Spartanburg 工厂运行;BMW 报告 Spartanburg 试点在 2025 年以毫米级精度搬运了 90,000 多个部件、累计运行 1,250 小时,支撑了 30,000 多辆 BMW X3 的生产(BMW 新闻稿,2026-02-27)。BMW 在德国的首台人形机器人是 Hexagon Robotics 的 AEON,部署于 Leipzig 工厂——2025-12 初步测试,2026 年夏起进入高压电池装配试点——同时设立了新的 BMW "生产领域 Physical AI 能力中心"(BMW 新闻稿,2026-02);关于 Figure 自身于 2026-03 扩展到 Leipzig 的报道与 BMW 自己的公告相矛盾(未证实)。Agility Robotics 与 Toyota Motor Manufacturing Canada 签署了 RaaS 协议(2026-02)(未证实)。Figure 的 BotQ 工厂据称每约 90 分钟下线一台机器人(截至 2026-04,未证实)。Tesla Optimus:Musk 在 2026-01 的 Q4 财报电话会上承认 Optimus "尚未在我们的工厂中实质性投入使用";Gen 3 计划 2026 年夏启动量产,最终定价 $20k–$30k(预估,未证实)。
- **资本与平台(截至 2026-06)**:Figure — 超 $1B 的 C 轮,投后估值 $39B(2025-09)。Unitree — 2026-03-20 提交上海科创板 IPO 申请,拟募资 ¥4.2B(约 $608–610M);经创纪录的 73 天快速通道后于 2026-06-01 过会,目标估值约 $6.2B(Caixin,截至 2026-05);2025 年营收 ¥1.7B,人形机器人占营收 51.5%。Agility Robotics — 通过约 $2.5B 的 SPAC 上市,手握约 $300M 预订单(2026-06),成为首家美股上市的纯人形机器人公司。AgiBot(智元机器人)— 计划以约 $5–6.4B 估值赴港 IPO。参见[投资](investment.md)、[中国版图](landscape-china.md)、[组织机构](organizations.md)。
- **研究平台标准化**:NVIDIA Isaac GR00T 参考人形机器人(2026-05-31/06-01 于 GTC Taipei 发布):Unitree H2 Plus 底盘(31 自由度,约 6 英尺,150 磅)+ Sharpa Wave 手(22 自由度,全身共 75 自由度)+ Jetson Thor T5000 + 完整 Isaac 技术栈(Teleop、GR00T 模型、Sim/Lab、ROS);2026 年末起可从 Unitree 购买;合作伙伴包括 Ai2、ETH Zurich、Stanford、UCSD。
- **部署门槛**:在线率经济学(电池、MTBF)、安全认证 — ISO 10218:2025 和 ANSI/A3 R15.06-2025 已适用,但针对动态平衡人形机器人的成熟标准尚不存在(ISO 25785-1 制定中)— 外加保险,以及证明相对人工的 $/任务成本优势。

## 依赖图:什么解锁什么

- 廉价执行器 + 边缘算力(L0)→ 平价研究用人形机器人 → **机群规模数据采集**(L3)
- 触觉皮肤 + 更好的手(L0)→ 富接触感知(L1)→ **灵巧操作策略**(L2/L3)— 当前受阻
- GPU 并行仿真(Isaac Lab)→ 15 分钟模拟到现实强化学习 → **运动/WBC 的解决**(L2)→ 移动操作(L4)
- VLM 预训练(相邻技术树)→ VLA 骨干 + 具身推理器(L4)→ 语言指挥的机器人(L5)
- 遥操作数据引擎(L3)→ 通用 VLA(L4)→ 策略辅助遥操作 → **更廉价的数据**(L3,自我强化循环)
- 世界模型(L4)→ 合成数据 + 离线评估 → 同时缓解数据瓶颈和真实试验瓶颈(L3)
- 部署机群(L5)→ 失败/纠正数据 → 自我改进闭环(L3)— 每个实验室都在追逐的飞轮;截至 2026 大多仍属愿景

## 各分支瓶颈(截至 2026-06)

| 分支 | 状态 | 当前瓶颈 | 可能的解锁 |
|---|---|---|---|
| 执行器 | 成熟,成本驱动 | 精密丝杠/减速器产能;占 BOM 30% 以上 | 中国供应链规模;Unitree 式定价 |
| 手与触觉 | **最薄弱环节** | 密集、耐用、廉价的触觉皮肤;手的鲁棒性 | 石墨烯/液态金属皮肤;规模化光学触觉单元 |
| 能源 | 制约运营 | 1–4 小时续航 vs 8 小时班次;250–350 Wh/kg 锂离子 | 固态电池;热插拔换电体系 |
| 边缘算力 | 非瓶颈 | —(Jetson Thor:2,070 FP4 TFLOPS,128 GB) | — |
| 感知 | 借力 VLM,较强 | 接触/力感知;成功检测 | 触觉硬件 + ER 级推理器 |
| 运动/WBC | 基本解决 | 长尾地形、鲁棒性认证 | 多仿真器随机化;机上自适应 |
| 操作 | 研究级 | 不确定性下的灵巧性;可变形物体;恢复能力 | 触觉 + 真实世界 RL + 更好的手 |
| 数据 | **头号瓶颈** | 遥操作吞吐(5–50 回合/操作员小时);无质量度量 | 策略辅助遥操作;视频自动标注;世界模型合成 |
| VLA | 快速收敛 | 零样本泛化差距;基准饱和 | 离散扩散;具身思维链;真实世界评测 |
| 世界模型 | 有前景但不成熟 | 物理保真度(接触/力)vs 视觉逼真度 | 物理落地的世界模型;交互轨迹训练 |
| 部署 | 商用早期 | 在线率、安全标准(人形 ISO 尚缺)、$/任务 | ISO 25785-1;换电;机群学习 |
| 评测 | 被低估的阻碍 | 仿真基准饱和;真实试验稀缺且依赖人工 | 现实到仿真评测(PolaRiS 式);标准化机群 |

## 跨层变数

- **闭源与开源差距**:闭源前沿模型(Gemini Robotics、π0.x)在开放世界泛化上领先,主要依靠专有数据机群——护城河是数据获取,而非架构(ICLR 2026 分析)。
- **中国成本曲线**:中国厂商主导了 2025 年的出货量,售价低约 10 倍;如果智能通过开放的 GR00T 式技术栈商品化,硬件成本领先地位可能决定市场归属。参见[中国版图](landscape-china.md)。
- **机器人的上下文学习(in-context learning)** 在当前 VLA 研究中几乎缺席,尽管它正是让 LLM 变得普遍有用的机制——一个显眼的开放分支(截至 ICLR 2026)。
- **自我改进的部署闭环**(部署数据 → 自动标注 → 再训练)将瓦解 L3 瓶颈;每家大实验室都宣称在建,但尚无人发表令人信服的规模化闭环(截至 2026-06)。

## 来源

- https://nvidianews.nvidia.com/news/nvidia-open-humanoid-robot-reference-design — Isaac GR00T 参考人形机器人规格(H2 Plus、Sharpa 手、Jetson Thor T5000、2,070 FP4 TFLOPS)、2026 年末上市、合作伙伴
- https://www.pi.website/blog — Physical Intelligence 发布时间线:π0(2024-10)、π0.5(2025-04)、π0.6 +RL(2025-11)、π0.7(2026-04-16)、MEM 记忆(2026-03)、FAST 分词器
- https://mbreuss.github.io/blog_post_iclr_26_vla.html — ICLR 2026 VLA 分析:164 篇投稿、离散扩散趋势、LIBERO 95–98% 饱和、开源/闭源泛化差距、数据质量批评
- https://deepmind.google/blog/gemini-robotics-er-1-6/ — Gemini Robotics-ER 1.6(2026-04-14):多视角、成功检测、仪表读数 93%
- https://www.infoq.com/news/2025/09/deepmind-gemini-robotics/ — Gemini Robotics-ER 1.5 发布、15 项具身基准 SOTA、API 可用性
- https://arxiv.org/html/2606.06556v1 — "Robots Need More Than VLAs & World Models":以落地为中心的批评;OXE 100 万+/22 种具身、DROID 约 76k、RH20T 110k+
- https://arxiv.org/pdf/2512.01996 — FastTD3/FastSAC:单块 RTX 4090 约 15 分钟训练模拟到现实人形运动(Unitree G1、Booster T1)
- https://people.eecs.berkeley.edu/~sastry/pubs/Pdfs%20of%202025/XueLeVERB2025.pdf — LeVERB:首个零样本模拟到现实视觉-语言全身控制
- https://interactanalysis.com/insight/joint-actuators-the-fundamental-component-for-humanoid-robots-power-and-dexterity/ — 执行器占人形机器人 BOM 30% 以上(最高超 50%)
- https://claru.ai/training-data/teleoperation — 遥操作吞吐 5–50 回合/操作员小时;百万演示目标;后勤瓶颈
- https://www.shaip.com/blog/robot-training-data-strategy/ — 遥操作 vs 仿真 vs 人类视频数据策略;策略辅助遥操作 5–10 倍效率声称
- https://techxplore.com/news/2026-03-graphene-based-artificial-skin-human.html — 剑桥石墨烯/液态金属触觉皮肤,灵敏度/尺寸提升约 10 倍(2026-03)
- https://www.labellerr.com/blog/genie-3-google-deepmind-world-model/ — Genie 3(2025-08):交互式世界模型,第一人称机器人训练数据用例
- https://www.vaasblock.com/news/humanoid-robotics-figure-tesla-optimus-commercial-reality-2026/ — Figure 03/Helix 在 BMW Spartanburg;Optimus 据 2026-01 财报电话会"不具实质性"(聚合来源;其 Figure-Leipzig 和 "Counterpoint 2026 年 5 万台运行" 说法与 BMW 和 Counterpoint 自己的发布相矛盾)
- https://counterpointresearch.com/en/insights/Global-Humanoid-Robot-Installations-Reach-16,000-Units-in-2025-as-Mass-Production-Picks-Pace — Counterpoint 一手来源:2025 年安装约 16,000 台人形机器人(80% 以上在中国),预测 2027 年装机量超 100,000 台
- https://techmarketbriefs.com/pre-ipo/figure-ai/ — Figure 超 $1B C 轮、投后估值 $39B(2025-09);BotQ 产能
- https://restofworld.org/2026/unitree-china-humanoid-robot-shanghai-ipo/ — Unitree 2026-03-20 提交 IPO 申请,募资 ¥4.2B(约 $610M)
- https://www.caixinglobal.com/2026-05-26/unitree-fast-tracks-shanghai-ipo-with-target-valuation-of-62-billion-102447449.html — Unitree 快速过会、目标估值约 $6.2B、2025 年出货 5,500 台人形机器人、2025 年财务数据
- https://kraneshares.com/a-complete-guide-to-unitree-robotics-2026-ipo-why-it-matters-for-star-market-etf-kstr-humanoid-robotics-etf-koid/ — Unitree 2025 年出货 5,500+ 台人形机器人、估值目标、中国出货量主导地位
- https://autonews.gasgoo.com/articles/market-industry/annual-champion-changes-hands-unitree-announces-over-5500-humanoid-robot-shipments-2014711162140991489 — Unitree 招股书 5,500+ "纯人形" vs Omdia 约 4,200 台统计(AgiBot 约 5,100 台);分类/口径争议
- https://www.forbes.com/sites/johnkoetsier/2026/06/24/first-humanoid-robot-maker-goes-public-in-us-25-billion-deal-new-robot-300-million-in-pre-orders/ — Agility Robotics $2.5B SPAC、$300M 预订单(2026-06)
- https://techcrunch.com/2026/06/24/agility-robotics-plans-to-go-public-via-spac-in-a-2-5b-deal/ — Agility SPAC 佐证:Churchill Capital Corp XI、约 $620M 募资、股票代码 AGLT
- https://theresarobotforthat.com/blog/humanoid-robot-safety-standards-2026/ — ISO 10218:2025、ANSI/A3 R15.06-2025、面向动态平衡机器人的 ISO 25785-1 制定中
- https://stdbattery.com/blog/detail/2026-humanoid-robot-market-status-outlook-lithium-battery-pack-core-specifications — 锂离子 250–350 Wh/kg、1–4 小时续航约束
- https://www.marktechpost.com/2026/01/29/ant-group-releases-lingbot-vla-a-vision-language-action-foundation-model-for-real-world-robot-manipulation/ — LingBot-VLA(蚂蚁集团,2026-01)
- https://www.buildfastwithai.com/blogs/nvidia-cosmos-3-isaac-groot-physical-ai-2026 — Cosmos 3 发布时间(2026-05-31),与 GR00T 参考机器人同期
- https://arxiv.org/abs/2511.14759 — π*0.6/RECAP 论文:优势条件化强化学习,最难任务上吞吐量 >2 倍、失败率约减半,意式咖啡/叠衣/装箱结果
- https://arxiv.org/abs/2606.02800 — Cosmos 3 技术报告:全模态混合 Transformer、开放发布、RoboArena 策略声称
- https://developer.nvidia.com/blog/scale-synthetic-data-and-physical-ai-reasoning-with-nvidia-cosmos-world-foundation-models/ — Cosmos WFM 规模:下载量 200 万+、约 2,000 万小时训练视频(截至 2026-01)
- https://nvidianews.nvidia.com/news/nvidia-blackwell-powered-jetson-thor-now-available-accelerating-the-age-of-general-robotics — Jetson Thor 2025-08-25 正式发售、$3,499 开发套件、7.5 倍于 Orin、首发采用者名单
- https://www.press.bmwgroup.com/global/article/detail/T0455864EN/bmw-group-to-deploy-humanoid-robots-in-production-in-germany-for-the-first-time?language=en — BMW 一手来源:Leipzig AEON(Hexagon)时间线、Spartanburg 90k+ 部件 / 1,250 运行小时、Physical AI 能力中心
- https://arxiv.org/abs/2503.14734 — GR00T N1 论文:88 小时自采 GR-1 遥操作数据经神经视频扩增约 10 倍至 827 小时;训练配比还含 OXE 子集 + 140k AgiBot-Alpha 真实轨迹;780k DexMimicGen 仿真轨迹
- https://nvidianews.nvidia.com/news/nvidia-isaac-gr00t-n1-open-humanoid-robot-foundation-model-simulation-frameworks — 11 小时内生成 780k 条合成轨迹(约 6,500 小时);较仅用真实数据提升 40%
- https://blog.pebblous.ai/project/AgenticAI/isaac-groot/en/ — GR00T N1 数据配比解读(二手来源)
- https://institute.bankofamerica.com/content/dam/transformation/humanoid-robots.pdf — 灵巧手约占人形机器人 BOM 的 31%,为最大单一部件
- https://www.trendforce.com/presscenter/news/20260128-12902.html — 人形机器人电池续航(<2 kWh,2–4 小时)、2035 年 74 GWh 固态电池需求预测、2026 年 5 万+ 出货预测
- https://cnevpost.com/2026/01/28/demand-for-solid-state-batteries-humanoid-robots-74-gwh-2035/ — 佐证 H1 0.864 kWh 和 Optimus Gen 2 2.3 kWh(约 2 小时动态运行)参考数据
- https://arxiv.org/abs/2510.03342 — Gemini Robotics 1.5:思考者/执行者拆分、具身推理、跨具身动作迁移
