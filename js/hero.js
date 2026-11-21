/* SONGGOL LAB hero bootstrap (no three.js here).
 * - Scene tabs switch copy + poster even without 3D, and tell the 3D scene via a "hero:scene" event.
 * - Three.js (js/scene.min.js) + GLB load only when every desktop condition passes, so phones,
 *   reduced-motion and no-WebGL visitors never download them.
 * - Section reveal on scroll.
 *
 * Local test switches: ?3d=0 poster only, ?3d=1 force a 3D attempt, ?quality=low|high (locks tier),
 *   ?minfps=0 keep 3D even when very slow, ?scene=home start scene,
 *   ?capture=car|home poster-capture mode (no UI, final framing).
 */
(function () {
  "use strict";
  var hero = document.getElementById("hero");
  var q = new URLSearchParams(location.search);
  var modeEl = document.getElementById("hud-mode");
  var modelEl = document.getElementById("hud-model");
  var clockEl = document.getElementById("hud-clock");
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var capture = q.get("capture");
  var SCENES = ["car", "home"];
  var MODEL_NAME = { car: "VEHICLE", home: "VIRTUAL HOUSE" };

  function setState(state, reason) {
    hero.dataset.heroState = state;
    if (reason) hero.dataset.heroReason = reason; else delete hero.dataset.heroReason;
    if (modeEl) modeEl.textContent = state === "3d" ? "REALTIME" : state === "loading" ? "LOADING" : "POSTER";
    window.__hero = Object.assign(window.__hero || {}, { state: state, reason: reason || null });
  }

  // ------------------------------------------------------------ scenes (copy + poster + 3D)
  var current = SCENES.indexOf(q.get("scene") || capture) >= 0 ? (q.get("scene") || capture) : "car";
  var tabs = [].slice.call(hero.querySelectorAll(".scene-tab"));
  function show(name, fromUser) {
    current = name;
    hero.dataset.scene = name;
    hero.setAttribute("aria-labelledby", "hero-title-" + name);
    [].forEach.call(hero.querySelectorAll(".hero-copy"), function (el) { el.hidden = el.dataset.scene !== name; });
    tabs.forEach(function (t) { t.setAttribute("aria-pressed", String(t.dataset.scene === name)); });
    if (modelEl) modelEl.textContent = MODEL_NAME[name];
    hero.dispatchEvent(new CustomEvent("hero:scene", { detail: name }));
    if (fromUser) stopAuto();
    restartBar();
  }
  tabs.forEach(function (t) { t.addEventListener("click", function () { show(t.dataset.scene, true); }); });

  // auto-advance every 9 s, paused on hover/focus, off for reduced motion or after a manual pick
  var AUTO_MS = 9000, autoTimer = null, autoOn = !reduce && !capture, paused = false;
  function restartBar() {
    hero.classList.remove("is-cycling");
    void hero.offsetWidth;
    if (autoOn) hero.classList.add("is-cycling");
  }
  function scheduleAuto() {
    clearTimeout(autoTimer);
    if (!autoOn || paused) return;
    autoTimer = setTimeout(function () {
      if (!document.hidden) show(SCENES[(SCENES.indexOf(current) + 1) % SCENES.length]);
      scheduleAuto();
    }, AUTO_MS);
  }
  function stopAuto() { autoOn = false; clearTimeout(autoTimer); hero.classList.remove("is-cycling"); }
  hero.addEventListener("pointerenter", function () { paused = true; hero.classList.add("is-paused"); clearTimeout(autoTimer); });
  hero.addEventListener("pointerleave", function () { paused = false; hero.classList.remove("is-paused"); restartBar(); scheduleAuto(); });
  hero.addEventListener("focusin", function () { paused = true; hero.classList.add("is-paused"); clearTimeout(autoTimer); });
  hero.addEventListener("focusout", function () { paused = false; hero.classList.remove("is-paused"); scheduleAuto(); });
  show(current);
  scheduleAuto();

  // decorative clock
  if (clockEl) {
    var tick = function () { clockEl.textContent = new Date().toLocaleTimeString("en-GB", { hour12: false }); };
    tick();
    setInterval(function () { if (!document.hidden) tick(); }, 1000);
  }

  // ------------------------------------------------------------ section reveal
  var revealEls = document.querySelectorAll(".reveal");
  if (reduce || !("IntersectionObserver" in window)) {
    [].forEach.call(revealEls, function (el) { el.classList.add("is-in"); });
  } else {
    var rio = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add("is-in"); rio.unobserve(e.target); } });
    }, { rootMargin: "0px 0px -10% 0px" });
    [].forEach.call(revealEls, function (el) { rio.observe(el); });
  }

  // ------------------------------------------------------------ 3D decision
  function webglOK() {
    try {
      var c = document.createElement("canvas");
      var gl = c.getContext("webgl2", { failIfMajorPerformanceCaveat: !q.get("3d") && !capture });
      if (!gl) return false;
      var lose = gl.getExtension("WEBGL_lose_context");
      if (lose) lose.loseContext();
      return true;
    } catch (e) { return false; }
  }
  function blocked() {
    if (capture) return webglOK() ? null : "no-webgl";
    var force = q.get("3d");
    if (force === "0") return "forced-poster";
    if (reduce) return "reduced-motion";
    if (force !== "1") {
      if (!window.matchMedia("(min-width: 900px) and (hover: hover) and (pointer: fine)").matches) return "small-or-touch";
      var conn = navigator.connection;
      if (conn && (conn.saveData || /(^|-)2g$/.test(conn.effectiveType || ""))) return "save-data";
    }
    if (!webglOK()) return "no-webgl";
    return null;
  }

  if (capture) document.documentElement.classList.add("is-capture");
  var why = blocked();
  if (why) { setState("poster", why); return; }

  setState("loading");
  var start = function () {
    import("./scene.min.js")
      .then(function (m) {
        return m.mountHero(hero, {
          glb: q.get("glb") || "assets/showroom.glb",
          quality: q.get("quality") || "auto",
          minFps: q.has("minfps") ? Number(q.get("minfps")) : 12,
          initial: current,
          capture: capture,
          onState: setState
        });
      })
      .catch(function (err) {
        console.warn("[hero] 3D unavailable, poster kept:", err && err.message);
        setState("poster", "scene-error");
      });
  };
  if (capture) start();
  else if ("requestIdleCallback" in window) requestIdleCallback(start, { timeout: 1200 });
  else setTimeout(start, 300);
})();
