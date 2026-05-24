/*
Esta seccion fue hecha con IA ya que por el momento no se mucho de JS, pero se puede mejorar con el tiempo, es un
carrusel horizontal que muestra las peliculas recien llegadas, y se pausa al hacer hover para que el usuario pueda
ver bien la pelicula sin que se mueva.
*/
(function () {
  const track = document.getElementById("stripTrack");
  if (!track) return;

  const speed = 0.3;
  let offset = 0;
  let animationId;
  let isPaused = false;

  // Pausar al hacer hover
  const container = document.getElementById("topStrip");
  container.addEventListener("mouseenter", () => (isPaused = true));
  container.addEventListener("mouseleave", () => (isPaused = false));

  function step() {
    if (!isPaused) {
      offset -= speed;
      const firstItem = track.firstElementChild;
      if (firstItem) {
        const itemWidth =
          firstItem.offsetWidth + parseFloat(getComputedStyle(track).gap || 0);
        if (offset <= -itemWidth) {
          track.appendChild(firstItem);
          offset += itemWidth;
        }
      }
      track.style.transform = `translateX(${offset}px)`;
    }
    animationId = requestAnimationFrame(step);
  }
  animationId = requestAnimationFrame(step);
})();
