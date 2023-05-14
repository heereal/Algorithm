function solution(my_string, queries) {
    let answer = my_string;
    for (const [a, b] of queries) {
        let slice = answer.slice(a, b + 1);
        let start = answer.substr(0, a);
        let end = answer.substr(b + 1);
        answer = start + slice.split("").reverse().join("") + end;
    }
    return answer;
}