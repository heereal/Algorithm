function solution(arr, query) {
    let answer = [...arr];
    for (const i in query) {
        if (i % 2 === 0 ) answer = answer.slice(0, query[i] + 1);
        if (i % 2 !== 0 ) answer = answer.slice(query[i]);
    }
    return answer;
}