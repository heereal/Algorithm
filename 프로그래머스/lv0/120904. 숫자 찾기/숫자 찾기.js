function solution(num, k) {
    const answer = num.toString().split("").indexOf(k.toString())
    return answer === -1 ? -1 : answer + 1;
}