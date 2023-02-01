function solution(s) {
    let answer = 0;
    let array = s.split(" ")
    array.map((n, i) => n === "Z" ? answer -= parseInt(array[i - 1]) : answer += parseInt(array[i]))
    return answer;
}