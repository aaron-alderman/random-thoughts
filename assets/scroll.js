const reveals = document.querySelectorAll('.reveal');
const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
      observer.unobserve(entry.target);
    }
  });
}, { threshold: 0.06, rootMargin: '0px 0px -40px 0px' });
reveals.forEach(el => observer.observe(el));

const sections = document.querySelectorAll('[id]');
const navLinks = document.querySelectorAll('.nav-link');
const navObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      navLinks.forEach(l => l.style.color = '');
      const active = document.querySelector('.nav-link[href="#' + entry.target.id + '"]');
      if (active) active.style.color = 'var(--gold-light)';
    }
  });
}, { threshold: 0.4 });
sections.forEach(s => navObserver.observe(s));
