export function generateRandomMatrixWithEdges(n, l) {
  //walidacja czy można zbudować graf
  const edgesLimit = (n*n-n) / 2
  if (l > edgesLimit) {
    throw new Error(`
      Cannot generate that much edgaes for this number of vertexes.
      For ${n} vertexes max ${edgesLimit} edges allowed.
    `);
  }

  l = parseInt(l);
  n = parseInt(n);
  let matrix = [];
  for (let i=0; i<n; i++){
    matrix[i]=[];
        for (let j=0; j<n; j++){
            matrix[i][j] = 0;
    }
  }

  while (l > 0) {
    let rand_i = randomNumber(0, n);
    let rand_j = randomNumber(rand_i, n);
    // console.log(rand_i, rand_j, l);

    if (rand_j != rand_i) {
      if (matrix[rand_i][rand_j] == 0) {
        matrix[rand_i][rand_j] = 1;
        l -= 1;
      }
    }
  }

  for (let i=0; i<n; i++){
    for (let j=0; j<(n-i); j++){
      matrix[j + i][i] = matrix[i][j + i];
    }
  }
  //macierz sąsiedztwa
  return matrix;
}

export function generateRandomMatrixWithProbability(n, p) {
  n = parseInt(n);
  p = parseFloat(p);

  // validate if given probability is within correct range
  if (p < 0 || p > 1) {
    throw new Error('Ivalid probability (p: [0, 1])');
  }

  let matrix = [];
  for (let i=0; i<n; i++) {
    matrix[i] = [];
    for (let j=0; j<n; j++) {
      matrix[i][j] = 0;
    }
  }

  for (let i=0; i<n; i++) {
    for (let j=0; j<(n-i); j++) {
      let r=Math.random();
      if (r<=p) {
        matrix[i][j + i] = 1;
      }
    matrix[i][i] = 0;
    }
  }

  for (let i=0; i<n; i++) {
    for (let j=0; j<(n-i); j++) {
      matrix[j + i][i] = matrix[i][j + i];
    }
  }
  //macierz sasiedztwa
  return matrix;
}

function randomNumber(min, max){
  const r = Math.random()*(max-min) + min
  return Math.floor(r)
}
