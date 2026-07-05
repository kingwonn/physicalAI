---
title: "公司深度剖析：Boston Dynamics"
slug: company-bostondynamics
updated: 2026-07-05
confidence: verified
lang: zh
source: ../wiki/company-bostondynamics.md
---
> Boston Dynamics(1992年由Marc Raibert创立,脱胎于MIT Leg Lab,总部位于马萨诸塞州Waltham,约1,000名员工)是腿式机器人领域历史最悠久的品牌,自2026年6月起成为Hyundai Motor Group全资子公司——Hyundai以3.25亿美元收购了SoftBank剩余的9.65%股份,此前已在2020–21年间以约8.8亿美元收购80%股份。其2026年的故事是从三十年的研究展演转向量产:电动版Atlas量产机型于2026年1月5日在CES首发(56个自由度、2.3米可及范围、50公斤举重),2026年整个产能全部承诺给Hyundai的Robotics Metaplant Application Center和Google DeepMind,一座目标2028年建成、年产3万台的工厂正在推进,Hyundai计划在其自有美国工厂部署超过25,000台Atlas。其技术路线颇为独特:硬件方面拥有世界一流的基于模型的控制(model-based control)传承,而"大脑"则外包给合作伙伴(RAI Institute负责强化学习、Toyota Research Institute负责大型行为模型(LBM)、Google DeepMind负责Gemini Robotics),而非自研VLA(视觉-语言-动作模型)。与此同时,Spot(约7.5万美元的四足机器人,已部署3,000+台)和Stretch(与DHL签订1,000+台增购谅解备忘录)才是真正带来营收的业务——但2025财年营收仅约1,500亿韩元(约1.1亿美元),净亏损约5,280亿韩元(约3.85亿美元),由Hyundai的股权融资支撑。相关背景参见:[人形机器人](humanoid-robots.md)、[运动控制](locomotion.md)、[美国格局](landscape-usa.md)、[关键人物](key-people.md)。

## 公司概览(截至2026-07)

| 字段 | 值 |
|---|---|
| 成立 | 1992年,由**Marc Raibert**创立(MIT/CMU Leg Lab衍生) |
| 总部 | 马萨诸塞州Waltham;约1,000名员工(Wikipedia,未注明日期,近期数据) |
| 股权 | **Hyundai Motor Group 100%**持股(SoftBank剩余9.65%股份以**3.25亿美元**收购,集团批准据报道发生于2026-06-22);2020–21年首次入股:以约8.8亿美元收购80%,估值11亿美元,董事长**郑义宣(Chung Eui-sun)个人据报道持有买方约20%**份额 |
| 管理层 | 临时CEO **Amanda McMaster**(同时兼任CFO),自2026-02-27起;Robert Playter(2019/2020–2026年任CEO,30年老将)已退休;永久CEO人选仍在遴选中 |
| 产品 | **Spot**(四足机器人,2020年6月起商用,基础价74,500美元)、**Stretch**(货箱搬运物流机器人,2022年商用)、**Atlas**(人形机器人;量产版本于2026-01-05在CES发布)、**Orbit**(车队管理软件) |
| 2025财年财务 | 营收**1,501亿韩元(约1.1亿美元)**;**净亏损5,284亿韩元(约3.85亿美元)**(韩国财报报道) |
| 估值 | SoftBank退出隐含约34亿美元估值——但该看跌期权是按2021年设定的条款执行,并非市场估值;流传中的约30万亿韩元(约200亿美元)分析师数字(未证实) |
| 车队规模 | Spot已部署3,000+台(聚合器数据,未证实);Stretch:DHL谅解备忘录增购1,000+台;Atlas 2026年产能已全部认购(Hyundai RMAC + Google DeepMind) |
| 主要合作伙伴 | Hyundai Mobis(执行器)、Google DeepMind(基础模型)、RAI Institute(强化学习)、Toyota Research Institute(大型行为模型)、LG Energy Solution(电池)、NVIDIA(GR00T早期合作方,Thor芯片采用方) |

## 三十年谱系:Leg Lab → 液压 → 电动量产

| 时代 | 里程碑 |
|---|---|
| 1980年代 | Raibert在MIT/CMU的**Leg Lab**跳跃机器人通过简单控制启发式方法证明了动态平衡——公司的智识源头(参见[历史](history.md)) |
| 1992 | Boston Dynamics作为MIT衍生公司成立;数十年获DARPA/军方资助 |
| 2005–2013 | **BigDog**(2005年,DARPA驮兽机器人)让动态腿式运动进入公众视野;PETMAN;**液压版Atlas**(2013年)为DARPA机器人挑战赛打造 |
| 2013–2017 | 被**Google X**收购(2013年12月,价格未披露);Google机器人计划解散,公司被转售 |
| 2017–2020 | 被**SoftBank**收购(金额未披露);Spot实现产品化;Playter出任CEO |
| 2020–2021 | **Spot面向大众商用发售**(2020年6月,74,500美元);**Hyundai以约8.8亿美元收购80%股份**(2020年12月宣布,2021年6月完成);Stretch于2021年3月发布 |
| 2017–2021 | 病毒式传播的跑酷/后空翻液压版Atlas视频——离线优化的行为库+在线MPC,**并非强化学习**([运动控制](locomotion.md)) |
| 2024-04 | **液压版Atlas退役**;全电动Atlas发布 |
| 2025 | RAI Institute强化学习合作(2025-02);TRI**大型行为模型**驱动Atlas(2025-08) |
| 2026 | **量产版Atlas于CES发布(2026-01-05)**+Google DeepMind合作;获CNET"最佳机器人";Playter离职(2026-02);Hyundai实现100%持股(2026-06);1亿美元马萨诸塞州扩建(2026-06) |

## 技术路线与架构(技术路线)

**硬件优先,大脑靠合作**——与[Figure的](company-figure.md)垂直整合思路正好相反。

- **基于模型的控制传承**:2017–2021年Atlas跑酷时代运行于手工设计的轨迹优化+MPC行为库之上;Boston Dynamics是学习式运动控制领域最后的主要坚守者,直到约2025年才转型([运动控制](locomotion.md))。
- **借助RAI Institute的强化学习**(合作于2025-02宣布):Raibert创办的、由Hyundai支持的研究院(成立于2022年)为Atlas联合开发仿真到现实(sim-to-real)的运动控制与全身操作-运动融合策略;此前的联合工作包括Spot的RL Researcher Kit(RAI的开源流程使Spot速度达到5.2米/秒,约为原厂速度的3倍)。RAI的框架催生了Atlas在CES 2026上展示的体操动作和自然步态([关键人物](key-people.md))。
- **借助TRI的操作能力**:2025年8月的演示使用了Toyota Research Institute的**大型行为模型(Large Behavior Model)**——一个约4.5亿参数、语言条件化的扩散-Transformer策略,统一控制全身、双手与双脚([组织机构](organizations.md))。
- **借助Google DeepMind的认知能力**(于CES 2026-01-05宣布):**Gemini Robotics基础模型作为Atlas的高层"大脑"**——官方称这些模型"旨在让任何形态和尺寸的机器人都能感知、推理、使用工具并与人类互动";"具身心智(embodied mind)"是媒体的说法,并非合作双方自己的措辞。联合研究"将在两家公司同时开展",而DeepMind是2026年Atlas全部产能的两个接收方之一。车队学习理念(BD规格说明书原文):"一旦某台Atlas学会一项新技能,该任务便可轻松部署到你整个Atlas车队。"某种意义上的重聚——Google曾于2013–2017年拥有BD([VLA模型](vla-models.md))。
- **BD不做的事**:并未训练自己的前沿VLA。其技术栈是一个"合作伙伴三明治"——BD拥有全身控制、硬件以及Orbit车队层(MES/WMS集成;支持自主、遥操作、平板遥控三种模式);高层"大脑"则属于DeepMind。这以速度换取了依赖性(见下文SWOT分析)。
- **量产版Atlas硬件参数**(官方规格说明书,标注日期2025-12):**56个自由度**,全旋转关节,**2.3米可及范围**,**瞬时举重50公斤/持续举重30公斤**(单手20公斤),**身高1.9米/重90公斤**,电池续航4小时(高强度举重下2小时),配备**约3分钟的自主电池更换**,工作温度范围-20°C至40°C,**IP67**防护等级,触觉手指与手掌(媒体描述为四指手);双组可更换电池包(媒体报道)。这是第五代设计,与上一代相比实现了"复杂度降低近一个数量级"——"独特零件数量大大减少"(Alberto Rodriguez,Atlas机器人行为总监,Forbes 2026-07)。

## 愿景与赌注

- **Playter在CES 2026上表示**:*"这是我们迄今为止打造的最好的机器人。Atlas将彻底改变行业的运作方式,它标志着我们向一个自幼年起就梦寐以求的长期目标迈出的第一步——让实用机器人走进我们的家庭,帮助我们的生活更安全、更高效、更充实。"*(中文译文;英文原文见上)
- **Raibert的创始理念**(如今由RAI Institute推进):打造能做人类和动物所能做之事的机器人——先经数十年打磨"运动智能(athletic intelligence)",认知能力随后跟进。2025–26年的合作结构实际上将Raibert的研究议程与BD的产品线重新绑定在一起。
- **Hyundai的理念**:机器人是下一代"汽车"。集团在CES 2026提出的"物理AI(Physical AI)"战略,使BD成为一场财阀级豪赌的制造业臂膀——260亿美元的美国投资额度、一座机器人工厂,以及以自身工厂作为首个大客户。Hyundai表示**工业部署先于任何家用场景**(KED,2026-03)。
- 值得注意的战略反转:BD三十年来一直是该领域的研究展示橱窗;当前的赌注在于**制造纪律,而非模型优势,才是制胜关键**——"每一个部件的设计都考虑到了与汽车供应链的兼容性"(Zack Jackowski,Atlas总经理)。

## 产品与部署(真实数据)

### Atlas(人形机器人)——截至2026-07
- **2026年整个量产产能已全部认购**给两大客户:**Hyundai的Robotics Metaplant Application Center(RMAC,佐治亚州,2026年开业)**与**Google DeepMind**;更多客户预计2027年初加入(公司口径)。
- **Hyundai部署计划**:在Hyundai/Kia各工厂部署25,000+台Atlas——**Metaplant America(佐治亚州萨凡纳)自2028年起**(零部件排序),Kia佐治亚工厂2029年,组件装配约自2030年起。这将占用计划中3万台/年产能的约83%(媒体测算)。
- 韩国本土豁免:Hyundai表示Atlas**不会**部署于韩国国内工厂——优先北美(Seoul Economic Daily,2026-04)——此前Hyundai分支的韩国金属工人工会曾声明"未经劳资协议,任何机器人都不得进入工作场所"(2026-01-22)。
- CES之后随即在波士顿总部启动生产;量产目标为**2028年**在一座年产3万台的美国工厂实现(已宣布;截至2026-07,选址细节尚不明朗)。

### Spot(四足机器人)——盈利尚未转正的现金牛
- **全球已部署3,000+台**(2026年,第三方数据,未证实;公司此前公布的里程碑数字曾超过1,500台);基础售价**74,500美元**(2020年发售,价格大致维持不变)。
- 应用领域:工业巡检(石油天然气、公用事业、采矿、建筑监测)、公共安全、科研;北美地区认证集成商35+家(市场报告,未证实)。欧洲约占市场28%(市场报告,未证实)。
- 第三方估计:**2025年Spot+Stretch合计出货超500台,营收约1.3亿美元**(聚合器数据,未证实——与1,501亿韩元的财报数字在方向上大体一致)。

### Stretch(物流货箱搬运)
- **DHL**:自2018年起合作,2023年起实现商用部署(先北美,后英国/欧洲);**2025-05-13签署战略性谅解备忘录,增购1,000+台Stretch**——该品类中已知规模最大的公开承诺,尽管仅是谅解备忘录而非正式采购订单(DHL集团一手信息)。
- 其他客户:**Gap**(先在纽约Fishkill试点,再到田纳西州为期一年试点,最终推广至俄亥俄/得州/加州)、**H&M、Maersk/Performance Team、Otto Group**。
- 性能表现:集装箱卸货速度高达**每小时700箱**(公司/DHL口径)。

## 商业模式与单位经济效益

- **模式**:直接产品销售+集成商渠道(Spot)、大客户车队协议(Stretch/DHL),而Atlas则采取**先内部部署为主**的策略,先投入母公司自家工厂,2027年起对外销售。Orbit软件是经常性收入的抓手(车队管理、MES/WMS集成);目前无公开的年化经常性收入(ARR)拆分数据。
- **Atlas定价信号**:据称低于"雇佣两名美国制造业工人两年的成本",约**32万美元**(KED,2026-01,引述"知情人士";无公开建议零售价)。据报道,BD在CES上向分析师透露的初始售价区间为**13万–14万美元**(三星证券Esther Yim,经Boston Globe报道,2026-03);Hyundai工会内部估算约为2亿韩元(约14.5万美元)(单一信源);上一代Atlas的制造成本"历史上曾高达20万美元以上"(Forbes)。参见[硬件](hardware.md)价格对比表。
- **单位经济效益尚未验证**:2025财年营收1,501亿韩元(约1.1亿美元),对比净亏损5,284亿韩元(约3.85亿美元)——亏损约为营收的3.5倍,距Spot开售已过去六年。Hyundai旗下三个未来业务关联公司(机器人、自动驾驶、AAM)**五年累计权益法亏损达2.21万亿韩元(约15亿美元)**(韩国财报报道,2026-05:2.2109万亿韩元,含HMG Global、Motional、Supernal)。
- **融资情况**:Hyundai持续注资的多轮股权融资——仅2025年8月一轮就募集约**9.7亿美元(约1.3万亿韩元)**,超过此前三轮总和(2022–24年共9,820亿韩元;韩国媒体报道)。SoftBank的持股比例从20%稀释至9.65%后才以3.25亿美元退出;具体机制尚不明朗——韩国媒体报道称SoftBank原计划按比例参与(约1.21亿美元)2025年8月那轮融资(未证实)。市场曾传出2027/2028年在纳斯达克上市的计划(单一信源,未证实)。
- 25,000台的Hyundai承诺,使人形机器人项目从一场市场赌注转变为**关联方需求**——降低了营收风险,但并非第三方市场验证(对比[Agility](company-agility.md)的外部客户订单、[Figure](company-figure.md)的宝马部署)。

## 与同行相比的优势/劣势

| 优势 | 劣势 |
|---|---|
| 三十年硬件与控制技术积淀;或可称该领域全身运动能力最强(CES 2026体操展示) | **学习式软件转型较晚**:约2025年才转向强化学习,无自研VLA——"大脑"属于DeepMind,而后者同时也与Apptronik等公司合作(未见排他性证据) |
| **Hyundai关联需求**(25,000+台)+260亿美元美国投资额度+汽车级量产know-how(集团年产能约700万辆) | 亏损约为营收3.5倍;反复注资;估值不透明 |
| 机器人领域品牌力最强;CES 2026"最佳机器人";人才招募磁石 | **成本高/生态封闭**:32万美元的价格信号 vs [Unitree](company-unitree.md) G1约1.6万美元;相比[NVIDIA](company-nvidia.md)的GR00T生态,缺乏开发者/开放模型叙事 |
| Spot/Stretch是拥有蓝筹客户(DHL、Gap、H&M、Maersk)的真实商业业务——在该领域实属难得 | 领导层空缺:自2026-02起为临时CEO;创始人的研究精力已外置于RAI Institute |
| 安全标准的话语权持有者:BD安全负责人共同主导ISO 25785-1标准起草([安全与监管](safety-regulation.md)) | 韩国工会已阻止国内部署;劳资政治为旗舰客户蒙上阴影 |
| 财阀级供应链:Mobis执行器、LG Energy电池、RAI/TRI/DeepMind研究三角 | 量产仍是一个**2028年的承诺**,而Figure、Agility及中国厂商已在2026年实现量产出货([人形机器人](humanoid-robots.md)) |

**质疑者观点**:BD二十年来一直是行业的"演示之王",却只交出约1.1亿美元的营收成绩单;Atlas计划的核心数字(2.5万台、年产3万台工厂、2028年)全都是Hyundai的前瞻性承诺,而非市场订单;对DeepMind的依赖意味着技术栈中最难、最具差异化的一层掌握在他人手中;倘若人形机器人任务经济性令人失望,Hyundai对每年约5,000亿韩元亏损的容忍度将成为唯一的失败风险点。**辩护者观点**:没有任何一家公司同时具备Spot/Stretch级别的成熟商用机器人硬件、一家车企的工厂产能,以及一个前沿实验室级AI合作伙伴——如果人形机器人真的演变为一场汽车级制造业游戏(这正是这场赌注的核心假设),BD相较于软件优先的对手将处于结构性更有利的位置。

## 制造与供应链定位

- **自建组装、财阀式垂直整合零部件供应**——既非Figure式的完全垂直整合,也非Agility式的委托代工。
- **现状**:Atlas生产始于波士顿地区总部(2026年1月);为筹备2028年量产,2026年6月宣布**在Waltham附近扩建1亿美元的机器人/AI中心**(KED)。
- **扩产计划**:在Hyundai 260亿美元美国投资计划下,拟建**一座2028年前投产、年产3万台的美国专用工厂**(截至2026-07,选址/细节尚未确认)。
- **执行器——Hyundai Mobis**(CES 2026宣布):Mobis机器人部件业务的首个商业客户;执行器约占**人形机器人材料成本的60%**(Korea Herald);集团计划由Mobis运营一座**美国工厂,自2028年起年产能超35万台执行器**——规模恰好匹配整个3万台产能(Seoul Economic Daily:从2026-03的"正在评估"到2026-05的"将设立")——Mobis还计划拓展至夹爪、传感器、控制器及电池包领域。
- **电池——LG Energy Solution**:供应合同覆盖美国前三大人形机器人项目(Tesla、Boston Dynamics、Figure);采用高镍三元化学体系(KED,2026-07)。
- **面向制造的设计理念**:量产版Atlas实现了"复杂度降低近一个数量级"以及"独特零件数量大幅减少"(相较上一代,Rodriguez语);"每个部件的设计都考虑了与汽车供应链的兼容性"(Jackowski语)。这正是Hyundai的核心增值所在:将人形机器人当作一个"车型项目"来对待,由Tier-1供应商(Mobis、LG)嵌入既有的汽车认证流程中。
- 对ODM/EMS行业读者而言:BD是一个**封闭体系**——没有已知的ODM/EMS代工外包,没有参考设计授权,零部件均来自集团关联的Tier-1供应商。机会窗口存在于零部件层级(执行器子部件、减速器、传感器、供应给Mobis/LG的电池包),而非整机组装层级。

## 来源

- https://bostondynamics.com/blog/boston-dynamics-unveils-new-atlas-robot-to-revolutionize-industry/ — 量产版Atlas发布公告(2026-01-05):56自由度、2.3米可及范围、50公斤举重、电池更换、RMAC+DeepMind 2026年产能分配、Playter/Jackowski语录、Orbit运行模式(官方)
- https://bostondynamics.com/blog/boston-dynamics-google-deepmind-form-new-ai-partnership/ — Google DeepMind合作:Gemini Robotics作为Atlas的"具身心智"、联合研究团队(官方)
- https://techcrunch.com/2026/01/05/boston-dynamicss-next-gen-humanoid-robot-will-have-google-deepmind-dna/ — DeepMind与Atlas合作的报道
- https://www.therobotreport.com/boston-dynamics-google-reunite-on-next-gen-atlas-humanoid/ — Google"重聚"框架报道、规格确认
- https://www.hyundainews.com/releases/4664 — Hyundai CES 2026 AI机器人战略:2026年RMAC、2028年Metaplant→2030年组装、年产3万台产能(官方)
- https://interestingengineering.com/ai-robotics/hyundai-25000-atlas-humanoid-robots-us-plants — 25,000+台Atlas部署于Hyundai/Kia各工厂;Kia佐治亚工厂2029年
- https://www.techtimes.com/articles/317005/20260522/hyundai-commits-25000-atlas-robots-own-factories-union-blocks-deployment-without-labor-deal.htm — 25,000台=年产3万台产能的约83%;工会对峙
- https://en.sedaily.com/finance/2026/01/22/not-a-single-robot-without-agreement-hyundai-motor-union — 工会声明(2026-01-22)、2亿韩元单机成本估算
- https://en.sedaily.com/news/2026/04/05/hyundai-motor-to-break-ground-on-ulsan-plant-rebuild-next-20260405 — Hyundai排除国内Atlas部署;海外优先
- https://www.kedglobal.com/robotics/newsView/ked202601200007 — Atlas定价低于约两年美国制造业工人薪酬成本(约32万美元上限);分析师13万–14万美元区间
- https://www.kedglobal.com/robotics/newsView/ked202606210001 — Hyundai以3.25亿美元收购SoftBank剩余9.65%股份;2021年看跌期权机制;2026-06-22获批
- https://www.kedglobal.com/robotics/newsView/ked202606250011 — 1亿美元马萨诸塞州机器人/AI中心扩建;为2028年量产做准备
- https://www.kedglobal.com/robotics/newsView/ked202603040003 — Hyundai:工业应用先于家用场景
- https://www.kedglobal.com/batteries/newsView/ked202607020005 — LG Energy Solution向Tesla、Boston Dynamics、Figure供应电池(高镍三元)
- https://www.koreaherald.com/article/10651569 — Hyundai Mobis为Atlas供应执行器;执行器约占材料成本60%;首个机器人部件客户
- https://en.sedaily.com/finance/2026/03/06/hyundai-mobis-weighs-us-plant-for-atlas-robot-parts — Mobis正评估美国工厂,自2028年起年产35万台执行器(单一信源)
- https://bostondynamics.com/news/hyundai-mobis-forms-strategic-collaboration-framework-with-boston-dynamics/ — Mobis与BD战略合作框架(官方)
- https://rai-inst.com/resources/press-release/boston-dynamics-atlas-partnership/ — RAI Institute强化学习合作(2025-02):仿真到现实、全身操作-运动融合、Spot强化学习套件传承(一手信息)
- https://bostondynamics.com/blog/large-behavior-models-atlas-find-new-footing/ — TRI大型行为模型驱动Atlas:约4.5亿参数语言条件化扩散策略(官方,2025-08)
- https://group.dhl.com/en/media-relations/press-releases/2025/dhl-group-signs-mou-with-boston-dynamics-and-accelerates-cross-business-automation-strategy.html — DHL谅解备忘录增购1,000+台Stretch,每小时700箱,自2018年起合作(一手信息,2025-05-13)
- https://wwd.com/sourcing-journal/logistics/boston-dynamics-stretch-robot-warehouses-gap-hm-dhl-supply-chain-1238793351/ — Stretch客户Gap/H&M/DHL;需求细节
- https://www.retailtouchpoints.com/features/retail-success-stories/why-gap-turned-to-robots-for-an-unpopular-fulfillment-task-unloading-boxes — Gap推广路径(Fishkill→田纳西→俄亥俄/得州/加州);每小时700箱
- https://venturebeat.com/ai/boston-dynamics-buy-spot-robot-74500 — Spot商用发售价74,500美元(2020-06)
- https://www.roboticscenter.ai/companies/boston-dynamics — Spot已部署3,000+台;2025年出货超500台/营收约1.3亿美元(聚合器数据,未证实)
- https://techcrunch.com/2026/02/10/boston-dynamics-ceo-robert-playter-steps-down-after-30-years-at-the-company/ — Playter离职(最后工作日2026-02-27);McMaster出任临时CEO
- https://en.wikipedia.org/wiki/Boston_Dynamics — 1992年成立、MIT衍生、股权变更链条(2013年Google、2017年SoftBank、Hyundai 8.8亿美元/80%)、约1,000名员工、产品发布日期
- https://www.ilyo.co.kr/?ac=article_view&entry_id=471437 — 2022–23财年亏损趋势(营收782亿→910亿韩元;净亏损2,551亿→3,348亿韩元);Hyundai融资态势(韩文,2024年——不含2025财年数据)
- https://finance.biggo.com/news/t1MPBJ0BNZYCTTDvFwpX — 2025财年营收1,501亿韩元/净亏损5,284亿韩元;约30万亿韩元估值框架;8.8亿美元收购80%对应11亿美元估值(韩国报道聚合)
- https://www.asiatoday.co.kr/kn/view.php?key=20260528010008586 — 机器人/自动驾驶/AAM关联公司五年累计权益法亏损2.2109万亿韩元(韩文,2026-05-28)
- https://www.bloter.net/news/articleView.html?idxno=640915 — 2025年8月股权融资约9.7亿美元(约1.3万亿韩元),超过此前三轮总和(9,820亿韩元);参与方明细含SoftBank约1.21亿美元按比例参与(韩文)
- https://bostondynamics.com/wp-content/uploads/2026/01/atlas-spec-sheet.pdf — 官方Atlas规格说明书(2025年12月):身高1.9米/重90公斤,瞬时50公斤/持续30公斤/单手20公斤举重,电池续航4小时(高强度举重2小时),3分钟自主电池更换,IP67,-20–40°C,自主/VR遥操作/平板模式,车队技能共享
- https://www.bostonglobe.com/2026/03/04/business/robots-hyundai-atlas-musk-optimus/ — 三星证券(Esther Yim):CES分析师简报,Atlas初始售价13万–14万美元
- https://en.sedaily.com/news/2026/05/20/hyundai-builds-robot-ecosystem-in-us-from-atlas-components — 集团将设立Mobis运营的美国执行器工厂(自2028年起年产35万台以上)
- https://www.newsspace.kr/news/article.html?no=13851 — SoftBank看跌期权截止日期;纳斯达克上市决策框架(韩文,未证实)
- https://douglasresearch.substack.com/p/boston-dynamics-rights-offering-of — 约1.2–1.3万亿韩元股权融资;潜在2027/28年纳斯达克IPO(单一信源,未证实)
- https://www.bloter.net/news/articleView.html?idxno=666151 — Hyundai按"2021年价格"收购:看跌期权按2021年约定条款执行,而非市场估值(韩文)
- https://www.forbes.com/sites/johnkoetsier/2026/07/02/boston-dynamics-new-atlas-humanoid-robot-order-of-magnitude-simpler/ — 第五代Atlas复杂度降低;Rodriguez语录;上一代制造成本超20万美元
- https://diginomica.com/ces-2026-can-boston-dynamics-atlas-robot-carry-humanoid-industry-its-shoulder — Playter完整CES语录;质疑者观点(莫拉维克悖论、中国成本压力)
- https://www.automate.org/robotics/industry-insights/boston-dynamics-to-begin-production-on-redesigned-atlas-humanoid-in-2026 — 2026年产能已认购完毕;2027年初外部客户
- https://www.hyundaimotorgroup.com/en/news/CONT0000000000199186 — Atlas获评"最佳机器人",CES 2026最佳产品(Hyundai官方)
