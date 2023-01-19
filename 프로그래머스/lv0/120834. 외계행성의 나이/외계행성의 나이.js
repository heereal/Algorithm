function solution(age) {
    const arr = Array.from({ length: 26 }, (v, i) => String.fromCharCode(i + 97));
    return (age + "").split("").map((n) => arr[n]).join("")
}