function solution(age) {
    return (age + "").split("").map((n) => "abcdefghij"[n]).join("")
}