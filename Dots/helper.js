var c = document.getElementById("canvas");
var ctx = c.getContext("2d", { alpha: false });

var beforeS = 0;

let fps = 0, counter = 0, lastTime = performance.now();

window.onload = function(){
    // window.onresize();
    c.height = window.innerHeight;
    c.width = window.innerWidth; 
    initDots();
    render();    
}

window.onresize = function(){

}

function getRan(min, max) {
  return Math.random() * (max - min) + min;
}

function drawPixel(x, y, color) {
  ctx.fillStyle = color;
  ctx.fillRect(Math.floor(x), Math.floor(y), 1, 1); // Use fillRect for better performance
}

function drawBall(x,y,r,c){
    ctx.save();
    ctx.fillStyle = c;
    ctx.beginPath();
    ctx.arc(x,y,r,0,Math.PI*2,true);
    ctx.fill();
    ctx.restore();
}

function updateFPS() {
  const now = performance.now();
  counter++;
  if (now - lastTime >= 1000) {
    fps = Math.round((counter * 1000) / (now - lastTime));
    counter = 0;
    lastTime = now;
  }
}
function showFPS() {
  ctx.save();
  ctx.font = "20px Arial";
  ctx.fillStyle = "lime";
  ctx.fillText(`FPS: ${fps}`, 10, 20);
  ctx.restore();
}

function render(){
    ctx.clearRect(0,0,c.width,c.height);
    updateFPS();
    
    for (let i=0; i<dots.length; i++) {
        dots[i].move(); 
        dots[i].render();
    };

    showFPS();
    requestAnimationFrame(render);
}

function drawPretty(){
    let m = 150;
    let n = 130;
    ctx.save();
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            ctx.fillStyle = `rgb(${getRan(200,255)} ${getRan(200, 250)} ${getRan(0,0)})`;
            ctx.fillRect(i*(c.width/m), j*(c.height/n), (c.width/m), (c.height/n));
        }
    };
    ctx.restore();
}
var count = 0; 
function throwBall(){
    ctx.save();
    for (let i = 0; i < 1000; i++){
        count++;
        x = Math.random() * c.width;
        y = Math.random() * c.height;
        size = Math.random() *2 + 1;
        // ctx.beginPath();
        // if (x>210 | y>110) ctx.arc(x, y, size, 0, Math.PI*2, true);
        // ctx.fillStyle = "rgba(32, 30, 32, 0.82)";
        // ctx.fill();
        if (x>200 | y>95) drawPixel(x,y,[255,255,255,255]);
    }
    ctx.font = "15px Arial";
    ctx.fillStyle = "green";
    ctx.fillText("Population: " + count, 50, 70);
    ctx.restore();
}

function initDots() {
  dots = []; // Clear existing dots
  for (let i = 0; i < 500; i++) { // Reduced to 1000 for better performance
    let l = Math.floor(Math.random() * 4) + 1;
    dots.push({
        l: l,
        x: Math.random() * canvas.width,
        y: Math.random() * canvas.height,
        vx: Math.pow(-1,l) *0* l, // Random velocity (-1 to 1)
        vy: Math.pow(-1,l) *1* l,
        c: "rgba(200,100,200,0.9)",
        r: l*1.3,
        move: function() {
            this.x += this.vx;
            this.y += this.vy;
            // Wrap around edges
            if (this.x < 0) this.x += canvas.width;
            if (this.x > canvas.width) this.x -= canvas.width;
            if (this.y < 0) this.y += canvas.height;
            if (this.y > canvas.height) this.y -= canvas.height;
        },
        render: function() {
            // drawPixel(this.x, this.y, this.c);
            ctx.globalCompositeOperation = "lighter";
            // drawBall(this.x, this.y, this.r, this.c);
            drawStar(this.x, this.y, this.r);
        }
    });
  }
}

function drawStar(x,y,r){
    let gradient = ctx.createRadialGradient(x, y, r, x, y, r*10);
    gradient.addColorStop(0, "rgba(0, 242, 255, 1)"); // Center: 0.1 brightness
    gradient.addColorStop(0.05, "rgba(255, 140, 255, 0.25)"); // Center: 0.1 brightness
    gradient.addColorStop(0.3, "rgba(255, 140, 255, 0.15)"); // Center: 0.1 brightness
    gradient.addColorStop(1, "rgba(255, 140, 255, 0)");   // Edge: fully transparent

    ctx.save();
    ctx.fillStyle=gradient;
    ctx.strokeStyle = "red";
    r = r* 5;
    ctx.fillRect(x-r*2,y-r*2,r*4,r*4);
    // ctx.strokeRect(x-r*2, y-r*2, r*4, r*4);
    ctx.restore();
}
