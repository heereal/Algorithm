function solution(s) {
    let array = [];
    s.split(" ").forEach((item) => item === "Z" ? array.pop() : array.push(+item));
    return array.reduce((acc, cur) => acc + cur, 0)
}