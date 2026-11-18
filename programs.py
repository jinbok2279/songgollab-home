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
 ('project-home-iot', '송골집 IoT · AI 월패드', 'iot', 'dev', '실증 중', 'Windows · 태블릿', 'v2.6', '공사 없이 우리 집에 맞춘 월패드. 집 구조 그대로의 화면, 음성 비서, 사람 감지 조명, 라디오.', ('#0B1630', '#1E40AF', 'home', '/assets/prog/home-main.jpg')),
 ('program-lagrills', '라그릴스 허브', 'iot', 'dev', '사업장 실증', 'Windows', 'v2.6', '셀프 바베큐장의 구역별 에어컨을 매장 PC 한 화면에서 켜고 끕니다.', ('#B45309', '#F59E0B', 'shop', 'https://i.ytimg.com/vi/jSeZK3VLMT4/hqdefault.jpg')),
 ('project-farm', 'IoT 비닐하우스', 'plan', 'plan', '기획 중', 'IoT', '—', '부모님과 짓는 농사에 홈 IoT를 옮겨 오는 스마트팜 실험.', ('#15803D', '#65A30D', 'leaf', '')),
 ('project-control', '중앙관제', 'ops', 'dev', '운영 중', 'Windows · 웹 · 휴대폰', 'v1.19.8', '다들 하나씩은 가지고 계시죠? 나만의 자비스~! 내가 만든 프로그램들이 알아서 모이는 관제 화면, 목소리로 묻고 시킵니다.', ('#0B1630', '#0FB5A2', 'radar', '/assets/prog/control-v1198-10.jpg')),
 ('program-printbench', '3D Print Bench', 'iot', 'dev', '개발 중', 'Windows', 'v0.9', '3D 프린터를 PC 한 화면에서 보고, 맡기고, 안전하게 돌리는 프로그램. 클라우드 없이 집 안 네트워크에서만.', ('#0B1A2A', '#22D3EE', 'radar', '/assets/prog/pb-monitor.jpg')),
 ('program-ai-team', 'AI Team', 'ops', 'dev', '내부 운영', 'Windows · 휴대폰', 'v4.6', '여러 AI에게 일을 나눠 맡기는 작업실. 팀장 AI가 계획·검수하고 팀원 AI들이 나눠 처리합니다.', ('#6D28D9', '#2563EB', 'ai', '')),
 ('program-sns', 'SNS 통합관리', 'ops', 'dev', '내부 운영', 'Windows', 'v0.6', '인스타그램·스레드·블로그를 한 프로그램에서. 글쓰기, 예약, 반응 보기까지.', ('#DB2777', '#F59E0B', 'sns', '')),
 ('program-login', '로그인 상태 점검판', 'ops', 'dev', '내부 사용', 'Chrome 확장', 'v1.0', '60여 개 사이트의 로그인·API 키 상태를 한 화면에서. 끊기면 바로 알려 줍니다.', ('#334155', '#64748B', 'lock', '/assets/prog/login-00-cover.jpg')),
 ('program-invest', '투자비 관리', 'ops', 'dev', '사용 중', 'Windows', 'v2.0', '알리익스프레스·G마켓 구매 내역을 프로젝트별로 자동 분류하고, 월별로 얼마 썼는지 한눈에.', ('#0E7490', '#0FB5A2', 'wallet', '/assets/prog/invest-dashboard.jpg')),
 ('project-commerce', '알리 소싱 도우미', 'biz', 'dev', '개발 중', 'Windows', 'v2.1', '팔 만한 해외 상품을 찾아 분석하고, 스마트스토어용 상품명·가격·홍보 글까지 만들어 줍니다.', ('#EA580C', '#F43F5E', 'cart', '')),
 ('program-trader', '송골트레이더', 'biz', 'dev', '개발 중', 'Windows', 'v0.3.0', '키움 모의·토스 실전 주식과 업비트 코인을 한 프로그램, 한 화면에서. 시장마다 엔진은 따로, 관제는 하나로.', ('#0B1530', '#22D3EE', 'chart', '/assets/prog/trader-stock.jpg')),
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
 lead='다들 하나씩은 가지고 계시죠? 나만의 자비스~! 집·일·프로그램을 한 화면에서, 목소리로 관리하는 송골랩 중앙관제(SONGGOLLAB HUD)입니다. 가운데 AI 코어를 중심으로, 내가 만든 프로그램들이 연결되는 순간 카드로 알아서 모입니다.',
 why='집에는 IoT 기기, 일에는 자동매매·SNS·3D 프린터·AI 도구가 있습니다. 프로그램이 하나씩 늘다 보니 창을 열고 닫는 데만 하루가 갔습니다. 무엇이 잘 돌고 무엇이 멈췄는지 한 화면에서 보고, 말로 묻고 시킬 수 있게 만들었습니다.',
 feats=[('카드로 자동 정리', '연결된 프로그램마다 카드 하나. 상태(연결·주의)와 꼭 알아야 할 숫자 한 줄만 보이고, 누르면 자세한 창이 열립니다.'),
        ('주소와 토큰만 넣으면 연결', '프로그램에 관제 주소와 토큰만 넣으면 첫 신호가 오는 순간 카드가 생깁니다. 보기 싫은 카드는 설정에서 숨깁니다.'),
        ('목소리로', '“자비스”라고 부르면 상시 듣기로 명령을 받습니다. 말 대신 글로 명령해도 됩니다.'),
        ('확인 카드', '출력 시작·정지처럼 되돌리기 어려운 일은 바로 하지 않고 확인 카드로 한 번 더 묻습니다.'),
        ('개발 현황판', '프로젝트 단계·로그인 점검·만료 일정·유료 구독을 한눈에 봅니다.'),
        ('폰 앱 · 전체 화면', '휴대폰에서 같은 관제를 보고, TV·모니터에는 전체 화면 관제 모드로 띄웁니다.')],
 flow=[('각 프로그램', '관제 주소 + 토큰으로 상태 보내기'), ('관제 서버', '첫 신호에 자동 등록 · 모아서 판정'), ('관제 화면', 'AI 코어 중심 카드 · 연결선'), ('목소리 · 조치', '묻고 시키기 · 위험한 일은 확인 카드')],
 log=[('v1.13', '노드 관제', '여러 PC·장치를 노드로 묶어 상태를 봅니다.'), ('v1.14 ~ 1.15', '메일 관제', '광고 메일 자동 정리, 관제 안에서 바로 읽기.'), ('v1.16', '방마다 지금', '송골집 창을 방별 현재 상태로.'), ('v1.17', '영화 같은 화면', '창이 열릴 때의 효과, 빛나는 연결선, 오늘의 뉴스 카드.'),
      ('v1.19.8', '연결 프로그램 15개 · 소개 영상', '송골오토트레이더·3D 프린터·AI Team·SNS 통합관리·앱 출시 현황까지 연결. 첫 소개 영상 공개 (2026-11-17).')],
 note='실제 운영 중인 화면입니다. 개인 금액·메일 이름은 가렸고, 접속 주소·토큰·보안 세부 사항은 공개하지 않습니다. 주식 쪽은 모의투자 화면이며 숫자는 기능 예시입니다.')
D['program-printbench'] = dict(
 lead='3D 프린터를 PC 한 화면에서 보고, 맡기고, 안전하게 돌리는 Windows 프로그램입니다. 출력 상태 확인부터 작업 대기열, 자동 슬라이스, 필라멘트 관리, 점검까지 한곳에서 합니다. 클라우드 없이 집 안 네트워크에서만 동작하고, 화면은 모두 한국어입니다.',
 why='3D 프린터는 출력 한 번에 몇 시간씩 걸립니다. 그동안 프린터 앞을 지키거나, 프린터 화면과 슬라이서를 오가며 확인해야 했습니다. 중고 프린터를 들인 날 바로 만들기 시작해, 그 일을 PC 한 화면으로 모았습니다.',
 feats=[('실시간 모니터링', '진행률, 남은 시간, 완료 예상 시각, 노즐·베드 온도와 그래프. 실제 출력 경로를 프린터 그림 안에서 3D로 보여 줍니다.'),
        ('작업 대기열 · 자동 슬라이스', '파일을 쌓아 두면 프린터가 비는 대로 순서대로 보냅니다. STL·3MF는 OrcaSlicer로 자동 슬라이스합니다.'),
        ('출력 전 미리보기', '설계 배치도, 슬라이스 결과, 첫 레이어를 그림으로 확인하고 층별 경로를 슬라이더로 봅니다.'),
        ('여러 대 · 필라멘트 관리', '프린터 여러 대에 작업을 나눠 보내고, 롤 용량을 등록하면 출력할 때마다 남은 양을 계산합니다.'),
        ('점검 · 캘리브레이션', '베드를 데운 뒤 레벨링·진동 보정을 한 번에 하는 전체 자가 점검, 통신·팬·가열을 확인하는 건강 점검.'),
        ('야간 조용 출력 · 자동 절전', '밤에는 출력 속도를 자동으로 낮추고, 출력이 없으면 히터·팬·조명을 끕니다. 휴대폰·ESP32-CAM을 카메라로 씁니다.')],
 flow=[('파일 넣기', 'G-code · STL · 3MF'), ('자동 슬라이스', '미리보기 그림 생성'), ('인터락 점검', '재료 · 온도 · 기종 · 노즐 · 잔량'), ('출력', '베드 비움 확인 후 시작'), ('모니터링', '필라멘트 자동 차감 · 완료 알림')],
 safety_title='출력 전에 막아 주는 안전장치 (인터락)',
 safety=[('재료', 'PLA용 G-code를 PETG가 걸린 프린터에서 시작하려 하면 막습니다.'), ('온도', '재료별 안전 범위를 벗어난 노즐·베드 온도면 막습니다.'), ('기종 · 노즐', '다른 기종용 G-code나 노즐 지름이 다르면 막습니다.'),
         ('잔량', '남은 필라멘트가 모자랄 것 같으면 막습니다.'), ('가장자리', '첫 레이어가 베드 끝까지 오면 알려 줍니다.'), ('막힌 이유를 그대로', '확인창에 이유를 보여 주고, 꼭 필요하면 한 번 더 확인한 뒤 시작합니다. 그 기록이 남습니다.')],
 env='Windows 10/11 64비트 · Creality K 계열 순정 펌웨어(K1에서 확인), Klipper·Bambu Lab은 준비 중 · PC와 프린터가 같은 공유기 · 자동 슬라이스는 OrcaSlicer 필요 · 인터넷은 모델 찾기에만 사용',
 log=[('v0.4', '첫 연결', '중고 K1을 들인 날, 모니터링부터 시작.'), ('v0.9', '대기열 · 인터락 · 점검', '작업 대기열과 자동 슬라이스, 출력 시작 인터락, 전체 자가 점검, 야간 조용 출력.'), ('2026-11', '중앙관제 연결 · 소개 영상', '관제 화면에 진행률·온도 카드, 90초 소개 영상 공개.')],
 note='Creality, K1, Bambu Lab, OrcaSlicer, Printables는 각 회사의 상표이며, 이 프로그램은 해당 회사와 관계가 없는 독립 프로그램입니다. 화면 속 프린터 주소는 예시 값입니다.')
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
 lead='프로젝트 11개가 쓰는 60여 개 사이트의 로그인·API 키 상태를 한 화면에서 보고, 끊기면 바로 알려 주는 Chrome 확장 도구입니다. 자동화가 갑자기 멈추면 코드보다 로그인부터 의심하세요.',
 why='송골랩의 프로젝트는 대부분 밤사이나 정해진 시간에 혼자 돌아가는 자동화예요. 그런데 멈춘 이유를 찾아보면 코드 문제가 아니라 어딘가 로그인이 끊겨 있는 경우가 많았어요. 앱 세션 만료, 7일 만에 풀린 구글 연결, 기한이 지난 API 키… 한 달 사이에 두 번이나 이것 때문에 작업이 통째로 멈췄어요. 그래서 "어디가 끊겼는지 한 화면에서 보고, 끊기면 바로 알려 주는" 도구를 직접 만들었어요.',
 feats=[('한눈에 보는 점검판', '모든 사이트를 끊김 · 확인 필요 · 만료 임박 · 정상 네 가지로 나눠 보여 주고, 문제 있는 곳이 항상 맨 위로 올라와요.'),
        ('「지금 챙길 것」', '끊기면 모든 자동화가 멈추는 「바탕」 항목은 따로 띄우고, 바로 열어서 로그인하는 버튼을 붙였어요.'),
        ('툴바에서 바로 확인', '끊긴 곳이 있으면 아이콘에 빨간 숫자, 새로 끊기면 Windows 알림. 10분마다 자동 점검하고 로그인·로그아웃 3초 뒤 다시 확인해요.'),
        ('로그인 방법 기록', '사이트마다 로그인 방법, 어느 계정, 비번 금고 저장 여부, 2단계 인증 종류를 적어 둬요. 금고에 없는 곳은 빨간 표시.'),
        ('구글 계정 복구 점검', '대부분의 로그인이 묶인 구글 계정 두 개의 복구 전화·복구 이메일·백업 코드 준비 여부를 맨 위에 고정했어요.'),
        ('API 키 만료 달력', 'API 키·토큰·무료 체험 기한을 D-day로 계산하고, 14일 전부터 「만료 임박」으로 바꿔 알려 줘요.')],
 flow=[('쿠키 (자동)', '그 사이트의 로그인 쿠키와 만료일 확인'), ('접속 (자동)', '집 안 서버에 접속되는지 확인'), ('만료일', '키·토큰·체험 기간을 D-day로'), ('직접 확인', '앱·CLI는 열어 보고 「확인함」, 2주 뒤 다시 알림')],
 log=[('v1.0', '첫 버전', '점검판, 툴바 팝업, 로그인 방법 기록, 구글 복구 점검, API 키 탭과 만료 달력.'), ('다음', '중앙관제 연동', '점검 결과를 관제실로 보내 끊기면 음성으로 알려 주게 할 예정이에요.'), ('다음', 'PC 점검 자동화 · 새 프로젝트 자동 등록', '데스크톱 앱·CLI 로그인·드라이브 동기화·절전 모드를 관제 PC가 직접 확인하고, 새 프로젝트의 사이트를 같은 양식으로 합쳐요.')],
 note='이 프로그램에는 비밀번호와 API 키 값을 절대 저장하지 않아요. 비밀번호는 전용 금고에만 두고, 점검판은 "어디에, 어떻게"만 기억해요. 비밀번호를 대신 입력하거나 세션을 몰래 연장하지 않고, 상태를 보고 알려 주는 것까지만 해요. 화면 속 상태값은 예시이며, 지금은 송골랩 내부용 Chrome 확장(v1.0)입니다.')
D['program-invest'] = dict(
 lead='알리익스프레스·G마켓 구매 내역을 프로젝트별로 자동 분류하고, 월별로 얼마 썼는지 한눈에 보는 Windows 프로그램입니다. 매주 주문 내역이 자동으로 쌓이고, 사람은 \'확인 필요\' 몇 건만 보면 됩니다.',
 why='홈IoT, 드라이브 콘솔, AI 비전카메라, 3D프린터, 온실 같은 프로젝트를 동시에 진행하면서 부품은 대부분 해외직구로 삽니다. 몇 달 지나면 "이 센서는 어느 프로젝트에 쓴 거였지?", "이번 달 홈IoT에만 얼마 들었지?"를 알기 어려워졌습니다. 주문 내역을 엑셀에 옮겨 적는 대신, 매주 자동으로 모으고 프로젝트별로 나눠 주는 프로그램을 만들었습니다.',
 feats=[('대시보드', '월·프로젝트·구매처로 걸러 보고, 이번 달 합계·구매 건수·가장 많이 쓴 프로젝트·확인 필요 건수를 한 화면에. 표에서 프로젝트를 바로 바꾸면 다음 업데이트 때도 유지됩니다.'),
        ('분석 — 숫자 대신 문장으로', '월말 예상, 직전 3개월 평균, 누적 투자. "전월보다 12% 늘었어요", "이 속도면 예산을 넘어요"처럼 문장으로 알려 줍니다.'),
        ('프로젝트별 예산', '월 예산을 넣으면 사용률 막대로 보여 주고, 프로젝트 × 월 표와 고액 지출 TOP 10을 함께 봅니다.'),
        ('매주 자동 업데이트', '주문 수집 → 키워드 규칙 + AI 분류 → 드라이브 저장 → 프로그램이 1분마다 확인해 반영. 중복은 걸러지고 취소 주문은 지워집니다.'),
        ('중앙관제 연동', '이번 달 합계, 프로젝트별 합계, 확인 필요 건수, 예산 초과 경고를 관제실로 보냅니다.'),
        ('이런 분께', '여러 DIY·IoT 프로젝트를 하며 해외직구를 자주 하는 분, 프로젝트별 원가를 알고 싶은 1인 사업자·메이커.')],
 flow=[('주문 내역 수집', '매주 알리·G마켓 최근 14일'), ('프로젝트 분류', '키워드 규칙 + AI 판단, 애매하면 확인 필요'), ('드라이브 저장', '주간 데이터 폴더에 JSON·CSV'), ('프로그램 반영', '1분마다 확인 · 중복 방지')],
 log=[('v1.0', '첫 버전', '대시보드, SQLite 저장, 분류 규칙, 자동 반영, 트레이 상주, 중앙관제 API.'), ('v1.1', '분석 탭', '월말 예상, 자동 분석 문장, 프로젝트별 예산, 고액 지출 TOP 10.'), ('v2.0', '설치형 · 주간 폴더 감시', 'Windows 설치 프로그램, 드라이브 주간 데이터 폴더를 1분마다 자동 확인.')],
 note='화면 이미지는 기능 설명용 예시이며, 표시된 금액은 예시 데이터입니다. 사용 기술: Python · SQLite · 로컬 API · 예약 작업(주간 수집) · 구글 드라이브 동기화.')
D['project-commerce'] = dict(
 lead='알리익스프레스에서 팔 만한 상품을 AI와 API로 찾아 분석하고, 네이버 스마트스토어용 해외구매대행 상품으로 정리해 블로그 홍보 글까지 만들어 주는 Windows 프로그램 「알리 소싱 도우미」입니다.',
 why='작은 판매자가 상품을 찾고, 사진·설명을 다듬고, 가격을 계산하고, 홍보 글을 쓰는 일은 매번 같은 반복입니다.',
 feats=[('상품 찾기 · 분석', '팔 만한 상품을 찾아 가격·배송·리뷰를 분석합니다.'), ('취급 가능 판정', '전기용품·생활용품 안전관리 기준으로 구매대행 가능한 품목인지 먼저 거릅니다.'),
        ('검색 노출 점수', '상품명 점수, 키워드 검색량·경쟁 상품 수로 키워드를 고르고 AI가 상품명을 다듬습니다.'), ('마진 계산', '수수료·반품 충당·광고비까지 넣어 남는 돈을 계산합니다.'),
        ('카테고리 자동', '경쟁 상품을 보고 카테고리를 자동으로 고릅니다.'), ('홍보 글', '블로그용 상품 소개 글을 만듭니다.')],
 flow=[('찾기', '해외 상품 후보'), ('거르기', '취급 가능 판정'), ('다듬기', '상품명·가격·카테고리'), ('올리기', '스마트스토어'), ('알리기', '블로그 글')],
 log=[('v1.x', '쿠팡 전용판', '쿠팡용으로 시작해 v1.9.1에서 마무리.'), ('v2.0', '네이버 전용으로 전환', ''), ('v2.1', '노출 최적화 · 자동 운영', '키워드 점수, AI 상품명, 마진 정밀화.')],
 note='판매·통관 관련 법규를 지키는 범위에서만 씁니다. 개인통관고유부호 등 고객 정보는 프로그램에 저장하지 않습니다.', image=('auto', '상품 등록 자동화 콘셉트'))
D['program-trader'] = dict(
 lead='키움 모의 · 토스 실전 주식과 업비트 코인을 한 프로그램, 한 화면에서 관리하는 Windows용 자동매매 관제 프로그램입니다. 따로 쓰던 주식 자동매매와 코인 자동매매를 송골트레이더 하나로 합쳤습니다. 시장마다 엔진은 따로 돌고, 사람은 한 화면에서 모두 봅니다.',
 why='주식 프로그램과 코인 프로그램을 따로 켜 두니 창도, 설정도, 복기도 두 벌이었습니다. 시장은 달라도 보는 사람은 한 명이라서, 화면은 하나로 모으고 엔진은 시장별로 분리해 서로 영향을 주지 않게 만들었습니다.',
 feats=[('네온 BUY / SELL 레이더', '매수 후보는 왼쪽 초록 영역, 매도 신호는 오른쪽 빨간 영역에 점으로 찍힙니다. 가운데에 가까울수록 신호가 강합니다. 위쪽 탭으로 키움 모의 · 토스 실전 · 업비트 코인을 바꿔 봅니다.'),
        ('차트 · 호가 · 체결', '감시 종목의 분봉 차트, 이동평균, 매수·매도 표시, 거래량과 체결강도를 한 화면에서 봅니다.'),
        ('수익률 현황', '누적·오늘·이번 달 수익률, 자산 추이, 일별 손익과 승률을 시장별로 정리합니다.'),
        ('복기 회의 — Claude AI', '장이 끝나면 Claude가 그날 매매를 정리하고, 매수 전 심사(진행·보류)의 결과를 30분 뒤 수익률로 다시 확인합니다.'),
        ('분석 · 감지 기록 · 매매 기록', '거래량 급증·호가 불균형·체결 쏠림 같은 감지 신호가 실제로 맞았는지 1분·5분·30분 뒤 수익률로 검증하고, 체결 내역을 남깁니다.'),
        ('보유 종목 자동 / 직접', '종목마다 프로그램에 맡길지(자동), 내가 직접 할지(직접)를 버튼 하나로 바꿉니다.'),
        ('설정 — API 연결 · 위험 한도', '증권사·거래소 키 연결, 1회 주문·종목당 최대·하루 매수 합계·하루 손실 한도·원금 보호선·진입 점수를 항목별로 정합니다.')],
 flow=[('시세 수신', '주식 · 코인 시장별 엔진'), ('신호 감지', '거래량 · 호가 · 체결'), ('점수 · 심사', '진입 점수 · Claude 심사'), ('주문 · 한도', '자동 · 직접, 위험 한도'), ('복기', '수익률 · 복기 회의')],
 safety=[('출금 기능 없음', '프로그램에는 출금 기능이 아예 없습니다.'), ('손실 한도 · 원금 보호선', '하루 손실 한도나 원금 보호선에 닿으면 그날 신규 매수를 멈춥니다.'), ('엔진 중복 실행 방지', '같은 시장 엔진이 두 번 켜지지 않습니다.'), ('바꾸기 전 확인', '설정을 바꿀 때 바뀌기 전 → 후 값을 보여 주고 확인을 받습니다.'), ('긴급 정지 · 전량 청산', '버튼 하나로 모든 엔진을 멈추고 보유분을 정리합니다.'), ('토스 실전은 따로', '실전 계좌는 별도 한도로 운영하고, 관제 화면은 주문을 보내지 않습니다.')],
 log=[('주식 v0.4', '주식 자동매매 따로 개발', '키움 모의로 검증, 금감원 공시 연동, 장 마감 복기.'), ('코인 v0.3', '코인 자동매매 따로 개발', '업비트 전 종목 감시, 매매 실험실.'), ('v0.3.0', '송골트레이더로 통합', '네온 레이더 대시보드, Claude 복기 회의, 시장별 엔진 분리 (2026-11).')],
 env='Windows 10/11 64비트, 설치 파일 하나. 키는 이 PC에만 Windows 보호 기능(DPAPI)으로 암호화해 저장합니다.')
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
 'program-printbench': [('/assets/prog/pb-monitor.jpg', '모니터링 — 프린터 그림 안에 출력물이 쌓이는 모습, 진행률·남은 시간·온도'),
   ('/assets/prog/pb-queue.jpg', '작업 대기열 — 설계 배치도·슬라이스 결과·첫 레이어 미리보기, 3D 경로'),
   ('/assets/prog/pb-printers.jpg', '프린터 — 여러 대를 카드로, 일괄 출력·베드 비움 확인'),
   ('/assets/prog/pb-check.jpg', '점검·설정 — 이동, 필라멘트 잔량, 캘리브레이션, 건강 점검'),
   ('/assets/prog/pb-models.jpg', '모델 찾기 — Printables 검색, 3D로 돌려 보고 대기열에'),
   ('/assets/prog/pb-settings.jpg', '설정 — 프린터 연결, 재료 프리셋, 카메라, 작업함·슬라이서'),
   ('/assets/prog/pb-interlock.jpg', '출력 시작 인터락 — 항목별로 켜고 끄기'),
   ('/assets/prog/pb-calib.jpg', '캘리브레이션 — 전체 자가 점검'),
   ('/assets/prog/pb-night.jpg', '야간 조용 출력 — 22:00~07:00 속도 50%')],
 'program-trader': [('/assets/prog/trader-stock.jpg', '대시보드 · 주식 — 네온 BUY/SELL 레이더, 감시 종목, 오늘 수익률 (화면 예시 · 예시 데이터)'),
   ('/assets/prog/trader-coin.jpg', '대시보드 · 코인 — 업비트 탭으로 바꾸면 같은 레이더에 코인이 찍힙니다 (화면 예시)'),
   ('/assets/prog/trader-chart.jpg', '차트 — 분봉 차트, 이동평균, 매수·매도 표시, 거래량과 체결강도'),
   ('/assets/prog/trader-return.jpg', '수익률 현황 — 누적·오늘 수익률, 자산 추이, 일별 손익 (예시 데이터)'),
   ('/assets/prog/trader-review.jpg', '복기 회의 — Claude가 그날 매매를 정리하고, 매수 심사 결과를 30분 뒤 수익률로 확인'),
   ('/assets/prog/trader-analysis.jpg', '분석 — 승률·손익비, 감지 신호별 적중률, 장기 점수 상위 종목'),
   ('/assets/prog/trader-detect.jpg', '감지 기록 — 거래량 급증 · 호가 불균형 · 체결 쏠림 신호와 1·5·30분 뒤 결과'),
   ('/assets/prog/trader-trades.jpg', '매매 기록 — 체결 내역과 실현 손익 (예시 데이터)'),
   ('/assets/prog/trader-hold.jpg', '보유 종목 — 종목마다 자동 / 직접 전환, 안전선 게이지'),
   ('/assets/prog/trader-api.jpg', '설정 · API 연결 — 키는 이 PC에만 암호화해 저장 (빈 입력 칸 화면)'),
   ('/assets/prog/trader-risk.jpg', '설정 · 위험 한도 — 1회 주문, 하루 손실 한도, 원금 보호선, 진입 점수')],
 'drive-console': [('/assets/drive-console.jpg', '태블릿 메인 화면'), ('/assets/prog/dc-phone.jpg', '휴대폰 세로 메인 화면 (v1.3.56)', 'tall'), ('/assets/drive-console-2.jpg', '차량 정보 화면')],
 'airang': [('/assets/airang-phone.jpg', '아이랑 휴대폰 화면', 'tall')],
 'project-home-iot': [('/assets/prog/home-main.jpg', '홈 화면 — 집 전체 상태, 전력 흐름, 장면, 방별 조명·온도·커튼, 보안'), ('/assets/prog/home-auto.jpg', '장면 · 자동화 — 아침 조명, 해 질 때 커튼, 빈 방 끄기, 외출 소등, 밤 소등'), ('/assets/prog/home-energy.jpg', '에너지 — 지금 쓰는 전력, 가전별 전력, 태양광·배터리·전기차 연결 상태'), ('/assets/prog/home-radio.jpg', '라디오 — 월패드에서 바로 듣는 즐겨찾기 방송, 꺼짐 예약')],
 'project-control': [('/assets/prog/control-v1198-10.jpg', '메인 화면 — 가운데 AI 코어를 중심으로 연결된 프로그램이 카드로 모입니다 (v1.19.8 실제 화면)'),
   ('/assets/prog/control-v1198-19.jpg', '카드마다 상태(연결·주의)와 핵심 숫자 한 줄, 누르면 자세한 창'),
   ('/assets/prog/control-v1198-42.jpg', '송골홈 — 방마다 조명·문·센서·냉장고 온도 (Home Assistant 연결)'),
   ('/assets/prog/control-v1198-49.jpg', '3D 프린터 — 진행률·노즐·베드 온도 실시간, 출력 시작은 확인 카드로'),
   ('/assets/prog/control-v1198-55.jpg', 'AI Team — 여러 AI에 일을 나눠 맡기고 지금 하는 일·검수 대기를 한눈에'),
   ('/assets/prog/control-v1198-62.jpg', 'SNS 통합관리 — 스레드 방문·팔로워·댓글·예약 글'),
   ('/assets/prog/control-v1198-69.jpg', '그 밖의 연결 프로그램 — 뉴스·Home Assistant·아이랑 정보·투자비·메일·앱 출시·노드 관제'),
   ('/assets/prog/control-v1198-77.jpg', '연결·설정 — 주소와 토큰만 넣으면 첫 신호에 자동 등록'),
   ('/assets/prog/control-v1198-84.jpg', '목소리로 — “자비스, 프린터 어때?” 위험한 명령은 확인 카드로')],
 'program-ai-team': [('/assets/prog/aiteam-flow.jpg', 'AI 팀 작업실이 일하는 방식'), ('/assets/prog/aiteam-home.jpg', '홈 화면 — 팀장 AI와 팀원 AI 연결 (재현 화면)'), ('/assets/prog/aiteam-order.jpg', '지시 화면 — 프로젝트별 대화와 지금 일하는 AI'), ('/assets/prog/aiteam-phone.jpg', '휴대폰 화면', 'tall')],
 'program-login': [('/assets/prog/login-01-dashboard.jpg', '점검판 메인 화면 — 문제 있는 곳이 항상 맨 위로 (화면 속 상태값은 예시)'), ('/assets/prog/login-02-popup.jpg', 'Chrome 툴바 아이콘을 누르면 뜨는 요약 팝업', 'tall'), ('/assets/prog/login-04-login-method.jpg', '사이트마다 "어떻게 로그인하는지"를 적어 두는 칸', 'tall'), ('/assets/prog/login-03-google-recovery.jpg', '맨 위에 고정한 구글 계정 복구 수단 점검'), ('/assets/prog/login-05-api-keys.jpg', '「API 키·토큰」 탭과 오른쪽 만료일 달력')],
 'program-invest': [('/assets/prog/invest-dashboard.jpg', '대시보드 — 이번 달 투자비, 프로젝트별·월별 그래프, 구매 내역에서 프로젝트 바로 바꾸기 (화면 예시 · 예시 데이터)'), ('/assets/prog/invest-analysis.jpg', '분석 — 월말 예상, 자동 분석 문장, 프로젝트별 예산 사용률, 프로젝트 × 월 표 (화면 예시 · 예시 데이터)'), ('/assets/prog/invest-flow.jpg', '매주 자동 업데이트 4단계 — 수집 → 분류 → 드라이브 저장 → 프로그램 반영')],
 'project-commerce': [('/assets/prog/ali-final.jpg', '마켓 등록 초안 확인 — 노출 최적화, 마진, 취급 판정')],
}
V = {
 'program-printbench': [('IrBtIR7gi1k', '3D 프린터 관리 프로그램, 직접 만들었습니다 (90초)')],
 'project-control': [('zH4ejgkLxcM', '나만의 자비스~! 송골랩 중앙관제 소개 (1분 34초)')],
 'drive-console': [('T9bEMuzRCQA', '30초 소개'), ('rpFFTn9Ux6Q', '3분 기능 설명 v1.3'), ('wwWg9VWy7Y4', '테스터 모집')],
 'airang': [('YRNth4rPD_I', '아이랑 경기'), ('y_lwf2FhGaQ', '아이랑 서울 25개 구'), ('uvaTydTX3Bk', '아이랑 충남')],
 'project-home-iot': [('jB_N9SyBGMU', 'IoT 이야기 EP.1'), ('66hwKAWMw84', 'EP.3 스마트홈의 하루'), ('mKFjxUG26es', 'EP.4 새는 전기 막기')],
 'program-lagrills': [('jSeZK3VLMT4', '라그릴스 허브 v2.6 소개'), ('oSnE9LrclWM', '셀프 바베큐장 라그릴스')],
 'project-farm': [('05GXvZZknDs', 'IoT 이야기 EP.5 — 멀리서 살피기')],
}
R = {
 'program-printbench': [('https://www.instagram.com/reel/Dfzp4hBtetm/', '인스타그램 릴스 ↗', '같은 소개 영상을 인스타에서 보기'), ('https://www.youtube.com/shorts/IrBtIR7gi1k', '유튜브 쇼츠 ↗', '90초 소개 영상')],
 'project-control': [('https://www.instagram.com/reel/Df1KJ2CqsRY/', '인스타그램 릴스 ↗', '나만의 자비스~! 소개 영상을 인스타에서 보기'), ('https://songgollab.blogspot.com', '송골랩 블로그 ↗', '연결된 프로그램 하나하나의 소개 글'), ('/project-home-iot', '송골집 IoT', '방마다 조명·문·센서'), ('/program-trader', '송골트레이더', '주식·코인 자동매매 (개인 테스트용)'), ('/program-ai-team', 'AI Team', '여러 AI에 일을 나눠 맡기는 작업실'), ('/program-sns', 'SNS 통합관리', '인스타·스레드·블로그 한곳에서')],
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
    def one(i, t):
        if i.startswith('/'):
            return f'<div class="video"><video src="{i}" poster="{i[:-4]}.jpg" controls preload="none" playsinline style="width:100%;height:100%;background:#000"></video></div><p class="vlabel">{t}</p>'
        return yt(i, t)
    return '<div class="vids">' + ''.join(f'<div>{one(i, t)}</div>' for i, t in items) + '</div>'

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
    tl = [('feat', '주요 기능'), ('how', '동작 방식')] + ([('safe', '안전장치')] if D[slug].get('safety') else []) + [('gallery', '이미지')] + ([('video', '영상')] if V.get(slug) else []) + ([('docs', '자료')] if R.get(slug) else []) + [('log', '개발 기록')]
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
    if d.get('safety'):
        body += sec(boxes(d['safety'], 3) + (f'<p class="p" style="margin-top:18px"><b>사용 환경</b> · {d["env"]}</p>' if d.get('env') else ''), 'safe', 'Safety · 안전장치', d.get('safety_title', '돈이 걸린 프로그램이라 먼저 막아 둔 것'), cls='alt')
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
    PAGES['projects'] = ('프로그램', '송골랩이 직접 만들고 쓰는 프로그램 14개 — 드라이브 콘솔, 아이랑, 송골집 IoT, 라그릴스 허브, 중앙관제, AI Team, SNS 통합관리, 알리 소싱 도우미, 송골트레이더 등.', 'projects',
                         hero + g['sec'](filters() + catalog(), cls='tight') + g['band']('관심 가는 프로그램이 있나요?', '써 보고 싶거나, 비슷한 걸 만들고 싶다면 편하게 연락 주세요.', g['btn']('/contact', '문의하기')), 'ko', FILTER_JS)
