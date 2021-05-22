const loadDataNavButton = document.getElementById('load-data-nav-btn')
const generateRandomNavButton = document.getElementById('generate-random-nav-btn')

const loadDataPanel = document.getElementById('generate-random-panel')
const generateRandomPanel = document.getElementById('load-data-panel')



loadDataNavButton.addEventListener('click', handleChangePanel);
generateRandomNavButton.addEventListener('click', handleChangePanel);

function handleChangePanel() {
  loadDataNavButton.classList.toggle('active-button');
  generateRandomNavButton.classList.toggle('active-button');

  loadDataPanel.classList.toggle('open-panel');
  generateRandomPanel.classList.toggle('open-panel');
}