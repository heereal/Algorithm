function solution(a, d, included) {
    return included.reduce((acc, cur, i) => acc + (cur && a + i * d), 0);
}