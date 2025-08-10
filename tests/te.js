const SIZE = 16;
const arr = new Array(SIZE).fill(0);
let sum = 0;

const start = Date.now();

for (let i = 0; i < 1_000_000_000; i++) {
    sum += i;
    arr[i % SIZE] = (arr[i % SIZE] + (sum & 0xFF)) % 100;
}

const end = Date.now();

const arrSum = arr.reduce((acc, val) => acc + val, 0);

console.log("Sum:", sum);
console.log("Array checksum:", arrSum);
console.log("Time:", (end - start) / 1000, "seconds");
