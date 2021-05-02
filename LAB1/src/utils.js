import { adjListToAdjMatrix } from './conversions';


export function createEmptyMatrix(n, m) {
  const matrix = [];

  for (let i = 0; i < n; i++) {
    matrix.push(new Array(m).fill(0));
  }

  return matrix;
}

export function transposeMatrix(matrix) {
  const transposedMatrix = [];

  if (matrix.length) {
    for (let i = 0; i < matrix[0].length; i++) {
      transposedMatrix.push([]);
    }
  
    for (let i = 0; i < matrix.length; i++) {
      for (let j = 0; j < matrix[0].length; j++) {
        transposedMatrix[j][i] = matrix[i][j];
      }
    }
  }

  return transposedMatrix;
}

export function isEqualMatrix(first, seccond) {
  if (first.length !== seccond.length) {
    return false;
  }

  if (first[0].length !== seccond[0].length) {
    return false;
  }

  for (let i = 0; i < first.length; i++) {
    for (let j = 0; j < first[0].length; j++) {
      if (first[i][j] !== seccond[i][j]) {
        return false;
      }
    }
  }

  return true;
}

export function isMatrixBuiltOfZerosAndOnesOnly(matrix) {
  let result = true;

  for (let i = 0; i < matrix.length; i++) {
    for (let j = 0; j < matrix[i].length; j++) {
      if (matrix[i][j] != 0 && matrix[i][j] != 1) {
        result = false;
        break;
      }
    }
  }

  return result;
}

export function calculateMatrixTrace(matrix) {
  let trace = 0;

  for (let i = 0; i < matrix.length; i++) {
    trace += matrix[i][i];
  }

  return trace;
}

export function isAdjacencyMatrix(inputRows) {
  const rowsCount = inputRows.length;
  let result = isMatrixBuiltOfZerosAndOnesOnly(inputRows);

  if (calculateMatrixTrace(inputRows) !== 0) {
    result = false;
  }

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

export function isIncidenceMatrix(inputRows) {
  const rowsCount = inputRows.length;
  const rowsLength = inputRows[0].length;
  let result = isMatrixBuiltOfZerosAndOnesOnly(inputRows);

  for (const row of inputRows) {
    if (row.length !== rowsLength) {
      result = false;
      break;
    }
  }

  if (result) {
    for (let i = 0; i < rowsLength; i++) {
      let oneOccurances = 0;
      console.log('kolumna: ' + i)
      for (let j = 0; j < rowsCount; j++) {
        console.log(inputRows[j][i]);
        if (inputRows[j][i] == 1) {
          oneOccurances++;
        }
      }

      console.log('jedynek: ' + oneOccurances)
      if (oneOccurances !== 2) {
        result = false;
        break;
      }
    }
  }

  return result;
}

export function isAdjacencyList(rows) {
  console.log(rows)
  const adjList = convertInputToAdjList(rows)
  console.log(adjList)
  return (
    rows.every(hasRowDotInFirstItem) && 
    doesConnectedVertexesContainSeccondVertexInList(adjList)
  );

  function hasRowDotInFirstItem(row) {
    return row.includes('.')
  }

  function doesConnectedVertexesContainSeccondVertexInList(rows) {
    const mat = adjListToAdjMatrix(rows);
    return isEqualMatrix(mat, transposeMatrix(mat));
  }
}


function convertInputToAdjList(rows) {
  const adjacencyList = {};

  for (let i = 0; i < rows.length; i++) {
    const cells = rows[i].split(' ').map(cell => parseInt(cell));
    adjacencyList[i + 1] = [];

    for (let j = 1; j < cells.length; j++) {
      adjacencyList[i + 1].push(cells[j]);
    }
  }

  return adjacencyList;
}