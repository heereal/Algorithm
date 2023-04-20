function solution(arr) {
    let array = [];
    for (const num of arr) {
        if ( array[array.length-1] !== num) array.push(num)
    }
    return array;
}