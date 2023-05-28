function solution(n, k) {
    return Array(Math.floor(n / k)).fill(0).map((_, index) => k * (index + 1));
}