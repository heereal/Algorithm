function solution(n, t) {
    let answer = n;
    for (i = 1; i <= t; i++) {
        answer = answer*2
    }
    return answer
}