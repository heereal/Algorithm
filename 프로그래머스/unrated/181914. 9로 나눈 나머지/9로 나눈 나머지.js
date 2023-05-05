function solution(number) {
    return number.split("").reduce((acc, cur) => acc + parseInt(cur), 0) % 9;
}