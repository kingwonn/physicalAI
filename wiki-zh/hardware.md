---
title: 硬件基座
slug: hardware
updated: 2026-07-03
confidence: verified
lang: zh
source: ../wiki/hardware.md
---
> Physical AI 的硬件基座——执行器、灵巧手(dexterous hand)、触觉/力传感、机载算力和电池——到 2026 年中已收敛为一套可辨识的"标准栈":上肢采用谐波减速器或准直驱(QDD)旋转关节,髋/膝/踝采用行星滚柱丝杠直线执行器,20+ 自由度腱驱动灵巧手配指尖触觉传感,机载推理用 NVIDIA Jetson(Orin → Thor),约 2 kWh 锂电池组提供 2–5 小时续航。BOM 成本快速下降(Goldman Sachs 测得制造成本同比下降约 40%;Tesla 目标规模化后约 $20k/台),但即便是美国制造的人形机器人也有大约 70% 的零部件可追溯到中国供应商,而中国对稀土磁体加工约 90% 的掌控在 2025 年出口管制扰乱 Optimus 生产时被证明是一个现实的卡点。整机平台见[人形机器人](humanoid-robots.md),供应链地理格局见[版图:中国](landscape-china.md)。

## 执行器

行业已基本收敛到一种**混合关节架构**:手臂和躯干用旋转式谐波/QDD 模组,腿部大负载关节用直线滚柱丝杠执行器。

| 执行器类型 | 机构 | 优势 | 劣势 | 典型位置 |
|---|---|---|---|---|
| 谐波(应变波)减速器 | 柔轮 + 波发生器,减速比 50–160:1 | 零背隙(≤15 角秒)、紧凑、大减速比 | 抗冲击差、柔轮疲劳、不可反驱 | 手臂、手腕、躯干 |
| 准直驱(QDD) | 高扭矩电机 + 低减速比(约 6–10:1)行星齿轮 | 可反驱、柔顺、高带宽力控、耐冲击 | 单位体积扭矩密度较低,电机质量/成本高 | 腿部(MIT Cheetah 谱系),部分全 QDD 设计 |
| 行星齿轮箱 | 多级行星轮系 | 载荷分布在多个齿上、耐冲击、便宜 | 有背隙,高减速比时体积大 | 髋、膝(旋转方案) |
| 行星滚柱丝杠(PRS) | 螺纹滚柱实现旋转→直线转换 | 极高的力密度、刚度和抗冲击载荷能力 | 精密磨削是制造瓶颈;昂贵 | 腿部直线执行器(髋、膝、踝) |
| 摆线 / RV 减速器 | 摆线凸轮减速 | 抗冲击能力强、刚性好 | 重量、成本、复杂度 | 部分髋/腰;源自工业机械臂 |

- 据中国供应链报道,Tesla Optimus 每台使用约 28 个执行器(旋转 + 直线混合),其中腿部约 14 个反向式行星滚柱丝杠,手部约 20 个空心杯电机(截至 2026-06,未证实)。
- QDD(由 MIT Mini Cheetah 谱系开创)以减速比换取可反驱性——这是富接触步态和安全人机交互的关键;多数 2025–26 年的人形机器人在腿部或全身采用 QDD 式低减速比关节(如 Unitree)。
- Figure 03 的执行器速度约为 Figure 02 的 2 倍,扭矩密度(Nm/kg)也有提升(公司口径,截至 2025-10)。
- PRS 供给是最紧的执行器瓶颈:精密螺纹磨床和航空级合金稀缺;中国厂商贝特科技(Beite Technology)正在昆山建设 18.5 亿元(约 $260M)工厂,目标年产 260 万套 PRS,预计 2026 年量产(中国行业报道,多家媒体)。
- 中国关节模组供应商 EYOU 宣称 2025 年在谐波和行星产品线共交付 95,000 套关节模组(单一来源,未证实)。
- 无稀土电机(铁氧体辅助)仍停留在愿景阶段:达到 NdFeB 输出水平的设计要重约 30%,而截至 2026 年初,尽管 Tesla 2023 年有过宣布,尚无确认已部署的商用无稀土驱动单元。

## 灵巧手

灵巧手是迭代最快的子系统——软件侧见[操作](manipulation.md)。

| 灵巧手(截至 2026-06) | 自由度 | 驱动方式 | 触觉 | 备注 |
|---|---|---|---|---|
| Tesla Optimus Gen 3 手 | 22(手)+ 3(腕) | 每前臂约 25 个执行器(共 50 个),腱驱动,执行器置于前臂 | 更大范围触觉覆盖开发中 | 执行器数量为 Gen 2(11 自由度)的 4.5 倍;演示过接住物体(2025–26) |
| Figure 03 手 | 每手 16+(以 F02 为基线);更柔软的自适应指尖 | 手内 + 掌部 | 指尖传感器可检测约 3 g 力;每手一枚掌部相机 | 主相机被遮挡时,掌部相机提供近距离视觉 |
| Unitree Dex5-1 | 20(16 主动 + 4 被动) | 手指直驱,约 1 kg | 可选 94 个压力点,1 kHz 更新率 | 指尖力约 10 N,重复定位精度约 1 mm;作为 H1/G1 选配件销售 |
| Shadow Dexterous Hand | 24 | 腱驱动,有气动/电动版本 | 可选 BioTac/GelSight | 自 OpenAI 魔方时代以来的科研基准 |
| Inspire RH56 系列 | 约 6 个主动 | 连杆机构 | 基础力感知 | 众多中国人形机器人上的低成本主力 |

- 设计趋势:把执行器从手部移到前臂、以腱传动连接(Optimus Gen 3、Figure)——为传感腾出手部空间、降低手部惯量、缓解热限制。
- 第二个趋势:工厂试点用便宜的欠驱动手(约 6 自由度),通用操作用 20+ 自由度的全驱动手;市场随之分层,中国厂商(Inspire、Unitree、BrainCo)持续压低价格。

## 传感

**视觉触觉(vision-based tactile,VBT)**——相机观测带照明的凝胶表皮的形变,给出高分辨率接触几何:
- GelSight(MIT 衍生公司)是参考技术;空间分辨率达微米级。
- **Meta AI × GelSight Digit 360**(2024-10 发布):指尖形态的 VBT 传感器,具备 18+ 种感知模态、全向指尖形变捕捉、力灵敏度低至约 1 mN;定位为带开放工具链的科研标准。
- 截至 2026 年中,VBT 基本仍是科研级;量产人形机器人出于耐用性考虑搭载更简单的压阻/电容式指尖阵列(Figure 明确称耐用性是其自研传感器的设计出发点)。

**量产触觉**(截至 2026):
- Figure 03:自研指尖传感器可检测约 3 g 的力,外加掌部相机(冗余近距离视觉)。
- Unitree Dex5-1:可选 94 点压力阵列,1 kHz。
- Optimus Gen 3:声称正在推进覆盖面更大的触觉传感集成(截至 2026-06,未证实)。

**力/力矩传感**:
- 六轴力/力矩(F/T)传感器安装在手腕/脚踝用于平衡和柔顺接触;历史上由 ATI、Schunk、AMTI 主导,单价 $3k–$10k+。
- 中国供应商(Hypersen、坤维、柯力、宇立)正在放量:2024 年全球六轴产品销量约 6 万个,中国约 1.7 万个(同比 +40%);一份预测称人形机器人力矩传感器市场到 2032 年达 $7.9B,CAGR 48%(市场研究数据,未证实)。
- 关节级力矩传感与基于电流的力矩估计仍是一个开放的成本/性能权衡;QDD 设计通常省去专用传感器,由电机电流估计力矩。

## 机载算力

NVIDIA 是事实标准;其生态打法见[组织机构](organizations.md)。

| 平台 | AI 算力 | 内存 | 功耗 | 价格(截至 2026-01) | 状态 |
|---|---|---|---|---|---|
| NVIDIA Jetson AGX Orin | 275 TOPS(INT8) | 64 GB | 15–60 W | 开发套件约 $1,999 | 2023–25 年的主力(Walker S2 及众多机型) |
| NVIDIA Jetson AGX Thor(T5000) | 2,070 TFLOPS(FP4,稀疏) | 128 GB LPDDR5X | 40–130 W | 开发套件 $3,499(2025-08) | 2025-08-25 正式上市;算力 7.5× Orin,能效 3.5×;14 核 Neoverse-V3AE |
| NVIDIA Jetson T4000 | 1,200 TFLOPS(FP4,稀疏) | 64 GB | 40–70 W | $1,999(1k 件起) | 中档 Thor 模组,2026-01 发布(CES) |
| Tesla AI5(自研) | 未公开;Musk 称在 Tesla 工作负载下推理约达 H100 级,约 10× AI4 | — | — | — | 2026-04-15 流片(Samsung + TSMC 代工);量产目标 2027 年中后期,初期面向 Optimus 与算力集群而非车辆 |

- Thor 的 128 GB 内存是对 Physical AI 的头条意义:可在设备端装下数十亿参数的 [VLA 模型](vla-models.md)外加感知。早期采用者(截至 2025-08):Agility、Amazon Robotics、Boston Dynamics、Figure、Caterpillar、Meta;1X、OpenAI、Physical Intelligence 在评估中。
- 常见模式是**分脑式算力**:实时控制器 CPU(x86 或 MCU,约 1 kHz 硬实时关节控制)+ 一块 NVIDIA 模组负责感知/策略——例如 UBTECH Walker S2 用 Intel i7-1185G7 搭配 Jetson AGX Orin 64 GB。
- 中国平台(地平线 Horizon Robotics、黑芝麻 Black Sesame、华为昇腾 Ascend)被定位为国产替代,但截至 2026 年中尚无广泛采用的人形机器人设计导入的报道(基于证据缺失,未证实)。
- 前沿架构问题——推理有多少在机载、多少在机外运行——见[开放问题](open-problems.md)。

## 电池与续航

| 机器人(截至 2026-06) | 电池组 | 宣称续航 | 充电/换电 |
|---|---|---|---|
| Tesla Optimus | 2.3 kWh,52 V | 轻负载工作宣称约 8 h(未证实) | 插电充电 |
| Figure 03 | 2.3 kWh | 峰值性能下宣称约 5 h(实际估计约 3–4 h,未证实) | 足部线圈 2 kW 感应无线充电;自主对接 |
| UBTECH Walker S2 | 双 48 V 锂电池组 | 每组约 2 h | **约 3 分钟自主换电**——机器人自行更换电池,支持 24/7 运行 |
| Unitree G1 | 9 Ah(约 0.8 kWh) | 约 2 h | 快拆电池组 |
| Apptronik Apollo | 可换电池组 | 每组约 4 h | 热插拔设计 |

- 现实检验:多数商用人形机器人单次充电实际续航 1.5–5 h,取决于任务强度;重度操作或快速行走会把标称数字大约砍半。
- 车队运营方靠热插拔轮换或机会式充电(Figure 的无线充电坞)解决续航,而不是更大的电池——电池质量会放大"质量惩罚螺旋"(更重的电池 → 更大的执行器 → 更重的机器人)。
- 随着机器人进入家庭和工厂,电池认证(UN38.3、多层 BMS 保护)在 2025 年成为营销卖点(Figure 03)。

## BOM 成本趋势

- Goldman Sachs(2024-02 报告):人形机器人制造成本同比下降约 40%——从 $50k–$250k/台降至约一年后的 $30k–$150k——远超此前 15–20%/年的预期;这是其市场预测上调超 6 倍($6B → 2035 年 $38B,出货量 4 倍至 140 万台)的关键驱动因素。
- Tesla 宣称的 Optimus 量产成本目标:约 $20,000/台(截至 2026)。流传的一份 BOM 拆分(未证实,来自 36kr):执行器约 35%,传感器及其他约 20%,丝杠/滚柱丝杠约 18%,减速器约 15%,电机约 12%。
- 市场售价(截至 2026-06):Unitree G1 起价约 $13.5k–16k(EDU 配置 $43.9k–$73.9k);多数工业级人形机器人集中在 $20k–$30k;Boston Dynamics 释放信号称 Atlas 定价低于约 $320k("低于两名美国制造业工人两年的工资";无公开 MSRP,仅直销)。Unitree 于 2024-05 以 $16k 发售 G1,入门价格基本持平而能力显著提升。
- 中国制造商的单台成本大约是西方同类产品的 ⅓–½(Morgan Stanley,截至 2026),重演 EV 成本剧本:一体化的国内供应链 + 庞大的国内试点部署。
- 即便算力能力跃升,算力在 BOM 中的占比反而在缩小(T4000 模组 $1,999,而 $20k 的机器人中执行器约占 $7k)。
- 成本曲线和出货量预测直接支撑[投资](investment.md)论点;产能扩张尝试(Figure BotQ:初期年产 1.2 万台、四年 10 万台;Tesla Fremont 产线改造目标约 100 万台/年,量产计划 2026 年底启动(未证实))在[最新进展](state-of-the-art.md)中跟踪。

## 供应链与中国的零部件主导地位

- **稀土磁体**:中国控制约 69% 的稀土开采和约 90% 的磁体加工/精炼(截至 2025,McKinsey)。平均每台人形机器人含约 0.9 kg 稀土金属(McKinsey;人形尺寸机器人 NdPr 最高约 1.3 kg);据报道每台 Optimus 的 NdFeB 磁体总质量约 3.5 kg。中国 2025-04 对重稀土磁体的出口管制直接扰乱了 Optimus 生产——Musk 在 2025-04-22 财报电话会上确认此事,称 Tesla 正在申请出口许可。
- **减速器**:日本 Harmonic Drive Systems 和 Nabtesco 仍领跑高端;中国厂商(苏州绿的谐波、浙江双环旗下 FORE)凭价格在中等精度档位抢占份额。
- **滚柱丝杠**:历史上是欧洲/日本垄断(Rollvis、GSA、Ewellix、NSK);中国新进入者(五洲新春、贝特、恒立)正激进扩产——关键约束是精密螺纹磨床,而磨床本身供应受限。
- **更广泛的份额**(McKinsey,截至 2025):在人形机器人价值链中,中国占精密轴承约 40%、电机约 35%、功率电子约 30%。
- Tesla Optimus 约 70% 的零部件可追溯到中国供应商,涵盖执行器总成(拓普集团、三花)、传动(绿的谐波、五洲新春、双环)以及电机/传感器(兆威、汇川)(截至 2026-06,未证实)。据报道 2025-10 三花获得约 $685M 的 Optimus 执行器零部件订单,2026 年起从墨西哥工厂交付——Tesla 与三花均未确认该订单,三花拒绝就"市场传闻"置评(单一来源,来自 36kr,未证实)。
- 战略后果:美国/欧盟的人形机器人项目面临与早期 EV 电池类似的零部件主权问题——去风险化行动(PRS 磨削回流、经 MP Materials 等实现非中国磁体加工)已经启动,但离对等还有数年。地理细节见[版图:中国](landscape-china.md)和[版图:美国](landscape-usa.md)。

## 关注事项

- VBT 触觉(GelSight 级)能否进入量产灵巧手,还是压阻阵列继续"够用就好"。
- 无稀土执行器电机能否达到扭矩密度对等(截至 2026,铁氧体方案约有 30% 的质量代价)。
- 2026 下半年 PRS 磨削产能对 Tesla/Figure 产量爬坡的匹配——被引用最多的物理瓶颈。
- 机载算力的分化:NVIDIA Thor 标准化 vs 自研芯片(Tesla AI5)vs 中国国产芯片。
- 电池:固态或高硅电池组能否在不触发质量螺旋的前提下把续航推过 5 h。

## 来源
- https://nvidianews.nvidia.com/news/nvidia-blackwell-powered-jetson-thor-now-available-accelerating-the-age-of-general-robotics — Jetson Thor 上市日期、规格(2,070 FP4 TFLOPS、128 GB、130 W)、$3,499 开发套件、采用者名单
- https://developer.nvidia.com/blog/introducing-nvidia-jetson-thor-the-ultimate-platform-for-physical-ai/ — Thor 架构细节(Neoverse-V3AE CPU、PVA、I/O)
- https://www.stocktitan.net/news/NVDA/nvidia-releases-new-physical-ai-models-as-global-partners-unveil-77essf0i9cjv.html — Jetson T4000 发布:1,200 FP4 TFLOPS、64 GB、$1,999(1k 件起)
- https://www.cnx-software.com/2025/08/19/3499-nvidia-jetson-agx-thor-developer-kit-2070-tops-jetson-t5000-som-for-robotics-and-edge-ai/ — T5000 模组细节与功耗范围
- https://www.figure.ai/news/introducing-figure-03 — Figure 03 灵巧手(3 g 指尖灵敏度、掌部相机)、2 kW 无线充电、执行器速度/扭矩宣称、BotQ 产能
- https://www.businesswire.com/news/home/20241031980322/en/GelSight-and-Meta-AI-Introduce-Digit-360-Tactile-Sensor — Digit 360 规格:18+ 种感知能力、约 1 mN 力灵敏度、全向形变
- https://www.unitree.com/mobile/Dex5-1/ — Unitree Dex5-1 灵巧手:20 自由度、可选 94 个触觉点、力/重复精度规格
- https://www.ubtrobot.com/en/humanoid/products/walker-s2 — Walker S2 3 分钟自主换电、双 48 V 电池组、52 自由度、算力配置
- https://eu.36kr.com/en/p/3780414717129481 — Optimus 零部件数量(约 28 个执行器、约 14 个滚柱丝杠)、$20k 成本目标、BOM 拆分、中国供应商图谱、三花 $685M 订单(单一来源)
- https://fortune.com/article/elon-musk-tesla-optimus-robots-china-rare-earths/ — 中国稀土出口管制扰乱 Optimus 生产
- https://www.adamasintel.com/tesla-rare-earth-free-motor/ — Tesla 无稀土电机计划的进展
- https://rareearthexchanges.com/news/teslas-rare-earth-exit-a-strategy-ahead-of-its-time-or-the-market/ — 截至 2026 年初无确认的无稀土部署;铁氧体约 30% 质量代价
- https://www.mckinsey.com/industries/industrials/our-insights/turning-humanoid-supply-chain-constraints-into-billion-dollar-wins — 中国零部件份额(轴承约 40%、电机约 35%、功率电子约 30%)、每台机器人 NdPr 用量
- https://advisor.morganstanley.com/john.howard/documents/field/j/jo/john-howard/The_Humanoid_100_-_Mapping_the_Humanoid_Robot_Value_Chain.pdf — Humanoid 100 价值链图谱;中国成本优势
- https://www.goldmansachs.com/insights/articles/the-global-market-for-robots-could-reach-38-billion-by-2035 — 40% 同比成本下降、$30k–150k 单台成本、2035 年 $38B 预测(报告 "Humanoid Robot: The AI Accelerant",2024-02-26;上调超 6 倍,从 $6B 起;出货量 4 倍至 140 万台)
- https://interestingengineering.com/ai-robotics/china-humanoid-robots-actuators — 中国关节架构的强项与短板;上肢谐波/下肢行星的收敛趋势
- https://botinfo.ai/articles/unitree-g1 — Unitree G1 2026 年各配置定价
- https://www.therobotreport.com/nvidia-jetson-thor-brings-2k-teraflops-of-ai-compute-to-robots/ — 对 Thor 规格与定位的独立确认
- https://www.yicaiglobal.com/news/six-axis-force-sensors-for-humanoid-robots-are-close-to-achieving-mass-production — 中国六轴力/力矩传感器量产进展
- https://www.intelmarketresearch.com/torque-sensor-for-humanoid-robot-market-2830 — 人形机器人力矩传感器市场预测(未证实的市场研究)
- https://www.robotwale.com/article/humanoid-robot-battery-runtime-reality-check — 标称与实际续航差距;热插拔运营模式
- https://developer.nvidia.com/blog/accelerate-ai-inference-for-edge-and-robotics-with-nvidia-jetson-t4000-and-nvidia-jetpack-7-1/ — Jetson T4000 官方规格:1,200 FP4 稀疏 TFLOPS、64 GB LPDDR5X、40–70 W 功耗区间
- https://www.figure.ai/news/f-03-battery-development — Figure 03 电池:2.3 kWh、峰值性能下宣称约 5 h 续航、2 kW 快充、主动散热 + 定制 BMS
- https://www.cnbc.com/2025/04/23/teslas-optimus-hit-by-chinas-rare-earth-restrictions-says-musk.html — Musk 在 2025-04-22 财报电话会上称:Optimus 生产受中国稀土出口管制影响;正申请出口许可
- https://www.teslarati.com/tesla-optimus-v3-hand-arm-details-revealed-new-patents/ — Optimus Gen 3/V3 灵巧手专利:22 自由度手、腱驱动、每臂 25 个前臂执行器
- https://electrek.co/2026/04/15/tesla-ai5-chip-taped-out-musk-ai6-dojo3/ — Tesla AI5 于 2026-04-15 流片;Samsung + TSMC 代工;量产目标 2027 年中后期;聚焦 Optimus/集群
- https://www.humanoidsdaily.com/news/tesla-optimus-production-rumors-fuel-supplier-stock-surge — 据报道的 $685M 三花订单未获 Tesla 或三花确认;三花拒绝就市场传闻置评
- https://www.kedglobal.com/robotics/newsView/ked202601200007 — Boston Dynamics 拟将 Atlas 定价低于约两名美国制造业工人两年工资(约 $320k);无公开 MSRP
- https://cnevpost.com/2025/07/17/ubtech-humanoid-robot-autonomous-battery-swap/ — 对 Walker S2 3 分钟自主换电、双 48 V 电池组、每组约 2 h 行走的独立确认
