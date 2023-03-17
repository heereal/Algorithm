function solution(absolutes, signs) {
    return absolutes.map((num, i) => signs[i] && num ? num : -num).reduce((acc, cur) => acc + cur, 0);
}