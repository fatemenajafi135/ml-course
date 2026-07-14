/* Shared deck logic: scaling + keyboard + click navigation */
(function () {
  const SLIDE_W = 1280;
  const SLIDE_H = 720;
  const deck    = document.getElementById('deck');
  const slides  = Array.from(document.querySelectorAll('.slide'));
  const total   = slides.length;
  let current   = 0;

  function scale() {
    const s = Math.min(window.innerWidth / SLIDE_W, window.innerHeight / SLIDE_H) * 0.90;
    deck.style.transform = `translate(-50%, -50%) scale(${s})`;
  }

  function goTo(n) {
    slides[current].classList.remove('active');
    current = (n + total) % total;
    slides[current].classList.add('active');
    document.querySelectorAll('.progress').forEach(bar => {
      bar.style.width = ((current + 1) / total * 100) + '%';
    });
    document.querySelectorAll('.slide-num').forEach(el => {
      el.textContent = (current + 1) + ' / ' + total;
    });
  }

  document.addEventListener('keydown', e => {
    if (e.key === 'ArrowRight' || e.key === 'ArrowDown' || e.key === ' ') goTo(current + 1);
    if (e.key === 'ArrowLeft'  || e.key === 'ArrowUp')                    goTo(current - 1);
  });

  deck.addEventListener('click', e => {
    goTo(e.clientX > window.innerWidth / 2 ? current + 1 : current - 1);
  });

  window.addEventListener('resize', scale);
  scale();
  goTo(0);
})();
