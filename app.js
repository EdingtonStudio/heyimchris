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
  // - Measure the next card's flow SENTINEL, never the card itself.
  //   Sentinels never stick or transform, so the measurement can't
  //   feed back into itself.
  // - Write a single --recede custom property; style.css derives the
  //   transform and dim from it, so nothing else fights over transform.
  function initWorkStack() {
    var sentinels = Array.prototype.slice.call(document.querySelectorAll('.work-sentinel'));
    var cards = Array.prototype.slice.call(document.querySelectorAll('.work-card'));
    if (cards.length < 2 || sentinels.length !== cards.length) return;

    var reduceMotion =
      window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    if (reduceMotion) return;

    var stickyTop = 100;
    function measure() {
      var t = parseFloat(getComputedStyle(cards[0]).top);
      if (!isNaN(t)) stickyTop = t;
    }

    // Damped follow, the Framer feel: each frame the applied value
    // eases a fraction of the way toward the scroll-derived target
    // instead of jumping to it, so the recede trails the scroll
    // slightly and settles with inertia. The rAF loop only runs
    // while something is still moving.
    var DAMPING = 0.16;
    var EPSILON = 0.0005;
    var target = [];
    var current = [];
    var running = false;

    function computeTargets() {
      var vh = window.innerHeight;
      var travel = Math.max(1, vh - stickyTop);
      for (var i = 0; i < cards.length - 1; i++) {
        var nextTop = sentinels[i + 1].getBoundingClientRect().top;
        var p = (vh - nextTop) / travel;
        target[i] = p < 0 ? 0 : p > 1 ? 1 : p;
      }
    }

    function tick() {
      computeTargets();
      var settled = true;
      for (var i = 0; i < cards.length - 1; i++) {
        var cur = current[i] || 0;
        var diff = target[i] - cur;
        if (Math.abs(diff) > EPSILON) {
          cur += diff * DAMPING;
          settled = false;
        } else {
          cur = target[i];
        }
        if (cur !== current[i]) {
          current[i] = cur;
          cards[i].style.setProperty('--recede', cur.toFixed(4));
        }
      }
      if (settled) {
        running = false;
      } else {
        requestAnimationFrame(tick);
      }
    }

    function wake() {
      if (!running) {
        running = true;
        requestAnimationFrame(tick);
      }
    }

    window.addEventListener('scroll', wake, { passive: true });
    window.addEventListener('resize', function () {
      measure();
      wake();
    });
    measure();
    wake();
  }
})();
