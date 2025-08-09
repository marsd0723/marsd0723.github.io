var c = document.getElementById("canvas");
var ctx = c.getContext("2d");

var counter = 0;
var fps = 0;
var beforeS = 0;

window.onload = function(){
    window.onresize();
}

window.onresize = function(){
    c.height = window.innerHeight;
    c.width = window.innerWidth; 
    initDots();
    render();
}

function drawPixel(x, y, color){
    // Create an ImageData object
    const imageData = ctx.createImageData(1, 1);
    // Set the pixel color (e.g., red)
    imageData.data[0] = color[0]; // Red
    imageData.data[1] = color[1];   // Green
    imageData.data[2] = color[2];   // Blue
    imageData.data[3] = color[3]; // Alpha (0-255 opaque)
    // Put the pixel on the canvas
    ctx.putImageData(imageData, x, y);
}

function preFPS(){
    if (Math.floor(Date.now()/1000) != beforeS){
        fps = counter;
        counter = 0;
    }
    beforeS = Math.floor(Date.now()/1000);
    counter++;  
}

function showFPS(){
    ctx.save();
    ctx.font = "30px Arial";
    ctx.fillStyle = "green";
    ctx.fillText("fps: " + fps, 50, 40);
    ctx.fillText("counter: " + counter, 50, 100);
    ctx.fillText(Math.floor(Date.now()/1000) +" : "+ beforeS, 50, 150);
    ctx.restore();
}

function render(){
    ctx.clearRect(0,0,c.width,c.height);
    preFPS();
    
    for (let i=0; i<dots.length; i++) {
        dots[i].move(); 
        dots[i].render();
    }

    showFPS();
    requestAnimationFrame(render);
}

var dots = [];

function initDots(){
    for (let i=0; i<2000; i++){
        x = Math.random() * c.width;
        y = Math.random() * c.height;
        dots.push({
            x: x, 
            y: y, 
            c: [255, 255, 255, 255],
            move: function(){
                this.x++;
                this.y++;
            },
            render: function(){
                drawPixel(this.x, this.y, this.c);
            }
        });
    } ;
}
