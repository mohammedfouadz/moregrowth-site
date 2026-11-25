"""MoreGrowth site v2: modern AI-era design with motion. Arabic at /, English at /en/."""
import os, sys
from urllib.parse import quote
sys.path.insert(0, os.path.dirname(__file__))
from icons import ICONS as I
from gen import AR, EN, SITE, PARTNER, EMAIL, SOC
from nl import NL
import re
from privacy import PRIVACY, UPDATED

OUT = sys.argv[1]

LINE = {
 "roadmap": '<path d="M9 4 3 6v14l6-2 6 2 6-2V4l-6 2-6-2Z"/><path d="M9 4v14M15 6v14"/>',
 "flow": '<rect x="3" y="3" width="7" height="7" rx="2"/><rect x="14" y="14" width="7" height="7" rx="2"/><path d="M10 6.5h4a3 3 0 0 1 3 3V14"/>',
 "chat": '<path d="M21 12a8 8 0 0 1-11.6 7.1L4 20l1-4.6A8 8 0 1 1 21 12Z"/><path d="M8.5 12h.01M12 12h.01M15.5 12h.01"/>',
 "spark": '<path d="M12 3l1.8 5.2L19 10l-5.2 1.8L12 17l-1.8-5.2L5 10l5.2-1.8L12 3Z"/><path d="M19 16l.7 2.3L22 19l-2.3.7L19 22l-.7-2.3L16 19l2.3-.7L19 16Z"/>',
 "learn": '<path d="M2 9l10-5 10 5-10 5L2 9Z"/><path d="M6 11v5c3 2.5 9 2.5 12 0v-5"/>',
 "shield": '<path d="M12 3l8 3v6c0 4.5-3.4 8.3-8 9-4.6-.7-8-4.5-8-9V6l8-3Z"/><path d="m9 12 2 2 4-4"/>',
}
AI_ICONS = ["roadmap", "flow", "chat", "spark", "learn", "shield"]
AI_SKIP = 3  # "AI-powered marketing" lives in the marketing track
LINE.update({
 "ads": '<circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/><path d="M8 11h6M11 8v6"/>',
 "mega": '<path d="M3 11v2a1 1 0 0 0 1 1h2l5 4V6L6 10H4a1 1 0 0 0-1 1Z"/><path d="M15 9a4 4 0 0 1 0 6M18 6a8 8 0 0 1 0 12"/>',
 "seo": '<path d="M3 20h18"/><path d="M6 16v-4M11 16V8M16 16v-6"/><path d="m5 9 5-4 4 3 5-4"/>',
 "pen": '<path d="M4 20h4L19 9a2.8 2.8 0 0 0-4-4L4 16v4Z"/><path d="m13.5 6.5 4 4"/>',
 "cal": '<rect x="3" y="5" width="18" height="16" rx="3"/><path d="M3 10h18M8 3v4M16 3v4"/><path d="m9 15 2 2 4-4"/>',
 "compass": '<circle cx="12" cy="12" r="9"/><path d="m15.5 8.5-2 5-5 2 2-5 5-2Z"/>',
})
MK_ICONS = ["ads", "mega", "seo", "pen", "cal", "compass"]
ARROW = '<svg class="arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'
CLIENTS = [("unrwa", "UNRWA"), ("jawwal", "Jawwal"), ("lucidya", "Lucidya"), ("jahez", "Jahez"), ("osarh", "OSARH"), ("ucasti", "UCAS Technology Incubator"), ("gsg", "Gaza Sky Geeks"), ("bti", "Business & Technology Incubator"), ("necklace", "Necklace"), ("gulf-co", "The Gulf Co."),
           ("b2bmerx", "B2Bmerx"), ("gulf-store", "Gulf Store"), ("one-studio", "One Studio")]

AR.update(
    t1="المسار الأول", t2="المسار الثاني", tk_start="ابدأ من هنا", tk_partner="شريك جوجل", tk_meet="نقطة الالتقاء", tk_ai="ذكاء اصطناعي", tk_mk="تسويق",
    t_ai_cta="اطلب تقييم الجاهزية", t_mk_cta="خطّط حملتك القادمة",
    t_note="المساران يعملان معًا: الذكاء الاصطناعي يجعل تسويقك أذكى، وبيانات التسويق تجعل الذكاء الاصطناعي أكثر فائدة.",
    pill_new="جديد", pill="خدمات التحول للذكاء الاصطناعي للمؤسسات",
    h1_a="نُعيد تشكيل", h1_b="بقوة", h1_grad="الذكاء الاصطناعي",
    rot=["التسويق", "المبيعات", "العمليات", "خدمة العملاء"],
    con_title="مساعد مورجروث الذكي", con_live="متصل",
    con=[("user", "ما الحملات التي تستنزف ميزانيتنا هذا الشهر؟"),
         ("ai", "حللت 4 حملات نشطة. حملة البحث العامة تستهلك 38% من الميزانية بعائد منخفض. أقترح إعادة التوزيع:"),
         ("user", "ممتاز، جهّز 3 إعلانات جديدة بالعربية"),
         ("ai", "تم ✓ كتبت 3 نسخ إعلانية وأرسلت مسودة التقرير للفريق للمراجعة.")],
    con_bars=[("البحث: العلامة", 82), ("إعادة الاستهداف", 64), ("التسوق", 47)],
    con_note="مثال توضيحي لمساعد ذكي يمكن بناؤه لمؤسستك",
    clients_p="شركات ومؤسسات عملنا معها",
    ai_flow_h="من البيانات إلى القرار، تلقائياً",
    flow=[("بيانات من أنظمتك وحملاتك", "متصل"), ("وكيل ذكي يحلل ويقترح", "ذكاء اصطناعي"), ("تقرير وإجراء بموافقة فريقك", "مؤتمت")],
    mk_more="جميع الحملات تُدار بمعايير شريك جوجل المعتمد",
    why_big=["G", "↗", "ع"],
    badge_bi="فريق يعمل بالعربية والإنجليزية والهولندية",
    theme_label="تبديل الوضع الفاتح والداكن", lang_label="اللغة",
)
EN.update(
    t1="Track 01", t2="Track 02", tk_start="Start here", tk_partner="Google Partner", tk_meet="Where they meet", tk_ai="AI", tk_mk="Marketing",
    t_ai_cta="Get an AI readiness check", t_mk_cta="Plan your next campaign",
    t_note="The two tracks work together: AI makes your marketing smarter, and marketing data makes AI more useful.",
    pill_new="New", pill="Enterprise AI transformation services",
    h1_a="We reshape your", h1_b="with", h1_grad="AI",
    rot=["marketing", "sales", "operations", "customer service"],
    con_title="MoreGrowth AI Assistant", con_live="Online",
    con=[("user", "Which campaigns are draining our budget this month?"),
         ("ai", "I analyzed 4 active campaigns. Generic Search uses 38% of spend at a low return. Suggested reallocation:"),
         ("user", "Great, draft 3 new Arabic ads"),
         ("ai", "Done ✓ 3 ad variants written and a draft report sent to your team for review.")],
    con_bars=[("Brand search", 82), ("Remarketing", 64), ("Shopping", 47)],
    con_note="Illustrative example of an assistant we can build for you",
    clients_p="Companies and organizations we have worked with",
    ai_flow_h="From data to decision, automatically",
    flow=[("Data from your systems & campaigns", "Connected"), ("AI agent analyzes and recommends", "AI"), ("Report & action, approved by your team", "Automated")],
    mk_more="All campaigns run to certified Google Partner standards",
    why_big=["G", "↗", "Aa"],
    badge_bi="Multilingual team: Arabic, English & Dutch",
    theme_label="Toggle light and dark mode", lang_label="Language",
)
NL.update(theme_label="Schakel tussen licht en donker", lang_label="Taal",
    t1="Spoor 01", t2="Spoor 02", tk_start="Begin hier", tk_partner="Google Partner", tk_meet="Waar ze samenkomen", tk_ai="AI", tk_mk="Marketing",
    t_ai_cta="Vraag een AI-readiness check aan", t_mk_cta="Plan je volgende campagne",
    t_note="De twee sporen versterken elkaar: AI maakt je marketing slimmer, en marketingdata maakt AI waardevoller.")
LANGS = [("ar", "/", "عربي", "العربية"), ("en", "/en/", "EN", "English"), ("nl", "/nl/", "NL", "Nederlands")]
SUN = '<svg class="i-sun" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg>'
MOON = '<svg class="i-moon" viewBox="0 0 24 24" aria-hidden="true"><path d="M21 12.8A9 9 0 1 1 11.2 3a7 7 0 0 0 9.8 9.8Z"/></svg>'


def svg_line(k):
    return f'<svg viewBox="0 0 24 24" aria-hidden="true">{LINE[k]}</svg>'


def page(t, privacy=False):
    sub = "privacy/" if privacy else ""
    r = t["root"] + ("../" if privacy else "")
    mailto = f"mailto:{EMAIL}?subject={quote(t['mail_subject'])}"
    nav = "".join(f'<li><a href="{(t["path"] + h) if privacy else h}">{l}</a></li>' for h, l in t["nav"])
    rot = "".join(f'<span class="{"on" if i == 0 else ""}">{w}</span>' for i, w in enumerate(t["rot"]))
    # console
    con = []
    for kind, txt in t["con"]:
        if kind == "user":
            con.append(f'<div class="msg user">{txt}</div>')
        else:
            extra = ""
            if "bars" not in "".join(con) and t["con_bars"]:
                extra = '<div class="bars">' + "".join(
                    f'<div class="bar"><span>{n}</span><div><i style="--w:{v}%"></i></div><span>{v}%</span></div>' for n, v in t["con_bars"]) + "</div>"
            con.append(f'<div class="msg ai"><small>{t["con_title"]}</small>{txt}{extra}</div>')
    con.insert(0, "")
    con_html = "".join(con) + '<div class="msg ai typing-row" style="display:none;opacity:1;transform:none;width:max-content"><span class="typing"><i></i><i></i><i></i></span></div>'
    # clients marquee (duplicated for seamless loop)
    tiles = "".join(f'<div class="logo-tile"><img src="{r}assets/clients/{f}.png" alt="{n}" loading="lazy" height="56" draggable="false"></div>' for f, n in CLIENTS)
    # two service tracks
    def track_items(items, icons, kind, skip=None):
        out, n = [], 0
        for i, (a, b) in enumerate(items):
            if i == skip:
                continue
            feat = kind == "ai" and n == 0
            badge = f'<span class="tk-badge">{t["tk_start"]}</span>' if feat else (f'<span class="tk-badge">{t["tk_partner"]}</span>' if kind == "mk" and n == 0 else "")
            out.append(f'<li class="tk-tile{" feat" if feat else ""}" style="--i:{n}"><span class="tk-ic">{svg_line(icons[i])}</span><div><strong>{a}{badge}</strong><span>{b}</span></div></li>')
            n += 1
        return "".join(out)
    ai_items = track_items(t["ai"], AI_ICONS, "ai", AI_SKIP)
    mk_items = track_items(t["mk"], MK_ICONS, "mk")
    shared = t["ai"][AI_SKIP]
    steps = "".join(f'<div class="tstep" data-reveal style="--d:{i * 0.1:.1f}s"><div class="dot">{i + 1:02d}</div><div><h3>{a}</h3><p>{b}</p></div></div>' for i, (a, b) in enumerate(t["steps"]))
    sectors = "".join(f"<span>{s}</span>" for s in t["sectors"])
    why = "".join(f'<article class="card" data-reveal style="--d:{i * 0.1:.1f}s"><div class="big grad">{t["why_big"][i]}</div><h3>{a}</h3><p>{b}</p></article>' for i, (a, b) in enumerate(t["why"]))
    values = "".join(f'<div data-reveal style="--d:{i * 0.07:.2f}s"><strong>{a}</strong><span>{b}</span></div>' for i, (a, b) in enumerate(t["values"]))
    soc_footer = "".join(f'<a href="{u}" target="_blank" rel="noopener" aria-label="{n}">{I[k]}</a>' for k, n, u in SOC)
    soc_contact = "".join(f'<li><a href="{u}" target="_blank" rel="noopener">{I[k]}<span>{n}</span></a></li>' for k, n, u in SOC[:2])
    url = SITE + t["path"] + sub
    ld = ('{"@context":"https://schema.org","@type":"ProfessionalService","name":"MoreGrowth Digital Solutions",'
          '"alternateName":"مورجروث للحلول الرقمية","url":"' + SITE + '/","email":"' + EMAIL + '",'
          '"logo":"' + SITE + '/assets/favicon.png","areaServed":"Middle East and North Africa",'
          '"sameAs":[' + ",".join(f'"{u}"' for _, _, u in SOC) + f',"{PARTNER}"]' + '}')
    GLOBE = '<svg class="i-globe" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c2.5 2.7 3.8 5.7 3.8 9s-1.3 6.3-3.8 9c-2.5-2.7-3.8-5.7-3.8-9S9.5 5.7 12 3Z"/></svg>'
    CHEV = '<svg class="i-chev" viewBox="0 0 24 24" aria-hidden="true"><path d="m6 9 6 6 6-6"/></svg>'
    cur = next(x for x in LANGS if x[0] == t["lang"])
    items = "".join(f'<li><a href="{p}{sub}" hreflang="{c}" lang="{c}"' + (' aria-current="page"' if c == t["lang"] else "") + f'><span>{full}</span><b>{short}</b></a></li>' for c, p, short, full in LANGS)
    langs = f'<details class="lang-dd"><summary aria-label="{t["lang_label"]}: {cur[3]}">{GLOBE}<span>{cur[2]}</span>{CHEV}</summary><ul>{items}</ul></details>'
    html = f"""<!doctype html>
<html lang="{t['lang']}" dir="{t['dir']}">
<head>
<meta charset="utf-8">
<script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag('consent','default',{{ad_storage:'denied',ad_user_data:'denied',ad_personalization:'denied',analytics_storage:'denied',wait_for_update:500}});try{{if(localStorage.getItem('mg-consent')==='granted')gtag('consent','update',{{ad_storage:'granted',ad_user_data:'granted',ad_personalization:'granted',analytics_storage:'granted'}})}}catch(e){{}}</script>
<!-- Google Tag Manager -->
<script>(function(w,d,s,l,i){{w[l]=w[l]||[];w[l].push({{'gtm.start':new Date().getTime(),event:'gtm.js'}});var f=d.getElementsByTagName(s)[0],j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src='https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);}})(window,document,'script','dataLayer','GTM-PMZVHFF');</script>
<!-- End Google Tag Manager -->
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{t['title']}</title>
<meta name="description" content="{t['desc']}">
<link rel="canonical" href="{url}">
<link rel="alternate" hreflang="ar" href="{SITE}/{sub}">
<link rel="alternate" hreflang="en" href="{SITE}/en/{sub}">
<link rel="alternate" hreflang="nl" href="{SITE}/nl/{sub}">
<link rel="alternate" hreflang="x-default" href="{SITE}/{sub}">
<meta property="og:type" content="website">
<meta property="og:title" content="{t['title']}">
<meta property="og:description" content="{t['desc']}">
<meta property="og:url" content="{url}">
<meta property="og:locale" content="{t['og_locale']}">
<meta property="og:image" content="{SITE}/assets/og.png">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:site" content="@moregrowthco">
<meta name="theme-color" content="#050b1a">
<meta name="color-scheme" content="dark light">
<script>(function(){{try{{var t=localStorage.getItem("mg-theme");if(t==="light"||t==="dark")document.documentElement.setAttribute("data-theme",t)}}catch(e){{}}}})()</script>
<link rel="icon" type="image/png" href="{r}assets/favicon.png">
<link rel="apple-touch-icon" href="{r}assets/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+Arabic:wght@400;500;600;700&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{r}assets/style.css">
<link rel="stylesheet" href="{r}assets/glass.css">
<link rel="stylesheet" href="{r}assets/tracks.css">
<script>document.documentElement.classList.add('js')</script>
<script type="application/ld+json">{ld}</script>
</head>
<body>
<!-- Google Tag Manager (noscript) -->
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-PMZVHFF" height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
<!-- End Google Tag Manager (noscript) -->
<a class="skip" href="#main">{t['skip']}</a>
<div class="progress" aria-hidden="true"></div>
<div class="ambient" aria-hidden="true"><div class="blob b1"></div><div class="blob b2"></div><div class="blob b3"></div><div class="grid"></div></div>

<header class="site-header">
  <div class="wrap">
    <nav class="nav" aria-label="main">
      <a class="brand" href="{t['path']}"><img class="logo-d" src="{r}assets/logo-white.png" alt="MoreGrowth" width="640" height="162"><img class="logo-l" src="{r}assets/logo-navy.png" alt="MoreGrowth" width="640" height="162"></a>
      <button class="menu-btn" aria-expanded="false" aria-controls="nav-links" aria-label="{t['menu']}"><span></span><span></span><span></span></button>
      <ul class="nav-links" id="nav-links">
        {nav}
        <li class="langs-li">{langs}</li>
        <li><button class="theme-btn" type="button" aria-label="{t['theme_label']}" title="{t['theme_label']}">{SUN}{MOON}</button></li>
        <li><a class="nav-cta" href="{mailto}" data-consult>{t['nav_cta']}</a></li>
      </ul>
    </nav>
  </div>
</header>

<main id="main">
<section class="hero">
  <canvas id="neural" aria-hidden="true"></canvas>
  <div class="wrap hero-grid">
    <div>
      <a class="pill" href="#services" data-reveal><b>{t['pill_new']}</b>{t['pill']}</a>
      <h1 data-reveal style="--d:.08s">{t['h1_a']} <span class="rotator grad" aria-live="polite">{rot}</span><br>{t['h1_b']} <span class="grad">{t['h1_grad']}</span></h1>
      <p class="lead" data-reveal style="--d:.16s">{t['lead']}</p>
      <div class="btns" data-reveal style="--d:.24s">
        <a class="btn btn-primary" href="{mailto}" data-consult="ai">{t['btn1']} {ARROW}</a>
        <a class="btn btn-ghost" href="#services">{t['btn2']}</a>
      </div>
      <div class="trust" data-reveal style="--d:.32s">
        <a href="{PARTNER}" target="_blank" rel="noopener">{I['g']}<span>{t['badge_partner']}</span></a>
      </div>
    </div>
    <div class="console" data-reveal="zoom" style="--d:.2s" aria-hidden="true">
      <div class="console-in">
        <div class="console-bar"><i></i><i></i><i></i>&nbsp; {t['con_title']}<span><b class="live"></b>{t['con_live']}</span></div>
        <div class="console-body">{con_html}</div>
        <div class="console-note">{t['con_note']}</div>
      </div>
    </div>
  </div>
  <div class="scroll-cue" aria-hidden="true"></div>
</section>

<div class="clients">
  <p data-reveal>{t['clients_p']}</p>
  <div class="marquee" data-reveal style="--d:.1s">
    <div class="track">{tiles}<span aria-hidden="true" style="display:contents">{tiles.replace('alt="', 'alt="" data-alt="')}</span></div>
  </div>
</div>

<section id="services">
  <div class="wrap">
    <div class="section-head">
      <p class="kicker">{t['svc_k']}</p>
      <h2 class="split">{t['svc_h']}</h2>
      <p data-reveal>{t['svc_p']}</p>
    </div>
    <div class="tk-tracks">
      <article class="tk-panel ai" data-reveal data-tilt>
        <div class="tk-ring" aria-hidden="true"></div><div class="tk-spot" aria-hidden="true"></div>
        <div class="tk-top">
          <div class="tk-orb" aria-hidden="true"><span></span>{svg_line('spark')}</div>
          <div class="tk-meta"><span class="tk-num">{t['t1']}</span><span class="tk-tag">{t['ai_tag']}</span></div>
        </div>
        <h3>{t['ai_h']}</h3>
        <p class="tk-lead">{t['ai_p']}</p>
        <ul class="tk-grid">{ai_items}</ul>
        <a class="tk-cta" href="{mailto}" data-consult="ai">{t['t_ai_cta']}{ARROW}</a>
      </article>
      <div class="tk-bridge" aria-hidden="true">
        <svg class="tk-flow" viewBox="0 0 40 400" preserveAspectRatio="none"><path class="rail" d="M20 0V400"/><path class="pulse up" d="M20 400V0"/><path class="pulse down" d="M20 0V400"/></svg>
        <div class="tk-knot">+</div>
      </div>
      <article class="tk-panel mk" data-reveal data-tilt style="--d:.12s">
        <div class="tk-ring" aria-hidden="true"></div><div class="tk-spot" aria-hidden="true"></div>
        <div class="tk-top">
          <div class="tk-orb" aria-hidden="true"><span></span>{svg_line('seo')}</div>
          <div class="tk-meta"><span class="tk-num">{t['t2']}</span><span class="tk-tag">{t['mk_tag']}</span></div>
        </div>
        <h3>{t['mk_h']}</h3>
        <p class="tk-lead">{t['mk_p']}</p>
        <ul class="tk-grid">{mk_items}</ul>
        <a class="tk-cta" href="{mailto}" data-consult="mk">{t['t_mk_cta']}{ARROW}</a>
      </article>
    </div>
    <div class="tk-meet" data-reveal>
      <div class="tk-chip c-ai"><i></i>{t['tk_ai']}</div>
      <div class="tk-line l1" aria-hidden="true"></div>
      <div class="tk-core"><span class="tk-k">{t['tk_meet']}</span><strong>{shared[0]}</strong><span class="tk-d">{shared[1]}</span></div>
      <div class="tk-line l2" aria-hidden="true"></div>
      <div class="tk-chip c-mk"><i></i>{t['tk_mk']}</div>
    </div>
    <p class="tk-note" data-reveal>{t['t_note']}</p>
  </div>
</section>

<section id="approach">
  <div class="wrap">
    <div class="section-head center">
      <p class="kicker">{t['ap_k']}</p>
      <h2 class="split">{t['ap_h']}</h2>
    </div>
    <div class="timeline"><i class="fill" aria-hidden="true"></i>{steps}</div>
    <div class="sectors" data-reveal aria-label="{t['sectors_h']}">{sectors}</div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="section-head">
      <p class="kicker">{t['why_k']}</p>
      <h2 class="split">{t['why_h']}</h2>
    </div>
    <div class="why">{why}</div>
  </div>
</section>

<section id="about">
  <div class="wrap story">
    <div>
      <p class="kicker">{t['ab_k']}</p>
      <h2 class="split">{t['ab_h']}</h2>
      <p data-reveal>{t['ab_p1']}</p>
      <p data-reveal>{t['ab_p2']}</p>
      <div class="values">{values}</div>
    </div>
    <blockquote class="quote" data-reveal="zoom">{t['quote']}</blockquote>
  </div>
</section>

<section id="contact">
  <div class="wrap">
    <div class="cta" data-reveal="zoom">
      <div class="cta-in">
        <div>
          <h2 class="split">{t['ct_h']}</h2>
          <p>{t['ct_p']}</p>
          <a class="btn btn-primary" href="{mailto}" data-consult>{t['nav_cta']} {ARROW}</a>
        </div>
        <ul class="contact-list">
          <li><a href="{mailto}">{I['mail']}<span class="ltr">{EMAIL}</span></a></li>
          {soc_contact}
        </ul>
      </div>
    </div>
  </div>
</section>
</main>

<footer>
  <div class="wrap foot">
    <img class="logo-d" src="{r}assets/logo-white.png" alt="MoreGrowth" width="640" height="162" loading="lazy"><img class="logo-l" src="{r}assets/logo-navy.png" alt="MoreGrowth" width="640" height="162" loading="lazy">
    <div class="socials">{soc_footer}</div>
    <div class="foot-meta"><a class="foot-link" href="{t['path']}privacy/">{PRIVACY[t['lang']]['link']}</a><span>© <span id="y">2026</span> {t['company']}. {t['rights']}.</span></div>
  </div>
</footer>
<script src="{r}assets/main.js" defer></script>
</body>
</html>
"""
    if privacy:
        P = PRIVACY[t["lang"]]
        html = html.replace(f"<title>{t['title']}</title>", f"<title>{P['title']}</title>")
        html = html.replace(f'content="{t["title"]}"', f'content="{P["title"]}"').replace(f'content="{t["desc"]}"', f'content="{P["desc"]}"')
        html = re.sub(r'<main id="main">.*?</main>', lambda m: privacy_main(t, P), html, count=1, flags=re.S)
    return html


def privacy_main(t, P):
    def sec(prefix, items):
        return "".join(f'<section class="pv-sec" id="{prefix}{i + 1}"><h3>{h}</h3>{b}</section>' for i, (h, b) in enumerate(items))
    toc = "".join(f'<li><a href="#a{i + 1}">{h}</a></li>' for i, (h, _) in enumerate(P["sections1"]))
    toc2 = "".join(f'<li><a href="#b{i + 1}">{h}</a></li>' for i, (h, _) in enumerate(P["sections2"]))
    return f"""<main id="main" class="pv">
<section class="pv-hero">
  <div class="wrap">
    <p class="kicker">{P['kicker']}</p>
    <h1>{P['h1']}</h1>
    <p class="pv-updated">{P['updated']}: <time datetime="2026-11-16">{UPDATED[t['lang']]}</time></p>
    <p class="pv-intro">{P['intro']}</p>
    <button type="button" class="btn btn-ghost pv-cookie" data-cookie-reset>{P['cookie_btn']}</button>
  </div>
</section>
<div class="wrap pv-layout">
  <nav class="pv-toc" aria-label="{P['toc']}">
    <strong>{P['toc']}</strong>
    <p><a href="#part1">{P['part1']}</a></p><ol>{toc}</ol>
    <p><a href="#part2">{P['part2']}</a></p><ol>{toc2}</ol>
  </nav>
  <div class="pv-body">
    <h2 id="part1">{P['part1']}</h2>
    {sec('a', P['sections1'])}
    <h2 id="part2">{P['part2']}</h2>
    {sec('b', P['sections2'])}
    <section class="pv-sec"><h3>{P['changes_h']}</h3>{P['changes']}</section>
  </div>
</div>
</main>"""


os.makedirs(os.path.join(OUT, "en"), exist_ok=True)
open(os.path.join(OUT, "index.html"), "w").write(page(AR))
open(os.path.join(OUT, "en", "index.html"), "w").write(page(EN))
os.makedirs(os.path.join(OUT, "nl"), exist_ok=True)
open(os.path.join(OUT, "nl", "index.html"), "w").write(page(NL))
for t, d in ((AR, "privacy"), (EN, "en/privacy"), (NL, "nl/privacy")):
    os.makedirs(os.path.join(OUT, d), exist_ok=True)
    open(os.path.join(OUT, d, "index.html"), "w").write(page(t, privacy=True))
print("written v2")
