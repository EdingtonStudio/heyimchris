#!/usr/bin/env python3
"""Assembles the static HTML pages for heyimchris.com from shared header/footer + per-page main content."""
import os

ROOT = os.path.dirname(os.path.abspath(__file__))

MENU_ICON = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M4 7h16M4 12h16M4 17h16"/></svg>'
CLOSE_ICON = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M6 6l12 12M18 6L6 18"/></svg>'

NAV_ITEMS = [
    ("about.html", "About"),
    ("notes.html", "Notes"),
    ("government.html", "Government"),
    ("contact.html", "Contact"),
]


def render_nav(active):
    links = []
    for href, label in NAV_ITEMS:
        current = ' aria-current="page"' if href == active else ""
        links.append(f'<a href="{href}"{current}>{label}</a>')
    return "\n        ".join(links)


def head(title, description, canonical, og_title=None, og_description=None, extra_head=""):
    og_title = og_title or title
    og_description = og_description or description
    if canonical == "index.html":
        canonical = ""
    return f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title}</title>
  <meta name="description" content="{description}" />
  <link rel="canonical" href="https://heyimchris.com/{canonical}" />
  <meta property="og:type" content="website" />
  <meta property="og:title" content="{og_title}" />
  <meta property="og:description" content="{og_description}" />
  <meta property="og:url" content="https://heyimchris.com/{canonical}" />
  <meta property="og:image" content="https://heyimchris.com/assets/og-image.png" />
  <meta property="og:image:width" content="1200" />
  <meta property="og:image:height" content="630" />
  <meta property="og:image:alt" content="Hey, I'm Chris in pale yellow script lettering with a smiley face on black" />
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="theme-color" content="#000000" />
  <link rel="icon" type="image/png" href="assets/favicon.png" />
  <link rel="apple-touch-icon" href="assets/apple-touch-icon.png" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&family=DM+Mono:wght@300;400;500&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="base.css" />
  <link rel="stylesheet" href="style.css" />
  <script defer src="/_vercel/insights/script.js"></script>
{extra_head}</head>
<body>
  <a class="skip-link" href="#main">Skip to content</a>
'''


def header(active):
    return f'''  <header class="site-header">
    <div class="wrap header-inner">
      <a class="brand-mark" href="index.html" aria-label="Chris Edington, home">
        <picture class="brand-wordmark"><source srcset="assets/ce-wordmark-static.png" media="(prefers-reduced-motion: reduce)" /><img src="assets/ce-wordmark-loop.gif" alt="Chris Edington" /></picture>
      </a>
      <nav class="main-nav" data-main-nav aria-label="Primary">
        {render_nav(active)}
      </nav>
      <button class="mobile-menu-btn" data-menu-toggle type="button" aria-label="Open menu" aria-expanded="false">
        {MENU_ICON}
      </button>
    </div>
  </header>
'''


FOOTER = '''  <footer class="site-footer">
    <div class="wrap">
      <div class="footer-top">
        <div class="footer-brand">
          <a class="brand-mark" href="index.html" aria-label="Chris Edington, home">
            <picture class="brand-wordmark"><source srcset="assets/ce-wordmark-static.png" media="(prefers-reduced-motion: reduce)" /><img src="assets/ce-wordmark-loop.gif" alt="Chris Edington" /></picture>
          </a>
          <p class="text-muted" style="margin-top: var(--space-4);">Creative director and founder. Building Edington Studio, Quell, and Mr. Sniff&rsquo;s from Pittsburgh, PA.</p>
          <p class="footer-veteran">A certified veteran-owned small business<span>VOSB &middot; SBA VetCert &middot; SAM.gov registered</span></p>
        </div>
        <div class="footer-cols">
          <div class="footer-col">
            <h4>Site</h4>
            <a href="about.html">About</a>
            <a href="notes.html">Notes</a>
            <a href="government.html">Government</a>
            <a href="contact.html">Contact</a>
          </div>
          <div class="footer-col">
            <h4>Elsewhere</h4>
            <a href="https://www.edington.co" target="_blank" rel="noopener">Edington Studio</a>
            <a href="https://www.shopquell.co" target="_blank" rel="noopener">Quell</a>
            <a href="https://www.linkedin.com/in/chris-edington/" target="_blank" rel="noopener">LinkedIn</a>
            <a href="https://dribbble.com/ChrisEdington" target="_blank" rel="noopener">Dribbble</a>
          </div>
        </div>
      </div>
      <div class="footer-bottom">
        <p>&copy; <span data-year>2026</span> Chris Edington</p>
        <p>Pittsburgh, PA</p>
      </div>
    </div>
  </footer>
  <script src="app.js" defer></script>
</body>
</html>
'''


def write_page(filename, active, title, description, main_html, og_title=None, og_description=None, extra_head=""):
    html = head(title, description, filename, og_title, og_description, extra_head) + header(active) + main_html + FOOTER
    with open(os.path.join(ROOT, filename), "w") as f:
        f.write(html)
    print("wrote", filename)
