function toggleTheme() {
  const root = document.documentElement;
  const current = root.classList.contains('dark-theme') ? 'dark' : 'light';
  const newTheme = current === 'dark' ? 'light' : 'dark';
  root.classList.remove(current + '-theme');
  root.classList.add(newTheme + '-theme');
  localStorage.setItem('theme', newTheme);
}

document.addEventListener('DOMContentLoaded', () => {
  const saved = localStorage.getItem('theme') || 'light';
  document.documentElement.classList.add(saved + '-theme');
});
