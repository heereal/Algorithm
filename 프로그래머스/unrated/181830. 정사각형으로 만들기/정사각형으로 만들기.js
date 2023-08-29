function solution(arr) {
    const row = arr[0].length;
    const column = arr.length;
    
    if (column > row) {
        arr.map((v) => v.push(...Array(column - row).fill(0)));
    }
    if (row > column) {
        for(let i = 0; i < row - column; i++) {
            arr.push(Array(row).fill(0));
        }
    }
    return arr;
}