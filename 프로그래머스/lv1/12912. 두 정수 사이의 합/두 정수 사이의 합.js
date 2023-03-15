function solution(a, b) {
    let answer = 0;
    for ( i = Math.min(a,b); i <= Math.max(a,b); i++) answer += i
    return answer;
}