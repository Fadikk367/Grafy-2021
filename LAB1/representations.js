const programInput = document.getElementById('programInput');
const errorMessageBox = document.getElementById('error-message');

const adjMatrixBox = document.getElementById('adjacenty-matrix');
const adjListBox = document.getElementById('adjacenty-list');
const incMatrixBox = document.getElementById('incidence-matrix');
const btn = document.querySelector('button');

const REPRESENTATION_TYPES = {
  ADJACENCY_MATRIX: 'ADJACENCY_MATRIX',
  ADJACENCY_LIST: 'ADJACENCY_LIST',
  INCIDENCE_MATRIX: 'INCIDENCE_MATRIX'
};

const convertionStrategiesByRepresentationTypes = new Map([
  [REPRESENTATION_TYPES.ADJACENCY_MATRIX, convertFromAdjacencyMatrix],
  [REPRESENTATION_TYPES.ADJACENCY_LIST, convertFromAdjacencyList],
  [REPRESENTATION_TYPES.INCIDENCE_MATRIX, convertFromIncidenceMatrix]
]);

console.log(convertionStrategiesByRepresentationTypes)

programInput.addEventListener('input', () => {
  const rows = programInput.value.split('\n');
  errorMessageBox.textContent = '';

  try {
    const inputRepresentationType = determineInputRepresentationType(rows);
    const convertionStrategy = convertionStrategiesByRepresentationTypes.get(inputRepresentationType);

    convertionStrategy(rows);
  } catch(err) {
    errorMessageBox.textContent = err.message;
  }
});

function determineInputRepresentationType(rows) {
  const cells = rows.map(row => row.split(' ').map(item => parseInt(item, 10)));

  if (isAdjacencyMatrix(cells)) {
    return REPRESENTATION_TYPES.ADJACENCY_MATRIX;
  } else if (isAdjacencyList(rows)) {
    return REPRESENTATION_TYPES.ADJACENCY_LIST;
  } else if (isIncidenceMatrix(cells)) {
    return REPRESENTATION_TYPES.INCIDENCE_MATRIX;
  } else {
    throw new Error('Unsupported representation structure!');
  }
}

function convertFromAdjacencyMatrix(rows) {
  const adjacencyMatrix = rows.map(row => row.split(' ').map(item => parseInt(item, 10)));
  const incidenceMatrix = GraphRepresentationConverter.adjMatrixToIncidenceMatrix(adjacencyMatrix);
  const adjacencyList = GraphRepresentationConverter.incidenceMatrixToAdjList(incidenceMatrix);

  draw(adjacencyMatrix);
  printRepresentations(adjacencyMatrix, adjacencyList, incidenceMatrix)
}

function convertFromAdjacencyList(rows) {
  const adjacencyList = convertInputToAdjList(rows);
  const adjacencyMatrix = GraphRepresentationConverter.adjListToAdjMatrix(adjacencyList);
  const incidenceMatrix = GraphRepresentationConverter.adjMatrixToIncidenceMatrix(adjacencyMatrix);
  
  draw(adjacencyMatrix);
  printRepresentations(adjacencyMatrix, adjacencyList, incidenceMatrix)
}

function convertFromIncidenceMatrix(rows) {
  const incidenceMatrix = rows.map(row => row.split(' ').map(item => parseInt(item, 10)));
  const adjacencyMatrix = GraphRepresentationConverter.incidenceMatrixToAdjMatrix(incidenceMatrix);
  const adjacencyList = GraphRepresentationConverter.incidenceMatrixToAdjList(incidenceMatrix);

  draw(adjacencyMatrix);
  printRepresentations(adjacencyMatrix, adjacencyList, incidenceMatrix)
}

function printRepresentations(adjacencyMatrix, ajdacencyList, incidenceMatrix) {
  printAdjacencyMatrix(adjacencyMatrix);
  printAdjList(ajdacencyList);
  printIncidenceMatrix(incidenceMatrix);
}


class GraphRepresentationConverter {
  static adjMatrixToAdjList(adjacencyMatrix) {
    const adjacencyList = {};

    adjacencyMatrix.map((row, i) => {
      adjacentVertexes = []
      
      for (let j = 0; j < row.length; j++) {
        if (row[j] === 1) {
          adjacentVertexes.push(j);
        }
      }
  
      adjacencyList[i] = adjacentVertexes;
    });

    return adjacencyList;
  }

  static adjMatrixToIncidenceMatrix(adjacencyMatrix) {
    let incidenceMatrix = [];
    adjacencyMatrix.map((row, i) => {
      
      for (let j = i+1; j < row.length; j++) {
        if (row[j] === 1) {
          const edge = new Array(row.length).fill(0);
          edge[j] = 1;
          edge[i] = 1;
          incidenceMatrix.push(edge);
        }
      }
      
    });
  
    return transposeMatrix(incidenceMatrix);
  }

  static incidenceMatrixToAdjMatrix(incidenceMatrix) {
    const transposed = transposeMatrix(incidenceMatrix);
    let adjacencyMatrix = new Array(transposed[0].length);
    
    for (let i = 0; i < transposed[0].length; i++) {
        adjacencyMatrix[i] = new Array(transposed[0].length).fill(0);
    }

    transposed.map((edge) => {        
      const indexA = edge.findIndex(item => item === 1);
      const indexB = edge.lastIndexOf(1);  
      adjacencyMatrix[indexA][indexB] = 1;
      adjacencyMatrix[indexB][indexA] = 1;
    });

    return adjacencyMatrix;
  }

  static incidenceMatrixToAdjList(incidenceMatrix) {
    const transposed = transposeMatrix(incidenceMatrix);
    let listFromInc = {};

    for (let i = 0; i < transposed[0].length; i++) {
      listFromInc[i] = [];
    }

    transposed.map((edge) => {        
        const indexA = edge.findIndex(item => item === 1);
        const indexB = edge.lastIndexOf(1);  
        listFromInc[indexA].push(indexB);
        listFromInc[indexB].push(indexA);
      });
      
    return listFromInc;
  }

  static adjListToAdjMatrix(adjList) {
    console.log(adjList);
    let matrixDimenstion = Object.keys(adjList).length;
    let adjacencyMatrix = createEmptyMatrix(matrixDimenstion, matrixDimenstion);
  
    for (const [vertex, adjacentVertexes] of Object.entries(adjList)) {
      for (const adjacentVertex of adjacentVertexes) {
        adjacencyMatrix[vertex][adjacentVertex - 1] = 1;
      }
    }
  
    return adjacencyMatrix;
  }
}

function transposeMatrix(matrix) {
  const transposedMatrix = [];

  for (let i = 0; i < matrix[0].length; i++) {
    transposedMatrix.push([]);
  }

  for (let i = 0; i < matrix.length; i++) {
    for (let j = 0; j < matrix[0].length; j++) {
      transposedMatrix[j][i] = matrix[i][j];
    }
  }

  return transposedMatrix;
}


function isAdjacencyMatrix(inputRows) {
  const rowsCount = inputRows.length;
  let result = true;

  for (const row of inputRows) {
    if (row.length !== rowsCount) {
      result = false;
      break;
    }
  }

  if (result) {
    const transposed = transposeMatrix(inputRows);
    result = isEqualMatrix(inputRows, transposed);
  }

  return result;
}

function createEmptyMatrix(n, m) {
  const matrix = [];

  for (let i = 0; i < n; i++) {
    matrix.push(new Array(m).fill(0));
  }
  console.log(matrix);
  return matrix;
}

function isIncidenceMatrix(inputRows) {
  const rowsCount = inputRows.length;
  const rowsLength = inputRows[0].length;
  let result = true;

  for (const row of inputRows) {
    if (row.length !== rowsLength) {
      result = false;
      break;
    }
  }

  if (result) {
    for (let i = 0; i < rowsLength; i++) {
      let oneOccurances = 0;
      // console.log('kolumna: ' + i)
      for (let j = 0; j < rowsCount; j++) {
        // console.log(inputRows[j][i]);
        if (inputRows[j][i] == 1) {
          oneOccurances++;
        }
      }

      // console.log('jedynek: ' + oneOccurances)
      if (oneOccurances !== 2) {
        result = false;
        break;
      }
    }
  }

  return result;
}

function isAdjacencyList(rows) {
  return rows.every(hasRowDotInFirstItem);

  function hasRowDotInFirstItem(row) {
    return row.includes('.')
  }
}

function isEqualMatrix(first, seccond) {
  if (first.length !== seccond.length) {
    console.log('1 wymiar neizgodny')
    return false;
  }

  if (first[0].length !== seccond[0].length) {
    console.log('drugi wymiar neizgodny')
    return false;
  }

  for (let i = 0; i < first.length; i++) {
    for (let j = 0; j < first[0].length; j++) {
      if (first[i][j] !== seccond[i][j]) {
        console.log('elementy niezgodne')
        return false;
      }
    }
  }

  return true;
}

function convertInputToAdjList(rows) {
  const adjacencyList = {};

  for (let i = 0; i < rows.length; i++) {
    const cells = rows[i].split(' ').map(cell => parseInt(cell));
    adjacencyList[i] = [];

    for (let j = 1; j < cells.length; j++) {
      adjacencyList[i].push(cells[j]);
    }
  }

  return adjacencyList;
}


function printAdjList(adjList) {
  let result = ``;

  for (const [vertex, neighbours] of Object.entries(adjList)) {
    result += `<div>(${vertex}) => [${neighbours.join(',')}]</div>`;
  }

  adjListBox.innerHTML = result;
}

function printAdjacencyMatrix(adjMatrix) {
  let result = ``;

  for (const row of adjMatrix) {
    result += `<div>${row.join(' ')}</div>`;
  }

  adjMatrixBox.innerHTML = result;
}

function printIncidenceMatrix(incMatrix) {
  let result = ``;

  for (const row of incMatrix) {
    result += `<div>${row.join(' ')}</div>`;
  }

  incMatrixBox.innerHTML = result;
}






function draw(matrix) {
  let canvas = document.getElementById('chart');

  if (canvas.getContext) {
      for(let i = 0; i < matrix.length; i++){
          if(matrix.length != matrix[i].length) throw new Error('Invalid matrix dimensions!');
      }
      let ctx = canvas.getContext('2d');
      let n = matrix.length;
      let R = 0.4 * canvas.height;
      let coords = [];
      for(let i = 0; i < n; i++){
          let xValue = R*Math.cos((i)*(360/n)*(Math.PI/180)) + canvas.width/2;
          let yValue = R*Math.sin((i)*(360/n)*(Math.PI/180)) + canvas.height/2;
          coords.push({x: xValue, y: yValue});
      }

      for(let i = 0; i < n; i++){
          for(let j = 0; j < i; j++){
              if(parseInt(matrix[i][j]) != 0){
                  ctx.beginPath();
                  ctx.moveTo(coords[i].x, coords[i].y);
                  ctx.lineTo(coords[j].x, coords[j].y)
                  ctx.stroke();
              }
          }
      }

      ctx.font = "24px Times New Roman";
      for(let i = 0; i < n; i++){
          ctx.beginPath();
          ctx.arc(coords[i].x, coords[i].y, 20, 0, Math.PI*2);
          ctx.fillStyle = "lightblue";
          ctx.fill();
          ctx.strokeStyle = "blue";
          ctx.stroke();
          ctx.fillStyle = "black";
          ctx.fillText(i+1, coords[i].x - 5, coords[i].y + 7);
      }
  }
}