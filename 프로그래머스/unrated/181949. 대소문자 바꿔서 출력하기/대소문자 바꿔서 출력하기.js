const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let input = [];

rl.on('line', function (line) {
    console.log([...line].map((str) => str.toUpperCase() === str ? str.toLowerCase() : str.toUpperCase()).join(""))
});