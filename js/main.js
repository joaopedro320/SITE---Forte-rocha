/* =========================================================
   Marmoraria Forte Rocha — interações (sem dependências)
   ========================================================= */
(() => {
  const $ = (s, c = document) => c.querySelector(s);
  const $$ = (s, c = document) => [...c.querySelectorAll(s)];
  const reduced = matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ---------- Rastreamento (GTM / GA4 / Meta Pixel, se instalados) ---------- */
  window.dataLayer = window.dataLayer || [];
  function track(event, params = {}) {
    window.dataLayer.push({ event, ...params });
    if (typeof window.gtag === 'function') window.gtag('event', event, params);
    if (typeof window.fbq === 'function' && event === 'whatsapp_click') window.fbq('track', 'Contact');
  }
  document.addEventListener('click', (e) => {
    const a = e.target.closest('[data-track]');
    if (a) track(a.dataset.track.startsWith('whatsapp') ? 'whatsapp_click' : a.dataset.track, { local: a.dataset.track, pagina: location.pathname });
  });

  const ano = $('#ano');
  if (ano) ano.textContent = new Date().getFullYear();

  /* ---------- Header, menu, voltar ao topo ---------- */
  const header = $('.site-header'), up = $('.go-up');
  const onScroll = () => {
    header.classList.toggle('is-scrolled', scrollY > 40);
    up.classList.toggle('is-on', scrollY > 700);
  };
  addEventListener('scroll', onScroll, { passive: true });
  onScroll();
  const toggle = $('.nav-toggle');
  const setMenu = (open) => {
    document.documentElement.classList.toggle('nav-open', open);
    toggle.setAttribute('aria-expanded', open);
    toggle.setAttribute('aria-label', open ? 'Fechar menu' : 'Abrir menu');
  };
  toggle.addEventListener('click', () => setMenu(!document.documentElement.classList.contains('nav-open')));
  $$('.main-nav a').forEach((a) => a.addEventListener('click', () => setMenu(false)));
  addEventListener('keydown', (e) => { if (e.key === 'Escape') setMenu(false); });

  /* ---------- Entrada ao rolar ---------- */
  const io = new IntersectionObserver((es) => es.forEach((e) => {
    if (!e.isIntersecting) return;
    e.target.classList.add('in');
    io.unobserve(e.target);
  }), { threshold: .15, rootMargin: '0px 0px -40px 0px' });
  $$('.rv, .perf').forEach((el) => io.observe(el));

  /* ---------- Contadores ---------- */
  const cio = new IntersectionObserver((es) => es.forEach((e) => {
    if (!e.isIntersecting) return;
    const el = e.target, end = +el.dataset.count;
    cio.unobserve(el);
    if (reduced) return;
    const t0 = performance.now(), dur = 2000;
    (function tick(t) {
      const p = Math.min(1, (t - t0) / dur);
      el.textContent = Math.round(end * (1 - Math.pow(1 - p, 3)));
      if (p < 1) requestAnimationFrame(tick);
    })(t0);
  }), { threshold: .6 });
  $$('[data-count]').forEach((el) => { if (!reduced) el.textContent = '0'; cio.observe(el); });

  /* ---------- Slider ---------- */
  const slider = $('.slider');
  if (slider) {
    const slides = $$('.slide', slider), dots = $$('.sl-dots button', slider);
    let i = 0, timer;
    const go = (n) => {
      i = (n + slides.length) % slides.length;
      slides.forEach((s, k) => { s.classList.toggle('is-on', k === i); s.setAttribute('aria-hidden', k !== i); });
      dots.forEach((d, k) => { d.classList.remove('is-on'); void d.offsetWidth; d.classList.toggle('is-on', k === i); });
      const cur = $('.sl-cur', slider); if (cur) cur.textContent = String(i + 1).padStart(2, '0');
      clearInterval(timer);
      if (!reduced) timer = setInterval(() => go(i + 1), 6000);
    };
    $('.sl-next', slider).addEventListener('click', () => go(i + 1));
    $('.sl-prev', slider).addEventListener('click', () => go(i - 1));
    dots.forEach((d, k) => d.addEventListener('click', () => go(k)));
    let sx = 0;
    slider.addEventListener('touchstart', (e) => { sx = e.touches[0].clientX; }, { passive: true });
    slider.addEventListener('touchend', (e) => { const dx = e.changedTouches[0].clientX - sx; if (Math.abs(dx) > 50) go(i + (dx < 0 ? 1 : -1)); });
    go(0);
  }

  /* ---------- Depoimentos (carrossel) ---------- */
  $$('.depo-wrap').forEach((wrap) => {
    const track = $('.depo-track', wrap), cards = $$('.depo', track);
    const dotsBox = wrap.parentElement.querySelector('.depo-dots');
    let i = 0, timer;
    const perView = () => (innerWidth > 960 ? 2 : 1);
    const pages = () => Math.max(1, cards.length - perView() + 1);
    const paint = () => {
      dotsBox.innerHTML = '';
      for (let k = 0; k < pages(); k++) {
        const b = document.createElement('button'); b.type = 'button'; b.setAttribute('aria-label', `Depoimento ${k + 1}`);
        if (k === i) b.className = 'is-on';
        b.addEventListener('click', () => go(k));
        dotsBox.appendChild(b);
      }
    };
    const go = (n) => {
      i = (n + pages()) % pages();
      const w = cards[0].getBoundingClientRect().width + 30;
      track.style.transform = `translateX(${-i * w}px)`;
      paint();
      clearInterval(timer);
      if (!reduced) timer = setInterval(() => go(i + 1), 5500);
    };
    addEventListener('resize', () => go(Math.min(i, pages() - 1)));
    let sx = 0;
    wrap.addEventListener('touchstart', (e) => { sx = e.touches[0].clientX; }, { passive: true });
    wrap.addEventListener('touchend', (e) => { const dx = e.changedTouches[0].clientX - sx; if (Math.abs(dx) > 50) go(i + (dx < 0 ? 1 : -1)); });
    go(0);
  });

  /* ---------- Filtros da galeria ---------- */
  const grid = $('#gal-grid');
  if (grid) {
    const chips = $$('.filters .chip');
    chips.forEach((c) => c.addEventListener('click', () => {
      const f = c.dataset.f;
      chips.forEach((x) => { x.classList.toggle('is-on', x === c); x.setAttribute('aria-pressed', x === c); });
      $$('.gal-item', grid).forEach((el, k) => {
        const ok = f === 'all' || el.dataset.cat === f;
        el.classList.toggle('is-hidden', !ok);
        if (ok) { el.classList.remove('in'); el.style.setProperty('--d', k % 4); requestAnimationFrame(() => el.classList.add('in')); }
      });
    }));
    if (location.hash) {
      const t = $(location.hash);
      if (t) { t.classList.add('in', 'is-flash'); setTimeout(() => t.classList.remove('is-flash'), 2500); }
    }
  }

  /* ---------- Lightbox ---------- */
  const dlg = $('#lightbox');
  if (dlg && typeof dlg.showModal === 'function') {
    const im = $('#lb-img'), cap = $('#lb-cap'), cnt = $('#lb-count'), extra = $('#lb-extra');
    let list = [], idx = 0;
    const show = (n) => {
      idx = (n + list.length) % list.length;
      const a = list[idx];
      im.style.animation = 'none'; void im.offsetWidth; im.style.animation = '';
      im.src = a.getAttribute('href'); im.alt = a.dataset.cap || '';
      cap.textContent = a.dataset.cap || '';
      cnt.textContent = `${idx + 1} / ${list.length}`;
      extra.innerHTML = a.dataset.wa ? `<a class="btn btn-brown" href="${a.dataset.wa}" target="_blank" rel="noopener" data-track="whatsapp_pedra"><svg><use href="#i-wa"/></svg> Orçamento com esta pedra</a>` : '';
    };
    document.addEventListener('click', (e) => {
      const a = e.target.closest('[data-lightbox]'); if (!a) return;
      e.preventDefault();
      list = $$(`[data-lightbox="${a.dataset.lightbox}"]:not(.is-hidden)`);
      show(list.indexOf(a));
      dlg.showModal(); document.body.classList.add('is-locked');
      track('galeria_abrir', { item: a.dataset.cap });
    });
    dlg.addEventListener('close', () => document.body.classList.remove('is-locked'));
    $('[data-close]', dlg).addEventListener('click', () => dlg.close());
    $('.lb-prev', dlg).addEventListener('click', () => show(idx - 1));
    $('.lb-next', dlg).addEventListener('click', () => show(idx + 1));
    dlg.addEventListener('click', (e) => { if (e.target === dlg || e.target.classList.contains('lb-figure')) dlg.close(); });
    dlg.addEventListener('keydown', (e) => { if (e.key === 'ArrowRight') show(idx + 1); if (e.key === 'ArrowLeft') show(idx - 1); });
    let sx = 0;
    dlg.addEventListener('touchstart', (e) => { sx = e.touches[0].clientX; }, { passive: true });
    dlg.addEventListener('touchend', (e) => { const dx = e.changedTouches[0].clientX - sx; if (Math.abs(dx) > 50) show(idx + (dx < 0 ? 1 : -1)); });
  }

  /* ---------- Formulário → WhatsApp ---------- */
  const form = $('#orcamento-form');
  if (form) {
    const tel = $('#f-tel', form), nome = $('#f-nome', form), msg = $('.form-msg', form);
    tel.addEventListener('input', () => {
      const d = tel.value.replace(/\D/g, '').slice(0, 11);
      tel.value = d.length > 6 ? `(${d.slice(0, 2)}) ${d.slice(2, d.length - 4)}-${d.slice(-4)}` : d.length > 2 ? `(${d.slice(0, 2)}) ${d.slice(2)}` : d;
    });
    form.addEventListener('submit', (e) => {
      e.preventDefault();
      const badNome = nome.value.trim().length < 2, badTel = tel.value.replace(/\D/g, '').length < 10;
      nome.classList.toggle('is-invalid', badNome); nome.setAttribute('aria-invalid', badNome);
      tel.classList.toggle('is-invalid', badTel); tel.setAttribute('aria-invalid', badTel);
      if (badNome || badTel) { msg.textContent = 'Preencha seu nome e um telefone com DDD.'; (badNome ? nome : tel).focus(); return; }
      const v = (id) => $(id, form).value.trim();
      const linhas = ['Olá! Vim pelo site da Forte Rocha e quero um orçamento.', '',
        `*Nome:* ${v('#f-nome')}`, `*Telefone:* ${v('#f-tel')}`, `*Projeto:* ${v('#f-tipo')}`, `*Material:* ${v('#f-mat')}`];
      if (v('#f-msg')) linhas.push(`*Mensagem:* ${v('#f-msg')}`);
      track('whatsapp_click', { local: 'formulario', pagina: location.pathname });
      track('generate_lead', { tipo: v('#f-tipo'), material: v('#f-mat') });
      msg.textContent = 'Abrindo o WhatsApp com a sua mensagem…';
      window.open(`https://wa.me/5519993648081?text=${encodeURIComponent(linhas.join('\n'))}`, '_blank', 'noopener');
    });
  }

  /* ---------- Mapa (carrega perto da tela) ---------- */
  const map = $('iframe[data-src]');
  if (map) {
    const mio = new IntersectionObserver((es) => { if (es[0].isIntersecting) { map.src = map.dataset.src; mio.disconnect(); } }, { rootMargin: '400px' });
    mio.observe(map);
  }

  /* ---------- Parallax leve (imagens com data-par) ---------- */
  const par = $$('[data-par]');
  if (par.length && !reduced) {
    let ticking = false;
    const run = () => {
      const vh = innerHeight;
      par.forEach((el) => {
        const r = el.parentElement.getBoundingClientRect();
        if (r.bottom < -100 || r.top > vh + 100) return;
        const p = (r.top + r.height / 2 - vh / 2) / vh; // -1..1 em torno do centro da tela
        el.style.transform = `translate3d(0, ${(-p * +el.dataset.par).toFixed(2)}%, 0) scale(1.15)`;
      });
      ticking = false;
    };
    addEventListener('scroll', () => { if (!ticking) { ticking = true; requestAnimationFrame(run); } }, { passive: true });
    run();
  }

  /* ---------- Balão do WhatsApp (aparece uma vez) ---------- */
  const wa = $('.wa-float');
  if (wa) setTimeout(() => { wa.classList.add('show-tip'); setTimeout(() => wa.classList.remove('show-tip'), 5000); }, 4000);
})();
