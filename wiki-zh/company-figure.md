---
title: "公司深度剖析:Figure AI"
slug: company-figure
updated: 2026-07-04
confidence: verified
lang: zh
source: ../wiki/company-figure.md
---
> Figure AI(2022 年由 Brett Adcock 创立,总部位于加州圣何塞)是全球估值最高的纯人形机器人公司——2025 年 9 月完成超 10 亿美元的 C 轮融资,投后估值高达 **390 亿美元**,18 个月内估值跳涨 15 倍——也是美国"垂直整合"路线的旗舰代表:自研机器人(Figure 03)、自研视觉-语言-动作模型(VLA)技术栈(Helix → Helix 02,2025 年 2 月弃用 OpenAI 后打造)、自建工厂(BotQ,产能从每天 1 台提升到约每小时 1 台,截至 2026 年 4 月已生产超 350 台 Figure 03)。其部署验证案例包括宝马 Spartanburg 工厂(Figure 02 支持了 3 万余辆 X3 的生产;Figure 03 目前负责排序物流)以及与 Catalyst Brands(JCPenney 等,2026 年 5 月)达成的零售物流协议。质疑方的论据同样具体:未披露任何营收,CEO 声明与宝马确认事实之间存在有据可查的差距(《财富》杂志,2025 年 4 月),一起安全问题吹哨人诉讼(2025 年 11 月),以及所谓交付数字大多是自我报告的内部机队数量,而非客户购买的实际单位。相关背景:[人形机器人](humanoid-robots.md)、[VLA 模型](vla-models.md)、[美国格局](landscape-usa.md)、[投资](investment.md)。

## 创始团队

- **2022 年创立**,创始人为 **Brett Adcock**——连续创业者(Vettery,以约 1 亿美元卖给 Adecco;Archer Aviation,通过 SPAC 上市)。Adcock 最初自筹资金创办 Figure,并在 A 轮中投入了 **2000 万美元个人资本**(据 Wikipedia 的资料来源);据称他仍持有约 50% 的股权(未证实)。
- 早期团队从 **波士顿动力、特斯拉、苹果、谷歌 DeepMind** 招募——最初刻意偏重硬件,与 OpenAI 分手后转向偏重 AI。
- **Corey Lynch**(前谷歌 Brain 研究员,专攻语言条件模仿学习)于 2023 年 6 月加入,以 AI 总监身份主导 Helix 项目——是塑造美国该领域的更广泛"谷歌机器人系"人才外溢的一部分(参见[关键人物](key-people.md))。
- 相对于估值,员工规模一直较小:早期报道约 180 人(Wikipedia),到 2025 年底增长到约 400 人,据 Adcock 发布的"员工数 vs 机器人数"图表,2026 年约为 650-660 人。Adcock 发帖称"**Figure 历史上首次出现机器人数量超过员工数量**"(X,2026 年 6 月 20 日——已确认为原始帖子);该图表显示机器人机队在 2026 年第二季度超过员工数量,数字大致为**700-750 台机器人 对 约 650 名员工**(均为公司自报数据,无第三方审计)。一个被广泛转载的"约 200-250 名员工"数字来源于单一聚合信息源,与图表显示的 2026 年年中交叉点不符(截至 2026 年 4 月已有超过 350 台机器人)——应视为错误信息。
- Adcock 还创办了 **Hark**,一个独立的个人 AI 硬件/模型实验室,以他个人的 1 亿美元资本起步(The Information,2026 年 3 月);Hark 完成了一轮 **7 亿美元 A 轮融资,投后估值 60 亿美元**,由 Parkway Venture Capital 领投——与 Figure A 轮/C 轮的同一领投方(TechCrunch,2026 年 5 月 21 日)。
- 使命定位("总体规划"):应对劳动力短缺的通用人形机器人 → 优先商业物流/制造业,其次进入家庭场景。

## 融资历史(截至 2026-07)

| 轮次 | 日期 | 金额 | 投后估值 | 领投方/主要投资者 |
|---|---|---|---|---|
| 自筹 | 2022 | Adcock 个人出资 | — | — |
| A 轮 | 2023-05 | 7000 万美元 | 未披露 | Parkway Venture Capital;含 Adcock 个人投入的 2000 万美元 |
| B 轮 | 2024-02-29 | **6.75 亿美元** | **26 亿美元** | 微软、OpenAI Startup Fund、英伟达、杰夫·贝索斯(通过 Bezos Expeditions)、Parkway、英特尔资本、Align Ventures、ARK Invest(据官方新闻稿;部分报道补充提及 Amazon Industrial Innovation Fund,但官方新闻稿未提及此投资者) |
| C 轮 | 2025-09-16 | **超 10 亿美元**("超过 10 亿美元",具体数额未披露) | **390 亿美元** | Parkway Venture Capital(领投);Brookfield、英伟达、麦格理资本、英特尔资本、LG Technology Ventures、高通风投、Salesforce、T-Mobile Ventures |

- 累计融资 **约 19 亿美元**(截至 2026 年 1 月)。据报道 C 轮融资期间曾以"15 亿美元、估值 395 亿美元"的条件进行推介(TechCrunch,2025 年 4 月);实际完成的轮次公布为"超 10 亿美元、投后估值 390 亿美元"——应以官方数字为准。
- 从 26 亿美元到 390 亿美元的估值跳涨(18 个月内 15 倍),使 Figure 成为全球估值最高的约 20 家初创公司之一,且**未披露任何营收**——参见[投资](investment.md)了解估值与营收之间的鸿沟(对比[宇树科技](company-unitree.md):约 60 亿美元的 IPO 估值*配合*约 2.35 亿美元的 2025 年营收)。
- 与 C 轮同步签署:与 **Brookfield** 达成数据合作("Project Go-Big"),开放约 10 万套住宅单元用于第一人称/人形机器人预训练数据采集——参见[数据](data.md)。
- 融资期间,Figure 向**二级市场经纪商发送了停止侵权函**,阻止其股份交易(TechCrunch,2025 年 4 月 29 日)——这一举动被不同解读为标准的股权登记簿管理措施,或估值控制手段。

## Helix:自研模型的押注

### 架构

- **Helix**(2025 年 2 月 20 日发布):面向人形机器人上半身全身控制的双系统视觉-语言-动作模型(VLA)。**System 2** 是一个基于开源模型的 70 亿参数视觉语言模型(VLM),以 7-9 Hz 运行,负责场景/语言理解,输出一个潜在目标向量供 **System 1** 使用——后者是一个 8000 万参数的视觉运动 Transformer,以 **200 Hz** 运行,在 35 自由度动作空间(手腕、单指、躯干、头部视线)上输出连续指令。训练数据约为 500 小时遥操作(teleoperation)数据;完全在双嵌入式 GPU 上运行;一套权重曾同时驱动两台机器人协作(公司宣称的多项"首创":首个全上半身人形 VLA、首个多机器人 VLA、首个完全端侧运行的商用 VLA)。权重闭源。
- **Helix 02**(2026 年 1 月 27 日):新增 **System 0**,一个 1000 万参数的全身反射/平衡控制器,以 **1 kHz** 运行,层级位于 S1/S2 之下,训练数据涵盖 20 万余个并行模拟环境中的 1000 多小时人类动作;集成了 Figure 03 的触觉指尖(灵敏度约 3 克)和掌心摄像头。标志性演示:约 4 分钟、61 个动作的洗碗机装卸循环,全程无需人工重置——公司自行报告,无第三方基准测试。Adcock 将 Helix 02 定位为"软件 2.0":Figure 称已删除最后约 109,504 行手工编写的 C++ 机器人控制代码(据访谈中的公司说法)。
- 公司声称 Helix 02 机器人已完成完整的 8 小时自主物流班次(2026 年 5 月,公司口径,未证实)。
- **约 200 小时的直播马拉松测试(2026 年 5 月)**:自动化行业分析师 Scott Walter 公开发起的一项 8 小时耐力挑战,最终演变为一次持续 200 小时的连续包裹分拣测试(约 2026 年 5 月 13 日开始,2026 年 5 月 22 日完成;通过 YouTube "F.03 Livestream" 系列公开直播,共 1-9 天),地点在 Figure 总部(据 Sherwood 报道为圣何塞;部分报道称为桑尼维尔)——一支由运行 Helix 02 的 Figure 03 组成的小型团队(三到四台,不同报道数字不一;通过更换电池轮换运行;被观众昵称为 Rose/Bob/Frank/Jim 等)分拣了**约 249,560 件包裹,零起硬件故障或系统级崩溃报告**(承认存在软件层面的偶发问题,如包裹掉落)。这是迄今为止 Figure 最具外部可观察性的可靠性数据点,尽管吞吐量/故障率指标仍为自我报告(截至 2026-07)。
- 完整的技术脉络参见[VLA 模型](vla-models.md);Helix 在物流场景中的规模化指标(包裹处理周期接近人类速度)由公司自行公布。

### 与竞品 VLA 的对比(截至 2026-07)

| 技术栈 | 所属公司 | 设计 | 具身策略 | 权重 |
|---|---|---|---|---|
| Helix / Helix 02 | Figure | 三层架构:S2 70 亿参数 VLM(7-9 Hz)→ S1 8000 万参数策略网络(200 Hz)→ S0 1000 万参数反射控制器(1 kHz);完全端侧运行 | **单一具身**(仅限 Figure 自家机器人);大量基于自有机队和遥操作数据训练 | 闭源 |
| π0 / π0.5 / π*0.6 / π0.7 | Physical Intelligence | 约 30 亿参数 VLM + 流匹配动作专家模块(约 50 Hz);RECAP 强化学习来自部署数据 | 跨具身(机械臂、移动平台、人形机器人) | π0/π0.5 开源 |
| GR00T N1-N2 | 英伟达 | 双系统架构(类似 Helix);N2 新增世界-动作建模 | 跨具身生态玩法,覆盖合作伙伴多种机器人 | 开源 |
| Gemini Robotics 1.5 | 谷歌 DeepMind | 具身推理(ER)推理器 + VLA;含端侧变体 | 跨具身;已部署于 Atlas、Apollo | 闭源 |
- Figure 的差异化优势:垂直整合程度最深(模型+硬件+工厂+机队数据飞轮)、控制速率层级最高(1 kHz 反射层)、全部端侧运行。其风险在于:单一具身的闭源技术栈意味着没有生态系统营收,也没有外部验证;所有核心能力均为公司自行报告。

### OpenAI:合作(2024)→ 分手(2025)

- **2024-02-29**:与 B 轮融资同步签署合作协议(OpenAI Startup Fund 参与投资)——OpenAI 为 Figure 机器人开发专用 AI 模型。2024 年 3 月 13 日 Figure 01 的语音对话演示(由 GPT 提供支持)走红网络,成为该合作关系的公众代表形象。
- **2025-02-04**:Adcock 宣布分手,称在完全端到端的自研机器人 AI 上取得了"重大突破"(16 天后揭晓为 Helix)。给出的理由是:具身 AI 必须垂直整合("我们不能像外包硬件一样外包 AI");大语言模型"越来越聪明,但也越来越商品化"。Adcock 后来表示该合作带来的价值"少得可怜",而 OpenAI 释放出将自行进军人形机器人的信号,促使他决定终止合作("我当时就想,'到此为止了'")。
- 后续发展:OpenAI 在 2025-26 年组建了自己的机器人部门,同时仍是 Physical Intelligence 和 1X 的投资者——参见[美国格局](landscape-usa.md)。

## Figure 03 硬件(2025 年 10 月 9 日发布)

- 第三代机器人,专为 **BotQ 大规模量产**(以压铸/注塑工艺取代 CNC 加工)和**家庭场景**共同设计;荣获 TIME 2025 年度最佳发明。
- 据 Figure 官方规格页:**身高 5 英尺 8 英寸(约 1.73 米)、体重 61 公斤、有效载荷 20 公斤、续航 5 小时、行走速度 1.2 米/秒**;**比 Figure 02 轻 9%**(发布公告)。此前部分二手报道中约 1.68 米的数字并未得到 Figure 自家规格表的支持(2026 年 7 月 4 日已更正)。
- 通过脚部线圈实现 **2 千瓦无线感应充电**(自主对接);电池容量约 2.3 千瓦时(据报道);续航 5 小时(官方规格页)。
- 感知与操作能力:摄像头帧率提升 2 倍、延迟降低 75%、视野扩大 60%;每只手配备**掌心摄像头**;指尖触觉传感器可检测约 3 克的力度(参见[触觉与灵巧手](tactile-hands.md));执行器速度比 02 代快 2 倍;支持语音对语音的音频交互。
- 采用柔软可水洗的织物外罩——这在工业人形机器人中是一个较为罕见的居家安全性/美观性信号。
- 目前不对个人销售(截至 2026-07):已有商业部署,同时公司提出约 2 万美元的消费级价格目标(未证实),以及"2026 年底更广泛面向家庭场景"的公司目标。

## BotQ 制造体系

- **2025 年 3 月宣布**:专用人形机器人工厂;第一代产线设计产能**每年最高 1.2 万台**;四年目标为**10 万台**(公司目标)。垂直整合程度高:自研执行器、关键模块专用产线、跨越 150 多个联网工位的定制化生产执行软件。
- **产能爬坡(官方数据,2026-04-29)**:产量从**每天 1 台(2026 年 1 月)提升到约每小时 1 台**,不足 120 天内吞吐量提升了 24 倍(公司称);**已生产超过 350 台 Figure 03**;跨越 10 多种物料型号,累计生产执行器超 9000 个;总装下线一次通过率超过 80%;电池产线良率在超过 500 组电池包中达到 99.3%;每台机器人经历超过 50 次过程检验和超过 80 项总装下线功能测试。
- 需要注意的是:所有数字均为公司自行发布,而这超过 350 台机器人大部分被分配用于*内部*研发、Helix 数据采集和家庭任务开发,只有一部分投入商业部署——这更像是一支数据飞轮机队,而非销售业绩记录。
- 需要注意约每小时 1 台并不等同于全年 1.2 万台的持续产能(那需要接近 24 小时不间断运转);应将"每小时 1 台"视为已验证的峰值产线速率,而非持续速率。此前一份"约每 90 分钟 1 台"的报道(2026 年 4 月)与上述产能爬坡轨迹相符(未证实)。

## 宝马 Spartanburg 工厂——已确认信息 vs. 传闻声称

本维基中区分一手信源事实与聚合信息偏差的典型案例。

**宝马已确认(一手新闻稿):**
- **2024-01**:签署商业协议——宝马成为 Figure 的首个客户;地点为南卡罗来纳州 Spartanburg 工厂。
- **2026-02-27(宝马新闻稿——"欧洲物理 AI"/莱比锡相关发布)**:Figure 02 试点结果——在车身车间,周一至周五每天 10 小时轮班,持续约 10 个月(Figure 自称整体部署为 11 个月),**在约 1,250 个运行小时内(约 120 万个操作步)搬运了超过 9 万个零部件,支持了超过 3 万辆宝马 X3 的生产**。这些数字最初由 Figure 自行发布(2025-11-19),随后获得宝马确认;宝马 2026 年 6 月的新闻稿重申"十个月内生产超过 3 万辆 X3"。
- **2026-06-25(宝马新闻稿;Figure 自家发布于 2026-06-30)**:**Figure 03** 已部署于 52 号车间执行**排序物流**任务——将未分类的零部件从料箱中拣取,放入按顺序排列的运输小车中,以实现按序装配交付;由 Helix 02 协调手部/手臂/躯干/双足动作(包括拖拽带轮小车);这是宝马 iFACTORY 计划的一部分,相关研发工作在 Spartanburg 和 Figure 两地同步进行。
- **2025 年初宝马确认的规模**(据宝马发言人向《财富》杂志透露):**仅一台机器人**,在非生产时段工作至约 2025 年 3 月,随后在实际生产期间执行同样有限的任务——这一规模远比当时公开的宣传口径要保守得多。

**来自聚合信息源/未证实——未获一手确认前不应升级采信:**
- "宝马 Spartanburg 工厂约有 40 台 Figure 03"——源自单一聚合信息源(未证实)。
- 宝马以"每台机器人每小时约 25 美元"计费(据报道,未证实)。
- "Figure 扩展至宝马莱比锡工厂"——**与宝马自己的公告相矛盾**:宝马在德国的首个人形机器人试点(莱比锡,2026 年夏)使用的是 **Hexagon Robotics 的 AEON**,而非 Figure。参见[前沿动态](state-of-the-art.md)。

## 客户与应用领域(截至 2026-07)

| 客户/领域 | 状态 | 确认方 |
|---|---|---|
| 宝马(汽车制造) | Figure 02 试点已完成;Figure 03 排序物流已上线 | 宝马 + Figure 一手信源 |
| Catalyst Brands(零售物流:JCPenney、Aéropostale、Brooks Brothers) | 2026-05-26 签署商业协议;首个站点为内华达州里诺配送中心(Joey Pouch 分拣系统);Figure 与 Brookfield 投资组合企业之间的首次桥接合作 | 双方各自公告 |
| 未具名"商业客户" | Figure 称已于 2024-12 开始向商业客户交付 Figure 02;身份未披露 | 公司口径(未证实) |
| UPS(包裹物流) | 2025-04 有报道称正在洽谈;双方均未确认 | 二手报道(未证实) |
| 家庭/消费者场景 | Figure 02 自 2025 年起进行家庭 alpha 测试(提前 2 年实现,归功于 Helix);Figure 03 专为家庭场景设计;更广泛供货预计"2026 年底" | 公司声明;尚无已出货的家庭产品 |

## 交付记录 vs. 公开声称——质疑方的论据

- 在 390 亿美元估值下**未披露任何营收**;整个估值几乎完全建立在叙事和能力演示之上(参见[投资](investment.md))。
- **《财富》杂志调查(2025-04-06)**:发现宝马工厂实际只有一台机器人在非生产时段工作,而公开宣传口径却暗示已有一整支机队投入生产;Adcock 称此为"彻头彻尾的谎言",并威胁提起诽谤诉讼,但未见实际提起诉讼。在 2025 年 6 月的一次会议上,他跳过了现场演示环节,并回避了有关宝马合作的提问(TechCrunch)。
- **吹哨人诉讼(2025 年 11 月提起)**:前产品安全负责人 Robert Gruendel(2024 年 10 月入职)指控,他在警告 Figure 机器人可能施加"相当于 ISO 15066 疼痛阈值 20 倍"的力量——足以造成颅骨骨折——之后数日内被解雇;他还指控一台故障机器人曾在钢制冰箱门上留下划痕,并称向 C 轮投资者展示的安全路线图在融资完成后被降级("可被解读为欺诈")。Figure 方面表示他是因绩效问题被解雇,并称这些指控为"不实之词";此后 Figure 已**反诉 Gruendel**,指控他将公司文件保存至个人谷歌账户,违反商业机密法及公司政策(The Information 报道)。这可能是人形机器人行业首起安全类吹哨人案件——参见[安全与监管](safety-regulation.md)。
- **交付数字大多为自我报告且以内部为主**:生产超过 350 台不等于售出超过 350 台;目前公开确认的外部部署仅有宝马(小规模机队,具体数量未证实)以及刚刚起步的 Catalyst Brands。相比之下,Agility 已公布超过 65,000 小时的客户现场机队运行时长——Figure 目前最接近的对标是那次约 200 小时的总部内部直播分拣测试(2026 年 5 月),令人印象深刻,但终究是内部测试而非客户现场部署。
- **所有 Helix 里程碑均缺乏第三方基准测试**(61 个动作的洗碗机测试、8 小时班次、物流周期时间等)——看似合理但未经审计;参见[评测](evaluation.md)。
- **理想化时间表模式**:4 年内 10 万台机器人、2026 年底家庭场景供货、"2025 年家庭 alpha 测试"——相比特斯拉 Optimus,Figure 的实际交付记录更好,但激励结构导致的前瞻性夸大声明模式是相似的。
- 为多头论调作辩护:宝马*确实*独立确认了 02 代试点的结果,并*确实*扩展到了难度更高的 Figure 03 应用场景;BotQ 的良率/吞吐量细节对一家私营公司而言异常详尽;而 Brookfield→Catalyst 这一结构为 Figure 提供了一条专属的部署渠道。

## 来源

- https://www.prnewswire.com/news-releases/figure-raises-675m-at-2-6b-valuation-and-signs-collaboration-agreement-with-openai-302074897.html — B 轮 6.75 亿美元、估值 26 亿美元 + 与 OpenAI 的合作协议、投资者名单(官方新闻稿,2024-02-29)
- https://www.prnewswire.com/news-releases/figure-exceeds-1b-in-series-c-funding-at-39b-post-money-valuation-302556936.html — C 轮"超 10 亿美元",投后估值 390 亿美元(官方新闻稿,2025-09-16)
- https://www.figure.ai/news/series-c — C 轮投资者名单、资金用途、Brookfield 数据合作(官方)
- https://en.wikipedia.org/wiki/Figure_AI — 创立(2022)、总部、A 轮 7000 万美元含 Adcock 个人 2000 万美元、约 180 名员工、合作/争议时间线
- https://www.figure.ai/news/helix — Helix 架构:S2 70 亿参数@7-9 Hz、S1 8000 万参数@200 Hz、35 自由度、约 500 小时遥操作、声称的多项首创(官方,2025-02-20)
- https://www.figure.ai/news/helix-02 — Helix 02:System 0 1000 万参数@1 kHz、触觉/掌心摄像头集成、61 动作洗碗机演示(官方,2026-01-27)
- https://www.humanoidsdaily.com/news/the-end-of-c-brett-adcock-on-helix-02-and-figure-s-path-to-room-scale-autonomy — Adcock 访谈:删除约 10.9 万行 C++ 代码,"软件 2.0"定位
- https://www.figure.ai/news/introducing-figure-03 — Figure 03 规格:轻 9%、2 千瓦无线充电、3 克触觉、掌心摄像头、量产设计(官方,2025-10;未给出身高/体重)
- https://www.figure.ai/figure — Figure 03 官方规格页:5 英尺 8 英寸、61 公斤、20 公斤载荷、5 小时续航、1.2 米/秒(解决了 1.68 米 vs 1.73 米的分歧)
- https://www.figure.ai/news/botq — BotQ 公告:第一代产线年产 1.2 万台、四年 10 万台目标、垂直整合(官方,2025-03)
- https://www.figure.ai/news/ramping-figure-03-production — 超 350 台、每天 1 台→每小时 1 台(不足 120 天)、超 9000 个执行器、良率数据(官方,2026-04-29)
- https://www.press.bmwgroup.com/global/article/detail/T0458778EN/bmw-group-advances-the-use-of-physical-ai-in-production-with-figure-03-project-in-spartanburg?language=en — 宝马一手信源:52 号车间 Figure 03 排序物流,Figure 02 试点回顾(2026-06-25)
- https://www.figure.ai/news/f-03-at-bmw — Figure 自家关于 Figure 03 落地宝马的公告(官方,2026-06-30)
- https://www.figure.ai/news/production-at-bmw — Figure 02 → 超 3 万辆汽车、超 9 万个零部件、超 1250 小时、周一至周五每天 10 小时班次(官方,2025-11-19)
- https://www.press.bmwgroup.com/global/article/detail/T0455864EN/bmw-group-to-deploy-humanoid-robots-in-production-in-germany-for-the-first-time?language=en — 宝马一手信源(2026-02-27):确认 Figure 02 试点数据(超 9 万个零部件、约 1250 小时、超 3 万辆 X3、十个月周一至周五每天十小时轮班);宣布莱比锡试点采用 Hexagon AEON,而非 Figure
- https://www.therobotreport.com/bmw-group-deploys-figure-03-humanoid-after-tests-previous-version/ — 独立确认 Figure 03 在 Spartanburg 的应用范围、Helix 02 拖拽小车能力
- https://fortune.com/2025/04/06/figure-ai-bmw-humanoid-robot-partnership-details-reality-exaggeration/ — 《财富》杂志:宝马确认仅一台机器人、非生产时段工作(质疑方的关键论据)
- https://mikekalil.com/blog/figure-ai-vs-fortune/ — Adcock 回应"彻头彻尾的谎言"、诽谤威胁
- https://techcrunch.com/2025/04/29/figure-ai-sent-cease-and-desist-letters-to-secondary-markets-brokers/ — 停止侵权函;15 亿美元/395 亿美元融资相关报道
- https://techcrunch.com/2025/06/06/figure-ai-ceo-skips-live-demo-sidesteps-bmw-deal-questions-on-stage-at-tech-conference/ — Adcock 跳过现场演示、回避宝马合作相关提问
- https://techcrunch.com/2025/02/04/figure-drops-openai-in-favor-of-in-house-models/ — 与 OpenAI 分手公告及理由
- https://x.com/adcock_brett/status/1886860098980733197 — Adcock 宣布分手的原始帖子(一手信源,2025-02-04)
- https://www.aol.com/articles/figure-ceo-speaks-openai-split-163554400.html — Adcock 事后回顾:合作带来的价值"少得可怜",OpenAI 转向自研人形机器人
- https://www.figure.ai/news/figure-signs-agreement-with-catalyst-brands — Catalyst Brands 合作协议、内华达州里诺配送中心(官方,2026-05-26)
- https://corporate.jcpenney.com/2026/05/26/catalyst-brands-taps-figure-ai-for-humanoid-automation/ — 客户方确认;Joey Pouch 分拣、与 Brookfield 的关联
- https://www.cnbc.com/2025/11/21/figure-ai-sued.html — CNBC:Gruendel 诉讼(2025-11-21 提起)、ISO 15066 力量 20 倍、冰箱划痕事件、Figure 的"表现不佳"回应
- https://gizmodo.com/you-must-read-this-riveting-whistleblower-lawsuit-about-allegedly-dangerous-robots-2000688737 — Gruendel 吹哨人诉讼细节(2025-11)
- https://www.theinformation.com/briefings/figure-countersues-safety-whistleblower — Figure 反诉 Gruendel:关于文件保存至个人账户的商业机密指控
- https://roboticsandautomationnews.com/2025/11/26/former-figure-ai-engineer-at-claims-companys-humanoid-robots-powerful-enough-to-fracture-human-skull/96962/ — 诉讼细节:ISO 15066 力量、冰箱事故、安全路线图指控
- https://techcrunch.com/2025/02/27/figure-will-start-alpha-testing-its-humanoid-robot-in-the-home-in-2025/ — 家庭 alpha 测试提前,归功于 Helix
- https://www.ttnews.com/articles/ups-figure-ai-robots — UPS 与 Figure 的洽谈(2025-04,未确认)
- https://www.therobotreport.com/brookfield-partners-figure-ai-develop-humanoid-pre-training-dataset/ — Brookfield 预训练数据合作
- https://x.com/adcock_brett/status/2068040783295627609 — Adcock 帖子(一手信源,2026-06-20):"Figure 历史上首次机器人数量超过员工数量" + 员工数 vs 机器人数图表
- https://robohorizon.com/en-us/news/2026/06/figure-ceo-the-robots-have-officially-outnumbered-the-humans/ — 图表解读:2026 年第二季度机器人数超 700,员工数约 650
- https://newskarnataka.com/technology/robots-now-outnumber-humans-at-figure-ai-says-ceo/21062026/ — 独立图表解读:2026 年第二季度约 740 台机器人,员工约 650-660 人,2025 年底员工约 400 人
- https://explainx.ai/blog/figure-ai-robots-outnumber-humans-milestone-2026 — 聚合信息源;其"机队超 750 台 vs 员工约 200-250 人"的表述与 Adcock 自己的图表(约 650 名员工)矛盾——不应采用
- https://www.techtimes.com/articles/316632/20260514/figure-ais-helix-02-robots-complete-full-8-hour-autonomous-shifts-humanoid-race-intensifies.htm — 8 小时自主班次声称(公司信源,未证实)
- https://sherwood.news/tech/figures-robots-just-sorted-packages-for-200-hours-straight/ — 约 200 小时直播分拣测试,约 249,560 件包裹(2026-05)
- https://interestingengineering.com/ai-robotics/figure-03-humanoid-robot-200-hour-shift — 零故障声称;Scott Walter 的 8 小时挑战起源;三台机器人(Bob/Jim/Rose);称地点为桑尼维尔总部(与 Sherwood 所称的圣何塞矛盾)
- https://www.humanoidsdaily.com/news/figure-ai-pops-champagne-as-autonomous-marathon-crosses-200-hours-without-hardware-failure — 测试于 2026-05-22 完成;机队轮换/更换电池;在承认零硬件故障声称的同时也承认存在软件层面问题
- https://www.technology.org/2026/05/20/figure-ai-humanoid-robots-livestream-package-sorting/ — 直播于 2026-05-13 开始;观众为机器人命名(Bob/Frank/Gary/Rose/Jim);10 小时人机对抗赛(实习生以 12,924 比 12,732 获胜)
- https://www.youtube.com/@figureai — "F.03 Livestream" 逐日视频系列(直播原始记录)
- https://techcrunch.com/2026/05/21/hark-raises-700m-series-a-for-its-secretive-universal-ai-interface/ — Hark(Adcock 的独立 AI 实验室):7 亿美元 A 轮融资,估值 60 亿美元,Parkway 领投
