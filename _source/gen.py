"""Generate the bilingual MoreGrowth static site (Arabic at /, English at /en/)."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from icons import ICONS as I

OUT = sys.argv[1] if len(sys.argv) > 1 else None
SITE = "https://moregrowth.co"
PARTNER = "https://www.google.com/partners/agency?id=5882315022"
EMAIL = "info@moregrowth.co"
SOC = [
    ("linkedin", "LinkedIn", "https://www.linkedin.com/company/moregrowthco"),
    ("instagram", "Instagram", "https://www.instagram.com/moregrowthco/"),
    ("facebook", "Facebook", "https://www.facebook.com/moregrowthco/"),
    ("x", "X (Twitter)", "https://twitter.com/moregrowthco/"),
]

AR = dict(
    lang="ar", dir="rtl", path="/", other="/en/", other_label="English", root="",
    title="مورجروث للحلول الرقمية | التحول للذكاء الاصطناعي والتسويق الرقمي",
    desc="مورجروث للحلول الرقمية: شريك جوجل المعتمد. نساعد المؤسسات على التحول للذكاء الاصطناعي ونمو المبيعات عبر الإعلانات المدفوعة وتحسين محركات البحث وكتابة المحتوى والاستشارات التسويقية.",
    og_locale="ar_AR",
    nav=[("#services", "خدماتنا"), ("#approach", "منهجيتنا"), ("#about", "من نحن"), ("#contact", "تواصل معنا")],
    nav_cta="احجز استشارة",
    eyebrow="شريك جوجل المعتمد · Google Partner",
    h1="نمو أذكى لمؤسستك: <em>ذكاء اصطناعي</em> يعمل، وتسويق يحقق نتائج",
    lead="مورجروث للحلول الرقمية تساعد المؤسسات والشركات في العالم العربي على تبنّي الذكاء الاصطناعي بشكل عملي، لتوفير الوقت والتكلفة ونمو حقيقي في المبيعات، إلى جانب خبرتنا في التسويق الرقمي والإعلانات المدفوعة.",
    btn1="ابدأ بتقييم جاهزية مجاني", btn2="استكشف خدماتنا",
    badge_partner="شريك جوجل للإعلانات: تحقق من الاعتماد",
    badge_bi="فريق يعمل بالعربية والإنجليزية",
    svc_k="خدماتنا", svc_h="مساران متكاملان لنمو مؤسستك",
    svc_p="نجمع بين خبرة تسويقية عملية منذ سنوات وفهم تطبيقي للذكاء الاصطناعي، حتى تكون التقنية في خدمة أهداف العمل، لا العكس.",
    ai_tag="التحول للذكاء الاصطناعي", ai_h="الذكاء الاصطناعي للمؤسسات",
    ai_p="من الفكرة إلى التطبيق: نحدد أين يصنع الذكاء الاصطناعي قيمة حقيقية في مؤسستك ونبنيها معك خطوة بخطوة.",
    ai=[
        ("تقييم الجاهزية وخارطة الطريق", "تحليل العمليات والبيانات وتحديد أعلى فرص العائد وأولويات التنفيذ."),
        ("أتمتة سير العمل والوكلاء الذكيون", "أتمتة المهام المتكررة في المبيعات وخدمة العملاء والعمليات والتقارير."),
        ("مساعدات ذكية ومحادثة باللغة العربية", "روبوتات محادثة ومساعدات معرفية مدربة على محتوى مؤسستك."),
        ("الذكاء الاصطناعي في التسويق", "إنتاج المحتوى، وتحليل الحملات، والاستهداف، والتخصيص على نطاق واسع."),
        ("تدريب الفرق ونشر الثقافة الرقمية", "ورش عمل عملية للإدارة والموظفين حول الاستخدام الآمن والمسؤول للأدوات."),
        ("الحوكمة وسياسات الاستخدام", "سياسات خصوصية البيانات والاستخدام المسؤول تناسب حجم مؤسستك."),
    ],
    mk_tag="التسويق الرقمي", mk_h="تسويق ونمو قائم على البيانات",
    mk_p="خدماتنا الأساسية التي بنينا عليها سمعتنا، مدعومة اليوم بأدوات الذكاء الاصطناعي.",
    mk=[
        ("إدارة حملات جوجل أدز", "البحث والتسوق والفيديو، بخبرة شريك جوجل المعتمد."),
        ("إعلانات منصات التواصل الاجتماعي", "ميتا، سناب شات، تيك توك، ولينكدإن."),
        ("تحسين محركات البحث SEO", "تحسين الظهور في نتائج البحث ومحركات الإجابة بالذكاء الاصطناعي."),
        ("كتابة المحتوى الإبداعي", "محتوى عربي وإنجليزي للمواقع والحملات ووسائل التواصل."),
        ("إدارة صفحات التواصل الاجتماعي", "تخطيط ونشر وتفاعل وتقارير شهرية."),
        ("الاستشارات التسويقية", "استراتيجيات النمو، والتسويق بالبريد الإلكتروني، وتطوير المواقع."),
    ],
    ap_k="منهجيتنا", ap_h="من التقييم إلى النتائج، بخطوات واضحة",
    steps=[
        ("نفهم", "جلسة تشخيص لأهدافك وعملياتك وبياناتك الحالية."),
        ("نخطط", "خارطة طريق بأولويات واضحة ومؤشرات أداء قابلة للقياس."),
        ("نجرّب", "مشروع تجريبي سريع يثبت القيمة قبل التوسع."),
        ("نوسّع", "تعميم ما ينجح، وتدريب الفريق، ومتابعة مستمرة."),
    ],
    sectors_h="قطاعات نخدمها",
    sectors=["الشركات الصغيرة والمتوسطة", "التجارة الإلكترونية", "المنظمات غير الحكومية", "التعليم والتدريب", "الخدمات المهنية", "الشركات الناشئة"],
    why_k="لماذا مورجروث", why_h="شريك يفهم السوق العربي ويقيس النتائج",
    why=[
        ("شريك جوجل المعتمد", "اعتماد رسمي في إدارة إعلانات جوجل أدز وفق معايير الأداء الخاصة بجوجل."),
        ("نتائج قابلة للقياس", "كل مشروع يبدأ بمؤشرات أداء واضحة وتقارير دورية شفافة."),
        ("عربي أولاً", "محتوى وأدوات ذكاء اصطناعي تفهم لغة وثقافة جمهورك."),
    ],
    ab_k="من نحن", ab_h="قصتنا",
    ab_p1="مورجروث للحلول الرقمية شركة متخصصة في التسويق الرقمي والنمو، تضم فريقاً من المتخصصين في الإعلانات المدفوعة والمحتوى وتحسين محركات البحث. خدمنا على مدى سنوات شركات ناشئة ومتوسطة في عدة أسواق عربية.",
    ab_p2="في عام 2023 فقدنا مقرنا ومشاريعنا في غزة بسبب الحرب. اليوم نعود بإصرار أكبر وتركيز جديد: مساعدة المؤسسات على النمو عبر الذكاء الاصطناعي والتسويق الرقمي. الشركة مسجلة في سلطنة عُمان، ونعمل عن بُعد مع عملاء في المنطقة.",
    quote="رؤيتنا: أن نكون روّاد الابتكار في مواكبة التقدم المتسارع في التسويق الرقمي والذكاء الاصطناعي بكل أشكاله الحديثة.",
    values=[("النزاهة والمسؤولية", "شفافية كاملة في كل ما نقوم به."), ("الجودة", "التزام بالمعايير والجداول الزمنية."), ("رضا العملاء", "نسعى لتجاوز التوقعات."), ("التطوير المستمر", "نتعلم ونتطور مع التقنية.")],
    ct_h="لنبدأ الحديث عن نمو مؤسستك",
    ct_p="احجز جلسة استشارية مجانية مدتها 30 دقيقة لتقييم جاهزية مؤسستك للذكاء الاصطناعي أو مراجعة أداء حملاتك التسويقية.",
    mail_subject="طلب استشارة من موقع مورجروث",
    rights="جميع الحقوق محفوظة",
    company="مورجروث للحلول الرقمية",
    menu="القائمة",
    skip="تخطَّ إلى المحتوى",
)

EN = dict(
    lang="en", dir="ltr", path="/en/", other="/", other_label="العربية", root="../",
    title="MoreGrowth Digital Solutions | Enterprise AI Transformation & Digital Marketing",
    desc="MoreGrowth Digital Solutions is a Google Partner agency helping organizations adopt AI and grow revenue through paid advertising, SEO, content writing and marketing consulting.",
    og_locale="en_US",
    nav=[("#services", "Services"), ("#approach", "Approach"), ("#about", "About"), ("#contact", "Contact")],
    nav_cta="Book a consultation",
    eyebrow="Google Partner agency",
    h1="Smarter growth: <em>AI that works</em> and marketing that delivers",
    lead="MoreGrowth Digital Solutions helps organizations across the Arab world adopt AI in practical ways, turning it into saved time, lower costs and real revenue growth, backed by our track record in digital marketing and paid advertising.",
    btn1="Get a free AI readiness check", btn2="Explore services",
    badge_partner="Google Ads Partner: verify our status",
    badge_bi="Bilingual team: Arabic & English",
    svc_k="Services", svc_h="Two connected tracks for your growth",
    svc_p="We combine years of hands-on marketing experience with applied AI know-how, so technology serves your business goals, not the other way round.",
    ai_tag="AI transformation", ai_h="AI for organizations",
    ai_p="From idea to implementation: we find where AI creates real value in your organization and build it with you, step by step.",
    ai=[
        ("AI readiness assessment & roadmap", "Review of processes and data to find the highest-return opportunities and set priorities."),
        ("Workflow automation & AI agents", "Automate repetitive work across sales, customer service, operations and reporting."),
        ("Arabic-first AI assistants", "Chatbots and knowledge assistants trained on your organization's content."),
        ("AI-powered marketing", "Content production, campaign analysis, targeting and personalization at scale."),
        ("Team training & AI literacy", "Practical workshops for leadership and staff on safe, responsible use."),
        ("AI governance & usage policies", "Data-privacy and responsible-use policies sized for your organization."),
    ],
    mk_tag="Digital marketing", mk_h="Data-driven marketing & growth",
    mk_p="The core services we built our reputation on, now amplified with AI tools.",
    mk=[
        ("Google Ads management", "Search, Shopping and video campaigns, run by a certified Google Partner."),
        ("Social media advertising", "Meta, Snapchat, TikTok and LinkedIn."),
        ("Search engine optimization", "Visibility in search results and in AI answer engines."),
        ("Creative content writing", "Arabic and English content for websites, campaigns and social."),
        ("Social media management", "Planning, publishing, community management and monthly reporting."),
        ("Marketing consulting", "Growth strategy, email marketing and web development."),
    ],
    ap_k="Approach", ap_h="From assessment to results, in clear steps",
    steps=[
        ("Understand", "A diagnostic session on your goals, processes and current data."),
        ("Plan", "A roadmap with clear priorities and measurable KPIs."),
        ("Pilot", "A fast pilot project that proves value before scaling."),
        ("Scale", "Roll out what works, train your team, keep improving."),
    ],
    sectors_h="Who we work with",
    sectors=["SMEs", "E-commerce", "NGOs & development programs", "Education & training", "Professional services", "Startups"],
    why_k="Why MoreGrowth", why_h="A partner that knows the Arab market and measures results",
    why=[
        ("Certified Google Partner", "Officially recognized for managing Google Ads to Google's performance standards."),
        ("Measurable outcomes", "Every engagement starts with clear KPIs and transparent, regular reporting."),
        ("Arabic first", "Content and AI tools that understand your audience's language and culture."),
    ],
    ab_k="About", ab_h="Our story",
    ab_p1="MoreGrowth Digital Solutions is a digital marketing and growth company with specialists in paid advertising, content and SEO. Over the years we have served startups and mid-sized companies across several Arab markets.",
    ab_p2="In 2023 we lost our office and our ongoing projects in Gaza to the war. We are back with more determination and a new focus: helping organizations grow through AI and digital marketing. The company is registered in the Sultanate of Oman and works remotely with clients across the region.",
    quote="Our vision: to lead in innovation, keeping pace with the rapid progress of digital marketing and AI in all its modern forms.",
    values=[("Integrity", "Full transparency in everything we do."), ("Quality", "Committed to standards and timelines."), ("Client satisfaction", "We aim to exceed expectations."), ("Continuous growth", "We learn and evolve with technology.")],
    ct_h="Let's talk about your growth",
    ct_p="Book a free 30-minute consultation to assess your organization's AI readiness or review the performance of your marketing campaigns.",
    mail_subject="Consultation request from moregrowth.co",
    rights="All rights reserved",
    company="MoreGrowth Digital Solutions",
    menu="Menu",
    skip="Skip to content",
)


def li(items):
    return "".join(f"<li><strong>{a}</strong><span>{b}</span></li>" for a, b in items)


def page(t):
    r = t["root"]
    from urllib.parse import quote
    mailto = f"mailto:{EMAIL}?subject={quote(t['mail_subject'])}"
    nav = "".join(f'<li><a href="{h}">{l}</a></li>' for h, l in t["nav"])
    soc_footer = "".join(f'<a href="{u}" target="_blank" rel="noopener" aria-label="{n}">{I[k]}</a>' for k, n, u in SOC)
    soc_contact = "".join(f'<li><a href="{u}" target="_blank" rel="noopener">{I[k]}<span>{n}</span></a></li>' for k, n, u in SOC[:2])
    steps = "".join(f'<div class="step"><h3>{a}</h3><p>{b}</p></div>' for a, b in t["steps"])
    why = "".join(f'<div><h3>{a}</h3><p>{b}</p></div>' for a, b in t["why"])
    values = "".join(f'<div><strong>{a}</strong><span>{b}</span></div>' for a, b in t["values"])
    sectors = "".join(f"<span>{s}</span>" for s in t["sectors"])
    url = SITE + t["path"]
    ld = ('{"@context":"https://schema.org","@type":"ProfessionalService","name":"MoreGrowth Digital Solutions",'
          '"alternateName":"مورجروث للحلول الرقمية","url":"' + SITE + '/","email":"' + EMAIL + '",'
          '"logo":"' + SITE + '/assets/favicon.png","areaServed":"Middle East and North Africa",'
          '"sameAs":[' + ",".join(f'"{u}"' for _, _, u in SOC) + f',"{PARTNER}"]' + '}')
    return f"""<!doctype html>
<html lang="{t['lang']}" dir="{t['dir']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{t['title']}</title>
<meta name="description" content="{t['desc']}">
<link rel="canonical" href="{url}">
<link rel="alternate" hreflang="ar" href="{SITE}/">
<link rel="alternate" hreflang="en" href="{SITE}/en/">
<link rel="alternate" hreflang="x-default" href="{SITE}/">
<meta property="og:type" content="website">
<meta property="og:title" content="{t['title']}">
<meta property="og:description" content="{t['desc']}">
<meta property="og:url" content="{url}">
<meta property="og:locale" content="{t['og_locale']}">
<meta property="og:image" content="{SITE}/assets/og.png">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:site" content="@moregrowthco">
<meta name="theme-color" content="#061733">
<link rel="icon" type="image/png" href="{r}assets/favicon.png">
<link rel="apple-touch-icon" href="{r}assets/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+Arabic:wght@400;500;600;700&family=IBM+Plex+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{r}assets/style.css">
<script type="application/ld+json">{ld}</script>
</head>
<body>
<a class="skip" href="#main">{t['skip']}</a>
<header class="site-header">
  <nav class="wrap nav" aria-label="main">
    <a class="brand" href="{t['path']}"><img src="{r}assets/logo-white.png" alt="MoreGrowth" width="640" height="162"></a>
    <button class="menu-btn" aria-expanded="false" aria-controls="nav-links" aria-label="{t['menu']}">&#9776;</button>
    <ul class="nav-links" id="nav-links">
      {nav}
      <li><a class="lang" href="{t['other']}" hreflang="{'en' if t['lang']=='ar' else 'ar'}">{t['other_label']}</a></li>
      <li><a class="nav-cta" href="{mailto}">{t['nav_cta']}</a></li>
    </ul>
  </nav>
</header>
<main id="main">
<section class="hero">
  <div class="wrap">
    <span class="eyebrow">{t['eyebrow']}</span>
    <h1>{t['h1']}</h1>
    <p class="lead">{t['lead']}</p>
    <div class="btns">
      <a class="btn btn-primary" href="{mailto}">{t['btn1']}</a>
      <a class="btn btn-ghost" href="#services">{t['btn2']}</a>
    </div>
    <div class="hero-badges">
      <a href="{PARTNER}" target="_blank" rel="noopener">{I['g']}<span>{t['badge_partner']}</span></a>
      <a href="#about"><span style="font-weight:700;color:var(--green)">ع / EN</span><span>{t['badge_bi']}</span></a>
    </div>
  </div>
</section>

<section id="services">
  <div class="wrap">
    <div class="section-head"><p class="kicker">{t['svc_k']}</p><h2>{t['svc_h']}</h2><p>{t['svc_p']}</p></div>
    <div class="pillars">
      <article class="pillar ai"><span class="tag">{t['ai_tag']}</span><h3>{t['ai_h']}</h3><p>{t['ai_p']}</p><ul class="svc">{li(t['ai'])}</ul></article>
      <article class="pillar"><span class="tag">{t['mk_tag']}</span><h3>{t['mk_h']}</h3><p>{t['mk_p']}</p><ul class="svc">{li(t['mk'])}</ul></article>
    </div>
  </div>
</section>

<section id="approach" class="soft">
  <div class="wrap">
    <div class="section-head"><p class="kicker">{t['ap_k']}</p><h2>{t['ap_h']}</h2></div>
    <div class="steps">{steps}</div>
    <h3 style="margin:44px 0 10px;color:var(--navy)">{t['sectors_h']}</h3>
    <div class="sectors">{sectors}</div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="section-head"><p class="kicker">{t['why_k']}</p><h2>{t['why_h']}</h2></div>
    <div class="why">{why}</div>
  </div>
</section>

<section id="about" class="soft">
  <div class="wrap story">
    <div>
      <p class="kicker">{t['ab_k']}</p><h2>{t['ab_h']}</h2>
      <p>{t['ab_p1']}</p>
      <p>{t['ab_p2']}</p>
      <div class="values">{values}</div>
    </div>
    <blockquote>{t['quote']}</blockquote>
  </div>
</section>

<section id="contact">
  <div class="wrap">
    <div class="cta">
      <div><h2>{t['ct_h']}</h2><p>{t['ct_p']}</p></div>
      <ul class="contact-list">
        <li><a href="{mailto}">{I['mail']}<span class="ltr">{EMAIL}</span></a></li>
        {soc_contact}
      </ul>
    </div>
  </div>
</section>
</main>
<footer>
  <div class="wrap foot">
    <img src="{r}assets/logo-white.png" alt="MoreGrowth" width="640" height="162">
    <div class="socials">{soc_footer}</div>
    <div>© <span id="y">2026</span> {t['company']}. {t['rights']}.</div>
  </div>
</footer>
<script>
document.getElementById('y').textContent=new Date().getFullYear();
var b=document.querySelector('.menu-btn'),n=document.getElementById('nav-links');
b.addEventListener('click',function(){{var o=n.classList.toggle('open');b.setAttribute('aria-expanded',o)}});
n.addEventListener('click',function(e){{if(e.target.tagName==='A'){{n.classList.remove('open');b.setAttribute('aria-expanded',false)}}}});
</script>
</body>
</html>
"""


if __name__ == "__main__":
    os.makedirs(os.path.join(OUT, "en"), exist_ok=True)
    open(os.path.join(OUT, "index.html"), "w").write(page(AR))
    open(os.path.join(OUT, "en", "index.html"), "w").write(page(EN))
    print("written")
