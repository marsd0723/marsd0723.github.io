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
    let m = 128;
    let n = 72;
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            ctx.fillStyle = `rgb(${Math.random()*255} ${Math.random()*128} ${Math.random()*64})`;
            ctx.fillRect(i*(c.width/m), j*(c.height/n), (c.width/m), (c.height/n));
        }
    };
    requestAnimationFrame(drawPretty);
}


