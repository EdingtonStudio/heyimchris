#!/usr/bin/env python3
import build as b

ARROW = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M7 17 17 7M7 7h10v10"/></svg>'
SHIELD = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 2 4 6v6c0 5 3.5 8.5 8 10 4.5-1.5 8-5 8-10V6l-8-4Z"/></svg>'

# ---------------------------------------------------------------- HOME
INDEX_MAIN = f'''  <main id="main">
    <section class="hero">
      <div class="wrap">
        <div class="hero-top">
          <span>Hey, I&rsquo;m Chris</span>
          <span class="status-chip"><span class="status-dot"></span>Based in Pittsburgh, PA</span>
        </div>
        <h1 class="display-hero hero-headline">Oh,<br />hey there.</h1>
        <div class="hero-foot">
          <p class="lede">I&rsquo;ve spent 15 years building brands for other people. I&rsquo;ve also built brands of my own: one I sold, two I&rsquo;m running right now. Edington Studio is the practice. Quell, Mr. Sniff&rsquo;s, and Puddle Pirate are the proof.</p>
        </div>
      </div>
    </section>

    <section class="section section--tight" style="border-top: 1px solid var(--color-border); padding-top: var(--space-8);">
      <div class="wrap">
        <p class="eyebrow">What I run</p>
        <h2 class="display-xl" style="max-width: 20ch;">The studio, and what it&rsquo;s built</h2>
      </div>
    </section>

    <section class="wrap">
      <div class="work-stack">
        <div class="work-card-wrap">
        <a class="work-card" href="https://www.edington.co" target="_blank" rel="noopener" style="--card-bg:#ECE8DD; --card-ink:#2733D9;">
          <div class="work-card-head">
            <div class="work-card-top">
              <span>Est. 2024</span>
              <span>Creative studio</span>
            </div>
            <div class="work-card-main">
              <div class="work-card-logo" style="height: clamp(38px, 4.8vw, 58px);"><img src="assets/EdingtonStudioLogo-blue.png" alt="Edington Studio" loading="lazy" decoding="async" /></div>
              <span class="work-card-arrow">{ARROW}</span>
            </div>
          </div>
          <div class="work-card-media work-card-media--image" style="background-image: url('assets/edington-studio-work.jpg');"></div>
        </a>
        </div>

        <div class="work-card-wrap">
        <a class="work-card" href="https://www.shopquell.co" target="_blank" rel="noopener" style="--card-bg:#3A1C2A; --card-ink:#DBCAFF;">
          <div class="work-card-head">
            <div class="work-card-top">
              <span>Est. 2023</span>
              <span>Art supply brand</span>
            </div>
            <div class="work-card-main">
              <div class="work-card-logo"><img src="assets/QuellLogo-lavender.svg" alt="Quell" loading="lazy" decoding="async" /></div>
              <span class="work-card-arrow">{ARROW}</span>
            </div>
          </div>
          <div class="work-card-media work-card-media--image" style="background-image: url('assets/quell-product.jpg');"></div>
        </a>
        </div>

        <div class="work-card-wrap">
        <a class="work-card" href="https://www.mrsniffs.co" target="_blank" rel="noopener" style="--card-bg:#D96B61; --card-ink:#000000;">
          <div class="work-card-head">
            <div class="work-card-top">
              <span>Newest</span>
              <span>Incense brand</span>
            </div>
            <div class="work-card-main">
              <div class="work-card-logo" style="height: clamp(38px, 4.8vw, 58px);"><img src="assets/mr-sniffs-wordmark-black-transparent.png" alt="Mr. Sniff&rsquo;s" loading="lazy" decoding="async" /></div>
              <span class="work-card-arrow">{ARROW}</span>
            </div>
          </div>
          <div class="work-card-media work-card-media--image" style="background-image: url('assets/mr-sniffs-incense.jpg');"></div>
        </a>
        </div>

        <div class="work-card-wrap work-card-wrap--last">
        <div class="work-card work-card--static" style="--card-bg:#3A3A3A; --card-ink:#BDBDBD;">
          <div class="work-card-head">
            <div class="work-card-top">
              <span>2013&ndash;2023</span>
              <span>Built &amp; sold</span>
            </div>
            <div class="work-card-main">
              <div class="work-card-logo" style="height: clamp(38px, 4.8vw, 58px);"><img src="assets/PuddlePirateLogo-gray-trimmed.png" alt="Puddle Pirate Co." loading="lazy" decoding="async" /></div>
            </div>
          </div>
          <div class="work-card-media work-card-media--image" style="background-image: url('assets/puddle-pirate-hats.jpg');"></div>
        </div>
        </div>
      </div>
    </section>

    <section class="section section--tight" style="border-top: 1px solid var(--color-border);">
      <div class="wrap split-grid">
        <div>
          <p class="eyebrow">How I think</p>
          <h2 class="display-xl">Discipline<br />beats a good<br />mood board.</h2>
        </div>
        <div>
          <p class="lede" style="margin-bottom: var(--space-6);">Most creative work fails at the handoff, not the concept. I structure every project around what actually ships: fewer rounds of exploration, more rounds of production.</p>
          <a class="btn-text" href="about.html#philosophy">Read how I work {ARROW}</a>
        </div>
      </div>
    </section>

    <section class="section section--tight" style="border-top: 1px solid var(--color-border);">
      <div class="wrap">
        <p class="eyebrow">Notes</p>
        <h2 class="display-xl" style="margin-bottom: var(--space-10);">Some things I&rsquo;ve written down</h2>
        <div class="teaser-grid">
          <a class="card" href="notes.html#discipline-is-the-strategy">
            <p class="note-meta">On building</p>
            <h3 class="display-md" style="margin-bottom: var(--space-3);">Discipline is the strategy</h3>
            <p class="text-muted">Strategy tells you what to build. Discipline is what actually builds it.</p>
          </a>
          <a class="card" href="notes.html#what-owning-it-taught-me">
            <p class="note-meta">On owning what you sell</p>
            <h3 class="display-md" style="margin-bottom: var(--space-3);">What running my own P&amp;L taught me</h3>
            <p class="text-muted">Client work teaches you craft. Owning a brand teaches you consequence.</p>
          </a>
        </div>
        <a class="btn-text" href="notes.html" style="margin-top: var(--space-10);">Read all notes {ARROW}</a>
      </div>
    </section>
  </main>
'''

b.write_page(
    "index.html",
    "",
    "Chris Edington \u2014 creative director and founder, Pittsburgh",
    "Creative director and founder of Edington Studio, Quell, Mr. Sniff\u2019s, and Puddle Pirate Co. Fifteen years building brands, some of them my own.",
    INDEX_MAIN,
    og_title="Built. Building. Both.",
)

print("done: index")

# ---------------------------------------------------------------- ABOUT
ABOUT_MAIN = '''  <main id="main">
    <section class="page-hero">
      <div class="wrap">
        <p class="eyebrow">About</p>
        <h1 class="display-3xl" style="margin-bottom: var(--space-4);">The long version</h1>
        <p class="lede">Fifteen years building brands. Some of them my own.</p>
      </div>
    </section>

    <section class="section section--tight">
      <div class="wrap about-grid">
        <div class="prose">
          <p>I&rsquo;m Chris Edington. I grew up in Wake Forest, North Carolina, and joined the Coast Guard in 2004. Four years of service took me to Charleston, South Carolina, where I started in design and earned a B.A. in Graphic Design from the Art Institute of Charleston in 2011.</p>
          <p>I spent the next decade working agency-side on brands like Porsche, Audi, Milk-Bone, and Rachael Ray Nutrish, then went in-house as creative director and later chief marketing officer at Island Brands USA, where I helped raise more than $5 million from over 6,000 investors and shipped the can design that carried the brand into national distribution.</p>
          <p>In 2013 I founded Puddle Pirate Co., a lifestyle brand for the Coast Guard community. Ten years and more than 10,000 shirts later, I sold it in 2023.</p>
          <p>In 2023 my wife Kaitlyn and I co-founded Quell, an art supply company built for working artists and educators. She runs the community and the classroom side. I run the brand and the build.</p>
          <p>In 2024 I started Edington Studio, a practice for founders who want the same thing I wanted when I was one: naming, identity, packaging, and web that actually ships, from someone who has done it himself.</p>
          <p>Most recently I started Mr. Sniff&rsquo;s, an incense brand I&rsquo;m building from scratch: sourcing, packaging, and fulfillment, out of Pittsburgh.</p>
          <p>I live in Pittsburgh with my wife and two kids. Edington Studio is a certified veteran-owned small business.</p>
        </div>
        <aside class="card" aria-label="At a glance">
          <p class="display-md" style="margin-bottom: var(--space-5);">At a glance</p>
          <dl class="info-grid" style="grid-template-columns: 1fr;">
            <div class="info-item">
              <dt>Based in</dt>
              <dd>Pittsburgh, PA</dd>
            </div>
            <div class="info-item">
              <dt>Service</dt>
              <dd>U.S. Coast Guard, 2004&ndash;2008</dd>
            </div>
            <div class="info-item">
              <dt>Studio</dt>
              <dd>Edington Studio, est. 2024</dd>
            </div>
            <div class="info-item">
              <dt>Certifications</dt>
              <dd>VOSB &middot; SBA-certified small business &middot; PA VBE</dd>
            </div>
            <div class="info-item">
              <dt>Education</dt>
              <dd>B.A. Graphic Design, Art Institute of Charleston, 2011</dd>
            </div>
          </dl>
        </aside>
      </div>
    </section>

    <section class="section section--tight" style="border-top: 1px solid var(--color-border);">
      <div class="wrap">
        <p class="eyebrow">Timeline</p>
        <h2 class="display-xl" style="margin-bottom: var(--space-10);">How I got here</h2>
        <div class="timeline">
          <div class="timeline-item">
            <p class="timeline-date">2024&ndash;now</p>
            <div>
              <p class="display-lg" style="margin-bottom: var(--space-2);">Edington Studio &middot; Founder &amp; creative director</p>
              <p class="text-muted">Naming, identity, packaging, and web for founder-led and product companies.</p>
            </div>
          </div>
          <div class="timeline-item">
            <p class="timeline-date">2023&ndash;now</p>
            <div>
              <p class="display-lg" style="margin-bottom: var(--space-2);">Quell &middot; Co-founder</p>
              <p class="text-muted">Art supplies for working artists and educators, co-founded with my wife Kaitlyn.</p>
            </div>
          </div>
          <div class="timeline-item">
            <p class="timeline-date">~2017&ndash;2021</p>
            <div>
              <p class="display-lg" style="margin-bottom: var(--space-2);">Island Brands USA &middot; Creative director, then CMO</p>
              <p class="text-muted">Helped raise more than $5 million from over 6,000 investors and shipped the can design that carried the brand into national distribution.</p>
            </div>
          </div>
          <div class="timeline-item">
            <p class="timeline-date">2013&ndash;2023</p>
            <div>
              <p class="display-lg" style="margin-bottom: var(--space-2);">Puddle Pirate Co. &middot; Founder</p>
              <p class="text-muted">A lifestyle brand for the Coast Guard community. Built it, ran it for ten years, sold it in 2023.</p>
            </div>
          </div>
          <div class="timeline-item">
            <p class="timeline-date">2004&ndash;2008</p>
            <div>
              <p class="display-lg" style="margin-bottom: var(--space-2);">U.S. Coast Guard</p>
              <p class="text-muted">Four years of active duty, stationed out of Charleston, South Carolina, where I started in design.</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section id="philosophy" class="section section--tight" style="border-top: 1px solid var(--color-border); scroll-margin-top: 96px;">
      <div class="wrap" style="max-width: var(--content-default); margin-inline: auto;">
        <p class="eyebrow">Philosophy</p>
        <h2 class="display-xl" style="margin-bottom: var(--space-8);">How I work</h2>
        <div class="prose">
          <p>I learned discipline before I learned design. Four years in the Coast Guard taught me that a plan is only as good as the person willing to run it at 4 a.m. in bad weather. Design school could not have taught me that. Neither could a portfolio review.</p>
          <p>Most creative work fails at the handoff, not the concept. A good idea sitting in a deck is worth nothing on its own. I care more about what ships than what pitches well, and I structure every project around that: fewer rounds of exploration, more rounds of production.</p>
          <p>Owning brands changed how I advise them. When the P&amp;L is mine, a font choice stops being a debate and starts being a decision with a deadline and a cost attached. I bring that same pressure to client work, because it makes the work better and it respects the client&rsquo;s money.</p>
          <p>I read Marcus Aurelius the way I read a production schedule: the obstacle is the work. Move through it.</p>
        </div>
      </div>
    </section>
  </main>
'''

b.write_page(
    "about.html",
    "about.html",
    "About \u2014 Chris Edington",
    "Coast Guard veteran turned creative director and founder. The full story behind Edington Studio, Quell, Mr. Sniff\u2019s, and Puddle Pirate Co.",
    ABOUT_MAIN,
)

print("done: about")

# ---------------------------------------------------------------- GOVERNMENT
GOVERNMENT_MAIN = '''  <main id="main">
    <section class="page-hero">
      <div class="wrap">
        <p class="eyebrow">Government &amp; public sector</p>
        <h1 class="display-3xl" style="margin-bottom: var(--space-4);">Certified.<br />Registered.<br />Ready to bid.</h1>
        <p class="lede">Edington Studio is a veteran-owned small business built for public sector branding, marketing, and web work.</p>
      </div>
    </section>

    <section class="section section--tight">
      <div class="wrap">
        <div class="prose" style="margin-bottom: var(--space-10);">
          <p>I served in the U.S. Coast Guard from 2004 to 2008. Edington Studio carries that into how it&rsquo;s certified and how it works with government buyers: registered, documented, and built for the compliance a contracting officer needs to see before anything else.</p>
        </div>
        <div class="badge-row" style="margin-bottom: var(--space-12);">
          <span class="badge">''' + SHIELD + ''' VOSB &middot; SBA VetCert</span>
          <span class="badge">''' + SHIELD + ''' SBA-certified small business</span>
          <span class="badge">''' + SHIELD + ''' PA Small Business + VBE</span>
        </div>

        <div class="card" style="margin-bottom: var(--space-10);">
          <dl class="info-grid">
            <div class="info-item">
              <dt>Entity</dt>
              <dd>Edington Studios LLC, DBA Edington Studio</dd>
            </div>
            <div class="info-item">
              <dt>UEI</dt>
              <dd>HVAJPX7E34T1</dd>
            </div>
            <div class="info-item">
              <dt>CAGE code</dt>
              <dd>18RE5</dd>
            </div>
            <div class="info-item">
              <dt>SAM.gov status</dt>
              <dd>Active, expires Jan 29, 2027</dd>
            </div>
            <div class="info-item">
              <dt>NAICS 541430 (primary)</dt>
              <dd>Graphic design, identity &amp; packaging</dd>
            </div>
            <div class="info-item">
              <dt>NAICS 541613</dt>
              <dd>Marketing consulting</dd>
            </div>
            <div class="info-item">
              <dt>NAICS 541511</dt>
              <dd>Custom web development (Shopify, Webflow)</dd>
            </div>
            <div class="info-item">
              <dt>NAICS 541810</dt>
              <dd>Advertising</dd>
            </div>
          </dl>
        </div>

        <div class="card" style="margin-bottom: var(--space-10);">
          <p class="display-md" style="margin-bottom: var(--space-3);">Capabilities statement</p>
          <p class="text-muted" style="margin-bottom: var(--space-5);">Available on request. Email and I&rsquo;ll send the current version.</p>
          <a class="btn btn-primary" href="mailto:chris@edington.co?subject=Capabilities%20statement%20request">Request capabilities statement</a>
        </div>

        <div class="card">
          <p class="display-md" style="margin-bottom: var(--space-3);">Point of contact</p>
          <p style="font-weight: 600;">Chris Edington</p>
          <p class="text-muted" style="margin-bottom: var(--space-1);">Edington Studios LLC, DBA Edington Studio</p>
          <a href="mailto:chris@edington.co" style="color: var(--color-fg); font-weight: 600; text-decoration: none; display: block;">chris@edington.co</a>
          <a href="tel:+19199461693" style="color: var(--color-fg); font-weight: 600; text-decoration: none; display: block;">919.946.1693</a>
        </div>
      </div>
    </section>
  </main>
'''

b.write_page(
    "government.html",
    "government.html",
    "Government \u2014 Chris Edington",
    "Edington Studio is a VOSB, SBA-certified small business, and PA VBE registered on SAM.gov. Certifications, NAICS codes, and a direct point of contact.",
    GOVERNMENT_MAIN,
)

# ---------------------------------------------------------------- NOTES
NOTES_MAIN = '''  <main id="main">
    <section class="page-hero">
      <div class="wrap">
        <p class="eyebrow">Notes</p>
        <h1 class="display-3xl" style="margin-bottom: var(--space-4);">Things I&rsquo;ve written down</h1>
        <p class="lede">Short, occasional. On brand, business, and building more than one thing at a time.</p>
      </div>
    </section>

    <section class="wrap">
      <article id="discipline-is-the-strategy" class="note-entry">
        <p class="note-meta">On building</p>
        <h2 class="display-xl" style="margin-bottom: var(--space-6);">Discipline is the strategy</h2>
        <div class="prose">
          <p>Every founder I&rsquo;ve worked with has a strategy deck. Almost none of them have a production calendar. That&rsquo;s the gap. Strategy tells you what to build. Discipline is what actually builds it.</p>
          <p>I learned this before I learned branding. In the Coast Guard, the plan mattered less than whether you showed up and executed it in bad conditions. Design school never taught me that. Running two of my own consumer brands did.</p>
          <p>When I sit down with a founder now, I spend less time on the mood board than most creative directors would like to admit. I spend more time on the calendar: what ships this week, who owns it, what happens if it slips. A brand with a beautiful identity and no production discipline is a brand that never launches.</p>
          <p>Strategy is the map. Discipline is the mileage. Most businesses fail on the second one, not the first.</p>
        </div>
      </article>

      <article id="what-owning-it-taught-me" class="note-entry">
        <p class="note-meta">On owning what you sell</p>
        <h2 class="display-xl" style="margin-bottom: var(--space-6);">What running my own P&amp;L taught me</h2>
        <div class="prose">
          <p>Client work teaches you craft. Owning a brand teaches you consequence.</p>
          <p>When I advised brands as a creative director, a bad packaging decision was a hard conversation. Owning Puddle Pirate Co., and now Quell and Mr. Sniff&rsquo;s, made a bad packaging decision a cost I pay, a shipment I have to explain, a customer I have to win back myself. That difference changes how carefully you work.</p>
          <p>It also changes what you charge for. I don&rsquo;t sell mood boards anymore. I sell the judgment that comes from having paid for my own mistakes already. That&rsquo;s what a founder is really hiring when they hire Edington Studio: someone who has run the numbers on his own brand and knows what a decision costs before he makes it for yours.</p>
          <p>Most creative directors have opinions about business. I have a P&amp;L with my name on it. That&rsquo;s the difference worth paying for.</p>
        </div>
      </article>
    </section>
  </main>
'''

b.write_page(
    "notes.html",
    "notes.html",
    "Notes \u2014 Chris Edington",
    "Short, occasional writing from Chris Edington on brand discipline, ownership, and building more than one thing at a time.",
    NOTES_MAIN,
)

# ---------------------------------------------------------------- CONTACT
MAIL_ICON = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 6-10 7L2 6"/></svg>'
PHONE_ICON = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.127.96.361 1.903.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0 1 22 16.92Z"/></svg>'
LINKEDIN_ICON = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6Z"/><rect x="2" y="9" width="4" height="12"/><circle cx="4" cy="4" r="2"/></svg>'
DRIBBBLE_ICON = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="10"/><path d="M8.56 2.75c4.37 6.03 6.02 9.42 8.03 17.72M2.25 12.06c5.36-.62 10.35-.75 15.16-2.11M4.15 18.19c1.75-3.62 5.02-8.72 9.63-12.34"/></svg>'

CONTACT_MAIN = '''  <main id="main">
    <section class="page-hero">
      <div class="wrap">
        <p class="eyebrow">Contact</p>
        <h1 class="display-3xl" style="margin-bottom: var(--space-4);">Say hello</h1>
        <p class="lede">No form. Just reach out directly.</p>
      </div>
    </section>

    <section class="section section--tight">
      <div class="wrap" style="max-width: var(--content-narrow); margin-inline: auto; display: flex; flex-direction: column; gap: var(--space-4);">
        <a class="contact-tile" href="mailto:chris@edington.co">
          <span>
            <span class="contact-tile-label">Email</span>
            <span class="contact-tile-value">chris@edington.co</span>
          </span>
          ''' + MAIL_ICON + '''
        </a>
        <a class="contact-tile" href="tel:+19199461693">
          <span>
            <span class="contact-tile-label">Phone</span>
            <span class="contact-tile-value">919.946.1693</span>
          </span>
          ''' + PHONE_ICON + '''
        </a>
        <a class="contact-tile" href="https://www.linkedin.com/in/chris-edington/" target="_blank" rel="noopener">
          <span>
            <span class="contact-tile-label">LinkedIn</span>
            <span class="contact-tile-value">in/chris-edington</span>
          </span>
          ''' + LINKEDIN_ICON + '''
        </a>
        <a class="contact-tile" href="https://dribbble.com/ChrisEdington" target="_blank" rel="noopener">
          <span>
            <span class="contact-tile-label">Dribbble</span>
            <span class="contact-tile-value">ChrisEdington</span>
          </span>
          ''' + DRIBBBLE_ICON + '''
        </a>
      </div>
    </section>

    <section class="section section--tight" style="border-top: 1px solid var(--color-border);">
      <div class="wrap" style="max-width: var(--content-narrow); margin-inline: auto; text-align: left;">
        <p class="display-md" style="margin-bottom: var(--space-3);">Looking for the studio?</p>
        <p class="text-muted" style="margin-bottom: var(--space-5);">For client and government work, visit the studio site directly.</p>
        <a class="btn-text" href="https://www.edington.co" target="_blank" rel="noopener">Visit edington.co ''' + ARROW + '''</a>
      </div>
    </section>
  </main>
'''

b.write_page(
    "contact.html",
    "contact.html",
    "Contact \u2014 Chris Edington",
    "Reach Chris Edington directly by email or phone. No forms.",
    CONTACT_MAIN,
)

print("done: government, notes, contact")
