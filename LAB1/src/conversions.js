import { 
  createEmptyMatrix, 
  transposeMatrix, 
  isAdjacencyMatrix, 
  isAdjacencyList, 
  isIncidenceMatrix 
} from './utils';
import { printRepresentations } from './printing';
import { draw } from './drawing';


export const REPRESENTATION_TYPES = {
  ADJACENCY_MATRIX: 'ADJACENCY_MATRIX',
  ADJACENCY_LIST: 'ADJACENCY_LIST',
  INCIDENCE_MATRIX: 'INCIDENCE_MATRIX'
};

export const convertionStrategiesByRepresentationTypes = new Map([
  [REPRESENTATION_TYPES.ADJACENCY_MATRIX, convertFromAdjacencyMatrix],
  [REPRESENTATION_TYPES.ADJACENCY_LIST, convertFromAdjacencyList],
  [REPRESENTATION_TYPES.INCIDENCE_MATRIX, convertFromIncidenceMatrix]
]);


export function determineInputRepresentationType(rows) {
  const cells = rows.map(row => row.split(' ').map(item => parseInt(item, 10)));
  console.log(1);
  if (!console.log(2) && isAdjacencyMatrix(cells)) {
    return REPRESENTATION_TYPES.ADJACENCY_MATRIX;
  } else if (!console.log(3) && isAdjacencyList(rows)) {
    return REPRESENTATION_TYPES.ADJACENCY_LIST;
  } else if (!console.log(4) && isIncidenceMatrix(cells)) {
    console.log(4);
    return REPRESENTATION_TYPES.INCIDENCE_MATRIX;
  } else {
    throw new Error('Invalid representation structure!');
  }
}

export function convertFromAdjacencyMatrix(rows) {
  console.log('adfj matrix')
  const adjacencyMatrix = rows.map(row => row.split(' ').map(item => parseInt(item, 10)));
  const incidenceMatrix = adjMatrixToIncidenceMatrix(adjacencyMatrix);
  const adjacencyList = adjMatrixToAdjList(adjacencyMatrix);

  draw(adjacencyMatrix);
  printRepresentations(adjacencyMatrix, adjacencyList, incidenceMatrix)
}

export function convertFromAdjacencyList(rows) {
  console.log('adfj list')
  const adjacencyList = convertInputToAdjList(rows);
  const adjacencyMatrix = adjListToAdjMatrix(adjacencyList);
  const incidenceMatrix = adjMatrixToIncidenceMatrix(adjacencyMatrix);
  
  draw(adjacencyMatrix);
  printRepresentations(adjacencyMatrix, adjacencyList, incidenceMatrix)
}

export function convertFromIncidenceMatrix(rows) {
  console.log('inc matrix')
  const incidenceMatrix = rows.map(row => row.split(' ').map(item => parseInt(item, 10)));
  const adjacencyMatrix = incidenceMatrixToAdjMatrix(incidenceMatrix);
  const adjacencyList = incidenceMatrixToAdjList(incidenceMatrix);

  draw(adjacencyMatrix);
  printRepresentations(adjacencyMatrix, adjacencyList, incidenceMatrix)
}

export function adjMatrixToAdjList(adjacencyMatrix) {
  const adjacencyList = {};

  adjacencyMatrix.map((row, i) => {
    const adjacentVertexes = []
      
    for (let j = 0; j < row.length; j++) {
      if (row[j] === 1) {
        adjacentVertexes.push(j+1);
      }
    }
  
    adjacencyList[i+1] = adjacentVertexes;
  });
    
  return adjacencyList;
}

export function adjMatrixToIncidenceMatrix(adjacencyMatrix) {
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

export function incidenceMatrixToAdjMatrix(incidenceMatrix) {
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

export function incidenceMatrixToAdjList(incidenceMatrix) {
  const transposed = transposeMatrix(incidenceMatrix);
  let listFromInc = {};

  for (let i = 0; i < transposed[0].length; i++) {
    listFromInc[i + 1] = [];
  }

  transposed.map((edge) => {        
      const indexA = edge.findIndex(item => item === 1);
      const indexB = edge.lastIndexOf(1);  
      listFromInc[indexA + 1].push(indexB + 1);
      listFromInc[indexB + 1].push(indexA + 1);
    });
      
  return listFromInc;
}

export function adjListToAdjMatrix(adjList) {
  let matrixDimenstion = Object.keys(adjList).length;
  let adjacencyMatrix = createEmptyMatrix(matrixDimenstion, matrixDimenstion);
  console.log(adjList);
  for (const [vertex, adjacentVertexes] of Object.entries(adjList)) {
    for (const adjacentVertex of adjacentVertexes) {
      adjacencyMatrix[vertex - 1][adjacentVertex - 1] = 1;
    }
  }
  
  return adjacencyMatrix;
}

function convertInputToAdjList(rows) {
  const adjacencyList = {};
  console.log('pre convert input')
  for (let i = 0; i < rows.length; i++) {
    const cells = rows[i].split(' ').map(cell => parseInt(cell));
    adjacencyList[i + 1] = [];

    for (let j = 1; j < cells.length; j++) {
      adjacencyList[i + 1].push(cells[j]);
    }
  }
  console.log('post convert input')
  return adjacencyList;
}