function solution(n) {
    let array = [n];
    while (n !== 1) {
        n % 2 === 0 ? n = n / 2 : n = 3 * n + 1;
        array.push(n);
    }
    return array;
}