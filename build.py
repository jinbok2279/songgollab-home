# -*- coding: utf-8 -*-
"""송골랩 홈페이지 하위 페이지 생성기.  python build.py  → 같은 폴더에 *.html 생성
글 내용은 이 파일 안에 있습니다. 고칠 때는 여기서 고치고 다시 실행하세요."""
import os, html
HERE = os.path.dirname(os.path.abspath(__file__))
SITE = 'https://songgollab.co.kr'
BLOG = 'https://songgollab.blogspot.com'
YT = 'https://www.youtube.com/@songgollab'
KAKAO = 'https://open.kakao.com/o/syctg5Qi'
IG = 'https://www.instagram.com/songgollab/'
AIRANG = 'https://airang.songgollab.co.kr'
MAIL = 'songgollab@gmail.com'

BI = 'https://blogger.googleusercontent.com/img/b/R29vZ2xl/'
IMG = {
 'ai': BI + 'AVvXsEgYF-cVpriRrvp1pE8CzI_EFpMgqdgCIDkHM4eo0XBc6Hy3WHJX1DCAoPtAtOmJhU0ve5bRUAZxmDmI6Y3heUMu5jGRPy_3Ff6GHVpwhTgy947GIyePXTtb1QPFVYLx9cNsgowKLixK3_jfquV85Dlj71QOGBGOkOdCpY704tV-w_WCo3Tl1WStaC7YUVQ/s800/sg-ai-concept.jpg',
 'iot': BI + 'AVvXsEgqAsp1mXH7fn9PA8mq-5qxbV_HkqCtQ6sg2JJfbQ2i4nmOqQXOxvgxEWSIQ3D3NPCYnmbH7oEMy-2BYS_PHblt4CAlYSCWBInfnHRszFEjy-6SIPTVD2g2a-IacFK0gORsnN1jk0A7rR3qhVNXWkhbY5NW7j4DUdXWPDpgBp-mxjdPZKiLQENkupKAifI/s800/sg-iot-concept.jpg',
 'auto': BI + 'AVvXsEihQUI4NZxXXvz9ECljExgfCBqdrg4GIQirLOXGKTVriLp4paMLMC_8WRTmsMOMBvTOcit-wsKBH15wEomowefdwMfz4Lgl2V8ngaatvRuHWcO_pGFmAiSYc4WTDUxFs3BEza6qGissqUXNZakBRoVVsKYTlSeRRzSfjTy8u7b-ylQw9TiHUHRy0AahyAE/s800/sg-automation-concept.jpg',
 'dc01': BI + 'AVvXsEic0eTIBWDMmzNk0FbJY8z2Z1l1tfl7i61TOfCkFnItZOYU_UZVBar1Eldf14IY6OzTpqGhPgvDE-t3sT7a5FVSCEQA-tYVerKi7kiAYrcnWRxlO53d7vZrRNo9jMKWJQEnC-GNuBRps44fiYo3LvbHmWUzgEroiEL_oR2auVbFH9kvcp9L3rHfknV5Gbw/s1280/%EB%93%9C%EB%9D%BC%EC%9D%B4%EB%B8%8C%EC%BD%98%EC%86%94_01_%EB%A9%94%EC%9D%B8%ED%99%94%EB%A9%B4_wm.jpg',
 'dc02': BI + 'AVvXsEhDnsujUlL3u122b8MS9E7V-K_06dwrBZ7gNDfqHwkIMfrNzjY9CH5tV2XehHZSXWszc2zKwPcKw7QyarFq7Yl48WTY60x2Ckqa5lpm5DCHIk0n1uOxz5EprASfxyUCuYuxqrcLYh1HSCPqp4cFhjR_nhaW5nWvPER5dAYOaaX3VXnWTFcFbCYXBFYbHYw/s1280/%EB%93%9C%EB%9D%BC%EC%9D%B4%EB%B8%8C%EC%BD%98%EC%86%94_02_%EA%B3%84%EA%B8%B0%ED%8C%90%EB%94%94%EC%9E%90%EC%9D%B8_wm.jpg',
 'dc03': BI + 'AVvXsEjaAFVP3aeY5yBJJp6BGUbhkWCtnfYFcgEKemCTzaxvL7owPOoDoj8Sc6NPvvbHwzyENH50fVTkBgW2KSkZtBH7ni9MDSguv4QPy_cD_3v_kAHeUWvTh5pTzhFMCOEP0lwrAtO-qIcv2poB4ozlLe8vtF-LardryV_daeRhSMg_Qi2JRL6wIRHwSQ0NOYQ/s1280/%EB%93%9C%EB%9D%BC%EC%9D%B4%EB%B8%8C%EC%BD%98%EC%86%94_03_%EB%B6%84%ED%95%A0%ED%99%94%EB%A9%B4_wm.jpg',
 'dc06': BI + 'AVvXsEhnAuSunm7q_-LnVCvWrb1tNQ7zgR0dz7rnrNT9_bDFy2uLiMjHPUIoZIH-0WpcfjLFvd1_FXP1YPaAZz2xqRESbLfetSNfZwTsRu3a_Xr-Xn1SRXKRmgmPcLoy1QsCxwnZRxz2mVuFmjZofzNSDWNd7HMn2mlbNkqgGKFcxTAluklQYxZldE39QUnvgkI/s1280/%EB%93%9C%EB%9D%BC%EC%9D%B4%EB%B8%8C%EC%BD%98%EC%86%94_06_%EC%9E%90%EB%B9%84%EC%8A%A4_wm.jpg',
 'dc07': BI + 'AVvXsEiLGjR8mqGRqp7wSaL16vaxVRkhmgWmzSll3jqkT3_22kVfCcwYCqTqnZ0TjBimN48n6TcFtTNxaijEsNaEkz4eDOUgKeADRTzrkorMe8XfcERbnk1DmghVwZD1L9WCuBBfRueWJ9jtNcsuBMnCD8J6y1e5H8eyud6yYNxJOiY1QdLsUngBU_fd4qUVEsU/s1280/%EB%93%9C%EB%9D%BC%EC%9D%B4%EB%B8%8C%EC%BD%98%EC%86%94_07_%EC%B0%A8%EA%B3%84%EB%B6%80_wm.jpg',
 'dc08': BI + 'AVvXsEgrvQMJXH9lSD2tIJrHNnZf7v65YwjNPcS5bzNLC28ZntifJtcIyBKXEEy3bU0XnkwFOWAmPDP0k0dF4SaesITuO8emSFLYOm6achISvGRXOBkRKlJCmvY_i7EyCOsnZ3o2tq_-2y5UgqFWHtPrEDAFfbygSEz9_9_3pvhGkecWmHWCWW-1o08fQqOVUM4/s1280/%EB%93%9C%EB%9D%BC%EC%9D%B4%EB%B8%8C%EC%BD%98%EC%86%94_08_%EC%84%A4%EC%A0%95_wm.jpg',
 'dc04': BI + 'AVvXsEgkHLiUjXIBvXTsXL95LuHfm4e93XLOdUVlHxEaSShyphenhyphenf3uIQj9Qon9AVYY3FkEB86QHmvrKvUFZSEyLHn7HJqpwgCA352Zo2y9tBJSLLNurX1iBTRYEoL1SInGvXUUofUhm1ToNJuXqQy1ZiGAtdZaVYf4ZDcLzFlmRx5IVkd3MrlvpWqhyphenhyphenjAUralsvaFo/s1280/%EB%93%9C%EB%9D%BC%EC%9D%B4%EB%B8%8C%EC%BD%98%EC%86%94_04_%EC%B0%A8%EB%9F%89%EC%A0%95%EB%B3%B4_K7_wm.jpg',
 'dc05': BI + 'AVvXsEgRcz7Qn3F3ychUkYvMAwRCBC8rFujfFEcUU0rTpTeKanQktH4p785QGH87F_vQokp_zrLOizETJYL4w85_9MpWLlnQg99Ps9v1Aq4tzEMVhBRtGiamppWQJBhwXhEA1mZGonqzRYJOr08zmdu9mumZYDtpqrqpgMa4dW4Y5AoTZ4Dpitb6orCo4VzscnM/s1280/%EB%93%9C%EB%9D%BC%EC%9D%B4%EB%B8%8C%EC%BD%98%EC%86%94_05_%EC%B0%A8%EB%9F%89%EC%A0%95%EB%B3%B4_%EB%94%94%EC%A0%A4_wm.jpg',
}
def lh(i, w=1280): return f'https://lh3.googleusercontent.com/d/{i}=w{w}'

# ---------- 공통 틀 ----------
NAV = [('log', '작업 일지'), ('projects', '프로그램'), ('services', '써 보기'), ('consulting', '반도체'), ('about', '소개')]

def page(slug, title, desc, body, on='', lang='ko', tail=''):
    def _item(k, v):
        cls = ' class=on' if k == on else ''
        if k != 'projects':
            return f'<a href="/{k}"{cls}>{v}</a>'
        import programs as _P
        groups = ''
        for ck, cn in _P.CATS[1:]:
            rows = ''.join(f'<a href="/{p[0]}"><span class="dot {p[3]}"></span>{p[1]}<em>{p[4]}</em></a>' for p in _P.P if p[2] == ck)
            groups += f'<div class="mm-col"><b>{cn}</b>{rows}</div>'
        return f'<div class="has-mm"><a href="/projects"{cls}>{v} ▾</a><div class="mm"><div class="mm-in">{groups}<a class="mm-all" href="/projects">프로그램 14개 한눈에 →</a></div></div></div>'
    nav = ''.join(_item(k, v) for k, v in NAV)
    t = f'{title} | 송골랩' if title else '송골랩 SONGGOL LAB'
    url = SITE + ('/' + slug if slug != 'index' else '/')
    return f'''<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(t)}</title>
<meta name="description" content="{html.escape(desc)}">
<meta property="og:title" content="{html.escape(t)}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:image" content="{SITE}/assets/og.jpg">
<meta property="og:url" content="{url}">
<link rel="canonical" href="{url}">
<link rel="icon" href="/assets/favicon.png">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/static/pretendard.min.css">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@500;700&display=swap">
<link rel="stylesheet" href="/assets/site.css">
</head>
<body class="pg-{slug}">
<header class="top" id="top">
  <div class="wrap">
    <a class="brand" href="/"><img src="/assets/logo-symbol.png" alt="송골랩 심벌"><span><b>송골랩</b><small>SONGGOL LAB</small></span></a>
    <nav class="nav" id="nav">{nav}<a class="ext" href="{BLOG}" target="_blank" rel="noopener">블로그</a></nav>
    <a class="btn btn-primary" href="/contact">문의하기</a>
    <button class="menu-btn" aria-label="메뉴 열기" onclick="document.getElementById('nav').classList.toggle('open')">☰</button>
  </div>
</header>
<main>
{body}
</main>
<footer class="foot">
  <div class="wrap">
    <div class="foot-brand">
      <div class="brand"><img src="/assets/logo-symbol.png" alt=""><span><b>송골랩</b><small>SONGGOL LAB</small></span></div>
      <p class="foot-tag">Semiconductor Process &amp; Equipment Engineering · Life-tech Lab</p>
      <p>상호 송골랩 · 대표 이진복 · <a href="mailto:{MAIL}">{MAIL}</a></p>
    </div>
    <div class="foot-cols">
      <div><b>SEMICONDUCTOR</b><a href="/consulting">반도체 세정 공정</a><a href="/consulting#areas">분야</a><a href="/contact?topic=반도체">사전 상담</a></div>
      <div><b>PROGRAMS</b><a href="/projects">프로그램 14개</a><a href="/drive-console">드라이브 콘솔</a><a href="/airang">아이랑</a><a href="/project-home-iot">홈 IoT</a></div>
      <div><b>ABOUT</b><a href="/about">소개</a><a href="/videos">영상</a><a href="{BLOG}" target="_blank" rel="noopener">블로그 ↗</a><a href="/drive-console-privacy">개인정보처리방침</a></div>
    </div>
  </div>
  <div class="wrap foot-bottom"><span>© 2026 SONGGOL LAB. All rights reserved.</span><span class="mono">BUILT IN YONGIN, KR</span></div>
</footer>
<script src="/assets/site.js" defer></script>{tail}
</body>
</html>
'''

def hero(crumbs, eyebrow, h1, lead, ctas='', extra=''):
    c = ' › '.join([f'<a href="/">홈</a>'] + [f'<a href="/{k}">{v}</a>' if k else f'<span>{v}</span>' for k, v in crumbs])
    return f'''<section class="page-hero"><div class="wrap">{extra}<div class="crumb">{c}</div>
<span class="eyebrow">{eyebrow}</span><h1>{h1}</h1><p class="lead">{lead}</p>{f'<div class="cta">{ctas}</div>' if ctas else ''}</div></section>'''

def sec(inner, id='', eyebrow='', h2='', p='', cls=''):
    head = (f'<span class="eyebrow">{eyebrow}</span>' if eyebrow else '') + (f'<h2>{h2}</h2>' if h2 else '') + (f'<p class="p">{p}</p>' if p else '')
    return f'<section class="sec {cls}"{f" id={id}" if id else ""}><div class="wrap">{head}{inner}</div></section>\n'

def btn(href, text, kind='primary', ext=False):
    e = ' target="_blank" rel="noopener"' if ext or href.startswith('http') else ''
    return f'<a class="btn btn-{kind}" href="{href}"{e}>{text}</a>'

def boxes(items, cols=3, num=False):
    out = []
    for i, it in enumerate(items, 1):
        t, s = it[0], it[1]
        out.append(f'<div class="box">{f"<i class=num>{i}</i>" if num else ""}<b>{t}</b><span>{s}</span></div>')
    return f'<div class="g{cols}">{"".join(out)}</div>'

def stats(items): return '<div class="g3">' + ''.join(f'<div class="stat"><b>{a}</b><span>{b}</span></div>' for a, b in items) + '</div>'

def log(items):
    out = []
    for it in items:
        d, t, s = it[:3]
        nx = ' class="next"' if d.startswith('다음') or d == 'Next' else ''
        out.append(f'<li{nx}><em>{d}</em><b>{t}</b><span>{s}</span></li>')
    return f'<ul class="log">{"".join(out)}</ul>'

def tbl(head, rows):
    h = ''.join(f'<th>{x}</th>' for x in head)
    r = ''.join('<tr>' + ''.join(f'<td>{c}</td>' for c in row) + '</tr>' for row in rows)
    return f'<div class="tbl-wrap"><table class="tbl"><thead><tr>{h}</tr></thead><tbody>{r}</tbody></table></div>'

def yt(i, label=''):
    v = f'<div class="video"><iframe src="https://www.youtube-nocookie.com/embed/{i}" title="{html.escape(label or "송골랩 영상")}" loading="lazy" allow="accelerometer; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div>'
    return v + (f'<p class="vlabel">{label}</p>' if label else '<div style="height:22px"></div>')

def gdrive(i, label=''):
    v = f'<div class="video"><iframe src="https://drive.google.com/file/d/{i}/preview" title="{html.escape(label or "영상")}" loading="lazy" allow="autoplay" allowfullscreen></iframe></div>'
    return v + (f'<p class="vlabel">{label}</p>' if label else '<div style="height:22px"></div>')

def figs(items, cls=''):
    out = []
    for src, alt, t, s, *rest in items:
        tall = ' tall' if rest and rest[0] == 'tall' else ''
        out.append(f'<figure class="fig{tall}" style="margin:0"><img src="{src}" alt="{alt}" loading="lazy"><figcaption class="cap"><b>{t}</b><span>{s}</span></figcaption></figure>')
    return f'<div class="figs {cls}">{"".join(out)}</div>'

def steps(items): return '<ol class="steps-v">' + ''.join(f'<li><b>{t}</b><span>{s}</span></li>' for t, s in items) + '</ol>'
def checks(items): return '<ul class="checks">' + ''.join(f'<li>{x}</li>' for x in items) + '</ul>'
def faq(items): return '<div class="faq">' + ''.join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q, a in items) + '</div>'
def toc(items): return '<nav class="toc" aria-label="이 페이지 목차"><div class="wrap">' + ''.join(f'<a href="#{k}">{v}</a>' for k, v in items) + '</div></nav>'

def band(h, p, buttons):
    return f'''<section class="band"><div class="wrap"><div class="cta-band"><div><h3>{h}</h3><p>{p}</p></div><div class="links">{buttons}</div></div></div></section>'''

def note(s, blue=False): return f'<div class="note{" blue" if blue else ""}">{s}</div>'

SAFETY = '드라이브 콘솔이 보여 주는 속도·연비·고장코드 등 차량 정보는 참고용이며, 정확한 점검과 진단은 정비소에서 받으세요. 운전 중에는 화면을 조작하지 말고, 안전 운전의 책임은 운전자에게 있습니다.'
PAGES = {}

# ======================================================================
# 서비스
PAGES['services'] = ('서비스', '송골랩이 만들어 공개한 무료 서비스 — 아이 키우는 집의 동네 정보 아이랑, 태블릿을 차 계기판으로 쓰는 드라이브 콘솔.', 'services',
 hero([('', '서비스')], '서비스 · 상용화 및 테스트 단계', '지금 바로<br>써 볼 수 있어요',
      '송골랩이 만들어 공개한 서비스입니다. 둘 다 무료이고, 써 보신 의견으로 계속 다듬고 있어요.',
      btn('#airang', '아이랑') + btn('#drive', '드라이브 콘솔', 'ghost'))
 + sec(f'''<div class="g2" style="align-items:center;gap:32px">
<div><span class="badge">공개 서비스 · 무료</span><h2>아이랑</h2>
<p class="p">아이 키우는 집을 위한 우리 동네 정보. 학교 일정·급식, 도서관, 유치원, 학원, 동네병원, 놓치기 쉬운 혜택, 주말 행사를 한곳에서. 회원가입이 없고 아이 정보는 휴대폰에만 저장돼요.</p>
<div class="chips"><span>경기 <b>31</b></span><span>서울 <b>25</b></span><span>인천 <b>5</b></span><span>충남 <b>2</b></span><span>차례로 늘어나는 중</span></div>
<div class="links">{btn(AIRANG, '아이랑 열기 ↗')}<a class="more" href="/airang">자세히 보기</a></div></div>
<div>{yt('YRNth4rPD_I', '아이랑 경기 소개 영상')}</div></div>
<div style="margin-top:8px">{boxes([('학교 일정 · 급식', '알레르기 표시까지'), ('도서관 · 유치원', '운영시간, 빈자리'), ('학원 수강료 비교', '동네 학원 한눈에'), ('병원 · 혜택 · 행사', '놓치기 쉬운 정보')], 4)}</div>
<p class="tag-concept" style="margin-top:14px">아이랑은 송골랩이 만든 무료 서비스입니다.</p>''', 'airang')
 + sec(f'''<div class="g2" style="align-items:center;gap:32px">
<div><span class="badge amber">테스트 중 · 테스터 모집 (선착순 20명)</span><h2>드라이브 콘솔</h2>
<p class="p">남는 안드로이드 태블릿·휴대폰을 우리 차 계기판으로. OBD 동글을 꽂으면 속도·연비·고장 코드를 실시간으로 보고, T맵과 유튜브를 나눠 띄울 수 있어요.</p>
<div class="chips"><span>실시간 계기판</span><span>고장 코드 설명</span><span>분할 화면 · 음성</span></div>
<div class="links">{btn('/drive-console#tester', '테스터 신청하기')}<a class="more" href="/drive-console">자세히 보기</a></div></div>
<div>{yt('T9bEMuzRCQA', '드라이브 콘솔 30초 소개')}</div></div>''', 'drive', cls='alt')
 + band('써 보시고 의견을 들려주세요', '불편한 점, 있었으면 하는 기능 모두 반영에 큰 도움이 됩니다.', btn('/contact', '의견 보내기')))

# ======================================================================
# 프로젝트 목록
def pcard(href, img, cap, st, stc, h, p, go):
    return f'''<a class="pcard" href="{href}"><div class="im" style="background-image:url('{img}')">{f'<small>{cap}</small>' if cap else ''}</div>
<div class="tx"><span class="st {stc}">{st}</span><h3>{h}</h3><p>{p}</p><span class="go">{go} →</span></div></a>'''

PAGES['projects'] = ('프로젝트', '송골랩이 지금 개발하고 있는 제품 — 홈 IoT·AI 월패드, 드라이브 콘솔, 아이랑, 라그릴스 허브, 중앙관제, 상품 등록 자동화, IoT 비닐하우스.', 'projects',
 hero([('', '프로젝트')], '프로젝트', '지금 개발하고 있는 제품', '직접 쓰면서 검증 중인 것과 기획 단계의 연구를 구분해서 보여 드려요.')
 + sec('<div class="pcards">' + ''.join([
    pcard('/project-home-iot', IMG['iot'], '콘셉트 이미지 · 실제 화면 아님', '자체 실사용 · 검증', '', '송골집 IoT · AI 월패드', '공사 없이, 우리 집에 맞춘 AI 월패드. 집 구조에 맞춘 관리 화면과 원격 관리.', '자세히'),
    pcard('/project-drive', IMG['dc01'], '개발 중 화면', '테스터 모집 · v1.3.53', '', '드라이브 콘솔', '남는 태블릿을 차 대시보드·내비·진단기로. 고장 코드 약 1만 개 해석.', '개발 기록'),
    pcard('/airang', '/assets/airang-phone.jpg', '', '공개 서비스 · 63곳', '', '아이랑', '아이 키우는 집의 우리 동네 정보. 매일 아침 자동으로 새 정보로 바뀝니다.', '자세히'),
    pcard(f'{BLOG}/2026/10/pc.html', 'https://i.ytimg.com/vi/jSeZK3VLMT4/maxresdefault.jpg', '', '사업장 실증', '', '라그릴스 허브', '셀프 바베큐장의 구역별 에어컨을 매장 PC 한 화면에서 켜고 끕니다.', '설치 기록'),
    pcard('/project-control', IMG['ai'], '콘셉트 이미지 · 실제 화면 아님', '내부 전용', 'int', '중앙관제', '개발 도구와 운영 중인 서비스를 통합 관리하는 내부 소프트웨어.', '자세히'),
    pcard('/project-commerce', IMG['auto'], '콘셉트 이미지 · 기획 단계', '구상 · 기획', 'plan', '상품 등록 자동화', '해외 쇼핑몰 상품을 다듬어 국내 쇼핑몰에 자동으로 올리는 프로그램 구상.', '자세히'),
    pcard('/project-farm', 'https://i.ytimg.com/vi/05GXvZZknDs/maxresdefault.jpg', 'IoT 이야기 영상 화면', '준비 중', 'plan', 'IoT 비닐하우스', '부모님과 함께 짓는 농사에 홈 IoT를 옮겨 오는 프로젝트.', '자세히'),
    pcard('/iot-guide', 'https://i.ytimg.com/vi/jB_N9SyBGMU/maxresdefault.jpg', '', 'IoT 이야기 · 5편', '', 'IoT, 쉽게 알아보기', '감지·전달·판단·동작 네 단계로 이해하는 영상 5편 연재.', '읽기'),
 ]) + '</div>', cls='tight')
 + band('이 중에 관심 가는 게 있나요?', '기술 교류나 협업 제안을 기다립니다.', btn('/contact', '문의하기')))

# ======================================================================
# 홈 IoT 프로젝트
PAGES['project-home-iot'] = ('송골집 IoT · AI 월패드', '공사 없이 우리 집에 맞춘 AI 월패드. 송골집과 셀프 바베큐장 라그릴스에서 직접 써 보며 검증하는 홈 IoT 프로젝트.', 'projects',
 hero([('projects', '프로젝트'), ('', '홈 IoT')], '01 · 대표 프로젝트 · 실증 중', '송골집 IoT · AI 월패드',
      '공사 없이, 우리 집에 맞춘 AI 월패드. 기기 설치부터 집 구조에 맞춘 관리 화면, 원격 관리까지 한 번에 맡습니다. 지금은 우리 집(송골집 2층)과 셀프 바베큐장 라그릴스에서 직접 써 보며 검증하고 있습니다.',
      btn('/contact', '설치 상담 문의') + btn('/iot-guide', 'IoT, 쉽게 알아보기', 'ghost'))
 + toc([('feat', '주요 기능'), ('how', '구성'), ('site', '실증 현장'), ('log', '개발 일지'), ('hist', '개발 이력')])
 + sec(boxes([
    ('홈 · 방 라이브', '시간·날씨·집에 있는 가족 수, 방마다 조명과 온도를 큰 카드로 봅니다.'),
    ('3D 평면도', '집 모양 그대로 보고, 방을 누르면 그 방의 기기와 조명 스위치가 나옵니다.'),
    ('가족지킴이', '가족이 동의한 휴대폰 위치와 배터리를 지도에서 확인합니다.'),
    ('에너지', '전력 센서로 잰 실제 값으로 가전별 전기 사용량과 요금을 봅니다.'),
    ('자동화', '조건이 맞으면 알아서 켜고 끕니다. 센서가 없는 규칙은 작동하는 척하지 않습니다.'),
    ('자비스 음성 비서', '"자비스"라고 부르면 듣고, 대답은 태블릿이나 구글 스피커로 들려줍니다.'),
    ('가전 관리', '냉장고·세탁기·TV·로봇청소기를 연결해 상태와 세탁 끝 알림을 받습니다.'),
    ('I/O 체크', '공장 설비 점검처럼, 등록된 기기가 정상인지 한눈에 봅니다.'),
    ('설정 공유', '노트북과 태블릿이 같은 설정을 쓰고, 한쪽에서 바꾸면 다른 쪽도 바뀝니다.')]), 'feat', '주요 기능', '한 화면에서 집 전체를')
 + sec(boxes([
    ('집 안 서버', '노트북 속 가상 서버에서 Home Assistant가 브랜드가 다른 기기를 하나로 묶습니다.'),
    ('관리 화면', '직접 만든 송골집 화면 서버가 우리 집 평면도에 맞춘 화면을 띄웁니다.'),
    ('태블릿 · 휴대폰', '벽에 붙인 태블릿과 가족 휴대폰으로 보고, 밖에서도 안전하게 접속합니다.')], 3, True), 'how', '구성', '이렇게 돌아갑니다', cls='tight')
 + sec(boxes([
    ('송골집 (우리 집 2층)', '35년 된 단독주택 2층. 벽 공사 없이 꽂고, 붙이고, 올려 두는 방식으로 자동화하고 있습니다. 관리 화면 v1.12 사용 중.'),
    ('라그릴스 셀프 바베큐장', 'BBQ 사이트 1~9, 객실, 매점 구역별 에어컨을 매장 PC 한 화면에서 켜고 끕니다. 허브 v2.6, 2026년 10월 4일 설치(2일 작업).')], 2)
    + '<div class="g2" style="margin-top:22px">' + f'<div>{yt("jSeZK3VLMT4", "라그릴스 허브 v2.6 소개")}</div><div>{yt("oSnE9LrclWM", "셀프 바베큐장 라그릴스 소개")}</div></div>'
    + f'<p><a class="more" style="font-weight:700;color:var(--blue)" href="{BLOG}/2026/10/pc.html" target="_blank" rel="noopener">라그릴스 설치기 전체 글 보기 →</a></p>', 'site', '실증 현장', '직접 써 보며 검증합니다', cls='alt')
 + sec(log([
    ('2026.10.02', '시작 — 우리 집 자동화 구성안 v1', '출발점은 단순했습니다. 집 안의 모든 기기를 한 화면에서 보고, 자동 제어로 전기를 아끼는 것. 그리고 부품은 최대한 저렴하게. 전기 공사 없이 2층만 자동화하기로 정했습니다.'),
    ('2026.10.05', '2층 구조 확정, 3D 평면도', '로봇청소기 지도와 집 사진으로 2층을 3D로 그렸습니다. 방을 누르면 그 방의 조명과 기기가 바로 나옵니다.'),
    ('v1.0 ~ v1.2', 'Home Assistant 첫 연결', '조명·가족지킴이·날씨를 연결하고, 노트북 실행 파일과 태블릿 접속, 3D 속도 개선이 이어졌습니다.'),
    ('v1.3 ~ v1.5', '구글 스피커와 자비스', '구글 스피커를 붙이고 "자비스" 음성 호출을 만들었습니다. 로봇청소기 제어·예약도 들어갔습니다.'),
    ('v1.6 ~ v1.7', '가전과 전기 사용량', '냉장고·세탁기 같은 가전을 삼성 SmartThings로 연결하고, 가전별 전기 사용량과 요금, 세탁 끝 알림을 보여 줍니다.'),
    ('v1.8 ~ v1.9', '부딪힌 문제를 하나씩', '연결 거부, 두 번째 모니터에 숨은 보안 경고 창, 태블릿에서만 다르게 보이던 지도까지 원인을 찾아 고쳤습니다. 자비스 마이크와 가족지킴이 실제 지도도 개선했습니다.'),
    ('2026.10.04', '두 번째 현장, 라그릴스', '우리 집에서 써 본 방식을 처음으로 업장에 옮겼습니다. 구역마다 IR 리모컨을 달고 매장 PC에 허브 v2.6을 설치했습니다.'),
    ('v1.10', '설정 맞추기와 I/O 체크', '노트북과 태블릿이 같은 설정을 쓰고, 등록된 기기가 정상인지 한눈에 봅니다. 센서가 없는 기능은 동작하는 척하지 않도록 정리했습니다.'),
    ('2026.10.11', 'IoT 이야기 영상 5편 공개', 'IoT가 무엇인지, 무엇이 좋아지는지 40초 영상 다섯 편으로 정리했습니다. <a href="/iot-guide" style="color:var(--blue);font-weight:700">IoT, 쉽게 알아보기 →</a>'),
    ('다음', '진짜 자동 제어 시작', 'Zigbee 센서와 에어컨 리모컨을 달아 방마다 재실·온도에 따라 움직이게 합니다. 라그릴스는 전 구역 전등, 예약 시간 연동, 에어컨 전력 확인으로 넓힙니다.')]), 'log', '개발 일지', '어떻게 만들어 왔나')
 + sec(tbl(['버전', '추가된 것'], [
    ('v1.0 ~ 1.2', 'Home Assistant 연결, 조명·가족지킴이·날씨, 태블릿 접속, 3D 평면도'),
    ('v1.3 ~ 1.5', '구글 스피커 연결, 자비스 음성 호출, 로봇청소기 제어·예약'),
    ('v1.6 ~ 1.7', '가전 관리, 가전별 전기 사용량·요금, 삼성 SmartThings 연결'),
    ('v1.8 ~ 1.9', '자비스 마이크 개선, 가족지킴이 실제 지도'),
    ('v1.10', '노트북·태블릿 설정 맞추기, I/O 체크, 방마다 기기 추가·삭제'),
    ('v1.12', '지금 쓰고 있는 버전'),
    ('라그릴스 v2.6', '객실·BBQ 사이트·매점 에어컨 통합 제어 (2026.10.04 설치)')]), 'hist', '개발 이력', '버전별 정리', cls='tight')
 + band('우리 집·우리 가게에도 적용해 보세요', '공사 없이 설치하고, 집 구조에 맞춘 화면을 만들어 드립니다.', btn('/contact', '설치 상담 문의') + btn(YT, '유튜브', 'ghost')))

# ======================================================================
# 드라이브 콘솔 개발 기록
PAGES['project-drive'] = ('드라이브 콘솔 개발 기록', '남는 태블릿을 차 대시보드·내비·진단기로. 3D 계기판, T맵 분할 화면, 인터넷 라디오, 음성 비서, OBD 진단을 담은 드라이브 콘솔의 개발 기록.', 'projects',
 hero([('projects', '프로젝트'), ('', '드라이브 콘솔')], '04 · 모빌리티 · 테스터 모집 · v1.3.53', '드라이브 콘솔 개발 기록',
      '집에서 쉬고 있는 태블릿을 내 차의 대시보드·내비·진단기로. 3D 계기판, T맵 분할 화면, 인터넷 라디오, 음성 비서, OBD 차량 진단을 태블릿 하나에 담았습니다. 실제 차(2017 올뉴K7 3.0 LPi)에서 OBD 연결과 고장 코드 읽기까지 확인했습니다.',
      btn('/drive-console#tester', '테스터 신청하기') + btn('/drive-console', '사용 안내 보기', 'ghost'))
 + sec(stats([('6 화면', '메인·프로그램·차량 정보·음성 비서·차계부·설정'), ('약 1만', '고장 코드 해석 · 현대·기아 427 · 국제 표준 9,415'), ('3종', '연료별 진단 · 가솔린 · 디젤 · LPi')]), cls='tight')
 + toc([('video', '영상'), ('tour', '화면 둘러보기'), ('diag', '진단'), ('how', '구성'), ('log', '개발 일지'), ('hist', '개발 이력')])
 + sec('<div class="g2">' + f'<div><h3 style="margin-top:0">30초로 보는 드라이브 콘솔</h3>{yt("T9bEMuzRCQA", "실시간 계기판, 고장 코드 설명, 차계부, 휴대폰 화면, 주행 중 자동 가림")}</div><div><h3 style="margin-top:0">3분 만에 보는 v1.3</h3>{yt("rpFFTn9Ux6Q", "메인 화면부터 분할 화면, 차량 정보, 고장 코드, 음성 비서, 차계부까지")}</div></div>', 'video', '영상', '영상으로 보기')
 + sec(figs([
    (IMG['dc01'], '드라이브 콘솔 메인 화면', '메인 화면 — 운전에 필요한 것만 크게', '왼쪽은 차량 상태(건강 점수·냉각수·연료 보정·회전수), 가운데는 GPS 속도로 움직이는 3D 계기판, 오른쪽은 KBS·MBC·SBS·CBS 8개 채널 인터넷 라디오. 위쪽에는 날씨·미세먼지와 인터넷·OBD 연결 상태가 보입니다.'),
    (IMG['dc02'], '계기판 디자인 6가지', '계기판 디자인 6가지 + 기본형', '3D 도로·크롬·골드·레드·유리판·길안내 바닥 중에서 설정에서 바로 고릅니다. 스킨마다 별빛 색과 도로 위 3D 차량이 달라지고, 속도가 바뀔 때만 다시 그려 태블릿 부담을 줄였습니다.'),
    (IMG['dc03'], 'T맵 분할 화면', '분할 화면 — 왼쪽 T맵 + 오른쪽 앱', '유튜브·음악 같은 앱을 내비와 같이 씁니다. 시속 8km가 넘으면 오른쪽 영상 앱을 자동으로 가리고, 지도와 소리는 그대로 둡니다(도로교통법 49조, 기본값 켜짐).'),
    (IMG['dc06'], '음성 비서 화면', '음성 비서', '"송골랩, 차 상태 알려줘", "쿨FM 틀어줘", "주유 5만 원 기록해줘" — 손 대지 않고 조작합니다.'),
    (IMG['dc07'], '차계부 화면', '차계부', '주유·정비 기록과 이번 달 지출, 엔진오일·보험·정기 검사 남은 기간을 한눈에.'),
    (IMG['dc08'], '설정 화면', '설정', 'OBD 연결(블루투스·Wi-Fi), 차량 등록, 계기판 디자인, 주행 중 영상 가림, 음성 비서 크기, 부르는 이름까지 한 화면에서 바꿉니다.')]), 'tour', '화면 둘러보기', '실제 앱 화면', cls='alt')
 + sec(figs([(IMG['dc04'], '차량 정보 화면 (올뉴K7)', '차량 정보 (2017 올뉴K7 3.0 LPi)', '냉간·예열 후 공회전·주행 중마다 다른 정상 범위로 판정하고, 여러 값을 묶어 "가능성 높은 원인 → 의심 부품 → 조치 순서"로 안내합니다. 며칠 타면 이 차의 평소값을 배워 달라지면 알려 줍니다.')], 'one')
    + '<h3>고장 코드: 뜻에서 조치 순서까지</h3>' + boxes([
        ('읽기', '엔진 저장·대기·영구 코드 + ABS·에어백·변속기 등 8개 장치'),
        ('뜻 찾기', '연료별 사전 → 현대·기아 427개 → 국제 표준 9,415개 순서'),
        ('당시 상황', '고장 당시 기록(냉각수·회전수·차속·부하)으로 상황 해석'),
        ('조치', '가장 의심되는 부품과 점검 순서, 위험도 3단계')], 4, True)
    + '<h3>v1.3 새 기능: 연료에 맞춘 진단</h3>'
    + figs([(IMG['dc05'], '디젤 차량 정보 화면', '디젤 차량 예시 (2019 현대 싼타페)', '매연 필터(DPF) 차압이 높으면 원인·의심 부품·조치 순서까지 바로 보여 줍니다. 예: "고속도로 20~30분 주행 → 그래도 안 되면 정비소 강제 재생".')], 'one')
    + '<div style="height:16px"></div>' + boxes([
        ('가솔린', '직분사(GDI) 자동 인식, 연료펌프·증발가스·터보 코드 약 40개, 연료 보정·산소 센서·촉매 판정'),
        ('디젤', 'DPF 차압·재생 필요도, 커먼레일 압력·EGR·과급압·요소수, 관련 코드 약 100개'),
        ('LPi', '올뉴K7 3.0 LPi 전용 기준, LPG 펌프·필터·펌프 드라이버 원인 분석')])
    + '<p class="p" style="margin-top:14px">연료는 차량 등록에서 고른 값을 먼저 쓰고, 없으면 ECU가 알려 주는 연료 종류로 자동 판별합니다.</p>', 'diag', '차량 진단', '값을 상황에 맞게 판정')
 + sec(boxes([
    ('차량 ECU', '엔진·변속기·ABS·에어백 등이 실시간 값과 고장 코드를 보관'),
    ('OBD 동글', '운전석 아래 단자에 꽂는 ELM327 동글, 블루투스 또는 Wi-Fi'),
    ('드라이브 콘솔 앱', '값 판정·원인 분석·고장 코드 해석, 계기판·라디오·음성 비서'),
    ('태블릿 안에서 처리', '차량 데이터는 외부 서버로 보내지 않습니다')], 4, True)
    + '<h3>품질 점검 — 누를 수 있는 건 다 눌러 봤어요</h3>' + stats([('75개', '버튼 자동 점검 · 오류 0건'), ('7가지', '연료별 시뮬레이션 · 오류 0건'), ('2,852개', '고장 코드 문구 전수 확인')]), 'how', '구성', '차량 – 동글 – 태블릿', cls='alt')
 + sec(log([
    ('v0.6', '시작 — 대시보드 화면 기본 틀', '처음 손에 있던 건 v0.6 설치 파일 하나였습니다. 여기서부터 화면과 기능을 하나씩 쌓았습니다.'),
    ('v0.9', '계기판과 분할 화면', '3D 계기판 7종, 분할 화면 아래 작은 메뉴(7:3·5:5·3:7), 6개 언어. 가짜 데이터는 모두 걷어 냈습니다.'),
    ('v1.0', 'Wi-Fi OBD 연결', 'OBD 동글에서 회전수·차속·냉각수·배터리 같은 실시간 값을 받아, 순간·평균 연비와 주행 가능 거리를 계산합니다.'),
    ('v1.0.1 ~ v1.0.11', '분할과 음성 비서 다듬기', '왼쪽 T맵 고정 분할, 분할 잠금, 화면 위에 뜨는 음성 비서 링, 앱 안 음성 인식, 시간대별 배경과 일주일 날씨, 떠 있는 창 지원까지 열한 번 고쳤습니다.'),
    ('v1.1', '블루투스 동글과 차량 정보', '블루투스 OBD 동글을 연결하고, 건강 점수·상황별 판정·원인 추정·내 차 평소값 학습을 담은 "차량 정보" 메뉴를 만들었습니다.'),
    ('v1.2', '메인 화면 개편과 인터넷 라디오', '왼쪽 차량 상태 패널, 도로 위 3D 차량, 8개 채널 라디오. 다른 화면에서도 라디오가 계속 나옵니다.'),
    ('v1.2.1', '고장 코드 전부 해석', '올뉴K7 상세 코드 427개와 국제 표준 9,415개를 한국어로. 엔진 외 8개 장치 고장 코드도 읽습니다.'),
    ('v1.2.2 ~ v1.2.3', '안전 먼저', '주행 중 영상 가림막, 화면 전환 정리, 음성 비서 창이 T맵을 가리지 않게. 버튼 75개를 자동 점검해 오류 0건을 확인했습니다.'),
    ('v1.3', '가솔린·디젤·LPi 모두 지원', '연료 자동 판별, 디젤 전용 값과 연료별 정비 사전을 더하고, 설명 문구를 전부 다시 검토했습니다.'),
    ('v1.3.1', '분할 종료 수정', '분할을 끝내면 앱이 앞에 뜰 때까지 확인하고 메인 화면으로 바로 돌아옵니다.'),
    ('v1.3.53', '부르는 이름 바꾸기 · 안전 운전 안내', '음성 비서를 부르는 이름(기본 "송골랩")을 바꿀 수 있고, 처음 실행하면 안전 운전 안내가 한 번 뜹니다.'),
    ('다음', '실차 검증 → 출시', '디젤·가솔린 차로 기준값 보정, 라디오 운영 방식 결정, KC 인증 동글과 함께 파는 패키지, Play 스토어 정책에 맞춘 배포를 준비합니다.')]), 'log', '개발 일지', '어떻게 만들어 왔나')
 + sec(tbl(['버전', '추가된 것'], [
    ('v0.6', '대시보드 화면 기본 틀'), ('v0.9', '3D 계기판 7종, 분할 메뉴, 6개 언어'),
    ('v1.0', 'Wi-Fi OBD, 실시간 차량 값, 연비·주행 가능 거리'),
    ('v1.0.1 ~ 1.0.11', 'T맵 고정 분할, 분할 잠금, 음성 비서 화면, 날씨, 떠 있는 창'),
    ('v1.1 ~ 1.1.1', '블루투스 동글, 차량 정보 메뉴, 원인 추정, 앱 종료 버튼'),
    ('v1.2', '메인 화면 개편, 3D 차량, 인터넷 라디오'),
    ('v1.2.1', '고장 코드 전체 해석, 발생 당시 값 분석, 다른 장치 고장 코드'),
    ('v1.2.2 ~ 1.2.3', '주행 중 영상 가림, 화면 전환 정리, 안전 점검'),
    ('v1.3', '가솔린·디젤·LPi 모두 지원, 연료별 정비 사전, 문구 전체 검토'),
    ('v1.3.1', '분할 종료 후 메인 화면 복귀 수정'),
    ('v1.3.53', '음성 비서 부르는 이름 바꾸기(기본 "송골랩"), 첫 실행 안전 운전 안내, 주행 중 영상 앱 자동 가림 (최신)')]) + note(SAFETY), 'hist', '개발 이력', '버전별 정리', cls='tight')
 + band('먼저 써 보고 싶으신가요?', '출시 전 실차 테스트에 함께할 분을 찾고 있습니다. 차종과 연료를 알려 주세요.', btn('/drive-console#tester', '테스터 신청') + btn('/contact', '문의하기', 'ghost')))

# ======================================================================
# 아이랑
PAGES['airang'] = ('아이랑', "송골랩이 만든 무료 학부모 정보 서비스 '아이랑' — 경기·서울·인천·충남 63곳. 학교 일정·급식, 도서관, 유치원, 학원, 병원, 혜택, 행사를 한 화면에서.", 'projects',
 hero([('projects', '프로젝트'), ('', '아이랑')], '03 · 지역 정보 · 시범 운영', '아이랑 — 우리 동네 아이 정보 한 화면에',
      "송골랩이 만든 무료 학부모 정보 서비스 '아이랑'이 경기·서울·인천·충남 63곳으로 넓어졌어요. 우리 아이 학교 일정과 급식(알레르기 표시), 도서관 운영시간과 인기 도서, 유치원 빈자리, 학원 수강료 비교, 동네 의원·약국, 놓치기 쉬운 출산·양육 혜택, 아이와 갈 공연·행사를 한 화면에서 볼 수 있어요. 회원가입이 없고 아이 정보는 휴대폰에만 저장돼요.",
      btn(AIRANG, '아이랑 열기 ↗') + btn('/contact', '의견 보내기', 'ghost'))
 + toc([('live', '실제 화면'), ('why', '왜 만들었나'), ('feat', '주요 기능'), ('how', '운영 방식'), ('log', '개발 일지'), ('hist', '로드맵')])
 + sec(f'''<div class="g2" style="align-items:start;gap:32px"><div><div style="border:8px solid #0B1220;border-radius:32px;overflow:hidden;max-width:380px;aspect-ratio:9/17;box-shadow:var(--shadow)"><iframe src="{AIRANG}" title="아이랑 실제 화면" loading="lazy" style="width:100%;height:100%;border:0"></iframe></div>
<p class="vlabel"><a href="{AIRANG}" target="_blank" rel="noopener" style="color:var(--blue);font-weight:700">새 창에서 열기 ↗</a></p></div>
<div><div class="chips"><span>경기 <b>31</b></span><span>서울 <b>25</b></span><span>인천 <b>5</b></span><span>충남 <b>2</b></span></div>{yt('y_lwf2FhGaQ', '아이랑 서울 25개 구 소개')}</div></div>''',
    'live', '실제 화면', '지금 운영 중인 화면 그대로', '안에서 눌러 보셔도 됩니다.')
 + sec('', 'why', '왜 만들었나', '부모가 매번 하나씩 찾아 들어가야 했습니다',
    '학교 학사일정은 나이스, 공연·축제는 시청, 프로그램과 열람실은 도서관, 유치원 빈자리는 유치원 알리미, 학원 정보와 채용 공고는 또 다른 곳에 있습니다. 아이랑은 이걸 한 화면에 모았습니다.', 'tight')
 + sec(boxes([('학교 일정', '학교 행사를 D-day로 정리'), ('아이와 함께 가요', '시청 공연·축제, 도서관 프로그램'), ('도서관', '열람실 빈자리, 인기 도서'), ('유치원 찾기', '정원·빈자리·통학버스'),
    ('학원 찾기', '3,400여 곳 검색, 신고 수강료'), ('수강료 비교', '동네·과목별 학원비 중간값'), ('엄마 일자리', '학교·유치원·어린이집 채용'), ('특목·자사고', '입시 시기, 지원 가능 학교')], 4)
    + '<p class="p" style="margin-top:14px">학원 수업 시작·끝 10분 전에 휴대폰 캘린더로 알려 주는 기능도 함께 있습니다.</p>', 'feat', '주요 기능', '여덟 가지 메뉴', cls='alt')
 + sec(boxes([('공공 데이터', '나이스·시청·도서관·교육청 등'), ('자동 수집', '매일 아침 프로그램이 모읍니다'), ('웹페이지', '새 정보로 바로 바뀝니다'), ('부모님 휴대폰', '링크 하나로 엽니다')], 4, True)
    + note('서버와 회원 정보가 없어 운영비가 거의 들지 않고, 사람 손 없이 매일 아침 돌아갑니다. 돈을 벌게 되더라도 <b>개인정보를 받지 않고, 핵심 정보는 무료로 두고, 광고는 광고라고 밝힌다</b>는 세 가지 원칙은 바꾸지 않습니다.', True), 'how', '운영 방식', '매일 아침 자동으로')
 + sec(log([
    ('2026.10 초', '시작 — 엄마들을 위한 교육 정보', '지역 엄마들을 위한 자녀 교육 정보 모음을 구상했습니다. 대상은 용인으로 정하고, 코딩보다 먼저 어디서 어떤 정보를 모을 수 있는지부터 정리했습니다.'),
    ('수집기', '매일 아침 자동 수집', 'GitHub에서 예약 실행되는 수집기를 만들어, 학사일정·행사·도서관·유치원·학원 정보를 매일 아침 모읍니다.'),
    ('웹앱', '설치 없는 웹앱으로 공개', '앱 설치 없이 링크로 열리는 웹앱(PWA)을 먼저 만들었습니다. 아이 별명·학교는 본인 휴대폰에만 저장됩니다.'),
    ('2026.10.08', '무료 시범 운영 시작', '무료·시범 운영으로 공개했습니다.'),
    ('2026.10.09 ~ 10', '첫 반응', '하루 방문자 89명, 90명. 당근 글 올린 뒤 1시간에 49명, 맘카페 글 뒤 1시간에 22명이 들어왔습니다. 많이 본 화면은 홈, 학원 찾기, 유치원, 도서관 순입니다.'),
    ('2026.10.30', '아이랑 경기 — 경기도 도시로 확장', "용인에서 시작한 정보 모음을 '아이랑'으로 이름을 바꾸고 경기도 도시로 넓혔습니다. 입구 주소 airang.songgollab.co.kr 에서 도시를 고르면 됩니다."),
    ('2026.11.02', '서울·인천·충남까지', '서울 25개 구, 인천 5곳(연수·남동·부평·미추홀·계양), 충남 2곳(천안·아산)이 열렸습니다. 입구에서 지역 버튼을 누르고 우리 동네를 고르면 됩니다.'),
    ('2026.11', '경기 31곳 · 모두 63곳', '경기 지역이 31곳으로 늘어 경기·서울·인천·충남 모두 63곳이 되었습니다.'),
    ('다음', '매일 다시 올 이유 만들기', '오늘 우리 아이 급식 메뉴, 유치원 모집 일정 안내, 앱 안 "다음 기능" 투표를 준비합니다.')]), 'log', '개발 일지', '어떻게 만들어 왔나', cls='alt')
 + sec(tbl(['단계', '내용'], [
    ('구상', '용인 대상, 수집 가능한 정보부터 정리'), ('수집기', '공공 데이터 매일 아침 자동 수집'),
    ('웹앱 공개', '여덟 가지 메뉴, 학원 알림, 무료·가입 없음 (2026.10 시범 운영)'),
    ('1단계', '월 1만 명까지 — 급식·유치원 모집 추가, 꾸준한 홍보, 의견 바로 반영'),
    ('2단계', '월 1만~5만 명 — 동네 학원·키즈 업체 광고, 채용 공고 상단 노출 ("광고" 표시)'),
    ('3단계', '월 5만 명 이상 — 도시 계속 늘리기, 지자체·기관 협업')]), 'hist', '개발 이력 · 로드맵', '앞으로의 계획')
 + band('우리 동네를 골라 지금 써 보세요', '무료이고, 가입 없이 바로 열립니다. 필요한 기능이 있으면 알려 주세요.', btn(AIRANG, '아이랑 열기 ↗') + btn('/contact', '의견 보내기', 'ghost')))

# ======================================================================
PAGES['project-control'] = ('중앙관제', '송골랩의 개발 도구와 운영 중인 서비스, 메일과 알림을 통합 관리하는 내부 소프트웨어.', 'projects',
 hero([('projects', '프로젝트'), ('', '중앙관제')], '내부 전용', '송골랩의 시스템을 한곳에서',
      '개발 도구와 운영 중인 서비스, 메일과 알림을 통합 관리하는 내부 소프트웨어입니다. 구성도, 접근 정보, 보안 세부 사항은 공개하지 않습니다.')
 + sec(f'<figure class="fig" style="margin:0;max-width:860px"><img src="{IMG["ai"]}" alt="통합 관리 콘셉트 이미지"><figcaption class="cap"><span>콘셉트 이미지 · 실제 화면 아님</span></figcaption></figure>', cls='tight')
 + sec(boxes([('시스템 상태', '운영 중인 서비스가 잘 돌아가는지 한눈에 봐요.'), ('메일 관리', '서비스로 들어오는 메일과 알림을 정리해요.'), ('보안 우선', '내부 전용으로, 세부 정보는 공개하지 않아요.')]), '', '주요 기능', '운영을 한 화면에')
 + band('다른 프로젝트도 둘러보세요', '송골랩이 지금 만들고 있는 제품들입니다.', btn('/projects', '프로젝트 전체') + btn('/contact', '문의하기', 'ghost')))

PAGES['project-commerce'] = ('상품 등록 자동화', '해외 쇼핑몰 상품을 다듬어 국내 쇼핑몰에 자동으로 올리는 프로그램 구상.', 'projects',
 hero([('projects', '프로젝트'), ('', '상품 등록 자동화')], '05 · 커머스 · 구상 · 기획', '상품 등록 자동화',
      '해외 쇼핑몰에서 상품을 골라 가져오고, 내용을 다듬어 국내 쇼핑몰에 자동으로 올려 주는 프로그램입니다. 재고 없이 시작하는 작은 판매자의 반복 작업을 줄이는 것이 목표입니다.')
 + sec(boxes([('상품 고르기', '배송이 빠른 해외 쇼핑몰에서 팔 만한 상품을 찾습니다.'), ('내용 다듬기', '상품명·설명·사진을 국내 쇼핑몰에 맞게 정리합니다.'),
    ('자동 등록', '쿠팡 같은 국내 쇼핑몰에 상품을 자동으로 올립니다.'), ('재고 없이', '주문이 들어오면 원래 판매처에서 바로 보내는 구조를 검토합니다.')], 4, True), '', '하려는 것', '반복 작업을 줄입니다', cls='tight')
 + sec(log([('2026.10', '구상 시작', '쿠팡에서 재고 없이 운영하는 자동 쇼핑몰을 준비하며, 해외 쇼핑몰 상품 연동 방법을 살펴보고 있습니다. 진행되는 대로 이곳에 기록하겠습니다.')]), '', '개발 일지', '진행 기록')
 + band('판매 자동화, 관심 있으신가요?', '함께 고민할 판매자분을 기다립니다.', btn('/contact', '문의하기')))

PAGES['project-farm'] = ('IoT 비닐하우스', '부모님과 함께 짓는 농사에 홈 IoT를 그대로 옮겨 오는 스마트 농장 프로젝트.', 'projects',
 hero([('projects', '프로젝트'), ('', 'IoT 비닐하우스')], '02 · 스마트 농장 · 준비 중', 'IoT 비닐하우스',
      '부모님과 함께 짓는 농사에 홈 IoT를 그대로 옮겨 오는 프로젝트입니다. 비닐하우스 상태를 멀리서 확인하고, 집과 같은 화면에서 관리하는 것이 목표입니다.')
 + sec(boxes([('하우스 상태 보기', '온도·습도를 휴대폰으로 확인하고, 너무 덥거나 추우면 알림을 받습니다.'), ('홈 IoT와 한 화면', '집에서 쓰는 Home Assistant와 같은 화면에서 하우스까지 봅니다.'),
    ('직접 써 보고 검증', '우리 밭에서 먼저 써 보고, 효과가 확인된 것만 서비스로 만듭니다.')]), '', '하려는 것', '멀리서도 하우스를', cls='tight')
 + sec(log([('2026.10', '프로젝트 등록', '홈 IoT와 연계한 스마트 농장·비닐하우스를 송골랩 프로젝트로 정했습니다. 진행되는 대로 이곳에 기록하겠습니다.')]), '', '개발 일지', '진행 기록')
 + band('농장 IoT, 같이 고민해요', '하우스나 축사에 필요한 기능이 있다면 알려 주세요.', btn('/contact', '의견 보내기') + btn('/project-home-iot', '홈 IoT 프로젝트 보기', 'ghost')))

# ======================================================================
PAGES['iot-guide'] = ('IoT, 쉽게 알아보기', 'IoT는 어려운 기술이 아니라 집이 알아서 챙겨 주는 생활 방식입니다. IoT 이야기 영상 5편으로 정리한 홈 IoT 입문.', 'projects',
 hero([('projects', '프로젝트'), ('', 'IoT, 쉽게 알아보기')], 'IoT 이야기 · 영상 5편', 'IoT, 쉽게 알아보기',
      'IoT는 어려운 기술이 아니라, 집이 알아서 챙겨 주는 생활 방식입니다. 송골랩이 만든 <b>IoT 이야기</b> 영상 5편과 함께 IoT가 무엇인지, 집에 들이면 무엇이 달라지는지 한 페이지에 정리했습니다.')
 + toc([('ep1', 'IoT가 뭐예요?'), ('ep2', '좋아지는 5가지'), ('ep3', '스마트홈의 하루'), ('ep4', '새는 전기 막기'), ('ep5', '부모님 댁 안심'), ('ours', '송골랩은 이렇게')])
 + sec(yt('jB_N9SyBGMU') + boxes([('감지', '센서가 온도, 움직임, 문 열림 같은 변화를 알아챕니다.'), ('전달', '와이파이나 Zigbee 무선으로 집 안 허브에 알립니다.'),
    ('판단', '허브가 정해 둔 규칙대로 지금 할 일을 정합니다.'), ('동작', '조명, 에어컨, 플러그가 실제로 켜지고 꺼집니다.')], 4, True)
    + '<p class="p" style="margin-top:14px">이 네 단계가 이어지면 휴대폰 하나로 집 밖에서도 집 상태를 보고 조절할 수 있습니다.</p>',
    'ep1', 'EP.1', 'IoT가 뭐예요?', 'IoT(사물인터넷)는 집 안의 물건이 인터넷으로 연결돼 스스로 <b>감지하고, 알려 주고, 움직이는</b> 기술입니다. 네 단계만 알면 쉽게 이해됩니다.')
 + sec(yt('rDhGRygyQW4') + boxes([('편리', '말 한마디, 버튼 하나로 조명과 에어컨을 켜고 끕니다.'), ('절약', '빈 방의 전등과 에어컨, 쓰지 않는 기기의 대기전력을 끕니다.'), ('안전', '문 열림이나 이상 상황을 휴대폰으로 바로 알려 줍니다.'),
    ('원격', '집 밖에서도 휴대폰으로 집 상태를 보고 기기를 조절합니다.'), ('자동', '귀가, 외출, 취침처럼 정해 둔 상황이 되면 알아서 움직입니다.')]),
    'ep2', 'EP.2', '설치하면 뭐가 좋아질까?', 'IoT를 들이면 생활이 달라지는 지점을 다섯 가지로 나눠 봤습니다.', 'alt')
 + sec(yt('66hwKAWMw84') + log([('07:00 기상', '하루를 시작합니다', '집 상태는 휴대폰 한 화면에서 확인합니다.'), ('외출', '한 번에 끄기', '버튼 하나로 집 안 전등과 에어컨을 한 번에 끕니다.'),
    ('낮', '빈집 알림', '빈집에 문 열림이나 움직임이 생기면 휴대폰으로 알려 줍니다.'), ('퇴근길', '미리 켜기', '집에 닿기 전에 미리 냉난방을 켜 둡니다.'), ('23:00 취침', '자동으로 끄기', '잠들 때 남은 조명이 자동으로 꺼집니다.')]),
    'ep3', 'EP.3', '스마트홈의 하루', '아침에 일어나서 잠들 때까지, IoT가 설치된 집은 이렇게 움직입니다.')
 + sec(yt('mKFjxUG26es') + boxes([('찾기 · 사용량 화면', '가전별 전기 사용량을 화면으로 보고, 어디서 새는지 찾습니다.'), ('막기 · 자동 규칙', '빈 방 조명 끄기, 쓰지 않는 기기 대기전력 차단을 자동으로 합니다.')], 2)
    + '<p class="p" style="margin-top:14px">실제로 얼마나 아꼈는지는 송골랩 실증 현장의 계절 데이터를 모은 뒤 개발 일지에 숫자로 공개하겠습니다.</p>',
    'ep4', 'EP.4', '켜져 있는 줄도 몰랐던 전기, 막기', '대기전력, 아무도 없는 방의 조명처럼 모르는 사이 새는 전기가 있습니다. IoT는 이 전기를 찾아내고, 알아서 막습니다.', 'alt')
 + sec(yt('05GXvZZknDs') + boxes([('연기 · 누수', '화재 연기나 물샘을 감지하면 바로 알려 줍니다.'), ('문 열림', '현관문이 열리고 닫히는 것을 확인합니다.'), ('온도', '집 안이 너무 춥거나 덥지 않은지 봅니다.'),
    ('생활 리듬 알림', '평소와 다르게 움직임이 없으면 알려 줍니다.'), ('원격 난방', '추운 날 멀리서도 보일러를 켜 드릴 수 있습니다.')]),
    'ep5', 'EP.5', '멀리 계신 부모님 댁, 안심', '따로 사시는 부모님 댁, 늘 마음이 쓰이시죠? 센서 몇 개와 알림만으로 멀리서도 살필 수 있습니다.')
 + sec(boxes([('공사 없이', '벽을 뚫거나 배선을 새로 깔지 않습니다. 꽂고, 붙이고, 올려 두는 방식이라 오래된 집도 괜찮습니다.'), ('우리 집 안 서버', 'Home Assistant 하나로 브랜드가 다른 기기를 묶습니다. 외부 업체 서버가 끊겨도 집은 계속 동작합니다.'),
    ('KC 인증 장비', '남의 집 전기를 만지는 일이라, 국내 인증을 받은 장비만 씁니다.')])
    + '<p class="p" style="margin-top:14px">송골랩은 직접 써 보고 검증한 것만 서비스로 만듭니다. 지금은 우리 집(송골집)과 셀프 바베큐장 라그릴스에서 실증 중입니다.</p>'
    + checks([f'<a href="{BLOG}/2026/10/pc.html" target="_blank" rel="noopener">바베큐장 에어컨, 매장 PC 한 화면으로 묶기 — 라그릴스 설치기</a>',
              f'<a href="{BLOG}/2026/10/iot-iot-ep1.html" target="_blank" rel="noopener">IoT가 뭐예요? — IoT 이야기 EP.1 글로 보기</a>',
              f'<a href="{BLOG}/2026/10/iot-iot-ep2.html" target="_blank" rel="noopener">IoT 설치하면 뭐가 좋아질까? — IoT 이야기 EP.2 글로 보기</a>']),
    'ours', '송골랩의 방식', '송골랩은 이렇게 합니다', cls='alt')
 + band('우리 집에도 IoT, 상담해 보세요', '집 구조와 원하는 기능을 알려 주시면 현장을 확인하고 맞춤으로 제안해 드립니다.', btn('/contact', '설치 상담 문의') + btn('/project-home-iot', '홈 IoT 프로젝트', 'ghost')))

# ======================================================================
PAGES['about'] = ('회사 소개', '송골랩은 2026년 10월 기술 개발을 시작했습니다. 만든 프로그램을 생활과 가게에서 직접 쓰면서 고치고, 쓸모가 확인된 것만 제품으로 다듬습니다.', 'about',
 hero([('', '회사 소개')], '송골랩 소개', '직접 만들고,<br>직접 쓰고, 검증합니다',
      '송골랩은 2026년 10월 기술 개발을 시작했습니다. 만든 프로그램을 생활과 가게에서 직접 쓰면서 고치고, 쓸모가 확인된 것만 제품으로 다듬습니다.')
 + sec('''<div class="g2" style="align-items:center;gap:32px"><div style="background:var(--surface);border:1px solid var(--line);border-radius:24px;padding:40px;display:grid;place-items:center"><img src="/assets/logo-symbol.png" alt="송골랩 심벌" style="width:180px"></div>
<div><span class="eyebrow">이름과 심벌</span><h2>송골, 고향 마을의 이름</h2><p class="p">송골은 고향 마을의 이름입니다. 그 마을에서 홈 IoT 화면 개발을 시작했고, 심벌은 송골의 <b>ㅅ</b>과 <b>ㄱ</b>이 맞물린 모양이에요.</p></div></div>''', cls='tight')
 + sec(boxes([('먼저 우리가 씁니다', '집과 가게에서 직접 써 보고 불편을 고친 뒤에 공개합니다.'), ('있는 그대로 알립니다', '과장된 수치보다 실제 구현 범위와 개발 단계를 그대로 보여 드립니다.'), ('계속 다듬습니다', '써 보신 분들의 의견으로 기능과 화면을 꾸준히 고칩니다.')], 3, True),
    '', '일하는 원칙', '기술의 가치는 실사용에서 확인합니다', cls='alt')
 + sec('''<div class="steps"><div><b>문제 정의</b><span>왜 필요한가</span></div><div><b>기획</b><span>무엇을 만들까</span></div><div><b>디자인</b><span>어떻게 쓸까</span></div><div><b>검토·승인</b><span>개발 기준 확정</span></div><div><b>구현</b><span>기능 개발</span></div><div><b>실사용 검증</b><span>오류와 불편 확인</span></div><div><b>개선·판단</b><span>제품화 검토</span></div></div>
<p class="p" style="margin-top:16px">그리고 다시 1번으로 — 쓰는 동안 계속 반복합니다.</p>''', '', '만드는 방식', '왜 필요한가부터 시작합니다')
 + sec(log([('2026.10', '기술 개발 시작', '홈 IoT 화면과 라그릴스 허브 실사용'), ('2026.10', '아이랑 공개', '용인에서 시작해 경기·서울·인천·충남으로 확장'), ('2026.11', '송골랩 사업자 등록', '드라이브 콘솔 구글 플레이 테스터 모집, 홈페이지 songgollab.co.kr 개설')]), '', '걸어온 길', '지금까지', cls='tight')
 + band('송골랩과 이야기 나눠요', '의견, 기술 교류, 협업 제안 모두 반가워요.', btn('/contact', '문의하기')))

# ======================================================================
CONTACT_FORM = f'''<form class="form" id="cform" novalidate>
<h2 style="margin:0">문의 남기기</h2>
<label>이름<input name="name" autocomplete="name" required></label>
<label>연락처 (이메일 또는 전화)<input name="contact" required></label>
<label>문의 분야<select name="topic"><option>반도체 공정·설비 컨설팅 사전 상담</option><option>드라이브 콘솔 테스터 신청</option><option>서비스 의견 · 아이랑</option><option>서비스 의견 · 드라이브 콘솔</option><option>오류 신고</option><option>프로젝트 의견 · 홈 IoT</option><option>설치 상담 · 홈 IoT</option><option>기술 교류</option><option>협업 · 사업 제안</option><option>기타</option></select></label>
<label>내용<textarea name="body" required placeholder="드라이브 콘솔 테스터 신청은 플레이스토어에서 쓰는 Gmail 주소를 적어 주세요."></textarea></label>
<label class="agree"><input type="checkbox" name="agree" required>문의 답변을 위한 개인정보(이름·연락처) 수집·이용에 동의합니다</label>
<p class="err" id="cerr" role="alert"></p>
<button class="btn btn-primary" type="submit" style="justify-self:start;border:0;cursor:pointer">보내기</button>
<p class="hint">보내기를 누르면 이메일 앱이 열립니다. 이메일 앱에서 한 번 더 보내야 접수됩니다. 받은 정보는 답변에만 쓰고 다른 곳에 넘기지 않습니다.</p>
</form>'''
def way(href, ico, t, s): return f'<a class="box" href="{href}"{" target=_blank rel=noopener" if href.startswith("http") else ""}><div class="ic">{ico}</div><b>{t}</b><span>{s}</span></a>'
SV = lambda d: f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">{d}</svg>'
PAGES['contact'] = ('문의', '테스터 신청, 서비스 의견, 오류 신고, 기술 교류와 협업 제안 — 송골랩에 편한 방법으로 남겨 주세요.', '',
 hero([('', '문의')], '문의', '의견과 제안을<br>기다립니다', '테스터 신청, 서비스 의견, 오류 신고, 기술 교류와 협업 제안 모두 좋아요. 편한 방법으로 남겨 주세요.')
 + sec('<div class="contact-ways">'
    + way(f'mailto:{MAIL}', SV('<rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/>'), '이메일', MAIL)
    + way(KAKAO, SV('<path d="M21 12a8 8 0 0 1-11.6 7.1L4 20l1.1-4.4A8 8 0 1 1 21 12z"/>'), '카카오톡 오픈채팅', '빠른 질문은 여기로')
    + way(IG, SV('<rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="1"/>'), '인스타그램 · 스레드', '@songgollab')
    + '</div>', cls='tight')
 + sec(CONTACT_FORM, 'form', cls='tight'))

# ======================================================================
VID = [
 ('v-drive', '드라이브 콘솔', '태블릿을 차 계기판으로 쓰는 앱', '/drive-console', [
   ('T9bEMuzRCQA', '30초 소개', '드라이브 콘솔 30초 소개', '남는 태블릿을 우리 차 계기판으로'),
   ('rpFFTn9Ux6Q', '기능 설명', '드라이브 콘솔 v1.3 설명', '화면 하나씩 둘러보기'),
   ('wwWg9VWy7Y4', '쇼츠', '테스터 모집', '출시 전 무료 · 선착순 20명')]),
 ('v-airang', '아이랑', '아이 키우는 집의 우리 동네 정보', '/airang', [
   ('YRNth4rPD_I', '소개', '아이랑 경기', '우리 동네 아이 정보 한 화면에'),
   ('y_lwf2FhGaQ', '소개', '아이랑 서울 25개 구', '학교 일정부터 학원비 비교까지'),
   ('uvaTydTX3Bk', '소개', '아이랑 충남 오픈', '천안·아산'),
   ('EiZWybfE3sw', '쇼츠', '아이랑 용인', '사이트 7곳 따로 볼 필요 없어요'),
   ('Jbqbh985kQk', '쇼츠', '아이랑 수원', '지금 문 연 소아과 찾기'),
   ('zJTOv4hFLMo', '쇼츠', '아이랑 성남', '다자녀·출산 지원'),
   ('X1Q4mHa_2GI', '쇼츠', '아이랑 안양', '셋째아 혜택'),
   ('yE315WaIP28', '쇼츠', '아이랑 고양', '이번 주말 어디 가지?'),
   ('H_5AHC9H9ao', '쇼츠', '아이랑 화성', '밤 9시 문 연 약국')]),
 ('v-iot', 'IoT 이야기', '40초로 이해하는 홈 IoT, 5편 연재', '/iot-guide', [
   ('jB_N9SyBGMU', 'EP.1', 'IoT가 뭐예요?', '40초 만에 이해하는 사물인터넷'),
   ('rDhGRygyQW4', 'EP.2', '설치하면 뭐가 좋아질까?', '편리·절약·안전·원격·자동'),
   ('66hwKAWMw84', 'EP.3', '스마트홈의 하루', '아침부터 밤까지'),
   ('mKFjxUG26es', 'EP.4', '켜져 있는 줄도 몰랐던 전기', 'IoT로 막기'),
   ('05GXvZZknDs', 'EP.5', '멀리 계신 부모님 댁', 'IoT로 안심')]),
 ('v-site', '실증 현장', '라그릴스에서 직접 써 보는 모습', '/project-home-iot', [
   ('jSeZK3VLMT4', '허브', '라그릴스 허브 v2.6 소개', '매장 PC 한 화면'),
   ('oSnE9LrclWM', '현장', '셀프 바베큐장 라그릴스 소개', '허브가 설치된 매장')]),
]
vb = ''
for vid, h, p, more, items in VID:
    cards = ''.join(f'<button class="vcard" data-yt="{i}" aria-label="{t} 재생"><div class="th"><img src="https://i.ytimg.com/vi/{i}/hqdefault.jpg" alt="" loading="lazy"></div><div class="tx"><span class="k">{k}</span><b>{t}</b><span>{s}</span></div></button>' for i, k, t, s in items)
    vb += f'<div class="vhead" id="{vid}"><div><h2>{h}</h2><p>{p}</p></div><a class="more" style="font-weight:700;color:var(--blue)" href="{more}">자세히 보기 →</a></div><div class="vgrid">{cards}</div>'
PAGES['videos'] = ('영상', '서비스 소개, 기능 설명, IoT 이야기까지. 송골랩 유튜브 채널의 영상을 주제별로 모았어요.', 'videos',
 hero([('', '영상')], '자료실 · 영상', '송골랩 유튜브', '서비스 소개, 기능 설명, IoT 이야기까지. 송골랩 유튜브 채널의 영상을 주제별로 모았어요. 누르면 이 자리에서 바로 재생돼요.',
      btn(YT, '▶ 채널 구독하기'))
 + toc([('v-drive', '드라이브 콘솔 · 3편'), ('v-airang', '아이랑 · 9편'), ('v-iot', 'IoT 이야기 · 5편'), ('v-site', '실증 현장 · 2편')])
 + sec(vb))

# ======================================================================
# 드라이브 콘솔 사용 안내 (한국어 / English)
def dc_page(L):
    K = L == 'ko'
    T = (lambda ko, en: ko if K else en)
    feat = [(lh('1i5sUHnLETEgypSmjiTJ_a3MbL97nG9mR') if K else lh('1GKcQ0RtmeRp47ZNP0-F1EjGnh-IBe-1a'), T('드라이브 콘솔 메인 화면', 'Drive Console home screen'), T('메인 화면', 'Home'), T('실시간 속도·연비·엔진 상태를 한 화면에서 보고, 가운데 둥근 플레이어로 음악을 들어요. 속도 숫자는 빠르기에 따라 하늘색 → 보라 → 주황 → 빨강으로 바뀌어요.', 'Live speed, fuel economy and engine status on one screen, with a round music player in the middle. The speed number changes colour as you go faster: sky blue, purple, orange, then red.')),
            (lh('1GXZbvv4KpdbXYEgOTP4LfatTRqNwlfui') if K else lh('1sVrVxIRMKypkjhM5QNnFu4hSXBt8pp8f'), T('차량 정보 화면', 'Vehicle info screen'), T('차량 정보', 'Vehicle info'), T('고장 코드를 읽고 차량 상태를 점검해요.', "Read fault codes and check your car's condition.")),
            (lh('1ZNNUD3StYysY9N91nzu8pOYe8bHK0Dvp') if K else lh('1nwa_9clXUDy8MlBAdvEVr214URA5K7_3'), T('차계부 화면', 'Car log screen'), T('차계부', 'Car log'), T('주유·정비 기록을 남기고 다음 정비를 알려 줘요.', 'Keep fuel and maintenance records and get reminders for the next service.')),
            (lh('13n_odlf_UXn00WrBr_btZF4IU321TouN') if K else lh('12m6JLHcNM1DvpKYg4B3lVhE7bN6cNMi2'), T('프로그램 분할 화면', 'Split screen'), T('프로그램 · 분할 화면', 'Apps · split screen'), T('T맵·유튜브 같은 앱 2개를 반반 나눠 써요.', 'Run two apps side by side, such as navigation (Google Maps, Waze…) and YouTube.')),
            (lh('1siuyXfaq3AupDA0xnygZQdeL7gjsYZce') if K else lh('196tQ4fqjTN8l7aq2yHNAlPLKy4siIF2e'), T('내 음악과 사진 앨범 화면', 'My music and photo album'), T('내 음악 · 사진 앨범', 'My music · photo album'), T('내 MP3를 듣고 가족 사진을 띄워요.', 'Play your own MP3s and show family photos.'))]
    phones = [(lh('1s_sumbOrc6l1tFVa0waQxZEdtHGQJ4Z5'), T('휴대폰 가로 메인 화면', 'Phone landscape home screen'), T('휴대폰 가로', 'Phone, landscape'), T('메인 화면', 'Home')),
              (lh('140UtPTVlaoPNGhnYs8vBFoVOOnkHSgKd'), T('휴대폰 가로 차량 정보 화면', 'Phone landscape vehicle info'), T('휴대폰 가로', 'Phone, landscape'), T('차량 정보', 'Vehicle info')),
              (lh('1nvnCD6z0Pv3VXxQya7SohPjrPEPDDj4y', 800), T('휴대폰 세로 메인 화면', 'Phone portrait home screen'), T('휴대폰 세로', 'Phone, portrait'), T('메인 화면', 'Home'), 'tall'),
              (lh('11uF_JEjTdxOFvXTwcxg99k3u_OVoP5WW', 800), T('휴대폰 세로 내 음악 화면', 'Phone portrait my music'), T('휴대폰 세로', 'Phone, portrait'), T('내 음악', 'My music'), 'tall')]
    mail_sub = '드라이브 콘솔 테스터 신청' if K else 'Drive Console tester'
    import urllib.parse as up
    mailto = f'mailto:{MAIL}?subject={up.quote(mail_sub)}&body={up.quote(T("플레이스토어에서 쓰는 Gmail 주소: ", "Gmail address used on Google Play: "))}'
    langlink = '<a class="lang" href="/drive-console-en">🇺🇸 English</a>' if K else '<a class="lang" href="/drive-console">🇰🇷 한국어</a>'
    body = (hero([('services', T('서비스', 'Services')), ('', T('드라이브 콘솔', 'Drive Console'))], T('드라이브 콘솔 · 안드로이드 태블릿 · 테스터 모집', 'Drive Console · Android tablet · Testers wanted'),
        T('남는 태블릿을<br>우리 차 계기판으로', 'Turn a spare tablet<br>into your dashboard'),
        T('안 쓰는 안드로이드 태블릿이나 휴대폰에 블루투스 OBD 동글 하나를 더하면 우리 차 전용 계기판이 됩니다. 구글 플레이 정식 출시 전에 테스터로 먼저 무료로 써 보세요.',
          'Turn a spare Android tablet or phone into your car\'s dashboard. Add a Bluetooth OBD dongle and you get live speed, fuel economy and fault codes. Try it free as a tester before the official Google Play launch.'),
        btn('#tester', T('테스터 신청하기 ↓', 'Become a tester ↓')) + btn('#setup', T('설치 방법 보기', 'See setup'), 'ghost'), langlink)
     + sec(boxes([(T('태블릿 + OBD', 'Tablet/phone + OBD'), T('안 쓰는 안드로이드 태블릿이나 휴대폰과 블루투스 OBD 동글이면 준비 끝', 'A spare Android tablet or phone and a Bluetooth OBD dongle are all you need')),
                  (T('무료 · 선착순 20명', 'Free · first 20'), T('구글 플레이 출시 전 테스터 모집', 'Google Play testers wanted before launch')),
                  (T('한국어 · English', 'English · 한국어'), T('설정 › 화면에서 언어 바꾸기', 'Change the language in Settings › Display'))]), cls='tight')
     + toc([('why', T('왜 OBD인가', 'Why OBD')), ('features', T('할 수 있는 것', 'Features')), ('ready', T('준비물', 'What you need')), ('setup', T('설치 방법', 'Setup')), ('use', T('사용 방법', 'How to use')), ('tester', T('테스터 모집', 'Testers wanted')), ('faq', T('자주 묻는 질문', 'FAQ'))])
     + sec(boxes([(T('고장 코드 실시간 감지', 'Live fault-code detection'), T('OBD 동글을 꽂으면 차가 보내는 고장 코드를 주행 중에도 바로 잡아냅니다.', 'Plug in an OBD dongle and Drive Console picks up the fault codes your car sends, even while you drive.')),
                  (T('분석 · 원인', 'Analysis · cause'), T('코드를 분석해서 무엇이 문제인지 원인까지 보여 줍니다.', 'It analyzes each code and shows what is likely wrong.')),
                  (T('예상 부품 · 점검 순서', 'Suspect parts · check steps'), T('의심되는 부품과 점검 순서까지 한 화면에 나옵니다.', 'Suspect parts and the order to check them, all on one screen.')),
                  (T('정비사에게 그대로', 'Show your mechanic'), T('원인을 알고 가서, 이 화면을 정비사에게 보여 주세요.', 'Know the cause before you go, and show this screen to your mechanic.'))], 4, True)
           + note(T('고장 코드는 원인을 좁혀 주는 참고 정보입니다. 최종 판단은 정비사의 점검으로 확인하세요.', 'Fault codes narrow down the cause; they are a guide. Have a mechanic confirm the final diagnosis.')),
           'why', T('왜 OBD인가', 'Why OBD'), T('왜 OBD를 써야 할까요?', 'Why OBD?'),
           T('정비소에 가면 보통 <b>증상만</b> 말하게 됩니다. 정비사는 원인을 추측해서 부품을 하나 바꿔 보고, 아니면 또 다른 부품을 바꿔 보고… 그렇게 정비비는 눈덩이처럼 커집니다. 소비자는 원인을 모른 채 비용만 내게 되죠.',
             "At the repair shop you usually just <b>describe the symptom</b>. The mechanic guesses the cause and swaps a part. If that is not it, another part gets swapped… and the bill snowballs, while you still don't know the real cause."))
     + sec((('<div class="g2">' + f'<div>{yt("T9bEMuzRCQA", "30초 소개 영상")}</div><div>{gdrive("1J0Kxy_wdajglsqpi6pJkJFjFr3Xihdcy", "기능을 하나씩 보여 주는 영상")}</div></div>') if K else gdrive('1bvehy3E7E4gXVtuP0NIXKFEo1b4BdYL9')),
           'video', T('영상', 'Video'), T('영상으로 보기', 'Watch the video'), cls='alt')
     + sec(figs(feat) + f'<h3>{T("휴대폰에서도 돼요", "Works on phones too")}</h3><p class="p">' + T('태블릿이 없어도 안 쓰는 안드로이드 휴대폰을 거치대에 꽂아 쓸 수 있어요 (가로·세로 모두). 앱 하나가 화면에 맞춰 저절로 바뀌고, 갤럭시 폴드는 펼치면 태블릿 화면으로 나와요.',
           'No tablet? Put a spare Android phone in the mount instead, in landscape or portrait. The same app adapts to the screen, and a Galaxy Fold shows the tablet layout when unfolded.') + '</p>'
           + figs(phones, 'phones') + '<div style="height:20px"></div>'
           + boxes([(T('음성 비서', 'Voice assistant'), T('"송골랩" 하고 부르면 말로 조작해요 (예: "송골랩, 유튜브 틀어줘"). 부르는 이름은 설정 › 음성·AI › 부르는 이름에서 바꿀 수 있어요. 기본은 \'송골랩\'이고, \'콘솔\'이나 원하는 이름(2~6글자)으로 정할 수 있어요. 음악이 나오는 동안에는 가운데 마이크 버튼을 눌러 말해 주세요.',
                    'Say "Songgollab" to control it by voice (e.g. "Songgollab, play YouTube"). You can change the wake name in Settings › Voice &amp; AI › Wake name — the default is "Songgollab", or pick "Console" or any name of 2–6 letters. While music is playing, tap the microphone button in the middle instead.')),
                    (T('한국어 · 영어', 'English · Korean'), T('설정 › 화면에서 언어를 바꿀 수 있어요.', 'Change the language in Settings › Display.'))], 2),
           'features', T('할 수 있는 것', 'Features'), T('이런 걸 할 수 있어요', 'What it does'))
     + sec(boxes([(T('안드로이드 태블릿 또는 휴대폰', 'Android tablet or phone'), T('안드로이드 7.0 이상. 태블릿은 10~11인치 가로 화면을 권장해요. 개발·시험 기기는 레노버 샤오신 패드 2025입니다.', 'Android 7.0 or later. For tablets, a 10–11 inch landscape screen is recommended. Developed and tested on a Lenovo Xiaoxin Pad 2025.')),
                  (T('블루투스 OBD 동글 (BLE)', 'Bluetooth OBD dongle (BLE)'), T('시험한 제품은 Vgate iCar Pro 2S(알리익스프레스 구매)입니다.', 'Tested with the Vgate iCar Pro 2S (bought on AliExpress).')),
                  (T('태블릿 거치대', 'Tablet mount'), T('대시보드용 흡착식 거치대', 'A suction mount for the dashboard')),
                  (T('차량용 충전기 · 케이블', 'Car charger and cable'), T('운전 중 계속 켜 두려면 필요해요.', 'Keeps the tablet on while you drive.'))], 4)
           + note(T('운전 중 날씨·지도·라디오 같은 인터넷 기능을 쓰려면 휴대폰 핫스팟(테더링)을 켜 주세요.', 'To use online features such as weather, maps and radio while driving, turn on your phone hotspot.'), True),
           'ready', T('준비물', 'What you need'), T('이것만 있으면 돼요', 'What you need'), cls='alt')
     + sec('<div class="g2" style="gap:32px;align-items:start"><div>' + steps([
            (T('OBD 동글 꽂기', 'Plug in the OBD dongle'), T('운전석 아래 OBD 단자에 동글을 꽂습니다. 불이 들어오면 준비 끝이에요.', "Plug the dongle into the OBD port under the driver's side. When its light comes on, it's ready.")),
            (T('거치대와 태블릿', 'Mount the tablet'), T('대시보드에 거치대를 붙이고 태블릿을 올립니다.', 'Stick the mount on the dashboard and place the tablet in it.')),
            (T('앱 설치', 'Install the app'), T('아래 "테스터 모집"으로 신청하면 설치 링크를 보내 드려요. 폰에서 링크를 열고 "테스터 되기" → "다운로드"를 누르면 플레이스토어에서 설치됩니다.', 'Apply under "Testers wanted" below and we\'ll send you an install link. Open it on your phone, tap "Become a tester" → "Download", and it installs from Google Play.')),
            (T('시작 준비 화면', 'Getting started screen'), T('꼭 필요: <b>다른 앱 위에 표시</b> 허용 하나뿐입니다. 켜면 좋음(선택): <b>마이크</b>(음성 비서) · <b>위치</b>', 'Only one permission is required: allow <b>Display over other apps</b>. Optional: <b>Microphone</b> (voice control) and <b>Location</b>.')),
            (T('동글 연결', 'Connect the dongle'), T('설정 › 연결에서 블루투스 OBD 동글을 고르면 계기판에 숫자가 들어옵니다. 시동이 켜져 있어야 해요.', 'Choose your Bluetooth OBD dongle in Settings › Connection and the gauges start showing numbers. The engine must be on.'))])
           + '</div><div>' + gdrive('1aezbUUbm5zP5xvN8CCvlRbewVC142Lpg' if K else '1o4Za5-ycxnHEEK1xsYi3HBK8wTMF8Baf', T('설치 편 영상', 'Setup video')) + '</div></div>',
           'setup', T('설치 방법', 'Setup'), T('5단계로 끝나요', 'Five steps'))
     + sec(boxes([(T('아래 메뉴', 'Bottom menu'), T('메인 화면 / 프로그램 / 차량 정보 / 음성 비서(가운데 마이크) / 내 음악 / 차계부 / 설정', 'Home / Apps / Vehicle / Voice assistant (middle microphone) / My music / Car log / Settings')),
                  (T('내 음악', 'My music'), T('"음악 추가" → MP3가 들어 있는 폴더를 골라 "이 폴더 사용" → "허용". 사진은 오른쪽 "사진 추가". 셔플·반복재생 버튼도 있어요.', '"Add music" → choose the folder with your MP3s → "Use this folder" → "Allow". Add photos with "Add photo" on the right. Shuffle and repeat buttons are included.')),
                  (T('분할 화면', 'Split screen'), T('프로그램에서 왼쪽(내비)·오른쪽 앱을 고르고 "실행"을 누르세요. 분할이 남으면 가운데 막대를 화면 끝까지 밀어 주세요.', 'In Apps, choose the left (navigation) and right apps, then tap "Run". If the split stays on screen, slide the middle bar all the way to the edge.')),
                  (T('음성 비서', 'Voice assistant'), T('음악이 나오는 동안에는 부르는 이름(기본 "송골랩") 호출이 잠시 쉬어요. 가운데 마이크 버튼을 눌러 말해 주세요.', 'The wake name (default "Songgollab") pauses while music is playing. Tap the middle microphone button to speak.'))], 2)
           + f'<h3>{T("업데이트 소식 · v1.3.53", "What’s new · v1.3.53")}</h3>' + checks([
               T("음성 비서를 부르는 이름을 바꿀 수 있어요. 기본은 '송골랩'이에요 (예: \"송골랩, 유튜브 틀어줘\").", 'You can change the name you use to call the voice assistant. The default is "Songgollab" (e.g. "Songgollab, play YouTube").'),
               T('처음 실행하면 "안전 운전 안내"가 한 번 떠요 — 운전 중 조작·영상 시청 금지, 차량 정보는 참고용.', 'A one-time "Drive safely" notice appears on first launch — no touching the screen or watching video while driving; vehicle data is for reference only.'),
               T('주행 중에는 분할 화면의 영상 앱을 자동으로 가려요 (기본 켜짐).', 'Video apps in split screen are hidden automatically while driving (on by default).'),
               T('화면 사진에서 자동차 회사 로고를 지웠어요.', 'Car maker logos were removed from the screenshots.')])
           + note('<b>' + T('안전하게 써 주세요.', 'Please drive safely.') + '</b> ' + T(SAFETY, 'Vehicle information shown by Drive Console — speed, fuel economy, trouble codes and more — is for reference only. Get accurate inspection and diagnosis at a repair shop. Do not operate the screen while driving; the driver is responsible for driving safely.')),
           'use', T('사용 방법', 'How to use'), T('이렇게 써요', 'How to use'), cls='alt')
     + sec('<div class="g2" style="gap:32px;align-items:start"><div>'
           + f'<h3 style="margin-top:0">{T("■ 이런 걸 할 수 있어요", "■ What it does")}</h3>' + checks([
               T('속도·RPM·냉각수 온도·배터리 전압·연비 실시간 표시', 'Live speed, RPM, coolant temperature, battery voltage and fuel economy'),
               T('고장 코드(DTC) 읽기 + 뜻 설명 (현대·기아 코드 포함)', 'Reads fault codes (DTC) and explains them (including Hyundai·Kia codes)'),
               T('T맵 + 유튜브 분할 화면 (주행 중엔 영상 자동 가림)', 'T map + YouTube split screen (video is hidden automatically while driving)'),
               T('음성 명령 · 차계부 · 주행 기록', 'Voice commands · car log · driving records')])
           + f'<h3>{T("■ 참여 조건", "■ Who can join")}</h3>' + checks([
               T('안드로이드 폰 또는 태블릿 (아이폰은 안 돼요)', 'Android phone or tablet (iPhone not supported)'),
               T('ELM327 OBD 동글(블루투스·와이파이) 있으면 더 좋아요 — <b>차나 동글이 없어도 참여할 수 있어요</b>', 'An ELM327 OBD dongle (Bluetooth or Wi-Fi) is a plus — <b>you can join without a car or dongle</b>'),
               T('무료', 'Free')])
           + f'<h3>{T("■ 신청 방법", "■ How to apply")}</h3>' + steps([
               (T('Gmail 주소 보내기', 'Send your Gmail address'), T(f'플레이스토어에서 쓰는 Gmail 주소를 {MAIL} 또는 인스타·스레드 DM(@songgollab)으로 보내 주세요.', f'Send the Gmail address you use on Google Play to {MAIL} or by DM on Instagram·Threads (@songgollab).')),
               (T('설치 링크 받기', 'Get the install link'), T('테스터로 등록한 뒤 설치 링크를 보내 드려요.', "Once you're registered, we'll send you the install link.")),
               (T('테스터 되기 → 다운로드', 'Become a tester → Download'), T('폰에서 링크를 열고 "테스터 되기" → "다운로드"를 누르면 끝! 신청한 Gmail 계정으로 플레이스토어에 로그인되어 있어야 해요.', 'Open the link on your phone, tap "Become a tester" → "Download", and you\'re done! Make sure Google Play is signed in with the Gmail you sent us.'))])
           + f'<h3>{T("■ 부탁드려요", "■ A small favor")}</h3>' + checks([
               T('<b>14일 동안 앱을 지우지 말고</b> 가끔 열어 주세요. 테스트 프로그램에서 "나가기"도 누르지 말아 주세요.', 'Please <b>keep the app installed for 14 days</b> and open it now and then. Please don\'t tap "Leave the program".'),
               T('써 보시고 플레이스토어 앱 페이지에 의견 한 줄 남겨 주시면 큰 도움이 됩니다.', 'A one-line review on the Google Play app page after trying it would help a lot.')])
           + '<div class="links" style="margin-top:24px">' + btn(mailto, T('✉️ 메일로 테스터 신청하기', '✉️ Apply by email')) + btn(IG, T('인스타 DM 보내기', 'DM on Instagram'), 'ghost') + '</div>'
           + note(T('※ 이메일 주소는 댓글 말고 꼭 메일이나 DM으로 보내 주세요.', '※ Please send your email address by email or DM, not in a public comment.'))
           + '</div><div>' + yt('wwWg9VWy7Y4', T('테스터 모집 영상', 'Testers wanted video')) + '</div></div>',
           'tester', T('테스터 모집', 'Testers wanted'), T('🚗 테스터 모집 (무료 · 선착순 20명)', '🚗 Testers wanted (free · first 20 people)'),
           T('태블릿·폰을 자동차 계기판으로 쓰는 앱 "드라이브 콘솔"이 구글 플레이 정식 출시를 앞두고 있어요. 출시 전에 먼저 써 보시고 의견을 주실 테스터를 모집합니다.',
             "Drive Console, the app that turns a tablet or phone into a car dashboard, is getting ready for its official Google Play launch. We're looking for testers to try it first and share feedback before release."))
     + sec(faq([
            (T('어떻게 설치하나요?', 'How do I install it?'), T('테스터로 등록되면 설치 링크를 보내 드려요. 폰에서 링크를 열고 "테스터 되기" → "다운로드"를 누르면 플레이스토어에서 바로 설치돼요. 파일을 따로 받을 필요가 없어요.', 'Once you\'re registered as a tester, we\'ll send you an install link. Open it on your phone and tap "Become a tester" → "Download" to install from Google Play. No separate file is needed.')),
            (T('동글이 안 잡혀요', "The dongle isn't found"), T('시동을 켜고, 태블릿 블루투스를 켠 뒤 설정 › 연결에서 다시 골라 주세요. 다른 앱(예: Car Scanner)이 동글을 잡고 있으면 그 앱을 꺼 주세요.', 'Turn the engine on, turn on Bluetooth on the tablet, then choose the dongle again in Settings › Connection. If another app (e.g. Car Scanner) is connected to the dongle, close that app.')),
            (T('값이 회색으로 나와요', 'Some values are grey'), T('차종마다 주는 값이 다릅니다. 회색은 기준이 없는 참고값이에요.', 'Each car reports different values. Grey values are for reference only and have no normal range.')),
            (T('운전 중에 조작해도 되나요?', 'Can I use it while driving?'), T('안전을 위해 정차 중에 조작하고, 운전 중에는 음성 비서를 써 주세요. 주행 중에는 분할 화면의 영상 앱이 자동으로 가려져요.', 'For safety, touch the screen only when stopped and use the voice assistant while driving. Video apps in split screen are hidden automatically while you drive.')),
            (T('후기는 어디에 남기나요?', 'Where can I leave a review?'), T('써 보셨다면 플레이스토어 앱 페이지나 문의 페이지로 후기와 질문을 남겨 주세요. 남겨 주신 후기는 이곳에도 옮겨 적어요.', 'Please leave a review on the Google Play page or send it through the contact page. We also add reviews here.'))])
           + f'<p class="p" style="margin-top:18px">{T("블로그 15일 체험판을 이미 쓰고 계신 분은 체험이 끝난 뒤 잠금 화면의 <b>기기 번호</b>를 카카오톡 문의로 보내 주세요.", "If you already use the 15-day trial from the blog, send us the <b>device number</b> from the lock screen on KakaoTalk when the trial ends.")}</p>',
           'faq', 'FAQ', T('자주 묻는 질문', 'FAQ'), cls='alt')
     + band(T('궁금한 점이 있으신가요?', 'Questions?'), T(f'카카오톡이나 {MAIL}으로 물어봐 주세요.', f'Message us on KakaoTalk or email {MAIL}.'),
            btn(KAKAO, T('카카오톡으로 문의하기', 'Message us on KakaoTalk')) + btn('/contact' if K else f'mailto:{MAIL}', T('문의 페이지', 'Email us'), 'ghost')))
    return body

PAGES['drive-console'] = ('드라이브 콘솔', '남는 안드로이드 태블릿·휴대폰을 우리 차 계기판으로. OBD 동글로 속도·연비·고장 코드를 실시간으로. 구글 플레이 출시 전 무료 테스터 모집.', 'services', dc_page('ko'))
PAGES['drive-console-en'] = ('Drive Console', 'Turn a spare Android tablet or phone into your car dashboard. Live speed, fuel economy and fault codes with an OBD dongle. Free testers wanted before the Google Play launch.', 'services', dc_page('en'), 'en')

# ======================================================================
# 개인정보처리방침 (블로거 원문 그대로 옮김 — 내용 수정 금지)
PRIV_KO = '''<p><a href="#privacy-en">🇺🇸 English</a></p><p>시행일: 2026년 11월 1일 · 운영: 송골랩 (songgollab.co.kr)</p><p>송골랩은 "드라이브 콘솔" 앱(이하 앱)을 만들고 운영합니다. 이 방침은 플레이스토어에서 받은 앱(패키지 kr.songgollab.driveconsole)에 적용됩니다.</p>
<h2>1. 모으는 정보와 쓰는 곳</h2>''' + tbl(['정보', '왜 쓰나요', '어디에 남나요'], [
 ('위치(정확한 위치)', '차의 속도 표시(동글이 없을 때), 지역 날씨·미세먼지', '휴대폰 안. 날씨를 받을 때만 대략적인 좌표가 날씨 서비스(Open-Meteo)로 전송돼요'),
 ('마이크(음성)', '음성 비서 명령 (부르는 이름 기본 "송골랩")', '휴대폰의 구글 음성 인식이 글자로 바꿔 줍니다. 앱은 소리를 녹음·저장·전송하지 않아요'),
 ('차량 정보(OBD 값·고장 코드)', '계기판, 차량 상태, 고장 코드 설명', '휴대폰 안에만 저장'),
 ('차계부·주행 기록, 차량 등록 정보', '지출·운행 기록', '휴대폰 안에만 저장'),
 ('사진·음악 파일', '사진 앨범, 음악 재생', '사용자가 고른 파일을 휴대폰 안에서만 읽어요'),
 ('설치된 앱 목록', '분할 화면에 띄울 앱(내비·음악) 고르기', '휴대폰 안에서만 사용, 전송하지 않아요')]) + '''
<h2>2. 다른 곳으로 보내는 경우</h2><p>사용자가 그 기능을 쓸 때만 보냅니다.</p><ul><li>날씨·미세먼지: Open-Meteo(open-meteo.com)에 대략적인 위치를 보내 날씨를 받아요.</li><li>AI 고장 코드 설명(선택): 사용자가 직접 Gemini 키를 넣은 경우, 고장 코드와 차종이 Google Gemini로 전송돼요.</li><li>지도(선택): 사용자가 직접 카카오 지도 키를 넣은 경우, 지도 화면을 카카오에서 불러와요.</li><li>그 밖에 광고, 분석 도구, 회원가입이 없고, 송골랩은 사용자 정보를 받거나 팔지 않아요.</li></ul>
<h2>3. 보관과 삭제</h2><p>앱에 저장된 정보는 모두 휴대폰 안에 있어요. 앱을 지우거나 휴대폰 설정 › 앱 › 드라이브 콘솔 › 저장공간 › 데이터 삭제를 하면 모두 지워져요.</p>
<h2>4. 권한</h2><p>위치·마이크·블루투스·알림·다른 앱 위에 표시 권한은 처음 쓸 때 물어보고, 휴대폰 설정에서 언제든 끌 수 있어요. 권한을 꺼도 관련 기능만 쓰지 못할 뿐 앱은 쓸 수 있어요.</p>
<h2>5. 어린이</h2><p>이 앱은 운전자를 위한 앱으로, 만 14세 미만 어린이를 대상으로 하지 않아요.</p>
<h2>6. 블로그에서 받는 15일 체험판</h2><p>송골랩 블로그에서 직접 받는 15일 체험판(APK)은 체험 기간 확인을 위해 기기 번호와 실행 기록을 송골랩에 보냅니다. 이 정보는 체험 기간 확인과 연장 안내에만 쓰고, 다른 곳에 팔거나 넘기지 않습니다. 플레이스토어판에는 이 기능이 없습니다.</p>
<h2>7. 문의</h2><p>이메일 songgollab@gmail.com · <a href="/contact">songgollab.co.kr/contact</a></p>
<h2>8. 바뀌는 경우</h2><p>방침이 바뀌면 이 글에 날짜와 함께 알려 드려요.</p>'''
PRIV_EN = '''<hr><h2 id="privacy-en">Drive Console Privacy Policy</h2><p>Effective date: November 1, 2026 · Operated by songgollab (songgollab.co.kr)</p><p>songgollab makes and operates the "Drive Console" app (the "app"). This policy applies to the app downloaded from Google Play (package kr.songgollab.driveconsole).</p>
<h3>1. Information we use and why</h3>''' + tbl(['Information', 'Why', 'Where it stays'], [
 ('Location (precise)', 'Speed display when no dongle is connected; local weather and air quality', 'On your phone. Only an approximate location is sent to the weather service (Open-Meteo) when weather is fetched'),
 ('Microphone (voice)', 'Voice assistant commands (default wake name "Songgollab")', "Your phone's Google speech recognition turns speech into text. The app does not record, store or send audio"),
 ('Vehicle data (OBD values, fault codes)', 'Dashboard, vehicle status, fault code explanations', 'Stored only on your phone'),
 ('Car log, driving records, vehicle details', 'Expense and trip records', 'Stored only on your phone'),
 ('Photos and music files', 'Photo album, music playback', 'Only the files you choose are read, on your phone'),
 ('List of installed apps', 'Choosing apps (navigation, music) for split screen', 'Used on your phone only, never sent')]) + '''
<h3>2. When data leaves your phone</h3><p>Only when you use the feature:</p><ul><li>Weather and air quality: an approximate location is sent to Open-Meteo (open-meteo.com).</li><li>AI fault code explanation (optional): if you enter your own Gemini key, the fault code and car model are sent to Google Gemini.</li><li>Map (optional): if you enter your own Kakao Map key, map tiles are loaded from Kakao.</li><li>There are no ads, analytics tools or sign-up. songgollab does not receive or sell your information.</li></ul>
<h3>3. Storage and deletion</h3><p>All data the app saves stays on your phone. Uninstall the app, or go to Settings › Apps › Drive Console › Storage › Clear data, to delete it all.</p>
<h3>4. Permissions</h3><p>Location, microphone, Bluetooth, notifications and display over other apps are requested when first needed and can be turned off any time in your phone settings. Turning a permission off only disables the related feature.</p>
<h3>5. Children</h3><p>The app is made for drivers and is not directed at children under 14.</p>
<h3>6. 15-day trial from the songgollab blog</h3><p>The 15-day trial (APK) downloaded directly from the songgollab blog sends a device number and launch records to songgollab to check the trial period. This is used only for the trial period and extension requests and is never sold or shared. The Google Play version does not include this.</p>
<h3>7. Contact</h3><p>Email songgollab@gmail.com · <a href="/contact">songgollab.co.kr/contact</a></p>
<h3>8. Changes</h3><p>If this policy changes, we will update this page with the date.</p>'''
PAGES['drive-console-privacy'] = ('드라이브 콘솔 개인정보처리방침', '드라이브 콘솔 앱(kr.songgollab.driveconsole) 개인정보처리방침 · Drive Console Privacy Policy', 'services',
 hero([('drive-console', '드라이브 콘솔'), ('', '개인정보처리방침')], '드라이브 콘솔 · Privacy Policy', '개인정보처리방침', '드라이브 콘솔 앱이 어떤 정보를 왜 쓰는지, 어디에 남는지 알려 드립니다.')
 + sec(f'<div class="legal">{PRIV_KO}{PRIV_EN}</div>', cls='tight'))

# ======================================================================
PAGES['404'] = ('페이지를 찾을 수 없어요', '요청하신 페이지가 없거나 주소가 바뀌었어요.', '',
 hero([('', '404')], '404', '페이지를 찾을 수 없어요', '주소가 바뀌었거나 없는 페이지예요. 블로그 글을 찾으신다면 송골랩 블로그에서 볼 수 있어요.',
      btn('/', '홈으로') + btn(BLOG, '블로그 가기 ↗', 'ghost')))

# ---------- 쓰기 ----------
def main():
    import home, programs  # 첫 화면·반도체 세정 공정(home.py), 프로그램 14개(programs.py)
    import workshop
    home.add(globals())
    programs.add(globals())
    workshop.add(globals())
    css = '\n'.join(open(os.path.join(HERE, 'assets', f), encoding='utf-8').read() for f in ('base.css', 'pages.css', 'theme.css', 'workshop.css', 'media.css'))
    open(os.path.join(HERE, 'assets/site.css'), 'w', encoding='utf-8').write(css)
    for slug, v in PAGES.items():
        title, desc, on, body = v[:4]
        lang = v[4] if len(v) > 4 else 'ko'
        tail = v[5] if len(v) > 5 else ''
        open(os.path.join(HERE, slug + '.html'), 'w', encoding='utf-8').write(page(slug, title, desc, body, on, lang, tail))
    urls = ['/' + k if k != 'index' else '/' for k in PAGES if k != '404']
    sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + ''.join(f'  <url><loc>{SITE}{u}</loc></url>\n' for u in urls) + '</urlset>\n'
    open(os.path.join(HERE, 'sitemap.xml'), 'w', encoding='utf-8').write(sm)
    open(os.path.join(HERE, 'robots.txt'), 'w', encoding='utf-8').write(f'User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n')
    print('pages:', len(PAGES) + 1)

if __name__ == '__main__':
    main()
