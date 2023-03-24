function solution(s) {
    let upperCase = [];
    let lowerCase = [];
    s.split("").forEach((str) => str !== str.toUpperCase() ? lowerCase.push(str) : upperCase.push(str))
    return lowerCase.sort().reverse().join("") + upperCase.sort().reverse().join("");
}