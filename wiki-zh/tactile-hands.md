---
title: 触觉感知与灵巧手
slug: tactile-hands
updated: 2026-07-03
confidence: verified
lang: zh
source: ../wiki/tactile-hands.md
---
> 灵巧手(dexterous hand)与触觉感知是 Physical AI 中最薄弱的硬件分支:其他所有子系统(腿部、执行器、算力、电池)都已收敛出"标准技术栈",唯独手仍是耐久性最差、成本最高、生态最碎片化的部件——而且触觉至今仍完全缺席前沿机器人策略模型。截至 2026-07,市场价差跨越 100 倍(AgiBot OmniHand 约 $1.4k 入门级到 Shadow Hand 约 $100–150k),两种感知路线并立(相机加凝胶的视觉触觉 vs 廉价触点阵列),同时中国主导的量产浪潮(2025 年全球出货 >30k 只手,基于 Gasgoo 推算)正在以远超耐久性和数据管线改善速度的节奏压低价格。触觉优先的模型(AnyTouch、TLA、VLA-Touch、OmniVTLA、FTP-1)和数据集(Touch100k、TacQuad、Daimon-Infinity)在 2025–26 年涌现,但还没有任何前沿[视觉-语言-动作模型(VLA)](vla-models.md)把触觉作为一等输入。本页深入覆盖手部硬件与触觉感知;策略/学习侧见[操作](manipulation.md),执行器/算力见[硬件](hardware.md)。

## 为什么手是最薄弱的分支

- 运动控制已在模拟到现实(sim2real)强化学习和标准执行器上收敛;手没有——接触物理很难仿真,导致手部硬件无法在仿真中低成本验证或训练(见[仿真](simulation.md))。
- 一只 20+ 自由度的手把最难的工程约束集中在最小的体积里:驱动密度、热限制、走线、传感器空间,以及持续的碰撞暴露。
- 该子系统承受三重惩罚:单机成本占比仅次于执行器、故障率最高(手指总在磕碰)、数据可得性最低(人类视频和多数遥操作(teleoperation)语料中都不含触觉信号——见[数据](data.md))。
- 截至 2026 正在形成的设计共识:把执行器移到前臂,用肌腱驱动手指(Tesla Optimus Gen-3、Figure 03、DexRobot)——为传感腾出手部体积,代价是线缆磨损以及控制中的摩擦/迟滞。

## 手部产品格局(截至 2026-07)

| 手 | 厂商(产地) | 自由度 | 驱动方式 | 触觉 | 价格(截至 2026) | 备注 |
|---|---|---|---|---|---|---|
| Shadow Dexterous Hand | Shadow Robot(英国) | 24 关节,20 主动 | 肌腱(电动/气动) | 129 个传感器;可选 BioTac/GelSight | 约 $100k–150k | 自 OpenAI Dactyl 以来的研究级自由度标杆;2.8 kg |
| Optimus Gen-3/V3 手 | Tesla(美国) | 22 手部 + 3 腕部 | 肌腱,每前臂约 25 个执行器(专利分析,未证实) | 指尖力感知;更大面积覆盖开发中 | 不对外销售 | V3 量产爬坡目标 2026 下半年(二手来源,未证实) |
| Figure 03 手 | Figure(美国) | 约 16(F02 基线) | 肌腱,置于前臂 | 指尖传感器可检测约 3 g 的力;每手一个掌心相机 | 不对外销售 | 因现有方案"无法承受真实世界使用"而自研传感器;设计原则:"极致耐久、长期可靠、高保真感知" |
| SharpaWave | Sharpa(新加坡) | 22 | 电机驱动,人手尺寸(1.2 kg) | 视触觉指尖:每指 >1,000 个触觉像素,0–30 N 量程内 0.005 N 灵敏度,180 FPS | 约 $50k(36kr 数字,未证实) | 指尖 >20 N;认证 100 万次抓取循环(公司口径);2025-10 起出货;进入 NVIDIA/Unitree H2 Plus 参考设计(2026-06) |
| Unitree Dex5-1 | Unitree(中国) | 20(16 主动 + 4 被动) | 直驱,约 1 kg | 可选 94 点阵列 @1 kHz | 美国经销商 $25k–27k;灰市/Alibaba 挂牌约 $6k–8k;无官方定价(未证实) | 指尖约 10 N,重复精度约 1 mm;手指可单独更换 |
| Inspire RH56E2 / FTP | Inspire Robots(中国) | 6 主动 | 连杆 | 最多 17 个触觉垫,量程 0–30 N | $8,900(美国零售,触觉配置);基础 DFX 型号更便宜 | 出货主力:2025 年交付约 1 万只;790 g,指尖约 30 N |
| Linker Hand L20 | LinkerBot(中国) | 20(16 主动 + 4 被动) | 电机 | 72 单元(6×12)阵列 @200 FPS;可选 VBT/电子皮肤 | RMB 49,900(约 $7k);L20 Lite <$5k | 100 N 握力;2025 年交付 >1 万只;O7(7 主动自由度)为低价线,L25/L30 为更高档位 |
| DexHand021 | DexRobot(中国) | 22(腕部一体) | 双肌腱 | 全掌多模态(Pro) | 零售约 $9.5k;Pro 约 $14k–28k | 50 N 负载,>30 万次循环宣称(公司 PR,未证实) |
| OmniHand 2025 | AgiBot/智元(中国) | 16(10 主动 + 6 被动) | 电机,500 g | 400+ 力感知点,滑移检测 | RMB 9,800–14,800(约 $1.4k–2.1k) | 最便宜的可信触觉手;Pro:19 自由度,0.1 N 分辨率;手部业务已拆分为独立公司(2026) |
| PaXini DexH13 | PaXini Tech(中国) | 13 | 电机 | 1,140 个多维触觉单元(宣称感知 15 个维度) | n/a(询价) | 在 CES 2026 提出"触觉基础设施"全栈路线 |
| Allegro Hand V5 | Wonik Robotics(韩国) | 16 | 电机 | 可选;Digit 360 集成伙伴 | 约 $15k–30k(二手来源) | 长期存在的研究级中档产品;Wonik 是 Meta 的 Digit 360 商业化手部伙伴 |
| DG-5F | Tesollo(韩国) | 20 | 电机 | 可选 | n/a | 瞄准人形机器人 OEM 市场 |
| F-TAC Hand | 北大 + BIGAI(中国,研究) | 15(拟人运动学) | 电机 | 17 个 VBT 传感器覆盖约 70% 掌面,0.1 mm 分辨率 | 不对外销售 | Nature Machine Intelligence 2025-06;迄今在手上演示的最密集触觉覆盖 |

- 市场结构:高端视触觉档(SharpaWave、Shadow)、$5k–10k 的中国高自由度档(LinkerBot L20、DexRobot、Inspire 触觉配置——Unitree 的 Dex5-1 只在灰市挂牌里出现在这一档;在西方经销商处要 $25k+),以及低于 $2.5k 的入门档(OmniHand RMB 9,800、LinkerBot O6/O6 Lite RMB 6,666/3,999、Inspire 基础款)——出货量正在向中间档位集中。
- 人形机器人 OEM(Tesla、Figure)自研手且不外售;中国 OEM 则越来越多地外购或拆分(智元的手部业务拆分预示着零部件供应商层正在形成,类似汽车行业的 Tier-1)。

## 视觉触觉(VBT):GelSight 谱系

相机注视一层可变形、带照明的凝胶皮肤;光度立体法可以以最高微米级分辨率恢复接触几何。

- 谱系:retrographic sensing(Johnson & Adelson,MIT,2009)→ GelSight Inc 拆分成立 → GelSlim(MIT)、DIGIT(Meta,2021,低成本开放设计,由 GelSight 制造)→ GelSight Mini(2022:单机 $499、替换凝胶 $49——正是这个价格让 VBT 成为大众化研究工具)→ 2024–25 各类变体(GelBelt、ThinTact、DTactive;见[操作](manipulation.md))。
- **Meta × GelSight Digit 360**(2024-10):指尖造型,约 830 万触点,全向形变捕捉,约 1 mN 力灵敏度,18+ 种感知模态(含振动、热、通过气体传感器感知气味),端上处理。向部分研究者免费分发;经 GelSight 和 Wonik Robotics 商业化;设计/代码完全开源。
- **F-TAC Hand**(北大/BIGAI,Nature MI 2025-06):第一只把 VBT 作为结构件而非外挂的手——17 个传感器以 6 种构型兼作承力部件,以 0.1 mm 分辨率覆盖约 70% 抓取表面;在 600 次真实世界对抗性抓取试验中优于无触觉基线。
- **Daimon Robotics DM-Tac**(深圳):宣称 40,000 感知单元/cm² 和 500 万次按压耐久(公司数据,未证实);搭载于 Daimon 自家手上并供给其 VTLA 模型线——中国最激进的商业化 VBT 押注。
- **Sharpa DTA**:180 FPS 动态触觉阵列,亚毫米空间分辨率——量产商用手中第一个 VBT 级感知(2025-10 出货;"第一"为公司/媒体表述,未证实)。
- 让 VBT 难以进入多数量产手的弱点:凝胶/皮肤磨损(ORCA 手研究中软硅胶指尖皮肤在约 2,000–4,000 次抓取循环内退化;GelSight 级凝胶是消耗品)、每指相机的体积与成本、帧率跟不上 1 kHz 控制回路,以及凝胶永久形变带来的标定漂移。

## 触点阵列、力/力矩与新兴电子皮肤

**触点阵列(taxel arrays)**(压阻/电容/磁式触垫)之所以在量产手上胜出,是因为它们薄、便宜、经得起接触:

| 系统 | 密度/数量 | 速率 | 状态 |
|---|---|---|---|
| Unitree Dex5-1 | 每手 94 点 | 1 kHz | 出货中(可选) |
| Inspire FTP 系列 | 每手 17 个触垫,0–30 N | — | 出货中 |
| LinkerBot L20 | 72 单元(6×12) | 200 FPS | 出货中 |
| AgiBot OmniHand | 400+ 点,0.1 N 分辨率(Pro) | — | 出货中 |
| PaXini ITPU | DexH13 上 1,140 个单元;宣称 15 个维度 | — | 出货中(需询价) |
| Tacta | 361 感知单元/cm²,4.5 mm 模块;全手演示 1,956 感知单元 | 1 kHz | CES 2026 演示(公司口径,未证实) |
| Figure 03 指尖 | 力检测阈值约 3 g | — | 自研,量产 |

- 与 VBT 的取舍:触点阵列以 kHz 速率给出力分布但没有精细几何;VBT 给出几何/纹理但脆弱且慢。混合式手(LinkerBot 可选 VBT 模块、SharpaWave 相机+触点指尖)两头下注。
- **力/力矩感知**(在[硬件](hardware.md)中深入讨论):六轴腕部 F/T 传感器加基于电流的关节力矩估计;中国供应商正快速上量。就手而言,指尖三轴力 + 关节电流是常见量产配方;每指全六轴仍停留在研究级。
- **新兴电子皮肤**:机器人电子皮肤(e-skin)市场估计 $266M(2025)→ $795M(2034)(市场研究,未证实);PDMS 基底占主导,石墨烯复合导体正在兴起;具备局部"疼痛"反射与模块化修复的神经形态电子皮肤已被演示(PNAS,2026);基于 EIT 的可拉伸皮肤和电容式大面积皮肤(CushSense)瞄准全臂/全身覆盖而非指尖。截至 2026-07,均未进入量产人形机器人。

## 触觉数据集与触觉优先模型

约束核心是数据:触觉无法从互联网抓取,遥操作装置很少记录它,而且每种传感器说的都是不同的"语言"(分辨率、凝胶光学、力标定)。

**数据集(截至 2026-07):**
- **Touch100k** — 首个达到 10 万样本规模的触觉-语言-视觉数据集;支撑 GelSight 风格的表征预训练(TLV-Link)。
- **TacQuad** — 覆盖 GelSight Mini、DIGIT、DuraGel、Tac3D 的多传感器对齐数据;专为攻克跨传感器迁移而建。
- **Daimon-Infinity**(2026-04):含触觉的多模态具身数据集;10,000 小时已在阿里 ModelScope 开源,宣称约 10 亿数据点,公司预计 2026 年底达到"数百万小时"(公司口径,未证实)——若属实将是最大的开放触觉标注语料。
- **RobOmni**(Daimon × Galbot,2026):隔离衡量触觉感知对操作提升多少的基准——对该领域触觉评测空白的早期回应(见[评测](evaluation.md))。

**模型:**
- **AnyTouch**(ICLR 2025)与 AnyTouch 2(2026):跨异构视触觉传感器的统一静态+动态表征——"传感器巴别塔"的变通方案。
- **TLA**(2025):面向接触密集任务(如轴孔装配)的触觉-语言-动作模型,通过跨模态语言对齐实现。
- **VLA-Touch**(2025):在不重训主干的情况下,为现有 VLA 外挂双层触觉反馈。
- **OmniVTLA**(2025-08)与 **TacVLA**(2026):带语义对齐触觉编码器的视觉-触觉-语言-动作架构。
- **FTP-1**(2026):跨触觉传感器训练、面向富接触操作的通用"基础触觉策略"——触觉领域第一个明确的基础模型叙事。
- 现状核查:以上均为研究规模;截至 2026-07,没有任何前沿 VLA(π 系列、Helix、Gemini Robotics、GR00T)把触觉输入作为有文档记载的一等模态(Figure 03 出厂带触觉指尖并称其支持滑移感知抓取,但 Figure 尚未公布 Helix 将触觉作为模型输入)。Daimon 的 VTLA 线是最接近的商业尝试(单一厂商,性能未证实)。

## 中国的灵巧手量产经济学

- 2025 年全球已知灵巧手出货超 30,000 只(Gasgoo 基于全球 >1.5 万台人形机器人出货、每台两只手推算;中国厂商占主导;单一来源);Inspire 约 1 万只(是其 2024 年 2,000 只的 5 倍),LinkerBot 于 2025-12 出货第 10,000 只手(峰值月份 >4,000 只;公司 PR),2026 年目标 5 万–10 万只(公司表态,未证实)。
- 产能扩张(截至 2026):Xynova 工厂计划 2026 年 Q2 投产,年产能 1 万只手(在手订单已 >1 万只);ENCOS 宣布全面量产;智元/AgiBot 将手部业务拆分为独立供应商(上海"临界点",2026)——市场正垂直分化出零部件层(见[格局:中国](landscape-china.md))。
- 价格崩塌的机制复刻了 EV/G1 剧本:本土电机/减速器/传感器供应链、人形机器人的共同需求拉动,以及激进的入门定价(OmniHand 的 RMB 9,800 首发折扣)。一只 20 自由度触觉手 2020 年成本 $100k+(Shadow 级);2025 年约 $7k(LinkerBot L20 级);入门级约 $1.4k–2.1k(OmniHand,2025-08 发布)。
- 低价买到的是什么并不清楚:各档位的耐久循环、持续负载下的力精度、触觉标定稳定性都没有独立审计(截至 2026-07);买家反馈品质差异很大(轶事性,未证实)。
- 西方/韩国的站位:高端感知(Sharpa 约 $50k、Digit 360 研究生态)或垂直整合(Tesla、Figure 自研)。截至 2026-07,没有任何美国/欧洲厂商参与 $5k–10k 的走量档位竞争。

## 为什么灵巧性仍是缺口

- **耐久性**:手指常年处于碰撞之中。肌腱/线缆磨损、软皮肤退化(ORCA 研究中约 2,000–4,000 次抓取循环,信号线在 4,500–7,000 次循环时断裂)以及连接器疲劳使手成为维护成本最高的子系统;厂商耐久宣称(SharpaWave 100 万次抓取循环、DexRobot >30 万次、DM-Tac 500 万次按压)均为公司自证,未经独立审计。
- **控制退化**:肌腱传动存在摩擦、迟滞和标定漂移,会在部署时间尺度上侵蚀重复精度——一篇 2026 年综述指出这些问题在手部评测中被系统性低报。
- **传感器漂移**:压阻触点因纳米颗粒分散和微结构差异出现初始电阻漂移;VBT 凝胶会永久形变;二者都需要重标定回路,而截至 2026-07 尚无量产技术栈将其自动化。
- **数据稀缺**:人类视频、多数遥操作装置和所有网络规模语料中都没有触觉;上述数据集比视觉-语言预训练数据小 3–5 个数量级。
- **传感器碎片化**:没有标准的触觉"格式"——跨传感器迁移(AnyTouch、TacQuad、FTP-1)仍是活跃的研究领域,而非已解决的管线问题。
- **仿真缺口**:凝胶光学、软接触和触点响应比刚体接触更难仿真,堵住了曾解决[运动控制](locomotion.md)的模拟到现实路径。
- **经济性 vs 需求**:多数已部署任务(物流拣选)用平行夹爪就能赚钱,所以手缺少让其他一切持续改进的部署驱动数据飞轮("夹爪够用"论见[操作](manipulation.md);更广泛的未解问题见[开放问题](open-problems.md))。

## 关注事项

- 2026 年是否会有前沿 VLA 把触觉作为一等输入(候选:π 系列后继、Daimon VTLA、FTP-1 规模化)?
- Daimon-Infinity 的"2026 年底数百万小时"宣称——若属实将是第一个互联网规模的触觉语料。
- $5k–10k 中国手档位的独立耐久性审计;LinkerBot 能否达到 5 万–10 万只。
- VBT 进入量产的轨迹:SharpaWave 的现场可靠性 vs Figure 明确的反凝胶耐久性押注。
- Tesla 的 V3 手爬坡(目标 2026 下半年)能否在汽车级产量下验证前臂肌腱架构。

## 来源

- https://www.robotwale.com/article/dexterous-hands-shadow-allegro-inspire-race-to-5-finger-dexterity — Shadow 约 $100k–150k、Allegro 约 $15k–30k 价格区间。
- https://www.shadowrobot.com/wp-content/uploads/2022/03/shadow_dexterous_hand_e_technical_specification.pdf — Shadow Hand:24 关节/20 主动,129 个传感器,2.8 kg。
- https://www.sharpa.com/pages/wave — SharpaWave:22 自由度,每指尖 >1,000 触觉像素,0.005 N 灵敏度,指尖 >20 N,100 万次循环认证。
- https://www.cnx-software.com/2026/06/02/sharpa-wave-high-end-dexterous-robotic-hand-with-22-dof-high-sensitivity-dynamic-tactile-array/ — SharpaWave DTA:180 FPS,亚毫米分辨率,1.2 kg。
- https://www.humanoidsdaily.com/news/sharpa-robotics-begins-shipping-sharpawave-dexterous-hand — SharpaWave 自 2025-10 起出货。
- https://roboticsandautomationnews.com/2026/06/09/sharpa-brings-dexterous-robot-hands-to-nvidia-and-unitree-humanoid-reference-design/102424/ — Sharpa 进入 NVIDIA/Unitree H2 Plus 参考设计;约 $50k 价格提及(二手来源)。
- https://www.unitree.com/mobile/Dex5-1/ — Dex5-1:20 自由度,94 触觉点,1 kHz,手指可更换。
- https://robostore.com/products/unitree-dex5-1 — Dex5-1 美国经销商预售 $25,000(尚未发货)。
- https://www.usrobotstore.com/products/unitree-5-finger-dexterous-hand-20-dof-dex5-1-dex5-1p-compatible-with-unitree-h2 — Dex5-1/Dex5-1P 美国经销商 $27,000;Alibaba 灰市挂牌约 $7k–8k(未证实)。
- https://www.usrobotstore.com/products/inspire-robots-5-finger-robotic-dexterous-hand-rh56e2 — Inspire RH56E2:$8,900,6 自由度,17 个触觉垫,790 g,指尖约 30 N。
- https://aifitlab.com/products/linkerbot-linker-hand-l20 — Linker Hand L20:20 自由度,72 单元阵列,100 N 握力,RMB 49,900。
- https://kr-asia.com/linkerbot-raises-new-funding-to-build-a-full-stack-platform-for-robot-dexterity — LinkerBot 融资、全栈平台,O6/O6 Lite/L6/L30 定价(RMB 3,999–99,900)。
- https://www.prnewswire.com/news-releases/10-000-dexterous-hands-shipped-150-million-raised-linkerbot-leads-the-market-302645409.html — LinkerBot 第 10,000 只手出货(2025-12-18),峰值月份 >4,000 只,融资 $150M(公司 PR)。
- https://www.prnewswire.com/news-releases/dexrobot-unveils-full-dexterous-hand-series-and-new-dextele-teleoperation-system-at-automate-2026-302808579.html — DexHand021 系列规格(公司 PR)。
- https://news.futunn.com/en/flash/19251630/zhiyuan-robotics-has-released-the-omnihand-2025-dexterous-hand-with — OmniHand 2025 定价(RMB 9,800 首发 / 14,800 触觉版)。
- https://store.agibot.com/products/omnihand-pro-2025 — OmniHand Pro:19 自由度,750 g,0.1 N 分辨率。
- https://humanoid.guide/product/dexh13/ — PaXini DexH13:1,140 个触觉单元。
- https://www.koreaherald.com/article/10651060 — PaXini 在 CES 2026 提出"触觉基础设施"全栈矩阵。
- https://www.therobotreport.com/tesollo-unveils-dexterous-robot-hand-for-humanoids/ — Tesollo DG-5F 20 自由度。
- https://www.teslarati.com/tesla-optimus-v3-hand-arm-details-revealed-new-patents/ — Optimus V3 手部专利:22 自由度,前臂肌腱驱动(二手来源)。
- https://www.figure.ai/news/introducing-figure-03 — Figure 03:约 3 g 指尖检测,掌心相机,以耐久性为导向的传感器设计。
- https://www.nature.com/articles/s42256-025-01053-3 — F-TAC Hand(Nature MI 2025-06):17 个 VBT 传感器,约 70% 覆盖,0.1 mm 分辨率,600 次试验。
- https://arxiv.org/abs/2412.14482 — F-TAC Hand 预印本,含设计细节。
- https://www.businesswire.com/news/home/20241031980322/en/GelSight-and-Meta-AI-Introduce-Digit-360-Tactile-Sensor — Digit 360:830 万触点,约 1 mN,18+ 模态。
- https://ai.meta.com/blog/fair-robotics-open-source/ — Digit 360 开源发布;GelSight + Wonik 商业化合作。
- https://www.gelsight.com/gelsightmini/ — GelSight Mini $499 / 凝胶 $49。
- https://autonews.gasgoo.com/articles/news/daimon-robotics-releases-embodied-dataset-daimon-infinity-2044748516201508865 — Daimon-Infinity:2026-04,1 万小时开源,约 10 亿数据点,DM-Tac 40k 单元/cm² 与 500 万次按压宣称。
- https://spectrum.ieee.org/daimon-robotics-physical-ai — DAIMON Robotics VBT + VTLA 介绍。
- https://www.therobotreport.com/daimon-robotics-and-galbot-jointly-launches-robomni-for-benchmarking-tactile-perception-and-dexterous-manipulation/ — RobOmni 触觉-操作基准。
- https://arxiv.org/html/2406.03813v1 — Touch100k 数据集。
- https://arxiv.org/pdf/2502.12191 — AnyTouch(ICLR 2025)+ TacQuad 多传感器数据集。
- https://arxiv.org/pdf/2602.09617 — AnyTouch 2:动态触觉表征学习。
- https://arxiv.org/html/2508.08706v1 — OmniVTLA:带语义对齐触觉的视觉-触觉-语言-动作模型。
- https://arxiv.org/pdf/2603.12665 — TacVLA:面向 VLA 的接触感知触觉融合。
- https://arxiv.org/pdf/2606.13102 — FTP-1:跨传感器的通用基础触觉策略。
- https://github.com/linchangyi1/Awesome-Touch — 触觉感知/策略精选索引(TLA、VLA-Touch、PolyTouch)。
- https://autonews.gasgoo.com/articles/news/from-prototypes-to-production-dexterous-hands-kick-off-a-mass-production-race-2016425582734970881 — 中国 2025 年出货 >30k(推算)、Inspire 约 1 万只、LinkerBot 目标、Xynova 工厂。
- https://autonews.gasgoo.com/articles/news/zhiyuan-robot-spins-off-dexterous-hand-business-humanoid-robots-trigger-a-division-of-labor-revolution-2013868661754662912 — 智元手部业务拆分。
- https://autonews.gasgoo.com/articles/news/encos-dexterous-hand-enters-full-mass-production-2008795632859136001 — ENCOS 全面量产。
- https://arxiv.org/html/2404.19448v1 — 压阻软皮肤手:5,000 次循环内传感器漂移 <0.3%;皮肤在装配过程中破裂(不含 2k 循环数字;见下方 ORCA)。
- https://link.springer.com/article/10.1007/s44245-026-00275-y — 2026 年综述:手部评测中肌腱摩擦/迟滞/标定漂移被低报。
- https://pmc.ncbi.nlm.nih.gov/articles/PMC11677542/ — 压阻触点初始电阻漂移及重复性修正。
- https://www.pnas.org/doi/10.1073/pnas.2520922122 — 具备疼痛/损伤感知与模块化修复的神经形态电子皮肤。
- https://www.intelmarketresearch.com/robot-electronic-skin-market-27486 — 电子皮肤市场 $266M(2025)→ $795M(2034)(市场研究,未证实)。
- https://arxiv.org/html/2504.04259v2 — ORCA 手:硅胶皮肤在约 2,000–4,000 次抓取循环内退化,信号线在约 4,500–7,000 次循环断裂;面向不间断灵巧学习的可靠性/成本框架。
