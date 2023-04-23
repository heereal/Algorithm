function solution(d, budget) {
    let sum = 0;
    let answer = 0;
    d.sort((a,b) => a - b);
    for (const num of d) {
        sum += num;
        if (sum > budget) break;
        answer++;
    }
    return answer;
}