---
title: 人形机器人产业全景
slug: humanoid-robots
updated: 2026-07-04
confidence: verified
lang: zh
source: ../wiki/humanoid-robots.md
---
> 截至 2026 年年中,人形机器人行业已从演示阶段跨入早期量产:各方预测趋于一致,2026 年全球出货量将达 ≥50,000 台(Morgan Stanley 仅针对中国的预测在年内从 1.4 万台上调至 5 万台),中国厂商在出货量上领先(AgiBot 于 2026-03 突破累计第 10,000 台;Unitree 目标出货最高 20,000 台),Figure 03 和 Apptronik Apollo 已在 BMW 和 Mercedes-Benz 承担真实班次工作,Agility Robotics 正通过 $2.5B 的 SPAC 上市并手握 $300M 的 Digit v5 合同订单,Hyundai 计划自 2028 年起在美国工厂部署 25,000 台以上 Boston Dynamics Atlas,Tesla 正将 Fremont 的 Model S/X 产线改造用于生产 Optimus V3,1X 则开放了 $20K 的 NEO 消费者预订。当前价格区间从约 $4,300(Unitree R1 版本)到 $100K 以上(西方工业平台)不等;商用级物料成本(BOM)在中国供应链下估计约 $46K/台,脱离中国供应链则约 $130K。

## 市场速览(截至 2026-07)

- **出货量拐点**:2025 年全球人形机器人出货量按不同机构口径为 **约 13.3K(Omdia)至约 18K(IDC)**(参见[技术现状](state-of-the-art.md)中的口径对照表);2026 年的预测集中在 **50,000 台** 或以上,绝大多数在中国制造。Morgan Stanley 年内两次上调 2026 年中国出货预测——14K(2026-01)→ 28K(春季)→ **50K(2026-06)**。
- **2025 年出货量领先者**:AgiBot **5,168 台**(Omdia 第一,份额 39%),Unitree **按 Omdia 口径 4,200 台(第二)**——但 Unitree 自己的 IPO 招股书宣称 **>5,500 台** 并自居榜首(来源相互矛盾);UBTech 工业级出货 **>500 台**。Morgan Stanley 估计中国厂商占全球出货量 **>80%**;一份 2026-06 的报告称约 90%(汇总数据,未证实)。参见[产业版图:中国](landscape-china.md)。
- **两个泾渭分明的市场**:工业/物流(Digit、Apollo、Atlas、Walker S2、BMW 工厂里的 Figure)与家庭/消费(1X NEO、Figure 的家用布局、Tesla 的长期愿景)。
- **资本向美国集中**:Figure **超 $1B 的 C 轮,投后估值 $39B**(2025-09);Apptronik **$520M,估值约 $5B**(2026-02,A 轮累计 >$935M);Agility **$2.5B 投前估值 SPAC**(2026-06-24);Unitree **约 $618M 的上海科创板 IPO**——2026-06-01 过会,2026-07 获中国证监会注册批准——目标估值约 RMB 42B(约 $6.2B)。参见[投资](investment.md)。
- **长期预测**:Goldman Sachs 预测 2035 年市场规模 $38B;Morgan Stanley 预测 2050 年 $5T,消费时代价格降至 $15–50K。
- **软件才是护城河**:硬件规格正在趋同;差异化转向视觉-语言-动作模型(VLA)/基础模型技术栈(Figure Helix、Google DeepMind 模型上 Atlas 和 Apollo、XPeng VLA 2.0、1X Redwood)。参见 [VLA 模型](vla-models.md)和[技术现状](state-of-the-art.md)。
- **RaaS(机器人即服务)是主流工业商业模式**:GXO 签下行业首份多年期人形机器人 RaaS 合同(Agility,2024);Schaeffler、Toyota Canada、Mercado Libre 相继跟进;1X 开创了消费者订阅模式($499/月)。

## 平台对比表(截至 2026-07)

规格优先取自官方页面,否则取自媒体报道;易变数据均标注日期或说明。

| 平台 | 厂商(国家) | 身高 / 体重 | 自由度(DoF) | 负载 | 价格 | 状态 |
|---|---|---|---|---|---|---|
| Optimus V3(第 3 代) | Tesla(美国) | ~1.73 m / ~57 kg | 约 28 个躯体执行器 + 22 自由度手部(未证实) | ~20 kg(未证实) | 目标 $20–30K;制造成本估计 $50–100K+ | 数百台内部部署,"主要用于学习"(Musk,2026-01-28 的 Q4'25 财报电话会);">1,000 台在产线上"的说法仅见于聚合媒体,无一手来源(未证实);Fremont 产线约 2026-08 启动;2027 年前不对外销售 |
| Figure 03 | Figure(美国) | 5'8"(~1.73 m)/ 61 kg(官方) | Helix 驱动约 25 个躯体执行器;多自由度手部,指尖 3 g 触觉 | 20 kg(官方) | 不对外销售;在 BMW 约 $25/机器人小时(据报道);消费级目标约 $20K(未证实) | BMW Spartanburg 商业化运行;BotQ 产线约 1 台/小时,已生产 >350 台(官方,2026-05) |
| Atlas(电动版) | Boston Dynamics(美国/Hyundai) | ~1.5 m / ~89 kg(未证实) | 56(据报道) | 持续 30 kg / 瞬时 50 kg(未证实) | 不对外销售 | 2026 年产能全部锁定给 Hyundai RMAC 和 Google DeepMind;2028 年起进入 Metaplant |
| Digit v5 | Agility Robotics(美国) | ~1.75 m | — | ~16 kg(v4) | RaaS(未披露) | 在 9 个客户站点累计 65,000+ 小时;$300M 的 v5 合同订单 |
| Apollo | Apptronik(美国) | 1.73 m / ~73 kg | — | 25 kg | 未披露 | 在 Mercedes-Benz、GXO、Jabil 试点;2027 年起商业交付 |
| NEO | 1X(挪威/美国) | ~1.68 m / 30 kg(约 66 磅,得到 Witt 实地报道佐证) | 22 自由度手部;腱驱动躯体 | 可搬运约 25 kg,可举起 68 kg | **$20K 或 $499/月** | 消费者预订(2025-10)——前五天 10,000+ 订金(公司口径);2026 年起美国家庭交付,配合遥操作(teleoperation)辅助 |
| G1 | Unitree(中国) | 1.32 m / ~35 kg | 23–43 | 每臂约 2–3 kg | 起售 **$13.5K**(官方);EDU 版最高 $73.9K | 事实上的全球科研平台;2 m/s,续航约 2 小时 |
| H2 | Unitree(中国) | 1.8 m(官方)/ ~70 kg(体重未证实) | 31(官方) | — | 起售 **$29.9K**(官方基础版,直销:无灵巧手,不支持二次开发);美加经销商渠道 $40.9K"商业版"/ $68.9K EDU 版;H2 Plus $100K(官方) | 2025-10 发布;可选仿生面部 |
| R1 | Unitree(中国) | ~1.21 m / ~25 kg | ~26 | 轻载 | 起售 **$4,290–5,900** | 2025-07 发布;入选 TIME 2025 年度最佳发明;击穿了爱好者/科研级价格底线 |
| 远征 A2 / A3(Expedition) | AgiBot / 智元(中国) | A2 ~1.69 m | — | — | 约 $100K 级(A2,据报道) | 2026-03 下线累计第 10,000 台;面向物流、零售、服务 |
| Walker S2 | UBTech(中国) | ~1.76 m | — | — | 约 $150K 级(未证实) | 2025-11 起批量交付;客户含 BYD、Foxconn、Geely、FAW-VW、BAIC、SF Express;订单 >RMB 800M |
| IRON(下一代) | XPeng(中国) | 1.78 m / 70 kg | **82**(每手 22) | — | 估计约 $150K(未证实) | 3 颗 Turing 芯片(据报道 2,250–3,000 TOPS)、固态电池;量产目标 2026 年底 |
| GR-3 | Fourier(中国) | 1.65 m / 71 kg | 55 | GR 系列可提供最高 50 kg 的病患支撑 | 未披露 | 面向医疗/陪伴的"照护机器人";累计出货约 300 台(未证实) |
| Galbot G1 | Galbot(中国) | 轮式底盘 + 双臂 | — | — | 估计约 $87K(未证实) | 零售/药房业务覆盖 30+ 城市;CATL、Bosch 试点;估值 $3B |
| CyberOne | Xiaomi(中国) | 1.77 m / 52 kg | — | — | 约 $100K(估计) | 内部研发;未量产 |
| T1 / K1 | Booster Robotics(中国) | T1 ~1.2 m | 23 | — | K1 起售约 $6K | 教育及 RoboCup 首选平台 |
| SE01 / PM01 | EngineAI(中国) | 全尺寸 + 紧凑型 | — | — | PM01 约 $12–14K(未证实) | 2026-04 完成 $200M B 轮 |

## 真实部署——实际在运转的项目(截至 2026-07)

| 部署 | 机器人 | 状态 |
|---|---|---|
| BMW Spartanburg(美国) | Figure 02 → 03 | Figure 02 连续约 11 个月每天执行 10 小时班次,在 1,250+ 运行小时中装载 90,000+ 个零件,支撑 **30,000+ 台 BMW X3** 的生产;Figure 03 现从事排序物流(据报道约 40 台);据报道德国工厂也在试点 |
| GXO Logistics(美国) | Agility Digit(+ Apollo 试点) | 首个商业化人形机器人 RaaS 部署(2024-06);在佐治亚州 Flowery Branch 搬运 >100,000 个料箱(2025-11) |
| Schaeffler、Toyota Canada、Mercado Libre | Agility Digit | 在真实生产现场运行;安大略省 Woodstock 的 Toyota 工厂以 RaaS 方式引入 7 台 Digit(2026-02);计入 9 个设施累计 65,000+ 小时 |
| Mercedes-Benz(德国/匈牙利) | Apptronik Apollo | 在柏林 Marienfelde 数字工厂园区和 Kecskemét 从事厂内物流与质检;Mercedes 是其投资方;商业交付计划 2027 年 |
| Hyundai/Kia 美国工厂 | Boston Dynamics Atlas | 计划部署 **>25,000 台 Atlas**(2026 年宣布),2028 年从佐治亚 Metaplant 开始,2029 年扩展至 Kia 佐治亚工厂;规划年产 3 万台的机器人工厂;据报道遭遇工会抵制 |
| BYD、Foxconn、Geely、FAW-VW、Dongfeng、BAIC、SF Express(中国) | UBTech Walker S2 | 数百台;Walker 系列累计订单 >RMB 800M(约 $112M);柳州工厂目标年产 5 千台;2026-01 签署 Airbus 航空试点(未证实) |
| 中国零售/药房 | Galbot G1(轮式) | Galbot Store 自主零售覆盖 30+ 城市;北京 10+ 家药房;2026-04 起与 FamilyMart 合作 |
| Tesla Fremont(内部) | Optimus | 数百台内部部署,"主要用于学习和数据采集"(Musk,2026-01-28 的 Q4'25 财报电话会);聚合媒体流传的">1,000 台在产线上"无一手来源(未证实);所有数字均为公司自报 |
| 美国家庭 | 1X NEO | 预订已开放;2026 年底起交付;复杂家务依赖人工遥操作员("Expert Mode") |

关于两大主导国家生态的更多细节:[产业版图:中国](landscape-china.md)和[产业版图:美国](landscape-usa.md);欧洲/日本/韩国见[产业版图:其他地区](landscape-row.md)。

## 重点公司笔记

### 美国
- **Tesla** 于 2026-01 宣布终止 Model S/X 生产(最后一批车 2026-05 下线),将 Fremont 改造为 Optimus 产线;产线启动推迟至 2026 年 7 月底至 8 月,涉及约 10,000 个独立零件,初期产出"相当缓慢";第二条产线约 2027 年落地 Giga Texas(第 4 代)。Musk 目标 2027 年底前面向消费者销售,远期 Fremont 年产 100 万台、Giga Texas 年产 1,000 万台——均属愿景;Tesla 自 2021 年以来每一个 Optimus 时间表都跳票。V3 公开亮相再度推迟(2026-04)。硬件:AI5 芯片、Grok 语音集成(二手报道,未证实)。产线安装已在进行:Tesla 副总裁 Lars Moravy 称首条 Optimus 产线已运抵 Fremont 并开始安装,并强调其"模块化"设计;Musk 于 2026-07-01 发布了配文"Walking the Optimus production line in Fremont"的照片(截至 2026-07)——量产启动仍指引在 7 月底至 8 月。
- **Figure** 是资本最充裕的纯人形机器人公司(累计融资约 $1.9B;2025-09 投后估值 $39B;投资方包括 Parkway、Brookfield、NVIDIA、Intel Capital、Qualcomm Ventures、Salesforce)。Figure 03(2025-10 发布):比 02 轻 9%,执行器速度提升 2 倍,2 kW 感应式无线充电,相机帧率翻倍且视场角拓宽 60%,指尖触觉可感知至 3 克(官方)。BotQ 产线年产能 12,000 台,4 年目标 100,000 台;产出在不到 4 个月内从 1 台/天提升到约 1 台/小时(官方说法,2026-05)。Brookfield 的"Project Go-Big"开放约 100,000 套住宅单元用于第一人称视角训练数据采集——参见[数据](data.md)。
- **Boston Dynamics** 已全面淘汰液压系统;电动版 Atlas 采用 Hyundai Mobis 直驱执行器(约 220 Nm/kg 扭矩密度,未证实),并获 CES 2026 "最佳机器人"奖;与 Google DeepMind 的合作让 Gemini 系列模型登上 Atlas。参见[组织机构](organizations.md)。
- **Agility** 通过 Churchill Capital XI SPAC 上市:投前估值 $2.5B,总募资 >$620M($420M 信托 + 约 $200M PIPE,$10/股),Nasdaq 代码 AGLT,预计 2026 年底前完成。Digit v5 定位为首款"协作安全型"人形机器人(NVIDIA Halos);RoboFab(俄勒冈州 Salem)设计年产能 1 万台,美国本土零件占比约 75%。投资方:DCVC、NVIDIA、Amazon、SoftBank Vision Fund 2、Schaeffler、Foxconn、Playground Global。
- **Apptronik** A 轮累计 >$935M(含 2026-02 以约 $5B 估值追加的 $520M);Jabil 既为 Apollo 代工又在自家工厂试点;Google DeepMind 提供基础模型 AI。
- **Sanctuary AI(加拿大)** 是行业的前车之鉴:管理层动荡后,它将 AI 技术栈与 Phoenix 硬件解耦,现在面向存量工业机械臂销售"Physical AI"。
- **1X**(挪威创立,2022 年起总部设在硅谷)在订单量上是消费级领跑者:$20K 定价下 **10,000+ 份 NEO 订金**($200 订金)——据 Forbes 报道在 2025-10 预订窗口开放前五天内订满(公司口径——Stephen Witt 在 New Yorker 的报道(2026-07-06 刊)也转述了该数字,但未独立核实)。Witt 的实地探访(截至 2026-07)补充了新的运营细节:硅谷工业园总部约 **800 名员工**,覆盖装配、测试和研发(记者观察);工厂位于 **Oakland 附近**(Hayward 工厂 2026-05 启用);NEO 确认为 **约 66 磅(约 30 kg)**——Witt 以"公主抱"姿势将其抱起——行走噪音 **22 dB**("大约相当于微风吹拂树叶的音量"),两项均与官方规格表一致;手部耐久测试台上的手指弯折循环计数器显示 286 万次。公司在正式场合重申了 2026 年家庭交付承诺("这是我们对世界做出的承诺,必须兑现"——产品负责人 Dar Sleeper),但 Witt 看到的流畅厨房演示实为 VR 遥操作,且 1X 拒绝演示 NEO 的自主能力——可靠性/遥操作分析参见[开放问题](open-problems.md),家庭隐私角度参见[安全与监管](safety-regulation.md)。

### 中国
- **Unitree** 是价格颠覆者,并将成为中国 A 股首家"具身智能"上市公司:上海科创板 IPO(约 $618M / RMB 4.2B,估值约 $6.2B)于 2026-06-01 过会,2026-07 获证监会注册批准;招股书显示 2025 年营收约 RMB 1.7B(+335%),调整后净利润同比增长约 674%(2024 年即已盈利——参见 [Unitree 深度解析](company-unitree.md)),人形机器人占营收 >50%;2026 年目标出货最高 20,000 台人形机器人,对比 2025 年自称的 >5,500 台(Omdia 计为 4,200 台)。拥有行业最宽的价格阶梯:R1 $4,290 → G1 $13.5K → H2 $29.9K → 工业级。参见[硬件](hardware.md)。
- **AgiBot(智元)**,由前华为的邓泰华与彭志辉于 2023-02 创立,是累计出货量冠军(2026-03 下线第 10,000 台);A2 以 106.3 km 徒步(苏州→上海)创吉尼斯纪录;远征 A3(2026-02)瞄准互动服务场景;正寻求科创板借壳上市(状态未证实)。
- **UBTech**(港交所上市):Walker S2 的 3 分钟自主电池热插拔支持连续排班;订单簿 >RMB 800M 且持续增长;拥有行业内最广泛的蓝筹工厂客户名单。
- **Galbot** 融资 RMB 2.5B(约 $362M,2026-03 交割;2025-12 宣布 >$300M 的一笔),投资方包括中国国家"大基金"——国家级基金首次押注具身智能;累计融资约 $800M,估值约 $3B,是中国估值最高的未上市人形机器人公司。
- **XPeng** 将 IRON 视为与汽车相邻的产品:约 110,000 m² 的人形机器人专用工厂于 2026 年 Q1 破土动工,量产目标 2026 年底,2030 年累计 100 万台目标(愿景);首批部署在展厅、博物馆、零售场景。
- **Fourier** 借助康复机器人渠道切入"照护机器人"人形赛道(GR-3)——医疗是它的突破口,不同于其他厂商的工厂/仓储路线。

## 单位经济与价格趋势

- **BOM(截至 2026)**:Morgan Stanley 估算 **中国供应链下约 $46K/台,否则约 $131K**(以 Tesla Optimus Gen 2 级机器人建模;仅执行器就从 $22K 变为 $58K)——约 2.8 倍的差距同时驱动着中国的价格优势和美国的关税/回流张力。
- **成本结构**:执行器约占 BOM 的 35–40%,电池约 15–20%,机载算力约 10–15%(行业估计,未证实)。
- **价格史**:2023 年科研级人形机器人 $150K–500K($90K 的 Unitree H1 已算"便宜")→ 2025 年 G1 街价 $16K、R1 $5,900 → 2026 年 R1 双臂版起售 $4,290、Booster K1 约 $6K、1X NEO 消费版 $20K、G1 在 Amazon 上架 $17,990。西方工业平台仍维持 $100K+ 或仅 RaaS 模式(Figure 在 BMW 约 $25/机器人小时,据报道,未证实)。
- **反向趋势**:Morgan Stanley 预测人形机器人 BOM 在 2025→2030 间*上涨*约 15%(到 2045 年 +40%),原因是机载算力需求增长,尽管每 FLOP 成本在下降。
- **通缩驱动力**:中国的执行器/灵巧手(dexterous hand)供应链(谐波与行星减速器、灵巧手)正以每年约 15–20% 的速度压低零部件成本(报道估计)。开放问题:西方厂商是拼价格,还是拼自主软件?
- **利润率现实检验**:Agility 的 SPAC 文件显示了该行业典型的巨额亏损;各家公司的营收相对估值仍然很小(截至 2026-06)。

## 开放问题

- 依赖遥操作兜底的家用机器人(NEO)能否足够快地转化为真正的自主能力以留住消费者?参见[开放问题](open-problems.md)。
- 工业人形机器人在规模化后能否在 ROI 上胜过固定自动化 + AMR,还是只能困守既有厂房(brownfield)的利基场景?
- 面对 $46K 对 $130K 的 BOM 差距,关税/出口管制会将供应链割裂到什么程度?
- 可靠性数据稀缺:只有 Agility 公布机队运行小时数;全行业几乎没有公开的 MTBF 数据。

关于行业如何走到今天,参见[历史](history.md);关于仍未解决的问题(灵巧操作、可靠性、数据),参见[开放问题](open-problems.md)。

## 来源

- https://www.figure.ai/news/introducing-figure-03 — Figure 03 设计、触觉/相机规格、2 kW 无线充电、BotQ 年产 1.2 万台产能(官方)
- https://www.figure.ai/figure — Figure 03 官方规格页:5'8"、61 kg、20 kg 负载、5 小时续航、1.2 m/s(修正了此前二手来源的 1.68 m 数据)
- https://www.figure.ai/news/ramping-figure-03-production — BotQ 提速至 1 台/小时,已交付 >350 台(官方)
- https://www.figure.ai/news/series-c — Figure 超 $1B 的 C 轮,投后估值 $39B;投资方名单;Brookfield(官方)
- https://www.press.bmwgroup.com/global/article/detail/T0458778EN/bmw-group-advances-the-use-of-physical-ai-in-production-with-figure-03-project-in-spartanburg?language=en — BMW:Figure 02 试点(30,000+ 台 X3)、Figure 03 在 Spartanburg 从事排序作业(官方)
- https://www.1x.tech/discover/neo-home-robot — NEO 官方规格:30 kg、举重 68 kg、22 dB、22 自由度手部、$20K / $499/月(官方)
- https://www.therobotreport.com/1x-announces-pre-order-launch-neo-humanoid-robot/ — NEO 开放预订,2026 年美国 / 2027 年国际交付时间表
- https://www.newyorker.com/magazine/2026/07/06/are-humanoid-robots-ready-to-be-deployed — Stephen Witt 实地探访:$20K 定价下 10,000+ 订金、总部约 800 名员工、约 66 磅体重、22 dB、Oakland 附近工厂、2026 年交付承诺、遥操作演示披露(经 Wayback 快照读取)
- https://www.forbes.com/sites/johnkoetsier/2026/04/30/1x-kicks-off-full-scale-production-of-humanoid-robot-neo/ — Forbes:2025-10 预订窗口前五天订满 10,000 台 NEO(公司口径);2026-04 启动全面量产
- https://www.unitree.com/g1/ — G1 官方规格:35 kg、23–43 自由度、起售 US$13.5K、续航约 2 小时(官方)
- https://www.humanoidsdaily.com/news/unitree-expands-r1-lineup-with-dual-arm-modular-platform-starting-at-4-290 — Unitree R1 产品线起售 $4,290
- https://shop.unitree.com/products/unitree-h2 — H2 官方:标准版 $29.9K、H2 Plus $100K;180 cm、31 自由度、360 N·m;仅 EDU 版支持二次开发
- https://robohorizon.com/en-us/news/2025/11/unitree-h2-price-and-limitations/ — H2 $29.9K 的细则:基础配置、不可升级灵巧手、依赖 App 控制
- https://botinfo.ai/articles/unitree-h2-humanoid-robot — 美加经销商价格档:$40.9K "商业版"(无 SDK,8 个月保修)、$68.9K EDU 版(完整 SDK/ROS 2)
- https://autonews.gasgoo.com/articles/news/unitree-wins-ipo-approval-as-robot-makers-face-tougher-profit-challenges-2061816669448765440 — Unitree 上海 IPO 获批(估值约 $6.2B)
- https://www.caixinglobal.com/2026-07-03/unitree-robotics-wins-approval-for-618-million-star-market-ipo-102460136.html — Unitree 获证监会注册批准(募资 $618M,目标估值 RMB 42B,2025 年营收 RMB 1.69B)
- https://roboticsandautomationnews.com/2026/03/31/unitree-robotics-files-for-610-million-ipo-as-humanoid-robot-sales-surge/100272/ — Unitree 招股书:2025 年营收 +335%,出货 >5,500 台人形机器人(该文"首个盈利年度"的表述不准确——招股书显示 2024 年已盈利)
- https://www.forbes.com/sites/jonmarkman/2026/04/27/unitree-g1-humanoid-robots-are-reshaping-the-robotics-investment-stack/ — Unitree 营收增长、2026 年 2 万台出货目标
- https://www.agilityrobotics.com/content/agility-robotics-to-go-public-through-merger-with-churchill-capital-corp-xi — SPAC 条款($2.5B、$420M 信托 + $200M PIPE、AGLT)、$300M 的 Digit v5 订单、6.5 万小时、9 个设施、RoboFab 年产 1 万台、75% 美国本土零件(官方)
- https://www.agilityrobotics.com/content/gxo-signs-industry-first-multi-year-agreement-with-agility-robotics — 首份人形机器人 RaaS 合同(官方)
- https://www.geekwire.com/2026/digit-maker-agility-robotics-to-go-public-in-2-5b-deal-heres-what-the-filings-say-about-its-finances/ — 从 SPAC 文件解读 Agility 财务
- https://www.therobotreport.com/humanoid-maker-agility-robotics-go-public-through-spac-merger/ — SPAC 条款的独立确认、9 个客户设施累计 65,000+ 小时、$300M v5 订单
- https://apptronik.com/news-collection/apptronik-closes-over-935-million-series-a — Apptronik A 轮累计 >$935M(官方)
- https://www.cnbc.com/2026/02/11/apptronik-raises-520-million-at-5-billion-valuation-for-apollo-robot.html — $520M 追加,估值约 $5B;Mercedes/GXO/Jabil 试点
- https://group.mercedes-benz.com/company/production/procuction-network/mbdfc-humanoid-robots.html — Apollo 在 Mercedes 柏林/Kecskemét 的岗位(官方)
- https://www.hyundainews.com/releases/4664 — Hyundai CES 2026 机器人战略,2028 年 Atlas 进 Metaplant,年产 3 万台机器人工厂(官方)
- https://interestingengineering.com/ai-robotics/hyundai-25000-atlas-humanoid-robots-us-plants — Hyundai 在美国工厂部署 25,000+ 台 Atlas 的计划
- https://bostondynamics.com/blog/boston-dynamics-unveils-new-atlas-robot-to-revolutionize-industry/ — 电动版 Atlas 发布(官方)
- https://electrek.co/2026/04/22/tesla-optimus-production-fremont-model-sx-line/ — Optimus V3 延期、Fremont Model S/X 产线改造
- https://electrek.co/2026/01/28/musk-admits-no-optimus-robots-are-doing-useful-work-at-tesla-after-claiming-otherwise/ — Q4'25 财报电话会:数百台部署"主要用于学习","仍处研发阶段"
- https://www.benzinga.com/markets/tech/26/07/60209589/elon-musk-says-teslas-model-s-model-x-line-is-now-building-optimus-robots — Musk 发布 Fremont 首条 Optimus 产线照片(2026-07-01);Moravy:产线已到位、安装已开始、"模块化"设计
- https://www.electrive.com/2026/05/11/final-tesla-model-s-rolls-off-the-production-line/ — 最后一台 Model S/X 于 2026-05 在 Fremont 下线
- https://www.automate.org/robotics/industry-insights/boston-dynamics-to-begin-production-on-redesigned-atlas-humanoid-in-2026 — 2026 年 Atlas 产能全部锁定给 Hyundai RMAC 与 Google DeepMind;其他客户 2027 年初起供货
- https://www.prnewswire.com/news-releases/ubtech-humanoid-robot-walker-s2-begins-mass-production-and-delivery-with-orders-exceeding-800-million-yuan-302616924.html — Walker S2 批量交付、RMB 800M 订单、年产 5 千台产能目标(官方通稿)
- https://www.therobotreport.com/agibot-rolls-out-10000th-humanoid-robot/ — AgiBot 第 10,000 台机器人(2026-03-31)、Omdia/IDC 2025 排名
- https://www.xpeng.com/news/019a56f54fe99a2a0a8d8a0282e402b7 — 下一代 IRON:82 自由度、Turing 芯片、VLA 2.0、固态电池(官方)
- https://www.humanoidsdaily.com/news/xpeng-to-break-ground-on-full-chain-humanoid-factory-to-meet-2026-production-goal — XPeng 110,000 m² 人形机器人工厂,2026 年底量产
- https://technode.com/2026/03/02/humanoid-robot-maker-galbot-raises-rmb-2-5-billion/ — Galbot RMB 2.5B 融资,含国家大基金
- https://www.prnewswire.com/news-releases/galbot-secures-over-300-million-in-new-funding-breaking-records-with-3-billion-valuation-in-chinas-humanoid-robot-sector-302647204.html — Galbot $300M+ 融资、$3B 估值(官方通稿)
- https://www.therobotreport.com/galbot-brings-in-300m-to-scale-mobile-manipulator-deployments/ — Galbot 部署情况:30+ 城市、药房
- https://www.cnbc.com/2026/06/24/morgan-stanley-china-humanoid-robot-market-forecast.html — Morgan Stanley 2026 年中国预测上调 14K → 28K → 50K(2026-06-24);中国厂商占 2025 年全球出货 >80%
- https://www.cryptopolitan.com/morgan-stanley-doubles-chinas-humanoid-shipment-target-to-50000/ — Morgan Stanley 将 2026 年中国出货预测上调至 5 万台
- https://www.scmp.com/tech/tech-trends/article/3339346/chinese-firms-outpace-us-rivals-2025-humanoid-robot-shipments-agibot-takes-lead — Omdia 2025 排名:AgiBot 5,168 台(39%)、Unitree 4,200 台(32%)、全球约 1.3 万台
- https://www.scmp.com/tech/article/3337151/china-packs-patent-punch-race-build-humanoid-robots — Morgan Stanley BOM:中国供应链 $46K 对比 $131K(以 Optimus Gen 2 建模;执行器 $22K → $58K)
- https://www.investing.com/news/stock-market-news/morgan-stanley-projects-a-humanoids-chip-tam-of-305b-by-2045-4384088 — Morgan Stanley:因算力/芯片单价上升,人形机器人 BOM 2025→2030 +15%(到 2045 年 +40%)
- https://www.morganstanley.com/insights/articles/humanoid-robot-market-5-trillion-by-2050 — 2050 年 $5T 市场预测、BOM 趋势(到 2030 年 +15%)
- https://www.goldmansachs.com/insights/articles/the-global-market-for-robots-could-reach-38-billion-by-2035 — Goldman 2035 年 $38B 预测
- https://www.techtimes.com/articles/318641/20260618/humanoid-robots-china-ships-90-global-units-now-leads-ai-benchmarks.htm — 中国占比约 90% 的说法;AgiBot/UBTech/Galbot/Fourier 累计里程碑
- https://cnmra.com/who-will-be-the-real-winner-in-the-implementation-of-embodied-ai-scenarios-in-2026/ — EngineAI $200M B 轮(2026-04)
