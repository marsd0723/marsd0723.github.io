const rows = 6;
const cols = 7;
const boardElement = document.getElementById('board');
var gameover = false;
var waiting = false;
var gamestart = false;

 // Generate empty board
for (let row = 0; row < rows; row++) {
    for (let col = 0; col < cols; col++) {
        const cell = document.createElement('div');
        cell.classList.add('cell');
        cell.dataset.row = row;
        cell.dataset.col = col;
        const img = document.createElement('img');
        img.src = "blank.png";
        cell.appendChild(img);
        boardElement.appendChild(cell);
    }
}

function updateLabel(s){
    document.getElementById('label').innerHTML = s;
    gameover = true;
    document.getElementById("stat").innerHTML = "Click to restart :)"
}

// // Example: Update a specific cell
// function setCell(row, col, imgSrc) {
//     const allCells = document.querySelectorAll('.cell');
//     const index = row * cols + col;
//     const cellImg = allCells[index].querySelector('img');
//     cellImg.src = imgSrc;
// }
function erase(){
    for (let row = rows-1; row >= 0; row--){
        for (let col= cols-1; col>= 0; col--){
            const index = row*cols + col;
            const cell = document.querySelectorAll('.cell')[index];
            const img = cell.querySelector('img');
            if (img.src.includes('red+.png')){
                img.src = 'red.png';
            }
            if (img.src.includes('yellow+.png')){
                img.src = 'yellow.png';
            }
        }
    }
}

    function dropPiece(col, color){
        for (let row = rows-1; row >= 0; row--){
            const index = row*cols + col;
            const cell = document.querySelectorAll('.cell')[index];
            const img = cell.querySelector('img');
            if (img.src.includes('blank.png')){
                img.src = color +'.png';
                return true;
            }
        }
        return false;
    }


    // Example: Handle click to drop piece
var r = 0;
    function getSvrRes(s, handler){
        console.log("waiting now");
        fetch(s) // Replace with your target URL
        .then(response => {
            if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
            }
            return response.text(); // Or .text(), .blob(), etc., depending on expected response type
        })
        .then(data => {
            let res = data.split(',');
            console.log("backend response: "+res);
            r = parseInt(res[0]);
            let status = parseInt(res[1]);
            let indic = res[2];
            if (gamestart) document.getElementById("stat").innerHTML = indic;
            if(status == -99) updateLabel("You Win!");
            if(status == -100) {handler(r, "yellow"); updateLabel("Draw Game!")};
            if(status == -101) {handler(r, "yellow"); updateLabel("You Lose!")};
            if (handler && status == 0) {erase(); handler(r, "yellow+");};
            waiting = false;
            console.log("waiting ends");
            return;
        })
        .catch(error => {
            console.error('There was a problem with the fetch operation:', error);
        });
    };

window.addEventListener('dragstart', function(e) {
    e.preventDefault();
});
window.addEventListener('selectstart', function(e) {
    e.preventDefault();
});

    document.getElementById("container").addEventListener('click', function(e) {
        gamestart = true;
        if (waiting) return;
        waiting = true;
        if (gameover) {window.location.reload(); return;};
        document.getElementById("stat").innerHTML = "AI Thinking...";
        let board = document.getElementById("board");
        let left = board.getBoundingClientRect().left;
        let colW = board.clientWidth / 7;
        let col = Math.floor((e.x-left) / colW);
        
        erase();
        if (!dropPiece(col, 'red+')) {waiting=false; return; };


        // Find the lowest empty row in that column
    //     for (let row = rows - 1; row >= 0; row--) {
    //         const index = row * cols + col;
    //         const targetCell = document.querySelectorAll('.cell')[index];
    //         const img = targetCell.querySelector('img');
    //         if (img.src.includes('blank.png') && count%2==1) {
    //             img.src = "red.png";
    //             break;
    //         }
    //         if (img.src.includes('blank.png') && count%2==0) {
    //             img.src = "yellow.png";
    //             break;
    //         }
    //     }
    // });
        getSvrRes('http://127.0.0.1:5100/connect4get?move='+col, dropPiece);
    })
window.onload = function(){
    getSvrRes('http://127.0.0.1:5100/reset')
}