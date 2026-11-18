# -*- coding: utf-8 -*-
"""English version (/en/). build.py가 불러 씁니다.
한국어 페이지와 같은 구조를 영어로 만듭니다. 새 영문 페이지를 만들면 EN_PAGES 에 한국어 slug를 넣으세요."""

NAV = [('log', 'Work log'), ('projects', 'Programs'), ('services', 'Try it'), ('consulting', 'Semiconductor'), ('about', 'About')]
CATS = [('all', 'All'), ('svc', 'Public services'), ('iot', 'IoT · Automation'), ('ops', 'Ops · AI tools'), ('biz', 'Commerce · Trading R&D'), ('plan', 'In planning')]

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

EN_PAGES = {'index', 'projects', 'about', 'log', 'consulting', 'services', 'videos',
            'iot-guide', 'project-drive', 'airang', 'project-home-iot',
            'project-control', 'program-printbench', 'project-robot', 'program-ai-team',
            'program-sns', 'program-login', 'program-invest', 'program-lagrills',
            'project-farm', 'project-commerce', 'program-trader', 'program-booking'}


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
  <a class="try rv" href="/en/airang"><div class="im" style="background-image:url('/assets/airang-phone.jpg');background-position:top"></div>
    <div class="tx"><span class="badge">Public service</span><h3>Airang</h3><p>Local info for families with kids in 63 towns in Korea, refreshed every morning on one screen. No sign-up.</p><span class="go">Explore Airang →</span></div></a>
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
  <div class="cta" style="display:flex;gap:10px;margin-top:22px;flex-wrap:wrap">{btn('/en/consulting', 'Read more →')}</div></div>
  <div><div class="panel"><div class="panel-head"><span>WAFER MAP · INSPECTION</span><b>● ANALYZING</b></div>{H.wafer_svg().replace('웨이퍼 맵 일러스트', 'Wafer map illustration')}<span class="panel-note">Illustration only · not real data</span></div></div>
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
    note = ''
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

    add_remaining(g)


# English content follows the current Korean source. Implementation details are
# deliberately shortened where the public disclosure rules require it.
ED = {
 'program-lagrills': dict(
  lead='I control the air conditioners across BBQ sites 1–9, guest rooms and the shop at La Grills from one counter PC. This was the first project I took from our home into a working business.',
  why='Before guests arrived, someone had to walk around with a remote and switch on each zone. After checkout, someone had to check again. It was easy to miss one during busy hours.',
  feats=[('Each zone on one screen', 'Switch the air conditioning for BBQ sites, guest rooms and the shop on or off by zone.'), ('Keep the existing equipment', 'The air conditioners stay in place; the hub brings their controls together.'), ('Always at the counter', 'The screen stays open on the shop PC so I can see which zones are on.'), ('Two days, no rewiring', 'Installed without new wiring on October 4, 2026.')],
  flow=[('Choose a zone', 'Open the shop screen'), ('Set the state', 'Turn cooling on or off'), ('Check', 'See the zone status')],
  log=[('2026.10.04', 'Hub v2.6 installed', 'Brought the zones together on the counter PC.'), ('Next', 'Lighting and booking schedules', 'Plans include lighting, scheduled preparation and power monitoring.')]),
 'project-control': dict(
  lead='Central Control (SONGGOLLAB HUD) brings my home, work and programs onto one screen. Connected programs appear as cards around an AI core, and I can ask questions or give commands by voice.',
  why='Home IoT, trading experiments, social channels, 3D printing and AI tools each had their own window. I wanted one place to see what was running, what had stopped and what needed attention.',
  feats=[('A card for each program', 'Connection status and one key figure stay visible. Open a card for more detail.'), ('Connected programs together', 'Newly connected programs appear on the board; I can hide cards I do not need.'), ('Voice or text', 'Ask about a program or give a command without switching windows.'), ('Confirm important actions', 'Actions such as starting or stopping a print ask for confirmation.'), ('Project overview', 'See development stages, sign-in issues, expiry dates and subscriptions.'), ('Phone and full screen', 'Use the same board on a phone or show it full screen on a monitor.')],
  flow=[('Connect', 'Bring programs onto the board'), ('See', 'Check status cards'), ('Ask', 'Use voice or text'), ('Confirm', 'Review important actions')],
  log=[('v1.13', 'Device overview', 'Brought several PCs and devices onto one board.'), ('v1.14–1.15', 'Mail view', 'Read and organise mail within the board.'), ('v1.16', 'Rooms at a glance', 'Added current home status by room.'), ('v1.17', 'Screen and news', 'Added visual effects and a news card.'), ('v1.19.8', '15 programs and an introduction video', 'Connected printing, AI tools, social channels and app-release status. Video published November 17, 2026.')],
  note='These are screens from daily use. Personal amounts and mail names are hidden. Connection details and security settings are not published. Stock figures are examples from a simulation account.'),
 'program-printbench': dict(
  lead='A Windows program I built to watch and manage my 3D printer from one screen. It brings together print status, queued jobs, slicing, filament tracking and checks, on the home network without a cloud service.',
  why='A print can take hours. I kept walking to the printer or switching between its screen and the slicer. I started this program the day I brought home a used printer.',
  feats=[('Live monitoring', 'See progress, time remaining, estimated completion and temperature graphs, with a 3D view of the print path.'), ('Queue and slicing', 'Queue files and prepare models for printing in one place.'), ('Preview before printing', 'Review the layout, sliced result, first layer and layer paths.'), ('Printers and filament', 'Manage more than one printer and keep track of filament remaining.'), ('Checks and calibration', 'Bring routine checks and calibration into one screen.'), ('Quiet nights and idle power', 'Use a quieter night mode and turn off idle equipment. View a connected camera.')],
  flow=[('Add a file', 'Choose a model or print file'), ('Preview', 'Review the prepared result'), ('Check', 'Review printer and material compatibility'), ('Confirm', 'Make sure the bed is clear'), ('Monitor', 'Follow progress and completion')],
  safety_title='Checks before a print starts',
  safety=[('Material', 'Warns about a mismatch between the file and loaded filament.'), ('Temperature', 'Checks whether the planned temperatures suit the material.'), ('Printer and nozzle', 'Checks printer and nozzle compatibility.'), ('Filament remaining', 'Warns if the roll may not have enough material.'), ('Bed edges', 'Flags first-layer paths near the bed boundary.'), ('A clear reason', 'Explains why a start was blocked and records any confirmed override.')],
  env='Windows 10/11, 64-bit. Tested with a Creality K1 on stock firmware. Support for other printers is in preparation. The PC and printer use the same home network; automatic slicing requires OrcaSlicer.',
  log=[('v0.4', 'First connection', 'Started with monitoring on the day the used K1 arrived.'), ('v0.9', 'Queue, checks and calibration', 'Added slicing, start checks, self-checks and quiet night printing.'), ('2026.11', 'Central Control and video', 'Added a status card and published a 90-second introduction.')],
  note='Creality, K1, Bambu Lab, OrcaSlicer and Printables are trademarks of their respective owners. This is an independent program. Printer addresses in the images are examples.'),
 'project-robot': dict(
  lead='I am turning a broken robot vacuum and an unused 3D printer into a home robot that comes when called and carries water. The target for new parts is about KRW 100,000. Design is complete; measurements have just started.',
  why='A worn wheel gear stopped a Samsung Jet Bot AI, but much of the machine was still usable. An old 3D printer was also sitting idle. I wanted to reuse them for a robot that could fit into our home IoT setup.',
  feats=[('Comes when called', 'The goal is to travel to the person calling it.'), ('Carries a cup', 'A tray is planned for small deliveries such as water.'), ('A tablet face', 'A tablet provides the face and interaction screen.'), ('Adjustable height', 'The design stays low while moving and raises the screen when stopped.'), ('Reused vacuum base', 'Keeps useful parts from the broken robot vacuum.'), ('Reused printer parts', 'Uses parts from an old printer to reduce new purchases.')],
  flow=[('Measure', 'Current stage'), ('Inspect', 'Check the donor equipment'), ('Test', 'Confirm reusable parts'), ('Build', 'Assemble the lift'), ('Move', 'Test travel at home'), ('Interact', 'Add tablet and delivery functions'), ('Finish', 'Check charging and safety')],
  safety_title='Design priorities',
  safety=[('Clear sensing', 'Keep the surroundings visible to the robot.'), ('Stable movement', 'Keep the moving body low.'), ('Balance', 'Check stability before raising the screen.'), ('Safe stopping', 'Plan for lost connections, obstacles and drops.'), ('Covered moving parts', 'Protect hot and moving components.'), ('Check before spending', 'Inspect critical donor parts before buying more.')],
  env='New-parts target: about KRW 90,000–100,000, reduced from the first estimate by reusing available parts. Purchases follow checks at each stage. An existing home PC and tablet are planned for use.',
  log=[('2026.11', 'First idea', 'A small home robot with a tablet and cup tray.'), ('2026.11.17', 'First short video', 'Could a broken robot vacuum become a butler robot?'), ('2026.11.18', 'Design complete; measurements begin', 'Confirmed the reuse plan. Next is inspecting the Jet Bot.')],
  note='Dimensions, height, balance and cost are estimates that will change after measurement. Some 3D images show earlier concepts. These are plans, not a finished working robot.'),
 'program-ai-team': dict(
  lead='An internal workshop for producing writing, video and code with AI support. I can review work and follow its progress from a PC or phone.',
  why='I needed to keep making things while managing usage and cost. This workshop helps me keep the work, review and results in one place.',
  feats=[('Project workspace', 'Keep requests and results together by project.'), ('Private material', 'Handle sensitive material with care.'), ('Everyday conversation', 'Use the same workspace for quick questions.'), ('Review before publishing', 'Review a video before approving a social post.'), ('Work log', 'See what was done and where a task stopped.'), ('PC and phone', 'Follow the work from either device and from Central Control.')],
  flow=[('Request', 'Describe the result I need'), ('Work', 'Follow progress'), ('Review', 'Check and revise'), ('Approve', 'Accept the result')],
  log=[('v4.4', 'Connection checks', 'Improved diagnosis of connection and permission problems.'), ('v4.5', 'Video review and publishing', 'Brought creation, approval and publishing into one workspace.'), ('v4.6', 'Workflow trial', 'Started a two-week trial of a revised workflow.')]),
 'program-sns': dict(
  lead='I manage Songgol Lab’s Instagram, Threads and blog in one program: writing, scheduling, checking reactions and finding useful topics.',
  why='Opening each channel separately to post and check its numbers was taking too much time.',
  feats=[('Channel overview', 'See visits and reactions in figures and charts.'), ('Write and schedule', 'Adapt a post for each channel and schedule it.'), ('Photo posts', 'Prepare posts from my photos.'), ('Publishing queue', 'Keep planned posts in order.'), ('Popular posts', 'Use the response to earlier posts when choosing the next topic.'), ('Central Control', 'See channel status on the main board.')],
  flow=[('Draft', 'Prepare words and photos'), ('Edit', 'Fit the channel'), ('Schedule', 'Choose a publishing time'), ('Review', 'See how the post did')],
  log=[('v0.4', 'Writing and scheduling', 'Added the basic publishing workflow.'), ('v0.5', 'Photo posts', 'Added photo-based posts.'), ('v0.6', 'Central Control', 'Added channel status on the board.')],
  note='Account passwords are not stored in this program. Connection credentials remain on the PC.'),
 'program-login': dict(
  lead='An internal Chrome extension that shows sign-in and credential expiry status for more than 60 sites used across 11 projects. It alerts me when a connection drops.',
  why='Several overnight jobs stopped because a login had expired. I built a board that helps me find the broken connection before spending time looking for a code bug.',
  feats=[('Problems first', 'Sites needing attention appear above healthy connections.'), ('What needs attention now', 'Important connections have a clear place on the board.'), ('Toolbar summary', 'Check the summary from Chrome and receive desktop alerts.'), ('Sign-in notes', 'Keep reminders about sign-in methods without storing passwords.'), ('Important accounts', 'Pin key accounts for early attention.'), ('Expiry calendar', 'See approaching credential and trial expiry dates.')],
  flow=[('Overview', 'See connection status'), ('Alert', 'Notice a problem'), ('Open', 'Check the affected service'), ('Confirm', 'Mark the review complete')],
  log=[('v1.0', 'First version', 'Dashboard, toolbar summary, sign-in notes and expiry calendar.'), ('Next', 'Central Control', 'Plans for status and voice alerts on the board.'), ('Next', 'Broader desktop checks', 'Plans to cover more desktop tools and projects.')],
  note='The board stores no passwords or API key values. It reports status; it does not enter passwords or silently extend sessions. Screens show example states. This is currently an internal Chrome extension.'),
 'program-invest': dict(
  lead='A Windows program that organises AliExpress and Gmarket purchases by project and shows monthly spending at a glance. I mainly review the entries that need a decision.',
  why='With several DIY and IoT projects running together, I stopped remembering which project a part belonged to or how much I had spent. I wanted to see the totals without copying every order into a spreadsheet.',
  feats=[('Dashboard', 'Filter by month, project and shop. Correct a project directly in the purchase list.'), ('Analysis in plain words', 'See spending trends, month-end estimates and accumulated costs.'), ('Project budgets', 'Compare spending with a monthly budget and review large purchases.'), ('Regular updates', 'Keep the purchase list current without duplicate or cancelled orders.'), ('Central Control', 'See totals, entries needing review and budget warnings on the board.'), ('For makers', 'Designed around several DIY projects and frequent parts purchases.')],
  flow=[('Update', 'Bring purchases into the list'), ('Review', 'Confirm project categories'), ('See totals', 'Check spending and budgets')],
  log=[('v1.0', 'First version', 'Dashboard, project categories and Central Control.'), ('v1.1', 'Analysis', 'Added estimates, plain-language summaries and budgets.'), ('v2.0', 'Windows installer', 'Added installation and regular data updates.')],
  note='Screens illustrate the features. All displayed amounts are example data.'),
 'project-commerce': dict(
  lead='Ali Sourcing Helper is a Windows program for reviewing overseas product candidates and preparing listing drafts for Naver Smart Store, including names, prices and introductory posts.',
  why='Finding a product, editing its description, working out a price and writing a post meant repeating the same preparation each time.',
  feats=[('Product review', 'Compare candidate products, prices, shipping and reviews.'), ('Eligibility review', 'Flag items that need attention before a listing is prepared.'), ('Listing names', 'Draft clearer product names.'), ('Margin view', 'Review costs and estimated margin.'), ('Categories', 'Prepare a suitable listing category.'), ('Introductory posts', 'Draft a blog introduction for a product.')],
  flow=[('Review', 'Look at product candidates'), ('Check', 'Review suitability'), ('Prepare', 'Edit the listing draft'), ('Publish', 'Use the reviewed result')],
  log=[('v1.x', 'First marketplace version', 'Started with a Coupang-focused version, ending at v1.9.1.'), ('v2.0', 'Naver version', 'Moved the project to Naver Smart Store.'), ('v2.1', 'Listing refinements', 'Improved product names, margin review and daily operation.')],
  note='Used within applicable sales and customs rules. Customer customs identifiers are not stored in the program.'),
 'program-trader': dict(
  lead='A private Windows project that brings my stock and cryptocurrency experiments onto one screen. It combines views for Kiwoom simulation, Toss stocks and Upbit crypto. My own private tool — not for sale.',
  why='Separate stock and crypto programs meant two sets of windows and reviews. I brought the views together so I could follow them in one place.',
  feats=[('Market dashboard', 'Switch between stock and crypto views.'), ('Charts and trades', 'Review charts, market activity and recorded trades.'), ('Performance view', 'See returns, asset trends and daily results by market.'), ('Daily review', 'Look back at the day’s trades.'), ('Records', 'Review observations and completed trades.'), ('Manual choice', 'Keep control over how each holding is managed.'), ('Risk settings', 'Review account connections and risk limits.')],
  flow=[('Watch', 'Follow each market'), ('Review', 'Look at current activity'), ('Manage', 'Check holdings and limits'), ('Reflect', 'Review the day')],
  safety_title='Controls for a personal experiment',
  safety=[('No withdrawals', 'There is no withdrawal function.'), ('Risk limits', 'Limits are part of the experiment.'), ('Duplicate-run checks', 'Avoid running the same market task twice.'), ('Confirm changes', 'Review changes before applying them.'), ('Emergency controls', 'Keep stop controls within reach.'), ('Separate accounts', 'Keep simulation and live-account views distinct.')],
  log=[('Stock v0.4', 'Stock project', 'Developed and checked with a simulation account.'), ('Crypto v0.3', 'Crypto project', 'Developed the separate crypto view.'), ('v0.3.0', 'Combined as Songgol Trader', 'Brought the dashboard and daily review into one program in November 2026.')],
  env='Windows 10/11, 64-bit. Connection credentials are protected on the local PC.',
  note='My own private tool — not for sale. Screens use example data. Trading rules, scores, timing and account connection details are not published.'),
 'project-farm': dict(
  lead='A planned experiment bringing home IoT to the family farm. The goal is a small, self-built greenhouse of about 17–20 m², with temperature and humidity visible from home.',
  why='I had to visit the field to find out whether the greenhouse was getting too hot or too cold.',
  feats=[('Greenhouse status', 'Check temperature and humidity on a phone, with alerts for unusual conditions.'), ('One home view', 'See the greenhouse alongside the house.'), ('Use it first', 'Test it in our own field before deciding what is useful enough to offer.')],
  flow=[('Observe', 'Check greenhouse conditions'), ('Review', 'See them from home'), ('Respond', 'Receive an alert and take action')],
  log=[('2026.10', 'Project registered', 'Planned a farm experiment linked to home IoT.'), ('Next', 'Build the greenhouse', 'Start with a small arched greenhouse.')]),
 'program-booking': dict(
  lead='A family booking assistant concept. Describe a trip in ordinary words, compare numbered options for flights, trains, stays, cars and restaurants, and approve only the bookings you choose.',
  why='Planning a trip meant switching between five or six apps just to compare the options.',
  feats=[('Ask in plain words', 'Describe dates, people and budget.'), ('Choose by number', 'Select an option from a numbered list.'), ('Connected plans', 'See suggestions that fit arrival times and the rest of the trip.'), ('Final approval', 'Bookings and payments proceed only after approval.')],
  flow=[('Request', 'Speak or type'), ('Compare', 'Review travel options'), ('Choose', 'Pick a numbered option'), ('Approve', 'Confirm the selected booking')],
  log=[('v0.1', 'Screen concepts', 'Prepared 12 mobile, voice and desktop mock-ups.'), ('Next', 'Refine the mock-ups', 'Bring the desktop screens into the same style.')],
  note='This project is at the mock-up stage; booking functions are planned.'),
}


def ehref(slug):
    if slug == 'drive-console':
        return '/drive-console-en'
    return '/en/' + ('' if slug == 'index' else slug)


def en_detail(g, slug):
    import programs as PG
    from html import escape
    d = ED[slug]
    p = next(x for x in PG.P if x[0] == slug)
    name, status, platform, one = EP[slug]
    category = dict(CATS)[p[2]]
    version = 'Stage 0' if p[6] == '0단계' else p[6]
    chips = f'<span>{status}</span><span>{platform}</span>'
    if version != '—': chips += f'<span>{version}</span>'
    chips += f'<span>{category}</span>'
    body = f'''<section class="page-hero"><div class="wrap"><div class="crumb"><a href="/en/">Home</a> › <a href="/en/projects">Programs</a> › <span>{name}</span></div><span class="eyebrow">{category}</span><h1>{name}</h1><p class="lead">{d['lead']}</p><div class="pmeta">{chips}</div></div></section>'''
    items = [('feat', 'Features'), ('how', 'How it works')]
    if d.get('safety'): items += [('safe', 'Safety')]
    if PG.G.get(slug) or not PG.V.get(slug): items += [('gallery', 'Gallery')]
    if PG.V.get(slug): items += [('video', 'Video')]
    if PG.R.get(slug): items += [('docs', 'Resources')]
    items += [('log', 'Development log')]
    body += g['toc'](items).replace('이 페이지 목차', 'On this page')
    images = PG.G.get(slug, [])
    if images:
        cover_index = 1 if slug == 'program-ai-team' else 0
        src = images[cover_index][0]
        cap = media_caption(slug, cover_index)
        side = f'<figure class="fig" style="margin:0"><img src="{src}" alt="{escape(cap, quote=True)}" loading="lazy"><figcaption class="cap"><span>{cap}</span></figcaption></figure>'
    else:
        c1,c2,ic,ph = p[8]
        side = f'<div class="prog" style="pointer-events:none">{PG.art(c1,c2,ic,ph)}</div><div class="tx"><span class="cat">ONE LINE</span><p>{one}</p></div></div>'
    body += g['sec'](f'<div class="split"><div><span class="eyebrow">Why I built it</span><h2>It started with a small annoyance</h2><p class="p">{d["why"]}</p></div><div>{side}</div></div>', cls='tight')
    body += g['sec'](g['boxes'](d['feats'], 2 if len(d['feats']) == 4 else 3), 'feat', 'Features', 'What it does', cls='alt')
    body += g['sec'](g['boxes'](d['flow'], min(len(d['flow']), 3), True), 'how', 'How it works', 'How I use it')
    if d.get('safety'):
        body += g['sec'](g['boxes'](d['safety'], 3), 'safe', 'Safety', d['safety_title'], cls='alt')
    if d.get('env'):
        body += g['sec'](g['note']('<b>Requirements and setup</b> · ' + d['env']), cls='tight')
    body += en_media(g, slug)
    body += g['sec'](g['log'](d['log']) + (g['note'](d['note'], True) if d.get('note') else ''), 'log', 'Development log', 'How it got here', cls='alt')
    body += g['band']('See the other programs', 'Programs I build and use at Songgol Lab.', g['btn']('/en/projects', 'All programs') + g['btn']('mailto:' + g['MAIL'], 'Email me', 'ghost'))
    return body


MEDIA_CAPTIONS = {
 'project-control': ['Main screen — connected programs around the AI core (v1.19.8)', 'Program cards — status and key figures', 'Songgol Home — room status', '3D printer — progress and temperatures', 'AI Team — current work and review status', 'Social Media Hub — channel overview', 'Other connected programs', 'Connections and card visibility', 'Voice commands and confirmation cards'],
 'program-printbench': ['Live print monitoring', 'Queue, layout and first-layer preview', 'Printer overview', 'Checks and filament status', 'Model browser', 'Printer and camera settings', 'Checks before starting a print', 'Calibration and self-check', 'Quiet night printing'],
 'project-robot': ['Current assembly concept', 'Raised-screen concept — estimated dimensions', 'Parts overview — mostly reused equipment', 'Body layout concept', 'The broken Samsung Jet Bot AI', 'The unused 3D printer', 'Printer parts planned for reuse', 'Early concept — tablet and cup tray', 'Early concept — clear sensor view', 'Early concept — lowered lift', 'Early concept — raised lift'],
 'program-ai-team': ['AI workshop overview', 'Home screen — recreated example', 'Project workspace', 'Phone screen'],
 'program-login': ['Dashboard — example connection states', 'Chrome toolbar summary', 'Sign-in reminders', 'Credential expiry calendar'],
 'program-invest': ['Spending dashboard — example data', 'Budgets and analysis — example data', 'Regular purchase updates'],
 'program-trader': ['Stock dashboard — example data', 'Crypto dashboard — example data', 'Market charts', 'Returns and asset trends — example data', 'Daily trade review', 'Results analysis', 'Observation records', 'Trade records — example data', 'Holdings overview', 'Connection settings — empty input fields', 'Risk settings'],
 'project-commerce': ['Listing draft — product name, margin and eligibility review'],
 'project-home-iot': ['Home screen — rooms, energy and devices', 'Scenes and home automation', 'Energy overview', 'Radio and sleep timer'],
 'airang': ['Airang on a phone'],
 'drive-console': ['Tablet home screen', 'Phone home screen', 'Vehicle information'],
}

# These existing Korean assets expose internal workflows or configuration values.
# Keep them in the source gallery; do not duplicate them on the English pages.
PRIVATE_MEDIA = {
    ('program-ai-team', 0), ('program-invest', 2),
    ('program-printbench', 5), ('program-printbench', 6), ('program-printbench', 8),
    ('program-trader', 5), ('program-trader', 9), ('program-trader', 10),
}


def media_caption(slug, index):
    return MEDIA_CAPTIONS[slug][index]


def en_media(g, slug, with_video=True):
    import programs as PG
    from html import escape
    body = ''
    images = PG.G.get(slug, [])
    if images:
        cells = []
        for i,x in enumerate(images):
            # Do not republish workflow diagrams that describe internal recipes.
            if (slug, i) in PRIVATE_MEDIA:
                continue
            cap = media_caption(slug, i)
            tall = ' tall' if len(x) > 2 else ''
            cells.append(f'<figure class="gi{tall}"><a href="{x[0]}" target="_blank" rel="noopener"><img src="{x[0]}" alt="{escape(cap, quote=True)}" loading="lazy"></a><figcaption>{cap}</figcaption></figure>')
        body += g['sec']('<div class="gal">' + ''.join(cells) + '</div>', 'gallery', 'Gallery', 'A look at the screens', cls='white-sec')
    videos = PG.V.get(slug, []) if with_video else []
    if videos:
        body += g['sec']('<div class="vids">' + ''.join('<div>' + g['yt'](vid, EP[slug][0] + ' · ' + ('Introduction' if i == 0 else f'Video {i+1}')) + '</div>' for i,(vid,_) in enumerate(videos)) + '</div>', 'video', 'Video', 'Watch the project')
    resources = []
    for href,_,_ in PG.R.get(slug, []):
        if href.startswith('/'):
            target = href.strip('/')
            href = ehref(target)
            label = EP[target][0] if target in EP else {'iot-guide':'Home IoT explained', 'project-drive':'Drive Console development log', 'drive-console-privacy':'Privacy policy'}.get(target, 'Read more')
            if target == 'drive-console-privacy': href = '/drive-console-privacy#privacy-en'
            desc = 'Project details'
        elif 'instagram.com' in href:
            label,desc = 'Instagram ↗', 'Watch the project video'
        elif 'youtube.com' in href:
            label,desc = 'YouTube ↗', 'Watch the introduction'
        elif href == 'https://airang.songgollab.co.kr':
            label,desc = 'Open Airang ↗', 'Choose your town'
        else:
            label,desc = 'Songgol Lab blog ↗', 'Project stories in Korean'
        resources.append(f'<a href="{href}"' + (' target="_blank" rel="noopener"' if href.startswith('http') else '') + f'><span class="ri" aria-hidden="true">↗</span><b>{label}</b><em>{desc}</em></a>')
    if resources:
        body += g['sec']('<div class="res">' + ''.join(resources) + '</div>', 'docs', 'Resources', 'More about the project')
    if not images and not videos:
        body += g['sec'](g['note']('Screens and videos will be added as they are ready. Internal projects show only material cleared for public viewing.', True), 'gallery', 'Gallery', 'A look at the screens', cls='tight')
    return body


def add_remaining(g):
    for slug,d in ED.items():
        g['PAGES']['en/' + slug] = (EP[slug][0], d['lead'], 'projects', en_detail(g, slug), 'en')
    add_other_pages(g)


# Exact text-node translations preserve the layout of the hand-built pages.
# A missing translation raises an error rather than publishing mixed languages.
TEXT = {}
def translations(pairs):
    for line in pairs.strip().splitlines():
        ko, english = line.split('|', 1)
        TEXT[ko] = english


translations('''
홈|Home
프로젝트|Programs
프로그램|Programs
아이랑|Airang
드라이브 콘솔|Drive Console
홈 IoT|Home IoT
서비스|Try it
영상|Videos
이 페이지 목차|On this page
송골랩 영상|Songgol Lab video
주요 기능|Features
왜 만들었나|Why I built it
운영 방식|In daily use
개발 일지|Development log
개발 이력|Version history
로드맵|Roadmap
실제 화면|Live view
구성|Overview
실증 현장|In daily use
화면 둘러보기|Screen tour
진단|Vehicle information
화면으로 보기|A look at the screens
영상으로 보기|Watch the project
설명 자료|Resources
어떻게 만들어 왔나|How it got here
이렇게 돌아갑니다|How I use it
버전별 정리|Version history
버전|Version
추가된 것|What changed
다음|Next
유튜브|YouTube
의견 보내기|Send feedback
문의하기|Email me
설치 상담 문의|Email me
테스터 신청하기|Join the test
테스터 신청|Join the test
사용 안내 보기|Read the guide
자세히 보기|Read more
자세히 보기 →|Read more →
아이랑 열기 ↗|Open Airang ↗
새 창에서 열기 ↗|Open in a new tab ↗
경기|Gyeonggi
서울|Seoul
인천|Incheon
충남|Chungnam
학교 일정|School calendar
아이와 함께 가요|Things to do with kids
도서관|Libraries
유치원 찾기|Kindergartens
학원 찾기|After-school classes
수강료 비교|Class fees
엄마 일자리|Local jobs for parents
특목·자사고|High-school admissions
자동 갱신|Regular updates
매일 아침 새 정보로|Fresh information each morning
웹앱|Web app
개발 이력 · 로드맵|History and roadmap
앞으로의 계획|Plans ahead
단계|Stage
내용|Details
구상|First idea
수집기|Daily updates
웹앱 공개|Web app launch
1단계|Stage 1
2단계|Stage 2
3단계|Stage 3
한 화면에서 집 전체를|The whole house on one screen
송골집 IoT · AI 월패드|Songgol Home IoT · AI wall pad
IoT, 쉽게 알아보기|Home IoT explained
IoT, 쉽게 알아보기 →|Home IoT explained →
홈 · 방 라이브|Home and rooms
3D 평면도|3D floor plan
가족지킴이|Family view
에너지|Energy
자동화|Automation
자비스 음성 비서|Voice assistant
가전 관리|Appliances
I/O 체크|Device checks
설정 공유|Shared settings
집 안 서버|Home hub
관리 화면|Home screen
태블릿 · 휴대폰|Tablet and phone
직접 써 보며 검증합니다|Tested in everyday use
송골집 (우리 집 2층)|Songgol Home — upstairs at our house
라그릴스 셀프 바베큐장|La Grills self-service BBQ
라그릴스 허브 v2.6 소개|La Grills Hub v2.6 introduction
셀프 바베큐장 라그릴스 소개|A look at La Grills
라그릴스 설치기 전체 글 보기 →|Read the La Grills installation story →
라그릴스 v2.6|La Grills v2.6
Images · 이미지|Gallery
Docs · 자료|Resources
Video · 영상|Video
실시간 계기판|Live dashboard
고장 코드 설명|Fault code explanations
분할 화면 · 음성|Split screen and voice
학교 일정 · 급식|School calendar and meals
도서관 · 유치원|Libraries and kindergartens
학원 수강료 비교|Class fee comparisons
병원 · 혜택 · 행사|Clinics, benefits and events
차례로 늘어나는 중|More towns are being added
공개 서비스 · 무료|Public service · Free
송골랩 유튜브|Songgol Lab on YouTube
▶ 채널 구독하기|▶ Subscribe on YouTube
드라이브 콘솔 · 3편|Drive Console · 3 videos
아이랑 · 9편|Airang · 9 videos
IoT 이야기 · 5편|Home IoT · 5 videos
실증 현장 · 2편|In daily use · 2 videos
30초 소개|30-second introduction
기능 설명|Feature tour
쇼츠|Shorts
소개|Introduction
테스터 모집|Testers wanted
IoT 이야기|Home IoT stories
허브|Hub
현장|On site
드라이브 콘솔 30초 소개|Drive Console in 30 seconds
드라이브 콘솔 v1.3 설명|Drive Console v1.3 tour
아이랑 경기|Airang in Gyeonggi
아이랑 서울 25개 구|Airang in Seoul’s 25 districts
아이랑 충남 오픈|Airang launches in Chungnam
아이랑 용인|Airang in Yongin
아이랑 수원|Airang in Suwon
아이랑 성남|Airang in Seongnam
아이랑 안양|Airang in Anyang
아이랑 고양|Airang in Goyang
아이랑 화성|Airang in Hwaseong
IoT가 뭐예요?|What is IoT?
설치하면 뭐가 좋아질까?|What changes at home?
스마트홈의 하루|A day in a smart home
켜져 있는 줄도 몰랐던 전기|The power you did not know was on
멀리 계신 부모님 댁|Looking after parents from afar
좋아지는 5가지|Five everyday benefits
새는 전기 막기|Reducing wasted power
부모님 댁 안심|Checking on parents
송골랩은 이렇게|How I approach it
감지|Sense
전달|Connect
판단|Decide
동작|Act
편리|Convenience
절약|Savings
안전|Safety
원격|Remote access
자동|Automation
07:00 기상|07:00 · Wake up
하루를 시작합니다|Start the day
외출|Going out
한 번에 끄기|Turn things off together
낮|During the day
빈집 알림|An alert from home
퇴근길|On the way home
미리 켜기|Prepare the room
23:00 취침|23:00 · Bedtime
자동으로 끄기|Lights off automatically
찾기 · 사용량 화면|See energy use
막기 · 자동 규칙|Reduce waste
연기 · 누수|Smoke and leaks
문 열림|Doors
온도|Temperature
생활 리듬 알림|Changes in routine
원격 난방|Remote heating
송골랩의 방식|My approach
송골랩은 이렇게 합니다|How I approach it
공사 없이|No rewiring
우리 집 안 서버|A hub at home
KC 인증 장비|KC-certified equipment
홈 IoT 프로젝트|Home IoT project
드라이브 콘솔 개발 기록|Drive Console development log
6 화면|6 screens
약 1만|About 10,000
3종|3 fuel types
30초로 보는 드라이브 콘솔|Drive Console in 30 seconds
3분 만에 보는 v1.3|A three-minute tour of v1.3
실제 앱 화면|Screens from the app
메인 화면 — 운전에 필요한 것만 크게|Home screen — key information at a glance
계기판 디자인 6가지 + 기본형|Six dashboard designs plus the standard view
분할 화면 — 왼쪽 T맵 + 오른쪽 앱|Split screen — TMAP and another app
음성 비서|Voice assistant
차계부|Car log
설정|Settings
차량 진단|Vehicle information
값을 상황에 맞게 판정|Information in context
차량 정보 (2017 올뉴K7 3.0 LPi)|Vehicle information — 2017 Kia K7 3.0 LPi
고장 코드: 뜻에서 조치 순서까지|Fault codes — from meaning to checks
읽기|Read
뜻 찾기|Explain
당시 상황|Context
조치|Checks
v1.3 새 기능: 연료에 맞춘 진단|New in v1.3 — fuel-specific information
디젤 차량 예시 (2019 현대 싼타페)|Diesel example — 2019 Hyundai Santa Fe
가솔린|Petrol
디젤|Diesel
LPi|LPi
차량 – 동글 – 태블릿|Car, dongle and tablet
차량 ECU|Vehicle ECU
OBD 동글|OBD dongle
드라이브 콘솔 앱|Drive Console app
태블릿 안에서 처리|Processed on the tablet
품질 점검 — 누를 수 있는 건 다 눌러 봤어요|Quality checks — testing the controls
75개|75
7가지|7
2,852개|2,852
반도체 세정 공정|Semiconductor wet-clean equipment
반도체 세정 공정 · 설비 엔지니어링|Semiconductor process and equipment engineering
해 온 일 보기 →|See my experience →
Experience · 현장에서 자주 만난 일|Experience
현상은 보이는데|The symptoms were visible,
원인이 잡히지 않던 일들|but the cause was not
Areas · 해 온 일|Areas of experience
직접 해 온 일들|Work I have done
세정장비 불량 원인 추적|Root-cause investigation
스케줄러 · 시퀀스 로직 검토|Scheduling and sequence review
공정 데이터 분석 도구|Process-data tools
평가 자동화 (구상)|Evaluation automation — ideas in progress
Process · 진행 순서|My approach
추측 대신,|Evidence I could reproduce,
재현되는 근거로|rather than guesswork
현상 관찰|Observe
언제·어디서·얼마나|When, where and how often
데이터 수집|Review the evidence
로그·레시피·이력|Logs and history
가설 분리|Separate possible causes
SW·HW·시퀀스·제어|Software, hardware, sequence and control
검증|Verify
조건을 바꿔 재현|Check reproducibility
기준 확정|Agree on criteria
합격선과 관리값|Clear acceptance criteria
이관|Document
문서화·현장 전달|Record the result for the field team
''')

translations('''
03 · 지역 정보 · 시범 운영|03 · Local information · Pilot service
아이랑 — 우리 동네 아이 정보 한 화면에|Airang — local information for families, on one screen
송골랩이 만든 무료 학부모 정보 서비스 '아이랑'이 경기·서울·인천·충남 63곳으로 넓어졌어요. 우리 아이 학교 일정과 급식(알레르기 표시), 도서관 운영시간과 인기 도서, 유치원 빈자리, 학원 수강료 비교, 동네 의원·약국, 놓치기 쉬운 출산·양육 혜택, 아이와 갈 공연·행사를 한 화면에서 볼 수 있어요. 회원가입이 없고 아이 정보는 휴대폰에만 저장돼요.|Airang is a free service I built for families in Korea, now covering 63 towns and districts across Gyeonggi, Seoul, Incheon and Chungnam. It brings school calendars and meals, libraries, kindergarten places, class fees, clinics, pharmacies, family benefits and events together. No sign-up is needed, and child profiles stay on the phone.
지금 운영 중인 화면 그대로|The service as it runs today
안에서 눌러 보셔도 됩니다.|You can explore the service here.
아이랑 실제 화면|Airang live service
아이랑 서울 25개 구 소개|Airang in Seoul’s 25 districts
부모가 매번 하나씩 찾아 들어가야 했습니다|Parents had to check each source separately
학교 학사일정은 나이스, 공연·축제는 시청, 프로그램과 열람실은 도서관, 유치원 빈자리는 유치원 알리미, 학원 정보와 채용 공고는 또 다른 곳에 있습니다. 아이랑은 이걸 한 화면에 모았습니다.|School calendars, city events, library programmes, kindergarten places, after-school classes and local jobs were scattered across different sites. Airang brings them into one view.
여덟 가지 메뉴|Eight menus
학교 행사를 D-day로 정리|Upcoming school dates at a glance
시청 공연·축제, 도서관 프로그램|City events, festivals and library programmes
열람실 빈자리, 인기 도서|Reading-room availability and popular books
정원·빈자리·통학버스|Places, vacancies and school buses
3,400여 곳 검색, 신고 수강료|Search over 3,400 providers and their reported fees
동네·과목별 학원비 중간값|Compare typical fees by area and subject
학교·유치원·어린이집 채용|Jobs at schools, kindergartens and childcare centres
입시 시기, 지원 가능 학교|Application dates and school options
학원 수업 시작·끝 10분 전에 휴대폰 캘린더로 알려 주는 기능도 함께 있습니다.|Phone calendar reminders are also available before classes begin and end.
매일 아침 자동으로|Fresh each morning
공공 데이터|Local information
나이스·시청·도서관·교육청 등|Schools, community services and events
웹페이지|One web page
새 정보로 바로 바뀝니다|Current information in one view
부모님 휴대폰|On a parent’s phone
링크 하나로 엽니다|Open with a single link
사람 손 없이 매일 아침 새 정보로 바뀝니다. 돈을 벌게 되더라도|The information is refreshed each morning. Even if the service earns revenue, three principles stay the same:
개인정보를 받지 않고, 핵심 정보는 무료로 두고, 광고는 광고라고 밝힌다|no collection of personal information, free core information and clearly labelled advertising
는 세 가지 원칙은 바꾸지 않습니다.|.
2026.10 초|Early October 2026
시작 — 엄마들을 위한 교육 정보|First idea — education information for parents
지역 엄마들을 위한 자녀 교육 정보 모음을 구상했습니다. 대상은 용인으로 정하고, 코딩보다 먼저 어디서 어떤 정보를 모을 수 있는지부터 정리했습니다.|I started with education information for parents in Yongin, defining what would be useful before building the app.
학사일정·행사·도서관·유치원·학원 정보가 매일 아침 자동으로 새로 바뀌게 만들었습니다.|Added daily updates for school dates, events, libraries, kindergartens and classes.
설치 없는 웹앱으로 공개|A web app without installation
앱 설치 없이 링크로 열리는 웹앱(PWA)을 먼저 만들었습니다. 아이 별명·학교는 본인 휴대폰에만 저장됩니다.|Published a web app that opens from a link. A child’s nickname and school stay on the user’s phone.
무료 시범 운영 시작|Free pilot begins
무료·시범 운영으로 공개했습니다.|Opened the service as a free pilot.
첫 반응|Early feedback
하루 방문자 89명, 90명. 당근 글 올린 뒤 1시간에 49명, 맘카페 글 뒤 1시간에 22명이 들어왔습니다. 많이 본 화면은 홈, 학원 찾기, 유치원, 도서관 순입니다.|The first daily visitor counts were 89 and 90. Local community posts brought visitors, with the home screen, classes, kindergartens and libraries getting the most attention.
아이랑 경기 — 경기도 도시로 확장|Airang expands across Gyeonggi
용인에서 시작한 정보 모음을 '아이랑'으로 이름을 바꾸고 경기도 도시로 넓혔습니다. 입구 주소 airang.songgollab.co.kr 에서 도시를 고르면 됩니다.|Renamed the Yongin project Airang and expanded to other cities in Gyeonggi. Choose a town at airang.songgollab.co.kr.
서울·인천·충남까지|Seoul, Incheon and Chungnam
서울 25개 구, 인천 5곳(연수·남동·부평·미추홀·계양), 충남 2곳(천안·아산)이 열렸습니다. 입구에서 지역 버튼을 누르고 우리 동네를 고르면 됩니다.|Added Seoul’s 25 districts, five areas in Incheon and Cheonan and Asan in Chungnam. Choose a region and then your town.
경기 31곳 · 모두 63곳|31 in Gyeonggi; 63 in total
경기 지역이 31곳으로 늘어 경기·서울·인천·충남 모두 63곳이 되었습니다.|Coverage reached 31 areas in Gyeonggi and 63 across all four regions.
매일 다시 올 이유 만들기|More reasons to return
오늘 우리 아이 급식 메뉴, 유치원 모집 일정 안내, 앱 안 "다음 기능" 투표를 준비합니다.|Plans include daily school meals, kindergarten application dates and a vote on the next feature.
용인 대상, 수집 가능한 정보부터 정리|Start with useful local information for Yongin
공공 데이터 매일 아침 자동 수집|Keep information up to date each morning
여덟 가지 메뉴, 학원 알림, 무료·가입 없음 (2026.10 시범 운영)|Eight menus and class reminders, free without sign-up; pilot began October 2026
월 1만 명까지 — 급식·유치원 모집 추가, 꾸준한 홍보, 의견 바로 반영|Up to 10,000 monthly visitors — add meals and application dates, introduce the service and act on feedback
월 1만~5만 명 — 동네 학원·키즈 업체 광고, 채용 공고 상단 노출 ("광고" 표시)|10,000–50,000 monthly visitors — consider clearly labelled local advertising and promoted job posts
월 5만 명 이상 — 도시 계속 늘리기, 지자체·기관 협업|Above 50,000 monthly visitors — expand coverage and explore community partnerships
우리 동네를 골라 지금 써 보세요|Choose your town and try it
무료이고, 가입 없이 바로 열립니다. 필요한 기능이 있으면 알려 주세요.|It is free and opens without sign-up. Let me know what would help your family.
01 · 대표 프로젝트 · 실증 중|01 · Home IoT · In daily use
공사 없이, 우리 집에 맞춘 AI 월패드. 기기 설치부터 집 구조에 맞춘 관리 화면, 원격 관리까지 한 번에 맡습니다. 지금은 우리 집(송골집 2층)과 셀프 바베큐장 라그릴스에서 직접 써 보며 검증하고 있습니다.|An AI wall pad tailored to the house without rewiring. I bring device installation, a floor-plan screen and remote access together. I am testing it upstairs at our house and at La Grills, a self-service BBQ site.
시간·날씨·집에 있는 가족 수, 방마다 조명과 온도를 큰 카드로 봅니다.|Large cards show time, weather, family presence, lights and room temperatures.
집 모양 그대로 보고, 방을 누르면 그 방의 기기와 조명 스위치가 나옵니다.|A floor plan follows the shape of our house. Tap a room to see its devices and lights.
가족이 동의한 휴대폰 위치와 배터리를 지도에서 확인합니다.|See family members’ phone locations and battery levels with their consent.
전력 센서로 잰 실제 값으로 가전별 전기 사용량과 요금을 봅니다.|See measured appliance energy use and estimated costs.
조건이 맞으면 알아서 켜고 끕니다. 센서가 없는 규칙은 작동하는 척하지 않습니다.|Devices respond to the conditions at home. Features without the required sensors are not shown as working.
"자비스"라고 부르면 듣고, 대답은 태블릿이나 구글 스피커로 들려줍니다.|Ask by voice and hear the answer on the tablet or a connected speaker.
냉장고·세탁기·TV·로봇청소기를 연결해 상태와 세탁 끝 알림을 받습니다.|See connected appliance status and receive notices such as the end of a wash.
공장 설비 점검처럼, 등록된 기기가 정상인지 한눈에 봅니다.|Check the health of registered devices at a glance.
노트북과 태블릿이 같은 설정을 쓰고, 한쪽에서 바꾸면 다른 쪽도 바뀝니다.|The laptop and tablet share the same settings.
노트북 속 가상 서버에서 Home Assistant가 브랜드가 다른 기기를 하나로 묶습니다.|Different brands of devices appear together in one home view.
직접 만든 송골집 화면 서버가 우리 집 평면도에 맞춘 화면을 띄웁니다.|The Songgol Home screen follows our floor plan.
벽에 붙인 태블릿과 가족 휴대폰으로 보고, 밖에서도 안전하게 접속합니다.|View the house from the wall tablet or a family phone, including while away.
35년 된 단독주택 2층. 벽 공사 없이 꽂고, 붙이고, 올려 두는 방식으로 자동화하고 있습니다. 관리 화면 v1.12 사용 중.|Upstairs in a 35-year-old house, using equipment that plugs in or mounts without wall work. The original field record uses screen version v1.12.
BBQ 사이트 1~9, 객실, 매점 구역별 에어컨을 매장 PC 한 화면에서 켜고 끕니다. 허브 v2.6, 2026년 10월 4일 설치(2일 작업).|Air conditioning for BBQ sites 1–9, guest rooms and the shop is controlled from the counter PC. Hub v2.6 was installed on October 4, 2026, after two days of work.
시작 — 우리 집 자동화 구성안 v1|First plan for our house
출발점은 단순했습니다. 집 안의 모든 기기를 한 화면에서 보고, 자동 제어로 전기를 아끼는 것. 그리고 부품은 최대한 저렴하게. 전기 공사 없이 2층만 자동화하기로 정했습니다.|The aim was simple: see the house on one screen, reduce wasted electricity and keep costs down. I started upstairs without electrical work.
2층 구조 확정, 3D 평면도|An upstairs floor plan
로봇청소기 지도와 집 사진으로 2층을 3D로 그렸습니다. 방을 누르면 그 방의 조명과 기기가 바로 나옵니다.|Added a 3D view of upstairs, with room-level lights and devices.
Home Assistant 첫 연결|First connected home view
조명·가족지킴이·날씨를 연결하고, 노트북 실행 파일과 태블릿 접속, 3D 속도 개선이 이어졌습니다.|Added lights, family view and weather, then improved tablet access and 3D performance.
구글 스피커와 자비스|Speaker and voice assistant
구글 스피커를 붙이고 "자비스" 음성 호출을 만들었습니다. 로봇청소기 제어·예약도 들어갔습니다.|Added a speaker, voice interaction and robot-vacuum controls.
가전과 전기 사용량|Appliances and energy use
냉장고·세탁기 같은 가전을 삼성 SmartThings로 연결하고, 가전별 전기 사용량과 요금, 세탁 끝 알림을 보여 줍니다.|Added appliance status, energy use, estimated costs and end-of-wash alerts.
부딪힌 문제를 하나씩|Fixing problems as they appeared
연결 거부, 두 번째 모니터에 숨은 보안 경고 창, 태블릿에서만 다르게 보이던 지도까지 원인을 찾아 고쳤습니다. 자비스 마이크와 가족지킴이 실제 지도도 개선했습니다.|Fixed connection and display issues, then improved the microphone and family map.
두 번째 현장, 라그릴스|A second site — La Grills
우리 집에서 써 본 방식을 처음으로 업장에 옮겼습니다. 구역마다 IR 리모컨을 달고 매장 PC에 허브 v2.6을 설치했습니다.|Took the home project into a working business for the first time with La Grills Hub v2.6.
설정 맞추기와 I/O 체크|Shared settings and device checks
노트북과 태블릿이 같은 설정을 쓰고, 등록된 기기가 정상인지 한눈에 봅니다. 센서가 없는 기능은 동작하는 척하지 않도록 정리했습니다.|Shared settings across the laptop and tablet, added device checks and made unsupported functions clear.
IoT 이야기 영상 5편 공개|Five Home IoT videos
IoT가 무엇인지, 무엇이 좋아지는지 40초 영상 다섯 편으로 정리했습니다.|Published five short videos about IoT and its everyday benefits.
진짜 자동 제어 시작|More real-world automation
Zigbee 센서와 에어컨 리모컨을 달아 방마다 재실·온도에 따라 움직이게 합니다. 라그릴스는 전 구역 전등, 예약 시간 연동, 에어컨 전력 확인으로 넓힙니다.|Plans include room-based presence and temperature controls, with lighting, booking schedules and energy monitoring at La Grills.
Home Assistant 연결, 조명·가족지킴이·날씨, 태블릿 접속, 3D 평면도|Connected home view, lights, family view, weather, tablet access and 3D floor plan
구글 스피커 연결, 자비스 음성 호출, 로봇청소기 제어·예약|Speaker, voice assistant and robot-vacuum controls
가전 관리, 가전별 전기 사용량·요금, 삼성 SmartThings 연결|Appliance status, energy use and estimated costs
자비스 마이크 개선, 가족지킴이 실제 지도|Microphone improvements and family map
노트북·태블릿 설정 맞추기, I/O 체크, 방마다 기기 추가·삭제|Shared settings, device checks and room-level device management
지금 쓰고 있는 버전|Version in this original field record
객실·BBQ 사이트·매점 에어컨 통합 제어 (2026.10.04 설치)|Combined air-conditioning control for rooms, BBQ sites and the shop; installed October 4, 2026
우리 집·우리 가게에도 적용해 보세요|Bring it to your home or shop
공사 없이 설치하고, 집 구조에 맞춘 화면을 만들어 드립니다.|I install devices without rewiring and build a screen around the layout of your home.
''')

translations('''
서비스 · 상용화 및 테스트 단계|Try it · Public services and testing
지금 바로|Ready to
써 볼 수 있어요|try today
송골랩이 만들어 공개한 서비스입니다. 둘 다 무료이고, 써 보신 의견으로 계속 다듬고 있어요.|Two services I built at Songgol Lab. Both are free, and I keep improving them with feedback.
아이 키우는 집을 위한 우리 동네 정보. 학교 일정·급식, 도서관, 유치원, 학원, 동네병원, 놓치기 쉬운 혜택, 주말 행사를 한곳에서. 회원가입이 없고 아이 정보는 휴대폰에만 저장돼요.|Local information for families in Korea: school calendars and meals, libraries, kindergartens, classes, clinics, benefits and weekend events. No sign-up; child profiles stay on the phone.
아이랑 경기 소개 영상|Airang in Gyeonggi — introduction
알레르기 표시까지|Including allergen information
운영시간, 빈자리|Opening times and availability
동네 학원 한눈에|Local classes at a glance
놓치기 쉬운 정보|Useful information that is easy to miss
아이랑은 송골랩이 만든 무료 서비스입니다.|Airang is a free service made by Songgol Lab.
테스트 중 · 테스터 모집 (선착순 20명)|In testing · Seeking testers (first 20 places)
남는 안드로이드 태블릿·휴대폰을 우리 차 계기판으로. OBD 동글을 꽂으면 속도·연비·고장 코드를 실시간으로 보고, T맵과 유튜브를 나눠 띄울 수 있어요.|Turn a spare Android tablet or phone into a car dashboard. With an OBD dongle, view vehicle readings and fault codes, with split-screen navigation and media features.
써 보시고 의견을 들려주세요|Try it and tell me what you think
불편한 점, 있었으면 하는 기능 모두 반영에 큰 도움이 됩니다.|Bug reports and ideas for useful features help me decide what to improve.
자료실 · 영상|Video library
서비스 소개, 기능 설명, IoT 이야기까지. 송골랩 유튜브 채널의 영상을 주제별로 모았어요. 누르면 이 자리에서 바로 재생돼요.|Introductions, feature tours and Home IoT stories from the Songgol Lab channel, grouped by topic. Select a video to play it here.
태블릿을 차 계기판으로 쓰는 앱|A car dashboard for a spare tablet
남는 태블릿을 우리 차 계기판으로|Give a spare tablet a new job in the car
화면 하나씩 둘러보기|A tour of the screens
출시 전 무료 · 선착순 20명|Free before launch · First 20 testers
아이 키우는 집의 우리 동네 정보|Local information for families
우리 동네 아이 정보 한 화면에|Family information in one view
학교 일정부터 학원비 비교까지|From school calendars to class fee comparisons
천안·아산|Cheonan and Asan
사이트 7곳 따로 볼 필요 없어요|One view instead of seven sites
지금 문 연 소아과 찾기|Find an open children’s clinic
다자녀·출산 지원|Benefits for growing families
셋째아 혜택|Support for a third child
이번 주말 어디 가지?|Where shall we go this weekend?
밤 9시 문 연 약국|Find a pharmacy open at 9 pm
40초로 이해하는 홈 IoT, 5편 연재|Five short introductions to home IoT
40초 만에 이해하는 사물인터넷|The Internet of Things in 40 seconds
편리·절약·안전·원격·자동|Convenience, savings, safety, remote access and automation
아침부터 밤까지|From morning to bedtime
IoT로 막기|Reducing waste with IoT
IoT로 안심|A little more peace of mind
라그릴스에서 직접 써 보는 모습|The project in everyday use at La Grills
매장 PC 한 화면|One screen at the counter
허브가 설치된 매장|The site where the hub is in use
IoT 이야기 · 영상 5편|Home IoT stories · Five videos
IoT는 어려운 기술이 아니라, 집이 알아서 챙겨 주는 생활 방식입니다. 송골랩이 만든|IoT can make the house take care of small everyday tasks. These five
영상 5편과 함께 IoT가 무엇인지, 집에 들이면 무엇이 달라지는지 한 페이지에 정리했습니다.|videos explain what it means and what changes at home.
IoT(사물인터넷)는 집 안의 물건이 인터넷으로 연결돼 스스로|IoT, the Internet of Things, connects household devices so they can
감지하고, 알려 주고, 움직이는|sense, notify and act
기술입니다. 네 단계만 알면 쉽게 이해됩니다.|. Here is a simple four-part overview.
센서가 온도, 움직임, 문 열림 같은 변화를 알아챕니다.|Notice changes such as temperature, movement or an open door.
와이파이나 Zigbee 무선으로 집 안 허브에 알립니다.|Bring those changes into the home view.
허브가 정해 둔 규칙대로 지금 할 일을 정합니다.|Decide whether a response is needed.
조명, 에어컨, 플러그가 실제로 켜지고 꺼집니다.|Lights, air conditioning and plugs respond.
이 네 단계가 이어지면 휴대폰 하나로 집 밖에서도 집 상태를 보고 조절할 수 있습니다.|Together, these features let you see and manage the house from a phone while away.
IoT를 들이면 생활이 달라지는 지점을 다섯 가지로 나눠 봤습니다.|Five ways IoT can help in everyday life.
말 한마디, 버튼 하나로 조명과 에어컨을 켜고 끕니다.|Use a voice request or a button to control lights and air conditioning.
빈 방의 전등과 에어컨, 쓰지 않는 기기의 대기전력을 끕니다.|Reduce lighting, cooling and standby power in unused rooms.
문 열림이나 이상 상황을 휴대폰으로 바로 알려 줍니다.|Receive a phone alert about an open door or something unusual.
집 밖에서도 휴대폰으로 집 상태를 보고 기기를 조절합니다.|Check the house and manage devices while away.
귀가, 외출, 취침처럼 정해 둔 상황이 되면 알아서 움직입니다.|Let the house respond to routines such as arriving, leaving and bedtime.
아침에 일어나서 잠들 때까지, IoT가 설치된 집은 이렇게 움직입니다.|A few examples, from waking up to going to bed.
집 상태는 휴대폰 한 화면에서 확인합니다.|Check the house on one phone screen.
버튼 하나로 집 안 전등과 에어컨을 한 번에 끕니다.|Switch off the lights and air conditioning together.
빈집에 문 열림이나 움직임이 생기면 휴대폰으로 알려 줍니다.|Receive an alert if a door opens or movement is detected while away.
집에 닿기 전에 미리 냉난방을 켜 둡니다.|Start heating or cooling before you arrive.
잠들 때 남은 조명이 자동으로 꺼집니다.|Let the remaining lights turn off at bedtime.
켜져 있는 줄도 몰랐던 전기, 막기|Reducing the power you did not know was on
대기전력, 아무도 없는 방의 조명처럼 모르는 사이 새는 전기가 있습니다. IoT는 이 전기를 찾아내고, 알아서 막습니다.|Standby devices and lights in empty rooms can use power unnoticed. IoT helps make that use visible and reduce it.
가전별 전기 사용량을 화면으로 보고, 어디서 새는지 찾습니다.|See appliance energy use and spot unnecessary consumption.
빈 방 조명 끄기, 쓰지 않는 기기 대기전력 차단을 자동으로 합니다.|Turn off empty-room lights and unused devices automatically.
실제로 얼마나 아꼈는지는 송골랩 실증 현장의 계절 데이터를 모은 뒤 개발 일지에 숫자로 공개하겠습니다.|I will report actual savings in the work log after collecting seasonal data from our test sites.
멀리 계신 부모님 댁, 안심|Looking after parents from afar
따로 사시는 부모님 댁, 늘 마음이 쓰이시죠? 센서 몇 개와 알림만으로 멀리서도 살필 수 있습니다.|A few sensors and alerts can help families check on a parent’s home from a distance.
화재 연기나 물샘을 감지하면 바로 알려 줍니다.|Receive an alert when a connected sensor detects smoke or a leak.
현관문이 열리고 닫히는 것을 확인합니다.|Check whether the front door is open or closed.
집 안이 너무 춥거나 덥지 않은지 봅니다.|See whether the house is getting too cold or too hot.
평소와 다르게 움직임이 없으면 알려 줍니다.|Notice unusual changes in activity.
추운 날 멀리서도 보일러를 켜 드릴 수 있습니다.|Help warm the house remotely on a cold day.
벽을 뚫거나 배선을 새로 깔지 않습니다. 꽂고, 붙이고, 올려 두는 방식이라 오래된 집도 괜찮습니다.|I use equipment that plugs in or mounts without new wall wiring, including in our older house.
Home Assistant 하나로 브랜드가 다른 기기를 묶습니다. 외부 업체 서버가 끊겨도 집은 계속 동작합니다.|The home view brings different brands together, with local control where supported.
남의 집 전기를 만지는 일이라, 국내 인증을 받은 장비만 씁니다.|I choose equipment certified for use in Korea.
송골랩은 직접 써 보고 검증한 것만 서비스로 만듭니다. 지금은 우리 집(송골집)과 셀프 바베큐장 라그릴스에서 실증 중입니다.|I test things in everyday use before deciding what is ready to offer. Current sites are our home and La Grills.
바베큐장 에어컨, 매장 PC 한 화면으로 묶기 — 라그릴스 설치기|La Grills installation story — air conditioning on one counter screen
IoT가 뭐예요? — IoT 이야기 EP.1 글로 보기|What is IoT? — Read episode 1 on the blog
IoT 설치하면 뭐가 좋아질까? — IoT 이야기 EP.2 글로 보기|What changes at home? — Read episode 2 on the blog
우리 집에도 IoT, 상담해 보세요|Ask about IoT for your home
집 구조와 원하는 기능을 알려 주시면 현장을 확인하고 맞춤으로 제안해 드립니다.|Tell me about your home and the features you need. I can review the site and suggest a suitable setup.
20년 동안 반도체 세정장비 현장에서 장비의 소프트웨어·하드웨어·동작 순서·제어를 함께 보며 불량의 원인을 찾아 왔습니다. 그 경험을 정리했습니다.|For 20 years I investigated defects on semiconductor wet-clean equipment, looking at software, hardware, sequences and controls together. This page records that experience.
장비 문제는 대부분 한 가지 원인으로 생기지 않습니다. 소프트웨어 설정, 하드웨어 상태, 동작 순서, 제어 값이 겹쳐서 나타납니다. 그래서 한 사람이 네 가지를 함께 봐야 빨리 풀립니다.|Equipment problems often involve several things at once. I learned to look at software, hardware, operating sequences and controls together.
원인을 모르는 파티클·비산이 간헐적으로 생긴다|Intermittent particles or splashing with an unclear cause
레시피를 바꿔도 결과가 들쭉날쭉하다|Inconsistent results after process changes
장비 대기·병목 때문에 처리량이 나오지 않는다|Waiting and bottlenecks that reduce throughput
데이터는 쌓이는데 볼 도구가 없다|Plenty of data without a useful way to review it
손으로 세는 반복 평가에 시간이 많이 든다|Repetitive manual evaluations that take too long
20년 동안 세정장비 현장에서 직접 다뤄 온 일만 적었습니다.|These are areas I have worked on directly during 20 years with wet-clean equipment.
파티클·비산·워터마크 같은 현상을 장비의 소프트웨어·하드웨어·동작 순서(시퀀스)·제어를 함께 엮어 보며 원인이 하나로 좁혀질 때까지 확인합니다.|Investigated particles, splashing and watermarks across equipment software, hardware, sequences and controls.
FOUP 스케줄링과 장비 동작 순서를 로직 단위로 비교해, 대기와 병목이 생기는 지점을 찾습니다.|Reviewed FOUP scheduling and equipment sequences to understand waiting and bottlenecks.
파티클 이력, E/R, 웨이퍼 맵처럼 쌓이기만 하던 데이터를 현장에서 바로 쓰는 분석 프로그램으로 만듭니다.|Built tools that make particle history, E/R and wafer maps useful on the fab floor.
감수지를 손으로 세던 비산 평가, 가스 감지기 값을 받아 적던 배기 효율 측정을 센서와 프로그램으로 바꾸는 방법을 구상하고 있습니다.|Exploring tools that reduce manual work in splash and exhaust evaluations.
원인을 찾았다고 말하려면 같은 조건에서 다시 일어나야 합니다.|A cause needs evidence that can be reproduced under the same conditions.
''')

translations('''
04 · 모빌리티 · 테스터 모집 · v1.3.53|04 · Mobility · Testing · v1.3.53
집에서 쉬고 있는 태블릿을 내 차의 대시보드·내비·진단기로. 3D 계기판, T맵 분할 화면, 인터넷 라디오, 음성 비서, OBD 차량 진단을 태블릿 하나에 담았습니다. 실제 차(2017 올뉴K7 3.0 LPi)에서 OBD 연결과 고장 코드 읽기까지 확인했습니다.|A spare tablet becomes a dashboard, navigation screen and vehicle-information display. I brought together a 3D dashboard, TMAP split screen, radio, voice assistant and OBD readings, and checked the connection and fault-code reading in my 2017 Kia K7 3.0 LPi.
메인·프로그램·차량 정보·음성 비서·차계부·설정|Home, apps, vehicle information, voice assistant, car log and settings
고장 코드 해석 · 현대·기아 427 · 국제 표준 9,415|Fault-code explanations — 427 Hyundai/Kia and 9,415 standard codes
연료별 진단 · 가솔린 · 디젤 · LPi|Fuel-specific information — petrol, diesel and LPi
실시간 계기판, 고장 코드 설명, 차계부, 휴대폰 화면, 주행 중 자동 가림|Dashboard, fault codes, car log, phone view and driving video cover
메인 화면부터 분할 화면, 차량 정보, 고장 코드, 음성 비서, 차계부까지|A tour of the dashboard, split screen, vehicle information, voice assistant and car log
드라이브 콘솔 메인 화면|Drive Console home screen
왼쪽은 차량 상태(건강 점수·냉각수·연료 보정·회전수), 가운데는 GPS 속도로 움직이는 3D 계기판, 오른쪽은 KBS·MBC·SBS·CBS 8개 채널 인터넷 라디오. 위쪽에는 날씨·미세먼지와 인터넷·OBD 연결 상태가 보입니다.|Vehicle status sits on the left, a 3D dashboard in the middle and internet radio on the right. Weather, air quality and connection status stay at the top.
계기판 디자인 6가지|Six dashboard designs
3D 도로·크롬·골드·레드·유리판·길안내 바닥 중에서 설정에서 바로 고릅니다. 스킨마다 별빛 색과 도로 위 3D 차량이 달라지고, 속도가 바뀔 때만 다시 그려 태블릿 부담을 줄였습니다.|Choose a dashboard design in settings. Each has its own colours and 3D vehicle view, with attention to tablet performance.
T맵 분할 화면|TMAP split screen
유튜브·음악 같은 앱을 내비와 같이 씁니다. 시속 8km가 넘으면 오른쪽 영상 앱을 자동으로 가리고, 지도와 소리는 그대로 둡니다(도로교통법 49조, 기본값 켜짐).|Navigation can sit beside another app. A driving video cover hides video while keeping the map and audio available. Use the screen only when safely parked.
음성 비서 화면|Voice assistant screen
"송골랩, 차 상태 알려줘", "쿨FM 틀어줘", "주유 5만 원 기록해줘" — 손 대지 않고 조작합니다.|Ask for vehicle status, select a radio station or record a fuel purchase by voice.
차계부 화면|Car log screen
주유·정비 기록과 이번 달 지출, 엔진오일·보험·정기 검사 남은 기간을 한눈에.|See fuel and maintenance records, monthly spending and upcoming service, insurance and inspection dates.
설정 화면|Settings screen
OBD 연결(블루투스·Wi-Fi), 차량 등록, 계기판 디자인, 주행 중 영상 가림, 음성 비서 크기, 부르는 이름까지 한 화면에서 바꿉니다.|Manage the vehicle, connection, dashboard appearance, driving video cover and voice-assistant preferences in one place.
차량 정보 화면 (올뉴K7)|Vehicle information — Kia K7
냉간·예열 후 공회전·주행 중마다 다른 정상 범위로 판정하고, 여러 값을 묶어 "가능성 높은 원인 → 의심 부품 → 조치 순서"로 안내합니다. 며칠 타면 이 차의 평소값을 배워 달라지면 알려 줍니다.|The vehicle view puts readings in context and presents possible causes and checks. It also helps highlight changes from the car’s usual readings.
엔진 저장·대기·영구 코드 + ABS·에어백·변속기 등 8개 장치|Read available fault codes from supported vehicle systems
연료별 사전 → 현대·기아 427개 → 국제 표준 9,415개 순서|Explain supported manufacturer and standard fault codes
고장 당시 기록(냉각수·회전수·차속·부하)으로 상황 해석|View information recorded when the fault occurred
가장 의심되는 부품과 점검 순서, 위험도 3단계|Show possible causes, checks and an urgency indication
디젤 차량 정보 화면|Diesel vehicle information
매연 필터(DPF) 차압이 높으면 원인·의심 부품·조치 순서까지 바로 보여 줍니다. 예: "고속도로 20~30분 주행 → 그래도 안 되면 정비소 강제 재생".|The diesel view includes supported DPF-related information and explains possible issues. Have a workshop assess any fault before deciding on repairs.
직분사(GDI) 자동 인식, 연료펌프·증발가스·터보 코드 약 40개, 연료 보정·산소 센서·촉매 판정|Supported petrol-system readings and explanations for relevant fault codes
DPF 차압·재생 필요도, 커먼레일 압력·EGR·과급압·요소수, 관련 코드 약 100개|Supported diesel-system readings, including DPF and related fault information
올뉴K7 3.0 LPi 전용 기준, LPG 펌프·필터·펌프 드라이버 원인 분석|LPi information developed around the Kia K7 3.0 LPi test vehicle
연료는 차량 등록에서 고른 값을 먼저 쓰고, 없으면 ECU가 알려 주는 연료 종류로 자동 판별합니다.|The vehicle profile keeps the displayed information relevant to its fuel type.
엔진·변속기·ABS·에어백 등이 실시간 값과 고장 코드를 보관|Provides available vehicle readings and fault information
운전석 아래 단자에 꽂는 ELM327 동글, 블루투스 또는 Wi-Fi|Connects the car to a supported tablet
값 판정·원인 분석·고장 코드 해석, 계기판·라디오·음성 비서|Presents readings, explanations, dashboard, radio and voice features
차량 데이터는 외부 서버로 보내지 않습니다|Vehicle data is not sent to an external server
버튼 자동 점검 · 오류 0건|Button checks — no errors found in that test
연료별 시뮬레이션 · 오류 0건|Fuel-type simulations — no errors found in that test
고장 코드 문구 전수 확인|Fault-code messages reviewed
시작 — 대시보드 화면 기본 틀|First dashboard frame
처음 손에 있던 건 v0.6 설치 파일 하나였습니다. 여기서부터 화면과 기능을 하나씩 쌓았습니다.|Started with a v0.6 installer and added screens and features one at a time.
계기판과 분할 화면|Dashboard and split screen
3D 계기판 7종, 분할 화면 아래 작은 메뉴(7:3·5:5·3:7), 6개 언어. 가짜 데이터는 모두 걷어 냈습니다.|Added dashboard designs, split-screen controls and six languages. Removed placeholder readings.
Wi-Fi OBD 연결|Wi-Fi OBD connection
OBD 동글에서 회전수·차속·냉각수·배터리 같은 실시간 값을 받아, 순간·평균 연비와 주행 가능 거리를 계산합니다.|Added live vehicle readings and estimated fuel-use information.
분할과 음성 비서 다듬기|Split-screen and voice refinements
왼쪽 T맵 고정 분할, 분할 잠금, 화면 위에 뜨는 음성 비서 링, 앱 안 음성 인식, 시간대별 배경과 일주일 날씨, 떠 있는 창 지원까지 열한 번 고쳤습니다.|Refined TMAP split screen, voice interaction, weather, backgrounds and floating-window support over eleven updates.
블루투스 동글과 차량 정보|Bluetooth and vehicle information
블루투스 OBD 동글을 연결하고, 건강 점수·상황별 판정·원인 추정·내 차 평소값 학습을 담은 "차량 정보" 메뉴를 만들었습니다.|Added Bluetooth OBD support and a vehicle-information screen with readings and explanations.
메인 화면 개편과 인터넷 라디오|Home screen and internet radio
왼쪽 차량 상태 패널, 도로 위 3D 차량, 8개 채널 라디오. 다른 화면에서도 라디오가 계속 나옵니다.|Added the vehicle-status panel, 3D vehicle and eight radio channels, with playback across screens.
고장 코드 전부 해석|Broader fault-code explanations
올뉴K7 상세 코드 427개와 국제 표준 9,415개를 한국어로. 엔진 외 8개 장치 고장 코드도 읽습니다.|Added explanations for 427 Kia K7 and 9,415 standard codes, plus readings from other supported systems.
안전 먼저|Driving-safety refinements
주행 중 영상 가림막, 화면 전환 정리, 음성 비서 창이 T맵을 가리지 않게. 버튼 75개를 자동 점검해 오류 0건을 확인했습니다.|Added the driving video cover and refined screen transitions and the voice overlay. The recorded button test found no errors.
가솔린·디젤·LPi 모두 지원|Petrol, diesel and LPi
연료 자동 판별, 디젤 전용 값과 연료별 정비 사전을 더하고, 설명 문구를 전부 다시 검토했습니다.|Added fuel-specific information and reviewed the explanatory text.
분할 종료 수정|Returning from split screen
분할을 끝내면 앱이 앞에 뜰 때까지 확인하고 메인 화면으로 바로 돌아옵니다.|Fixed the return to the home screen after closing split screen.
부르는 이름 바꾸기 · 안전 운전 안내|Custom assistant name and driving notice
음성 비서를 부르는 이름(기본 "송골랩")을 바꿀 수 있고, 처음 실행하면 안전 운전 안내가 한 번 뜹니다.|Added a custom assistant name and a driving-safety notice on first launch.
실차 검증 → 출시|More vehicle testing, then release
디젤·가솔린 차로 기준값 보정, 라디오 운영 방식 결정, KC 인증 동글과 함께 파는 패키지, Play 스토어 정책에 맞춘 배포를 준비합니다.|Plans include more real-vehicle checks, decisions about radio, a certified-dongle package and store release preparation.
대시보드 화면 기본 틀|First dashboard frame
3D 계기판 7종, 분할 메뉴, 6개 언어|Dashboard designs, split-screen menu and six languages
Wi-Fi OBD, 실시간 차량 값, 연비·주행 가능 거리|Wi-Fi OBD, vehicle readings and fuel-use estimates
T맵 고정 분할, 분할 잠금, 음성 비서 화면, 날씨, 떠 있는 창|TMAP split screen, voice interface, weather and floating windows
블루투스 동글, 차량 정보 메뉴, 원인 추정, 앱 종료 버튼|Bluetooth, vehicle-information screen and app controls
메인 화면 개편, 3D 차량, 인터넷 라디오|Home screen, 3D vehicle and internet radio
고장 코드 전체 해석, 발생 당시 값 분석, 다른 장치 고장 코드|Broader fault explanations, recorded context and more supported systems
주행 중 영상 가림, 화면 전환 정리, 안전 점검|Driving video cover, screen transitions and checks
가솔린·디젤·LPi 모두 지원, 연료별 정비 사전, 문구 전체 검토|Fuel-specific information for petrol, diesel and LPi; text review
분할 종료 후 메인 화면 복귀 수정|Fixed return from split screen
음성 비서 부르는 이름 바꾸기(기본 "송골랩"), 첫 실행 안전 운전 안내, 주행 중 영상 앱 자동 가림 (최신)|Custom assistant name, first-launch driving notice and automatic driving video cover; latest version in this record
드라이브 콘솔이 보여 주는 속도·연비·고장코드 등 차량 정보는 참고용이며, 정확한 점검과 진단은 정비소에서 받으세요. 운전 중에는 화면을 조작하지 말고, 안전 운전의 책임은 운전자에게 있습니다.|Vehicle readings and fault-code explanations are for reference. Have a qualified workshop inspect and diagnose faults. Do not operate the screen while driving; the driver is responsible for safe operation.
먼저 써 보고 싶으신가요?|Would you like to try it?
출시 전 실차 테스트에 함께할 분을 찾고 있습니다. 차종과 연료를 알려 주세요.|I am looking for real-vehicle testers before release. Please include your vehicle model and fuel type.
''')


def translated_body(body):
    import re
    from html import escape, unescape
    def text(value):
        value = unescape(value)
        stripped = value.strip()
        if not stripped or not re.search('[가-힣]', stripped): return value
        if stripped not in TEXT:
            # Video cards use the video title followed by an accessible play verb.
            if stripped.endswith(' 재생') and stripped[:-3] in TEXT:
                return 'Play ' + TEXT[stripped[:-3]]
            raise ValueError('Missing English translation: ' + stripped)
        return value.replace(stripped, TEXT[stripped])
    parts = re.split('(<[^>]+>)', body)
    for i,part in enumerate(parts):
        if part.startswith('<'):
            part = re.sub(r'(alt|aria-label|title)="([^"]*)"', lambda m: m[1] + '="' + escape(text(m[2]), quote=True) + '"', part)
            # Keep shared media IDs; local page links stay in the English tree.
            def link(m):
                href = m[1]
                if href.startswith('/contact'):
                    href = 'mailto:songgollab@gmail.com'
                elif href.startswith('/drive-console-privacy'):
                    href = '/drive-console-privacy#privacy-en'
                elif href.startswith('/drive-console'):
                    href = href.replace('/drive-console', '/drive-console-en', 1)
                elif href.startswith('/') and not href.startswith('//'):
                    path, mark, anchor = href.partition('#')
                    slug = path.strip('/') or 'index'
                    if slug in EN_PAGES:
                        href = ehref(slug) + (mark + anchor if mark else '')
                return 'href="' + href + '"'
            parts[i] = re.sub(r'href="([^"]*)"', link, part)
        else:
            parts[i] = escape(text(part), quote=False)
    return ''.join(parts)


def add_other_pages(g):
    import re
    specs = {
      'airang': ('Airang', 'Local information for families across 63 towns and districts in Korea. Free, with no sign-up.', 'projects'),
      'project-home-iot': ('Songgol Home IoT · AI wall pad', 'A home IoT and wall-pad project tested in our house and at La Grills.', 'projects'),
      'services': ('Try it', 'Try Airang and Drive Console, two free services from Songgol Lab.', 'services'),
      'videos': ('Videos', 'Songgol Lab project introductions, feature tours and Home IoT stories.', ''),
      'iot-guide': ('Home IoT explained', 'Five short videos about connected homes, energy use and everyday convenience.', 'projects'),
      'project-drive': ('Drive Console development log', 'The development history and screens of Drive Console, a dashboard for a spare Android tablet.', 'projects'),
      'consulting': ('Semiconductor wet-clean equipment', 'Twenty years of experience investigating defects and working with semiconductor wet-clean equipment.', 'consulting'),
    }
    for slug,(title,desc,menu) in specs.items():
        body = g['PAGES'][slug][3]
        # Replace the appended Korean media sections with their English versions.
        body = re.sub(r'<section\b[^>]*>.*?</section>', lambda m: '' if any(label in m[0] for label in ('Images · 이미지', 'Video · 영상', 'Docs · 자료')) else m[0], body, flags=re.S)
        if slug in ('airang', 'project-home-iot'):
            pos = body.rfind('<section class="band">')
            body = translated_body(body[:pos]) + en_media(g, slug, slug == 'project-home-iot') + translated_body(body[pos:])
        else:
            body = translated_body(body)
        g['PAGES']['en/' + slug] = (title, desc, menu, body, 'en')
    add_work_log(g)


def add_work_log(g):
    import workshop as W
    # Recent entries retain the source dates, versions, order and kind.
    entries = [
      ('Robot design complete; measurements begin', 'The reuse plan is set. Next is inspecting the donor robot vacuum.'),
      ('3D Print Bench page published', 'Monitoring, queues, slicing and start checks on one PC screen.'),
      ('Central Control introduction video', 'A 94-second look at the working screen with 15 connected programs.'),
      ('Stocks and crypto in one program', 'Combined the two personal projects as Songgol Trader.'),
      ('A new home at songgollab.co.kr', 'Moved the website to its own domain. The blog remains a separate journal.'),
      ('12 closed-test participants', 'The 14-day closed test for Drive Console has started.'),
      ('Android release requirements', 'Updated platform settings without changing the screens or features.'),
      ('AI workshop trial', 'Started a two-week trial of a revised workflow.'),
      ('Trading project refinements', 'Simplified the settings in the private trading experiment.'),
      ('Screen effects and daily news', 'Added transitions, connection lines and a news card.'),
      ('Create, review and publish', 'Video work now includes an approval step before publishing.'),
      ('Radio on the wall pad', 'Added radio, full-screen mode and app installation support.'),
      ('Mail and room views', 'Added mail reading and current home status by room.'),
      ('Naver listing preparation', 'Refined product names and margin review.'),
      ('Purchase-list updates', 'Improved how new purchases appear in the spending view.'),
      ('Home reliability', 'Added monitoring to help recover from a stopped home service.'),
      ('Presence-sensing lights', 'Started using room-presence lighting at home.'),
    ]
    kinds = {'new':('New feature','k-new'), 'fix':('Fix','k-fix'), 'ship':('Released','k-ship'), 'milestone':('Milestone','k-ms')}
    cells = []
    for source,(title,description) in zip(W.LOG, entries):
        date,(slug,_),version,_,_,kind = source
        date = 'November' if date == '11월' else date
        version = 'Stage 0' if version == '0단계' else version.replace('주식', 'Stock')
        name = EP[slug][0] if slug else 'Songgol Lab'
        label,cls = kinds[kind]
        target = f'<a href="{ehref(slug)}">{name}</a>' if slug else f'<span>{name}</span>'
        cells.append(f'<li class="rv"><time>{date}</time><div class="lg"><div class="lg-top"><span class="kb {cls}">{label}</span>{target}' + (f'<code>{version}</code>' if version else '') + f'</div><b>{title}</b><p>{description}</p></div></li>')
    hero = g['hero']([], 'Work log', 'Built, used, improved', 'Recent changes from my workshop. Entries below are from November 2026.').replace('<a href="/">홈</a>', '<a href="/en/">Home</a> › <span>Work log</span>')
    body = hero + g['sec']('<ol class="wlog">' + ''.join(cells) + '</ol>', cls='tight')
    body += g['band']('Earlier entries', 'The complete archive, including October 2026, is available in Korean.', g['btn']('/log', 'Full log in Korean') + g['btn']('/en/projects', 'All programs', 'ghost'))
    g['PAGES']['en/log'] = ('Work log', 'Recent development changes from the Songgol Lab workshop.', 'log', body, 'en')
