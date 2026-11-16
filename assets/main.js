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

  /* language dropdown: close on outside click / Escape */
  var dd = document.querySelector('.lang-dd');
  if (dd) {
    document.addEventListener('click', function (e) { if (dd.open && !dd.contains(e.target)) dd.open = false; });
    dd.addEventListener('keydown', function (e) { if (e.key === 'Escape') { dd.open = false; dd.querySelector('summary').focus(); } });
  }

  /* consultation request dialog */
  (function () {
    // Web3Forms access key (free, sends submissions to info@moregrowth.co). Empty = fall back to a pre-filled email.
    var FORM_KEY = '00d75d06-4b46-4b0f-b273-9262a13f2475';
    var links = document.querySelectorAll('[data-consult]');
    if (!links.length || typeof HTMLDialogElement !== 'function') return;
    var L = {
      ar: { title: 'احجز استشارة مجانية', sub: 'جلسة 30 دقيقة مع فريقنا. نرد خلال يوم عمل واحد.', name: 'الاسم الكامل', email: 'البريد الإلكتروني', company: 'اسم الشركة أو المؤسسة', phone: 'رقم الهاتف أو واتساب', ph: '+968 …', opt: '(اختياري)', interest: 'بماذا نساعدك؟', ai: 'الذكاء الاصطناعي', mk: 'التسويق الرقمي', both: 'الاثنان', msg: 'أخبرنا باختصار عن هدفك', send: 'أرسل الطلب', sending: 'جارٍ الإرسال…', okT: 'تم استلام طلبك ✓', okP: 'شكرًا لك! سنتواصل معك على بريدك خلال يوم عمل واحد لتحديد موعد الجلسة.', close: 'إغلاق', err: 'تعذر الإرسال. حاول مرة أخرى أو راسلنا على info@moregrowth.co', req: 'يرجى تعبئة الحقول المطلوبة', subject: 'طلب استشارة من الموقع', privacy: 'نستخدم بياناتك فقط للتواصل معك بخصوص طلبك.' },
      en: { title: 'Book a free consultation', sub: 'A 30-minute session with our team. We reply within one business day.', name: 'Full name', email: 'Work email', company: 'Company or organization', phone: 'Phone or WhatsApp', ph: '+968 …', opt: '(optional)', interest: 'What can we help with?', ai: 'AI transformation', mk: 'Digital marketing', both: 'Both', msg: 'Tell us briefly about your goal', send: 'Send request', sending: 'Sending…', okT: 'Request received ✓', okP: 'Thank you! We will email you within one business day to schedule your session.', close: 'Close', err: 'Could not send. Please try again or email info@moregrowth.co', req: 'Please fill in the required fields', subject: 'Consultation request from the website', privacy: 'We only use your details to reply to your request.' },
      nl: { title: 'Plan een gratis adviesgesprek', sub: 'Een sessie van 30 minuten met ons team. We reageren binnen één werkdag.', name: 'Volledige naam', email: 'Zakelijk e-mailadres', company: 'Bedrijf of organisatie', phone: 'Telefoon of WhatsApp', ph: '+31 …', opt: '(optioneel)', interest: 'Waarmee kunnen we helpen?', ai: 'AI-transformatie', mk: 'Digitale marketing', both: 'Beide', msg: 'Vertel kort over je doel', send: 'Verstuur aanvraag', sending: 'Versturen…', okT: 'Aanvraag ontvangen ✓', okP: 'Bedankt! We mailen je binnen één werkdag om de sessie in te plannen.', close: 'Sluiten', err: 'Versturen mislukt. Probeer opnieuw of mail naar info@moregrowth.co', req: 'Vul de verplichte velden in', subject: 'Adviesaanvraag via de website', privacy: 'We gebruiken je gegevens alleen om op je aanvraag te reageren.' }
    };
    var t = L[doc.lang] || L.en;
    var d = document.createElement('dialog');
    d.className = 'consult';
    d.setAttribute('aria-labelledby', 'consult-title');
    d.innerHTML =
      '<button type="button" class="c-x" aria-label="' + t.close + '">&times;</button>' +
      '<form class="c-form" novalidate>' +
        '<h2 id="consult-title">' + t.title + '</h2><p class="c-sub">' + t.sub + '</p>' +
        '<fieldset class="c-interest"><legend>' + t.interest + '</legend>' +
          ['ai', 'mk', 'both'].map(function (k, i) { return '<label><input type="radio" name="interest" value="' + k + '"' + (i === 2 ? ' checked' : '') + '><span>' + t[k] + '</span></label>'; }).join('') +
        '</fieldset>' +
        '<div class="c-grid">' +
          '<label class="c-f"><span>' + t.name + ' *</span><input name="name" autocomplete="name" required></label>' +
          '<label class="c-f"><span>' + t.email + ' *</span><input name="email" type="email" autocomplete="email" inputmode="email" dir="ltr" required></label>' +
          '<label class="c-f"><span>' + t.company + ' *</span><input name="company" autocomplete="organization" required></label>' +
          '<label class="c-f"><span>' + t.phone + ' <em>' + t.opt + '</em></span><input name="phone" type="tel" autocomplete="tel" inputmode="tel" dir="ltr" placeholder="' + t.ph + '"></label>' +
        '</div>' +
        '<label class="c-f"><span>' + t.msg + ' <em>' + t.opt + '</em></span><textarea name="message" rows="3"></textarea></label>' +
        '<input type="checkbox" name="botcheck" class="c-hp" tabindex="-1" autocomplete="off" aria-hidden="true">' +
        '<p class="c-err" role="alert" hidden></p>' +
        '<button type="submit" class="btn btn-primary c-send">' + t.send + '</button>' +
        '<p class="c-priv">' + t.privacy + '</p>' +
      '</form>' +
      '<div class="c-ok" hidden><div class="c-ok-ic" aria-hidden="true">✓</div><h2>' + t.okT + '</h2><p>' + t.okP + '</p><button type="button" class="btn btn-ghost c-done">' + t.close + '</button></div>';
    document.body.appendChild(d);
    var form = d.querySelector('form'), ok = d.querySelector('.c-ok'), err = d.querySelector('.c-err'), send = d.querySelector('.c-send');
    function open(interest) {
      form.hidden = false; ok.hidden = true; err.hidden = true;
      var r = form.querySelector('input[value="' + (interest || 'both') + '"]'); if (r) r.checked = true;
      d.showModal(); doc.classList.add('modal-open');
      setTimeout(function () { form.name.focus(); }, 50);
      (window.dataLayer = window.dataLayer || []).push({ event: 'consult_open', interest: interest || 'both' });
    }
    function close() { d.close(); }
    d.addEventListener('close', function () { doc.classList.remove('modal-open'); });
    links.forEach(function (a) { a.addEventListener('click', function (e) { e.preventDefault(); open(a.getAttribute('data-consult')); }); });
    d.querySelector('.c-x').addEventListener('click', close);
    d.querySelector('.c-done').addEventListener('click', close);
    d.addEventListener('click', function (e) { if (e.target === d) close(); });
    function done(interest) {
      form.reset(); form.hidden = true; ok.hidden = false; ok.querySelector('.c-done').focus();
      (window.dataLayer = window.dataLayer || []).push({ event: 'generate_lead', interest: interest });
    }
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var bad = null;
      ['name', 'email', 'company'].forEach(function (n) { var f = form[n]; var v = f.value.trim(); var inv = !v || (n === 'email' && !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(v)); f.setAttribute('aria-invalid', inv ? 'true' : 'false'); if (inv && !bad) bad = f; });
      if (bad) { err.textContent = t.req; err.hidden = false; bad.focus(); return; }
      if (form.botcheck.checked) return;
      err.hidden = true;
      var data = { name: form.name.value.trim(), email: form.email.value.trim(), company: form.company.value.trim(), phone: form.phone.value.trim(), interest: t[form.interest.value], message: form.message.value.trim(), page: location.href };
      if (!FORM_KEY) {
        var body = Object.keys(data).map(function (k) { return k + ': ' + data[k]; }).join('\n');
        location.href = 'mailto:info@moregrowth.co?subject=' + encodeURIComponent(t.subject + ': ' + data.company) + '&body=' + encodeURIComponent(body);
        done(form.interest.value);
        return;
      }
      send.disabled = true; send.textContent = t.sending;
      var payload = Object.assign({ access_key: FORM_KEY, subject: t.subject + ': ' + data.company, from_name: 'moregrowth.co', replyto: data.email, botcheck: false }, data);
      var interest = form.interest.value;
      fetch('https://api.web3forms.com/submit', { method: 'POST', headers: { 'Content-Type': 'application/json', Accept: 'application/json' }, body: JSON.stringify(payload) })
        .then(function (r) { return r.json(); })
        .then(function (j) { if (j && j.success) done(interest); else throw 0; })
        .catch(function () { err.textContent = t.err; err.hidden = false; })
        .then(function () { send.disabled = false; send.textContent = t.send; });
    });
  })();

  /* cookie consent (Google Consent Mode v2) */
  (function () {
    var stored = null;
    try { stored = localStorage.getItem('mg-consent'); } catch (e) {}
    var reset = document.querySelector('[data-cookie-reset]');
    if (reset) reset.addEventListener('click', function () {
      try { localStorage.removeItem('mg-consent'); } catch (e) {}
      if (stored === 'granted' && typeof window.gtag === 'function') {
        window.gtag('consent', 'update', { ad_storage: 'denied', ad_user_data: 'denied', ad_personalization: 'denied', analytics_storage: 'denied' });
      }
      stored = null;
      if (!document.querySelector('.consent')) show();
    });
    if (stored === 'granted' || stored === 'denied') return;
    show();
    function show() {
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
    }
  })();

  /* service tracks: pointer spotlight + gentle tilt */
  if (!matchMedia('(prefers-reduced-motion: reduce)').matches && matchMedia('(hover: hover)').matches) {
    document.querySelectorAll('[data-tilt]').forEach(function (p) {
      p.addEventListener('pointermove', function (e) {
        var r = p.getBoundingClientRect(), x = (e.clientX - r.left) / r.width, yy = (e.clientY - r.top) / r.height;
        p.style.setProperty('--mx', (x * 100) + '%'); p.style.setProperty('--my', (yy * 100) + '%');
        p.style.setProperty('--ry', ((x - .5) * 5) + 'deg'); p.style.setProperty('--rx', ((.5 - yy) * 4) + 'deg');
      });
      p.addEventListener('pointerleave', function () { p.style.setProperty('--rx', '0deg'); p.style.setProperty('--ry', '0deg'); });
    });
  }

  var y = document.getElementById('y'); if (y) y.textContent = new Date().getFullYear();
})();
