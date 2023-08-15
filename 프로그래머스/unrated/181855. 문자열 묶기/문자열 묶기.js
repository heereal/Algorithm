function solution(strArr) {
    const sortedArr = strArr.sort((a, b) => a.length - b.length);
    let numArr = strArr.reduce((arr, str) => { 
        arr[str.length - 1]++;
        return arr;
    }, Array(sortedArr[sortedArr.length - 1].length).fill(0))
    return numArr.sort((a, b) => a - b)[numArr.length - 1];
}