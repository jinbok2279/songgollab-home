# -*- coding: utf-8 -*-
"""첫 화면(index)과 반도체 컨설팅(consulting) 페이지. build.py가 불러 씁니다."""
import math

def wafer_svg():
    """웨이퍼 맵 그림 (설명용 일러스트, 실제 데이터 아님)."""
    R, s, cx, cy = 200, 17, 220, 220
    hot = {(9, 1), (10, 1), (11, 1), (12, 2), (13, 2), (8, 1), (14, 3)}
    warn = {(7, 2), (12, 1), (15, 3), (13, 3), (11, 2), (6, 2)}
    chk = {(10, 11), (11, 11), (10, 12), (12, 12), (4, 13), (5, 6)}
    out = []
    n = int(2 * R / s) + 1
    ox, oy = cx - n * s / 2, cy - n * s / 2
    for i in range(n):
        for j in range(n):
            x, y = ox + i * s, oy + j * s
            if all(math.hypot(px - cx, py - cy) <= R - 6 for px, py in ((x, y), (x + s, y), (x, y + s), (x + s, y + s))):
                c = 'die'
                if (i, j) in hot: c += ' hot'
                elif (i, j) in warn: c += ' warn'
                elif (i, j) in chk: c += ' chk'
                elif (i * 7 + j * 3) % 5 == 0: c += ' ok'
                out.append(f'<rect class="{c}" x="{x:.1f}" y="{y:.1f}" width="{s - 2}" height="{s - 2}" rx="2"/>')
    dies = ''.join(out)
    return f'''<svg class="wafer" viewBox="0 0 440 440" role="img" aria-label="웨이퍼 맵 일러스트">
<defs><radialGradient id="wg" cx="40%" cy="35%" r="75%"><stop offset="0" stop-color="#22355E"/><stop offset="1" stop-color="#0B1428"/></radialGradient>
<linearGradient id="sg" x1="0" x2="0" y1="0" y2="1"><stop offset="0" stop-color="#19C2B0" stop-opacity="0"/><stop offset=".5" stop-color="#19C2B0" stop-opacity=".55"/><stop offset="1" stop-color="#19C2B0" stop-opacity="0"/></linearGradient>
<clipPath id="wc"><circle cx="{cx}" cy="{cy}" r="{R}"/></clipPath></defs>
<circle cx="{cx}" cy="{cy}" r="{R + 8}" fill="none" stroke="rgba(160,190,255,.18)" stroke-dasharray="2 6"/>
<circle cx="{cx}" cy="{cy}" r="{R}" fill="url(#wg)" stroke="#5E6F91" stroke-width="1.5"/>
<g clip-path="url(#wc)">{dies}<rect class="scan" x="0" y="{cy - 20}" width="440" height="40" fill="url(#sg)"/></g>
<path d="M{cx - 9} {cy + R - 1} a9 9 0 0 1 18 0" fill="#060B18" stroke="#5E6F91"/>
<path d="M{cx + 120} {cy - 150} L{cx + 175} {cy - 200} L{cx + 205} {cy - 200}" fill="none" stroke="#F59E0B" stroke-width="1.2"/>
<text x="{cx + 150}" y="{cy - 206}" fill="#F5B544" font-family="JetBrains Mono,monospace" font-size="10">EDGE · CLUSTER</text>
</svg>'''


def add(g):
    PAGES, btn, BLOG, MAIL = g['PAGES'], g['btn'], g['BLOG'], g['MAIL']

    AREAS = [
        ('01', '세정 공정 최적화', '습식 세정의 약액·린스·건조 조건과 레시피를 데이터로 다시 보고, 결과가 흔들리는 이유를 찾습니다.', ['WET CLEAN', 'RECIPE', 'RINSE/DRY']),
        ('02', '불량 원인 추적', '파티클·비산·워터마크 같은 현상을 장비의 SW·HW·시퀀스·제어를 함께 엮어 보며 원인을 좁혀 갑니다.', ['PARTICLE', 'ROOT CAUSE', 'SEQUENCE']),
        ('03', '신규 장비 평가 · 양산 전환', '평가 계획과 합격 기준을 세우고, 평가에서 양산으로 넘어가는 과정을 단계별로 함께합니다.', ['JDP', 'EVALUATION', 'RAMP-UP']),
        ('04', '시퀀스 · 물류 로직 검토', 'FOUP 스케줄링, 대기·병목 구간을 로직 단위로 비교해 처리량을 막는 지점을 찾습니다.', ['SCHEDULER', 'FOUP', 'THROUGHPUT']),
        ('05', '공정 데이터 분석 도구', 'E/R·웨이퍼 맵·파티클 이력을 현장에서 바로 쓸 수 있는 분석 프로그램으로 만듭니다.', ['E/R', 'WAFER MAP', 'TOOLING']),
        ('06', '평가 자동화', '감수지 카운트처럼 손으로 하던 반복 평가를 센서와 자동화로 바꾸는 방법을 설계합니다.', ['AUTOMATION', 'SENSOR', 'SPLASH']),
    ]
    areas_html = '<div class="areas">' + ''.join(
        f'<div class="area rv"><span class="no">{n} /</span><h3>{t}</h3><p>{d}</p><div class="kw">{"".join(f"<span>{k}</span>" for k in kw)}</div></div>'
        for n, t, d, kw in AREAS) + '</div>'
    FLOW = [('현상 관찰', '언제·어디서·얼마나'), ('데이터 수집', '로그·레시피·이력'), ('가설 분리', 'SW·HW·시퀀스·제어'), ('검증', '조건을 바꿔 재현'), ('기준 확정', '합격선과 관리값'), ('이관', '문서화·현장 전달')]
    flow_html = '<div class="flow">' + ''.join(f'<div class="rv"><b>{a}</b><span>{b}</span></div>' for a, b in FLOW) + '</div>'
    FEE = '''<div class="fee rv"><div class="ic2"><svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 12l5 5L21 4"/></svg></div>
<div><h3>성과 연동형으로 진행합니다</h3><p>시작할 때 목표 기준을 함께 정하고, 그 기준을 달성했을 때 합당한 비용을 받는 방식을 기본으로 생각하고 있습니다. 세부 조건은 상담에서 정합니다.</p></div>
<a class="btn btn-teal" href="/contact?topic=반도체">사전 상담</a></div>'''

    # ------------------------------------------------------------ 첫 화면
    hero = f'''<section class="hx dark grid-bg glow"><div class="wrap">
<div>
  <span class="eyebrow">Semiconductor Process · Equipment Engineering</span>
  <h1>보이지 않는 원인까지<br><span class="grad">끝까지 추적합니다</span></h1>
  <p class="lead">송골랩은 20년 동안 반도체 세정장비 공정 현장에서 장비의 SW·HW·시퀀스·제어를 함께 엮어 불량의 원인을 찾아 온 엔지니어링 랩입니다.</p>
  <div class="status"><i></i>반도체 공정·설비 컨설팅 준비 중 · 사전 상담을 받습니다</div>
  <div class="cta">{btn('/contact?topic=반도체', '사전 상담 문의 →', 'teal')}{btn('/consulting', '컨설팅 분야 보기', 'line')}</div>
  <div class="metrics"><div><b>20년</b><span>세정장비 공정 현장</span></div><div><b>4 Layer</b><span>SW · HW · 시퀀스 · 제어</span></div><div><b>Root cause</b><span>현상이 아니라 원인으로</span></div></div>
</div>
<div><div class="panel">
  <div class="panel-head"><span>WAFER MAP · INSPECTION</span><b>● ANALYZING</b></div>
  {wafer_svg()}
  <div class="panel-foot"><div>PATTERN<b class="a">Edge cluster</b></div><div>LAYER<b>Sequence</b></div><div>STATUS<b class="t">Root cause</b></div></div>
  <span class="panel-note">설명용 일러스트 · 실제 데이터 아님</span>
</div></div>
</div></section>'''

    areas_sec = f'''<section class="s2"><div class="wrap">
<div class="head"><div><span class="eyebrow">Engineering · 컨설팅 분야</span><h2>장비 앞에서 20년,<br>문제를 푸는 순서가 있습니다</h2></div>
<p>현상만 보고 부품을 바꾸지 않습니다. 장비가 남긴 기록과 동작 순서를 함께 놓고, 원인이 하나로 좁혀질 때까지 확인합니다.</p></div>
{areas_html}
<p style="margin-top:22px"><a class="more" style="font-weight:700;color:var(--blue)" href="/consulting">컨설팅 자세히 보기 →</a></p>
</div></section>'''

    how_sec = f'''<section class="s2 dark grid-bg"><div class="wrap" style="position:relative;z-index:1">
<div class="head"><div><span class="eyebrow">How we work · 일하는 방식</span><h2>추측 대신,<br>재현되는 근거로</h2></div>
<p>원인을 찾았다고 말하려면 같은 조건에서 다시 일어나야 합니다. 그 근거를 기준값과 문서로 남겨 현장에 넘깁니다.</p></div>
{flow_html}{FEE}
</div></section>'''

    lab_sec = f'''<section class="s2"><div class="wrap">
<div class="head"><div><span class="eyebrow">Lab · 랩 프로젝트</span><h2>현장에서 쓰던 방식으로,<br>생활 속 문제도 풀어 봅니다</h2></div>
<p>엔지니어의 개인 연구로 만들고, 직접 쓰면서 다듬는 프로젝트들입니다. 일부는 누구나 무료로 써 볼 수 있어요.</p></div>
<div class="lab">
  <a class="rv" href="/drive-console"><div class="im" style="background-image:url('/assets/drive-console.jpg')"><span class="b t">테스터 모집 · 무료</span></div>
    <div class="tx"><span class="k">MOBILITY · ANDROID</span><h3>드라이브 콘솔</h3><p>남는 태블릿을 차 계기판으로. OBD로 고장 코드 약 1만 개를 해석하고 원인과 점검 순서까지 보여 줍니다.</p><span class="go">테스터 신청 →</span></div></a>
  <a class="rv" href="/airang"><div class="im" style="background-image:url('/assets/airang-phone.jpg');background-position:top"><span class="b">공개 서비스 · 63곳</span></div>
    <div class="tx"><span class="k">LOCAL DATA · WEB</span><h3>아이랑</h3><p>아이 키우는 집의 동네 정보를 매일 아침 자동으로 모아 한 화면에.</p><span class="go">자세히 →</span></div></a>
  <a class="rv" href="/project-home-iot"><div class="im" style="background-image:url('/assets/iot-concept.jpg')"><span class="b">실증 중</span></div>
    <div class="tx"><span class="k">HOME IoT · AUTOMATION</span><h3>홈 IoT · AI 월패드</h3><p>공사 없이 집과 가게의 기기를 한 화면에서 보고 자동으로 제어합니다.</p><span class="go">자세히 →</span></div></a>
</div>
<p class="labnote">그 밖에 중앙관제, 상품 등록 자동화, IoT 비닐하우스까지 — <a style="color:var(--blue);font-weight:700" href="/projects">랩 프로젝트 전체 보기 →</a></p>
</div></section>'''

    blog_sec = f'''<section class="s2" style="padding-top:0"><div class="wrap">
<div class="two">
  <div><span class="eyebrow">Journal · 블로그</span><h3 style="font-size:24px;margin:10px 0 18px">개발 일지와 소식</h3>
    <div class="posts" id="posts"><a class="card post" href="{BLOG}" target="_blank" rel="noopener"><span class="d">블로그</span><b>개발 일지와 소식은 송골랩 블로그에서 볼 수 있어요</b></a></div></div>
  <div class="card tl"><span class="eyebrow">Timeline</span><h3 style="font-size:24px;margin:10px 0 18px">걸어온 길</h3><ul>
    <li><b>20년</b>반도체 세정장비 공정 엔지니어 — 공정 개발, 장비 평가, 불량 원인 추적</li>
    <li><b>2026.10</b>송골랩 랩 프로젝트 시작 · 홈 IoT, 아이랑, 드라이브 콘솔</li>
    <li><b>2026.11</b>송골랩 사업자 등록 · 홈페이지 songgollab.co.kr 개설</li>
    <li><b>준비 중</b>반도체 공정·설비 컨설팅</li></ul></div>
</div></div></section>'''

    cta = f'''<section class="s2" style="padding-top:0"><div class="wrap"><div class="cta-x grid-bg glow">
<div><span class="eyebrow" style="color:var(--teal)">Contact</span><h3 style="margin-top:10px">장비 문제,<br>같이 끝까지 봅시다</h3><p>컨설팅 사전 상담, 랩 프로젝트 의견, 협업 제안 모두 반갑습니다.</p></div>
<div class="links">{btn('/contact?topic=반도체', '사전 상담 문의', 'teal')}{btn('mailto:' + MAIL, MAIL, 'line')}</div>
</div></div></section>'''

    tail = '''<script>function sgPosts(d){try{var box=document.getElementById('posts');var es=(d.feed.entry||[]).slice(0,4);if(!es.length)return;box.innerHTML='';es.forEach(function(e){var l=(e.link||[]).find(function(x){return x.rel==='alternate'});var a=document.createElement('a');a.className='card post';a.href=l?l.href:'https://songgollab.blogspot.com';a.target='_blank';a.rel='noopener';var dt=new Date(e.published.$t);var s=document.createElement('span');s.className='d';s.textContent=dt.getFullYear()+'.'+String(dt.getMonth()+1).padStart(2,'0')+'.'+String(dt.getDate()).padStart(2,'0');var t=document.createElement('b');t.textContent=e.title.$t;a.append(s,t);box.append(a)})}catch(_){}}</script>
<script src="https://songgollab.blogspot.com/feeds/posts/summary?alt=json-in-script&max-results=4&callback=sgPosts" async></script>'''

    PAGES['index'] = ('', '송골랩 — 20년 반도체 세정장비 공정 경험으로 장비 불량의 원인을 끝까지 추적하는 엔지니어링 랩. 반도체 공정·설비 컨설팅 준비 중, 드라이브 콘솔·아이랑·홈 IoT 랩 프로젝트.', '',
                      hero + areas_sec + how_sec + lab_sec + blog_sec + cta, 'ko', tail)

    # ------------------------------------------------------------ 컨설팅
    CASES = ['원인을 모르는 파티클·비산이 간헐적으로 생긴다', '레시피를 바꿔도 결과가 들쭉날쭉하다', '신규 장비 평가가 합격 기준을 넘지 못한다',
             '장비 데이터는 쌓이는데 볼 도구가 없다', '스케줄러·시퀀스 때문에 처리량이 나오지 않는다', '현장 엔지니어마다 트러블슈팅 순서가 다르다']
    ENG = [('SHORT · 원인 분석', '단기 원인 분석', '특정 불량이나 이상 현상 하나를 정해, 데이터와 재현 시험으로 원인을 좁히고 대책을 정리합니다.'),
           ('PROJECT · 평가 동행', '장비 평가 · 양산 전환', '평가 계획부터 합격 기준, 양산 이관 문서까지 평가 기간 동안 함께합니다.'),
           ('TOOL · 도구 제작', '분석 도구 제작', 'E/R·웨이퍼 맵·이력 데이터를 현장에 맞는 분석 프로그램으로 만들어 드립니다.')]
    body = f'''<section class="page-hero"><div class="wrap"><div class="crumb"><a href="/">홈</a> › <span>반도체 컨설팅</span></div>
<span class="eyebrow">Semiconductor Process · Equipment Consulting</span><h1>반도체 공정·설비 컨설팅</h1>
<p class="lead">20년 동안 세정장비 공정 현장에서 쌓은 경험으로, 장비의 SW·HW·시퀀스·제어를 함께 보며 불량의 원인을 찾고 기준을 세웁니다.</p>
<div class="status"><i></i>준비 중 · 사전 상담과 일정 협의를 받고 있습니다</div>
<div class="cta">{btn('/contact?topic=반도체', '사전 상담 문의 →', 'teal')}{btn('#areas', '분야 보기', 'line')}</div></div></section>
<section class="s2"><div class="wrap split">
  <div><span class="eyebrow">When · 이런 상황이라면</span><h2 style="font-size:clamp(26px,3vw,38px);font-weight:800;letter-spacing:-.03em;margin:10px 0 14px;line-height:1.25">현상은 보이는데<br>원인이 잡히지 않을 때</h2>
  <p style="color:var(--ink2)">장비 문제는 대부분 한 가지 원인으로 생기지 않습니다. 소프트웨어 설정, 하드웨어 상태, 동작 순서, 제어 값이 겹쳐서 나타납니다. 그래서 한 사람이 네 가지를 함께 봐야 빨리 풀립니다.</p></div>
  <ul class="cases">{"".join(f'<li class="rv">{c}</li>' for c in CASES)}</ul>
</div></section>
<section class="s2" id="areas" style="padding-top:0"><div class="wrap"><div class="head"><div><span class="eyebrow">Areas · 컨설팅 분야</span><h2>여섯 가지 분야</h2></div><p>세정장비 공정을 중심으로, 현장에서 직접 다뤄 온 일들입니다.</p></div>{areas_html}</div></section>
<section class="s2 dark grid-bg"><div class="wrap" style="position:relative;z-index:1"><div class="head"><div><span class="eyebrow">Process · 진행 순서</span><h2>추측 대신,<br>재현되는 근거로</h2></div><p>원인을 찾았다고 말하려면 같은 조건에서 다시 일어나야 합니다.</p></div>{flow_html}{FEE}</div></section>
<section class="s2"><div class="wrap"><div class="head"><div><span class="eyebrow">Engagement · 진행 형태</span><h2>필요한 만큼만</h2></div><p>상황에 맞춰 범위를 정합니다. 아래는 예시이며 상담에서 조정합니다.</p></div>
<div class="engage">{"".join(f'<div class="rv"><span class="k">{k}</span><h3>{t}</h3><p>{d}</p></div>' for k, t, d in ENG)}</div>
<div class="note blue" style="margin-top:24px;max-width:none">지금은 <b>준비 단계</b>로, 사전 상담과 일정 협의만 받고 있습니다. 상담 단계에서는 고객사·장비의 기밀 자료를 받지 않으며, 필요한 경우 비밀유지 약정 후 진행합니다.</div>
</div></section>
<section class="s2" style="padding-top:0"><div class="wrap"><div class="cta-x grid-bg glow">
<div><span class="eyebrow" style="color:var(--teal)">Contact</span><h3 style="margin-top:10px">장비 문제,<br>같이 끝까지 봅시다</h3><p>회사명 없이 현상만 간단히 적어 주셔도 됩니다.</p></div>
<div class="links">{btn('/contact?topic=반도체', '사전 상담 문의', 'teal')}{btn('mailto:' + MAIL + '?subject=%5B%EB%B0%98%EB%8F%84%EC%B2%B4%20%EC%BB%A8%EC%84%A4%ED%8C%85%20%EC%82%AC%EC%A0%84%20%EC%83%81%EB%8B%B4%5D', '메일 보내기', 'line')}</div>
</div></div></section>'''
    PAGES['consulting'] = ('반도체 공정·설비 컨설팅', '20년 반도체 세정장비 공정 경험 — 세정 공정 최적화, 불량 원인 추적, 장비 평가·양산 전환, 시퀀스·물류 로직, 공정 데이터 분석 도구. 준비 중 · 사전 상담 가능.', 'consulting', body)
