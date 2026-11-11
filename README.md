# 송골랩 홈페이지 (songgollab.co.kr)

정적 사이트입니다. 서버·데이터베이스 없이 HTML 파일만으로 돌아갑니다.

- `index.html` — 첫 화면 (직접 편집)
- 나머지 페이지 — `build.py` 안에 글이 있습니다. 고친 뒤 `python build.py` 를 실행하면 `*.html` 이 다시 만들어집니다.
- `assets/` — 로고, 사진, 공통 스타일(`base.css` + `pages.css` → `site.css`), 공통 스크립트(`site.js`)
- 블로그 글은 계속 Google Blogger(songgollab.blogspot.com)에 둡니다.

주소는 `.html` 없이 씁니다 (예: `/drive-console`). Cloudflare Pages·GitHub Pages 모두 그대로 동작합니다.
