// 송골랩 홈페이지 공통 스크립트
(function () {
  var top = document.getElementById('top');
  if (top) addEventListener('scroll', function () { top.classList.toggle('scrolled', scrollY > 8); }, { passive: true });

  // 영상 카드: 누르면 그 자리에서 재생
  document.querySelectorAll('.vcard[data-yt]').forEach(function (b) {
    b.addEventListener('click', function () {
      if (b.classList.contains('playing')) return;
      var th = b.querySelector('.th');
      th.innerHTML = '<iframe src="https://www.youtube-nocookie.com/embed/' + b.dataset.yt + '?autoplay=1" title="영상" allow="autoplay; encrypted-media; picture-in-picture" allowfullscreen></iframe>';
      b.classList.add('playing');
    });
  });

  // 문의 폼 → 이메일 앱으로
  var f = document.getElementById('cform');
  if (f) {
    var q = new URLSearchParams(location.search).get('topic');
    if (q) { var s = f.topic; for (var i = 0; i < s.options.length; i++) if (s.options[i].text.indexOf(q) > -1) s.selectedIndex = i; }
    f.addEventListener('submit', function (e) {
      e.preventDefault();
      var err = document.getElementById('cerr');
      if (!f.name.value.trim() || !f.contact.value.trim() || !f.body.value.trim()) { err.textContent = '이름, 연락처, 내용을 모두 적어 주세요.'; return; }
      if (!f.agree.checked) { err.textContent = '개인정보 수집·이용에 동의해 주세요.'; return; }
      err.textContent = '';
      var subject = '[송골랩 문의] ' + f.topic.value + ' - ' + f.name.value.trim();
      var body = '이름: ' + f.name.value.trim() + '\n연락처: ' + f.contact.value.trim() + '\n분야: ' + f.topic.value + '\n\n' + f.body.value.trim() + '\n\n(songgollab.co.kr 문의 페이지에서 보냄)';
      location.href = 'mailto:songgollab@gmail.com?subject=' + encodeURIComponent(subject) + '&body=' + encodeURIComponent(body);
    });
  }
})();
