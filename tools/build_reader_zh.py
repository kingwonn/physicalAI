#!/usr/bin/env python3
"""Render the Chinese wiki mirror (wiki-zh) into a single-file HTML reader."""
import os, re, html, importlib.util

spec = importlib.util.spec_from_file_location('br', '/tmp/claude-1001/-home-builder-ai-cc-physicalAI/78d7bb40-9179-4141-9e39-ffdea1c9ef2c/scratchpad/build_reader.py')
# We reuse md2html/inline/parse by re-implementing paths here instead of importing (base script runs at import).

WIKI = '/home/builder/ai/cc/physicalAI/wiki-zh'
OUT = '/tmp/claude-1001/-home-builder-ai-cc-physicalAI/78d7bb40-9179-4141-9e39-ffdea1c9ef2c/scratchpad/physicalai-wiki-reader-zh.html'

GROUPS = [
    ('总览', [('HOME', 'HOME.md')]),
    ('核心', [('history', 'history.md'), ('state-of-the-art', 'state-of-the-art.md'), ('tech-tree', 'tech-tree.md'), ('on-device-brain', 'on-device-brain.md'), ('visions', 'visions.md')]),
    ('技术', [('vla-models', 'vla-models.md'), ('world-models', 'world-models.md'), ('humanoid-robots', 'humanoid-robots.md'), ('manipulation', 'manipulation.md'),
             ('locomotion', 'locomotion.md'), ('simulation', 'simulation.md'), ('hardware', 'hardware.md'),
             ('data', 'data.md'), ('data-collection-devices', 'data-collection-devices.md'), ('data-foundry', 'data-foundry.md'), ('data-engine-roadmap', 'data-engine-roadmap.md'), ('lecun-worldmodels-rethink', 'lecun-worldmodels-rethink.md'), ('tactile-hands', 'tactile-hands.md'), ('component-supply-chain', 'component-supply-chain.md'), ('evaluation', 'evaluation.md')]),
    ('人与组织', [('key-people', 'key-people.md'), ('organizations', 'organizations.md'), ('academic-labs', 'academic-labs.md')]),
    ('区域格局', [('landscape-usa', 'landscape-usa.md'), ('landscape-china', 'landscape-china.md'), ('landscape-row', 'landscape-row.md')]),
    ('资本与前沿', [('investment', 'investment.md'), ('odm-opportunity', 'odm-opportunity.md'), ('odm-competitors', 'odm-competitors.md'), ('open-problems', 'open-problems.md'), ('safety-regulation', 'safety-regulation.md')]),
    ('公司深度', [('company-figure', 'company-figure.md'), ('company-unitree', 'company-unitree.md'), ('company-pi', 'company-pi.md'), ('company-nvidia', 'company-nvidia.md'), ('company-optimus', 'company-optimus.md'), ('company-bostondynamics', 'company-bostondynamics.md'), ('company-agility', 'company-agility.md'), ('company-1x', 'company-1x.md'), ('company-skild', 'company-skild.md'), ('company-agibot', 'company-agibot.md'), ('company-ubtech', 'company-ubtech.md')]),
    ('参考', [('glossary', 'glossary.md')]),
]

KNOWN = {fn.split('/')[-1]: slug for _, pages in GROUPS for slug, fn in pages}

def inline(s):
    s = html.escape(s, quote=False)
    s = re.sub(r'`([^`]+)`', r'<code>\1</code>', s)
    s = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', s)
    s = re.sub(r'(?<![\w*])\*([^*\n]+)\*(?![\w*])', r'<em>\1</em>', s)
    s = re.sub(r'~~([^~]+)~~', r'<del>\1</del>', s)
    def link(m):
        text, url = m.group(1), m.group(2)
        base = url.split('#')[0].split('/')[-1]
        if base in KNOWN:
            return f'<a href="#{KNOWN[base]}">{text}</a>'
        if url.startswith('http'):
            return f'<a href="{url}" target="_blank" rel="noopener">{text}</a>'
        return text
    s = re.sub(r'\[([^\]]+)\]\(([^)\s]+)\)', link, s)
    s = re.sub(r'(?<!href=")(?<!">)(https?://[^\s<>"]+)', r'<a href="\1" target="_blank" rel="noopener">\1</a>', s)
    return s

def md2html(text):
    lines = text.split('\n')
    out, i = [], 0
    ul_depth = 0
    in_ol = False
    in_bq = False
    def close_lists():
        nonlocal ul_depth, in_ol
        while ul_depth > 0:
            out.append('</ul>'); ul_depth -= 1
        if in_ol: out.append('</ol>'); in_ol = False
    def close_bq():
        nonlocal in_bq
        if in_bq: out.append('</blockquote>'); in_bq = False
    while i < len(lines):
        ln = lines[i]
        if ln.strip().startswith('|') and i + 1 < len(lines) and re.match(r'^\s*\|[\s\-:|]+\|\s*$', lines[i+1]):
            close_lists(); close_bq()
            hdr = [c.strip() for c in ln.strip().strip('|').split('|')]
            out.append('<div class="tw"><table><thead><tr>' + ''.join(f'<th>{inline(c)}</th>' for c in hdr) + '</tr></thead><tbody>')
            i += 2
            while i < len(lines) and lines[i].strip().startswith('|'):
                cells = [c.strip() for c in lines[i].strip().strip('|').split('|')]
                out.append('<tr>' + ''.join(f'<td>{inline(c)}</td>' for c in cells) + '</tr>')
                i += 1
            out.append('</tbody></table></div>')
            continue
        s = ln.rstrip()
        m = re.match(r'^(#{2,4})\s+(.*)', s)
        if m:
            close_lists(); close_bq()
            lvl = len(m.group(1))
            out.append(f'<h{lvl}>{inline(m.group(2))}</h{lvl}>')
        elif re.match(r'^\s*([-*+])\s+', s):
            close_bq()
            if in_ol: out.append('</ol>'); in_ol = False
            indent = len(s) - len(s.lstrip())
            depth = 2 if indent >= 2 else 1
            while ul_depth < depth: out.append('<ul>'); ul_depth += 1
            while ul_depth > depth: out.append('</ul>'); ul_depth -= 1
            item = re.sub(r'^\s*[-*+]\s+', '', s)
            item = item.replace('[ ]', '☐', 1).replace('[x]', '☑', 1) if item.startswith('[') else item
            out.append(f'<li>{inline(item)}</li>')
        elif re.match(r'^\s*\d+\.\s+', s):
            close_bq(); close_lists()
            if not in_ol: out.append('<ol>'); in_ol = True
            out.append(f'<li>{inline(re.sub(r"^\s*\d+\.\s+", "", s))}</li>')
        elif s.startswith('>'):
            close_lists()
            if not in_bq: out.append('<blockquote>'); in_bq = True
            out.append(f'<p>{inline(s.lstrip(">").strip())}</p>')
        elif re.match(r'^-{3,}$', s.strip()):
            close_lists(); close_bq()
            out.append('<hr>')
        elif not s.strip():
            close_lists(); close_bq()
        else:
            close_lists(); close_bq()
            out.append(f'<p>{inline(s)}</p>')
        i += 1
    close_lists(); close_bq()
    return '\n'.join(out)

def parse(fn):
    raw = open(os.path.join(WIKI, fn)).read()
    meta = {}
    if raw.startswith('---'):
        end = raw.index('\n---', 3)
        for l in raw[3:end].strip().split('\n'):
            if ':' in l:
                k, v = l.split(':', 1)
                meta[k.strip()] = v.strip().strip('"')
        raw = raw[end+4:]
    return meta, raw

nav, sections = [], []
total = 0
for gname, pages in GROUPS:
    items = []
    for slug, fn in pages:
        if not os.path.exists(os.path.join(WIKI, fn)):
            continue
        meta, body = parse(fn)
        title = meta.get('title', slug)
        conf = meta.get('confidence', '')
        upd = meta.get('updated', '')
        badge = '<span class="ok">✓ 已核查</span>' if conf == 'verified' else ('<span class="dr">草稿</span>' if conf else '')
        head = f'<div class="pagehead"><h1>{html.escape(title)}</h1><p class="pmeta">{badge}{("<span>更新 " + upd + "</span>") if upd else ""}<span class="slugtag">{slug}</span></p></div>'
        sections.append(f'<article id="{slug}" class="page">{head}{md2html(body)}</article>')
        items.append((slug, title))
        total += 1
    if items:
        nav.append((gname, items))

navhtml = ''
for gname, items in nav:
    navhtml += f'<div class="ng"><p class="nglabel">{gname}</p>'
    for slug, title in items:
        navhtml += f'<a class="nl" href="#{slug}" data-slug="{slug}" data-t="{html.escape(title.lower())}">{html.escape(title)}</a>'
    navhtml += '</div>'

page = '''<title>physicalAI 知识库(中文版)</title>
<style>
:root{--paper:#F4F6F7;--panel:#FFF;--ink:#1A2329;--steel:#5B6B75;--line:#D8DFE3;--accent:#C0392B;--ok:#2B8A3E;--wait:#8A97A0;
--sans:-apple-system,"Segoe UI","Helvetica Neue","PingFang SC","Microsoft YaHei","Noto Sans CJK SC",sans-serif;
--mono:ui-monospace,"SF Mono","Cascadia Code",Consolas,Menlo,monospace}
html{background:var(--paper);scroll-behavior:smooth}
body{font-family:var(--sans);color:var(--ink);line-height:1.75;margin:0;display:flex;min-height:100vh}
a{color:var(--accent);text-decoration:none}a:hover{text-decoration:underline}
nav{width:250px;flex:none;border-right:1px solid var(--line);background:var(--panel);padding:18px 0 40px;position:sticky;top:0;height:100vh;overflow-y:auto}
.brand{padding:0 18px 12px;border-bottom:1px solid var(--line);margin-bottom:10px}
.brand .eb{font-family:var(--mono);font-size:10px;letter-spacing:.13em;text-transform:uppercase;color:var(--accent);margin:0 0 4px}
.brand h2{font-size:15px;margin:0}
.brand p{font-size:11px;color:var(--steel);margin:4px 0 0}
#q{margin:10px 18px;width:calc(100% - 36px);box-sizing:border-box;padding:6px 9px;border:1px solid var(--line);border-radius:5px;font-family:var(--mono);font-size:12px;background:var(--paper);color:var(--ink)}
.ng{margin:12px 0 0}
.nglabel{font-family:var(--mono);font-size:10px;letter-spacing:.12em;text-transform:uppercase;color:var(--wait);margin:0 0 3px;padding:0 18px}
.nl{display:block;padding:4px 18px;font-size:13px;color:var(--ink);border-left:3px solid transparent}
.nl:hover{background:var(--paper);text-decoration:none}
.nl.on{border-left-color:var(--accent);background:var(--paper);font-weight:600}
main{flex:1;min-width:0;padding:34px 44px 80px}
.page{display:none;max-width:820px;margin:0 auto}
.page.show{display:block}
.pagehead{border-top:4px solid var(--accent);padding-top:18px;margin-bottom:6px}
.pagehead h1{font-size:26px;margin:0 0 6px;letter-spacing:-.01em}
.pmeta{display:flex;gap:14px;align-items:center;font-family:var(--mono);font-size:11px;color:var(--steel);margin:0 0 8px}
.pmeta .ok{color:var(--ok)}.pmeta .dr{color:#9A6A00}
.slugtag{color:var(--wait)}
h2{font-size:19px;margin:30px 0 10px;padding-bottom:6px;border-bottom:1px solid var(--line)}
h3{font-size:15px;margin:22px 0 8px}h4{font-size:13.5px;margin:18px 0 6px}
p{margin:8px 0}li{margin:4px 0}ul,ol{padding-left:24px;margin:8px 0}
blockquote{margin:14px 0;padding:10px 16px;border-left:3px solid var(--accent);background:var(--panel);border-radius:0 6px 6px 0;color:var(--steel)}
blockquote p{margin:4px 0}
code{font-family:var(--mono);font-size:.88em;background:#EAEEF0;padding:1px 5px;border-radius:4px}
.tw{overflow-x:auto;margin:14px 0;border:1px solid var(--line);border-radius:6px;background:var(--panel)}
table{border-collapse:collapse;width:100%;font-size:13px}
th{font-family:var(--mono);font-size:11px;letter-spacing:.06em;text-transform:uppercase;color:var(--steel);text-align:left;padding:8px 12px;border-bottom:1px solid var(--line);white-space:nowrap;background:var(--paper)}
td{padding:7px 12px;border-bottom:1px solid var(--line);vertical-align:top}
tr:last-child td{border-bottom:none}
hr{border:none;border-top:1px solid var(--line);margin:22px 0}
@media(max-width:760px){
 body{display:block}
 nav{position:static;width:auto;height:auto;border-right:none;border-bottom:1px solid var(--line)}
 main{padding:20px 16px 60px}}
</style>
<nav>
 <div class="brand">
  <p class="eb">Physical AI · LLM-Wiki · 中文版</p>
  <h2>physicalAI 知识库</h2>
  <p>__TOTAL__ 页全译 · 与英文版同步 · <a href="https://claude.ai/code/artifact/68ac0327-eba9-4992-b59e-f0a842129433" target="_blank" rel="noopener">English ↗</a> · <a href="https://claude.ai/code/artifact/821047d4-fdd2-44a8-b26e-0034119ae56f" target="_blank" rel="noopener">控制台 ↗</a></p>
 </div>
 <input id="q" placeholder="筛选页面…" oninput="flt(this.value)">
 __NAV__
</nav>
<main>__SECTIONS__</main>
<script>
function show(){
 var h=(location.hash||'#HOME').slice(1);
 var el=document.getElementById(h);
 if(!el){h='HOME';el=document.getElementById('HOME')}
 document.querySelectorAll('.page').forEach(function(p){p.classList.remove('show')});
 document.querySelectorAll('.nl').forEach(function(n){n.classList.toggle('on',n.dataset.slug===h)});
 if(el){el.classList.add('show');window.scrollTo(0,0)}
}
function flt(v){
 v=v.toLowerCase();
 document.querySelectorAll('.nl').forEach(function(n){n.style.display=(!v||n.dataset.t.indexOf(v)>=0||n.dataset.slug.indexOf(v)>=0)?'block':'none'});
}
window.addEventListener('hashchange',show);show();
</script>'''

page = page.replace('__NAV__', navhtml).replace('__SECTIONS__', '\n'.join(sections)).replace('__TOTAL__', str(total))
open(OUT, 'w').write(page)
print('zh pages rendered:', total, '| bytes:', os.path.getsize(OUT))
