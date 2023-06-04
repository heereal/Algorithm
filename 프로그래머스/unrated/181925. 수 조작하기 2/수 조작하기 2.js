function solution(numLog) {
    let answer = '';
    for (let i = 0; i <= numLog.length - 2; i++) {
        let minus = numLog[i + 1] - numLog[i];
        if (minus === 1) answer += 'w';
        if (minus === -1) answer += 's';
        if (minus === 10) answer += 'd';
        if (minus === -10) answer += 'a'; 
    }
    return answer;
}