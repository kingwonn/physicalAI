# blog-zh — 中文博客：源材料归档与分析

这个目录是 physicalAI wiki 的**中文博客层**：以一手中文源材料（播客、长访谈、行业文章）为单位，
每篇博客 = 一份源材料的**归档**（它说了什么，观点归属给讲者）+ **分析**（它对技术树/产业地图的增量，
以及与本 wiki 已有页面的碰撞点）。

与 `wiki/` 的关系与分工：

- **wiki 页面**是中立的、经对抗式事实核查的知识页；**博客**是源材料驱动的、带分析立场的单篇文章。
- 博客提出的新事实**不直接改写 wiki 正文**，而是作为线索推入 `wiki/_meta/queue.md`，
  由循环的 Verify 层（独立多源核查）裁决后再进入正文页。这保持了 wiki「facts need primary
  sources」的纪律，同时让博客可以先行、快速沉淀。
- 博客的 `confidence` 一律从 `draft` 起步；若其关键事实后续被 verify 通过并写入 wiki 页，
  在文末「核查状态」处回注。

## 文件约定

- 文件名：`NNN-<slug>.md`，编号与源材料编号一致（S-001 → `001-…`）。
- 页格式沿用 CLAUDE.md：frontmatter（title/slug/updated/confidence + `lang: zh`）、
  开头一段可独立阅读的摘要、bullet 为主的正文、末尾 `## Sources`。
- 观点必须归属：「许华哲认为…」而非当成事实陈述；易变事实标注「截至 YYYY-MM」；
  单一来源标 `(unverified)`。
- 方法论见 [methodology.md](methodology.md)：这些分析是怎么做出来的（定位→重建→合成→并入）。

## 索引

| # | 文章 | 源材料 | 状态 |
|---|---|---|---|
| — | [分析方法论：一期播客如何变成一篇档案](methodology.md) | （方法页） | draft |
| 001 | [许华哲再次具身创业：「具身智能是世界上的新物种」](001-latetalk-166-xuhuazhe.md) | 晚点聊 LateTalk 166（2026-05-25） | draft |

配套的可视化档案站（源材料库 / 技术树 / 产业地图，随每篇博客修订）：
https://claude.ai/code/artifact/903d6ad2-2090-4e2f-845a-68c982c0631a
（源码在 kingwonn/ycfs 仓库 `embodied-ai/` 目录，分支 `claude/embodied-ai-tech-history-hxx4ew`。）
