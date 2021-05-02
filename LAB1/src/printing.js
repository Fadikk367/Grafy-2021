const adjMatrixBox = document.getElementById('adjacenty-matrix');
const adjListBox = document.getElementById('adjacenty-list');
const incMatrixBox = document.getElementById('incidence-matrix');


export function printRepresentations(adjacencyMatrix, ajdacencyList, incidenceMatrix) {
  printAdjacencyMatrix(adjacencyMatrix);
  printAdjList(ajdacencyList);
  printIncidenceMatrix(incidenceMatrix);
}

export function printAdjList(adjList) {
  let result = ``;

  for (const [vertex, neighbours] of Object.entries(adjList)) {
    result += `<div>${vertex}. ${neighbours.join(' ')}</div>`;
  }

  adjListBox.innerHTML = result;
}

export function printAdjacencyMatrix(adjMatrix) {
  let result = ``;

  for (const row of adjMatrix) {
    result += `<div>${row.join(' ')}</div>`;
  }

  adjMatrixBox.innerHTML = result;
}

export function printIncidenceMatrix(incMatrix) {
  let result = ``;

  for (const row of incMatrix) {
    result += `<div>${row.join(' ')}</div>`;
  }

  incMatrixBox.innerHTML = result;
}