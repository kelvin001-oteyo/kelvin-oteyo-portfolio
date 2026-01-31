const tabs = document.querySelectorAll('.tab-btn');
const contents = document.querySelectorAll('.tab-content');

tabs.forEach(tab => {
  tab.addEventListener('click', () => {
    tabs.forEach(t => t.classList.remove('active'));
    contents.forEach(c => c.classList.remove('active'));

    tab.classList.add('active');
    document.getElementById(tab.dataset.tab).classList.add('active');
  });
});
document.querySelectorAll('.skill-progress').forEach(bar => {
  const level = bar.dataset.level;
  bar.style.width = level + '%';
});


const projectCards = document.querySelectorAll('.project-card');

const observer = new IntersectionObserver(entries => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.style.opacity = 1;
      entry.target.style.transform = 'translateY(0)';
    }
  });
}, {
  threshold: 0.2
});

projectCards.forEach(card => observer.observe(card));



window.addEventListener('load', () => {
  document.querySelector('.hero').classList.add('show');
});

document.querySelectorAll('.fill').forEach(bar => {
  const width = bar.style.width;
  bar.style.width = '0';

  setTimeout(() => {
    bar.style.width = width;
  }, 500);
});







 