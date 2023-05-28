function solution(my_string) {
    let answer = Array(52).fill(0);
    let alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz".split("");
    my_string.split("").forEach((str) => answer[alphabet.indexOf(str)] += 1);
    return answer;
}