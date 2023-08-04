function solution(n) {
    let arr = Array(n).fill(Array(n).fill(0));
    return arr.map((numArr, fisrtIndex) => numArr.map((num, secondIndex) => fisrtIndex === secondIndex ? 1 : 0));
}