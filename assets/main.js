(function () {
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var doc = document.documentElement;

  /* header state + scroll progress + timeline fill */
  var header = document.querySelector('.site-header');
  var bar = document.querySelector('.progress');
  var tl = document.querySelector('.timeline');
  var steps = tl ? tl.querySelectorAll('.tstep') : [];
  function onScroll() {
    var y = window.scrollY, h = doc.scrollHeight - innerHeight;
    header.classList.toggle('scrolled', y > 20);
    if (bar) bar.style.transform = 'scaleX(' + (h > 0 ? y / h : 0) + ')';
    if (tl) {
      var r = tl.getBoundingClientRect();
      var p = Math.min(1, Math.max(0, (innerHeight * 0.75 - r.top) / (r.height + innerHeight * 0.25)));
      tl.style.setProperty('--p', p.toFixed(3));
      steps.forEach(function (s, i) { s.classList.toggle('lit', p >= (i + 0.2) / steps.length); });
    }
  }
  addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  /* mobile menu */
  var btn = document.querySelector('.menu-btn'), links = document.getElementById('nav-links');
  btn.addEventListener('click', function () {
    var o = links.classList.toggle('open');
    btn.setAttribute('aria-expanded', o);
  });
  links.addEventListener('click', function (e) {
    if (e.target.closest('a')) { links.classList.remove('open'); btn.setAttribute('aria-expanded', false); }
  });

  /* split headings into words for staggered reveal */
  document.querySelectorAll('.split').forEach(function (el) {
    var words = el.textContent.trim().split(/\s+/);
    el.setAttribute('aria-label', el.textContent.trim());
    el.innerHTML = words.map(function (w, i) {
      return '<span class="w" aria-hidden="true" style="--i:' + i + '">' + w + '</span>';
    }).join(' ');
  });

  /* reveal on scroll */
  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (e) {
      if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
    });
  }, { threshold: 0.15, rootMargin: '0px 0px -40px 0px' });
  document.querySelectorAll('[data-reveal], .split').forEach(function (el) { io.observe(el); });

  /* rotating word */
  var rot = document.querySelectorAll('.rotator span');
  if (rot.length && !reduce) {
    var ri = 0;
    setInterval(function () {
      rot[ri].classList.remove('on');
      ri = (ri + 1) % rot.length;
      rot[ri].classList.add('on');
    }, 2600);
  }

  /* spotlight cards */
  document.querySelectorAll('.card').forEach(function (c) {
    c.addEventListener('pointermove', function (e) {
      var r = c.getBoundingClientRect();
      c.style.setProperty('--mx', (e.clientX - r.left) + 'px');
      c.style.setProperty('--my', (e.clientY - r.top) + 'px');
    });
  });

  /* AI console demo */
  var msgs = document.querySelectorAll('.console .msg');
  var typing = document.querySelector('.console .typing-row');
  function playConsole() {
    if (reduce) { msgs.forEach(function (m) { m.classList.add('show'); }); if (typing) typing.style.display = 'none'; return; }
    var t = 300;
    msgs.forEach(function (m, i) {
      var isAi = m.classList.contains('ai');
      if (isAi && typing) {
        setTimeout(function () { typing.style.display = 'flex'; }, t);
        t += 1300;
      }
      setTimeout(function () { if (isAi && typing) typing.style.display = 'none'; m.classList.add('show'); }, t);
      t += isAi ? 1600 : 900;
    });
    setTimeout(function () {
      msgs.forEach(function (m) { m.classList.remove('show'); });
      setTimeout(playConsole, 700);
    }, t + 5000);
  }
  var con = document.querySelector('.console');
  if (con) {
    var cio = new IntersectionObserver(function (e) {
      if (e[0].isIntersecting) { playConsole(); cio.disconnect(); }
    }, { threshold: 0.3 });
    cio.observe(con);
  }

  /* neural network canvas */
  var cv = document.getElementById('neural');
  if (cv && cv.getContext) {
    var ctx = cv.getContext('2d'), pts = [], W, H, dpr, mouse = { x: -1e4, y: -1e4 }, running = true, raf;
    var cols = ['0,217,122', '79,208,245', '139,123,255'];
    function size() {
      dpr = Math.min(window.devicePixelRatio || 1, 2);
      W = cv.clientWidth; H = cv.clientHeight;
      cv.width = W * dpr; cv.height = H * dpr;
      ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
      var n = Math.round(Math.min(90, W * H / 14000));
      pts = [];
      for (var i = 0; i < n; i++) {
        pts.push({ x: Math.random() * W, y: Math.random() * H, vx: (Math.random() - .5) * .35, vy: (Math.random() - .5) * .35, c: cols[i % 3], r: Math.random() * 1.6 + .8 });
      }
    }
    function frame() {
      ctx.clearRect(0, 0, W, H);
      var D = 140;
      for (var i = 0; i < pts.length; i++) {
        var p = pts[i];
        if (!reduce) {
          p.x += p.vx; p.y += p.vy;
          if (p.x < 0 || p.x > W) p.vx *= -1;
          if (p.y < 0 || p.y > H) p.vy *= -1;
          var mx = mouse.x - p.x, my = mouse.y - p.y, md = Math.hypot(mx, my);
          if (md < 180) { p.x += mx * .006; p.y += my * .006; }
        }
        for (var j = i + 1; j < pts.length; j++) {
          var q = pts[j], d = Math.hypot(p.x - q.x, p.y - q.y);
          if (d < D) {
            ctx.strokeStyle = 'rgba(' + p.c + ',' + (1 - d / D) * .35 + ')';
            ctx.lineWidth = 1;
            ctx.beginPath(); ctx.moveTo(p.x, p.y); ctx.lineTo(q.x, q.y); ctx.stroke();
          }
        }
        ctx.fillStyle = 'rgba(' + p.c + ',.9)';
        ctx.beginPath(); ctx.arc(p.x, p.y, p.r, 0, 6.283); ctx.fill();
      }
      if (running && !reduce) raf = requestAnimationFrame(frame);
    }
    size(); frame();
    var rt; addEventListener('resize', function () { clearTimeout(rt); rt = setTimeout(function () { size(); if (reduce) frame(); }, 200); });
    cv.parentElement.addEventListener('pointermove', function (e) {
      var r = cv.getBoundingClientRect(); mouse.x = e.clientX - r.left; mouse.y = e.clientY - r.top;
    });
    cv.parentElement.addEventListener('pointerleave', function () { mouse.x = mouse.y = -1e4; });
    new IntersectionObserver(function (e) {
      var vis = e[0].isIntersecting;
      if (vis && !running) { running = true; if (!reduce) frame(); }
      if (!vis) { running = false; cancelAnimationFrame(raf); }
    }).observe(cv);
  }

  /* theme toggle: follows the device until the visitor picks one */
  var tb = document.querySelector('.theme-btn');
  if (tb) tb.addEventListener('click', function () {
    var cur = doc.getAttribute('data-theme') || (matchMedia('(prefers-color-scheme: light)').matches ? 'light' : 'dark');
    var next = cur === 'light' ? 'dark' : 'light';
    doc.setAttribute('data-theme', next);
    try { localStorage.setItem('mg-theme', next); } catch (e) {}
  });

  /* cookie consent (Google Consent Mode v2) */
  (function () {
    var stored = null;
    try { stored = localStorage.getItem('mg-consent'); } catch (e) {}
    if (stored === 'granted' || stored === 'denied') return;
    var T = {
      ar: ['نستخدم ملفات تعريف الارتباط لقياس زيارات الموقع وتحسين تجربتك. هل توافق؟', 'موافق', 'رفض'],
      en: ['We use cookies to measure site traffic and improve your experience. Do you accept?', 'Accept', 'Decline'],
      nl: ['We gebruiken cookies om websiteverkeer te meten en je ervaring te verbeteren. Ga je akkoord?', 'Accepteren', 'Weigeren']
    };
    var t = T[doc.lang] || T.en;
    var box = document.createElement('div');
    box.className = 'consent';
    box.setAttribute('role', 'dialog');
    box.setAttribute('aria-live', 'polite');
    box.innerHTML = '<p></p><div class="consent-actions"><button type="button" class="consent-no"></button><button type="button" class="consent-yes"></button></div>';
    box.querySelector('p').textContent = t[0];
    box.querySelector('.consent-yes').textContent = t[1];
    box.querySelector('.consent-no').textContent = t[2];
    function choose(v) {
      try { localStorage.setItem('mg-consent', v); } catch (e) {}
      if (v === 'granted' && typeof window.gtag === 'function') {
        window.gtag('consent', 'update', { ad_storage: 'granted', ad_user_data: 'granted', ad_personalization: 'granted', analytics_storage: 'granted' });
        (window.dataLayer = window.dataLayer || []).push({ event: 'consent_granted' });
      }
      box.remove();
    }
    box.querySelector('.consent-yes').addEventListener('click', function () { choose('granted'); });
    box.querySelector('.consent-no').addEventListener('click', function () { choose('denied'); });
    document.body.appendChild(box);
  })();

  var y = document.getElementById('y'); if (y) y.textContent = new Date().getFullYear();
})();
