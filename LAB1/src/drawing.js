const canvas = document.getElementById('chart');

canvas.width = canvas.offsetWidth;
canvas.height = canvas.offsetHeight;


export function draw(matrix) {
  if (canvas.getContext) {
    for(let i = 0; i < matrix.length; i++){
      if(matrix.length != matrix[i].length) throw new Error('Invalid matrix dimensions!');
    }
    let ctx = canvas.getContext('2d');
    ctx.clearRect(0, 0, canvas.width, canvas.height);
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
          const offset = (i+1).toString().length*6;
          ctx.fillText(i, coords[i].x - offset, coords[i].y + 7);
      }
  }
}

export function clearCanvas() {
  let ctx = canvas.getContext('2d');
  ctx.clearRect(0, 0, canvas.width, canvas.height);
}