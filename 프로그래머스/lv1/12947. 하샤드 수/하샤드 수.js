function solution(x) {
    return x % x.toString().split("").reduce((acc, cur) => parseInt(acc) + parseInt(cur), 0) === 0;
}