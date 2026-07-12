---
title: 公司档案:Scale AI 机器人数据业务 (Company Dossier: Scale AI Physical AI)
slug: case-scale
updated: 2026-07-12
confidence: verified
---
> **说人话:**这家是硅谷最大的 AI 数据标注公司 Scale AI 里的一个新事业部,叫 Physical AI(具身智能数据业务)。它卖的是"喂机器人模型的操作数据"——用穿戴设备和真机遥操作采集人类演示,加工标注后卖给 Physical Intelligence、Generalist 这类机器人模型公司。跟我们的关系:它就是中文媒体问"谁会成为具身的 Scale AI"里那个 Scale AI 本尊——我们数据引擎设计的国际对标原型,也是验证"数据即服务"这条商业模式能不能跑通的头号样本。**身份解析:**本页只讲 Scale AI, Inc.(美国,scale.com)旗下机器人数据业务;与加拿大魁北克的政府背景非营利机构 "Scale AI"(scaleai.ca)无任何关系,勿混淆。

## 1. 愿景与论纲 — 逐字引语

- **Ben Levin**(时任 Physical AI 总经理,2025-09-24 业务发布博文署名作者):*"Unlike text or images, robotic manipulation data can't be scraped from the web."*(不像文本和图像,机器人操作数据没法从网上爬。)他并非只讲数量:博文明言"光有原始轨迹不够"(*"Raw trajectories alone aren't sufficient"*),要在动作数据上叠加语义层,编码**意图(intent)、任务结构(task structure)、失败模式(failure modes)**。
- 发布博文三支柱(原文小标题):**Abundant(量足)、Diverse(多样)、Enriched(语义增强)**——即"采得多、场景杂、标得深"。(产品页现行文案已改用 Global/Scalable/Diverse 口径,2026-07 核验。)
- **Jason Droege**(CEO,2026 年展望博文):*"…delivering more than 150,000 hours of data and onboarding 10 new robotics customers."*(2025 年交付超 15 万小时数据、新增 10 个机器人客户。)注意:机器人只是他列举的几条增长线之一,公司主叙事仍是面向企业/政府的"可靠 AI"。
- **James Davidson**(Teradyne Robotics 首席 AI 官,2026-03 合作声明):*"the future of robotics AI will be shaped as much by data quality as by model architecture."*(机器人 AI 的未来,数据质量与模型架构同等重要。)

**批判读法:**Scale 没有任何一份由 CEO 署名的"机器人宣言"——愿景话语全部出自事业部总经理和产品页,这本身就说明机器人业务在公司优先级栈里是"增长项"而非旗舰叙事。**这对我们意味着什么:**对标 Scale 时要对标它的事业部打法,而不是把整个 290 亿美元估值当成"机器人数据市场"的证据。

## 2. 创始人与团队

- **Alexandr Wang** — Scale 创始人,2016 年从 MIT 辍学与 Lucy Guo 创办(YC S16)。2025 年 6 月 Meta 以 143 亿美元买下 49% 无投票权股份后,他离职去领导 Meta Superintelligence Labs。重要性:公司灵魂人物已离场,现在的 Scale 是"后 Wang 时代"。
- **Jason Droege** — 现任 CEO(2025-06 起先任临时 CEO,2026 年多个来源已直称 CEO)。背景白话:Uber Eats 的创始操盘人,此前是 Scale 首席战略官。重要性:他正把公司从"七成标注、三成应用"翻转为应用优先——机器人数据业务的资源分配取决于他的棋盘。
- **Ben Levin** — 机器人业务的实际缔造者,Physical AI 总经理(2025-09 发布博文署名 GM,2026-03 UR 合作博文仍列为合著者)。背景白话(据其 LinkedIn 自述,均 unverified 无第二来源):Pomona 数学本科 → BCG 咨询 → Mapbox 地图数据 GM → Scale 高级产品经理 → **在 Hugging Face 参与建设并规模化 LeRobot(开源机器人数据/工具生态;注意 LeRobot 项目 2024 年由 HF 的 Rémi Cadène 团队创建,"缔造者"应理解为核心建设者而非唯一创始人)**。重要性有两层:其一,Scale 机器人业务的技术血统直接来自开源界最大的机器人数据项目;其二,**本次调研最重磅发现:其 LinkedIn 现任头衔为 NVIDIA "Director, Robotics & Physical AI Data"(2026-07 核验)**——Scale 机器人业务的创始负责人已在英伟达,且未找到任何继任者公告。(unverified:精确离职日期、GM 头衔起始时间;另有多处综述称其"离开 Hugging Face 加入 NVIDIA",Scale→HF→NVIDIA 还是 HF→Scale→NVIDIA 的履历顺序未能钉死)
- **Brad Porter** — 不是团队成员但必须列:Scale 2020–2022 年的 CTO(此前在亚马逊管 50 万台物流机器人),离职创办 Cobot——而 Cobot 现在是 Scale 机器人业务页面上的署名客户。重要性:所谓客户背书里有一层"自己人"关系。
- 团队规模侧写(来自 2026-07 在招 JD):机器人部门自称"历史性高速增长",目标"数千万美元级新增收入",走智能眼镜/传感器的第一视角(egocentric,戴在人身上以人眼视角采集)路线;Physical AI 技术负责人岗带 4–6 名研究员,方向是 VLA(视觉-语言-动作模型)与世界模型,SF 底薪 24.9–31.1 万美元。

**这对我们意味着什么:**灵魂人物流失 + 无继任者,是 Scale 机器人业务组织脆弱性的直接证据;同时 NVIDIA 吸走此类人才,说明"机器人数据负责人"这个物种正在被平台巨头收编。

## 3. 产品全览与规划

| 产品 | 是什么(白话) | 格位(参照 [data-companies-compare](data-companies-compare.md) 家族分类) | 关键规格 | 价格 | 披露度 |
|---|---|---|---|---|---|
| Physical AI Data Engine | 总品牌:从采集到标注的一条龙数据服务 | 服务层,横跨 A/B | 累计 10 万+生产小时(2025-09),2025 全年交付 15 万+小时;自称日采 1000+ 小时 | 无公开价目;有聚合站称起步 20–30 万美元 (unverified,低置信) | 低 |
| Scale Harness | 自研"无机器人"手持/穿戴采集装置(人拿着干活,设备记录动作)——UMI 同类 | 家族 A(免真机采集) | BOM(物料清单)、传感器、动作标签怎么算出来的,全部未披露 | 未披露 | 极低 |
| Bespoke Collection Platforms | 按客户机器人本体定制的采集硬件,Scale 代运营 | 定制,A/B 皆可 | 无公开规格 | 未披露 | 极低 |
| Multi-Modal Grounding Annotations | 标注层:给动作数据加"目标/步骤/失败原因"语义标签,模型辅助人工 | 标注服务 | 无量化指标披露 | 未披露 | 低 |
| UR AI Trainer(与 Universal Robots 合作) | 装在优傲协作臂上的"师徒采集套件":人拖动 2 台 UR3e 领导臂,2 台 UR7e 跟随臂实时复现,全程录数据 | 家族 B/C(真机测量,零本体差) | Jetson Orin 随机算力(on-robot,装在采集单元上)+ Orbbec 3D 相机,工作站结构与 Vention 联合开发;动作+力+视觉同步流,打包成 VLA 训练集;瞄准 UR 全球 10 万+ 存量装机 | 未披露(查遍 8+ 家行业媒体无价) | 中(硬件规格因用现成 UR 平台而"漏出") |

采集环境三条线:集中式"数据工厂"(旧金山实验室,地址/面积/机器人数量全部未披露)、分布式居家采集、工业现场(UR 线)。**已宣布路线图:**2026 年内与 UR 联合发布一个"UR 机器人上采集的大规模工业数据集"(开源还是商业授权未说明);NVIDIA Physical AI Data Factory Blueprint(GTC 2026 发布的合成数据参考架构)一侧的对接方是 UR 母公司 Teradyne Robotics——NVIDIA 官方新闻稿列名的是 Teradyne,**不是 Scale**,Scale 与 Blueprint 的关系只是经由这条合作链间接搭上。**这对我们意味着什么:**Scale 的产品矩阵与我们 [data-engine-v2](data-engine-v2.md) 的"A 族铺量 + B 族保真"双轨几乎同构,但它把 B 族保真外包给了 UR 的现成计量体系——借船出海,不自己造船。

## 4. 技术栈方案

- **标签路径**(为什么重要:动作标签是"真值"还是"算出来的",直接决定数据保真度,是我们 [data-engine-first-principles](data-engine-first-principles.md) 的第一性问题):Scale Harness 的动作标签是 SLAM/视觉里程计恢复(算出来的)还是编码器测量(读出来的)?**零披露**,连误差/漂移数字都没有——完美复现了本 wiki 在对比页发现的行业"计量格全空"模式。唯一例外是 UR AI Trainer:标签直接来自 UR 自家关节与力传感器,属实测、零本体差——但那份保真是 UR 的功劳,不是 Scale 方法论的披露。
- **同步**(为什么重要:多传感器时间戳对不齐,力和图像就"对不上口型",数据白采):UR 官方称动作/力/视觉"同步",但无延迟/抖动指标;Harness 完全未提。
- **传感器/格式**(为什么重要:格式决定数据能不能跨模型复用):Harness 传感器 BOM 未披露;数据格式(RLDS/LeRobot/Zarr 之类)任何 Scale 材料中均未出现——讽刺的是其 GM 正是 LeRobot 缔造者。
- **开源足迹**(为什么重要:开源是技术实力的可验证信号):GitHub org(scaleapi)活跃但**机器人相关仓库为零**,全是 LLM/agent 工具;Hugging Face org 有 5 模型 32 数据集,**全部是 LLM 安全/代码基准,机器人为零**;机器人方向 arXiv 论文为零;USPTO/Google Patents 机器人数据采集专利为零。

**批判读法:**Scale 机器人业务的技术透明度接近 Generalist 的全黑箱,而非 UMI 的全开放;它的可信度目前完全靠客户名单背书,而非可复核的技术披露。**这对我们意味着什么:**行业标杆尚且不敢/不愿披露计量指标,我们坚持在设计文档里写明标签路径与误差预算,本身就是差异化。

## 5. GTM 与资金

**真付费客户(Scale 官方页面署名确认):**
- **Physical Intelligence** — 署名数据供应关系(与本 wiki [company-pi](company-pi.md) 交叉印证)。
- **Generalist AI** — CEO Pete Florence 逐字背书:*"Scale has been a trusted partner in making abundant, high-quality, custom data."* **注意:这修正了我们 [case-generalist](case-generalist.md) 里"Generalist 数据链全自研闭环"的旧判断——它也外购 Scale 数据。**
- **Cobot** — CEO Brad Porter 背书,但他是 Scale 前 CTO(见 §2),客户与"自己人"身份重叠,背书含金量需打折。
- **Dyna** — 仅出现在 Scale 自家页面第四位;疑为 Dyna Robotics(2025-09 融 1.2 亿美元),但**无任何第二来源确认合作** (unverified)。

**仪式性/渠道动作:**UR/Teradyne 合作(2026-03,NVIDIA GTC 发布)目前是发布会+联合数据集承诺,尚无公开付费出货证据——是渠道杠杆(借 UR 10 万台存量装机做采集网络),与觅蜂的"设备上架"、鹿明借 UR 渠道的思路同构。定价全线企业定制、无价目表,入口是一个邮箱(physical-ai@scale.com)。

**融资全史(公司整体,非机器人单列):**

| 轮次 | 时间 | 金额 | 估值 | 领投 |
|---|---|---|---|---|
| 种子(YC) | 2016 | $12 万 | — | YC |
| — | 2019-08 | $1 亿 | >$10 亿 | Founders Fund |
| E 轮 | 2021-04 | $3.25 亿 | $73 亿 | Dragoneer/Greenoaks/Tiger |
| F 轮 | 2024-05 | $10 亿 | $138 亿 | Accel 领投;Amazon、Meta、NVIDIA 等参投 |
| Meta 入股 | 2025-06 | **$143 亿购 49% 无投票权股** | 隐含 ~$292 亿 | Meta 独家 |

(维基百科单处出现 $148 亿为孤例,主流一手来源均为 $143 亿。)关键结构性事实:Meta 另承诺**每年至少 4.5 亿美元、为期 5 年**的商业合同(以"不超过 Meta 年度 AI 开支一半"为上限,Forbes 报道口径)——相当于 Scale 2025 年 ~10 亿美元收入的约一半,即 Scale 的增长故事有一半是 Meta 合同撑起来的。副作用:交易后 OpenAI 出走,Google 暂停数月后已恢复合作,xAI 亦曾缩减(Forbes 2026-05;此点更新了 [data-foundry](data-foundry.md) 的旧表述)。2025 年收入略低于 10 亿美元(上年 8.7 亿);应用业务年化收入 2025 年底约 2 亿美元,Droege 称 2026 年应用与国际业务目标各自翻倍(未给全公司营收数字目标)。**机器人业务的收入、毛利、人数从未单独披露。**社区声量:Reddit/HN/X 上关于其机器人数据质量、价格、Harness 硬件的讨论为**零**——与 Generalist 一样,全部可见度都是媒体驱动而非用户口碑驱动。**这对我们意味着什么:**"具身 Scale AI"这个原型本身尚未证明机器人数据是一门可单独核算的生意;引用它做融资叙事时,要预备投资人追问"Scale 自己都不敢拆机器人报表"。

## 6. 没搞清楚的

1. **Levin 的继任者** — 查了 Scale 招聘页、LinkedIn、发布稿;无公告。可能因离职太新、公司刻意低调。
2. **Scale Harness 的 BOM/传感器/标签算法/误差指标** — 查了产品页、发布博文、JD、arXiv、两大专利库;零披露。原因大概率是商业保密(数据公司的方法论即护城河),而非没有。
3. **UR AI Trainer 价格** — 查了 UR 产品页、Scale 博客、8+ 家 GTC 报道;无价。渠道型硬件常按项目报价,可能永远不公开。
4. **机器人业务单列收入/人数** — 查了 Forbes 深稿、Droege 展望文、JD(收入数字被打码为 $XXM+);并入"数据业务"合并披露,拆不出来。
5. **"Dyna" 合作实据** — 查了 Dyna 自家新闻、Salesforce Ventures 组合页、行业报道;仅 Scale 单方列名。可能是早期未公告合同。
6. **SF 实验室地址/规模** — 本轮未做物业/许可证核查(可仿 AgiBot 临港那次的实地核验思路做后续)。
7. **2026 联合数据集开源与否** — 双方新闻稿均未说明。

## 7. 与我们设计的对撞要点

1. **双轨同构,保真外包:**Scale 的 Harness(A 族)+ UR 真机(B/C 族)组合,与 [data-engine-v2](data-engine-v2.md) 的双轨结论同构——但它的 B 族保真完全寄生于 UR 的计量体系。印证我们"B 族不必自研本体、优先借现成工业臂计量"的判断,同时警示:借船者拿不到船的图纸。
2. **计量披露全空,再次验证第一性缺口:**[data-engine-first-principles](data-engine-first-principles.md) 的核心论断——行业普遍不披露标签误差预算——在最大玩家身上再次成立。我们把误差预算写进规格书这条差异化路线,对撞后依然站得住。
3. **语义增强层是 Scale 的真差异点:**"intent / task structure / failure modes"(意图/任务结构/失败模式)三层语义标注,恰是我们 v2 设计里标注深度维度的现成命名法,可直接借用其框架反推我们的标注 schema。
4. **渠道杠杆先例:**UR 存量 10 万台 = Scale 的采集网络,这为我们的"借模组厂/渠道商存量设备铺采集网"(参见 Quectel 楔子思路)提供了国际先例与话术弹药。
5. **人才即漏洞:**LeRobot 缔造者被 Scale 挖来、又被 NVIDIA 挖走——机器人数据组织的核心资产是极少数"采集方法论"人才;我们的引擎设计必须把方法论文档化,不能寄存在个人脑子里。

## 8. 观察哨

- **Levin 继任者公告**(或 Physical AI 部门重组信号)——组织健康度的第一指标。
- **2026 年内 Scale×UR 联合工业数据集**:开源与否、格式、规模、许可条款——直接标定行业数据定价锚。
- Droege 下一次财报级披露里机器人是否首次单列数字。
- Dyna 合作是否获得第二来源确认。
- NVIDIA(Levin 新东家)是否推出与 Scale 竞争的第一方数据服务——若成真,Scale 经由 Teradyne/UR 挂上 NVIDIA 生态的路线将变成与房东竞争。

## Sources

- https://scale.com/blog/physical-ai — 2025-09-24 业务发布博文,Levin 署名:Abundant/Diverse/Enriched 三支柱小标题、"can't be scraped from the web" 引语、10 万+生产小时、physical-ai@scale.com(2026-07-12 复核)
- https://scale.com/physical-ai — 产品页:Harness、客户名单(PI/Generalist/Cobot/Dyna)、Florence/Porter 引语、日采 1000+ 小时(2026-07-12 复核)
- https://scale.com/blog/scale-ai-universal-robots-physical-ai — 2026-03-16 UR 合作,Davidson 引语、10 万台装机、2026 数据集承诺(2026-07-12 复核)
- https://www.universal-robots.com/news-and-media/news-center/universal-robots-scale-ai-launch-imitation-learning-system-accelerate-ai-training-lab-to-factory/ 及 PRNewswire 同稿(2026-03)— UR AI Trainer 配置:2×UR3e 领导臂 / 2×UR7e 跟随臂、Jetson Orin、Orbbec、Vention 工作站(2026-07-12 复核)
- https://scale.com/blog/scales-next-era-building-for-2026 — Droege 展望:15 万小时、10 新客户、10 亿美元新签(引语 2026-07-12 逐字复核)
- https://scale.com/blog/scale-ai-announces-next-phase-of-company-evolution — Meta 143 亿美元入股、Wang 离任官方口径
- https://www.forbes.com/sites/richardnieva/2026/05/14/scale-meta-deal/ — 财务深稿:2025 收入略低于 10 亿(上年 8.7 亿)、Meta 年付至少 4.5 亿×5 年、OpenAI 走/Google 回、70/30 业务结构翻转、应用 ARR 2 亿
- https://techcrunch.com/2024/05/21/data-labeling-startup-scale-ai-raises-1b-as-valuation-doubles-to-13-8b/ 、https://www.cnbc.com/2025/06/12/scale-ai-founder-wang-announces-exit-for-meta-part-of-14-billion-deal.html — F 轮(Accel 领投)与 Meta 交易金额交叉验证
- https://nvidianews.nvidia.com/news/nvidia-announces-open-physical-ai-data-factory-blueprint-to-accelerate-robotics-vision-ai-agents-and-autonomous-vehicle-development — Blueprint 列名 Teradyne Robotics 而非 Scale(2026-07-12 核验)
- https://www.linkedin.com/in/benjaminlevin/ — 现任头衔 "Director, Robotics & Physical AI Data @ Nvidia"(2026-07-12 搜索结果标题核验);履历自述(LeRobot、Mapbox、BCG)(unverified 精确日期与顺序)
- scale.com/careers 在招 JD ×2(2026-07-12 在线核验)— 机器人部门规模与方向侧写
- github.com/scaleapi 与 huggingface.co/ScaleAI — 2026-07-12 直接核验:机器人开源足迹为零
- 36氪/甲子光年(2025-06-11)— 中文媒体"谁会成为具身的 Scale AI"框架
- scaleai.ca "About us" — 加拿大同名机构无关性确认
