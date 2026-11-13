#!/usr/bin/env python3
"""Static site generator for the Nebras Technology website.

Run:  python3 _build/build.py
Writes every page as a plain .html file at the repository root.
"""
import os, html

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMG = "assets/img/"

# ------------------------------------------------------------------ icons
ARR_UR = '<svg viewBox="0 0 12 12" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M3 9 9 3M4 3h5v5"/></svg>'
ARR_R = '<svg viewBox="0 0 12 12" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M1.5 6h9M7 2.5 10.5 6 7 9.5"/></svg>'
ARR_L = '<svg viewBox="0 0 12 12" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M10.5 6h-9M5 2.5 1.5 6 5 9.5"/></svg>'
CHEV = '<svg viewBox="0 0 10 10" fill="none" stroke="currentColor" stroke-width="1.6"><path d="m2 3.5 3 3 3-3"/></svg>'
CRUMB = '<svg viewBox="0 0 8 8" fill="none" stroke="currentColor" stroke-width="1.5"><path d="m2.5 1 3 3-3 3"/></svg>'
SEND = '<svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M14.5 1.5 7 9M14.5 1.5 10 14.5 7 9 1.5 6z"/></svg>'

ICONS = {
    "video": '<svg viewBox="0 0 24 24"><rect x="2.5" y="6" width="13" height="12" rx="2"/><path d="m15.5 10 6-3.5v11l-6-3.5"/></svg>',
    "disc": '<svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="9.5"/><circle cx="12" cy="12" r="2.5"/><path d="M7 9.5a5.5 5.5 0 0 1 3-3M17 14.5a5.5 5.5 0 0 1-3 3"/></svg>',
    "shield": '<svg viewBox="0 0 24 24"><path d="M12 2.5 4 5.5v6c0 5 3.4 8.6 8 10 4.6-1.4 8-5 8-10v-6z"/><path d="m8.5 12 2.5 2.5 4.5-5"/></svg>',
    "calendar": '<svg viewBox="0 0 24 24"><rect x="3" y="4.5" width="15" height="15" rx="2"/><path d="M3 9h15M7.5 2.5v4M13.5 2.5v4"/><circle cx="17.5" cy="17.5" r="4.5"/><path d="M17.5 15.5v2l1.4 1.2"/></svg>',
    "chart": '<svg viewBox="0 0 24 24"><path d="M3 20.5h18M5 17l4.5-5 3.5 3 6.5-8"/><path d="M15.5 7h4v4"/></svg>',
    "code": '<svg viewBox="0 0 24 24"><path d="m8 7-5 5 5 5M16 7l5 5-5 5M13.5 4.5l-3 15"/></svg>',
    "ops": '<svg viewBox="0 0 24 24"><circle cx="6" cy="6" r="2.5"/><circle cx="18" cy="18" r="2.5"/><path d="M8.5 6H15a3 3 0 0 1 0 6H9a3 3 0 0 0 0 6h6.5"/></svg>',
    "sales": '<svg viewBox="0 0 24 24"><path d="M3 8.5 7 5l4 2 4-2 6 4v6l-6 4-4-2"/><path d="m3 8.5 0 6 5 4 3-2.5M11 7l-3 3.5 2 1.5 3-2"/></svg>',
    "wrench": '<svg viewBox="0 0 24 24"><path d="M14.5 6.5a4 4 0 0 0 5 5l1-1a5.5 5.5 0 0 1-7.4 5.2L6.5 22 2 17.5l6.3-6.6A5.5 5.5 0 0 1 13.5 3.5z"/></svg>',
    "megaphone": '<svg viewBox="0 0 24 24"><path d="M3 10v4h3l8 5V5L6 10zM17.5 9a4 4 0 0 1 0 6M6 14l1.5 6h3L9 15"/></svg>',
    "swap": '<svg viewBox="0 0 24 24"><path d="M4 8h15M15 4l4 4-4 4M20 16H5M9 12l-4 4 4 4"/></svg>',
    "users": '<svg viewBox="0 0 24 24"><circle cx="9" cy="8" r="3.5"/><path d="M2.5 20a6.5 6.5 0 0 1 13 0M16 4.5a3.5 3.5 0 0 1 0 7M18 14a6 6 0 0 1 3.5 6"/></svg>',
    "message": '<svg viewBox="0 0 24 24"><path d="M4 4h16v12H9l-5 4z"/><path d="M8 8.5h8M8 12h5"/></svg>',
    "scan": '<svg viewBox="0 0 24 24"><path d="M3 8V4h4M17 4h4v4M21 16v4h-4M7 20H3v-4"/><circle cx="12" cy="11" r="3"/><path d="m14.5 13.5 3 3"/></svg>',
    "phone": '<svg viewBox="0 0 24 24"><rect x="6" y="2.5" width="12" height="19" rx="2.5"/><path d="M10.5 18.5h3"/></svg>',
    "clock": '<svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="9.5"/><path d="M12 6.5V12l3.5 2.5"/></svg>',
    "globe": '<svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="9.5"/><path d="M2.5 12h19M12 2.5c3 3.3 3 15.7 0 19M12 2.5c-3 3.3-3 15.7 0 19"/></svg>',
    "pin": '<svg viewBox="0 0 24 24"><path d="M12 22s7-6.5 7-12a7 7 0 0 0-14 0c0 5.5 7 12 7 12z"/><circle cx="12" cy="10" r="2.5"/></svg>',
}
SOC = {
    "LinkedIn": '<svg viewBox="0 0 24 24"><rect x="3" y="9" width="4" height="12"/><circle cx="5" cy="4.5" r="2"/><path d="M10 21V9h4v2c1-1.5 2.5-2.3 4-2.3 2.4 0 3.5 1.6 3.5 4.3v8h-4v-7c0-1.4-.6-2-1.7-2S14 13 14 14.4V21z"/></svg>',
    "Facebook": '<svg viewBox="0 0 24 24"><path d="M14 8h3V4h-3a4 4 0 0 0-4 4v3H7v4h3v7h4v-7h3l1-4h-4V8.8c0-.5.3-.8.8-.8z"/></svg>',
    "Instagram": '<svg viewBox="0 0 24 24"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.3" cy="6.7" r=".6"/></svg>',
}

def esc(s):
    return html.escape(s, quote=True)

def img(src, alt="", cls="", extra="", lazy=True):
    c = f' class="{cls}"' if cls else ""
    ld = "lazy" if lazy else "eager"
    return f'<img src="{IMG}{src}" alt="{esc(alt)}"{c} loading="{ld}" decoding="async"{extra}>'

def eyebrow(t, cls=""):
    return f'<span class="eyebrow {cls}">{t}</span>'

# ------------------------------------------------------------------ navigation
SOLUTIONS_MENU = [
    ("Radiology", "radiology.html", [("PaXtreme PACS", "paxtreme.html"), ("OneRIS", "oneris.html"), ("OneAccred", "oneaccred.html"), ("OneRad", "onerad.html"), ("InstaShare", "instashare.html"), ("Neo Q partnership", "neoq.html")]),
    ("Endoscopy", "endoscopy.html", [("EndoStream", "endostream.html"), ("OneEndo", "oneendo.html")]),
    ("Dental", "dental.html", [("DentaLore Cloud", "dentalore-cloud.html"), ("DentaLore DS", "dentalore-ds.html")]),
]

def header(active):
    def a(key, label, href):
        cls = "nav-link active" if active == key else "nav-link"
        return f'<li><a class="{cls}" href="{href}">{label}</a></li>'
    co_cls = "nav-link active" if active == "company" else "nav-link"
    so_cls = "nav-link active" if active == "solutions" else "nav-link"
    sol = ""
    for title, href, subs in SOLUTIONS_MENU:
        sol += f'<div><span class="dd-title">{title}</span><a href="{href}">{title} division</a>' + "".join(f'<a class="sub" href="{h}">{l}</a>' for l, h in subs) + "</div>"
    return f'''<header class="site-header">
  <div class="container">
    <a class="brand" href="index.html" aria-label="Nebras Technology home">{img("brand/nebras-logo.png", "Nebras Technology")}</a>
    <nav class="nav" aria-label="Main">
      <ul>
        <li class="has-dd"><a class="{co_cls}" href="about.html">Company {CHEV}</a>
          <div class="dropdown"><a href="about.html">About us</a><a href="leadership.html">Leadership &amp; team</a><a href="milestones.html">Milestones</a></div></li>
        <li class="has-dd"><a class="{so_cls}" href="solutions.html">Solutions {CHEV}</a>
          <div class="dropdown mega">{sol}<a class="dd-all" href="solutions.html">All solutions →</a></div></li>
        {a("neoq", "Neo Q", "neoq.html")}
        {a("clients", "Clients", "clients.html")}
        {a("news", "News", "news.html")}
        {a("contact", "Contact", "contact.html")}
      </ul>
      <a class="btn btn-primary btn-sm nav-cta" href="contact.html#demo">Request a demo</a>
    </nav>
    <button class="burger" aria-label="Open menu" aria-expanded="false"><span></span></button>
  </div>
</header>'''

def footer(big_cta=False):
    cta = ""
    if big_cta:
        cta = f'''<div class="cta-big reveal">
      <div><h2>Ready to move your center<br><span class="o">into the future?</span></h2>
      <p>Talk to the team that designs, codes, installs and supports every product, all from Cairo.</p></div>
      <div class="btns"><a class="btn btn-primary" href="contact.html#demo">Request a demo {ARR_UR}</a><a class="btn btn-ghost" href="contact.html">Contact us</a></div>
    </div>'''
    socials = "".join(f'<a href="#" aria-label="{k}">{v}</a>' for k, v in SOC.items())
    return f'''<footer class="site-footer">
  <div class="container">
    {cta}
    <div class="foot-grid">
      <div>{img("brand/nebras-logo.png", "Nebras Technology")}
        <p class="about">Intelligent healthcare information systems for radiology, endoscopy and dental care. Since 2007, in 16 countries.</p>
        <div class="socials">{socials}</div></div>
      <div><h4>Radiology</h4><ul><li><a href="paxtreme.html">PaXtreme PACS</a></li><li><a href="oneris.html">OneRIS</a></li><li><a href="oneaccred.html">OneAccred</a></li><li><a href="onerad.html">OneRad</a></li><li><a href="instashare.html">InstaShare</a></li></ul></div>
      <div><h4>Endoscopy &amp; Dental</h4><ul><li><a href="endostream.html">EndoStream</a></li><li><a href="oneendo.html">OneEndo</a></li><li><a href="dentalore-cloud.html">DentaLore Cloud</a></li><li><a href="dentalore-ds.html">DentaLore DS</a></li><li><a href="neoq.html">Neo Q partnership</a></li></ul></div>
      <div><h4>Company</h4><ul><li><a href="about.html">About us</a></li><li><a href="leadership.html">Leadership &amp; team</a></li><li><a href="milestones.html">Milestones</a></li><li><a href="clients.html">Clients</a></li><li><a href="news.html">News</a></li><li><a href="contact.html">Contact</a></li></ul></div>
      <div><h4>Get in touch</h4><address><p>37 Amman St, Dokki<br>Giza, Egypt</p><p><a href="tel:+20237615212">+20 2 3761 5212</a><br><a href="mailto:info@nebrastech.com">info@nebrastech.com</a></p></address></div>
    </div>
    <div class="foot-bottom"><span>© 2026 Nebras Technology. All rights reserved.</span><span>Designed in Cairo · Built in Cairo · Used in 16 countries</span></div>
  </div>
</footer>'''

THEMES = {
    "pax":     dict(accent="#ff791a", ink="#ba6028", a="#07080a", b="#2a1608", contrast="#fff", cta="linear-gradient(135deg,#0d0d10,#07080a)"),
    "ris":     dict(accent="#6fa3ff", ink="#3f6fc7", a="#081a5c", b="#193ea8", contrast="#081a5c", cta="linear-gradient(135deg,#0c2a8a,#081a5c)"),
    "accred":  dict(accent="#2ad499", ink="#18936b", a="#03251d", b="#0a5a42", contrast="#03251d", cta="linear-gradient(135deg,#064433,#03251d)"),
    "rad":     dict(accent="#ff4d66", ink="#c23a55", a="#120409", b="#4a0a1d", contrast="#fff", cta="linear-gradient(135deg,#2e0712,#120409)"),
    "insta":   dict(accent="#45beff", ink="#2d8ac4", a="#041b44", b="#0a56a8", contrast="#041b44", cta="linear-gradient(135deg,#073a80,#041b44)"),
    "neoq":    dict(accent="#11d2d8", ink="#0f9faa", a="#032129", b="#06535d", contrast="#032129", cta="linear-gradient(135deg,#053f48,#032129)"),
    "endo":    dict(accent="#1bd0be", ink="#149a93", a="#012934", b="#06606a", contrast="#012934", cta="linear-gradient(135deg,#04505a,#012934)"),
    "oneendo": dict(accent="#a595ff", ink="#6a58e0", a="#120d3a", b="#2d2380", contrast="#120d3a", cta="linear-gradient(135deg,#251c6e,#120d3a)"),
    "cloud":   dict(accent="#ff8a1f", ink="#c0661f", a="#291204", b="#6a3108", contrast="#fff", cta="linear-gradient(135deg,#4a2006,#291204)"),
    "ds":      dict(accent="#ffc70e", ink="#b08a12", a="#201a01", b="#5a4500", contrast="#201a01", cta="linear-gradient(135deg,#3d3102,#201a01)"),
    "navy-blue":   dict(accent="#5b9aff", ink="#d96d12", a="#0a1f4d", b="#11286a", contrast="#fff", cta=""),
    "navy-teal":   dict(accent="#1bd0be", ink="#d96d12", a="#0a1f4d", b="#11286a", contrast="#fff", cta=""),
    "navy":        dict(accent="#f7841f", ink="#d96d12", a="#0a1f4d", b="#11286a", contrast="#fff", cta=""),
}

def theme_style(key):
    t = THEMES[key]
    s = f"--accent:{t['accent']};--accent-ink:{t['ink']};--hero-a:{t['a']};--hero-b:{t['b']};--accent-contrast:{t['contrast']};"
    if t["cta"]:
        s += f"--cta-bg:{t['cta']};--cta-glow:{t['accent']};"
    return s

def page(fname, title, desc, body, active="", big_cta=False, theme="navy"):
    out = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<meta name="theme-color" content="#0a1f4d">
<link rel="icon" type="image/png" href="{IMG}brand/nebras-logo.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Poppins:wght@500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/style.css">
</head>
<body style="{theme_style(theme)}">
{header(active)}
<main>
{body}
</main>
{footer(big_cta)}
<script src="assets/js/main.js"></script>
</body>
</html>
'''
    with open(os.path.join(ROOT, fname), "w", encoding="utf-8") as f:
        f.write(out)
    print("wrote", fname)

def crumbs(*items):
    parts = []
    for i, (label, href) in enumerate(items):
        if i == len(items) - 1:
            parts.append(f"<span>{label}</span>")
        else:
            parts.append(f'<a href="{href}">{label}</a>{CRUMB}')
    return f'<nav class="crumbs" aria-label="Breadcrumb">{"".join(parts)}</nav>'

def cta_box(t1, t2, text, b1="Book a live demo", b2="All solutions", b2href="solutions.html", style=""):
    st = f' style="{style}"' if style else ""
    return f'''<section class="cta-wrap"{st}><div class="container"><div class="cta-box reveal">
  <div><h2>{t1}<br><span>{t2}</span></h2><p>{text}</p></div>
  <div class="btns"><a class="btn btn-accent" href="contact.html#demo">{b1} {ARR_UR}</a><a class="btn btn-ghost" href="{b2href}">{b2}</a></div>
</div></div></section>'''

def stats(items, cls=""):
    return f'<div class="stats {cls}">' + "".join(f"<div class='stat'><b>{a}</b><span>{b}</span></div>" for a, b in items) + "</div>"

# ------------------------------------------------------------------ data
RAD_LOGOS = [f"clients/radiology-{i:02d}.{'jpg' if i >= 14 else 'png'}" for i in range(1, 19)]
ENDO_LOGOS = [f"clients/endoscopy-{i:02d}.jpg" for i in range(1, 23)]
DENT_LOGOS = [f"clients/dental-{i:02d}.{'jpg' if i >= 17 else 'png'}" for i in range(1, 24)]
SCHOOL_LOGOS = DENT_LOGOS[16:]
CLINIC_LOGOS = DENT_LOGOS[:16]

def logo_grid(logos, cls=""):
    return f'<div class="logo-grid {cls}">' + "".join(f'<div class="logo-tile">{img(l, "Client logo")}</div>' for l in logos) + "</div>"

def trusted(title, logos, cls="", bg=True, eyebrow_txt=""):
    eb = eyebrow(eyebrow_txt) if eyebrow_txt else ""
    return f'''<section class="section {'bg-alt' if bg else ''}"><div class="container">
  <div class="sec-head"><div>{eb}<h2 class="h-md">{title}</h2></div><a class="link-arrow" href="clients.html">All clients {ARR_R}</a></div>
  {logo_grid(logos, cls)}
</div></section>'''

PRODUCTS = {
    "pax": ("logos/paxtreme.png", "PaXtreme", "paxtreme.html", "g-pax"),
    "ris": ("logos/oneris.png", "OneRIS", "oneris.html", "g-ris"),
    "accred": ("logos/oneaccred.png", "OneAccred", "oneaccred.html", "g-accred"),
    "rad": ("logos/onerad.png", "OneRad", "onerad.html", "g-rad"),
    "insta": ("logos/instashare.png", "InstaShare", "instashare.html", "g-insta"),
    "endo": ("logos/endostream.png", "EndoStream", "endostream.html", "g-endo"),
    "oneendo": ("logos/oneendo.png", "OneEndo", "oneendo.html", "g-oneendo"),
    "cloud": ("logos/dentalore.png", "DentaLore Cloud", "dentalore-cloud.html", "g-cloud"),
    "ds": ("logos/dentalore-ds.png", "DentaLore DS", "dentalore-ds.html", "g-ds"),
    "hs": ("logos/dentalore-hs.png", "DentaLore HS", None, "g-hs"),
}
PROD_CARD_TEXT = {
    "pax": ("PACS", "Reliable, cost-effective PACS with desktop and web viewers."),
    "ris": ("RIS", "Scheduling, reporting, accounting and stock in one system."),
    "accred": ("Quality &amp; documentation", "Digital patient documentation, ready for GAHAR reviews."),
    "rad": ("Workstation", "Capture and reporting for cath-lab, CT, X-ray and more."),
    "insta": ("Patient reports", "Reports and images to the patient on WhatsApp and SMS."),
    "endo": ("Documentation", "Capture, report and share every endoscopy procedure."),
    "oneendo": ("Center management", "The complete endoscopy-center information system."),
    "cloud": ("Clinics", "Cloud dental practice management, from visit to invoice."),
    "ds": ("Universities", "The academic platform for dental schools and students."),
    "hs": ("Hospitals", "The newest member of the DentaLore family, for dental hospitals."),
}

def prod_card(key):
    logo, name, href, g = PRODUCTS[key]
    tag, text = PROD_CARD_TEXT[key]
    end = f'<span class="go">Explore {ARR_UR}</span>' if href else '<span class="soon">Coming 2026</span>'
    tagname = "a" if href else "div"
    hr = f' href="{href}"' if href else ""
    return f'<{tagname} class="pcard {g} reveal"{hr}>{img(logo, name, "plogo")}<span class="tag">{tag}</span><p>{text}</p>{end}</{tagname}>'

def prod_grid(keys):
    return '<div class="prod-grid">' + "".join(prod_card(k) for k in keys) + "</div>"

# device helpers
def monitor(src, alt=""):
    return f'<div class="monitor"><div class="screen">{img(src, alt)}</div></div>'

def laptop(src, alt=""):
    return f'<div class="laptop"><div class="screen">{img(src, alt)}</div></div>'

def panel(icon, caption):
    return f'<div class="panel">{ICONS[icon]}<span>{caption}</span></div>'

def shot(src, alt="", cls=""):
    return f'<div class="shot-card {cls}">{img(src, alt)}</div>'

def trio(main, s1, s2):
    return f'<div class="trio">{shot(main, "Screenshot")}<div class="side">{shot(s1, "Screenshot")}{shot(s2, "Screenshot")}</div></div>'

def file_card(compact=False):
    rows = [("Medical history", "Completed"), ("Consent form", "Digitally signed"), ("Allergy check", "Completed"), ("Safety checklist", "Completed"), ("Signature", "Verified")]
    r = "".join(f'<div class="fr"><span>{a}</span><span class="ok">✓ {b}</span></div>' for a, b in rows)
    return f'<div class="file-card"><div class="fh">{img("logos/oneaccred.png", "OneAccred")}<span>Patient file · Documentation</span></div>{r}<div class="note">⚑ Supports GAHAR quality &amp; accreditation reviews</div></div>'

# ------------------------------------------------------------------ HOME
def build_home():
    div_cards = f'''<div class="div-cards">
      <a class="div-card reveal" href="radiology.html" style="--c:#6ea2ff">{img("photos/radiology-card.jpg", "Radiologist reviewing scans")}<small>01</small><h3>Radiology</h3><p>PACS, RIS, workstations and patient delivery.</p><div class="kpi"><b>263</b>radiology clients</div></a>
      <a class="div-card reveal" href="endoscopy.html" style="--c:#1bd0be">{img("photos/endoscopy-card.jpg", "Endoscopy specialist")}<small>02</small><h3>Endoscopy</h3><p>Every procedure captured, reported and shared.</p><div class="kpi"><b>90%</b>of the Egyptian market</div></a>
      <a class="div-card reveal" href="dental.html" style="--c:#ff8a1f">{img("photos/dental-card.jpg", "Dentist with patient")}<small>03</small><h3>Dental</h3><p>From the clinic chair to the dental school.</p><div class="kpi"><b>1,200</b>clinics on the cloud</div></a>
    </div>'''
    band_items = ""
    for _ in range(4):
        band_items += '<span>Radiology</span><i>✦</i><span class="ol">Endoscopy</span><i>✦</i><span>Dental</span><i>✦</i>'
    bento = f'''<div class="bento">
      <a class="pcard g-pax span2 row2 big reveal" href="paxtreme.html">{img("logos/paxtreme.png", "PaXtreme", "plogo")}<p>Reliable, cost-effective PACS with desktop and web viewers.</p><span class="go" style="margin-top:14px;padding-top:0">Explore {ARR_UR}</span>{img("screens/paxtreme-viewer-1.jpg", "PaXtreme viewer", "shot")}</a>
      <a class="pcard g-neoq span2 reveal" href="neoq.html">{img("logos/neoq-white.png", "Neo Q", "plogo")}<p>The 30-second report. PaXtreme® and RadioReport® together.</p><span class="go">Discover {ARR_UR}</span><span class="big30">30<small>s</small></span></a>
      <a class="pcard g-ris reveal" href="oneris.html">{img("logos/oneris.png", "OneRIS", "plogo")}<p>The whole radiology center in one system.</p><span class="go">Explore {ARR_UR}</span></a>
      <a class="pcard g-insta reveal" href="instashare.html">{img("logos/instashare.png", "InstaShare", "plogo")}<p>Reports and images to the patient in one tap.</p><span class="go">Explore {ARR_UR}</span></a>
      <a class="pcard g-accred reveal" href="oneaccred.html">{img("logos/oneaccred.png", "OneAccred", "plogo")}<p>Digital documentation, ready for GAHAR.</p><span class="go">Explore {ARR_UR}</span></a>
      <a class="pcard g-rad reveal" href="onerad.html">{img("logos/onerad.png", "OneRad", "plogo")}<p>Cath-lab to ultrasound, captured beat by beat.</p><span class="go">Explore {ARR_UR}</span></a>
      <a class="pcard g-endo span2 reveal" href="endostream.html">{img("logos/endostream.png", "EndoStream", "plogo")}<p>Capture, report and share every endoscopy procedure in under a minute.</p><span class="go">Explore {ARR_UR}</span>{img("screens/endostream-capture.jpg", "EndoStream capture", "shot")}</a>
      <a class="pcard g-oneendo reveal" href="oneendo.html">{img("logos/oneendo.png", "OneEndo", "plogo")}<p>The whole endoscopy center on one clock.</p><span class="go">Explore {ARR_UR}</span></a>
      <a class="pcard g-ds reveal" href="dentalore-ds.html">{img("logos/dentalore-ds.png", "DentaLore DS", "plogo")}<p>Where future dentists learn and graduate.</p><span class="go">Explore {ARR_UR}</span></a>
      <a class="pcard g-cloud span2 reveal" href="dentalore-cloud.html">{img("logos/dentalore.png", "DentaLore Cloud", "plogo")}<p>Everything your clinic needs, in one cloud. 1,200 clinics and counting.</p><span class="go">Explore {ARR_UR}</span>{img("screens/dentalore-chart.jpg", "DentaLore Cloud dental chart", "shot")}</a>
      <div class="pcard g-hs span2 reveal">{img("logos/dentalore-hs.png", "DentaLore HS", "plogo")}<p>Dental hospitals get their own DentaLore. New in 2026.</p><span class="go">Coming soon</span><span class="big26">2026</span></div>
      <a class="pcard light span2 reveal" href="solutions.html">{eyebrow("Not sure where to start?")}<h3>Find the right combination for your center.</h3><span class="go" style="--c:var(--orange-ink)">Explore all solutions {ARR_UR}</span></a>
    </div>'''
    bars = "".join(f'<div class="row"><span>{a}</span><div class="track"><i style="width:{w}%"></i></div><b>{b}</b></div>' for a, w, b in [("Normal report", 3, "2 sec"), ("Head", 8, "30 sec"), ("Knee", 33, "&lt; 2 min"), ("Spine", 50, "&lt; 3 min"), ("Abdomen", 100, "&lt; 6 min")])
    tl = [("2007", "Nebras Technology is founded"), ("2008", "OneRIS"), ("2010", "PaXtreme PACS · Desktop"), ("2014", "DentaLore Cloud · PaXtreme Printing"), ("2018", "PaXtreme Web"), ("2023", "DentaLore DS"), ("2025", "InstaShare"), ("2026", "DentaLore DHS · The 30-second report")]
    row1 = "".join(f'<div class="logo-tile">{img(l, "Client logo", lazy=False)}</div>' for l in RAD_LOGOS)
    row2 = "".join(f'<div class="logo-tile">{img(l, "Client logo", lazy=False)}</div>' for l in SCHOOL_LOGOS + CLINIC_LOGOS[:9] + ENDO_LOGOS[:6])
    news = news_cards()
    body = f'''
<section class="home-hero">
  <div class="container">
    {eyebrow("Healthcare information systems · Since 2007")}
    <h1>Smarter software.<span class="o">Better healthcare.</span></h1>
    <div class="hero-row"><p>Intelligent systems for radiology, endoscopy and dental care, designed, coded and supported by our own teams in Cairo. Trusted by more than 1900 customers in 16 countries.</p>
      <div class="btns"><a class="btn btn-primary" href="contact.html#demo">Request a demo {ARR_UR}</a><a class="btn btn-ghost" href="solutions.html">Explore solutions</a></div></div>
    <div style="position:relative">{div_cards}<div class="pulse-line" aria-hidden="true">{img("brand/pulse-hero.png", "")}</div></div>
    {stats([("2007", "Founded in Cairo"), ("16", "Countries served"), ("1900+", "Customers today"), ("10", "Products, 3 divisions")])}
  </div>
</section>
<div class="band" aria-hidden="true"><div class="band-track">{band_items}</div></div>

<section class="section"><div class="container">
  <div class="sec-head"><div>{eyebrow("The product family")}<h2 class="h-md">Ten products.<br><span class="o">Each with its own pulse.</span></h2></div><a class="link-arrow" href="solutions.html">All solutions {ARR_R}</a></div>
  {bento}
</div></section>

<section class="section"><div class="container bignum reveal">
  <div class="num">1900<span class="o">+</span></div>
  <div><h3>customers in 16 countries trust Nebras with their radiology, endoscopy and dental operations.</h3>
    <div class="mini-stats"><div><b>263</b><span>Radiology clients</span></div><div><b>230</b><span>Endoscopy clients</span></div><div><b>1,200</b><span>Dental clinics</span></div><div><b>8</b><span>Dental schools</span></div></div></div>
</div></section>

<section class="neoq-sec"><div class="container neoq-grid">
  <div class="reveal"><div class="glow30">30</div><small>SECONDS</small></div>
  <div class="reveal">{eyebrow("Strategic partnership · Integrated with PaXtreme")}<br>{img("logos/neoq-teal.png", "Neo Q", "neoq-logo")}
    <h2>The report that<br><span>takes 30 seconds.</span></h2>
    <p>PaXtreme® and RadioReport® together: one connected workflow for images, structured reports and AI. The radiologist signs every report.</p>
    <div class="bars">{bars}</div>
    <a class="btn btn-teal" href="neoq.html" style="margin-top:28px">Discover the partnership {ARR_UR}</a></div>
</div></section>

<section class="people">{img("photos/team-development.jpg", "The Nebras team in Cairo")}
  <span class="outline-word" aria-hidden="true">CAIRO</span>
  <div class="container reveal">{eyebrow("Our people")}<h2>Designed in Cairo. Built in Cairo.<br>Used in 16 countries.</h2><a class="btn btn-ghost" href="leadership.html">Meet the team</a></div>
</section>

<section class="journey"><div class="container">
  <div class="sec-head on-dark"><div>{eyebrow("Our journey")}<h2 class="h-md">Nearly two decades,<br><span class="o">one pulse.</span></h2></div><a class="link-arrow" style="color:var(--orange)" href="milestones.html">All milestones {ARR_R}</a></div>
  <div class="timeline reveal">{"".join(f"<div><b>{y}</b><span>{t}</span></div>" for y, t in tl)}</div>
</div></section>

<section class="section"><div class="container">
  <div class="sec-head"><h2 class="h-md">Trusted by ministries,<br><span class="o">hospitals and clinics.</span></h2><a class="link-arrow" href="clients.html">All clients {ARR_R}</a></div>
</div>
  <div class="logo-marquee"><div class="track">{row1}{row1}</div><div class="track rev">{row2}{row2}</div></div>
</section>

<section class="founder">
  <div class="ph">{img("photos/ahmed-morsy.jpg", "Dr. Ahmed Morsy, Founder & CEO")}</div>
  <div class="tx reveal">{eyebrow("Founder’s message")}
    <blockquote>“Healthcare providers should spend their time on patients, not on paperwork.”</blockquote>
    <p>When I founded Nebras Technology in 2007, the idea was simple: build software that is intuitive, reliable and well supported, designed around real clinical workflows and priced with real healthcare challenges in mind.</p>
    <cite><b>Dr. Ahmed Morsy</b><span>Founder &amp; CEO · Nebras Technology</span></cite></div>
</section>

<section class="section"><div class="container">
  <div class="sec-head"><h2 class="h-md">Latest from<br><span class="o">Nebras.</span></h2><a class="link-arrow" href="news.html">All news {ARR_R}</a></div>
  {news}
</div></section>
'''
    page("index.html", "Nebras Technology · Smarter software. Better healthcare.", "Intelligent systems for radiology, endoscopy and dental care, designed, coded and supported by our own teams in Cairo. Trusted by more than 1900 customers in 16 countries.", body, big_cta=True)

def news_cards():
    items = [
        ("photos/news-alfardous-1.jpg", "Partnership · EIRC 2026", "Al Fardous Scan chooses the complete Nebras × Neo Q solution", "Signed at EIRC 2026 in Cairo, Al Fardous Scan adopts structured AI reporting together with the full Nebras system, bringing the 30-second report into daily practice."),
        ("photos/news-eirc-2.jpg", "Event · EIRC 2026", "From vision to reality: NI + AI on the EIRC stage", "Dr. Ahmed Morsy and Dr. Sven Haller showed how natural and artificial intelligence work together, with live structured reporting powered by PaXtreme and RadioReport."),
        ("screens/dentalore-queue.jpg", "Product · DentaLore Cloud", "Queue Management arrives in DentaLore", "Call patients, manage waiting queues and move visits between rooms from one screen. Available from 13 November for clinics with an active subscription."),
    ]
    return '<div class="news-grid">' + "".join(f'<article class="news-card reveal"><div class="im">{img(i, h)}</div><small>{t}</small><h3>{h}</h3><p>{p}</p></article>' for i, t, h, p in items) + "</div>"

# ------------------------------------------------------------------ ABOUT
def build_about():
    body = f'''
<section class="about-hero">{img("photos/about-hero.jpg", "Nebras leadership team")}
  <div class="container">
    {crumbs(("Home", "index.html"), ("Company", "about.html"), ("About us", ""))}
    {eyebrow("About us")}
    <h1>We build the software behind <span class="o">better healthcare.</span></h1>
    {stats([("2007", "Founded in Cairo, Egypt"), ("16", "Countries served"), ("1900+", "Customers today"), ("3", "Divisions, one workflow")])}
  </div>
</section>
<section class="section"><div class="container intro2 reveal">
  <h2>Since 2007, Nebras Technology has developed intelligent healthcare information systems that simplify daily operations, strengthen decision-making and support the full journey of patient care.</h2>
  <p>From radiology centers and endoscopy units to dental clinics, hospitals and universities, our software is built around real clinical workflows and priced with real healthcare challenges in mind.</p>
</div></section>
<section class="mv"><span class="outline-word" aria-hidden="true">MISSION</span><div class="container mv-grid reveal">
  <small>01 · Our mission</small>
  <p>To simplify healthcare operations with intuitive, reliable and affordable software, so providers spend their time on <span>patients, not on paperwork.</span></p>
</div></section>
<section class="mv dark"><span class="outline-word" aria-hidden="true">VISION</span><div class="container mv-grid reveal">
  <small>02 · Our vision</small>
  <p>To be the most trusted healthcare software partner in the region, connecting <span>images, reports and patients</span> across radiology, endoscopy and dental care.</p>
</div></section>
<section class="section"><div class="container">
  {eyebrow("What we stand for")}<h2 class="h-md" style="margin-top:18px">Four words<br><span class="o">we live by.</span></h2>
  <div class="values reveal">
    <div><h3>Intuitive.</h3><p>Easy to learn and built around real clinical workflows.</p></div>
    <div><h3>Reliable.</h3><p>Stability, accuracy and uninterrupted performance.</p></div>
    <div><h3>Supported.</h3><p>A dedicated local team committed to your success.</p></div>
    <div><h3>Scalable.</h3><p>Grows with you, priced with real-world healthcare in mind.</p></div>
  </div>
</div></section>
<section class="reach"><div class="container reach-grid">
  <div class="reveal"><div class="n16">16</div><h2>countries,<br><span>one standard of care.</span></h2><p>From the Atlantic coast of Mauritania to Papua New Guinea. One team in Cairo, one standard of software and support.</p></div>
  <div class="regions reveal">
    <div><h4>Middle East <em>07</em></h4><p>Saudi Arabia · Bahrain · Qatar · Oman · Iraq · Jordan · Palestine</p></div>
    <div><h4>Africa <em>06</em></h4><p><b>Egypt · Headquarters</b> · Sudan · Morocco · Mauritania · Kenya · Uganda</p></div>
    <div><h4>Europe &amp; Asia-Pacific <em>03</em></h4><p>Turkey · Malaysia · Papua New Guinea</p></div>
  </div>
</div></section>
<section class="section"><div class="container img-cards">
  <a class="img-card reveal" href="leadership.html">{img("photos/team-dentalore.jpg", "Nebras team at DentaLore booth")}<small>Leadership &amp; team</small><h3>The minds behind the software.</h3><span class="link-arrow">Meet the team {ARR_R}</span></a>
  <a class="img-card reveal" href="milestones.html">{img("photos/team-sales.jpg", "Nebras team at an exhibition")}<small>Milestones</small><h3>2007 to today, one pulse.</h3><span class="link-arrow">See the journey {ARR_R}</span></a>
</div></section>
{cta_box("Beside you,", "long after go-live.", "One accountable team from first meeting to go-live, and long after.")}
'''
    page("about.html", "About us · Nebras Technology", "Since 2007, Nebras Technology has developed intelligent healthcare information systems for radiology, endoscopy and dental care.", body, "company")

def build_leadership():
    heads = [("code", "Development", "Head of Development"), ("ops", "Operations", "Head of Operations"), ("sales", "Sales", "Head of Sales"), ("wrench", "Technical", "Head of Technical"), ("megaphone", "Marketing", "Head of Marketing")]
    hh = "".join(f'<div class="head reveal"><div class="box">{ICONS[i]}<em>Photo</em></div><small>{s}</small><b>{t}</b><span>Name &amp; photo to be added</span></div>' for i, s, t in heads)
    body = f'''
<section class="page-hero grid-bg"><span class="outline-word" aria-hidden="true">PEOPLE</span>
  <div class="container">
    {crumbs(("Home", "index.html"), ("Company", "about.html"), ("Leadership &amp; team", ""))}
    {eyebrow("Leadership &amp; team")}
    <h1 class="h-lg">The minds behind<br><span class="o">the software.</span></h1>
    <p class="lead">Every product is designed, coded and supported by our own teams in Cairo. No outsourcing, no distance.</p>
  </div>
</section>
<section class="section"><div class="container">
  <div class="leader reveal">
    <figure class="lph">{img("photos/ahmed-morsy.jpg", "Dr. Ahmed Morsy")}<figcaption><small>Founder &amp; CEO</small><b>Dr. Ahmed Morsy</b></figcaption></figure>
    <div><span class="q">“</span><blockquote>Healthcare providers should spend their time on patients, not on paperwork and complicated systems.</blockquote><p>Today, more than 1900 customers in 16 countries trust us with their radiology, endoscopy and dental operations. That trust is the standard we hold ourselves to every day.</p></div>
  </div>
  <div class="leader rev reveal">
    <figure class="lph">{img("photos/hany-hussein.jpg", "Eng. Hany Hussein")}<figcaption><small>Co-founder &amp; General Manager</small><b>Eng. Hany Hussein</b></figcaption></figure>
    <div><span class="q">“</span><blockquote>Great software is the kind you barely notice. It simply gives clinicians their time back.</blockquote><p>Behind every installation is a team that listens, delivers locally and stays beside our customers long after go-live. That is how we earn trust, one center at a time.</p></div>
  </div>
</div></section>
<section class="section on-dark" style="background:var(--navy-900)"><div class="container">
  {eyebrow("Top management")}<h2 class="h-md" style="margin-top:18px">Five teams.<br><span class="o">One accountable leadership.</span></h2>
  <div class="heads">{hh}</div>
</div></section>
<section class="section" data-carousel><div class="container">
  <div class="carousel-head"><div>{eyebrow("Our people")}<h2 class="h-md">Every team,<br><span class="o">one Nebras.</span></h2></div>
    <div class="car-btns"><button data-prev aria-label="Previous">{ARR_L}</button><button data-next aria-label="Next">{ARR_R}</button></div></div>
  <div class="car-track">
    <div class="team-card">{img("photos/team-management.jpg", "Management team")}<small>Management team</small><p>One accountable team, from the first meeting to go-live and long after.</p></div>
    <div class="team-card">{img("photos/team-development.jpg", "Development team")}<small>Development team</small><p>Every feature starts with a real clinical problem. We write the code that turns it into a calmer day.</p></div>
    <div class="team-card">{img("photos/team-sales.jpg", "Sales team")}<small>Sales team</small><p>Every proposal starts with your workflow and your goals.</p></div>
    <div class="team-card">{img("photos/ai-department.jpg", "AI department")}<small>AI department</small><p>We teach software to see what matters, so radiologists report faster and patients hear sooner.</p></div>
  </div>
</div></section>
{cta_box("Work with the people", "who build it.", "One accountable team from first meeting to go-live, and long after.")}
'''
    page("leadership.html", "Leadership & team · Nebras Technology", "Every Nebras product is designed, coded and supported by our own teams in Cairo.", body, "company")

def chip(logo, bg="#0b0b0e"):
    return f'<span style="background:{bg}">{img(logo, "")}</span>'

def build_milestones():
    rows = [
        ("2007", "photos/ahmed-morsy.jpg", "Nebras Technology is founded", "Three products from day one: EndoStream, OneRad and DentaLore Desktop.", [chip("logos/endostream.png", "#0b5a5e"), chip("logos/onerad.png", "#4a0a1d"), chip("logos/dentalore.png", "#4a2006")], ""),
        ("2008", None, "OneRIS", "Scheduling, reporting, billing and stock. The whole radiology center in one system.", [chip("logos/oneris.png", "#13309a")], ""),
        ("2010", "screens/paxtreme-viewer-2.jpg", "PaXtreme PACS · Desktop", "Our PACS and desktop diagnostic viewer for imaging centers.", [chip("logos/paxtreme.png")], ""),
        ("2014", "screens/dentalore-chart.jpg", "DentaLore Cloud · PaXtreme Printing", "Dental practice management moves to the cloud; smart film and paper printing for radiology.", [chip("logos/dentalore.png", "#4a2006"), chip("logos/paxtreme.png")], "contain"),
        ("2018", "screens/paxtreme-worklist.jpg", "PaXtreme Web", "A web viewer to read every study from any browser, anywhere.", [chip("logos/paxtreme.png")], ""),
        ("2023", "photos/dental-school-clinic.jpg", "DentaLore DS", "Academic Dental Solutions for dental universities.", [chip("logos/dentalore-ds.png", "#3a3005")], ""),
        ("2025", "screens/instashare-dashboard.jpg", "InstaShare", "Reports and images go to the patient on WhatsApp and SMS.", [chip("logos/instashare.png", "#0c4fa6")], "contain"),
        ("2026", "photos/news-alfardous-1.jpg", "DentaLore DHS · The 30-second report", "The newest member of the DentaLore family, and RadioReport® by Neo Q integrated with PaXtreme.", [chip("logos/dentalore.png", "#4a2006"), chip("logos/neoq-white.png", "#032129")], ""),
    ]
    out = ""
    for i, (y, im, t, d, chips, cls) in enumerate(rows):
        rev = " rev" if i % 2 else ""
        now = " now" if y == "2026" else ""
        imh = f'<div class="vim {cls}">{img(im, t)}</div>' if im else ""
        if y == "2007":
            imh = f'<div class="vim" style="aspect-ratio:16/10">{img(im, t, extra=chr(32) + "style=" + chr(34) + "object-position:center 15%" + chr(34))}</div>'
        out += f'<div class="vrow{rev}{now} reveal"><div class="vyear">{y}</div><div class="vcard">{imh}<h3>{t}</h3><p>{d}</p><div class="vchips">{"".join(chips)}</div></div></div>'
    body = f'''
<section class="page-hero grid-bg"><div class="container">
  {crumbs(("Home", "index.html"), ("Company", "about.html"), ("Milestones", ""))}
  <div class="ms-hero-years"><span>2007</span>{img("brand/pulse-milestones.png", "")}<span class="o">2026</span></div>
  <div style="margin-top:26px">{eyebrow("Milestones")}</div>
  <h1 class="h-lg" style="margin-top:14px">Nearly two decades,<br><span class="o">one pulse.</span></h1>
  <p class="lead">From three products in 2007 to ten products, three divisions and 1900+ customers in 16 countries.</p>
</div></section>
<section class="section"><div class="container"><div class="vtl">{out}</div>
  <div class="today reveal"><small>TODAY</small><h2>Since 2007 · 16 countries · 1900+ customers</h2></div>
</div></section>
{cta_box("Write the next", "chapter with us.", "Tell us about your center and see where Nebras fits.")}
'''
    page("milestones.html", "Milestones · Nebras Technology", "From three products in 2007 to ten products, three divisions and 1900+ customers in 16 countries.", body, "company")

def build_solutions():
    def block(num, label, h, sub, link, linkhref, keys, alt=False):
        return f'''<section class="section {'bg-alt' if alt else ''}"><div class="container">
  <div class="sec-head"><div>{eyebrow(f"{num} · {label}")}<h2 class="h-md">{h}<br><span class="o">{sub}</span></h2></div><a class="link-arrow" href="{linkhref}">{link} {ARR_R}</a></div>
  {prod_grid(keys)}
</div></section>'''
    body = f'''
<section class="page-hero grid-bg"><span class="outline-word" aria-hidden="true">SOLUTIONS</span><div class="container">
  {crumbs(("Home", "index.html"), ("Solutions", ""))}
  {eyebrow("Ten products · Three divisions")}
  <h1 class="h-lg">One family.<br><span class="o">Ten brands.</span></h1>
  <p class="lead">Built in Cairo and trusted in 16 countries. Every product shares the same engineering team, the same support and the same standard.</p>
</div></section>
{block("01", "Radiology", "See further.", "Report faster. Care sooner.", "Radiology division", "radiology.html", ["pax", "ris", "accred", "rad", "insta"])}
{block("02", "Endoscopy", "Every procedure captured,", "reported and shared.", "Endoscopy division", "endoscopy.html", ["endo", "oneendo"], True)}
{block("03", "Dental", "From the clinic chair", "to the dental school.", "Dental division", "dental.html", ["cloud", "ds", "hs"])}
{cta_box("Not sure where", "to start?", "Tell us about your center and we will recommend the right combination.")}
'''
    page("solutions.html", "Solutions · Nebras Technology", "Ten products across radiology, endoscopy and dental care. One family, ten brands.", body, "solutions")

# ------------------------------------------------------------------ DIVISIONS
def division(fname, theme, crumb, eb, h1a, h1b, lead, photo, statsl, outline, prodtitle, keys, extra, trust_title, logos, logo_cls, cta_name, title, desc):
    body = f'''
<section class="page-hero" style="padding-bottom:0">
  {img(photo, "", extra=' style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover;opacity:.35;z-index:0"')}
  <div style="position:absolute;inset:0;background:linear-gradient(90deg,rgba(10,31,77,.96) 35%,rgba(10,31,77,.55));z-index:1"></div>
  <span class="outline-word" aria-hidden="true" style="z-index:1;bottom:-.12em">{outline}</span>
  <div class="container">
    {crumbs(("Home", "index.html"), ("Solutions", "solutions.html"), (crumb, ""))}
    {eyebrow(eb)}
    <h1 class="h-lg" style="max-width:820px">{h1a}<br><span class="accent">{h1b}</span></h1>
    <p class="lead">{lead}</p>
    <a class="btn btn-primary" href="contact.html#demo" style="margin-top:30px">Request a demo {ARR_UR}</a>
    {stats(statsl, "three")}
    <div style="height:120px"></div>
  </div>
</section>
<section class="section"><div class="container">
  {eyebrow("Products", "o")}<h2 class="h-md" style="margin:18px 0 40px">{prodtitle}</h2>
  {prod_grid(keys)}
</div></section>
{extra}
{trusted(trust_title, logos, logo_cls)}
<div style="height:100px"></div>
{cta_box(f"See {cta_name}", "in action.", "A live walkthrough with our specialists, built around your own workflow.", style="--accent:var(--orange);--accent-contrast:#fff")}
'''
    page(fname, title, desc, body, "solutions", theme=theme)

def build_divisions():
    neoq_strip = f'''<section style="background:radial-gradient(ellipse at 0% 100%,#06535d,transparent 50%),#032129;padding:44px 0"><div class="container" style="display:flex;align-items:center;gap:30px;flex-wrap:wrap;justify-content:space-between">
  <div style="display:flex;align-items:center;gap:30px;flex-wrap:wrap">{img("logos/neoq-teal.png", "Neo Q", extra=' style="height:28px;width:auto"')}
  <div><h3 style="color:#fff;font-size:22px">The 30-second report</h3><p style="color:rgba(255,255,255,.7);font-size:13.5px;margin-top:4px">PaXtreme® integrated with RadioReport® by Neo Q: structured reporting and AI in one workflow.</p></div></div>
  <a class="btn btn-ghost btn-sm" href="neoq.html">Discover the partnership</a></div></section>'''
    division("radiology.html", "navy-blue", "Radiology", "01 · Radiology division", "See further.", "Report faster. Care sooner.",
             "Imaging, reporting, practice management and patient delivery: one connected suite for radiology centers and hospitals.",
             "photos/radiology-hero.jpg", [("263", "Radiology clients"), ("5", "Connected products"), ("24/7", "Tele-radiology reading")], "RADIOLOGY",
             "Radiology solutions", ["pax", "ris", "accred", "rad", "insta"], neoq_strip, "Trusted in radiology", RAD_LOGOS, "", "radiology",
             "Radiology · Nebras Technology", "PACS, RIS, workstations and patient delivery: one connected suite for radiology centers and hospitals.")
    division("endoscopy.html", "navy-teal", "Endoscopy", "02 · Endoscopy division", "Every procedure captured,", "reported and shared.",
             "Egypt’s pioneer in endoscopy documentation, from university hospitals to private groups in Malaysia, Qatar and Oman.",
             "photos/endoscopy-hero.jpg", [("90%", "of the Egyptian endoscopy market"), ("230", "Endoscopy clients"), ("60 s", "From last image to report")], "ENDOSCOPY",
             "Endoscopy solutions", ["endo", "oneendo"], "", "Trusted in endoscopy", ENDO_LOGOS, "endo", "endoscopy",
             "Endoscopy · Nebras Technology", "Egypt’s pioneer in endoscopy documentation. Every procedure captured, reported and shared.")
    division("dental.html", "navy", "Dental", "03 · Dental division", "From the clinic chair", "to the dental school.",
             "Practice management for clinics, an academic platform for universities and, new in 2026, a solution for dental hospitals.",
             "photos/dental-hero.jpg", [("1,200", "Clinics on DentaLore Cloud"), ("8", "Dental schools"), ("7,900+", "Students on DentaLore DS")], "DENTAL",
             "Dental solutions", ["cloud", "ds", "hs"], "", "Trusted in dental", DENT_LOGOS, "", "dental",
             "Dental · Nebras Technology", "Practice management for clinics, an academic platform for universities and a solution for dental hospitals.")

# ------------------------------------------------------------------ PRODUCT PAGES
DEV = ("photos/team-development.jpg", "Development team", "Every feature starts with a real clinical problem. We write the code that turns it into a calmer day.")
AI = ("photos/ai-department.jpg", "AI department", "We teach software to see what matters, so radiologists report faster and patients hear sooner.")
SALES = ("photos/team-sales.jpg", "Sales team", "Every proposal starts with your workflow and your goals.")

def feature(i, f):
    rev = " rev" if i % 2 else ""
    pts = "".join(f"<div><b>{a}</b><span>{b}</span></div>" for a, b in f["points"])
    return f'''<div class="feature{rev} reveal" id="f{i+1}">
  <div class="f-media">{f["media"]}</div>
  <div><div class="f-label"><span class="num-dot">{i+1:02d}</span>{f["label"]}</div>
    <h3>{f["t1"]}<br><span>{f["t2"]}</span></h3><p class="desc">{f["desc"]}</p><div class="f-points">{pts}</div></div>
</div>'''

def product_page(d):
    chips = ""
    for pos, (b, s) in d["chips"].items():
        chips += f'<div class="chip {pos}"><b>{b}</b><span>{s}</span></div>'
    glance_vis = d.get("glance_visual")
    if glance_vis:
        glance = f'<div class="glance"><div>{eyebrow("At a glance")}<h3>{d["glance"]}</h3><div class="tags">{"".join(f"<span>{t}</span>" for t in d["tags"])}</div></div><div>{glance_vis}</div></div>'
    else:
        glance = f'<div style="max-width:760px">{eyebrow("At a glance")}<h3 style="font-size:clamp(18px,1.7vw,22px);font-weight:500;line-height:1.4;margin:16px 0 22px">{d["glance"]}</h3><div class="tags">{"".join(f"<span>{t}</span>" for t in d["tags"])}</div></div>'
    pills = "".join(f'<a href="#f{i+1}"><span class="num-dot">{i+1:02d}</span>{f["pill"]}</a>' for i, f in enumerate(d["features"]))
    feats = "".join(feature(i, f) for i, f in enumerate(d["features"]))
    team = "".join(f'<div class="team-card">{img(a, b)}<small>{b}</small><p>{c}</p></div>' for a, b, c in d["team"])
    why = "".join(f"<li><i>{i+1:02d}</i>{t}</li>" for i, t in enumerate(d["why"]))
    body = f'''
<section class="p-hero"><span class="outline-word" aria-hidden="true">{d["outline"]}</span><div class="container">
  {crumbs(("Home", "index.html"), ("Solutions", "solutions.html"), d["div"], (d["name"], ""))}
  <div class="p-hero-grid">
    <div>{img(d["logo"], d["name"], "plogo")}{eyebrow(d["eyebrow"])}
      <h1>{d["h1a"]} <span class="accent">{d["h1b"]}</span></h1>
      <p class="lead">{d["lead"]}</p>
      <div class="btns"><a class="btn btn-accent" href="contact.html#demo">Request a demo {ARR_UR}</a><a class="btn btn-ghost" href="contact.html">Download brochure</a></div></div>
    <div class="p-visual reveal">{d["hero_visual"]}{chips}</div>
  </div>
</div></section>
<section class="section"><div class="container reveal">{glance}</div></section>
<section class="section bg-alt" id="inside"><div class="container">
  <div class="inside-head"><h2 class="h-md">Inside {d["name"]}</h2><div class="pills">{pills}</div></div>
  {feats}
</div></section>
<section class="statement"><span class="outline-word" aria-hidden="true">{d["outline"]}</span><div class="container reveal"><h2>{d["statement"]}</h2></div></section>
{d.get("extra", "")}
<section class="section" data-carousel><div class="container">
  <div class="carousel-head"><div>{eyebrow(d.get("team_eyebrow", "The team behind " + d["name"]))}<h2 class="h-md">{d.get("team_title", "People who build<br><span class='accent-ink'>and support it.</span>")}</h2></div>
    <div class="car-btns"><button data-prev aria-label="Previous">{ARR_L}</button><button data-next aria-label="Next">{ARR_R}</button></div></div>
  <div class="car-track">{team}</div>
</div></section>
<section class="section" style="padding-top:20px"><div class="container why reveal">
  <div>{eyebrow("Why " + d.get("why_name", d["name"]))}<h2 class="h-md" style="margin-top:16px">{d["why_title"]}</h2></div>
  <ol>{why}</ol>
</div></section>
{trusted("Trusted by leading centers", d["logos"], d.get("logo_cls", ""))}
<div style="height:100px" class="bg-alt"></div>
{cta_box("See " + d["name"], "in action.", "Book a live walkthrough with our specialists, built around your own workflow.")}
'''
    page(d["file"], d["title"], d["desc"], body, "solutions", theme=d["theme"])

RADIO_DIV = ("Radiology", "radiology.html")
ENDO_DIV = ("Endoscopy", "endoscopy.html")
DENT_DIV = ("Dental", "dental.html")

def build_products():
    product_page(dict(
        file="paxtreme.html", theme="pax", name="PaXtreme", logo="logos/paxtreme.png", div=RADIO_DIV, outline="PACS",
        title="PaXtreme PACS · Nebras Technology", desc="A scalable, reliable and easy-to-use PACS built to fit the way your center already works.",
        eyebrow="Radiology · PACS", h1a="Reliable, cost-effective PACS", h1b="that fits your workflow.",
        lead="A scalable, reliable and easy-to-use PACS built to fit the way your center already works. Go filmless and raise productivity, profitability and the quality of patient service.",
        hero_visual=monitor("screens/paxtreme-viewer-2.jpg", "PaXtreme viewer"), chips={"tr": ("24/7", "tele-radiology"), "bl": ("263", "radiology clients")},
        glance="Full diagnostic power on the radiologist’s workstation with PaXtreme VU, and every study in any browser with PaXtreme Web. One archive, smart storage and built-in reporting.",
        tags=["MPR · 3D · Fusion", "Smart worklist", "PaXtreme VU", "PaXtreme Web", "RIS, EMR &amp; HIS ready", "Tele-radiology"],
        glance_visual=trio("screens/paxtreme-viewer-3.jpg", "screens/paxtreme-viewer-4.jpg", "screens/paxtreme-worklist-small.jpg"),
        features=[
            dict(pill="For the radiologist", label="For the radiologist", t1="Everything the", t2="radiologist needs.", desc="Compare series, measure, reconstruct and print without leaving the viewer.",
                 points=[("Viewing tools", "Compare series, scroll multi-frame studies, presets, magnify, rotate and flip."), ("Measure &amp; annotate", "Distance, area, angle and density, with text, arrows and circles."), ("3D &amp; MPR", "Real-time 3D reconstruction with cropping and built-in presets."), ("Print &amp; share", "Film-style printing, CD export, import and compare with history.")],
                 media=monitor("screens/paxtreme-viewer-1.jpg", "PaXtreme viewer")),
            dict(pill="For the center", label="For the center", t1="Control, storage and", t2="reporting, simplified.", desc="Administration, storage and reporting that run quietly in the background.",
                 points=[("Easy administration", "Manage work queues and patients, review the activity log and monitor remotely."), ("Smart storage", "Storage tiers that balance themselves, so images stay fast and safe."), ("Study handling", "Automatic routing and reconciliation of studies, with secure user access."), ("Reporting built in", "Typed, approved, finalized. Use Word or the built-in module.")],
                 media=laptop("screens/paxtreme-worklist-small.jpg", "PaXtreme worklist")),
            dict(pill="Two viewers", label="Two viewers", t1="Desktop power.", t2="Browser freedom.", desc="The same archive behind two viewers, so every radiologist reads the way they prefer.",
                 points=[("PaXtreme VU", "Full diagnostic power on the radiologist’s workstation."), ("PaXtreme Web", "Read every study from any browser, anywhere, with no workstation lock-in.")],
                 media=monitor("screens/paxtreme-worklist.jpg", "PaXtreme Web worklist")),
            dict(pill="Tele-radiology", label="Tele-radiology", t1="One worklist.", t2="Read around the clock.", desc="Studies from every site land in one PaXtreme Web worklist, and readers across time zones pick them up day and night.",
                 points=[("Read from anywhere", "Home, hospital or another continent: the same study, the same tools."), ("Around the clock", "Readers in different time zones keep the worklist moving 24/7."), ("Many sites, one standard", "Clinics and hospitals share one radiology team and one quality bar.")],
                 media=monitor("screens/paxtreme-viewer-3.jpg", "PaXtreme viewer")),
            dict(pill="AI-ready", label="AI-ready", t1="Guided today.", t2="AI when you are.", desc="PaXtreme connects with RadioReport® by Neo Q for structured reporting and the 30-second report.",
                 points=[("Structured reporting", "Guided templates with ICD coding in the same workflow."), ("Error checks", "Side, gender, referral and missing-organ checks as you report.")],
                 media=monitor("screens/paxtreme-viewer-4.jpg", "PaXtreme viewer")),
        ],
        statement='The future of radiology everywhere in the world <span>is tele-radiology.</span>',
        team=[DEV, AI], why_title='A filmless center,<br><span class="accent-ink">from day one.</span>',
        why=["Replace hard-copy images with unlimited digital storage", "Improve report quality", "Customize your interface and layout", "Better diagnosis, better patient outcomes", "Access images from several sites at once", "Prioritize exams with smart worklists", "Connects with your RIS, EMR and HIS"],
        logos=RAD_LOGOS))

    product_page(dict(
        file="oneris.html", theme="ris", name="OneRIS", logo="logos/oneris.png", div=RADIO_DIV, outline="RIS",
        title="OneRIS · Nebras Technology", desc="Scheduling, reporting, accounting, inventory and analytics: the whole radiology center in one system, since 2008.",
        eyebrow="Radiology · RIS", h1a="One platform for every", h1b="radiology-center operation.",
        lead="Scheduling, reporting, accounting, inventory and analytics: the whole radiology center in one system, since 2008.",
        hero_visual=monitor("screens/oneris-schedule.jpg", "OneRIS schedule"), chips={"tr": ("2008", "in daily use since"), "bl": ("6", "modules, one system")},
        glance="OneRIS runs the front desk, the reporting room and the back office together, so every exam, invoice and stock item is tracked from booking to final report.",
        tags=["Smart schedule", "Reporting workflow", "Accounting &amp; insurance", "Inventory", "Sales", "Statistics"],
        glance_visual=trio("screens/oneris-reporting.jpg", "screens/oneris-accounting.jpg", "screens/oneris-inventory.jpg"),
        features=[
            dict(pill="Scheduling", label="Scheduling", t1="Every exam,", t2="color-coded.", desc="See the whole day at a glance and keep every room moving.",
                 points=[("Exam status", "Color-coded status, shared notes and attached documents."), ("Receipts", "Printed receipts straight from the booking.")], media=monitor("screens/oneris-schedule.jpg", "OneRIS schedule")),
            dict(pill="Reporting", label="Reporting", t1="From typing", t2="to approval.", desc="Word templates, automatic patient data and signatures in one flow.",
                 points=[("Templates", "Word templates filled with patient data automatically."), ("Signatures", "Typing, review and approval tracked for every report.")], media=monitor("screens/oneris-reporting.jpg", "OneRIS reporting")),
            dict(pill="Accounting &amp; insurance", label="Accounting &amp; insurance", t1="Money in, money out,", t2="in one place.", desc="Payments, expenses, salaries, insurance and patient invoices together.",
                 points=[("Total in · total out", "A live balance for the whole center."), ("Insurance", "Claims and patient shares handled side by side.")], media=laptop("screens/oneris-accounting.jpg", "OneRIS accounting")),
            dict(pill="Inventory &amp; sales", label="Inventory &amp; sales", t1="Never short.", t2="Always informed.", desc="Stock, referrals and staff commissions tracked without spreadsheets.",
                 points=[("Inventory", "Stock and target levels, one-click orders and purchase-order tracking."), ("Sales", "Each referring physician’s cases, filtered by sales rep."), ("Statistics", "Financial balance, commissions and exam activity at a glance.")], media=monitor("screens/oneris-inventory.jpg", "OneRIS inventory")),
        ],
        statement='Run a smarter, <span>more profitable center.</span>', team=[DEV, AI],
        why_title='Less admin.<br><span class="accent-ink">More patients.</span>',
        why=["Run far more efficiently than with paper", "Improve the quality of patient care", "Save costs and boost revenues", "Make every financial transaction easier to manage", "Produce and manage high-quality analytics"],
        logos=RAD_LOGOS))

    product_page(dict(
        file="oneaccred.html", theme="accred", name="OneAccred", logo="logos/oneaccred.png", div=RADIO_DIV, outline="QUALITY",
        title="OneAccred · Nebras Technology", desc="OneAccred turns patient documentation into a secure, digital workflow inside OneRIS.",
        eyebrow="Radiology · Quality &amp; documentation", h1a="Less paper.", h1b="More digital.",
        lead="OneAccred turns patient documentation into a secure, digital workflow inside OneRIS. Every patient has a history, and every detail matters.",
        hero_visual=file_card(), chips={"tr": ("0", "paper files"), "bl": ("GAHAR", "review-ready")},
        glance="Histories, allergies, consents and safety checks recorded digitally, traceable for any inquiry and ready for accreditation reviews.",
        tags=["Patient safety", "Facility protection", "Patient rights", "Quality ready", "Less paperwork", "RIS integrated"],
        features=[
            dict(pill="Safety", label="Safety", t1="Smarter documentation.", t2="Safer patient care.", desc="Each patient file carries its history, allergies and safety checks before the exam begins.",
                 points=[("Patient safety", "Histories, allergies and safety checks."), ("Facility protection", "Reliable records for any inquiry."), ("Patient rights", "Consents organized and always traceable.")], media=file_card()),
            dict(pill="Accreditation", label="Accreditation", t1="Accreditation-ready,", t2="always.", desc="Documents prepared for GAHAR quality and accreditation reviews, inside the radiology workflow.",
                 points=[("Quality ready", "Documents ready for reviews and GAHAR."), ("Less paperwork", "Faster access, less physical storage."), ("RIS integrated", "Built into the OneRIS workflow.")], media=panel("shield", "GAHAR · General Authority for Healthcare Accreditation and Regulation")),
        ],
        statement='Every detail documented.<br><span>Every patient matters.</span>', team=[DEV, AI],
        why_title='Quality you can<br><span class="accent-ink">prove.</span>',
        why=["Digital consents and signatures", "Allergy and safety checks before every exam", "Traceable records for any inquiry", "Ready for GAHAR reviews", "Built into OneRIS"],
        logos=RAD_LOGOS))

    product_page(dict(
        file="onerad.html", theme="rad", name="OneRad", logo="logos/onerad.png", div=RADIO_DIV, outline="BEAT",
        title="OneRad · Nebras Technology", desc="OneRad captures, reports and archives procedures from the cath-lab to ultrasound.",
        eyebrow="Radiology · Workstation", h1a="Radiology &amp; cardiology,", h1b="captured beat by beat.",
        lead="OneRad captures, reports and archives procedures from the cath-lab to ultrasound, with up to three hours of recording per procedure.",
        hero_visual=f'<div class="ecg-card">{img("screens/onerad-ecg.png", "ECG trace")}<small>● REC · UP TO 3 HOURS PER PROCEDURE</small></div>',
        chips={"tr": ("5", "modalities"), "bl": ("3 h", "recording per procedure")},
        glance="Video input and foot-switch control, on-the-fly reports from templates and a DICOM gateway that keeps everything connected.",
        tags=["Cath-lab", "CT", "X-ray", "Ultrasound", "Angiography"],
        features=[
            dict(pill="Capture", label="Capture", t1="Capture without", t2="leaving the patient.", desc="Video input and foot-switch control keep hands on the procedure.",
                 points=[("Capture", "Video input and foot-switch control."), ("Report", "On-the-fly reports from templates.")], media=panel("video", "Video input · Foot switch")),
            dict(pill="Share &amp; connect", label="Share &amp; connect", t1="One click to CD.", t2="One gateway to PACS.", desc="Burn studies with the viewer included, and route everything through DICOM.",
                 points=[("CD / DVD", "One click, with the viewer included."), ("DICOM gateway", "Worklist, store and print, with backup.")], media=panel("disc", "CD / DVD · DICOM gateway")),
        ],
        statement='Every beat, every frame, <span>documented.</span>', team=[DEV, AI],
        why_title='Built for the<br><span class="accent-ink">procedure room.</span>',
        why=["Up to 3 hours of recording per procedure", "Foot-switch control", "Reports from templates", "CD and DVD with viewer", "DICOM worklist, store and print"],
        logos=RAD_LOGOS))

    product_page(dict(
        file="instashare.html", theme="insta", name="InstaShare", logo="logos/instashare.png", div=RADIO_DIV, outline="SHARE",
        title="InstaShare · Nebras Technology", desc="Report and images reach the patient the moment the doctor finishes, on WhatsApp or SMS.",
        eyebrow="Radiology · Patient reports", h1a="From film envelopes", h1b="to one tap.",
        lead="Report and images reach the patient the moment the doctor finishes: matched, reviewed and sent on WhatsApp or SMS from one dashboard.",
        hero_visual=laptop("screens/instashare-dashboard.jpg", "InstaShare dashboard"), chips={"tr": ("1", "tap to send"), "bl": ("0", "films, CDs or return visits")},
        glance="A digital booklet in the patient’s pocket: the report, sharp scrollable images and one secure link for the referring physician.",
        tags=["WhatsApp &amp; SMS", "Secure link", "HD scans", "Share with the doctor", "Paper-free", "Orders dashboard"],
        glance_visual=f'<div class="trio">{shot("screens/instashare-scans.jpg", "HD scans")}<div class="side">{shot("screens/instashare-report.jpg", "Report", "light")}{shot("screens/instashare-dashboard.jpg", "Dashboard", "light")}</div></div>',
        features=[
            dict(pill="Match", label="Match", t1="Right report,", t2="right patient.", desc="Report and images are paired with the right patient record before anything leaves the center.",
                 points=[("Match", "Report and images paired with the right patient record."), ("Review", "Name, ID and date checked side by side.")], media=laptop("screens/instashare-dashboard.jpg", "InstaShare dashboard")),
            dict(pill="Send", label="Send", t1="Delivered the moment", t2="it’s ready.", desc="WhatsApp or SMS, one click from the dashboard.",
                 points=[("Send", "WhatsApp or SMS, one click from the dashboard."), ("Secure link", "Private access for the patient.")], media=shot("screens/instashare-scans.jpg", "HD scans")),
            dict(pill="Digital booklet", label="Digital booklet", t1="Everything the patient needs,", t2="in their pocket.", desc="The patient opens the report and HD images on their phone, and shares one link with their doctor.",
                 points=[("HD scans", "Sharp and scrollable."), ("Share with the doctor", "One link for the referring physician."), ("Paper-free", "No film, ink or envelopes.")],
                 media=f'<div style="max-width:300px;margin:0 auto">{shot("screens/instashare-report.jpg", "Digital report", "light")}</div>'),
        ],
        statement='Print films, burn a CD, pack the envelope, wait, come back. <span>Not anymore.</span>', team=[DEV, AI],
        why_title='Three steps.<br><span class="accent-ink">Zero mismatches.</span>',
        why=["Zero films printed", "Zero CDs burned", "Zero return visits", "Zero mismatches with three-step checks", "Patients served the moment the report is signed"],
        logos=RAD_LOGOS))

    sheets = '<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:10px;align-items:start">' + "".join(
        f'<div class="shot-card light" style="margin-top:{m}px">{img(f"screens/endostream-sheet-{n}.jpg", "Procedure report")}</div>' for n, m in [(1, 0), (2, 24), (3, 0), (4, 24)]) + "</div>"
    product_page(dict(
        file="endostream.html", theme="endo", name="EndoStream", logo="logos/endostream.png", div=ENDO_DIV, outline="SCOPE",
        title="EndoStream · Nebras Technology", desc="An endoscopy data management & documentation workstation. Capture everything, report in under a minute and share in one click.",
        eyebrow="Endoscopy · Documentation", h1a="An endoscopy data management &amp;", h1b="documentation workstation.",
        lead="EndoStream manages the endoscopy unit from the patient file to the final report. Capture everything, report in under a minute and share in one click.",
        hero_visual=monitor("screens/endostream-capture.jpg", "EndoStream capture"), chips={"tr": ("60 s", "last image to report"), "bl": ("90%", "of the Egyptian market")},
        glance="High-quality images and video from every endoscopy device, branded reports for every procedure, and an archive that connects to your PACS and HIS.",
        tags=["Patient management", "Image &amp; video capture", "Procedure reports", "Statistics &amp; insight", "ERCP &amp; EUS", "HIS / PACS integration"],
        glance_visual=trio("screens/endostream-report.jpg", "screens/endostream-video.jpg", "screens/endostream-archive.jpg"),
        features=[
            dict(pill="Capture", label="Capture", t1="Capture everything.", t2="Miss nothing.", desc="Images and video from every endoscopy device, by foot switch or scope buttons.",
                 points=[("Capture everything", "High-quality images and video. ERCP and EUS supported."), ("Annotate &amp; explain", "Text and arrow annotation, voice memos for images and videos.")], media=monitor("screens/endostream-capture.jpg", "EndoStream capture")),
            dict(pill="Report", label="Report", t1="Capture. Report.", t2="Done in under a minute.", desc="Point-and-click, on-the-fly reports from pre-entered text, with unlimited template designs.",
                 points=[("Reports in 60 seconds", "From the last image to a finished, branded report."), ("Images go straight in", "Drop images and video frames into the report layout.")], media=monitor("screens/endostream-report.jpg", "EndoStream report")),
            dict(pill="Every procedure", label="Every procedure", t1="A complete reporting system", t2="for every procedure.", desc="Branded with your center’s identity, printed or shared digitally.",
                 points=[("Bronchoscopy", "Every segment documented, with key frames beside the findings."), ("Upper GI", "Anatomy diagram and captured frames, ready to print or share."), ("Upper endoscopy", "Findings, conclusion and up to six images on one page."), ("Sigmoidoscopy", "Indications, instrument and illustrated findings.")], media=sheets),
            dict(pill="Share &amp; measure", label="Share &amp; measure", t1="Endoscopy is no", t2="longer isolated.", desc="Archive, search, share and measure every case in the unit.",
                 points=[("Share in one click", "Send to PACS or e-mail, burn a CD with its viewer, or create a PowerPoint."), ("Connected", "HIS / EIS integration: reports flow in, no double entry."), ("Know your numbers", "Age, indications, diagnoses, scopes used and each physician’s monthly cases.")], media=monitor("screens/endostream-stats.jpg", "EndoStream statistics")),
        ],
        statement='Prepare any report<br><span>in under 60 seconds.</span>', team=[DEV, SALES],
        why_title='Why endoscopy centers<br><span class="accent-ink">choose EndoStream.</span>',
        why=["Easy, permanent access to all your patients’ data", "Prepare any report in under 60 seconds", "Unlimited report templates for every need", "Track cases for research or performance goals", "Send images to PACS and reports to HIS"],
        logos=ENDO_LOGOS, logo_cls="endo"))

    orbit = '''<div class="orbit"><div class="ring1"></div>
  <div class="core">''' + ICONS["clock"] + '''<b>OneEndo</b><span>+ EndoStream</span></div>
  <div class="node" style="left:38%;top:2%"><i></i>Scheduling</div>
  <div class="node" style="left:2%;top:40%"><i></i>Sales</div>
  <div class="node" style="right:2%;top:40%"><i></i>Patients</div>
  <div class="node" style="left:34%;bottom:0"><i></i>Accounting</div>
  <div class="node" style="right:12%;bottom:6%"><i></i>Inventory</div></div>'''
    product_page(dict(
        file="oneendo.html", theme="oneendo", name="OneEndo", logo="logos/oneendo.png", div=ENDO_DIV, outline="CENTER",
        title="OneEndo · Nebras Technology", desc="OneEndo is a complete endoscopy-center information system, from the first appointment to the final invoice.",
        eyebrow="Endoscopy · Center management", h1a="The whole endoscopy center,", h1b="on one clock.",
        lead="OneEndo is a complete endoscopy-center information system, from the first appointment to the final invoice. Together with EndoStream, every procedure is documented and every operation managed.",
        hero_visual=orbit, chips={"tr": ("+", "works with EndoStream"), "bl": ("1", "system for the whole center")},
        glance="Documentation and management working as one, built by the same team.",
        tags=["Scheduling", "Patient management", "Accounting", "Inventory", "Sales"],
        features=[
            dict(pill="Operations", label="Operations", t1="Bookings, rooms and scopes,", t2="planned in one view.", desc="Every room and every scope scheduled on one clock.",
                 points=[("Scheduling", "Bookings, rooms and scopes planned in one view."), ("Patient management", "One file for every patient and procedure.")], media=panel("calendar", "Scheduling · Patient management")),
            dict(pill="Business", label="Business", t1="Revenue, stock and invoices,", t2="under control.", desc="The back office of the unit, connected to every procedure.",
                 points=[("Accounting", "Invoices, payments and insurance in one place."), ("Inventory", "Scopes, consumables and stock levels."), ("Sales", "Referrals and revenue tracked per physician.")], media=panel("chart", "Accounting · Inventory · Sales")),
        ],
        statement='Documentation and management <span>working as one.</span>', team=[DEV, SALES],
        why_title='One clock for the<br><span class="accent-ink">whole unit.</span>',
        why=["One file for every patient and procedure", "Rooms and scopes planned together", "Invoices, payments and insurance in one place", "Stock levels for scopes and consumables", "Works hand in hand with EndoStream"],
        logos=ENDO_LOGOS, logo_cls="endo"))

    product_page(dict(
        file="dentalore-cloud.html", theme="cloud", name="DentaLore Cloud", logo="logos/dentalore.png", div=DENT_DIV, outline="CLOUD",
        title="DentaLore Cloud · Nebras Technology", desc="Everything your clinic needs, in one cloud: charting, imaging, lab, stock and finance.",
        eyebrow="Dental · Clinics", h1a="Everything your clinic needs,", h1b="in one cloud.",
        lead="From the first appointment to the final invoice: charting, imaging, lab, stock and finance, wherever your clinic is.",
        hero_visual=laptop("screens/dentalore-chart.jpg", "DentaLore Cloud dental chart"), chips={"tr": ("Cloud", "work from anywhere"), "bl": ("1,200", "active clinics")},
        glance="DentaLore Cloud brings clinical care, insight and supplies together, so the whole clinic runs on one screen.",
        tags=["3D dental chart", "Smart scheduler", "Patient images", "Analytics", "Lab workflow", "Inventory &amp; finance"],
        glance_visual=f'<div class="trio">{shot("screens/dentalore-queue.jpg", "Smart scheduler", "light")}<div class="side">{shot("screens/dentalore-images.jpg", "Patient images", "light")}{shot("screens/dentalore-analytics.jpg", "Analytics", "light")}</div></div>',
        features=[
            dict(pill="Clinical care", label="Clinical care", t1="From the first visit", t2="to the final invoice.", desc="Chart every tooth, plan every visit and view every image.",
                 points=[("3D dental chart", "Procedures planned, in progress or completed, with fees and providers."), ("Smart scheduler", "Clinics side by side, color-coded visit status at a glance."), ("Patient images", "Panoramic, periapical and intraoral images in one viewer.")], media=laptop("screens/dentalore-chart.jpg", "Dental chart")),
            dict(pill="Insight &amp; control", label="Insight &amp; control", t1="Safe, traceable", t2="and under control.", desc="Live numbers, tracked lab cases and the right access for every user.",
                 points=[("Analytics dashboard", "Patients, procedures, visits, financials and top providers, live."), ("Lab workflow", "Shades, products, cost and delivery, with every remake tracked."), ("Access rights", "View, add, edit and delete rights for every user and module.")], media=laptop("screens/dentalore-analytics.jpg", "Analytics")),
            dict(pill="Supplies &amp; finance", label="Supplies &amp; finance", t1="Never run out.", t2="Always know where you stand.", desc="Cash flow and stock, side by side.",
                 points=[("Cash flow", "Income and expenses by cash, card, wallet or transfer."), ("Inventory dashboard", "Stock value, expiry alerts, low and high levels, purchase orders."), ("Main stock", "Every product with stock, target and reorder levels.")], media=laptop("screens/dentalore-inventory.jpg", "Inventory")),
        ],
        statement='We keep <span>1,200 clinics</span> running on one cloud.',
        team=[("photos/team-dentalore.jpg", "DentaLore Cloud team", "From the first appointment to the final invoice, 1,200 clinics on one cloud."), DEV],
        why_title='Built for the<br><span class="accent-ink">modern clinic.</span>',
        why=["Work from any device, in any branch", "Every tooth charted in 3D", "Lab cases tracked to delivery", "Stock and cash flow always visible", "Onboarding and training from day one"],
        logos=CLINIC_LOGOS))

    schools = [("dental-17.jpg", "Ain Shams University", "2,000"), ("dental-18.jpg", "MSA University", "1,200"), ("dental-19.jpg", "German University in Cairo", "400"), ("dental-20.jpg", "Horus University", "900"),
               ("dental-21.jpg", "British University in Egypt", "1,100"), ("dental-22.jpg", "Arab Academy", "500"), ("dental-23.jpg", "Nahda University", "1,000"), (None, "Al Salam University", "800")]
    sc = "".join(f'<div class="school"><div class="sl">{img("clients/" + l, n) if l else "<strong>SUE</strong>"}</div><b>{n}</b><span>{s} students</span></div>' for l, n, s in schools)
    extra = f'''<section class="section"><div class="container reveal">{eyebrow("Trusted by leading dental schools")}<h2 class="h-md" style="margin-top:16px">8 dental schools.<br><span class="accent-ink">One platform.</span></h2><div class="schools">{sc}</div></div></section>'''
    phones = f'<div class="phones"><div class="phone">{img("screens/ds-phone-1.jpg", "DentaLore DS mobile app")}</div><div class="phone">{img("screens/ds-phone-2.jpg", "DentaLore DS work list")}</div></div>'
    product_page(dict(
        file="dentalore-ds.html", theme="ds", name="DentaLore DS", logo="logos/dentalore-ds.png", div=DENT_DIV, outline="CAMPUS",
        title="DentaLore DS · Nebras Technology", desc="Where future dentists learn, practice and graduate. The academic platform for dental schools.",
        eyebrow="Dental · Universities", h1a="Where future dentists", h1b="learn, practice and graduate.",
        lead="Every case a student treats is assigned, supervised, graded and recorded in one connected journey, on desktop and mobile.",
        hero_visual=laptop("screens/ds-hero.jpg", "DentaLore DS"), chips={"tr": ("7,900+", "students"), "bl": ("8", "dental schools")},
        glance="One platform for student progress, patient records, clinics and accreditation, with one team that knows every university we serve.",
        tags=["Patient assignment", "Evaluation &amp; grades", "3D tooth chart", "Medical alerts", "Mobile app", "Arabic &amp; English"],
        glance_visual=trio("screens/ds-chart.jpg", "screens/ds-small-1.jpg", "screens/ds-patient.jpg"),
        features=[
            dict(pill="Learning journey", label="Learning journey", t1="From first case", t2="to graduation.", desc="Assign, work, evaluate, graduate: each step graded, noted and signed by the instructor.",
                 points=[("Assign", "Instructors assign cases to students in each department."), ("Work", "Students treat their patients and complete each procedure step."), ("Evaluate", "Each step graded, noted and signed by the instructor.")], media=laptop("screens/ds-assign.jpg", "Assign cases")),
            dict(pill="Patient management", label="Patient management", t1="Everything about every patient,", t2="all in one place.", desc="A large, centralized patient database with Arabic and English interfaces.",
                 points=[("Smart search", "By name, ID, phone and address."), ("Medical alerts", "Visual alerts for critical information."), ("Referral management", "Manage referrals in and out.")], media=laptop("screens/ds-patient.jpg", "Patient file")),
            dict(pill="Mobile app", label="Mobile app", t1="Smart. Connected.", t2="Student-centric.", desc="Every assigned patient, procedure and grade in the student’s pocket.",
                 points=[("Assigned patients", "Patients and procedures, always at hand."), ("Track status", "Procedure status and student grades in real time.")], media=phones),
        ],
        statement='<span>7,900+ students</span> on the journey across 8 dental schools.', extra=extra,
        team=[("photos/ds-academic-team.jpg", "DentaLore DS academic team", "We help dental schools teach, track and graduate every student."), ("photos/dental-school-clinic.jpg", "In the clinic", "Students learn, practice and graduate on DentaLore DS.")],
        why_title='Teaching the next<br><span class="accent-ink">generation of dentists.</span>',
        why=["Every case assigned, supervised and graded", "Student grades in real time", "Medical alerts on every patient file", "Desktop for clinics and instructors, mobile for students", "Ready for accreditation reviews"],
        logos=SCHOOL_LOGOS))

# ------------------------------------------------------------------ NEO Q
def build_neoq():
    bars = "".join(f'<div class="row"><span>{a}</span><div class="track"><i style="width:{w}%"></i></div><b>{b}</b></div>' for a, w, b in [("Normal report", 3, "2 sec"), ("Head", 8, "30 sec"), ("Knee", 33, "&lt; 2 min"), ("Spine", 50, "&lt; 3 min"), ("Abdomen", 100, "&lt; 6 min")])
    errs = [("swap", "Localization", "Right side, right region. Wrong-side slips are flagged as you report."), ("users", "Gender &amp; organs", "Organs mentioned are cross-checked against the patient’s gender."),
            ("message", "Referral comments", "The report is checked against the referring clinician’s comments."), ("scan", "Missing body parts", "Absent or removed body parts are flagged and commented.")]
    eh = "".join(f'<div class="err reveal">{ICONS[i]}<b>{t}</b><span>{d}</span></div>' for i, t, d in errs)
    body = f'''
<section class="p-hero"><span class="outline-word" aria-hidden="true" style="left:45%">30</span><div class="container">
  {crumbs(("Home", "index.html"), ("Solutions", "solutions.html"), ("Radiology", "radiology.html"), ("Neo Q partnership", ""))}
  <div class="p-hero-grid">
    <div><div class="cobrand">{img("brand/nebras-logo.png", "Nebras")}<em>×</em>{img("logos/neoq-teal.png", "Neo Q", extra=' style="height:26px"')}</div>
      <div style="margin-top:22px">{eyebrow("Strategic partnership · Germany × MENA")}</div>
      <h1>The <span style="color:var(--accent)">30-second</span><br>report.</h1>
      <p class="lead">PaXtreme® and RadioReport® together: one connected workflow for images, structured reports and AI. RadioReport is developed in Berlin and delivered across the region with Nebras.</p>
      <div class="btns"><a class="btn btn-accent" href="contact.html#demo">Book a live demo {ARR_UR}</a></div></div>
    <div class="reveal"><div class="ring"><svg viewBox="0 0 120 120"><circle cx="60" cy="60" r="54" fill="none" stroke="rgba(255,255,255,.08)" stroke-width="3"/><circle cx="60" cy="60" r="54" fill="none" stroke="#11d2d8" stroke-width="3" stroke-linecap="round" stroke-dasharray="339.3" stroke-dashoffset="254" style="filter:drop-shadow(0 0 6px #11d2d8)"/></svg><div class="in"><b>30</b><span>SECONDS</span></div></div></div>
  </div>
</div></section>
<section class="section"><div class="container glance reveal">
  <div>{eyebrow("Speed by examination")}<h2 class="h-md" style="margin:16px 0 18px">Faster reports.<br><span class="accent-ink">Same radiologist.</span></h2><p class="lead" style="font-size:14.5px">Structured reporting removes the typing. The radiologist reviews, decides and signs every report.</p></div>
  <div class="bars light">{bars}<div class="axis"><span></span><div><span>0</span><span>2 min</span><span>4 min</span><span>6 min</span></div><span></span></div></div>
</div></section>
<section class="section bg-alt"><div class="container">
  {eyebrow("Get it right the first time")}<h2 class="h-md" style="margin:16px 0 18px">Common errors.<br><span class="accent-ink">Gone.</span></h2>
  <p class="lead" style="font-size:14.5px">Structured checks flag these four as you report, so they never reach the signed report.</p>
  <div class="err-grid">{eh}</div>
</div></section>
<section class="triple"><div class="container grid3">
  <div class="reveal"><small>01</small><b>Increase reporting capacity</b><p>Complete more reports each day and deliver results sooner.</p></div>
  <div class="reveal"><small>02</small><b>Simplify the reporting day</b><p>Images, guided reporting and ICD coding in one workflow.</p></div>
  <div class="reveal"><small>03</small><b>Progress to AI with confidence</b><p>Start guided today and add AI as your needs evolve.</p></div>
</div></section>
<section class="section"><div class="container practice reveal">
  <div class="im">{img("photos/news-alfardous-1.jpg", "Al Fardous Scan signing at EIRC 2026")}</div>
  <div>{eyebrow("In practice")}<h2 class="h-md" style="margin:16px 0 18px">Al Fardous Scan<br><span class="accent-ink">goes first.</span></h2>
  <p style="color:var(--muted);font-size:14.5px;margin-bottom:12px">Signed at EIRC 2026, Al Fardous Scan chose not only structured AI reporting but the complete Nebras × Neo Q solution, moving from talking about AI to putting it into practice.</p>
  <a class="link-arrow" href="news.html">Read the story {ARR_R}</a></div>
</div></section>
<section class="section" style="padding-top:20px" data-carousel><div class="container">
  <div class="carousel-head"><div>{eyebrow("The team behind the 30-second report")}<h2 class="h-md">Nebras × Neo Q,<br><span class="accent-ink">side by side.</span></h2></div>
    <div class="car-btns"><button data-prev aria-label="Previous">{ARR_L}</button><button data-next aria-label="Next">{ARR_R}</button></div></div>
  <div class="car-track">
    <div class="team-card">{img("photos/news-alfardous-1.jpg", "Al Fardous Scan signing")}<small>Nebras × Neo Q</small><p>Al Fardous Scan signs at EIRC 2026.</p></div>
    <div class="team-card">{img(AI[0], AI[1])}<small>{AI[1]}</small><p>{AI[2]}</p></div>
    <div class="team-card">{img("photos/news-eirc-2.jpg", "EIRC 2026")}<small>EIRC 2026</small><p>From vision to reality: NI + AI on the EIRC stage.</p></div>
  </div>
</div></section>
{cta_box("Report in", "30 seconds.", "See PaXtreme and RadioReport working together on your own studies.")}
'''
    page("neoq.html", "Neo Q partnership · The 30-second report · Nebras Technology", "PaXtreme® and RadioReport® together: one connected workflow for images, structured reports and AI.", body, "neoq", theme="neoq")

# ------------------------------------------------------------------ CLIENTS / NEWS / CONTACT
def build_clients():
    body = f'''
<section class="page-hero grid-bg"><span class="outline-word" aria-hidden="true">TRUST</span><div class="container">
  {crumbs(("Home", "index.html"), ("Clients", ""))}
  {eyebrow("Our clients")}
  <h1 class="h-lg">Trusted by ministries,<br><span class="o">hospitals and clinics.</span></h1>
  <p class="lead">From national ministries and university hospitals to private clinics, in 16 countries.</p>
  {stats([("1900+", "Customers"), ("263", "Radiology clients"), ("230", "Endoscopy clients"), ("1,200", "Dental clinics")])}
</div></section>
<section class="section client-sec"><div class="container">
  {eyebrow("01 · Radiology")}<h2 class="h-md">Ministries, hospitals<br><span class="o">and imaging centers.</span></h2><div style="height:26px"></div>
  {logo_grid(RAD_LOGOS)}
</div></section>
<section class="section bg-alt client-sec"><div class="container">
  {eyebrow("02 · Endoscopy")}<h2 class="h-md">Leading hospitals,<br><span class="o">worldwide.</span></h2>
  <p class="lead" style="font-size:14.5px">From Malaysia, Qatar and Oman to Egypt’s university hospitals, national institutes, military and private hospital groups, plus 200 more centers.</p>
  {logo_grid(ENDO_LOGOS, "endo")}
</div></section>
<section class="section client-sec"><div class="container">
  {eyebrow("03 · Dental")}<h2 class="h-md">Clinics and<br><span class="o">dental schools.</span></h2><div style="height:26px"></div>
  {logo_grid(DENT_LOGOS)}
</div></section>
{cta_box("Join 1900+", "healthcare providers.", "Talk to us about your center, your workflow and your goals.")}
'''
    page("clients.html", "Clients · Nebras Technology", "Trusted by ministries, hospitals and clinics in 16 countries.", body, "clients")

def build_news():
    body = f'''
<section class="page-hero grid-bg"><span class="outline-word" aria-hidden="true">NEWS</span><div class="container">
  {crumbs(("Home", "index.html"), ("News", ""))}
  {eyebrow("Media · News")}
  <h1 class="h-xl">News &amp; <span class="o">stories.</span></h1>
  <p class="lead">Partnerships, products and moments from the Nebras team.</p>
</div></section>
<section class="section"><div class="container">
  <article class="news-feature reveal">
    <div class="im">{img("photos/news-alfardous-1.jpg", "Al Fardous Scan signing with Nebras and Neo Q")}</div>
    <div><small>Partnership · EIRC 2026 · Cairo</small><h2>Al Fardous Scan chooses the complete Nebras × Neo Q solution</h2>
      <p>At EIRC 2026, Al Fardous Scan signed with Nebras Technology and Neo Q. The center took more than structured reporting: it chose the complete Nebras × Neo Q solution, bringing the 30-second report into clinical practice.</p>
      <p>Beyond talking about AI, the center is putting it into practice, with intelligent automation and structured, standardized reporting built on PaXtreme® and RadioReport®.</p></div>
  </article>
  {news_cards()}
</div></section>
'''
    page("news.html", "News & stories · Nebras Technology", "Partnerships, products and moments from the Nebras team.", body, "news", big_cta=True)

def build_contact():
    mapbg = '''<svg class="mapbg" viewBox="0 0 400 210" preserveAspectRatio="xMidYMid slice"><defs><pattern id="g" width="18" height="18" patternUnits="userSpaceOnUse"><path d="M18 0H0V18" fill="none" stroke="rgba(255,255,255,.05)"/></pattern></defs><rect width="400" height="210" fill="url(#g)"/>
<path d="M240 -10C250 60 225 120 245 230" stroke="#2a63d6" stroke-width="14" fill="none" opacity=".55"/>
<g stroke="rgba(255,255,255,.22)" stroke-width="1.5" fill="none"><path d="M60 10 380 70"/><path d="M40 190 380 110"/><path d="M130 0 165 210"/><path d="M0 120 400 160"/><path d="M300 0 270 210"/></g></svg>'''
    sols = ["Radiology · PaXtreme, OneRIS, InstaShare", "Radiology · OneAccred, OneRad", "Neo Q · The 30-second report", "Endoscopy · EndoStream, OneEndo", "Dental · DentaLore Cloud", "Dental · DentaLore DS", "Not sure yet"]
    body = f'''
<section class="page-hero grid-bg" style="padding-bottom:90px"><div class="container">
  {crumbs(("Home", "index.html"), ("Contact", ""))}
  <div class="contact-hero-grid">
    <div><div class="hello">Hello<span>.</span></div>
      <h1 class="h-md" style="margin:28px 0 18px">Let’s talk about<br><span class="o">your center.</span></h1>
      <p class="lead">Every partnership starts with a conversation. We listen first, so the right solution reaches the right center.</p>
      <div class="contact-lines"><div><small>Call us</small><a href="tel:+20237615212">+20 2 3761 5212</a></div><div><small>Write to us</small><a href="mailto:info@nebrastech.com">info@nebrastech.com</a></div></div></div>
    <figure class="contact-photo reveal">{img("photos/sales-development.jpg", "Sales development at Nebras")}<figcaption><small>Sales development</small><b>The first voice you’ll hear at Nebras.</b></figcaption></figure>
  </div>
</div></section>
<section class="section" id="demo"><div class="container contact-grid">
  <form class="form-card reveal" id="demo-form">
    <h2>Request a demo</h2>
    <div class="fgrid">
      <div class="field"><label for="f-name">Full name</label><input id="f-name" name="name" placeholder="Dr. Sara Ahmed" required></div>
      <div class="field"><label for="f-org">Organization</label><input id="f-org" name="org" placeholder="Center or hospital"></div>
      <div class="field"><label for="f-email">Work e-mail</label><input id="f-email" name="email" type="email" placeholder="name@center.com" required></div>
      <div class="field"><label for="f-phone">Phone</label><input id="f-phone" name="phone" type="tel" placeholder="+20 …"></div>
      <div class="field full"><label for="f-sol">Solution</label><select id="f-sol" name="solution">{"".join(f"<option>{s}</option>" for s in sols)}</select></div>
      <div class="field full"><label for="f-msg">Message</label><textarea id="f-msg" name="message" placeholder="Tell us about your workflow"></textarea></div>
    </div>
    <button class="btn btn-primary" type="submit">Send request {SEND}</button>
    <p class="form-note">Thank you. Your e-mail app has opened with your request ready to send.</p>
  </form>
  <div class="reveal">
    <div class="map-card">{mapbg}<div class="map-pin"><i></i><div><b>Nebras Technology</b><span>37 Amman St, Dokki, Giza</span></div></div><small>DOKKI · GIZA · EGYPT</small></div>
    <div class="info-grid">
      <div class="info">{ICONS["phone"]}<small>Mobile</small><p><a href="tel:+201065534412">+20 106 553 4412</a><br><a href="tel:+201069035666">+20 106 903 5666</a></p></div>
      <div class="info">{ICONS["clock"]}<small>Working hours</small><p>Sunday to Thursday<br>10:00 to 18:00</p></div>
      <div class="info">{ICONS["globe"]}<small>Web</small><p><a href="https://www.nebrastech.com">www.nebrastech.com</a><br><a href="https://www.nebras-dentalore.com">www.nebras-dentalore.com</a></p></div>
      <div class="info">{ICONS["pin"]}<small>Address</small><p>37 Amman St, Dokki<br>Giza, Egypt</p></div>
    </div>
  </div>
</div></section>
'''
    page("contact.html", "Contact · Nebras Technology", "Let’s talk about your center. Request a demo of any Nebras solution.", body, "contact", big_cta=True)

if __name__ == "__main__":
    build_home(); build_about(); build_leadership(); build_milestones(); build_solutions()
    build_divisions(); build_products(); build_neoq(); build_clients(); build_news(); build_contact()
