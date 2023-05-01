function solution(str1, str2) {
    let answer = "";
    for (const i in str1) {
        answer += str1[i];
        answer += str2[i];
    }
    return answer;
}