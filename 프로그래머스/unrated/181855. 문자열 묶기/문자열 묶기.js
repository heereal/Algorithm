function solution(strArr) {
    const sortedArr = strArr.sort((a, b) => b.length - a.length);
    let numArr = strArr.reduce((arr, str) => { 
        arr[str.length - 1]++;
        return arr;
    }, Array(sortedArr[0].length).fill(0))
    return Math.max(...numArr);
}