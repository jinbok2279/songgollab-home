# -*- coding: utf-8 -*-
"""v4 '엔지니어의 공개 작업실' — 첫 화면(index)과 작업 일지(/log). build.py가 불러 씁니다.
숫자는 STATS 의 기준일 값입니다. 고칠 때 기준일도 같이 바꾸세요."""

AS_OF = '2026.11.12'
STATS = [('42', '일', '첫 줄을 쓴 지 (2026.10.01)'), ('14', '개', '만든 프로그램'), ('238', '번', '버전 업데이트'), ('12', '명', '드라이브 콘솔 테스터'), ('63', '곳', '아이랑이 열린 동네')]

# 날짜, 프로그램(slug, 이름), 버전, 제목, 내용, 종류(new/fix/ship/milestone)
LOG = [
 ('11.12', ('', '송골랩'), '', '홈페이지 이사 · songgollab.co.kr', '블로그에 얹혀 있던 홈페이지를 직접 만든 사이트로 옮겼습니다. 블로그는 블로그대로 남깁니다.', 'milestone'),
 ('11.12', ('drive-console', '드라이브 콘솔'), '', '비공개 테스트 12명 · 14일 카운트 시작', '구글 정식 출시 조건(테스터 12명이 14일 이상)을 채우는 중입니다.', 'ship'),
 ('11월', ('drive-console', '드라이브 콘솔'), 'v1.3.57', '구글 필수 설정 반영', '안드로이드 최신 기준(targetSdk 36)과 큰 화면 가로 고정을 맞췄습니다. 화면·기능 변화 없음.', 'fix'),
 ('11.10', ('program-ai-team', 'AI Team'), 'v4.6.0', '모두 같이 일하기 실험', '등급을 끄고 모든 AI가 일을 조각내 고르게 나눠 맡는 2주 실험을 시작했습니다.', 'new'),
 ('11.10', ('program-stock', '주식자동매매'), 'v0.4.13', '판단 기준을 하나로', '설정을 단순하게 정리하고 진입 기준을 되돌렸습니다.', 'fix'),
 ('11.09', ('project-control', '중앙관제'), 'v1.17.0', '영화 같은 화면 · 오늘의 뉴스', '창이 열릴 때의 효과와 빛나는 연결선, 첫 화면 뉴스 카드를 넣었습니다.', 'new'),
 ('11.09', ('program-ai-team', 'AI Team'), 'v4.5.0', '지시 한 번 → 영상 → 승인 → 게시', '말 한 번으로 영상을 만들고, 승인하면 SNS에 바로 올라갑니다.', 'new'),
 ('11.09', ('project-home-iot', '송골집 IoT'), 'v2.6.4', '월패드에 라디오', '월패드 화면에서 라디오를 틀고, 전체 화면과 앱 설치를 지원합니다.', 'new'),
 ('11.08', ('project-control', '중앙관제'), 'v1.14 ~ 1.16', '메일 관제 · 방마다 지금', '광고 메일 자동 정리, 관제 안에서 메일 읽기, 송골집 방별 현재 상태.', 'new'),
 ('11.08', ('project-commerce', '알리 소싱 도우미'), 'v2.1.0', '네이버 노출 최적화', '키워드 점수와 AI 상품명, 마진 계산을 다듬었습니다.', 'new'),
 ('11.08', ('program-invest', '투자비 관리'), 'v2.0.1', '구매 내역 자동 가져오기', '매주 모인 주문 기록을 1분마다 확인해 새 것만 반영합니다.', 'new'),
 ('11.08', ('project-home-iot', '송골집 IoT'), 'v2.6.3', 'HA 지킴이', '집 안 서버가 멈추면 알아채고 되살리는 감시 기능을 넣었습니다.', 'fix'),
 ('11.07', ('project-home-iot', '송골집 IoT'), 'v2.6.2', '사람 감지 조명', '사람이 들어오면 켜지고 나가면 꺼지는 조명을 실제로 쓰기 시작했습니다.', 'new'),
 ('11.03', ('project-commerce', '알리 소싱 도우미'), 'v2.0.0', '네이버 전용으로 전환', '쿠팡판을 마무리하고 스마트스토어 전용으로 다시 짰습니다.', 'milestone'),
 ('11.03', ('program-coin', '코인자동매매'), 'v0.3.6', '매매 실험실', '규칙을 바꿔 보며 결과를 비교하는 실험실을 만들었습니다.', 'new'),
 ('11.02', ('airang', '아이랑'), '', '서울·인천·충남까지', '서울 25개 구, 인천 5곳, 충남 2곳이 열렸습니다.', 'milestone'),
 ('11.02', ('', '송골랩'), '', '사업자 등록', '송골랩이 개인사업자로 정식 출발했습니다.', 'milestone'),
 ('10.31', ('program-stock', '주식자동매매'), 'v0.4.8', '금감원 공시 연동', '공시를 함께 보고 판단합니다.', 'new'),
 ('10.30', ('airang', '아이랑'), '', '아이랑 경기 · 이름을 바꾸다', '용인 정보 모음을 「아이랑」으로 바꾸고 경기도 도시로 넓혔습니다.', 'milestone'),
 ('10.30', ('program-sns', 'SNS 통합관리'), 'v0.4 ~ 0.6', '글쓰기 · 예약 · 관제 연동', '하루에 여섯 번 버전을 올렸습니다.', 'new'),
 ('10.29', ('drive-console', '드라이브 콘솔'), 'v1.3.53', '플레이스토어판', '부르는 이름 바꾸기, 첫 실행 안전 운전 안내, 주행 중 영상 자동 가림.', 'ship'),
 ('10.29', ('airang', '아이랑'), 'v1.0.59b', '7벌을 1벌로', '도시마다 따로 있던 앱 7벌을 원본 하나로 합쳤습니다.', 'fix'),
 ('10.24', ('program-coin', '코인자동매매'), 'v0.3.2 ~ 0.3.4', '자동 업데이트 · 신규 상장 대응', '', 'new'),
 ('10.11', ('project-home-iot', '송골집 IoT'), '', 'IoT 이야기 영상 5편', 'IoT가 무엇인지 40초 영상 다섯 편으로 정리했습니다.', 'ship'),
 ('10.08', ('airang', '아이랑'), '', '무료 시범 운영 시작', '첫날 하루 방문자 89명.', 'ship'),
 ('10.04', ('program-lagrills', '라그릴스 허브'), 'v2.6', '첫 사업장 설치', '바베큐장 에어컨을 매장 PC 한 화면으로. 공사 없이 이틀.', 'ship'),
 ('10.02', ('project-home-iot', '송골집 IoT'), 'v1', '우리 집 자동화 구성안', '집 안의 모든 기기를 한 화면에서. 부품은 최대한 저렴하게.', 'new'),
 ('10.01', ('', '송골랩'), '', '첫 줄', '퇴근 뒤와 쉬는 날, AI 개발 도구와 함께 첫 프로그램을 쓰기 시작했습니다.', 'milestone'),
]
KIND = {'new': ('새 기능', 'k-new'), 'fix': ('고침', 'k-fix'), 'ship': ('공개', 'k-ship'), 'milestone': ('이정표', 'k-ms')}

NOW = [('작업 중', '드라이브 콘솔', '정식 출시 준비 · 비공개 테스트 14일 중'), ('실험 중', 'AI Team', '모든 AI가 같이 일하기 · 2주'), ('실증 중', '송골집 IoT', '사람 감지 조명 · 월패드 라디오'), ('준비 중', 'IoT 비닐하우스', '아치형 하우스 짓기부터')]

def log_items(items):
    out = []
    for d, (slug, prog), ver, t, s, k in items:
        kl, kc = KIND[k]
        p = f'<a href="/{slug}">{prog}</a>' if slug else f'<span>{prog}</span>'
        out.append(f'''<li class="rv"><time>{d}</time><div class="lg"><div class="lg-top"><span class="kb {kc}">{kl}</span>{p}{f'<code>{ver}</code>' if ver else ''}</div><b>{t}</b>{f'<p>{s}</p>' if s else ''}</div></li>''')
    return '<ol class="wlog">' + ''.join(out) + '</ol>'

def add(g):
    PAGES, btn, BLOG, MAIL = g['PAGES'], g['btn'], g['BLOG'], g['MAIL']
    import programs as PG

    now_html = ''.join(f'<li><span class="st">{a}</span><b>{b}</b><em>{c}</em></li>' for a, b, c in NOW)
    recent = ''.join(f'<li><time>{d}</time><b>{prog}</b><code>{ver or "—"}</code><span>{t}</span></li>' for d, (_, prog), ver, t, _s, _k in LOG[2:7])
    hero = f'''<section class="ws-hero soft"><div class="wrap">
<div>
  <span class="eyebrow">Songgol Lab · Open Workshop</span>
  <h1>20년 동안 반도체 장비를 고쳤습니다.<br><span class="grad">지금은 생활을 고칩니다.</span></h1>
  <p class="lead">송골랩은 한 엔지니어의 <b>공개 작업실</b>입니다. 집·차·가게에서 불편한 걸 찾으면 프로그램으로 만들고, 직접 쓰면서 고치고, 그 과정을 전부 여기에 남깁니다.</p>
  <div class="cta">{btn('/log', '작업 일지 보기 →')}{btn('#try', '지금 써 보기', 'line')}</div>
</div>
<div class="bench" aria-label="작업대 현황">
  <div class="bench-top"><span class="dots"><i></i><i></i><i></i></span><span class="mono">songgollab — workbench</span><span class="live"><i></i>LIVE</span></div>
  <div class="bench-img"><img src="/assets/drive-console.jpg" alt="작업 중인 드라이브 콘솔 화면"><span class="tag">지금 작업대 위 · 드라이브 콘솔</span></div>
  <ul class="bench-now">{now_html}</ul>
  <div class="bench-sub mono">최근 반영</div>
  <ul class="bench-log">{recent}</ul>
</div>
</div></section>'''

    stats = '<section class="ws-stats"><div class="wrap"><div class="nums">' + ''.join(
        f'<div class="rv"><b>{n}<small>{u}</small></b><span>{t}</span></div>' for n, u, t in STATS) + f'</div><p class="asof mono">{AS_OF} 기준</p></div></section>'

    log_sec = f'''<section class="s2"><div class="wrap">
<div class="head"><div><span class="eyebrow">Work log · 작업 일지</span><h2>이번 주 작업대에서<br>있었던 일</h2></div>
<p>잘 된 것도, 고친 것도 그대로 적습니다. 버전 번호가 바뀔 때마다 한 줄씩 쌓입니다.</p></div>
{log_items(LOG[:9])}
<p style="margin-top:26px"><a class="more" style="font-weight:700;color:var(--blue)" href="/log">작업 일지 전체 보기 →</a></p>
</div></section>'''

    try_sec = f'''<section class="s2 white" id="try"><div class="wrap">
<div class="head"><div><span class="eyebrow">Try it · 써 보기</span><h2>작업실에서 나온 것,<br>지금 바로 써 보세요</h2></div><p>둘 다 무료입니다. 써 보시고 불편한 점을 알려 주시면 다음 작업 일지에 올라갑니다.</p></div>
<div class="tries">
  <a class="try rv" href="/drive-console"><div class="im" style="background-image:url('/assets/drive-console.jpg')"></div>
    <div class="tx"><span class="badge amber">테스터 모집 · 무료</span><h3>드라이브 콘솔</h3><p>남는 안드로이드 태블릿·휴대폰을 차 계기판으로. 고장 코드를 읽고 원인과 점검 순서까지 보여 줍니다.</p><span class="go">테스터 신청하기 →</span></div></a>
  <a class="try rv" href="/airang"><div class="im" style="background-image:url('/assets/airang-phone.jpg');background-position:top"></div>
    <div class="tx"><span class="badge">공개 서비스 · 63곳</span><h3>아이랑</h3><p>아이 키우는 집의 동네 정보를 매일 아침 자동으로 모아 한 화면에. 가입 없이 바로 열립니다.</p><span class="go">우리 동네 고르기 →</span></div></a>
</div></div></section>'''

    bench_list = ''.join(
        f'<a class="tool rv" href="/{s}"><span class="dot {st}"></span><b>{n}</b><em>{stl}</em><code>{v if v != "—" else ""}</code></a>'
        for s, n, c, st, stl, pl, v, one, art in PG.P)
    tools_sec = f'''<section class="s2"><div class="wrap">
<div class="head"><div><span class="eyebrow">On the bench · 작업대 위의 것들</span><h2>지금까지 만든 14개</h2></div>
<p>공개 서비스부터 집·가게의 IoT, 운영을 돕는 도구, 개인 연구, 기획 중인 것까지. 눌러서 자세히 보세요.</p></div>
<div class="tools">{bench_list}</div>
<p style="margin-top:22px"><a class="more" style="font-weight:700;color:var(--blue)" href="/projects">프로그램 자세히 보기 →</a></p>
</div></section>'''

    import home as H
    semi = f'''<section class="s2 white" id="semi"><div class="wrap">
<div class="semi" style="box-shadow:none;border:0;padding:0;background:transparent">
  <div><span class="eyebrow">Semiconductor · 반도체 세정장비</span>
  <h2>보이지 않는 원인까지<br>끝까지 추적합니다</h2>
  <p>이 작업실의 시작은 반도체 세정장비 현장입니다. 20년 동안 장비의 소프트웨어·하드웨어·동작 순서·제어를 함께 엮어 불량의 원인을 찾아 왔습니다. 그 일을 따로 정리했습니다.</p>
  <div class="status"><i></i>반도체 공정·설비 컨설팅 준비 중 · 사전 상담 가능</div>
  <div class="cta" style="display:flex;gap:10px;margin-top:22px;flex-wrap:wrap">{btn('/consulting', '반도체 세정장비 보기 →')}{btn('/contact?topic=반도체', '사전 상담', 'line')}</div></div>
  <div><div class="panel"><div class="panel-head"><span>WAFER MAP · INSPECTION</span><b>● ANALYZING</b></div>{H.wafer_svg()}<span class="panel-note">설명용 일러스트 · 실제 데이터 아님</span></div></div>
</div>
<div style="margin-top:40px">{H.SEMI['areas']}</div>
</div></section>'''

    owner = f'''<section class="s2"><div class="wrap owner">
<div class="ph"><div class="ph-slot"><svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><rect x="3" y="6" width="18" height="14" rx="2"/><circle cx="12" cy="13" r="4"/><path d="M8 6l2-3h4l2 3"/></svg><span>작업 사진 자리</span></div></div>
<div><span class="eyebrow">The engineer · 작업실 주인</span><h2>장비 앞에서 20년,<br>원인을 끝까지 찾던 사람</h2>
<p>반도체 세정장비 공정 현장에서 장비의 소프트웨어·하드웨어·동작 순서·제어를 함께 엮어 불량의 원인을 찾아 왔습니다. 그 방식 그대로 — 왜 필요한지부터 묻고, 직접 써 보고, 재현되는 근거가 있을 때만 다음으로 넘어갑니다.</p>
<div class="principles"><span>먼저 내가 쓴다</span><span>있는 그대로 적는다</span><span>쓰는 동안 계속 고친다</span></div>
<div class="cta" style="display:flex;gap:10px;margin-top:22px;flex-wrap:wrap">{btn('/about', '작업실 소개')}{btn('/consulting', '반도체 세정 공정 →', 'line')}</div></div>
</div></section>'''

    doors = f'''<section class="s2"><div class="wrap doors">
<a class="door rv" href="/drive-console#tester"><span class="eyebrow">Door 1</span><h3>써 보기</h3><p>드라이브 콘솔 테스터 신청, 아이랑 사용, 프로그램 의견 보내기.</p><span class="go">테스터 신청 →</span></a>
<a class="door dark2 rv" href="/contact"><span class="eyebrow">Door 2</span><h3>같이 일하기</h3><p>반도체 세정 공정 사전 상담, 프로그램 개발 의뢰, 협업 제안.</p><span class="go">문의하기 →</span></a>
</div></section>'''

    PAGES['index'] = ('', '송골랩 — 20년 반도체 장비 엔지니어의 공개 작업실. 집·차·가게의 불편을 프로그램으로 만들고 직접 쓰면서 고치는 과정을 작업 일지로 남깁니다.', '',
                      hero + stats + log_sec + try_sec + tools_sec + semi + owner + doors, 'ko', '')

    full = g['hero']([('', '작업 일지')], 'Work log · 작업 일지', '작업대에서<br>있었던 모든 일',
                     f'2026년 10월 1일 첫 줄부터 지금까지. 새 기능, 고친 것, 공개한 것, 이정표를 날짜순으로 남깁니다. 프로그램 이름을 누르면 자세한 소개로 갑니다.')
    legend = '<div class="legend">' + ''.join(f'<span class="kb {c}">{l}</span>' for l, c in KIND.values()) + '</div>'
    PAGES['log'] = ('작업 일지', '송골랩 공개 작업실의 작업 일지 — 2026.10.01 첫 줄부터 프로그램 14개, 버전 업데이트 238번의 기록.', 'log',
                    full + g['sec'](legend + log_items(LOG), cls='tight') + g['band']('다음 줄은 무엇이 될까요?', '필요한 기능이나 불편한 점을 알려 주시면 작업 일지에 올라갑니다.', btn('/contact', '의견 보내기')))
