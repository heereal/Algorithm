function solution(array) {
    const numArr = Array(Math.max(...array) + 1).fill(0);
    for ( const num of array ) {
        numArr[num] += 1
    };
    return numArr.indexOf(Math.max(...numArr)) !== numArr.lastIndexOf(Math.max(...numArr)) ? -1 : numArr.indexOf(Math.max(...numArr));
}