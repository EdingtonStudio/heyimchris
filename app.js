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

  // Work-card stack: each card overlaps the next through a large negative
  // margin (see style.css). As the following card's top edge slides up over
  // this one's bottom edge, scale this card down slightly and nudge it up
  // so it visibly "recedes" behind the incoming card instead of a flat,
  // static hand-off. Progress is driven by the REAL measured overlap
  // between adjacent cards, not a fixed scroll distance, so it always
  // tracks what's actually happening on screen.
  function initWorkStack() {
    var cards = Array.prototype.slice.call(document.querySelectorAll('.work-card'));
    if (cards.length < 2) return;

    var reduceMotion =
      window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    if (reduceMotion) return;

    var RECEDE_RANGE = 240; // px of adjacent overlap over which the recede fully completes — must match style.css's OVERLAP_PULL (.work-card-wrap + .work-card-wrap margin-top)
    var ticking = false;

    function update() {
      ticking = false;
      for (var i = 0; i < cards.length; i++) {
        var next = cards[i + 1];
        if (!next) {
          cards[i].style.transform = '';
          continue;
        }
        var rect = cards[i].getBoundingClientRect();
        var nextRect = next.getBoundingClientRect();
        var overlap = rect.bottom - nextRect.top;
        var progress = overlap <= 0 ? 0 : overlap >= RECEDE_RANGE ? 1 : overlap / RECEDE_RANGE;
        var scale = 1 - progress * 0.06;
        var translate = progress * -28;
        cards[i].style.transform =
          progress === 0 ? '' : 'translateY(' + translate.toFixed(2) + 'px) scale(' + scale.toFixed(4) + ')';
      }
    }

    function onScroll() {
      if (!ticking) {
        ticking = true;
        requestAnimationFrame(update);
      }
    }

    window.addEventListener('scroll', onScroll, { passive: true });
    window.addEventListener('resize', onScroll);
    update();
  }
})();
