function solution(x) {
    let answer = 0;
    x.toString().split("").forEach((num) => answer += parseInt(num));
    return x % answer === 0 ? true : false;
}