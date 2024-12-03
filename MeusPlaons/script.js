function toggleSection(id, header) {
    const section = document.getElementById(id);
    const arrow = header.querySelector('.arrow');
  
    // Toggle the visibility of the section
    section.style.display = section.style.display === 'none' ? 'block' : 'none';
  
    // Toggle the 'rotated' class to rotate the arrow
    arrow.classList.toggle('rotated');
  }
  
  // Initialize the visibility of the sections
  document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('.plans').forEach(section => {
      section.style.display = 'none';
    });
    // Set initial arrow state to closed
    document.querySelectorAll('.arrow').forEach(arrow => {
      arrow.classList.add('rotated');
    });
  });
