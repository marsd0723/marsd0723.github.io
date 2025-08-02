var c = document.getElementById("canvas");
var ctx = c.getContext("2d");

window.onload = function(){
    window.onresize();
}

window.onresize = function(){
    c.height = window.innerHeight;
    c.width = window.innerWidth; 
    drawPretty();
}

function drawPretty(){
    for (let i = 0; i < 32; i++) {
        for (let j = 0; j < 18; j++) {
            ctx.fillStyle = `rgb(${Math.random()*255} ${Math.random()*255} ${Math.random()*255})`;
            ctx.fillRect(i*(c.width/32), j*(c.height/18), (c.width/32), (c.height/18));
        }
    };
    requestAnimationFrame(drawPretty);
}


