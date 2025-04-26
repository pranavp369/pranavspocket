function toggleMenu() {
    const menu = document.getElementById('mobileMenu');
    menu.classList.toggle('show');
  }

function toggleTheme() {
  const body = document.body;
  const isLight = body.classList.contains('light-mode');
  
  body.classList.toggle('light-mode', !isLight);
  body.classList.toggle('dark-mode', isLight);

  const newIcon = isLight ? '☀️' : '🌙';
  document.getElementById('themeToggle').innerText = newIcon;
  document.getElementById('themeToggleMobile').innerText = newIcon;
  }

document.getElementById('themeToggle').addEventListener('click', toggleTheme);
document.getElementById('themeToggleMobile').addEventListener('click', toggleTheme);