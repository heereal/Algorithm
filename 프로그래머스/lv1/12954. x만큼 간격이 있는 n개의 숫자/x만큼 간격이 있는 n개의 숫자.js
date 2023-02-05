function solution(x, n) {
    let answer = [];
    if ( x === 0 ) {
        answer = Array(n).fill(0)
    } else {
        for (i = x; Math.abs(i) <= Math.abs(x*n); i += x) {
            answer.push(i)
        }
    }
    return answer
}