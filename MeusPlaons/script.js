function toggleSection(id, header) {
  const section = document.getElementById(id);
  const arrow = header.querySelector('.arrow');

  // Abilitar a visibilidade das abas
  if (section.style.display === 'none' || section.style.display === ''){
    section.style.display = 'block';
    arrow.classList.remove('rotated');
  }else{
    section.style.display = 'none';
    arrow.classList.add('rotated');
  }
}

// Inicializa a visibilidade das abas
document.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('.plans').forEach(section => {
    section.style.display = 'none';
  });
  // Definir o estado da seta como fechado
  document.querySelectorAll('.arrow').forEach(arrow => {
    arrow.classList.add('rotated');
  });
});
