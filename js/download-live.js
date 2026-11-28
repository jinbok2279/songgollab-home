/*
 * 다운로드 페이지 자동 갱신 (송골랩 체험판 서버 공개 목록)
 *
 * - 체험판 관리 프로그램에서 버전을 등록하면, 이 스크립트가 서버 목록을 읽어
 *   다운로드 버튼 · 버전 · 날짜 · 크기 · SHA-256 · 파일 이름을 바꿉니다.
 * - 서버에 연결되지 않으면 HTML에 적힌 내용을 그대로 보여 줍니다.
 * - /download/            : data-live 가 붙은 카드만 갱신, 목록에 없는 새 프로그램은 카드를 추가,
 *                           관리 프로그램에 등록됐지만 공개를 끈 프로그램(data-live 카드)은 숨김
 * - /download/<app>/      : 상세 페이지의 버튼·버전 정보·버전 기록 표를 갱신
 * 서버가 내보내는 값: app, name, desc, platform, url, fileName, version, date, notes, sha256, size (개인정보 없음)
 */
(function () {
  'use strict';
  var CATALOG = 'https://script.google.com/macros/s/AKfycbyGoa2YuUVN2UFibTpRw4TskrEEsBJfj3g2VlAo4nyJorRalQtSX9l5ehDourgR_pGh/exec?catalog=1';

  function ymd(ms) {
    var d = new Date(ms + 9 * 3600 * 1000);   // 한국 시간
    return d.toISOString().slice(0, 10);
  }
  function mb(bytes) {
    var v = bytes / 1048576;
    return (v >= 10 ? Math.round(v * 10) / 10 : Math.round(v * 100) / 100).toString().replace(/\.0+$/, '') + 'MB';
  }
  function verNum(v) { return String(v || '').split(/[^0-9]+/).filter(Boolean).map(Number); }
  function newer(a, b) {
    var x = verNum(a), y = verNum(b);
    for (var i = 0; i < Math.max(x.length, y.length); i++) {
      var d = (x[i] || 0) - (y[i] || 0);
      if (d) return d > 0;
    }
    return false;
  }
  function safeUrl(u) { return /^https:\/\/drive\.google\.com\//.test(u) ? u : ''; }
  function txt(el, s) { if (el && s) el.textContent = s; }

  /* 카드(목록 페이지) 갱신 */
  function fillCard(card, p) {
    var url = safeUrl(p.url);
    var btn = card.querySelector('.dl-act a.btn-primary');
    if (btn && url) btn.href = url;
    var soft = card.querySelectorAll('.chips .chip-soft');
    soft.forEach(function (c) {
      var t = c.textContent.trim();
      if (/^v\d/.test(t) && p.version) c.textContent = 'v' + p.version;
      else if (/^\d{4}-\d{2}-\d{2}$/.test(t) && p.date) c.textContent = ymd(p.date);
      else if (/MB$/.test(t) && p.size) c.textContent = mb(p.size);
    });
    var sub = card.querySelector('.dl-sub');
    if (sub && p.size) sub.textContent = (p.platform || 'Windows') + ' · ' + mb(p.size);
    fillHash(card, p);
  }
  function fillHash(root, p) {
    var hash = root.querySelector('.dl-hash');
    if (hash) {
      if (p.sha256) txt(hash.querySelector('code'), p.sha256);
      else hash.style.display = 'none';   // 새 파일의 값을 모르면 옛 값을 보이지 않음
    }
    root.querySelectorAll('.dl-note code, .dd-meta code').forEach(function (c) {
      if (/\.(exe|apk|msi|zip)$/i.test(c.textContent) && p.fileName) c.textContent = p.fileName;
    });
  }

  /* 새 프로그램 카드 만들기 */
  function el(tag, cls, text) { var e = document.createElement(tag); if (cls) e.className = cls; if (text) e.textContent = text; return e; }
  function makeCard(p) {
    var a = el('article', 'dl-row'); a.id = p.app; a.setAttribute('data-live', '');
    var icon = el('div', 'dl-icon');
    icon.innerHTML = '<svg class="glyph" viewBox="0 0 54 54" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="7" y="10" width="40" height="28" rx="3"/><path d="M19 46h16M27 38v8"/></svg>';
    var main = el('div', 'dl-main'), chips = el('div', 'chips');
    chips.appendChild(el('span', 'chip', p.platform || 'Windows'));
    if (p.version) chips.appendChild(el('span', 'chip chip-soft', 'v' + p.version));
    if (p.date) chips.appendChild(el('span', 'chip chip-soft', ymd(p.date)));
    if (p.size) chips.appendChild(el('span', 'chip chip-soft', mb(p.size)));
    chips.appendChild(el('span', 'chip chip-soft', '30일 무료 체험'));
    main.appendChild(chips);
    main.appendChild(el('h3', '', p.name));
    if (p.desc) main.appendChild(el('p', '', p.desc));
    if (p.sha256) { var h = el('p', 'dl-hash'); h.appendChild(el('span', '', 'SHA-256')); h.appendChild(el('code', '', p.sha256)); main.appendChild(h); }
    if (p.fileName) { var n = el('p', 'dl-note'); n.appendChild(document.createTextNode('파일: ')); n.appendChild(el('code', '', p.fileName)); n.appendChild(document.createTextNode(' · 구글 드라이브에서 받습니다')); main.appendChild(n); }
    var act = el('div', 'dl-act'), b = el('a', 'btn btn-primary', '무료 체험판 다운로드');
    b.href = safeUrl(p.url); b.rel = 'noopener';
    act.appendChild(b);
    if (p.size) act.appendChild(el('span', 'dl-sub', (p.platform || 'Windows') + ' · ' + mb(p.size)));
    a.appendChild(icon); a.appendChild(main); a.appendChild(act);
    return a;
  }
  function groupFor(platform) {
    var want = platform === 'Android' ? /안드로이드|Android/ : /Windows/;
    var groups = document.querySelectorAll('.dl-group');
    for (var i = 0; i < groups.length; i++) {
      var h = groups[i].querySelector('h2');
      if (h && want.test(h.textContent)) return groups[i];
    }
    return null;
  }

  function onList(list, managed) {
    var byApp = {}, isManaged = {};
    (managed || []).forEach(function (a) { isManaged[a] = true; });
    list.forEach(function (p) { if (p && p.app && safeUrl(p.url)) byApp[p.app] = p; });

    // 목록 페이지
    if (document.querySelector('.dl-group')) {
      document.querySelectorAll('article.dl-row[data-live]').forEach(function (card) {
        var p = byApp[card.id];
        if (p) { fillCard(card, p); delete byApp[card.id]; }
        else if (isManaged[card.id]) card.style.display = 'none';   // 관리 프로그램에서 공개를 끔
      });
      Object.keys(byApp).forEach(function (k) {
        if (document.getElementById(k)) return;
        var g = groupFor(byApp[k].platform);
        if (g) g.appendChild(makeCard(byApp[k]));
      });
      return;
    }

    // 상세 페이지 /download/<app>/
    var m = location.pathname.match(/\/download\/([a-z0-9-]+)\/?/);
    var p = m && byApp[m[1]];
    if (!p) return;
    var url = safeUrl(p.url);
    document.querySelectorAll('.dd-cta a.btn-primary').forEach(function (b) {
      if (url) b.href = url;
      if (p.size) b.textContent = b.textContent.replace(/\d+(\.\d+)?MB/, mb(p.size));
    });
    document.querySelectorAll('.dd-cta .dd-meta').forEach(function (meta) {
      meta.textContent = meta.textContent
        .replace(/^v[\d.]+/, p.version ? 'v' + p.version : '$&')
        .replace(/\d{4}-\d{2}-\d{2}/, p.date ? ymd(p.date) : '$&');
    });
    fillHash(document, p);
    // 버전 기록 표에 새 버전 한 줄 추가
    var body = document.querySelector('.pv-table tbody');
    var first = body && body.querySelector('tr th');
    if (body && p.version && first && newer(p.version, first.textContent.trim())) {
      var tr = document.createElement('tr');
      tr.appendChild(el('th', '', 'v' + p.version));
      tr.appendChild(el('td', '', p.date ? ymd(p.date) : ''));
      tr.appendChild(el('td', '', p.notes || '새 버전'));
      body.insertBefore(tr, body.firstChild);
    }
  }

  function load() {
    var ctl = window.AbortController ? new AbortController() : null;
    var timer = setTimeout(function () { if (ctl) ctl.abort(); }, 8000);
    fetch(CATALOG, ctl ? { signal: ctl.signal } : {})
      .then(function (r) { return r.json(); })
      .then(function (d) { clearTimeout(timer); if (d && d.ok && Array.isArray(d.programs)) onList(d.programs, d.managed); })
      .catch(function () { clearTimeout(timer); /* 연결 실패: HTML 내용 그대로 */ });
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', load);
  else load();
})();
