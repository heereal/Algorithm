function solution(q, r, code) {
    return code.split("").map((str, i) => i % q === r ? str : "").join("");
}