function solution(my_string) {
    let answer = ""
    for (i = my_string.length-1; i >= 0; i--) {
        answer += my_string[i]
    }
    return answer;
}