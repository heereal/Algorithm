function solution(numbers, n) {
    return numbers.reduce((acc, cur) => {
        if (acc > n) return acc;
        acc += cur;
        return acc;
    }, 0);
}