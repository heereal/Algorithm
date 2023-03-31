function solution(array, n) {
    let array2 = array.sort((a,b) => a-b).map((num) => Math.abs(n-num))
    let index = array2.indexOf(Math.min(...array2))
    return array[index]
}