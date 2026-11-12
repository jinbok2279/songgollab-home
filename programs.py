# -*- coding: utf-8 -*-
"""송골랩 프로그램 14개 — 목록(/projects)과 상세 페이지. build.py가 불러 씁니다.
내부 주소·계정·키·IP 같은 정보는 넣지 않습니다."""

ICON = {
 'car': '<path d="M5 17h14M6 17l1.5-5h9L18 17"/><circle cx="8" cy="17" r="2"/><circle cx="16" cy="17" r="2"/><path d="M12 12V7m-3 2l3-2 3 2"/>',
 'kid': '<circle cx="12" cy="7" r="3"/><path d="M5 21v-2a7 7 0 0 1 14 0v2"/>',
 'home': '<path d="M3 11l9-8 9 8"/><path d="M5 10v10h14V10"/><path d="M10 20v-5h4v5"/>',
 'shop': '<path d="M3 9h18v12H3z"/><path d="M3 9l2-6h14l2 6"/><path d="M9 13h6"/>',
 'radar': '<circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/><path d="M12 12l6-6"/>',
 'ai': '<rect x="4" y="6" width="16" height="12" rx="3"/><path d="M9 11h.01M15 11h.01M9 15h6M12 2v4"/>',
 'sns': '<rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="1"/>',
 'cart': '<circle cx="9" cy="20" r="1.5"/><circle cx="18" cy="20" r="1.5"/><path d="M2 3h3l3 12h11l2-8H6"/>',
 'chart': '<path d="M3 3v18h18"/><path d="M7 15l4-4 3 3 5-6"/>',
 'coin': '<circle cx="12" cy="12" r="9"/><path d="M9 9h4.5a2 2 0 0 1 0 4H9h5a2 2 0 0 1 0 4H9V7"/>',
 'wallet': '<rect x="3" y="6" width="18" height="14" rx="2"/><path d="M3 10h18M16 15h2"/>',
 'lock': '<rect x="5" y="11" width="14" height="10" rx="2"/><path d="M8 11V7a4 4 0 0 1 8 0v4"/>',
 'leaf': '<path d="M12 22V12"/><path d="M12 12C12 7 8 4 3 4c0 5 4 8 9 8z"/><path d="M12 12c0-4 3-7 8-7 0 4-3 7-8 7z"/>',
 'plane': '<path d="M2 16l20-8-8 14-2-6-10 0z"/>',
}

CATS = [('all', '전체'), ('svc', '공개 서비스'), ('iot', 'IoT · 자동화'), ('ops', '운영 · AI 도구'), ('biz', '커머스 · 투자 연구'), ('plan', '기획 중')]

# slug, 이름, 분류, 상태(live/test/dev/plan), 상태 글, 플랫폼, 버전, 한 줄, 그림(c1,c2,icon,사진)
P = [
 ('drive-console', '드라이브 콘솔', 'svc', 'live', '테스터 모집', 'Android', 'v1.3.57', '남는 태블릿·휴대폰을 차 계기판으로. OBD로 고장 코드 약 1만 개를 해석하고 원인·점검 순서까지.', ('#1E3A8A', '#2563EB', 'car', '/assets/drive-console.jpg')),
 ('airang', '아이랑', 'svc', 'live', '공개 · 63곳', 'Web (PWA)', 'v1.0', '아이 키우는 집의 동네 정보를 매일 아침 자동으로 모아 한 화면에. 가입 없음, 무료.', ('#0FB5A2', '#2563EB', 'kid', '/assets/airang-phone.jpg')),
 ('project-home-iot', '송골집 IoT · AI 월패드', 'iot', 'dev', '실증 중', 'Windows · 태블릿', 'v2.6', '공사 없이 우리 집에 맞춘 월패드. 집 구조 그대로의 화면, 음성 비서, 사람 감지 조명, 라디오.', ('#0B1630', '#1E40AF', 'home', '/assets/iot-concept.jpg')),
 ('program-lagrills', '라그릴스 허브', 'iot', 'dev', '사업장 실증', 'Windows', 'v2.6', '셀프 바베큐장의 구역별 에어컨을 매장 PC 한 화면에서 켜고 끕니다.', ('#B45309', '#F59E0B', 'shop', 'https://i.ytimg.com/vi/jSeZK3VLMT4/hqdefault.jpg')),
 ('project-farm', 'IoT 비닐하우스', 'plan', 'plan', '기획 중', 'IoT', '—', '부모님과 짓는 농사에 홈 IoT를 옮겨 오는 스마트팜 실험.', ('#15803D', '#65A30D', 'leaf', '')),
 ('project-control', '중앙관제', 'ops', 'dev', '내부 운영', 'Windows · 웹', 'v1.17', '내가 만든 프로그램들의 상태를 한 화면에 모으고, 음성으로 묻고, 메일까지 정리하는 관제실.', ('#0B1630', '#0FB5A2', 'radar', '')),
 ('program-ai-team', 'AI Team', 'ops', 'dev', '내부 운영', 'Windows · 휴대폰', 'v4.6', '여러 AI에게 일을 나눠 맡기는 작업실. 팀장 AI가 계획·검수하고 팀원 AI들이 나눠 처리합니다.', ('#6D28D9', '#2563EB', 'ai', '')),
 ('program-sns', 'SNS 통합관리', 'ops', 'dev', '내부 운영', 'Windows', 'v0.6', '인스타그램·스레드·블로그를 한 프로그램에서. 글쓰기, 예약, 반응 보기까지.', ('#DB2777', '#F59E0B', 'sns', '')),
 ('program-login', '로그인 상태 점검판', 'ops', 'dev', '사용 중', 'Chrome 확장', 'v1.0', '여러 사이트의 로그인 상태와 키 만료일을 한눈에. 복구 수단 점검표 포함.', ('#334155', '#64748B', 'lock', '')),
 ('program-invest', '투자비 관리', 'ops', 'dev', '사용 중', 'Windows', 'v2.0', '프로젝트에 들어간 부품·장비 구매 내역을 자동으로 모아 프로젝트별·월별로 분석합니다.', ('#0E7490', '#0FB5A2', 'wallet', '')),
 ('project-commerce', '알리 소싱 도우미', 'biz', 'dev', '개발 중', 'Windows', 'v2.1', '팔 만한 해외 상품을 찾아 분석하고, 스마트스토어용 상품명·가격·홍보 글까지 만들어 줍니다.', ('#EA580C', '#F43F5E', 'cart', '')),
 ('program-stock', '주식 자동매매 연구', 'biz', 'dev', '개인 연구', 'Windows', 'v0.4', '실시간 거래량·체결·호가 변화를 점수로 만들어 신호를 찾고, 장 마감 후 AI가 복기합니다.', ('#1D4ED8', '#0EA5E9', 'chart', '')),
 ('program-coin', '코인 자동매매 연구', 'biz', 'dev', '개인 연구', 'Windows', 'v0.3', '원화 마켓 전체를 실시간으로 감시하고, 정해 둔 규칙대로만 사고팝니다.', ('#A16207', '#EAB308', 'coin', '')),
 ('program-booking', 'AI 예약 비서', 'plan', 'plan', '시안 단계', 'Mobile · PC', '—', '말로 요청하면 항공·기차·숙소·식당을 찾아 번호로 보여 주고, 고른 것만 예약하는 가족용 비서.', ('#0369A1', '#7C3AED', 'plane', '')),
]

def art(c1, c2, icon, photo):
    if photo:
        return f'<div class="art photo" style="--c1:{c1};--c2:{c2}"><img class="ph" src="{photo}" alt="" loading="lazy">'
    return f'<div class="art" style="--c1:{c1};--c2:{c2}"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">{ICON[icon]}</svg>'

def card(p):
    slug, name, cat, st, stl, plat, ver, one, (c1, c2, ic, ph) = p
    catname = dict(CATS)[cat]
    stc = {'live': 'live', 'plan': 'plan'}.get(st, '')
    meta = f'<span>{plat}</span>' + (f'<span>{ver}</span>' if ver != '—' else '')
    return f'''<a class="prog rv" data-cat="{cat}" href="/{slug}">{art(c1, c2, ic, ph)}<span class="st {stc}">{stl}</span></div>
<div class="tx"><span class="cat">{catname.upper() if cat != "svc" else "PUBLIC SERVICE"}</span><h3>{name}</h3><p>{one}</p><div class="meta">{meta}</div></div></a>'''

def catalog(limit=None):
    items = P if not limit else P[:limit]
    return '<div class="progs" id="progs">' + ''.join(card(p) for p in items) + '</div>'

def filters():
    return '<div class="filters" id="filters">' + ''.join(f'<button data-f="{k}"{" class=on" if k == "all" else ""}>{v}</button>' for k, v in CATS) + '</div>'

FILTER_JS = '''<script>(function(){var b=document.querySelectorAll('#filters button');b.forEach(function(x){x.addEventListener('click',function(){b.forEach(function(y){y.classList.toggle('on',y===x)});var f=x.dataset.f;document.querySelectorAll('#progs .prog').forEach(function(c){c.classList.toggle('hide',f!=='all'&&c.dataset.cat!==f)})})})})();</script>'''

# ---------------------------------------------------------------- 상세 내용
D = {}
D['program-lagrills'] = dict(
 lead='셀프 바베큐장 라그릴스의 BBQ 사이트 1~9, 객실, 매점 에어컨을 매장 PC 한 화면에서 켜고 끕니다. 송골집에서 먼저 써 본 방식을 처음으로 실제 사업장에 옮긴 프로젝트입니다.',
 why='손님이 오기 전에 구역마다 직접 다니며 리모컨으로 에어컨을 켜고, 퇴실 뒤 꺼졌는지 다시 확인해야 했습니다. 바쁜 시간에는 빠뜨리기 쉬웠습니다.',
 feats=[('구역별 한 화면 제어', 'BBQ 사이트 1~9, 객실, 매점까지 구역별 버튼으로 켜고 끕니다.'), ('IR 리모컨 연결', '구역마다 IR 리모컨 장치를 달아, 기존 에어컨을 바꾸지 않고 제어합니다.'),
        ('매장 PC 상주', '카운터 PC에서 늘 켜 두고, 지금 켜진 구역을 한눈에 봅니다.'), ('공사 없이 2일', '배선 공사 없이 이틀 만에 설치했습니다. (2026.10.04)')],
 flow=[('매장 PC', '허브 화면에서 구역 선택'), ('집 안 서버', '명령을 기기로 전달'), ('IR 리모컨', '각 구역 에어컨에 신호'), ('에어컨', '켜짐·꺼짐')],
 log=[('2026.10.04', '허브 v2.6 설치', '구역마다 IR 리모컨을 달고 매장 PC에 허브를 설치했습니다.'), ('다음', '전 구역 전등 · 예약 연동', '예약 시간에 맞춰 미리 켜고, 에어컨 전력을 확인하는 기능으로 넓힙니다.')],
 videos=['jSeZK3VLMT4', 'oSnE9LrclWM'], links=[('/project-home-iot', '송골집 IoT 보기'), ('https://songgollab.blogspot.com/2026/10/pc.html', '설치기 글 ↗')])
D['project-control'] = dict(
 lead='송골랩이 만든 프로그램들(홈 IoT, 드라이브 콘솔, 아이랑 관리, 자동매매 연구, AI Team 등)의 상태를 한 화면에 모으는 내부 관제실입니다. 음성으로 묻고, 메일을 정리하고, 각 프로그램 담당 AI에게 수정 요청까지 보냅니다.',
 why='프로그램이 늘어나면서 무엇이 잘 돌고 무엇이 멈췄는지 하나씩 열어 봐야 했습니다. 한 화면에서 보고, 문제가 생기면 바로 손쓸 수 있게 만들었습니다.',
 feats=[('프로그램 상태 모음', '연결된 프로그램마다 카드 하나. 정상·주의·끊김을 색으로 보고, 누르면 자세한 상황 창이 열립니다.'), ('음성 비서', '말로 묻고 답을 듣습니다. 화면 가운데 코어가 말할 때 반응합니다.'),
        ('메일 관제', '여러 메일함을 한곳에서 읽고, 광고 메일은 자동으로 휴지통·보관함으로 보냅니다.'), ('오늘의 뉴스', '분야별 주요 기사 제목을 첫 화면에서 봅니다.'),
        ('개발 연락소', '각 프로그램을 맡은 AI에게 질문하거나 수정을 요청하고 답을 모아 봅니다.'), ('집 밖 접속 · 태블릿', 'PC·태블릿·휴대폰 화면을 따로 맞췄고, 밖에서도 안전하게 접속합니다.')],
 flow=[('각 프로그램', '정해진 규격으로 상태 보내기'), ('관제 서버', '모아서 저장·판정'), ('관제 화면', '카드·연결선으로 표시'), ('알림 · 조치', '음성·메일·수정 요청')],
 log=[('v1.13', '노드 관제', '여러 PC·장치를 노드로 묶어 상태를 봅니다.'), ('v1.14 ~ 1.15', '메일 관제', '광고 메일 자동 정리, 관제 안에서 바로 읽기.'), ('v1.16', '방마다 지금', '송골집 창을 방별 현재 상태로.'), ('v1.17', '영화 같은 화면', '창이 열릴 때의 효과, 빛나는 연결선, 오늘의 뉴스 카드 복구.')],
 note='내부 전용 프로그램이라 구성도·접속 정보·보안 세부 사항은 공개하지 않습니다. 이미지는 콘셉트입니다.', image=('ai', '통합 관리 콘셉트 이미지'))
D['program-ai-team'] = dict(
 lead='하나의 AI에 모든 일을 맡기지 않고, 일의 성격에 따라 여러 AI에게 나눠 맡기는 작업실입니다. 팀장 AI가 계획을 세우고 검수하며, 팀원 AI들이 조각을 나눠 처리합니다.',
 why='AI 사용량과 비용을 줄이면서도, 글·영상·코드를 꾸준히 만들어야 했습니다. 쉬운 일은 가볍고 저렴한 AI가, 어려운 일은 강한 AI가 맡도록 나눴습니다.',
 feats=[('팀장 · 부팀장 · 팀원', 'Claude가 계획·검수·코딩, GPT가 부팀장, DeepSeek·Qwen·Gemini가 팀원으로 일합니다.'), ('로컬 AI 활용', 'PC 안의 로컬 AI가 자동 확인·예비 작업·보안 자료를 맡아 바깥으로 보내지 않습니다.'),
        ('일상 대화는 바로', '가벼운 대화는 빠른 AI가 바로 답합니다.'), ('영상 → 승인 → 게시', '지시 한 번으로 영상을 만들고, 승인하면 SNS에 바로 올립니다.'),
        ('작업 일지', '누가 무엇을 했고 어디서 막혔는지(한도·시간 초과·연결 끊김 등) 기록합니다.'), ('PC · 휴대폰', 'PC와 휴대폰에서 같은 작업실을 씁니다. 중앙관제와 연결됩니다.')],
 flow=[('지시', '사람이 할 일을 말함'), ('계획', '팀장 AI가 조각으로 나눔'), ('배정', '팀원 AI에게 고르게 맡김'), ('검수', '팀장이 확인·수정'), ('결과', '파일·게시·보고')],
 log=[('v4.4', '점검 진단', '연결·권한 문제를 스스로 진단합니다.'), ('v4.5', '영상 자동 게시', '지시 → 영상 → 승인 → 게시를 한 흐름으로.'), ('v4.6', '모두 같이 일하기', '등급을 끄고 모든 AI가 조각을 나눠 맡는 2주 실험 중.')])
D['program-sns'] = dict(
 lead='송골랩의 인스타그램, 스레드, 블로그를 한 프로그램에서 관리합니다. 글을 쓰고, 예약하고, 반응을 보고, 인기 글을 찾습니다.',
 why='채널마다 따로 들어가 글을 올리고 숫자를 확인하는 데 시간이 많이 들었습니다.',
 feats=[('관제실 화면', '채널별 방문·반응을 큰 숫자와 그래프로 한눈에.'), ('글쓰기 · 예약', '한 번 쓴 글을 채널에 맞게 다듬어 예약합니다.'), ('사진 글', '드라이브 폴더의 사진으로 글을 만듭니다.'),
        ('폴더 자동 올리기', '정해 둔 폴더에 파일을 넣으면 순서대로 올라갑니다.'), ('인기 글 찾기', '반응이 좋은 글을 찾아 다음 글 주제로 씁니다.'), ('중앙관제 연동', '채널 상태를 관제실로 보냅니다.')],
 flow=[('글 · 사진', '쓰거나 폴더에 넣기'), ('다듬기', '채널별 길이·태그'), ('예약', '시간 정해 올리기'), ('반응 보기', '숫자 모아 다음 글에')],
 log=[('v0.4', '글쓰기 · 예약 · 폴더 자동 올리기', ''), ('v0.5', '사진 글', '드라이브를 거쳐 사진 글 올리기.'), ('v0.6', '중앙관제 연동', '관제 규격으로 상태 보내기, 자동 시작.')],
 note='계정 비밀번호는 저장하지 않고, 연결 키는 PC 안에만 둡니다.')
D['program-login'] = dict(
 lead='구글·GitHub·도메인·각종 개발 서비스까지, 여러 사이트의 로그인 상태와 API 키 만료일을 한 화면에서 점검하는 Chrome 확장 프로그램입니다.',
 why='프로그램을 여러 개 운영하다 보니 어느 사이트 로그인이 풀렸는지, 어떤 키가 곧 만료되는지 몰라 작업이 자주 멈췄습니다.',
 feats=[('로그인 상태 한눈에', '사이트별 로그인 여부를 초록·노랑·회색으로 보여 줍니다.'), ('키 · 토큰 만료일', '만료일을 넣어 두면 다가올 때 알려 줍니다.'),
        ('복구 수단 점검표', '복구 전화·메일·백업 코드·2단계 인증을 하나씩 확인합니다.'), ('확인함 기록', '확장이 볼 수 없는 앱은 열어 보고 "확인함"을 누르면 14일 뒤 다시 알려 줍니다.')],
 flow=[('확장 설치', 'Chrome에 추가'), ('자동 점검', '사이트별 로그인 확인'), ('점검판', '색으로 상태 표시'), ('알림', '풀림·만료 임박')],
 log=[('v1.0', '첫 버전', '점검판, 키·토큰 탭, 복구 수단 점검표.')],
 note='비밀번호는 저장하지 않습니다. 모든 기록은 내 브라우저 안에만 남습니다.')
D['program-invest'] = dict(
 lead='프로젝트에 들어간 부품·장비 구매 내역을 쇼핑몰 주문 기록에서 자동으로 모아, 프로젝트별·월별로 얼마를 썼는지 분석하는 프로그램입니다.',
 why='홈 IoT, 드라이브 콘솔 같은 프로젝트마다 부품을 여러 쇼핑몰에서 사다 보니, 어디에 얼마를 썼는지 정리가 안 됐습니다.',
 feats=[('주문 자동 가져오기', '매주 정해진 시간에 최근 주문을 모아 폴더에 넣으면, 프로그램이 새 것만 가져옵니다.'), ('프로젝트별 분류', '상품명을 보고 프로젝트를 자동으로 고르고, 직접 고친 분류는 유지합니다.'),
        ('월별 분석', '프로젝트별·월별 지출을 그래프로 봅니다.'), ('취소 주문 정리', '취소된 주문은 자동으로 뺍니다.'), ('중앙관제 연동', '지출 현황을 관제실로 보냅니다.')],
 flow=[('주간 수집', '쇼핑몰 주문 기록'), ('폴더', '주간 파일로 저장'), ('가져오기', '새 것만 · 중복 방지'), ('분석', '프로젝트별 · 월별')],
 log=[('v1.x', '구매 내역 분류', ''), ('v2.0', '자동 가져오기 · 관제 연동', '주간 파일을 1분마다 확인해 새 것만 반영합니다.')])
D['project-commerce'] = dict(
 lead='알리익스프레스에서 팔 만한 상품을 AI와 API로 찾아 분석하고, 네이버 스마트스토어용 해외구매대행 상품으로 정리해 블로그 홍보 글까지 만들어 주는 Windows 프로그램 「알리 소싱 도우미」입니다.',
 why='작은 판매자가 상품을 찾고, 사진·설명을 다듬고, 가격을 계산하고, 홍보 글을 쓰는 일은 매번 같은 반복입니다.',
 feats=[('상품 찾기 · 분석', '팔 만한 상품을 찾아 가격·배송·리뷰를 분석합니다.'), ('취급 가능 판정', '전기용품·생활용품 안전관리 기준으로 구매대행 가능한 품목인지 먼저 거릅니다.'),
        ('검색 노출 점수', '상품명 점수, 키워드 검색량·경쟁 상품 수로 키워드를 고르고 AI가 상품명을 다듬습니다.'), ('마진 계산', '수수료·반품 충당·광고비까지 넣어 남는 돈을 계산합니다.'),
        ('카테고리 자동', '경쟁 상품을 보고 카테고리를 자동으로 고릅니다.'), ('홍보 글', '블로그용 상품 소개 글을 만듭니다.')],
 flow=[('찾기', '해외 상품 후보'), ('거르기', '취급 가능 판정'), ('다듬기', '상품명·가격·카테고리'), ('올리기', '스마트스토어'), ('알리기', '블로그 글')],
 log=[('v1.x', '쿠팡 전용판', '쿠팡용으로 시작해 v1.9.1에서 마무리.'), ('v2.0', '네이버 전용으로 전환', ''), ('v2.1', '노출 최적화 · 자동 운영', '키워드 점수, AI 상품명, 마진 정밀화.')],
 note='판매·통관 관련 법규를 지키는 범위에서만 씁니다. 개인통관고유부호 등 고객 정보는 프로그램에 저장하지 않습니다.', image=('auto', '상품 등록 자동화 콘셉트'))
D['program-stock'] = dict(
 lead='실시간 거래량·체결·호가 변화를 감지해 점수를 매기고, 신호가 좋은 종목을 찾는 주식 자동매매 연구 프로그램입니다. 장이 끝나면 AI가 그날의 매매를 복기합니다.',
 why='감으로 하는 매매 대신, 신호를 숫자로 만들고 결과를 기록해 정말 승률이 나오는지부터 확인하려고 만들었습니다.',
 feats=[('실시간 감지 · 점수', '거래량 급증, 체결 강도, 호가 변화를 점수로 만듭니다.'), ('모의투자 자동매매', '증권사 모의투자 계좌에서 규칙대로 자동으로 사고팝니다.'),
        ('한도 · 승인', '실전 계좌는 정해 둔 한도 안에서 알림·승인 방식으로만 움직입니다.'), ('공시 연동', '금융감독원 공시(DART)를 함께 봅니다.'),
        ('AI 복기', '장 마감 후 AI가 그날 매매를 돌아보고 다음 날 설정에 반영합니다.'), ('날짜별 기록', '설정과 결과를 날짜별로 남겨 비교합니다.')],
 flow=[('시세 수신', '실시간 체결·호가'), ('감지', '변화 포착'), ('점수', '진입 기준 비교'), ('매매', '모의·한도 안'), ('복기', 'AI가 정리')],
 log=[('v0.4.8', '공시 연동', ''), ('v0.4.11', '첫날 복기', ''), ('v0.4.13', '설정 단순화', '항상 같은 기준으로 판단하게 정리.')],
 note='개인 연구용 프로그램입니다. 배포·판매하지 않으며 투자 권유가 아닙니다. 수익률과 매매 전략은 공개하지 않습니다.')
D['program-coin'] = dict(
 lead='국내 거래소 원화 마켓의 모든 코인을 실시간으로 감시하고, 미리 정해 둔 규칙대로만 사고파는 자동매매 연구 프로그램입니다.',
 why='24시간 움직이는 시장을 사람이 계속 볼 수는 없습니다. 감정 없이 규칙대로만 움직이면 결과가 어떻게 되는지 확인하려고 만들었습니다.',
 feats=[('전체 마켓 감시', '원화 마켓 전체를 실시간으로 봅니다.'), ('규칙대로만', '진입·청산·비중 규칙을 정해 두고 그대로만 움직입니다.'),
        ('비중 제한', '한 코인에 너무 많이 들어가지 않도록 최대 비중을 둡니다.'), ('매매 실험실', '규칙을 바꿔 보며 결과를 비교합니다.'),
        ('자동 업데이트', '수정이 생기면 바로 반영됩니다.'), ('중앙관제 연동', '상태와 결과를 관제실로 보냅니다.')],
 flow=[('시세 수신', '전체 마켓'), ('조건 확인', '규칙 비교'), ('주문', '비중 제한 안'), ('기록 · 분석', '기간별 결과')],
 log=[('v0.3.2', '자동 업데이트', ''), ('v0.3.4', '신규 상장 코인 포함', ''), ('v0.3.6', '매매 실험실', '작은 계좌에서도 규칙이 동작하도록 고침.')],
 note='개인 연구용 프로그램입니다. 배포·판매하지 않으며 투자 권유가 아닙니다. 수익률과 매매 전략은 공개하지 않습니다.')
D['project-farm'] = dict(
 lead='부모님과 함께 짓는 농사에 홈 IoT를 그대로 옮겨 오는 프로젝트입니다. 5~6평 아치형 비닐하우스를 직접 지어, 온도·습도를 멀리서 보고 집과 같은 화면에서 관리하는 것이 목표입니다.',
 why='하우스 안이 너무 덥거나 추워지는 걸 밭에 가 봐야만 알 수 있었습니다.',
 feats=[('하우스 상태 보기', '온도·습도를 휴대폰으로 확인하고, 너무 덥거나 추우면 알림을 받습니다.'), ('홈 IoT와 한 화면', '집에서 쓰는 Home Assistant 화면에서 하우스까지 봅니다.'), ('직접 써 보고 검증', '우리 밭에서 먼저 써 보고, 효과가 확인된 것만 서비스로 만듭니다.')],
 flow=[('센서', '온도·습도'), ('무선 전달', '집 안 서버로'), ('판단', '기준 넘으면'), ('알림 · 동작', '휴대폰 · 환기')],
 log=[('2026.10', '프로젝트 등록', '홈 IoT와 연계한 스마트 농장으로 정했습니다.'), ('다음', '하우스 짓기', '아치형 파이프와 비닐로 5~6평 하우스를 먼저 짓습니다.')])
D['program-booking'] = dict(
 lead='"이번 주말 제주 2박 3일" 처럼 말로 요청하면 항공·기차·숙소·렌터카·식당을 찾아 번호로 보여 주고, 내가 고른 것만 예약해 주는 가족용 AI 예약 비서입니다.',
 why='여행 하나를 준비하려면 앱 대여섯 개를 오가며 비교해야 했습니다.',
 feats=[('말로 요청', '날짜·인원·예산을 말하면 조건을 정리합니다.'), ('번호로 고르기', '"2번 진행해 줘"처럼 번호로 고릅니다.'), ('자동 연계', '도착 시간에 맞춰 렌터카·숙소를 이어서 제안합니다.'), ('최종 승인', '결제·예약은 내가 승인한 것만 진행합니다.')],
 flow=[('요청', '말 또는 글'), ('검색', '항공·숙소·식당'), ('제안', '번호 목록'), ('승인', '고른 것만 예약')],
 log=[('v0.1', '화면 시안', '휴대폰 화면형·음성형, 데스크톱 화면 시안 12장을 만들었습니다.'), ('다음', '시안 다듬기', '데스크톱 화면을 같은 스타일로 맞춥니다.')])


# ---------------------------------------------------------------- 이미지 · 영상 · 자료
G = {
 'drive-console': [('/assets/drive-console.jpg', '태블릿 메인 화면'), ('/assets/prog/dc-phone.jpg', '휴대폰 세로 메인 화면 (v1.3.56)', 'tall'), ('/assets/drive-console-2.jpg', '차량 정보 화면')],
 'airang': [('/assets/airang-phone.jpg', '아이랑 휴대폰 화면', 'tall')],
 'project-home-iot': [('/assets/prog/home-energy.jpg', '에너지 화면 — 가전별 실시간 전력 (재현 화면)'), ('/assets/prog/home-auto.jpg', '장면 · 자동화 화면 — 아침 조명, 빈 방 끄기, 외출 소등 (재현 화면)')],
 'project-control': [('/assets/prog/control-main.jpg', '관제 메인 화면 — 프로그램 10개를 한 화면에 (재현 화면)')],
 'program-ai-team': [('/assets/prog/aiteam-flow.jpg', 'AI 팀 작업실이 일하는 방식'), ('/assets/prog/aiteam-home.jpg', '홈 화면 — 팀장 AI와 팀원 AI 연결 (재현 화면)'), ('/assets/prog/aiteam-order.jpg', '지시 화면 — 프로젝트별 대화와 지금 일하는 AI'), ('/assets/prog/aiteam-phone.jpg', '휴대폰 화면', 'tall')],
 'project-commerce': [('/assets/prog/ali-final.jpg', '마켓 등록 초안 확인 — 노출 최적화, 마진, 취급 판정')],
}
V = {
 'drive-console': [('T9bEMuzRCQA', '30초 소개'), ('rpFFTn9Ux6Q', '3분 기능 설명 v1.3'), ('wwWg9VWy7Y4', '테스터 모집')],
 'airang': [('YRNth4rPD_I', '아이랑 경기'), ('y_lwf2FhGaQ', '아이랑 서울 25개 구'), ('uvaTydTX3Bk', '아이랑 충남')],
 'project-home-iot': [('jB_N9SyBGMU', 'IoT 이야기 EP.1'), ('66hwKAWMw84', 'EP.3 스마트홈의 하루'), ('mKFjxUG26es', 'EP.4 새는 전기 막기')],
 'program-lagrills': [('jSeZK3VLMT4', '라그릴스 허브 v2.6 소개'), ('oSnE9LrclWM', '셀프 바베큐장 라그릴스')],
 'project-farm': [('05GXvZZknDs', 'IoT 이야기 EP.5 — 멀리서 살피기')],
}
R = {
 'drive-console': [('/drive-console', '사용 안내 · 설치 방법', '준비물, 5단계 설치, 사용법, 자주 묻는 질문'), ('/project-drive', '개발 기록 · 화면 둘러보기', 'v0.6부터 v1.3.53까지, 고장 코드 진단 구조'), ('/drive-console-privacy', '개인정보처리방침', '한국어 · English'), ('/drive-console-en', 'English page', 'Drive Console in English')],
 'airang': [('https://airang.songgollab.co.kr', '아이랑 바로 열기 ↗', '도시를 골라 바로 사용'), ('/airang', '아이랑 소개 · 로드맵', '운영 방식, 개발 일지, 단계별 계획'), ('https://songgollab.blogspot.com', '블로그 글 ↗', '아이랑 서울·경기·충남 소개 글')],
 'project-home-iot': [('/iot-guide', 'IoT, 쉽게 알아보기', '영상 5편으로 정리한 홈 IoT 입문'), ('https://songgollab.blogspot.com/2026/10/pc.html', '라그릴스 설치기 ↗', '바베큐장 에어컨을 한 화면으로')],
 'program-lagrills': [('https://songgollab.blogspot.com/2026/10/pc.html', '설치기 전체 글 ↗', '2일 작업 기록')],
}

def gallery(slug):
    items = G.get(slug)
    if not items: return ''
    cells = ''.join(f'<figure class="gi{" tall" if len(x) > 2 else ""}"><a href="{x[0]}" target="_blank" rel="noopener"><img src="{x[0]}" alt="{x[1]}" loading="lazy"></a><figcaption>{x[1]}</figcaption></figure>' for x in items)
    return f'<div class="gal">{cells}</div>'

def videos(slug, yt):
    items = V.get(slug)
    if not items: return ''
    return '<div class="vids">' + ''.join(f'<div>{yt(i, t)}</div>' for i, t in items) + '</div>'

def resources(slug):
    items = R.get(slug)
    if not items: return ''
    return '<div class="res">' + ''.join(f'<a href="{h}"{" target=_blank rel=noopener" if h.startswith("http") else ""}><span class="ri"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 3h7v7M10 14L21 3M21 14v7H3V3h7"/></svg></span><b>{t}</b><em>{d}</em></a>' for h, t, d in items) + '</div>'

def media_sections(g, slug, with_video=True):
    sec = g['sec']; out = ''
    gl, vd, rs = gallery(slug), (videos(slug, g['yt']) if with_video else ''), resources(slug)
    if gl: out += sec(gl, 'gallery', 'Images · 이미지', '화면으로 보기', cls='white-sec')
    if vd: out += sec(vd, 'video', 'Video · 영상', '영상으로 보기')
    if rs: out += sec(rs, 'docs', 'Docs · 자료', '설명 자료')
    if not gl and not vd: out += sec('<div class="note blue" style="max-width:none">화면 사진과 영상은 정리되는 대로 이곳에 올립니다. 개인 연구·내부 프로그램은 계좌·금액·접속 정보가 보이지 않는 화면만 공개합니다.</div>', 'gallery', 'Images · 이미지', '화면으로 보기', cls='tight')
    return out

def detail(g, slug):
    btn, sec, boxes, log, note, yt, IMG = g['btn'], g['sec'], g['boxes'], g['log'], g['note'], g['yt'], g['IMG']
    p = next(x for x in P if x[0] == slug); d = D[slug]
    _, name, cat, st, stl, plat, ver, one, (c1, c2, ic, ph) = p
    chips = f'<span class="{ "live" if st=="live" else ("plan" if st=="plan" else "") }">● {stl}</span><span>{plat}</span>' + (f'<span>{ver}</span>' if ver != '—' else '') + f'<span>{dict(CATS)[cat]}</span>'
    hero = f'''<section class="page-hero"><div class="wrap"><div class="crumb"><a href="/">홈</a> › <a href="/projects">프로그램</a> › <span>{name}</span></div>
<span class="eyebrow">{dict(CATS)[cat]}</span><h1>{name}</h1><p class="lead">{d["lead"]}</p><div class="pmeta">{chips}</div></div></section>'''
    tl = [('feat', '주요 기능'), ('how', '동작 방식'), ('gallery', '이미지')] + ([('video', '영상')] if V.get(slug) else []) + ([('docs', '자료')] if R.get(slug) else []) + [('log', '개발 기록')]
    body = hero + g['toc'](tl)
    side = ''
    if G.get(slug):
        x = G[slug][0]
        side = f'<figure class="fig" style="margin:0"><img src="{x[0]}" alt="{x[1]}" loading="lazy"><figcaption class="cap"><span>{x[1]}</span></figcaption></figure>'
    elif d.get('image'):
        k, alt = d['image']
        side = f'<figure class="fig" style="margin:0"><img src="{IMG[k]}" alt="{alt}" loading="lazy"><figcaption class="cap"><span>콘셉트 이미지 · 실제 화면 아님</span></figcaption></figure>'
    else:
        side = f'<div class="prog" style="pointer-events:none">{art(c1, c2, ic, ph)}</div><div class="tx"><span class="cat">ONE LINE</span><p style="margin-top:6px">{one}</p></div></div>'
    body += sec(f'<div class="split"><div><span class="eyebrow">Why · 왜 만들었나</span><h2 style="font-size:clamp(24px,2.6vw,32px);font-weight:800;letter-spacing:-.02em;margin:10px 0 12px">불편에서 시작했습니다</h2><p class="p">{d["why"]}</p></div><div>{side}</div></div>', cls='tight')
    body += sec(boxes(d['feats'], 3 if len(d['feats']) != 4 else 2), 'feat', 'Features · 주요 기능', '할 수 있는 것', cls='alt')
    body += sec(boxes(d['flow'], len(d['flow']) if len(d['flow']) <= 4 else 3, True), 'how', 'How it works · 동작 방식', '이렇게 돌아갑니다')
    body += media_sections(g, slug)
    body += sec(log([(a, b, c) for a, b, c in d['log']]) + (note(d['note'], True) if d.get('note') else ''), 'log', 'Log · 개발 기록', '어떻게 만들어 왔나', cls='alt')
    links = ''.join(btn(h, t, 'ghost') for h, t in d.get('links', []))
    body += g['band']('다른 프로그램도 둘러보세요', '송골랩이 직접 만들고 쓰는 프로그램 14개를 모아 두었습니다.', btn('/projects', '프로그램 전체') + links + btn('/contact', '문의하기', 'ghost'))
    return body

def add(g):
    PAGES = g['PAGES']
    for slug in D:
        p = next(x for x in P if x[0] == slug)
        PAGES[slug] = (p[1], p[7], 'projects', detail(g, slug))
    for slug in ('drive-console', 'airang', 'project-home-iot'):
        v = list(PAGES[slug]); body = v[3]; i = body.rfind('<section class="band">')
        m = media_sections(g, slug, slug == 'project-home-iot')
        v[3] = body[:i] + m + body[i:] if i > 0 else body + m
        PAGES[slug] = tuple(v)
    hero = g['hero']([('', '프로그램')], 'Programs · 프로그램', '직접 만들고, 직접 쓰는<br>프로그램 14개',
                     '20년 장비 엔지니어가 생활과 일에서 겪은 불편을 하나씩 프로그램으로 만들었습니다. 공개 서비스부터 내부 도구, 개인 연구, 기획 중인 것까지 모두 모았습니다.')
    PAGES['projects'] = ('프로그램', '송골랩이 직접 만들고 쓰는 프로그램 14개 — 드라이브 콘솔, 아이랑, 송골집 IoT, 라그릴스 허브, 중앙관제, AI Team, SNS 통합관리, 알리 소싱 도우미, 자동매매 연구 등.', 'projects',
                         hero + g['sec'](filters() + catalog(), cls='tight') + g['band']('관심 가는 프로그램이 있나요?', '써 보고 싶거나, 비슷한 걸 만들고 싶다면 편하게 연락 주세요.', g['btn']('/contact', '문의하기')), 'ko', FILTER_JS)
