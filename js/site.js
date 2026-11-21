/* SONGGOL LAB — small site behaviours (no libraries).
   menu toggle · scroll reveal · project filters · click-to-play videos · latest blog posts */
(function () {
  "use strict";
  document.documentElement.classList.remove("no-js");
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  // ---- mobile menu
  var btn = document.querySelector(".menu-btn");
  var nav = document.getElementById("site-nav");
  if (btn && nav) {
    btn.addEventListener("click", function () {
      var open = nav.classList.toggle("is-open");
      btn.setAttribute("aria-expanded", String(open));
      btn.setAttribute("aria-label", open ? "메뉴 닫기" : "메뉴 열기");
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && nav.classList.contains("is-open")) { nav.classList.remove("is-open"); btn.setAttribute("aria-expanded", "false"); btn.focus(); }
    });
  }

  // ---- reveal on scroll
  var els = document.querySelectorAll(".reveal");
  if (reduce || !("IntersectionObserver" in window)) {
    [].forEach.call(els, function (el) { el.classList.add("is-in"); });
  } else {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add("is-in"); io.unobserve(e.target); } });
    }, { rootMargin: "0px 0px -8% 0px" });
    [].forEach.call(els, function (el) { io.observe(el); });
  }

  // ---- filters (projects list, library)
  [].forEach.call(document.querySelectorAll("[data-filter-group]"), function (group) {
    var target = document.getElementById(group.getAttribute("data-filter-group"));
    if (!target) return;
    var buttons = [].slice.call(group.querySelectorAll("button[data-filter]"));
    function apply(val) {
      buttons.forEach(function (b) { b.setAttribute("aria-pressed", String(b.getAttribute("data-filter") === val)); });
      [].forEach.call(target.children, function (item) {
        var tags = (item.getAttribute("data-tags") || "").split(" ");
        item.hidden = !(val === "all" || tags.indexOf(val) >= 0);
      });
      try { history.replaceState(null, "", val === "all" ? location.pathname : location.pathname + "#" + val); } catch (e) {}
    }
    buttons.forEach(function (b) { b.addEventListener("click", function () { apply(b.getAttribute("data-filter")); }); });
    var start = decodeURIComponent((location.hash || "").slice(1));
    if (start && buttons.some(function (b) { return b.getAttribute("data-filter") === start; })) apply(start);
  });

  // ---- click-to-play videos: nothing loads from YouTube until the visitor asks
  document.addEventListener("click", function (e) {
    var play = e.target.closest && e.target.closest(".vid-play");
    if (!play) return;
    var frame = play.parentNode;
    var id = frame.getAttribute("data-yt");
    if (!id) return;
    var f = document.createElement("iframe");
    f.src = "https://www.youtube-nocookie.com/embed/" + encodeURIComponent(id) + "?autoplay=1&rel=0&playsinline=1";
    f.title = frame.getAttribute("data-title") || "영상";
    f.allow = "accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture; fullscreen";
    f.allowFullscreen = true;
    frame.innerHTML = "";
    frame.appendChild(f);
  });

  // ---- latest posts from the Blogger feed (JSONP; static links stay if it fails)
  function loadFeed(list, feed, keepOnEmpty) {
    var max = Number(list.getAttribute("data-max") || 3);
    var cb = "__sgFeed" + Date.now() + Math.floor(Math.random() * 1e4);
    var s = document.createElement("script");
    var timer = setTimeout(fail, 8000);
    function fail() { cleanup(); if (!keepOnEmpty) list.innerHTML = '<p class="empty">글을 불러오지 못했습니다. <a href="https://songgollab.blogspot.com">블로그에서 보기 ↗</a></p>'; }
    function cleanup() { clearTimeout(timer); try { delete window[cb]; } catch (e) { window[cb] = undefined; } if (s.parentNode) s.parentNode.removeChild(s); }
    window[cb] = function (data) {
      cleanup();
      var entries = (data && data.feed && data.feed.entry) || [];
      if (!entries.length) {
        if (!keepOnEmpty) list.innerHTML = '<p class="empty">이 프로젝트 라벨이 붙은 글이 아직 없습니다.</p>';
        return;
      }
      var frag = document.createDocumentFragment();
      entries.slice(0, max).forEach(function (en) {
        var link = (en.link || []).filter(function (l) { return l.rel === "alternate"; })[0];
        if (!link) return;
        var a = document.createElement("a"); a.href = link.href;
        var small = document.createElement("small");
        var d = new Date(en.published && en.published.$t);
        small.textContent = "송골랩 블로그" + (isNaN(d) ? "" : " · " + d.getFullYear() + "." + String(d.getMonth() + 1).padStart(2, "0") + "." + String(d.getDate()).padStart(2, "0"));
        var span = document.createElement("span"); span.textContent = (en.title && en.title.$t) || "제목 없음";
        a.appendChild(small); a.appendChild(span); frag.appendChild(a);
      });
      if (frag.childNodes.length) { list.innerHTML = ""; list.appendChild(frag); }
    };
    s.src = feed + (feed.indexOf("?") >= 0 ? "&" : "?") + "callback=" + cb;
    s.async = true; s.onerror = fail;
    document.head.appendChild(s);
  }
  [].forEach.call(document.querySelectorAll("[data-blogger-feed]"), function (list) { loadFeed(list, list.getAttribute("data-blogger-feed"), true); });

  // ---- 작업 일지: filter by project label (Blogger label feed)
  var lf = document.querySelector("[data-log-filter]");
  var target = document.querySelector(".page [data-blogger-feed]");
  if (lf && target) {
    var base = target.getAttribute("data-blogger-feed").replace(/\/-\/[^?]+/, "");
    [].forEach.call(lf.querySelectorAll("button"), function (b) {
      b.addEventListener("click", function () {
        [].forEach.call(lf.querySelectorAll("button"), function (x) { x.setAttribute("aria-pressed", String(x === b)); });
        var label = b.getAttribute("data-log-label");
        var feed = label ? base.replace("/feeds/posts/default", "/feeds/posts/default/-/" + encodeURIComponent(label)) : base;
        target.innerHTML = '<p class="empty">불러오는 중…</p>';
        loadFeed(target, feed, false);
      });
    });
  }
})();
