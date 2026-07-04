# Media feed watchlist (blogs / YouTube / podcasts)

Zero-config RSS/Atom feeds for the news-sweep step. Rule: feed items are
**leads and sentiment**, not facts — anything promoted to a wiki page still
needs a primary source. Check ✅-tested feeds first; resolve ⏳ ones on first
use and record the URL here.

## Blogs & vertical media (RSS)

| Feed | URL | Status |
|---|---|---|
| The Robot Report | https://www.therobotreport.com/feed/ | ✅ tested 2026-07-04 |
| IEEE Spectrum (robotics topic) | https://spectrum.ieee.org/feeds/topic/robotics.rss | ✅ tested 2026-07-04 |
| NVIDIA blog | https://blogs.nvidia.com/feed/ | ⏳ resolve on first use |
| Humanoids Daily | https://www.humanoidsdaily.com/feed | ⏳ resolve on first use |
| Fei-Fei Li Substack | https://drfeifei.substack.com/feed | ⏳ (Substack always serves /feed) |
| Company blogs (Figure news, pi.website, 1X blog, DeepMind blog, Tesla AI) | — | ⏳ many lack RSS; WebFetch index page instead |

## YouTube channels (official RSS: `youtube.com/feeds/videos.xml?channel_id=<ID>`)

| Channel | channel_id | Status |
|---|---|---|
| Boston Dynamics | UC7vVhkEfw4nOGp8TyDk7RcQ | ✅ tested 2026-07-04 |
| Unitree | UCsMbp4V8oxzHCMdOUP-3oWw | ✅ tested 2026-07-04 (resolved from `"channelId"` in @unitreerobotics/about HTML; feed works) |
| Figure, Tesla, NVIDIA, 1X, Agility, UBTech | — | ⏳ resolve channel_id from channel page `<meta itemprop="channelId">` on first use |

Notes: channel RSS gives titles/dates/links only (enough for lead detection).
For transcripts, `yt-dlp` is not installed; treat video claims as
`(unverified)` unless covered by a written source.

## Podcasts (public podcast RSS; Spotify shows republish these)

| Show | Feed | Status |
|---|---|---|
| Lex Fridman Podcast | https://lexfridman.com/feed/podcast/ | ✅ tested 2026-07-04 — robotics guests occasionally |
| The Robot Report Podcast | — | ⏳ resolve via therobotreport.com |
| Robohub Podcast | — | ⏳ resolve on first use |

Usage: scan episode titles/show notes for names on our watch list (founders,
labs); extract claims from show notes; direct quotes need a transcript or a
secondary written source before entering a page.
