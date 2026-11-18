# -*- coding: utf-8 -*-
"""English version (/en/). build.py가 불러 씁니다.
한국어 페이지와 같은 구조를 영어로 만듭니다. 새 영문 페이지를 만들면 EN_PAGES 에 한국어 slug를 넣으세요."""

NAV = [('log', 'Work log'), ('projects', 'Programs'), ('services', 'Try it'), ('consulting', 'Semiconductor'), ('about', 'About')]
CATS = [('all', 'All'), ('svc', 'Public services'), ('iot', 'IoT · Automation'), ('ops', 'Ops · AI tools'), ('biz', 'Commerce · Trading R&D'), ('plan', 'In planning')]
KR_ONLY = {'airang', 'program-trader', 'project-commerce', 'program-lagrills'}

# slug: (English name, status, platform, one-liner)
EP = {
 'drive-console': ('Drive Console', 'Testers wanted', 'Android', 'Turn a spare tablet or phone into your car dashboard. Reads about 10,000 OBD fault codes and explains the likely cause and what to check.'),
 'airang': ('Airang', 'Live · 63 towns', 'Web (PWA)', 'Local info for families with kids — school calendars, meals, academies, clinics — refreshed every morning on one screen. Free, no sign-up.'),
 'project-home-iot': ('Songgol Home IoT · AI wall pad', 'Field-testing', 'Windows · Tablet', 'A wall pad built for our own house with no renovation: a floor-plan screen, voice assistant, presence-sensing lights and radio.'),
 'program-lagrills': ('La Grills Hub', 'Running on site', 'Windows', 'Turns zone-by-zone air conditioners at a self-service BBQ place on and off from one counter PC.'),
 'project-farm': ('IoT Greenhouse', 'In planning', 'IoT', 'Bringing our home IoT setup to the family farm — a small smart-farm experiment.'),
 'project-control': ('Central Control (HUD)', 'In daily use', 'Windows · Web · Phone', 'Everyone wants their own JARVIS-style assistant. Every program I build shows up on one control screen, and I can ask it things by voice.'),
 'program-printbench': ('3D Print Bench', 'In development', 'Windows', 'Watch, queue and safely run your 3D printer from one PC screen. No cloud — it stays on your home network.'),
 'project-robot': ('Butler Robot', 'Design done', 'Robot vacuum + 3D printer parts', 'Turning a broken robot vacuum and an old 3D printer into a butler robot that comes when called and brings you water.'),
 'program-ai-team': ('AI Team', 'Internal', 'Windows · Phone', 'A workshop where work is split across several AIs — a lead AI plans and reviews, team AIs handle the pieces.'),
 'program-sns': ('Social Media Hub', 'Internal', 'Windows', 'Instagram, Threads and the blog in one program — write, schedule and track reactions.'),
 'program-login': ('Login Status Board', 'Internal', 'Chrome extension', 'Sign-in and API-key status for 60+ sites on one screen, with an alert the moment something drops.'),
 'program-invest': ('Project Spend Tracker', 'In use', 'Windows', 'Sorts AliExpress and Gmarket purchases by project automatically and shows monthly spend at a glance.'),
 'project-commerce': ('Ali Sourcing Helper', 'In development', 'Windows', 'Finds overseas products worth selling and drafts listings — titles, prices and promo posts — for a Korean marketplace.'),
 'program-trader': ('Songgol Trader', 'In development', 'Windows', 'Korean stocks and crypto in one program and one screen. Separate engines per market, one control view. A personal test project.'),
 'program-booking': ('AI Booking Assistant', 'Mock-ups', 'Mobile · PC', 'Ask in plain words and it finds flights, trains, stays and restaurants, lists them by number, and books only what you pick.'),
}
NAMES = {k: (v[0], v[1]) for k, v in EP.items()}

EN_PAGES = {'index', 'projects', 'about'}


def card(p):
    import programs as PG
    slug, name, cat, st, stl, plat, ver, one, (c1, c2, ic, ph) = p
    n, s, pl, o = EP[slug]
    href = '/drive-console-en' if slug == 'drive-console' else ('/en/' + slug if slug in EN_PAGES else '/' + slug)
    stc = {'live': 'live', 'plan': 'plan'}.get(st, '')
    catname = dict(CATS)[cat]
    kr = ''
    meta = f'<span>{pl}</span>' + (f'<span>{ver}</span>' if ver not in ('—', '0단계') else '') + kr
    return f'''<a class="prog rv" data-cat="{cat}" href="{href}">{PG.art(c1, c2, ic, ph)}<span class="st {stc}">{s}</span></div>
<div class="tx"><span class="cat">{catname.upper() if cat != "svc" else "PUBLIC SERVICE"}</span><h3>{n}</h3><p>{o}</p><div class="meta">{meta}</div></div></a>'''


def add(g):
    PAGES, btn, BLOG, MAIL = g['PAGES'], g['btn'], g['BLOG'], g['MAIL']
    g['EN_PAGES'].update(EN_PAGES)
    import programs as PG
    import home as H
    import workshop as W

    # ---------------------------------------------------------------- home
    now = [('Working on', 'Drive Console', 'Getting ready for the public launch · 14-day closed test'), ('Testing', 'AI Team', 'All AIs working together · 2-week trial'),
           ('Field-testing', 'Songgol Home IoT', 'Presence-sensing lights · wall-pad radio'), ('Next up', 'Butler Robot', 'Measuring parts before the first build')]
    now_html = ''.join(f'<li><span class="st">{a}</span><b>{b}</b><em>{c}</em></li>' for a, b, c in now)
    recent = [('11.18', 'Butler Robot', 'Stage 0', 'Design done · measuring starts'), ('11.18', '3D Print Bench', 'v0.9', 'Program page published'),
              ('11.17', 'Central Control', 'v1.19.8', 'Intro video released'), ('11.14', 'Songgol Trader', 'v0.3.0', 'Stocks + crypto merged into one'),
              ('11.12', 'Songgol Lab', '—', 'Moved to songgollab.co.kr')]
    recent_html = ''.join(f'<li><time>{d}</time><b>{p}</b><code>{v}</code><span>{t}</span></li>' for d, p, v, t in recent)
    hero = f'''<section class="ws-hero soft"><div class="wrap">
<div>
  <span class="eyebrow">Songgol Lab · Open Workshop</span>
  <h1>For 20 years I fixed semiconductor equipment.<br><span class="grad">Now I fix everyday life.</span></h1>
  <p class="lead">Songgol Lab is one engineer's <b>open workshop</b> in Yongin, Korea. When something at home, in the car or at the shop is a hassle, I turn it into a program, use it myself, keep fixing it — and log the whole process here.</p>
  <div class="cta">{btn('/en/projects', 'See the programs →')}{btn('#try', 'Try it now', 'line')}</div>
</div>
<div class="bench" aria-label="Workbench status">
  <div class="bench-top"><span class="dots"><i></i><i></i><i></i></span><span class="mono">songgollab — workbench</span><span class="live"><i></i>LIVE</span></div>
  <div class="bench-img"><img src="/assets/drive-console.jpg" alt="Drive Console on the workbench"><span class="tag">On the bench now · Drive Console</span></div>
  <ul class="bench-now">{now_html}</ul>
  <div class="bench-sub mono">Recent changes</div>
  <ul class="bench-log">{recent_html}</ul>
</div>
</div></section>'''

    stats_items = [('48', 'days', 'since the first line (2026.10.01)'), (str(len(PG.P)), '', 'programs built'), ('238', '', 'version updates'), ('12', '', 'Drive Console testers'), ('63', '', 'towns on Airang')]
    stats = '<section class="ws-stats"><div class="wrap"><div class="nums">' + ''.join(
        f'<div class="rv"><b>{n}<small>{u}</small></b><span>{t}</span></div>' for n, u, t in stats_items) + '</div><p class="asof mono">as of 2026.11.18</p></div></section>'

    try_sec = f'''<section class="s2 white" id="try"><div class="wrap">
<div class="head"><div><span class="eyebrow">Try it</span><h2>Out of the workshop —<br>use them today</h2></div><p>Both are free. Tell me what bugs you and it goes into the next work log.</p></div>
<div class="tries">
  <a class="try rv" href="/drive-console-en"><div class="im" style="background-image:url('/assets/drive-console.jpg')"></div>
    <div class="tx"><span class="badge amber">Testers wanted · Free</span><h3>Drive Console</h3><p>Turn a spare Android tablet or phone into a car dashboard. It reads fault codes and shows the likely cause and what to check, in order.</p><span class="go">Join the test →</span></div></a>
  <a class="try rv" href="/airang"><div class="im" style="background-image:url('/assets/airang-phone.jpg');background-position:top"></div>
    <div class="tx"><span class="badge">Public service</span><h3>Airang</h3><p>Local info for families with kids in 63 Korean towns, collected every morning onto one screen. No sign-up. (Korean only)</p><span class="go">Open Airang →</span></div></a>
</div></div></section>'''

    tools = ''.join(
        f'<a class="tool rv" href="{"/drive-console-en" if s == "drive-console" else ("/en/" + s if s in EN_PAGES else "/" + s)}"><span class="dot {st}"></span><b>{EP[s][0]}</b><code>{v if v not in ("—", "0단계") else ""}</code></a>'
        for s, n, c, st, stl, pl, v, one, art in PG.P)
    tools_sec = f'''<section class="s2"><div class="wrap">
<div class="head"><div><span class="eyebrow">On the bench</span><h2>{len(PG.P)} programs so far</h2></div>
<p>From public services to IoT for the house and shop, tools that keep things running, personal R&amp;D and ideas still on paper. Click any of them for details.</p></div>
<div class="tools">{tools}</div>
<p style="margin-top:22px"><a class="more" style="font-weight:700;color:var(--blue)" href="/en/projects">See all programs →</a></p>
</div></section>'''

    semi = f'''<section class="s2 white" id="semi"><div class="wrap">
<div class="semi" style="box-shadow:none;border:0;padding:0;background:transparent">
  <div><span class="eyebrow">Semiconductor · Wet-clean equipment</span>
  <h2>Tracking down the cause<br>no one can see</h2>
  <p>This workshop started on the fab floor. For 20 years I tracked down defects on semiconductor wet-clean equipment by tying together its software, hardware, sequences and controls. I wrote that experience up separately.</p>
  <div class="cta" style="display:flex;gap:10px;margin-top:22px;flex-wrap:wrap">{btn('/consulting', 'Read more (Korean) →')}</div></div>
  <div><div class="panel"><div class="panel-head"><span>WAFER MAP · INSPECTION</span><b>● ANALYZING</b></div>{H.wafer_svg()}<span class="panel-note">Illustration only · not real data</span></div></div>
</div>
</div></section>'''

    owner = f'''<section class="s2"><div class="wrap owner">
<div class="ph" style="display:flex;align-items:center;justify-content:center;background:radial-gradient(circle at 50% 35%,#1B2B4D,#0A1428 70%);border-radius:24px;padding:36px"><img class="logo-full" src="/assets/logo-full.png" alt="Songgol Lab logo" style="max-width:100%"></div>
<div><span class="eyebrow">The engineer</span><h2>20 years at the machine,<br>always chasing the root cause</h2>
<p>On the semiconductor wet-clean floor I learned to ask why something is needed first, try it for real, and only move on when the result can be reproduced. I build everything here the same way.</p>
<div class="principles"><span>I use it first</span><span>I write it down as it is</span><span>I keep fixing it while I use it</span></div>
<div class="cta" style="display:flex;gap:10px;margin-top:22px;flex-wrap:wrap">{btn('/en/about', 'About the workshop')}{btn('/en/projects', 'All programs →', 'line')}</div></div>
</div></section>'''

    doors = f'''<section class="s2"><div class="wrap doors">
<a class="door rv" href="/drive-console-en#tester"><span class="eyebrow">Door 1</span><h3>Try it</h3><p>Join the Drive Console test or send feedback on any program.</p><span class="go">Join the test →</span></a>
<a class="door dark2 rv" href="mailto:{MAIL}"><span class="eyebrow">Door 2</span><h3>Say hello</h3><p>Feedback, bug reports, or just to talk tech.</p><span class="go">Email me →</span></a>
</div></section>'''

    PAGES['en'] = ('', "Songgol Lab — a semiconductor equipment engineer's open workshop. Programs for home, car and shop, built and used every day, with every step logged.", '',
                   hero + stats + try_sec + tools_sec + semi + owner + doors, 'en', '')

    def ehero(cur, eyebrow, h1, lead):
        return g['hero']([], eyebrow, h1, lead).replace('<a href="/">홈</a>', f'<a href="/en/">Home</a> › <span>{cur}</span>', 1)

    # ---------------------------------------------------------------- programs
    filt = '<div class="filters" id="filters">' + ''.join(f'<button data-f="{k}"{" class=on" if k == "all" else ""}>{v}</button>' for k, v in CATS) + '</div>'
    cat = '<div class="progs" id="progs">' + ''.join(card(p) for p in PG.P) + '</div>'
    ph = ehero('Programs', 'Programs', f'Built by me,<br>used by me — {len(PG.P)} programs',
                   'An engineer with 20 years on semiconductor equipment, turning everyday hassles into programs one at a time. Public services, internal tools, personal R&amp;D and ideas still in planning — all here.')
    note = '<p class="p" style="margin-top:18px;color:var(--ink3,#64748B)">Detail pages are being translated. Until then, programs without an English page open the Korean page.</p>'
    PAGES['en/projects'] = ('Programs', f'{len(PG.P)} programs built and used by Songgol Lab — Drive Console, Central Control, 3D Print Bench, Butler Robot, home IoT and more.', 'projects',
                            ph + g['sec'](filt + cat + note, cls='tight') + g['band']('See something you like?', 'Want to try one, or build something similar? Drop me a line.', btn(f'mailto:{MAIL}', 'Email me')), 'en', PG.FILTER_JS)

    # ---------------------------------------------------------------- about
    boxes, sec, log = g['boxes'], g['sec'], g['log']
    PAGES['en/about'] = ('About', 'Songgol Lab started building in October 2026. I use what I make at home and at our shop, fix it as I go, and only polish into products the things that prove useful.', 'about',
     ehero('About', 'About Songgol Lab', 'Built by hand,<br>used for real, then proven',
               'Songgol Lab started building in October 2026. I use what I make at home and at our shop, fix it as I go, and only polish into products the things that prove useful.')
     + sec('''<div class="g2" style="align-items:center;gap:32px"><div style="background:radial-gradient(circle at 50% 35%,#1B2B4D,#0A1428 70%);border-radius:24px;padding:44px"><img class="logo-full" src="/assets/logo-full.png" alt="Songgol Lab logo — a symbol where the Korean letters ㅅ and ㄱ interlock"></div>
<div><span class="eyebrow">Name and symbol</span><h2>Songgol, the name of my home village</h2><p class="p">Songgol is the village I come from. I started building home-IoT screens there, and the symbol interlocks <b>ㅅ</b> and <b>ㄱ</b>, the first letters of Song and Gol in Korean.</p></div></div>''', cls='tight')
     + sec(boxes([('We use it first', 'Everything runs in our own house and shop first, and gets fixed before it goes public.'), ('We show it as it is', 'Real scope and real development stage, not inflated numbers.'), ('We keep refining', 'Features and screens keep improving from what users tell us.')], 3, True),
           '', 'How I work', 'Technology proves itself in real use', cls='alt')
     + sec('''<div class="steps"><div><b>Define the problem</b><span>Why is it needed?</span></div><div><b>Plan</b><span>What to build</span></div><div><b>Design</b><span>How it will be used</span></div><div><b>Review</b><span>Lock the criteria</span></div><div><b>Build</b><span>Develop features</span></div><div><b>Use it for real</b><span>Find bugs and friction</span></div><div><b>Improve · decide</b><span>Product or not</span></div></div>
<p class="p" style="margin-top:16px">Then back to step one — the loop keeps running while I use it.</p>''', '', 'The process', 'It always starts with “why”')
     + sec(log([('2026.10', 'Started building', 'Home-IoT screens and the La Grills Hub in daily use'), ('2026.10', 'Airang launched', 'Started in Yongin, then Gyeonggi, Seoul, Incheon and Chungnam'), ('2026.11', 'Registered as a business', 'Drive Console Google Play testing, songgollab.co.kr launched')]), '', 'So far', 'The road so far', cls='tight')
     + g['band']('Let’s talk', 'Feedback, tech talk or collaboration ideas are all welcome.', btn(f'mailto:{MAIL}', 'Email me')), 'en')
