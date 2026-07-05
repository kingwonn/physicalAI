---
title: 移远通信 × Physical AI:机会契合分析
slug: pitch-quectel
updated: 2026-07-05
confidence: verified
audience: Quectel executives
---
> 结论(可独立阅读):对移远通信(603236)而言,Physical AI 不是一道"要不要进入"的选择题——公司**已经在里面**。截至 2026-07,移远已推出面向机器人的专用算力模组(SG885G/48 TOPS、SH602HA-AP/10 TOPS BPU、CES 2026 旗舰 SP895BD-AP/77 TOPS)、与逐际动力(LimX)合作"Robrain"机器人大脑方案并在 MWC 上海 2025 现场跑在双足人形 TRON 1 上、四足通信模组已对宇树(Unitree)量产(据财经媒体,secondary),并在 2025 年定增中把"AI 算力模组及 AI 解决方案产业化"(含 AI 机器人解决方案)列为独立募投项目(¥4.11 亿,总募资 ≤¥23 亿,primary)。因此本文的真问题是**"如何把已经跑起来的机器人业务从试点级放大到产线级/战略级"**。移远的自然打法是**军火商逻辑**:不赌哪家整机胜出,卖每台机器人——不论人形、四足、AMR 还是服务机器人——都要的算力/连接/定位。可寻址市场当下仍小(见 §4:2026 全球人形整机硬件盘 ~$20 亿,但模组是**跨品类**的,叠加四足/AMR/服务机器人后模组可寻址盘估约 **$3–8 亿/年(2026,粗估,高不确定)**,并随整机放量以三位数增速扩张)。现在不是**放量**窗口,而是**设计导入(design-in)+ 客户绑定**窗口——同行(美格、广和通、Thundercomm、高通、NVIDIA)正在同一批整机客户处抢 socket,而移远的份额优势、量产成熟度与已落地的机器人案例是最强筹码。风险直白:盘子仍小、可靠性未过关、模组是价格战重灾区、且高通/NVIDIA 正越过模组商直供整机。

配套阅读(避免重复通用内容):通用 ODM/军火商框架见 [ODM 机会图谱](../wiki/odm-opportunity.md);板载算力硬件底座见 [硬件底座](../wiki/hardware.md);Jetson/NVIDIA 平台见 [NVIDIA 深度](../wiki/company-nvidia.md);中国供应链地理见 [中国格局](../wiki/landscape-china.md)。本文只落到 **Quectel 特定判断**。

范围与证据说明:面向 Quectel 高管决策。所有单源/未证实项在正文与 §来源显式标注 `(secondary)`/`(single-source)`/`(unverified)`;凡引公司年报/SSE 披露为 `(primary)`。TAM 严格区分**硬件营收盘**与**工资替代 TAM**(后者是投资叙事,非模组可寻址,见 [ODM §1](../wiki/odm-opportunity.md#1-market-size-honestly-bounded-as-of-2026-07))。

---

## 1. 一句话论点(thesis)

> **移远不赌哪家整机赢,卖每台机器人都要的三样东西——算力、连接、定位。这是"军火商"打法:整机品牌大概率洗牌(NDRC 已警告 >150 个雷同项目,见 [ODM §4](../wiki/odm-opportunity.md#4-timing-is-2026-27-the-entry-window)),但无论谁活下来,都要在机身里塞一块算力/连接/定位模组。移远赢在"卖铲子",而非赌"淘金者"。**

为什么这比整机组装更防御(defensible):

- **横切品类,不押单一形态**:算力+连接+定位是人形、四足、AMR、服务机器人**共同**的刚需。若 Rodney Brooks 式判断成立(赢家长轮子、非拟人手,见 [开放问题](../wiki/open-problems.md)),整机组装线是错资产,但**模组照卖**——形态之争对移远近乎中性。这正是 [ODM §5](../wiki/odm-opportunity.md#5-strategic-options-for-a-generic-odm-build--partner--invest--wait) 里"picks-and-shovels 在洗牌和形态之争中都能存活"的逻辑。
- **不与客户抢生意**:一旦自造整机(如立讯 3,000 台自研机、广达 Techman),就成了每个潜在整机客户的竞争对手,断了供货路。移远做零部件/参考方案/软件栈,可以同时供货 LimX、宇树、德壹、EEVE 而不冲突。
- **复用现成军火库**:移远的 5G/4G/LPWA、Wi-Fi/BT、GNSS、智能模组(SoM)、云平台、天线,是**已量产、已认证、已规模化**的产线,不是从零搭。军火商的护城河是"客户在设计冻结时刻的信任 + 量产成熟度",移远两样都有。
- **军火商 vs 整机的利润几何**:整机组装在 EMS 经济学下只值产品价值的 ~6–10%([ODM §1](../wiki/odm-opportunity.md#1-market-size-honestly-bounded-as-of-2026-07)),且要背整机可靠性/交付风险;算力模组是**差异化零部件楔子**,ASP 高、绑定深、随整机放量而放量,却不承担整机成败。

一句话:**移远该做机器人的"英特尔 Inside + 高德地图",不做机器人的"富士康"。**

---

## 2. 能力契合:现有能力 → Physical AI 价值链

对照 [ODM §2](../wiki/odm-opportunity.md#2-value-chain-opening-map-for-odmsems) 的"卖铲子 + 零部件楔子"路径,移远的能力映射:

| Physical AI 需求 | 移远现有能力 | 现成 / 要补 | 备注 |
|---|---|---|---|
| **板载算力(VLA/感知推理)** | 智能模组线 SG885G(QCS8550,48 TOPS)、SH602HA-AP(D-Robotics Sunrise5/X5M,10 TOPS BPU)、CES 2026 旗舰 SP895BD-AP(高通 Snapdragon Q-8750,3nm,77 TOPS,可跑 110 亿参数 LLM 端侧)(primary/secondary) | **基本现成** | 已覆盖 10→48→77 TOPS 梯队;白皮书画到 "100 TOPS 以上" 路线 |
| **蜂窝连接(遥测/OTA/云协同)** | 全系 2G–5G、5G RedCap(RG255C 已 NAL/CCC 认证)、LPWA/NB-IoT、Wi-Fi/BT(FCS950)、LoRa(KG200Z) | **现成、且是移远最强项** | 全球蜂窝模组 #1(~36–37% 份额,secondary);机器人"云边混合"架构的天然连接层 |
| **精确定位(导航/建图)** | GNSS 定位模组线;与 Point One Navigation 合作推厘米级定位(secondary) | **现成(高精度需深化)** | AMR/割草机器人刚需;是"算力+连接"之外的第三条腿 |
| **边缘 AI / 端侧大模型** | SG885G 端侧跑 DeepSeek-R1 蒸馏版 >40 tok/s;智能模组集成火山引擎豆包多模态 VLM;2025-07 发布 "AI 大模型技术白皮书"(边+云、多模态)(secondary) | **现成** | 与 [硬件底座·板载算力](../wiki/hardware.md#onboard-compute) 的"split-brain"范式一致:实时控制 MCU + AI 模组做感知/策略 |
| **多传感器融合/感知栈** | SH602HA-AP 支持 VSLAM、双目深度、语音识别、Transformer/BEV/Occupancy 模型执行、LiDAR/结构光/ToF 融合(primary) | **现成(参考方案级)** | 已把"感知硬件抽象"打包进模组 |
| **整机大脑参考方案** | "Robrain"(SG885G + 云边混合 LLM + 麦克风阵列),LimX TRON 1 现场落地(primary) | **现成(方案级,需产品化/规模化)** | 从"模组"上升到"子系统",绑定更深 |
| **量产制造** | 常州"全球智能制造中心"(~16 万㎡ 建面,全自动线,覆盖 4G/5G/智能模组/车规/GNSS/天线)+ 自有工厂 + 代工混合(secondary) | **现成** | 军火商要的是产能+良率+认证,移远已有 |
| **热管理 / 供电 / 电池 BMS** | 未见移远机器人专用供电/热管理产品 | **要补 / 或不做** | 属整机侧,军火商可不碰(见 [ODM §2](../wiki/odm-opportunity.md#2-value-chain-opening-map-for-odmsems) 低难度行) |
| **执行器/减速器/灵巧手** | 无(非移远赛道) | **不做** | 这是立讯/绿的谐波/贝斯特的战场,移远刻意不进——见 [硬件·执行器](../wiki/hardware.md#actuators) |

**净判断**:移远在"算力+连接+定位"三件套上**几乎全部现成**;真正要补的不是硬件,而是(a)高算力路线的持续投入(100+ TOPS,已在定增募投里,见 §3)、(b)机器人专用软件栈/中间件的深度(VLA 适配、实时性、ROS2 集成)、(c)整机客户的**具名设计导入关系**(见 §8 待补)。移远刻意**不进**执行器/结构件——这符合军火商纪律,避免陷入 15–20%/年通缩的红海([ODM §2](../wiki/odm-opportunity.md#2-value-chain-opening-map-for-odmsems) "毒药"行)。

---

## 3. 起点盘点:移远在机器人上到底做了什么

**诚实定性:这不是"空白/仅早期",而是已有多季度、多产品、多合作的活跃业务——本项目是"扩张",不是"进入"。** 但需注意:公开财报**未单列机器人营收**,无法证实其在总营收中的占比,所以"活跃"指产品/PR/合作的活跃,不等于已成规模营收。

事实清单(按证据强度):

| 动作 | 时间 | 证据质量 | 说明 |
|---|---|---|---|
| 定增募投列"AI 算力模组及 AI 解决方案产业化"项目,含 **AI 机器人解决方案** | 披露 2025-03-31 | **primary**(SSE/募集说明书) | 总募资 ≤¥23 亿;该项目 ¥4.11 亿、建设期 18 个月;募集说明书注册稿把范围写明为**人形/工业/服务机器人 + 端侧高算力智能模块**——这是移远机器人战略最硬的官方背书 |
| SG885G 智能模组(QCS8550,48 TOPS)明确面向"机器人/AR-VR/边缘计算" | ~2023–24 | primary | 后续机器人大脑方案的底座 |
| **Robrain 机器人大脑**方案 × 逐际动力(LimX),跑在双足人形 TRON 1 | MWC 上海 2025-06-18 | primary | 从"模组"升级到"子系统方案";定位展厅导览机器人 |
| SH602HA-AP 专用"机器人算力模组"(D-Robotics Sunrise5/X5M,10 TOPS BPU,Ubuntu 22.04) | CES 2026(~Jan 7–15) | primary | 点名人形/轮臂/四足/陪伴服务机器人;并绑定古月居 OriginMan 机器人(secondary) |
| CES 2026 旗舰 SP895BD-AP(高通 Snapdragon Q-8750,3nm,**77 TOPS**,端侧 110 亿参数 LLM) | 2026-01(CES) | **primary**(Quectel 官网产品页)+ secondary(新浪/IT之家) | 算力梯队登顶;虽宣传侧未点名机器人,但属同一智能模组矩阵。注:部分英文媒体(CNX Software)记为 80 TOPS,系不同口径/四舍五入,以 Quectel 官方 77 TOPS 为准 |
| 四足机器人通信模组对**宇树(Unitree)**量产 | 报道 2025-02 | **secondary**(东方财富) | 基于移远 5G 模组;移远IR只说"行业头部公司",未在披露中具名 |
| 具名"星动纪元/RobotEra"(星动)为量产适配客户 | 报道 2026-02 | **secondary**(东方财富"被低估的人形概念股") | 财经媒体口径,非公司披露 |
| AI 具身理疗机器人 × **德壹(Deyi)**,端侧 LLM(SG885G-WF/48 TOPS)+ 8-DOF 3D 视觉导航,广州美博会 | 2025-03 | **secondary**(多家转载 + Quectel 官网 primary) | "全球首款搭载端侧大模型的 AI 具身理疗机器人"系**公司营销口径**(superlative,自证);发布事实本身多源可核 |
| GNSS 高精度定位 × Point One Navigation(面向 AMR) | — | secondary | 厘米级定位合作 |
| EEVE "Willow" 割草 AMR 采用移远 LTE/GNSS 模组 | — | secondary | 具体 AMR 客户 design-win |
| IR 反复表态"持续关注人形机器人创新技术,按客户需求做研发";智能模组/控制器/视觉"已应用于双足/四足具身智能行业头部公司产品" | 2024–2025 多次 | secondary | **从不点名**具体客户(未提宇树/星动/智元) |

**空白 / 尚未证实**:
- 未见移远自造/自售整机(全部是零部件/参考方案/软件栈供第三方)——**符合军火商定位,是特性不是缺陷**。
- 未见机器人营收的公开占比拆分(有股吧标题喊"AI 机器人业务大爆发",`unverified`,当评论看)。H1 2025 模组 ASP 升至 ~¥180(+25% YoY),财经媒体部分归因于高价值 AI/机器人模组的结构性上移(secondary,非公司确认)。
- 未见移远出现在 WRC 2025(北京,2025-08)的具体展台报道(`unverified`,可能是低可见度或未被索引)。
- 无独立"机器人事业部"或机器人专属 P&L;"艾络迅"等子品牌是智能模组之上的平台/品牌层,非机器人业务单元(secondary)。

---

## 4. 市场与可切份额(诚实量级)

**先分清两个盘**(严格沿用 [ODM §1](../wiki/odm-opportunity.md#1-market-size-honestly-bounded-as-of-2026-07) 的纪律):
- **工资替代 TAM**(黄仁勋 $40–50T、Figure "$42T/年")= 投资叙事,**不是移远可寻址**。
- **硬件营收盘** = 单位数 × 硬件 ASP,才是模组能吃的。移远营收随后者、绝不随前者。

**整机硬件盘(锚点,来自 [ODM §1](../wiki/odm-opportunity.md#1-market-size-honestly-bounded-as-of-2026-07)):** 2026 全球 ~5 万台人形 × ~$40K 混合 ASP ≈ **~$20 亿全球人形整机硬件营收**(与 Morgan Stanley 对中国 2026 人形市场 ~$20 亿的量级一致)。

**但模组是跨品类的——盘子比"人形整机"大。** IDC(2026-01-15)对**中国 2026** 的拆分:

| 品类(中国 2026) | 用户支出规模 | YoY | 来源 |
|---|---|---|---|
| 人形机器人 | ~$13 亿 | +100%+ | IDC(secondary) |
| 四足机器人 | >$7 亿 | +100% | IDC(secondary) |
| 商用服务机器人 | ~$4 亿 | +15% | IDC(secondary) |
| **中国具身智能整体(用户支出)** | **>$110 亿** | ~+120% | IDC(secondary) |

再叠加 AMR/割草/巡检等移动机器人(全球盘更大),移远的"算力+连接+定位"可服务的**整机品类基数远大于人形整机的 ~$20 亿**。

### 模组可寻址盘(SAM)粗估——方法与不确定性

**方法(illustrative,本文自算,高不确定):**
- **算力模组**:一台需 AI 算力的机器人,算力模组价值粗估 **$300–1,500/台**(参考:SoM 在 $20K 机器人 BOM 里算力约占几个百分点,见 [硬件·BOM](../wiki/hardware.md#bom-cost-trends);高端多模组人形如"通天晓"用双 SNM970 更高)。取 2026 全球有 AI 算力需求的机器人(人形 ~5 万 + 四足/AMR/服务机器人若干十万台,量级不确定)——**仅人形一项**:5 万 × $300–1,500 ≈ **$1,500 万–7,500 万/年**;叠加四足/AMR/服务机器人(基数大但单价低),算力模组全球盘量级 **~$1–4 亿/年(2026)**。
- **连接 + 定位模组**:单价低($5–50/台蜂窝、$5–30/台 GNSS),但**渗透率可达近 100%**(几乎每台联网/需定位的机器人都要),且移远是全球 #1,可切份额高。这一层量级 **~$2–4 亿/年(2026)**,并随整机放量线性增长。
- **合计模组可寻址盘(移远视角,2026):粗估 ~$3–8 亿/年区间**,随整机三位数增速在 2027–28 快速扩张。

**⚠️ 不确定性标注(必读):**
1. 上述为**本文自算的量级估计,非独立市场研究**,单价/渗透率/基数均为区间假设,可差 2–3 倍。
2. 有中文财经媒体(东方财富,2026-02)引"机器人通信模组全球市场 2025 约 **¥50 亿**、CAGR ~60%"(**single-source,当叙事看,不可作确定事实**)——若属实,与本文粗估量级同阶(¥50 亿≈$7 亿),可作交叉参照但不可采信为准。
3. **可切份额 ≠ 可寻址盘**:移远虽是蜂窝 #1,但算力模组是**新战场**,高通/NVIDIA/Thundercomm/美格/广和通同场竞争(见 §5),份额远未锁定。
4. **别把 $110 亿"具身智能用户支出"当模组盘**——那是整机+服务+软件的总支出,模组只吃其中零部件的一小片。

**净判断:模组盘现在小(单位数亿美元),但(a)跨品类基数比人形整机大、(b)增速三位数、(c)移远在连接/定位层份额高、算力层刚起步。这是"小而快、且移远有先发案例"的盘——值得产线级投入,但不足以支撑"战略级 all-in"叙事,除非 2027–28 整机放量兑现。**

---

## 5. 友商记分牌(FOMO / 威胁)

按机器人承诺度排序;所有条目带日期与证据质量。竞争分三层(见 [ODM §2](../wiki/odm-opportunity.md#2-value-chain-opening-map-for-odmsems) 的"谁把高通硅片封成 SoM"结构性发现):

| # | 玩家 | 层级 | 机器人动作(日期) | 证据质量 | 对移远含义 |
|---|---|---|---|---|---|
| 1 | **美格智能(002881)** | 中国模组同行 | SNM970(QCS8550,48 TOPS)为**双模组 ~100 TOPS 人形"通天晓/Ultra Magnus"**(美格 × 阿加犀 × 高通)算力核心,CES 2025(2025-01-07)发布;SG880 系列覆盖 0.2→48 TOPS,明确适配人形;2025 年内多次因端侧 AI/机器人叙事涨停(具体"7 连板"streak `unverified`) | secondary | **最直接对标**:同用 QCS8550,同打人形;美格"高弹性高风险"叙事抢眼球。威胁:抢同一批高通生态整机客户 |
| 2 | **广和通(300638)** | 中国模组同行 | **Fibot 具身智能开发平台**(机械臂+算力+全向底盘,主控 SC171/QCM6490/12 TOPS,复现斯坦福 Mobile ALOHA,2024-03-29 发布);**2026-04-20 *联合*领投珞博智能(Robopoet)Pre-A**——但珞博是 **AI 陪伴硬件/潮玩(Fuzozo 芙崽)** 公司,非具身/人形机器人,广和通角色是"通信底座+全球资费+战略投资" | primary(Fibot)/secondary(投资) | 威胁:广和通用"平台+投资"绑定模式(**注:珞博案是 AI 陪伴玩具,不是具身机器人;此条对移远的机器人威胁被此前高估**);移远若只卖模组,绑定深度可能落后 |
| 3 | **Thundercomm(创通/中科创达系)** | 高通生态集成商 | **TurboX IRB10** 开发板(高通 Dragonwing IQ10,**峰值 700 TOPS**,支持 20 路并发摄像头),Embedded World 2026 发布,点名工业 AMR/全尺寸人形/商用服务机器人 | primary | **高端算力威胁**:700 TOPS 远超移远当前 77 TOPS 梯队;非电信模组商,是纯高通生态集成商——直接抢人形 SoM socket |
| 4 | **高通(Qualcomm)** | 芯片/平台原厂 | CES 2026 推**全套机器人技术**(Dragonwing IQ10,从家用到全尺寸人形);Figure 与高通合作"定义下一代计算架构" | primary | **结构性威胁**:原厂**越过模组商直供整机**。移远/美格/广和通都建在高通硅片上,议价与被"去中间化"风险并存 |
| 5 | **NVIDIA** | 芯片/平台原厂 | Jetson Thor(Blackwell,2,070 FP4 TFLOPS,128GB)2025-08 GA,人形早期采用者含 Agility/Boston Dynamics/Figure 等;Galbot G1 Premium 直集成 Jetson AGX Thor | primary | 高端人形大脑事实标准(见 [NVIDIA 深度](../wiki/company-nvidia.md#act-layer-jetson-and-the-halos-safety-platform))。移远走高通生态,与 Jetson 错位竞争,但高端人形多选 Thor |
| 6 | **Lantronix / Thundercomm** | 高通生态集成商 | 把 QCS8550 封成 SoM(Open-Q 8550CS,48 INT8 TOPS 等) | primary | 与移远/美格在"谁封 QCS8550 成 SoM"上正面竞争 |

**结构性读数(关键)**:机器人"板载算力/连接模组"市场**不是单层**——(1)中国电信模组商(移远/广和通/美格/日海),(2)高通生态专用集成商(Thundercomm/Lantronix),(3)芯片原厂直供(高通/NVIDIA)。移远的相对优势:**蜂窝连接 #1 + 定位 + 量产成熟 + 已有具名机器人案例(LimX/宇树)**;相对短板:**纯算力峰值落后**(77 TOPS vs Thundercomm 700 TOPS、Jetson Thor 2,070 TFLOPS)、**软件/生态深度**、以及**被原厂去中间化**的长期风险。

**FOMO 温度**:同行动作密集(美格 CES 2025 人形、广和通 2026-04 股权投资[注:标的珞博为 AI 陪伴玩具而非人形]、Thundercomm 2026 EW 700 TOPS、高通 CES 2026 全套)——**都在过去 18 个月**。这是典型的 design-win 竞速,每一步都让下一步更便宜(见 [ODM §6](../wiki/odm-opportunity.md#6-what-would-make-this-urgent-fomo-evidence-honestly-framed))。移远已在场,但**不能只靠"卖模组"守——需向"方案/绑定/投资"上移**,否则被广和通式深绑或原厂直供夹击。

---

## 6. 战略选项矩阵(build / partner / design-win / 投资)

针对移远,每条给量级与先例,并分**试点级 / 产线级 / 战略级**。判断:移远已在"试点级"(Robrain、德壹),应向"产线级"重心倾斜,选择性做 1–2 个"战略级"下注。

| 选项 | 分级 | 先例/参照 | 量级 | 关键风险 | 适合移远当…… |
|---|---|---|---|---|---|
| **深化算力模组梯队(100+ TOPS)** | 产线级 | 定增 ¥4.11 亿 AI 模组募投(primary);美格/Thundercomm 峰值更高 | ¥4–10 亿(已在募投内) | 峰值算力军备竞赛烧钱;高通/NVIDIA 原厂压顶 | ……要守住高通生态 SoM 卡位、补齐 vs Thundercomm 700 TOPS 的差距(**推荐:已在做,加速**) |
| **把 Robrain 类"机器人大脑方案"产品化+多客户复制** | 产线级 | Robrain × LimX(primary);广和通 Fibot 平台 | 低 → 中 | 方案交付/售后重资源;整机客户可能自研大脑 | ……要从"卖模组"上移到"卖子系统",加深绑定(**推荐**) |
| **具名整机客户 design-win 扩张(宇树/星动/智元/UBTech…)** | 产线级 → 战略级 | 宇树四足量产(secondary)、星动(secondary) | 中(随客户放量) | 整机客户洗牌(NDRC 警告 >150 雷同项目);ASP 通缩 | ……选**资本充足、订单可信**的整机客户绑定,别赌小厂(见 [ODM §4](../wiki/odm-opportunity.md#4-timing-is-2026-27-the-entry-window)) |
| **连接+定位"全渗透"策略** | 产线级 | Point One(定位)、EEVE(AMR)已落地 | 中(高渗透、低单价) | 单价低、价格战 | ……用 #1 蜂窝份额把"每台机器人都装移远连接/定位"做成默认(**移远最防御的一层,推荐**) |
| **战略投资/入股具身 AI 初创** | 战略级 | 广和通*联合*领投珞博(2026-04,secondary;注:珞博是 AI 陪伴玩具,非人形/具身);NVIDIA 投 Figure/Skild([投资](../wiki/investment.md)) | 中(财务) | 泡沫估值 mark-to-market;买信息不买产能 | ……要买 board-level 信息与优先 design-in,并跟上广和通的绑定深度(**选择性做 1–2 个**) |
| **合资/联合开发机器人参考整机** | 战略级 | 广和通 Fibot 更偏此;LimX 合作可深化 | 中–高 | **渠道冲突**——一旦近似自造整机,威胁供货中立性 | ……**谨慎**:军火商纪律下宜停在"参考方案"、不越线到"自售整机" |
| **自造/自售整机** | ——(不建议) | 立讯 3,000 台自研机、广达 Techman | 高 | 与所有整机客户为敌;护城河是移远没有的整机软件 | ……**不适合移远**——会断掉军火商供货路,放弃 #1 模组中立性 |
| **等待/观望** | ——(不建议) | Wistron/英业达(de facto) | 无 | 已在场却退场=把 LimX/宇树先发拱手让人;design-win 具汽车级黏性,晚进只剩残羹 | ……**不适合**:移远已有先发,观望是浪费领先 |

**组合建议(portfolio beats single bet,呼应 [ODM §5](../wiki/odm-opportunity.md#5-strategic-options-for-a-generic-odm-build--partner--invest--wait)):**
"**加速算力梯队(产线级)+ 机器人大脑方案产品化(产线级)+ 连接/定位全渗透(产线级)+ 1–2 个具身 AI 战略投资(战略级)**",总敞口可控(大部分已在 ¥4.11 亿募投内 + 数亿投资额度),复制广和通"平台+投资"绑定深度,同时守住军火商中立性——**不碰整机自造、不碰执行器红海**。

---

## 7. 为什么是现在(FOMO,诚实版)

### 看多(bull:窗口正开)

- **设计导入窗口**:机器人 BOM 仍在流动(见 [硬件·板载算力](../wiki/hardware.md#onboard-compute) 的 split-brain 范式尚未定型),此刻共同定义 DFM/接口的供应商,会像早期 iPhone/EV 供应商一样成为**黏性在位者**。移远已在 LimX/宇树处卡位。
- **同行动作密集**(§5):美格 CES 2025 人形、广和通 2026-04 股权(标的珞博为 AI 陪伴玩具,非人形)、Thundercomm 2026 EW 700 TOPS、高通 CES 2026 全套——**过去 18 个月**的竞速,每步都在抢同一批整机客户的 socket。
- **需求信号(制度性,非消费)**:
  - **国网 ~¥68 亿具身机器人采购**(2026,分阶段:500 台人形/3,000 台双臂/5,000 台四足,见 [ODM §4](../wiki/odm-opportunity.md#4-timing-is-2026-27-the-entry-window);季度phasing 为 single-source)——每台都要连接/算力/定位。
  - **工信部/国资委"真实场景训练"专项行动**(2026-06-09 primary MIIT):年底前 100+ 高价值场景、"万台级"部署能力——制度性需求承诺机制。
  - **IPO/SPAC 资本到账**:宇树 ~$618M STAR IPO(2026-07-02 注册获批)、Agility ~$620M SPAC——新融资的整机厂 2026–27 必须把现金转成产能,而**产能决策正是 make-vs-buy 定案时刻**。
- **移远自身资本动作**:2025 定增 ≤¥23 亿(含 ¥4.11 亿 AI 机器人模组募投,primary)——**弹药已备**,不是"要不要投钱",而是"已投,如何打"。

### 看空 / 风险(bear:为什么可能太早)

- **盘子仍小**:即便完美的 2026(全球 ~5 万台人形),模组盘仍是单位数亿美元(§4),对移远 ¥243 亿(2025)总营收是**零头**——机器人是**期权/卡位**,不是近期 P&L 支柱。别把机器人当增长主引擎叙事卖给投资者。
- **可靠性未过关**:旗舰西方试点(Figure 02 @ BMW)~11 个月后退役、可见磨损、未扩队(见 [ODM §4](../wiki/odm-opportunity.md#4-timing-is-2026-27-the-entry-window));MTBF 行业几乎无公开数据([开放问题](../wiki/open-problems.md))。为未兑现的需求建产能=搁浅 capex。
- **价格战/通缩**:模组是移远利润承压区——2025 Q3 毛利率 17.71%(略降),中国零部件年通缩 15–20%。算力模组虽 ASP 高,但一旦标准化,同样滑向价格战(美格 SNM970、Thundercomm、Lantronix 同封 QCS8550)。
- **原厂去中间化**:高通(CES 2026 全套机器人技术)、NVIDIA(Jetson Thor)**越过模组商直供整机**;Figure 直接与高通合作"定义计算架构"。移远的"封 SoM"角色可能被原厂+整机自研双向挤压。
- **峰值算力落后**:移远 77 TOPS vs Thundercomm 700 TOPS、Jetson Thor 2,070 TFLOPS——高端全尺寸人形大脑这一档,移远当前不在第一梯队。
- **具名不足的风险**:公司披露从不点名客户,财经媒体的"宇树/星动"口径均为 secondary——真实绑定深度**外部无法证实**(见 §8)。
- **时间线滑坡是常态**:每一个 Optimus 里程碑自 2021 起均延期;把所有 2026 放量日期当**aspirational**([ODM §4](../wiki/odm-opportunity.md#4-timing-is-2026-27-the-entry-window))。

### 净读数

**2026–27 不是"放量"窗口,是"锚定客户 + 设计导入"窗口。** 移远的独特处境是**已经在场**(LimX/宇树/德壹/EEVE + ¥4.11 亿募投),所以对移远,"为什么是现在"的答案不是"是否进入",而是:**趁 design-win 竞速正烈、整机厂产能决策正在定案、而移远仍握先发案例与 #1 连接份额时,把已经跑起来的机器人业务从试点级推到产线级,并用 1–2 个战略投资锁定深绑——成本相对移远资产负债表低,而被锁在 2028–30 真实放量之外的代价高。** 若 2026 预测像历次一样滑坡,"紧迫"平滑转为"尚早",移远的低成本卡位也不受伤——这正是军火商姿态的非对称优势。

---

## 8. 待补信息(需 Quectel 内部才能确认)

外部资料无法证实的关键未知,列清以便高管/IR 内部核对:

1. **现有机器人客户到底是谁、绑定多深?** 财经媒体点名宇树/星动/智元均为 secondary;公司披露只说"行业头部公司"。**具名客户名单、每客户量产状态、是独家还是多供?**
2. **机器人业务的真实营收与占比?** 无公开拆分。**机器人相关模组/方案 2025 营收多少、占总营收(¥243 亿)几何、毛利率相对基础模组如何?**(股吧"大爆发"为 unverified)
3. **算力模组路线图**:白皮书画到 "100+ TOPS",CES 2026 已到 77 TOPS。**下一代峰值目标、是否直面 Thundercomm 700 TOPS / Jetson Thor 档位?是否押注高通 Dragonwing IQ10?自研 vs 高通/D-Robotics 绑定的比例?**
4. **¥4.11 亿 AI 模组募投里,机器人具体占多少?** 该项目还含 AI 玩具/眼镜/工业/AI-BOX。**机器人子项预算、里程碑、产能目标?**
5. **Robrain / 机器人大脑方案的商业化状态**:LimX 之外**还落地了几家?是量产还是仍 demo?营收贡献?**
6. **是否有战略投资/合资计划?** 对标广和通*联合*领投珞博(2026-04;注:珞博为 AI 陪伴玩具而非人形/具身,广和通此单更偏"连接+资费+财务",非机器人整机绑定)。**移远有无机器人/具身 AI 股权投资额度与标的清单?**
7. **德壹"全球首款 AI 理疗机器人"**(single-source):**是否真实量产、移远供了什么、订单规模?**
8. **软件/生态深度**:**是否有机器人专用中间件、ROS2/VLA 适配团队规模、与整机大脑软件栈的分工?**(军火商能不能只卖硬件、还是被迫做软件?)
9. **被原厂去中间化的对冲**:**若高通/NVIDIA 直供整机,移远的差异化护城河(连接/定位/量产/本地服务)能守多久?有无 exclusive 生态协议?**
10. **产能与制造**:**常州中心是否已为机器人模组预留专线?产能弹性?车规/功能安全(对标 NVIDIA Halos)认证进度?**

---

## 来源

- 移远通信 2024 年年度报告(via 新浪财经/东方财富/证券之星摘官方 cninfo/SSE 披露)—— 营收 ¥185.94 亿(+34.14%)、归母净利 ¥5.88 亿(+548%)、研发 ¥16.69 亿(8.97%)。`primary`
- http://dataclouds.cninfo.com.cn/shgonggao/hsomarket/2026/20260423/1bf93ab98b02412e8d42990bc28da4a6.PDF —— 移远 2025 年年度报告摘要:营收 ¥243.26 亿(+30.83%)、归母净利 ¥8.37 亿(+42.3%)、研发 ¥19.51 亿。`primary`
- https://www.stcn.com/article/detail/1629003.html —— 移远拟定增募资**≤¥23 亿**:车载及 5G 模组扩产 ¥9.57 亿、**AI 算力模组及 AI 解决方案产业化 ¥4.11 亿(含 AI 机器人解决方案)**;披露 2025-03-31。`primary`
- https://stock.stockstar.com/notice/SN2025110500000211.shtml —— 2025 定增募集说明书(注册稿):AI 模组项目建设期 18 个月,范围含**人形/工业/服务机器人 + 端侧高算力智能模块**。`primary`
- https://static.sse.com.cn/stock/disclosure/announcement/c/202507/603236_20250728_QRJ3.pdf —— SSE 审核问询函回复(2025-07-28),定增申请文件(二进制 PDF,未逐字解析;仅作募投项目佐证)。`primary`
- https://www.quectel.com.cn/news-and-pr/smart-module-sp895bd-ap —— **SP895BD-AP** 官方产品发布页:高通跃龙 Q-8750(**3nm**),**77 TOPS** NPU,INT4/INT8/INT16/FP16,端侧可跑 **110 亿参数 LLM**。`primary`(TOPS 以此为准)
- https://finance.sina.com.cn/stock/relnews/cn/2026-01-13/doc-inhhcnuc5016711.shtml / https://www.ithome.com/0/912/495.htm —— CES 2026 旗舰智能模组 **SP895BD-AP** 77 TOPS 报道;引中信建投端侧 AI 市场 ¥3,219 亿(2025)→¥1.22 万亿(2029),CAGR 40%。`secondary`(注:CNX Software 记为 80 TOPS,取 Quectel 官方 77 TOPS)
- Quectel 官网/新闻(quectel.com.cn):SG885G(QCS8550,48 TOPS,面向机器人)、SH602HA-AP(D-Robotics Sunrise5/X5M,10 TOPS BPU)、智能模组矩阵、常州全球智能制造中心。`primary`
- MWC 上海 2025(2025-06-18):移远 × 逐际动力(LimX)联合发布 **Robrain** 机器人大脑,跑在双足人形 **TRON 1**。`primary`
- https://caifuhao.eastmoney.com/news/20250212181951581030520 —— 移远与**宇树(Unitree)**机器人业务合作:四足通信模组已量产。`secondary`
- (东方财富/caifuhao,2026-02)"移远:被低估的人形机器人概念股"—— 具名**宇树、星动纪元/RobotEra**为量产适配客户;引"机器人通信模组全球市场 2025 约 ¥50 亿、CAGR ~60%"。`single-source`(市场规模数据当叙事,不采信为准)
- https://finance.sina.com.cn/stock/relnews/cn/2025-03-09/doc-inenzyar4675839.shtml —— 移远 IR:智能模组已在**双足/四足具身智能机器人**等产品上应用(未点名客户)。`secondary`
- https://stock.stockstar.com/RB2025030700036855.shtml —— 移远 IR:智能模组已在具身智能机器人**行业头部公司**产品上应用。`secondary`
- https://news.qq.com/rain/a/20240809A08FOB00 —— 移远 IR:持续关注人形机器人创新技术,按客户需求做研发。`secondary`
- https://blog.csdn.net/meigsmart/article/details/145025816 —— **美格智能** SNM970 助力人形机器人"通天晓/Ultra Magnus",CES 2025(2025-01-07),双模组 ~100 TOPS。`secondary`
- https://www.stcn.com/article/detail/1484136.html —— 美格高算力 AI 模组助力**首款基于高通计算平台的人形机器人**面世。`secondary`
- https://www.meigsmart.com/articledetail/378.html —— 美格 SNM970(QCS8550,48 TOPS)产品发布。`primary`
- https://www.fibocom.com/products/info_itemid_8500.html —— **广和通 Fibot** 具身智能开发平台(机械臂+算力+全向底盘,主控 SC171/QCM6490/12 TOPS,复现斯坦福 Mobile ALOHA,2024-03-29)。`primary`
- https://www.electronicsweekly.com/news/products/quectel-sh602ha-ap-computing-module-targets-robotic-devices-2026-01/ —— **SH602HA-AP** 官方发布(基于新闻稿):**点名 humanoid / wheel-arm / quadruped / service-companion 机器人**,D-Robotics Sunrise 5(X5M),10 TOPS BPU,**Ubuntu 22.04**,支持 VSLAM/双目深度/BEV/Occupancy/LiDAR·结构光·ToF 融合。`primary`(证实 §3 的机器人品类具名)
- https://www.quectel.com.cn/news-and-pr/ai-embodied-physiotherapy-robot —— 移远 × **德壹(Deyi)**"全球首款搭载端侧大模型的 AI 具身理疗机器人"(SG885G-WF/48 TOPS,8-DOF 3D 视觉,广州美博会 2025-03);多家转载。`secondary`(+ Quectel 官网 primary;"全球首款"为公司营销口径)
- https://www.fibocom.com/newscenter/info_itemid_10748.html —— **广和通*联合*领投珞博智能(Robopoet)Pre-A**(2026-04-20);**珞博是 AI 陪伴硬件/养成系潮玩公司(Fuzozo 芙崽),非人形/具身机器人**;广和通角色="蜂窝模组+全球 SIM 资费+战略投资"。`primary`(修正:原叙述"延伸到具身 AI 股权"高估,实为 AI 陪伴玩具连接绑定)
- https://www.thundercomm.com/turbox-irb10-launches-at-embedded-world-2026 —— **Thundercomm TurboX IRB10**(高通 Dragonwing IQ10,峰值 700 TOPS,20 路摄像头),Embedded World 2026,点名工业 AMR/全尺寸人形/服务机器人。`primary`
- https://www.qualcomm.com/news/releases/2026/01 —— **高通** CES 2026 推全套机器人技术(家用→全尺寸人形);Figure 合作"定义下一代计算架构"。`primary`
- https://www.idc.com/resource-center/blog/... (2026-01-15)—— IDC 中国 2026 市场:人形 ~$13 亿(+100%+)、四足 >$7 亿(+100%)、商用服务 ~$4 亿(+15%)、**具身智能整体用户支出 >$110 亿(~+120%)**。`secondary`
- https://finance.sina.com.cn/stock/relnews/cn/2025-07-29/... —— 中国/全球蜂窝通信模组市场规模(2024 全球 ¥436 亿→2025E ¥486 亿;移远 2024 全球份额 37%)。`secondary`
- 内部交叉页(本仓库): [ODM 机会图谱](../wiki/odm-opportunity.md)(军火商框架、市场量级、友商记分牌、时机)、[硬件底座](../wiki/hardware.md)(板载算力/BOM/供应链)、[NVIDIA 深度](../wiki/company-nvidia.md)(Jetson/三计算机/竞争位)、[投资](../wiki/investment.md)、[开放问题](../wiki/open-problems.md)。`verified`(仓库内已核页)

> 单源/未证实汇总(高管审阅重点):机器人营收占比(无披露)、宇树/星动具名(secondary)、德壹"全球首款"(公司营销口径,发布事实多源可核)、"机器人通信/边缘算力模组 ¥50 亿·移远份额~35%"(single-source 研究口径,当叙事看)、模组 SAM 粗估($3–8 亿/年,本文自算)、WRC 2025 缺席(unverified)、ASP 上移归因机器人(secondary)、美格"7 连板"具体 streak(unverified)。
>
> 本轮对抗核查修正(2026-07-05):(1)广和通"领投珞博"→**联合领投**,且珞博为 **AI 陪伴玩具(Fuzozo)非人形/具身**,原"延伸到具身 AI 股权"表述已降级并加注;(2)SP895BD-AP TOPS 证据升级为 **primary**(Quectel 官网 77 TOPS),并标注 CNX Software 的 80 TOPS 异口径;(3)德壹从 single-source 升为 **多源 secondary + Quectel primary**;(4)美格"7 连板"具体 streak 标 unverified;(5)SH602HA-AP 机器人品类具名、Ubuntu 22.04、VSLAM/BEV/Occupancy 均经 primary 新闻稿证实。核心事实(SG885G/48 TOPS、SH602HA-AP/10 TOPS BPU、SP895BD-AP/77 TOPS、Robrain×LimX TRON 1、宇树四足量产、定增 ≤¥23 亿含 ¥4.11 亿 AI 机器人募投·注册稿人形/工业/服务机器人范围、IDC 2026 中国拆分、Thundercomm 700 TOPS、高通 CES 2026 全套+Figure、Jetson Thor 2,070 FP4 TFLOPS、移远蜂窝 IoT 模组 #1)**全部经 primary/secondary 核实站得住**。
