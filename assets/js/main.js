(function () {
  var body = document.body;
  var burger = document.querySelector('.burger');
  if (burger) {
    burger.addEventListener('click', function () {
      var open = body.classList.toggle('menu-open');
      burger.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  }
  // Mobile: tap a dropdown parent to expand it
  document.querySelectorAll('.has-dd > .nav-link').forEach(function (link) {
    link.addEventListener('click', function (e) {
      if (window.matchMedia('(max-width:1080px)').matches) {
        e.preventDefault();
        link.parentElement.classList.toggle('open');
      }
    });
  });

  // Carousels
  document.querySelectorAll('[data-carousel]').forEach(function (wrap) {
    var track = wrap.querySelector('.car-track');
    var step = function () {
      var c = track.querySelector('.team-card');
      return c ? c.getBoundingClientRect().width + 12 : 400;
    };
    var prev = wrap.querySelector('[data-prev]');
    var next = wrap.querySelector('[data-next]');
    if (prev) prev.addEventListener('click', function () { track.scrollBy({ left: -step(), behavior: 'smooth' }); });
    if (next) next.addEventListener('click', function () { track.scrollBy({ left: step(), behavior: 'smooth' }); });
  });

  // Reveal on scroll
  var els = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add('in'); io.unobserve(en.target); }
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });
    els.forEach(function (el) { io.observe(el); });
  } else {
    els.forEach(function (el) { el.classList.add('in'); });
  }

  // Demo request form -> opens an e-mail draft to Nebras
  var form = document.getElementById('demo-form');
  if (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var d = new FormData(form);
      var lines = ['Full name: ' + d.get('name'), 'Organization: ' + d.get('org'), 'Work e-mail: ' + d.get('email'),
        'Phone: ' + d.get('phone'), 'Solution: ' + d.get('solution'), '', d.get('message')];
      var href = 'mailto:info@nebrastech.com?subject=' + encodeURIComponent('Demo request - ' + (d.get('org') || d.get('name'))) +
        '&body=' + encodeURIComponent(lines.join('\n'));
      window.location.href = href;
      var note = form.querySelector('.form-note');
      if (note) note.style.display = 'block';
    });
  }
})();
