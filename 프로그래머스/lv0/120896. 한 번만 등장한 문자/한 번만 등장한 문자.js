function solution(s) {
    let answer = [];
    for (const str of s) if ( s.indexOf(str) === s.lastIndexOf(str)) answer.push(str);
    return answer.sort().join("");
}