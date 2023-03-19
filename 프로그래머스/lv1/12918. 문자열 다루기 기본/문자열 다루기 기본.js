function solution(s) {
    return (s.length === 4 || s.length === 6) && !s.split("").map((v) => parseInt(v)).includes(NaN);
}