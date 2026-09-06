// app.js — mobile nav + footer year
(function () {
  document.addEventListener('DOMContentLoaded', function () {
    var menuBtn = document.querySelector('[data-menu-toggle]');
    var nav = document.querySelector('[data-main-nav]');
    if (menuBtn && nav) {
      menuBtn.addEventListener('click', function () {
        var isOpen = nav.classList.toggle('is-open');
        menuBtn.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
        document.body.style.overflow = isOpen ? 'hidden' : '';
      });
      nav.querySelectorAll('a').forEach(function (link) {
        link.addEventListener('click', function () {
          nav.classList.remove('is-open');
          menuBtn.setAttribute('aria-expanded', 'false');
          document.body.style.overflow = '';
        });
      });
    }

    var yearEls = document.querySelectorAll('[data-year]');
    yearEls.forEach(function (el) {
      el.textContent = new Date().getFullYear();
    });

    initWorkStack();
  });

  // Work-card stack recede. Card i eases back as the NEXT card travels up
  // the viewport: progress runs 0 (next card entering at the bottom) to 1
  // (next card reaching its sticky pin line), so the recede tracks the
  // whole approach instead of popping in the last few hundred pixels.
  //
  // Two rules keep it smooth:
  // - Measure the next card's WRAP, never the card itself. Wraps are never
  //   transformed, so the measurement can't feed back into itself.
  // - Write a single --recede custom property; style.css derives the
  //   transform and dim from it, so nothing else fights over transform.
  function initWorkStack() {
    var wraps = Array.prototype.slice.call(document.querySelectorAll('.work-card-wrap'));
    if (wraps.length < 2) return;
    var cards = wraps.map(function (w) {
      return w.querySelector('.work-card');
    });
    if (cards.some(function (c) { return !c; })) return;

    var reduceMotion =
      window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    if (reduceMotion) return;

    var stickyTop = 100;
    function measure() {
      var t = parseFloat(getComputedStyle(cards[0]).top);
      if (!isNaN(t)) stickyTop = t;
    }

    var ticking = false;
    var last = [];

    function update() {
      ticking = false;
      var vh = window.innerHeight;
      var travel = Math.max(1, vh - stickyTop);
      for (var i = 0; i < cards.length - 1; i++) {
        var nextTop = wraps[i + 1].getBoundingClientRect().top;
        var p = (vh - nextTop) / travel;
        p = p < 0 ? 0 : p > 1 ? 1 : p;
        p = Math.round(p * 1000) / 1000;
        if (p !== last[i]) {
          last[i] = p;
          cards[i].style.setProperty('--recede', p);
        }
      }
    }

    function onScroll() {
      if (!ticking) {
        ticking = true;
        requestAnimationFrame(update);
      }
    }

    window.addEventListener('scroll', onScroll, { passive: true });
    window.addEventListener('resize', function () {
      measure();
      onScroll();
    });
    measure();
    update();
  }
})();
