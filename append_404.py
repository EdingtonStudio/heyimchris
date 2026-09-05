#!/usr/bin/env python3
import build as b

MAIN_404 = '''  <main id="main">
    <section class="hero" style="text-align: left;">
      <div class="wrap">
        <p class="eyebrow">404</p>
        <h1 class="display-hero" style="font-size: var(--text-3xl);">Page not<br />found.</h1>
        <div class="cta-row" style="margin-top: var(--space-8);">
          <a class="btn btn-primary" href="index.html">Back home</a>
        </div>
      </div>
    </section>
  </main>
'''

b.write_page(
    "404.html",
    "",
    "Page not found \u2014 Chris Edington",
    "This page does not exist.",
    MAIN_404,
)
print("done: 404")
