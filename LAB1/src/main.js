import { 
  determineInputRepresentationType, 
  convertionStrategiesByRepresentationTypes,
  convertFromAdjacencyMatrix
} from './conversions';
import { generateRandomMatrixWithEdges, generateRandomMatrixWithProbability } from './random';
import { clearCanvas } from './drawing';


const errorMessageBox = document.getElementById('error-message');


document.form0.addEventListener('submit', e => {
  e.preventDefault();

  const rows = document.form0.data.value.trim().split('\n');
  errorMessageBox.textContent = '';

  try {
    const inputRepresentationType = determineInputRepresentationType(rows);
    const convertionStrategy = convertionStrategiesByRepresentationTypes.get(inputRepresentationType);

    convertionStrategy(rows);
  } catch(err) {
    clearCanvas();
    errorMessageBox.textContent = err.message;
  }
});

document.form1.addEventListener('submit', e => {
  e.preventDefault();
  errorMessageBox.textContent = '';

  const matrixDimenstin = parseInt(document.form1.vertexes.value);
  const edgesCount = parseInt(document.form1.edges.value);

  try {
    const adjMatrix = generateRandomMatrixWithEdges(matrixDimenstin , edgesCount);
    const adjMatrixStr = adjMatrix.map(row => row.join(" "));
    convertFromAdjacencyMatrix(adjMatrixStr);
  } catch(err) {
    clearCanvas();
    errorMessageBox.textContent = err.message;
  }
});



document.form2.addEventListener('submit', e => {
  e.preventDefault();
  errorMessageBox.textContent = '';
  
  const matrixDimenstin = parseInt(document.form2.vertexes.value);
  const probability = parseFloat(document.form2.probability.value);
  
  try {
    const adjMatrix = generateRandomMatrixWithProbability(matrixDimenstin, probability);
    const adjMatrixStr = adjMatrix.map(row => row.join(" "));
    convertFromAdjacencyMatrix(adjMatrixStr);
  } catch(err) {
    clearCanvas();
    errorMessageBox.textContent = err.message;
  }
})



// Logic for toggling "menu"
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