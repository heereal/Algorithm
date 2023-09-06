function solution(n) {
    const ternary = n.toString(3).split('').reverse().join('');
    return parseInt(ternary, 3);
}