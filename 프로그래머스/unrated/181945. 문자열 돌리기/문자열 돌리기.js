const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.on('line', function (line) {
    const array = line.split("")
    for (const num of array) {
        console.log(num)
    }
});