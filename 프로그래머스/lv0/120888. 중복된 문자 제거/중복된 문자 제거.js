function solution(my_string) {
    let answer = "";
    my_string.split("").forEach((item) => answer.includes(item) ? null : answer += item)
    return answer;
}