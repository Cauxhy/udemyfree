const menuButton = document.getElementById('menu-button');
const closeButton = document.getElementById('close-button');
const mobileMenu = document.getElementById('mobile-menu');

menuButton.addEventListener('click', () => {
  mobileMenu.classList.remove('hidden');
  mobileMenu.classList.add('menu-enter', 'menu-enter-active');
  mobileMenu.classList.remove('menu-exit');
});
closeButton.addEventListener('click', () => {
  mobileMenu.classList.add('menu-exit', 'menu-exit-active');
  setTimeout(() => {
    mobileMenu.classList.add('hidden');
    mobileMenu.classList.remove('menu-enter', 'menu-enter-active', 'menu-exit', 'menu-exit-active');
  }, 300); // Animation duration
});