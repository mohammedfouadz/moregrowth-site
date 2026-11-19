"""Rebuild / support campaign page (AR + EN), unlisted and noindex.

Run from the repo root:  python3 _source/rebuild.py
Writes /rebuild/index.html and /en/rebuild/index.html, reusing the head,
header and footer of the privacy pages so the chrome stays identical.
Edit the TEXT dicts and BUDGET below, then re-run.
"""
import re, pathlib, html

ROOT = pathlib.Path(__file__).resolve().parent.parent
GOAL = 67200
RAISED = 0          # update as money comes in
SUPPORTERS = 0

# (ar, en, amount for 6 months) — salaries/workspace from Mohammed, rest estimates
BUDGET = [
    ("رواتب فريق غزة (10 موظفين × 600 دولار شهريًا)", "Gaza team salaries (10 people × $600/month)", 36000),
    ("التسويق وجلب العملاء (2,000 دولار شهريًا)", "Marketing to win new clients ($2,000/month)", 12000),
    ("أجهزة بدل التي فُقدت", "Laptops and phones to replace what was lost", 5000),
    ("احتياطي ورسوم تحويل", "Contingency and transfer fees", 3000),
    ("الأدوات والاشتراكات (500 دولار شهريًا)", "Software and subscriptions ($500/month)", 3000),
    ("الأوراق القانونية في عُمان", "Legal papers in Oman", 2500),
    ("غرفة العمل في غزة (400 دولار شهريًا)", "Gaza workspace room ($400/month)", 2400),
    ("مزودو الخدمات المحاسبية والقانونية (300 دولار شهريًا)", "Accounting and legal providers ($300/month)", 1800),
    ("الأوراق القانونية في فلسطين", "Legal papers in Palestine", 1500),
]
assert sum(b[2] for b in BUDGET) == GOAL

ICON_IMG = '<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="4" width="18" height="16" rx="3"/><circle cx="9" cy="10" r="2"/><path d="m21 16-5-5-9 9"/></svg>'
ICON_USER = '<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="8" r="4"/><path d="M4 21c1.5-4 4.5-6 8-6s6.5 2 8 6"/></svg>'
ARROW = '<svg class="arrow" viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'

T = {
"ar": dict(
    tpl="privacy/index.html", out="rebuild/index.html", url="https://moregrowth.co/rebuild/",
    assets="../assets", locale="ar_AR", cur="عربي",
    title="نعيد البناء | ادعم عودة فريق مورجروث في غزة",
    desc="دُمّر مكتبنا في غزة ثلاث مرات. ساعدنا في تغطية ستة أشهر من التكاليف الجارية لنعيد تشغيل فريقنا ونتوسع في المنطقة العربية.",
    kicker="نعيد البناء",
    h1="أعِد فريقنا في غزة إلى العمل،<br><span class=\"grad\">وادعم عائلاتهم من جديد.</span>",
    sub="دُمّر مكتبنا ثلاث مرات. ولم يُدمَّر الفريق.",
    lead="مورجروث للحلول الرقمية شركة تسويق رقمي من غزة، وشريك معتمد من Google منذ 2020. نجمع 67,200 دولار لتغطية ستة أشهر من التكاليف الجارية، حتى نعيد تشغيل فريقنا في غزة ونقف على أقدامنا من جديد.",
    cta="ادعم عودة الفريق", cta2="اقرأ قصتنا",
    raised="جُمع حتى الآن", of="من هدف", supporters="داعمًا", soon="تنطلق الحملة قريبًا",
    photo_cap="مبنى مكتبنا في غزة بعد القصف",
    stats=[("15+", "موظفًا قبل الحرب، يعيلون عائلات كثيرة"), ("15", "عميلًا في السعودية وفلسطين والكويت والبحرين"), ("3", "مرات دُمّر فيها مكتبنا"), ("2020", "شريك معتمد من Google منذ")],
    story_k="قصتنا", story_h="من فريق يكبر إلى مكتب تحت الركام",
    ch=[
        ("ما بنيناه", "في غزة بنينا مورجروث للحلول الرقمية: فريق من أكثر من 15 موظفًا وموظفة، يعيل عملهم عائلات كثيرة. منذ 2020 ونحن شريك معتمد من Google، وخدمنا 15 عميلًا في السعودية وفلسطين والكويت والبحرين في التسويق الرقمي والإعلانات المدفوعة وكتابة المحتوى والاستشارات التسويقية."),
        ("ما حدث", "في الحرب دُمّر مكتبنا ثلاث مرات. في كل مرة كنا نجمع ما تبقى ونبدأ من جديد، حتى لم يبقَ ما نجمعه. توقفت العقود، وضاعت المشاريع، وتفرّق الفريق."),
        ("لماذا لم نتوقف", "الشركة ما زالت قائمة، ولدينا فريق يعمل اليوم في عُمان وفلسطين، لكن بلا مكتب. أعدنا بناء موقعنا وهويتنا، وعدنا للتواصل مع العملاء. ما ينقصنا هو الشيء الوحيد الذي لا يُبنى بالإصرار وحده: ستة أشهر من التكاليف الجارية حتى تقف الشركة على قدميها من جديد."),
    ],
    ph_team="صورة الفريق في المكتب (قريبًا)",
    ba_k="قبل وبعد", ba_h="المكتب الذي عملنا منه",
    before="قبل الحرب", after="بعد القصف", ph_before="صورة المكتب قبل الحرب (قريبًا)",
    tl=[("المرة الأولى", "التاريخ قريبًا"), ("المرة الثانية", "التاريخ قريبًا"), ("المرة الثالثة", "التاريخ قريبًا")],
    team_k="الفريق", team_h="الوجوه التي ستعود إلى العمل", team_p="نشارك صور زملائنا بموافقتهم.", ph_member="زميل من الفريق",
    impact_k="مسؤوليتنا المجتمعية", impact_h="لم نكن شركة أرباح فقط",
    impact_p="جزء من عملنا كان دائمًا لمجتمعنا في غزة، وإعادة الفريق تعني عودة هذا الأثر أيضًا.",
    impact=[
        ("+500", "طالب وخريج في آخر سنة", "قدّمنا دورات تدريبية تعزز ثقافة العمل الحر وبناء الدخل لدى الأفراد وخريجي الجامعات."),
        ("UCAS", "بالشراكة مع مؤسسات تعليمية", "دعمنا بالشراكة مع مؤسسات مثل الكلية الجامعية للعلوم التطبيقية (UCAS) التسويق والمبيعات لمشاريع نسائية منزلية عديدة، تعزيزًا لدور المرأة في المجتمع."),
        ("غزة", "مع مجتمع غزة التقني", "ساهمنا في الأعمال الخيرية من خلال مجتمع غزة التقني، كجزء من مسؤوليتنا كشركة."),
    ],
    plan_k="ما سنبنيه", plan_h="نعيد تشغيل فريق غزة أولًا",
    plan=[
        ("الأولوية", "إعادة تشغيل فريق غزة", "10 من زملائنا يعودون إلى العمل برواتب منتظمة، من غرفة عمل مستقلة نستأجرها في غزة ومجهزة بالكهرباء والإنترنت، ليداوموا منها ويخدموا عملاء من المنطقة العربية والعالم."),
        ("بالتوازي", "التوسع في المنطقة العربية", "انطلاقًا من مقرنا المسجل في سلطنة عُمان، نبني قاعدة عملاء في المنطقة في التسويق الرقمي والتحول بالذكاء الاصطناعي، حتى يتحول هذا الدعم إلى دخل مستدام بعد الأشهر الستة."),
    ],
    legal_h="ولنعمل بشكل قانوني سليم، نسوّي أوراقنا",
    legal=[("في فلسطين", ["تجديد السجل التجاري", "عضوية اتحاد شركات أنظمة المعلومات الفلسطيني (PITA)", "تخليص الضرائب المتراكمة"]),
           ("في سلطنة عُمان", ["السجل التجاري", "اشتراك غرفة تجارة وصناعة عُمان", "المصاريف التأسيسية"])],
    budget_k="أين تذهب الأموال", budget_h="67,200 دولار لستة أشهر",
    budget_p="الرواتب نصف المبلغ، ويليها التسويق لجلب العملاء. الأرقام أدناه خطتنا الحالية، وسننشر ما يُصرف فعلًا كل شهر.",
    total="المجموع", phases=[("المرحلة الأولى: 33,600 دولار", "الأجهزة، والأوراق القانونية، وأول ثلاثة أشهر من التشغيل."), ("المرحلة الثانية: 33,600 دولار", "الأشهر من الرابع إلى السادس، والتوسع في المنطقة.")],
    sup_k="كيف تشارك", sup_h="كل مساهمة تذهب إلى بند محدد",
    tiers=[("400$", "شهر كامل في غرفة العمل"), ("600$", "راتب شهر لزميل في غزة"), ("6,000$", "شهر كامل من رواتب الفريق")],
    any_amt="أو أي مبلغ تختاره",
    methods_h="طرق الدعم", methods_p="التحويل البنكي إلى حساب الشركة في سلطنة عُمان متاح الآن: راسلنا وسنرسل لك تفاصيل الحساب مباشرة. ونجهّز أيضًا رابطًا للدعم الإلكتروني بالبطاقة.",
    mail_btn="راسلنا للدعم", mail_subj="دعم إعادة بناء مورجروث",
    biz_h="لأصحاب الشركات", biz_p="يمكنك أيضًا دعمنا بشراء خدمات تسويق مقدمًا أو برعاية الحملة، ونصدر لك فاتورة رسمية من شركتنا في عُمان.",
    trust_k="الشفافية", trust_h="نلتزم أمامك بما يلي",
    trust=["تقرير شهري على هذه الصفحة بما جُمع وما صُرف وما تحقق.", "إن جمعنا أكثر من الهدف نمدد فترة التشغيل، وإن جمعنا أقل نحمي الرواتب أولًا.", "رسالة شكر شخصية لكل داعم، وحائط شكر لمن يرغب بظهور اسمه أو شعار شركته.", "الشركة مسجلة في سلطنة عُمان، ويمكنك التحقق من شراكتنا مع Google من الرابط أدناه."],
    partner_link="ملفنا على Google Partners",
    faq_h="أسئلة شائعة",
    faq=[("هل الدعم معفى من الضريبة؟", "لا. نحن شركة ولسنا جمعية خيرية، لذلك لا يمكننا إصدار إيصال إعفاء ضريبي. يمكن للشركات الحصول على فاتورة إذا اشترت خدمات مقدمًا."),
         ("من يستلم الأموال؟", "تُستلم الأموال باسم الشركة المسجلة في سلطنة عُمان، وتُحوّل الرواتب منها إلى الفريق في غزة."),
         ("كيف أعرف أين صُرفت مساهمتي؟", "ننشر تقريرًا شهريًا على هذه الصفحة، ونجيب على أي سؤال عبر info@moregrowth.co.")],
    sign="محمد، مؤسس مورجروث", sign_p="شكرًا لأنك قرأت قصتنا. مشاركتك لهذه الصفحة دعم أيضًا.",
),
"en": dict(
    tpl="en/privacy/index.html", out="en/rebuild/index.html", url="https://moregrowth.co/en/rebuild/",
    assets="../../assets", locale="en_US", cur="EN",
    title="Rebuild MoreGrowth | Help our Gaza team get back to work",
    desc="Our office in Gaza was destroyed three times. Help us cover six months of running costs to restart our team and grow across the Arab region.",
    kicker="Rebuild MoreGrowth",
    h1="Bring our Gaza team back to work,<br><span class=\"grad\">and support their families again.</span>",
    sub="Our office was destroyed three times. Our team was not.",
    lead="MoreGrowth Digital Solutions is a digital marketing agency from Gaza and a Google Partner since 2020. We are raising $67,200 to cover six months of running costs, so we can restart our Gaza team and stand on our own feet again.",
    cta="Back our comeback", cta2="Read our story",
    raised="raised so far", of="of", supporters="supporters", soon="Campaign opens soon",
    photo_cap="Our office building in Gaza after the strike",
    stats=[("15+", "people on our team before the war, supporting many families"), ("15", "clients in Saudi Arabia, Palestine, Kuwait and Bahrain"), ("3", "times our office was destroyed"), ("2020", "Google Partner since")],
    story_k="Our story", story_h="From a growing team to an office under rubble",
    ch=[
        ("What we built", "In Gaza we built MoreGrowth Digital Solutions: a team of more than 15 people whose salaries supported many families. Since 2020 we have been a Google Partner, serving 15 clients in Saudi Arabia, Palestine, Kuwait and Bahrain with digital marketing, paid ads, content and marketing consulting."),
        ("What happened", "During the war our office was destroyed three times. Each time we gathered what was left and started again, until there was nothing left to gather. Contracts stopped, projects were lost, and the team was scattered."),
        ("Why we didn't stop", "The company is still standing, with team members working today in Oman and Palestine, but without an office. We have rebuilt our website and brand and are back in touch with clients. What we lack is the one thing determination alone can't build: six months of running costs until the business can carry itself again."),
    ],
    ph_team="Team photo at the office (coming soon)",
    ba_k="Before and after", ba_h="The office we worked from",
    before="Before the war", after="After the strike", ph_before="Office before the war (coming soon)",
    tl=[("First time", "Date coming soon"), ("Second time", "Date coming soon"), ("Third time", "Date coming soon")],
    team_k="The team", team_h="The people going back to work", team_p="We share our colleagues' photos with their consent.", ph_member="Team member",
    impact_k="Social responsibility", impact_h="We were never only about profit",
    impact_p="Part of our work has always gone back to our community in Gaza. Bringing the team back brings that impact back too.",
    impact=[
        ("500+", "students and graduates in the last year", "Our training courses build a freelancing culture and help individuals and university graduates earn an income."),
        ("UCAS", "with education partners", "Together with institutions such as the University College of Applied Sciences (UCAS), we supported marketing and sales for many home-based businesses run by women."),
        ("Gaza", "with the Gaza tech community", "We contribute to charitable work through Gaza's tech community, as part of our responsibility as a company."),
    ],
    plan_k="What we will build", plan_h="Restarting our Gaza team comes first",
    plan=[
        ("Priority", "Restart the Gaza team", "Ten of our colleagues return to work on regular salaries, from a dedicated room we rent in Gaza with power and internet, serving clients across the Arab region and beyond."),
        ("In parallel", "Grow across the Arab region", "From our registered company in Oman we build a client base for digital marketing and AI transformation, so this support turns into sustainable revenue after six months."),
    ],
    legal_h="And we put our legal house in order",
    legal=[("In Palestine", ["Renew our commercial registration", "Membership of PITA, the Palestinian IT Association", "Clear accumulated taxes"]),
           ("In Oman", ["Commercial registration", "Oman Chamber of Commerce and Industry membership", "Setup costs"])],
    budget_k="Where the money goes", budget_h="$67,200 for six months",
    budget_p="Salaries are half the total, followed by marketing to win clients. These figures are our current plan, and we will publish actual spending every month.",
    total="Total", phases=[("Phase 1: $33,600", "Equipment, legal papers and the first three months of operations."), ("Phase 2: $33,600", "Months four to six, and regional growth.")],
    sup_k="How to help", sup_h="Every contribution goes to a specific line",
    tiers=[("$400", "A full month in the workspace"), ("$600", "One month's salary for a colleague in Gaza"), ("$6,000", "A full month of team salaries")],
    any_amt="Or any amount you choose",
    methods_h="Ways to give", methods_p="Bank transfer to our company account in Oman is open now: email us and we will send you the account details. A card payment link is on its way.",
    mail_btn="Email us to give", mail_subj="Supporting the MoreGrowth rebuild",
    biz_h="For business owners", biz_p="You can also support us by prepaying for marketing services or sponsoring the campaign, with a formal invoice from our company in Oman.",
    trust_k="Transparency", trust_h="Our commitments to you",
    trust=["A monthly report on this page: what came in, what was spent, and what it achieved.", "If we raise more, we extend the runway. If we raise less, salaries are protected first.", "A personal thank-you to every supporter, and a thank-you wall for those who want their name or logo shown.", "We are a registered company in Oman, and you can verify our Google Partner status below."],
    partner_link="Our Google Partners profile",
    faq_h="Questions",
    faq=[("Is my support tax-deductible?", "No. We are a company, not a charity, so we can't issue tax receipts. Businesses that prepay for services receive a normal invoice."),
         ("Who receives the money?", "Funds are received by our company registered in Oman, which pays the team in Gaza."),
         ("How will I know how it was spent?", "We publish a monthly report on this page and answer any question at info@moregrowth.co.")],
    sign="Mohammed, founder of MoreGrowth", sign_p="Thank you for reading our story. Sharing this page is support too.",
),
}


def ph(label, icon=ICON_IMG, cls=""):
    return f'<figure class="rb-ph {cls}"><div>{icon}<span>{label}</span></div></figure>'


def money(n, lang):
    return f"${n:,}" if lang == "en" else f"{n:,}$"


def body(lang, t):
    a = t["assets"]
    pct = round(RAISED * 100 / GOAL)
    mail = f'mailto:info@moregrowth.co?subject={html.escape(t["mail_subj"])}'
    stats = "".join(f'<div data-reveal style="--d:{i*.08}s"><b>{n}</b><span>{s}</span></div>' for i, (n, s) in enumerate(t["stats"]))
    ch = "".join(f'<div class="rb-ch" data-reveal><span class="rb-num">0{i+1}</span><h3>{h}</h3><p>{p}</p></div>' for i, (h, p) in enumerate(t["ch"]))
    tl = "".join(f'<li><b>{h}</b><span>{d}</span></li>' for h, d in t["tl"])
    team = "".join(ph(t["ph_member"], ICON_USER, "rb-face") for _ in range(6))
    plan = "".join(f'<article class="rb-card{" rb-prio" if i == 0 else ""}" data-reveal style="--d:{i*.1}s"><span class="rb-tag">{tag}</span><h3>{h}</h3><p>{p}</p></article>' for i, (tag, h, p) in enumerate(t["plan"]))
    legal = "".join(f'<div class="rb-legal-col"><h4>{h}</h4><ul>{"".join(f"<li>{x}</li>" for x in items)}</ul></div>' for h, items in t["legal"])
    mx = max(b[2] for b in BUDGET)
    i = 0 if lang == "ar" else 1
    rows = "".join(f'<li><span class="rb-b-l">{b[i]}</span><span class="rb-b-bar"><i style="--w:{b[2]*100/mx:.1f}%"></i></span><span class="rb-b-v">{money(b[2], lang)}</span></li>' for b in BUDGET)
    phases = "".join(f'<div><b>{h}</b><p>{p}</p></div>' for h, p in t["phases"])
    tiers = "".join(f'<a class="rb-tier" href="{mail}" data-reveal style="--d:{k*.08}s"><b>{v}</b><span>{d}</span></a>' for k, (v, d) in enumerate(t["tiers"]))
    trust = "".join(f"<li>{x}</li>" for x in t["trust"])
    impact = "".join(f'<article class="rb-card rb-impact" data-reveal style="--d:{k*.08}s"><b>{n}</b><span class="rb-tag">{tag}</span><p>{p}</p></article>' for k, (n, tag, p) in enumerate(t["impact"]))
    faq = "".join(f"<details class=\"rb-faq\"><summary>{q}</summary><p>{ans}</p></details>" for q, ans in t["faq"])
    meter_txt = f'<b>{money(RAISED, lang)}</b> {t["raised"]} · {t["of"]} {money(GOAL, lang)}' if RAISED else f'<b>{money(GOAL, lang)}</b> · {t["soon"]}'
    return f'''<main id="main" class="rb">
<section class="rb-hero">
  <div class="wrap rb-hero-grid">
    <div>
      <p class="kicker">{t["kicker"]}</p>
      <h1>{t["h1"]}</h1>
      <p class="rb-hsub">{t["sub"]}</p>
      <p class="rb-lead">{t["lead"]}</p>
      <div class="rb-meter" role="img" aria-label="{RAISED} / {GOAL}"><div class="rb-meter-bar"><i style="--w:{max(pct,1)}%"></i></div><p>{meter_txt}</p></div>
      <div class="rb-ctas"><a class="btn btn-primary" href="#support" data-rb-cta>{t["cta"]} {ARROW}</a><a class="btn btn-ghost" href="#story">{t["cta2"]}</a></div>
    </div>
    <figure class="rb-hero-photo" data-reveal="zoom"><img src="{a}/rebuild/office-destroyed.jpg" alt="{t["photo_cap"]}" width="1170" height="1560"><figcaption>{t["photo_cap"]}</figcaption></figure>
  </div>
</section>
<section class="wrap rb-stats">{stats}</section>

<section class="wrap rb-sec" id="story">
  <p class="kicker">{t["story_k"]}</p><h2>{t["story_h"]}</h2>
  <div class="rb-story">{ch}</div>
  {ph(t["ph_team"], cls="rb-wide")}
</section>

<section class="wrap rb-sec">
  <p class="kicker">{t["ba_k"]}</p><h2>{t["ba_h"]}</h2>
  <div class="rb-ba">
    <div><span class="rb-ba-tag">{t["before"]}</span>{ph(t["ph_before"])}</div>
    <div><span class="rb-ba-tag rb-after">{t["after"]}</span><figure class="rb-photo"><img src="{a}/rebuild/office-destroyed.jpg" alt="{t["photo_cap"]}" loading="lazy" width="1170" height="1560"></figure></div>
  </div>
  <ol class="rb-tl">{tl}</ol>
</section>

<section class="wrap rb-sec">
  <p class="kicker">{t["team_k"]}</p><h2>{t["team_h"]}</h2><p class="rb-sub">{t["team_p"]}</p>
  <div class="rb-team">{team}</div>
</section>

<section class="wrap rb-sec">
  <p class="kicker">{t["impact_k"]}</p><h2>{t["impact_h"]}</h2><p class="rb-sub">{t["impact_p"]}</p>
  <div class="rb-impacts">{impact}</div>
</section>

<section class="wrap rb-sec">
  <p class="kicker">{t["plan_k"]}</p><h2>{t["plan_h"]}</h2>
  <div class="rb-plan">{plan}</div>
  <div class="rb-legal" data-reveal><h3>{t["legal_h"]}</h3><div class="rb-legal-grid">{legal}</div></div>
</section>

<section class="wrap rb-sec" id="budget">
  <p class="kicker">{t["budget_k"]}</p><h2>{t["budget_h"]}</h2><p class="rb-sub">{t["budget_p"]}</p>
  <div class="rb-budget" data-reveal><ul>{rows}</ul><p class="rb-total"><span>{t["total"]}</span><b>{money(GOAL, lang)}</b></p></div>
  <div class="rb-phases">{phases}</div>
</section>

<section class="wrap rb-sec" id="support">
  <p class="kicker">{t["sup_k"]}</p><h2>{t["sup_h"]}</h2>
  <div class="rb-tiers">{tiers}</div>
  <p class="rb-any">{t["any_amt"]}</p>
  <div class="rb-give">
    <div class="rb-card"><h3>{t["methods_h"]}</h3><p>{t["methods_p"]}</p><a class="btn btn-primary" href="{mail}" data-rb-cta>{t["mail_btn"]} {ARROW}</a></div>
    <div class="rb-card"><h3>{t["biz_h"]}</h3><p>{t["biz_p"]}</p><a class="btn btn-ghost" href="{mail}">info@moregrowth.co</a></div>
  </div>
</section>

<section class="wrap rb-sec">
  <p class="kicker">{t["trust_k"]}</p><h2>{t["trust_h"]}</h2>
  <div class="rb-trust"><ul>{trust}</ul><a class="rb-partner" href="https://www.google.com/partners/agency?id=5882315022" target="_blank" rel="noopener">{t["partner_link"]} ↗</a></div>
  <h3 class="rb-faq-h">{t["faq_h"]}</h3>{faq}
  <div class="rb-sign"><p>{t["sign_p"]}</p><b>{t["sign"]}</b></div>
</section>
</main>'''


def build(lang):
    t = T[lang]
    src = (ROOT / t["tpl"]).read_text(encoding="utf-8")
    head_hdr, rest = src.split('<main id="main"', 1)
    footer = rest.split("</main>", 1)[1]
    s = head_hdr
    s = re.sub(r"<title>.*?</title>", f"<title>{t['title']}</title>", s)
    s = re.sub(r'(<meta (?:name="description"|property="og:description") content=")[^"]*', lambda m: m.group(1) + t["desc"], s)
    s = re.sub(r'(<meta property="og:title" content=")[^"]*', lambda m: m.group(1) + t["title"], s)
    s = re.sub(r'<link rel="canonical"[^>]*>', f'<link rel="canonical" href="{t["url"]}">\n<meta name="robots" content="noindex">', s)
    s = re.sub(r'<link rel="alternate" hreflang="nl"[^>]*>\n', "", s)
    s = re.sub(r'(hreflang="(?:ar|x-default)" href=")[^"]*', lambda m: m.group(1) + "https://moregrowth.co/rebuild/", s)
    s = re.sub(r'(hreflang="en" href=")[^"]*', lambda m: m.group(1) + "https://moregrowth.co/en/rebuild/", s)
    s = re.sub(r'(<meta property="og:url" content=")[^"]*', lambda m: m.group(1) + t["url"], s)
    s = re.sub(r'(<meta property="og:image" content=")[^"]*', lambda m: m.group(1) + f"https://moregrowth.co/assets/rebuild/og-{lang}.jpg", s)
    s = s.replace('<script type="application/ld+json">', '<link rel="stylesheet" href="%s/rebuild.css">\n<script type="application/ld+json">' % t["assets"], 1)
    # language menu: AR + EN only
    s = re.sub(r'href="/privacy/"', 'href="/rebuild/"', s)
    s = re.sub(r'href="/en/privacy/"', 'href="/en/rebuild/"', s)
    s = re.sub(r'<li><a href="/nl/privacy/"[^<]*<span>[^<]*</span><b>NL</b></a></li>', "", s)
    out = s + body(lang, t) + footer
    p = ROOT / t["out"]
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(out, encoding="utf-8")
    print("wrote", p.relative_to(ROOT))


if __name__ == "__main__":
    for l in T:
        build(l)
