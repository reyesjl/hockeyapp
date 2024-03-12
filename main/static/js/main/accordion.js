document.addEventListener("DOMContentLoaded", function() {
  const accordions = document.querySelectorAll('.accordion-item');

  function setActiveAccordion() {
    accordions.forEach(function(accordion) {
      const statusDot = accordion.querySelector('.status-dot');
      const panel = accordion.querySelector('.accordion-content');
      if (accordion.classList.contains('active')) {
        panel.style.display = 'block';
        statusDot.style.backgroundColor = 'green';
      } else {
        panel.style.display = 'none';
        statusDot.style.backgroundColor = 'gray';
      }
    });
  }

  function toggleAccordion(accordion) {
    const statusDot = accordion.querySelector('.status-dot');
    const panel = accordion.querySelector('.accordion-content');
    accordion.classList.toggle('active');
    panel.style.display = panel.style.display === 'block' ? 'none' : 'block';
    statusDot.style.backgroundColor = panel.style.display === 'block' ? 'green' : 'gray';
  }

  setActiveAccordion();

  accordions.forEach(function(accordion) {
    accordion.addEventListener('click', function() {
      accordions.forEach(function(item) {
        if (item !== accordion) {
          item.classList.remove('active');
          item.querySelector('.status-dot').style.backgroundColor = 'gray';
          item.querySelector('.accordion-content').style.display = 'none';
        }
      });
      toggleAccordion(accordion);
    });
  });
});