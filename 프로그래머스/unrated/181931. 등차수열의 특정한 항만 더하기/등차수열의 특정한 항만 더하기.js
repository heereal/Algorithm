function solution(a, d, included) {
    let array = Array(included.length).fill(0).map((v, i) => a + i * d);
    return included.reduce((acc, cur, i) => acc + (cur && array[i]), 0);
}