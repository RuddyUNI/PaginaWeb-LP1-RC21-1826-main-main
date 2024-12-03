// Alternancia del modo oscuro
const darkModeToggle = document.getElementById('darkModeToggle');
const body = document.body;
const darkModeIcon = document.getElementById('darkModeIcon');

darkModeToggle.addEventListener('click', () => {
  body.classList.toggle('dark-mode');
  
  // Cambiar la imagen del icono según el modo
  if (body.classList.contains('dark-mode')) {
    darkModeIcon.src = '{% static "images/modo_oscuro_luna.png" %}'; // Imagen para modo oscuro
  } else {
    darkModeIcon.src = '{% static "images/modo_oscuro_sol.png" %}'; // Imagen para modo claro
  }
});
