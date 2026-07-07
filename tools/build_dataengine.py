#!/usr/bin/env python3
BASE='/tmp/claude-1001/-home-builder-ai-cc-physicalAI/78d7bb40-9179-4141-9e39-ffdea1c9ef2c/scratchpad/'
# ① 设计原则 (从60设备+10系统蒸馏)
PRIN=[
 ["单时钟公理","1ms 时钟误差=1mm 标签误差(1m/s 手速)。所有模态共享一个晶振;Gen-2 起「任何一路数据不得携带软件时间戳」"],
 ["Measured > recovered,按需付钱","编码器 0 误差 vs SLAM 地板 6–24mm;6mm 够预训练、不够精密插装 → 精度按任务价值分层采购"],
 ["Inpainting 即自认失败","DexUMI 机械+视觉双补 = 事后修域差距的成本自白 → 采集与部署共用同一颗传感头,构造层面归零"],
 ["疲劳墙不可谈判","遥操 ~35 demos/h 人体硬顶($118–136/h);可穿戴 111 demos/h 可众包 → 走量永远归 W 系"],
 ["力/触觉是视频伪造不了的信号","力通道 Gen-1 第一天上人手(~$21 应变梁+ADC);触觉 2 垫→100+ taxel→1,000 taxel/指逐代加密"],
 ["T265 之死 = 供应链纪律","每个关键单源件带命名第二源,断供 90 天内替代过台架;计算模组双源并行认证"],
 ["QC 在采集现场","漂移告警/自动重采/标定健康设备端闭环;被浪费的不是小时是环境多样性(清华幂律)"],
 ["精度主张带日期验收门","每次精度跳变附 pass/fail 日期 + 回退路径;先证伪,后流片"],
]
# ② 需求推导 ladder: [维度, Gen-1, Gen-2(设计目标), Gen-3(设计目标), 推导依据]
REQ=[
 ["标签率","≥60 Hz","≥200 Hz","500 Hz–1 kHz","训练 N Hz 策略需 ≥N Hz 标签(π0 50Hz→Helix S1 200Hz),否则插值伪影进梯度"],
 ["位姿精度","recovered 3–6mm / measured ~1mm","≤2mm / 1°(月9门禁)","全线 1mm / 0.5°","标签噪声必须低于任务公差(精密插装 0.5–2mm)"],
 ["力","单轴抓握 0.5N @1kSPS(原生)","六轴 0.1N @1kHz","0.01N / 0–50N","人手作业 0.5–30N;力控窗口 0.1–1N;冲击瞬态 ~200Hz→奈奎斯特 ≥500Hz"],
 ["触觉","GelSight 定性(选配 $499)","100+ taxel @500Hz","1,000 taxel/指 @1kHz","滑移检测需 ~10² taxel/指;64–1,000 taxel 是训练有效区"],
 ["同步","<0.5ms(声学啁啾)","<10µs(硬件触发)","≤1µs 片上 + gPTP <1µs","200Hz 融合→对齐 ≤0.5ms;1kHz 瞬态→≤100µs"],
]
# ③ 三代: [名, 窗口, mix, 核心硬件, 精度/吞吐, BOM, 门禁/备注]
GENS=[
 ["Gen-1 「既有芯片」","月 0–6 · 90 天出货","W/L/R = 80/15/5",
  "W1:GoPro Hero9→13 二源 + 155°鱼眼 + AS5600 磁编码 + TAL220 应变梁力通道 + ICM-42688 副 IMU + STM32H7;W1e 被动头戴 $350;L1:GELLO 孪生臂 XL330(0.088°)+ 2× D405($272);R1:Orin Nano Super($249)总线侦听 + 干预按钮",
  "SLAM 3–5mm(锚板)· ≥110 demos/h · 同步 <0.5ms 声学啁啾","W1 $520 / L1 双臂 $2,600 / R1 $1,400",
  "全 COTS 零流片;修正数据月 3 起流(RECAP 式);3 万 h 验收 · ~2,000 台 · ~$6/h"],
 ["Gen-2 「自研模组」","月 6–15 · (设计目标)","W主/W被/L/R = 45/15/25/15",
  "公共传感头板卡(三 SKU 共用):2× AR0234 全局快门 + 双 155° 鱼眼立体 + ICM-42688 2kHz 硬触发 + STM32H7 时戳协处理;计算双源:RDK S100(¥2,799,80 TOPS,R52+ 锁步)∥ Quectel SP895BD-AP(Q-8750,80 TOPS);腕部六轴 F/T(Landot)+ 100+ taxel 触觉垫 + 压电接触麦 + 120Hz 注视",
  "≤2mm/1° @200Hz · 采集/部署变体 BOM 差 <5% 同产线","W2 $800–1,400 / L2 $2,400 / R2 $2,400",
  "月 9 台架门禁:ATE≤2mm 且野外中位 ≤4mm,不过→L 系扩产替位;前置:6mm-vs-2mm 精度价值消融 + pretrain-vs-label 消融;40 万 h · ~15,000 台 · $2.5–4/h;保真度 SLA 证书上市"],
 ["Gen-3 「自研芯片+未来传感器」","月 15–24 · (设计目标)","W/L/R = 30/25/45(R 反超)",
  "C1 SoC:锁步 R52 双核 1µs 片上时戳 + EtherCAT/8×CAN-FD + 固定功能 VIO(1kHz @0.5W)+ 40 TOPS NPU(压缩到 token ~100:1)+ 安全隔离区;<$40 @100k,NRE $15–25M;传感器:事件相机(IMX636 类,>10k fps 等效/120dB)+ 1,000 taxel/指尖 0.01N + e-skin 25–50 taxel/cm² + 接触音 8–48kHz + 注视 200Hz + 全身 6 点 IMU",
  "全线 1mm/0.5° @1kHz · 多设备 gPTP <1µs","整机 5–8W · 8–12h 电池日",
  "封线纪律:不上片=通用 AP/基带/部署推理;每块保留 COTS 降级;无事件相机仍须达 2.5mm;300 万 h/年 · ~10 万台 + 5k+ R 化机器人 · <$1–1.5/h"],
]
# ⑤ LeCun 对撞: [论断, 我们的证据, 裁决]
LECUN=[
 ["VLA/模仿 scaling 是 dead end,「已被视为失败」(播客)","GEN-0 幂律 270k h 未饱和 · EgoScale 对数线性 · 清华多样性幂律 · π0.5 未见家庭泛化","我们硬:三条实测曲线 vs 一句修辞;但 RoboChallenge π0.5 均值仅 43.7%——scaling 在赢 ≠ 已够用"],
 ["人类数据效率证明架构缺陷(20h 学开车)","双重反驳:人类感官流 ~10¹⁴ 字节与 LLM 文本同量级;4 岁儿童 ~1,500 亿视觉帧","平局偏我们——且这条恰好支持被动视频 scaling,两边同向"],
 ["JEPA + 极少动作数据即可操作(V-JEPA 2-AC:1M h 视频 + <62h → 零样本 65–80%)","对照基线是 2024 年的 Octo;65–80% 抓放 ≈ VLA 阵营 2024 水平;无接触密集、无力觉","各赢一半:预训练数据效率他赢;绝对操作能力与任务广度我们赢——头对头至今无人做"],
 ["世界模型应预测潜变量,「别做生成式」","数据引擎角色必须出像素(DreamGen/Cosmos Transfer);DreamerV3/Genie 3 是现成反例","我们硬:潜空间 vs 像素是分角色互补,不是路线战争"],
 ["世界模型 MPC「intrinsically safe」","成本函数照样可被博弈;可靠性来自部署期修正数据(RECAP 有部署曲线),不来自架构先验","我们硬:「架构即安全」无实证"],
 ["被动视频足以学直觉物理 → 动作标签塌缩","Helix S1 200Hz 需 ≥200Hz 标签;力/触觉不在视频里;V-JEPA 2-AC 自己也要 62h 动作数据收口","分层各对:世界模型吃 S2 / 动作标签吃 S1 / RL 修正吃 S0——每个 2025-26 前沿系统都是同一张三层配方"],
]
# ⑥ 终局: [年份, 标题, 内容]
END=[
 ["2028","品类合并之年","「数据采集设备」与「机器人传感头」合并为一个品类:≥30% 新机采用第三方标准传感头(2026 为 0%);单时钟格式年产 ≥100 万 h;≥1 个前沿 VLA 训练集 ≥50% 来自同构数据。可穿戴/ego 成预训练默认来源,遥操退守 <5% 的纠错通道。若遥操仍 >30% → 时间表证伪"],
 ["2030","倒置之年","机器人为机器人采集:部署舰队回传占新增数据 >70%;人类演示 <10%;数据现货价 <$0.5–1/h(2026 遥操价的 1/100)。人类角色收缩为干预标注与偏好判断;W/L 系转型「分布尾部补采仪器」按稀缺度计价;C1 主要出货形态是机器人身上的 R 系芯片"],
 ["终态","采集行业消失,脊柱活下来","采集功能溶解进消费级 AR 眼镜与工作手套,人类日常生活成为被动语料。穿越终局的三层资产:传感头模组(Quectel 式量价)· C1 SoC 授权(高通式进 OEM BOM)· 时钟/格式/QC 认证云(ARM 式生态税——物理 AI 的数据清算所)。判据:认证格式 2029 前被 ≥3 家非客户机构采用;C1 硅 2030 前进 ≥1 家 top-10 本体厂 BOM"],
]
import json
D=json.dumps({"prin":PRIN,"req":REQ,"gens":GENS,"lecun":LECUN,"end":END},ensure_ascii=False)
HTML='''<title>SOTA 数据引擎 · 三代路线图</title>
<style>
:root{--paper:#F3F5F5;--panel:#FFF;--ink:#0F171C;--steel:#55666C;--mute:#83979B;--line:#DCE2E2;--line2:#E9EEEE;
--teal:#0C8C88;--tealbr:#12B3AC;--heat:#E4592A;--amber:#C9A24A;--good:#2E8B57;
--sans:"PingFang SC","Microsoft YaHei","Noto Sans CJK SC",system-ui,sans-serif;--mono:ui-monospace,"SF Mono",Consolas,Menlo,monospace}
*{box-sizing:border-box}html{background:var(--paper)}
body{margin:0;font-family:var(--sans);color:var(--ink);line-height:1.6;font-size:15px;-webkit-font-smoothing:antialiased}
.wrap{max-width:1040px;margin:0 auto;padding:0 22px}
a{color:var(--teal);text-decoration:none}a:hover{text-decoration:underline}
.mh{border-top:4px solid var(--teal);background:var(--ink);color:#E8EEEE;padding:30px 0 24px}
.mh .eb{font-family:var(--mono);font-size:11px;letter-spacing:.2em;text-transform:uppercase;color:var(--tealbr);margin:0 0 10px}
.mh h1{font-size:clamp(23px,4vw,34px);font-weight:800;margin:0 0 8px;text-wrap:balance}
.mh p{margin:0;color:#9DB0B3;font-size:14px;max-width:56em}
h2{font-family:var(--mono);font-size:13px;letter-spacing:.1em;text-transform:uppercase;color:var(--steel);margin:36px 0 6px;padding-bottom:8px;border-bottom:1px solid var(--line)}
.sub{font-size:13px;color:var(--steel);margin:0 0 14px}
.tw{overflow-x:auto;border:1px solid var(--line);border-radius:8px;margin:14px 0}
table{border-collapse:collapse;width:100%;font-size:13px;min-width:720px}
th{font-family:var(--mono);font-size:11px;letter-spacing:.04em;text-transform:uppercase;color:var(--steel);font-weight:600;text-align:left;padding:10px 12px;border-bottom:1px solid var(--line);background:var(--paper);vertical-align:bottom}
td{padding:10px 12px;border-bottom:1px solid var(--line2);vertical-align:top;line-height:1.55}
tr:last-child td{border-bottom:none}
.dim{font-weight:700;white-space:nowrap}.reg{font-family:var(--mono);font-size:11.5px;color:var(--mute)}
.pgrid{display:grid;grid-template-columns:repeat(2,1fr);gap:10px;margin:14px 0}
@media(max-width:720px){.pgrid{grid-template-columns:1fr}}
.pcard{background:var(--panel);border:1px solid var(--line);border-radius:8px;padding:12px 15px;border-left:3px solid var(--teal)}
.pcard b{display:block;font-size:14px;margin-bottom:4px}
.pcard span{font-size:12.5px;color:var(--steel);line-height:1.55}
.gen{background:var(--panel);border:1px solid var(--line);border-radius:10px;margin:16px 0;overflow:hidden}
.gen .hd{display:flex;flex-wrap:wrap;align-items:baseline;gap:8px 16px;padding:14px 20px;background:linear-gradient(180deg,rgba(12,140,136,.07),transparent);border-bottom:1px solid var(--line2)}
.gen .hd h3{margin:0;font-size:18px}
.gen .hd .win{font-family:var(--mono);font-size:11.5px;color:var(--mute)}
.gen .hd .mix{font-family:var(--mono);font-size:11.5px;color:#fff;background:var(--teal);padding:2px 9px;border-radius:5px}
.gen .bd{padding:14px 20px}
.gen .row{font-size:13px;line-height:1.6;margin:0 0 8px}
.gen .k{font-family:var(--mono);font-size:10px;letter-spacing:.04em;color:var(--mute);text-transform:uppercase;display:inline-block;min-width:74px}
.gen .gate{border-top:1px dashed var(--line);padding-top:8px;color:var(--steel);font-size:12.5px}
.timeline{display:flex;align-items:center;gap:0;margin:18px 0 4px;font-family:var(--mono);font-size:11px;color:var(--mute)}
.timeline .seg{flex:1;height:6px;border-radius:3px;margin:0 3px}
.lecun{background:var(--panel);border:1.5px solid var(--amber);border-radius:10px;padding:4px 0 0;margin:14px 0;overflow:hidden}
.egrid{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin:14px 0}
@media(max-width:760px){.egrid{grid-template-columns:1fr}}
.ecard{background:var(--ink);color:#DCE6E6;border-radius:10px;padding:18px 20px}
.ecard .yr{font-family:var(--mono);font-size:22px;font-weight:700;color:var(--tealbr)}
.ecard b{display:block;font-size:15px;margin:4px 0 8px;color:#fff}
.ecard p{margin:0;font-size:12.5px;line-height:1.65;color:#AEBFBF}
.readbox{background:linear-gradient(180deg,rgba(12,140,136,.05),var(--panel));border:1.5px solid var(--teal);border-radius:10px;padding:18px 22px;margin:20px 0}
.readbox .h{font-family:var(--mono);font-size:11px;letter-spacing:.1em;text-transform:uppercase;color:var(--teal);font-weight:600;margin:0 0 9px}
.readbox p{margin:0 0 8px;font-size:14px;line-height:1.7}
.readbox b{color:var(--heat)}.readbox .em{color:var(--teal);font-weight:700}
footer{border-top:1px solid var(--line);padding:22px 0 40px;font-size:12.5px;color:var(--steel);margin-top:36px}
footer .m{font-family:var(--mono);font-size:11px;color:var(--mute);margin-top:8px;display:flex;flex-wrap:wrap;gap:6px 18px}
</style>
<div class="mh"><div class="wrap">
  <p class="eb">SOTA 数据引擎 · 设计提案 · 三代路线图 · LeCun 对撞检验</p>
  <h1>W/L/R 数据脊柱:从既有芯片到自研 SoC 的 18–24 个月</h1>
  <p>由具身大脑 scaling 需求(S2/S1/S0)倒推的数据采集系统设计:三份竞争设计书(可穿戴/收敛/车队)经三镜头评委团裁决(C 140 &gt; B 131 &gt; A 125),定案 = C 的数据脊柱 + A 的误差预算工程 + B 的同构传感头。已通过 LeCun ETH Zürich 世界模型演讲(2026-05-29,一手证实)对撞检验:<strong style="color:#12B3AC">骨架成立,被动视频升格为共同主力</strong>。全部前瞻规格为 (设计目标)。</p>
</div></div>
<div class="wrap">
  <h2>① 设计原则 · 从 60 设备 + 10 系统蒸馏</h2>
  <div class="pgrid" id="prin"></div>

  <h2>② 需求推导 · 大脑 scaling 决定数据规格</h2>
  <p class="sub">S2(7–10Hz 慎思)吃量与多样性;<strong>S1(50–200Hz 视觉运动)是整个设计的真正驱动者</strong>;S0(500Hz–1kHz 反射)走仿真重定向 + 部署修正。Gen-2/3 列均为 (设计目标)。</p>
  <div class="tw"><table>
    <thead><tr><th>维度</th><th>Gen-1</th><th>Gen-2 (设计目标)</th><th>Gen-3 (设计目标)</th><th>推导依据</th></tr></thead>
    <tbody id="req"></tbody>
  </table></div>

  <h2>③ 三代路线图</h2>
  <div class="timeline"><span>月 0</span><div class="seg" style="background:var(--teal)"></div><span>6</span><div class="seg" style="background:var(--amber)"></div><span>15</span><div class="seg" style="background:var(--heat)"></div><span>24</span></div>
  <div id="gens"></div>

  <h2>④ LeCun 对撞检验 · 世界模型论纲 vs 我们的证据链</h2>
  <p class="sub">LeCun @ ETH Zürich 2026-05-29「World Models: Enabling the next AI revolution」(活动/日期/视频经其本人帖一手证实;讲内引语按二手处理)。逐条对撞:</p>
  <div class="tw lecun"><table>
    <thead><tr><th>LeCun 论断</th><th>我们已核查的证据</th><th>裁决</th></tr></thead>
    <tbody id="lecun"></tbody>
  </table></div>
  <div class="readbox">
    <p class="h">再思考裁决 · 分层各对</p>
    <p><strong style="color:var(--ink)">映射到 S2/S1/S0,两边都对、只是不在同一层:</strong><span class="em">世界模型预训练吃 S2</span>(被动视频的主场,他基本对)· <span class="em">动作标签微调吃 S1</span>(视频给不了 200Hz 力控标签,我们对)· <span class="em">RL 修正吃 S0/可靠性</span>(他的框架没有部署飞轮层,我们对)。V-JEPA 2-AC(1M h 视频 + 62h 动作)、1X NEO、GR00T、π0.5——2025-26 每个前沿系统都是同一张三层配方,差别只在预训练目标函数。<b>62h 收口数据谁生产?我们这种引擎。</b></p>
    <p><strong style="color:var(--ink)">一句话最大改动:</strong>被动第一视角视频从防御性副 SKU(W1e $350)<b>升格为带自有保真度规格的共同主力产品线</b>(度量深度 + ego-pose ATE 证书 = 世界模型动作条件化保真度证书),混合体从 W/L/R 三元扩为 <span class="em">W主/W被/L/R 四元(Gen-2 参考 45/15/25/15)</span>;新增 pretrain-vs-label 门禁消融;力数据买家从两类扩到三类(策略 + sim 校准 + <b>世界模型物理校准</b>)——范式之争打得越凶,中立军火商越贵。</p>
  </div>

  <h2>⑤ 终局 · PhysicalAI 的面貌(带判据,可证伪)</h2>
  <div class="egrid" id="end"></div>

  <div class="readbox">
    <p class="h">⑥ 评委团与风险(摘要)</p>
    <p><strong style="color:var(--ink)">三镜头三个赢家:</strong>工程判 A 胜(误差预算工程最硬)· 数据科学判 C 胜(数据混合体是一阶设计变量)· 战略判 B 胜(采集=部署是唯一不需转身的终局论)。总分 <span class="em">C 140 &gt; B 131 &gt; A 125</span> 定骨架,评委钦点嫁接:A 的声学啁啾同步与 $21 力通道、B 的锁步时戳岛与三层终态、GELLO 终身保留为野外计量基准仪。<b>两个门禁实验先于两笔最大 capex:6mm-vs-2mm 精度消融先于 Gen-2 精度投资;同构 co-training 消融先于部署变体投资——先证伪,后流片。</b></p>
    <p><strong style="color:var(--ink)">头号风险:</strong>2mm 野外跳票(→L 系扩产替位)· 同构≠域差距归零(每 5k h 消融)· 仿真/纯视频吃掉 S1(→转部署修正+力触觉,视频永远伪造不了)· 部署飞轮提前(→砍 W3 全转 R/C1——组合可转向,单设备只能陪葬)· 供应链单点(每件带第二源)。</p>
  </div>
</div>
<footer><div class="wrap">
  <div>来源:physicalAI 知识库 <a href="https://github.com/kingwonn/physicalAI/blob/main/wiki/data-engine-roadmap.md">wiki/data-engine-roadmap.md</a> + <a href="https://github.com/kingwonn/physicalAI/blob/main/wiki/lecun-worldmodels-rethink.md">wiki/lecun-worldmodels-rethink.md</a>(均 confidence: verified;设计提案,非现有产品)。Gen-1 具名件经对抗核查 2026-07 可购(Hero9 停产已换 Hero13 二源);Gen-2/3 全部 (设计目标)。评委团裁决与嫁接记录、LeCun 引语防火墙(播客≠ETH 现场)见源页。</div>
  <div class="m"><span>快照 2026-07-07</span><span>3 代 · 4 SKU · 6 对撞 · 3 终局判据</span><span>对抗核查</span></div>
</div></footer>
<script>
const D=__DATA__;
function esc(s){const d=document.createElement("div");d.textContent=s==null?"":s;return d.innerHTML;}
document.getElementById("prin").innerHTML=D.prin.map(p=>`<div class="pcard"><b>${esc(p[0])}</b><span>${esc(p[1])}</span></div>`).join("");
document.getElementById("req").innerHTML=D.req.map(r=>`<tr><td class="dim">${esc(r[0])}</td><td>${esc(r[1])}</td><td>${esc(r[2])}</td><td>${esc(r[3])}</td><td class="reg" style="font-size:12px;color:var(--steel)">${esc(r[4])}</td></tr>`).join("");
const colors=["var(--teal)","var(--amber)","var(--heat)"];
document.getElementById("gens").innerHTML=D.gens.map((g,i)=>`<div class="gen" style="border-top:3px solid ${colors[i]}"><div class="hd"><h3>${esc(g[0])}</h3><span class="win">${esc(g[1])}</span><span class="mix">${esc(g[2])}</span></div><div class="bd"><p class="row"><span class="k">核心硬件</span>${esc(g[3])}</p><p class="row"><span class="k">精度/吞吐</span>${esc(g[4])}</p><p class="row"><span class="k">BOM/功耗</span>${esc(g[5])}</p><p class="row gate"><span class="k">门禁/规模</span>${esc(g[6])}</p></div></div>`).join("");
document.getElementById("lecun").innerHTML=D.lecun.map(l=>`<tr><td style="min-width:180px">${esc(l[0])}</td><td>${esc(l[1])}</td><td style="min-width:170px;color:var(--steel)">${esc(l[2])}</td></tr>`).join("");
document.getElementById("end").innerHTML=D.end.map(e=>`<div class="ecard"><div class="yr">${esc(e[0])}</div><b>${esc(e[1])}</b><p>${esc(e[2])}</p></div>`).join("");
</script>'''
DOCTYPE='<!doctype html>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1">\n'
open(BASE+'data-engine-roadmap.html','w').write(DOCTYPE+HTML.replace('__DATA__',D))
print('written · prin',len(PRIN),'· req',len(REQ),'· gens',len(GENS),'· lecun',len(LECUN),'· end',len(END))
