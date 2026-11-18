# 송골랩 홈페이지 (songgollab.co.kr)

정적 사이트입니다. 서버·데이터베이스 없이 HTML 파일만으로 돌아갑니다.

- `index.html` — `workshop.py`에서 생성하는 첫 화면
- 나머지 페이지 — `build.py` 안에 글이 있습니다. 고친 뒤 `python build.py` 를 실행하면 `*.html` 이 다시 만들어집니다.
- `assets/` — 로고, 사진, 공통 스타일(`base.css` + `pages.css` → `site.css`), 공통 스크립트(`site.js`)
- `en.py` — 영문 페이지와 메뉴, 번역 데이터. `EN_PAGES`가 한/영 전환과 영문 내부 링크를 연결합니다. 현재 `/en/` 아래 23개 페이지입니다.
- `drive-console-en.html` — 기존 영문 안내 페이지를 유지합니다. `/en/drive-console`은 새로 만들지 않습니다.
- 블로그 글은 계속 Google Blogger(songgollab.blogspot.com)에 둡니다.

주소는 `.html` 없이 씁니다 (예: `/drive-console`). Cloudflare Pages·GitHub Pages 모두 그대로 동작합니다.

영문판을 수정한 뒤에도 `python build.py`로 전체를 재생성합니다. 개별 제작 페이지의 한국어 문장이 바뀌면 `en.py`의 해당 `TEXT` 번역도 갱신해야 합니다. 번역이 빠진 문장은 빌드 오류로 알려 줍니다. 공개 제한으로 제외한 화면은 `PRIVATE_MEDIA`에 기록되어 있습니다. 영문 작업 일지는 최근 17개 항목을 싣고 전체 한국어 기록으로 연결합니다.
