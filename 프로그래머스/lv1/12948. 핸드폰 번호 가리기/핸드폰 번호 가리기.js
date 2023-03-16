function solution(phone_number) {
    let answer = "";
    for (i = 0; i <= phone_number.length - 1; i++) {
        i <= phone_number.length - 5 ? answer += "*" : answer += phone_number[i]
    }
    return answer;
}