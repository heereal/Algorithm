function solution(start, end) {
    return Array(end - start + 1).fill(0).map((v,i) => i + start);
}