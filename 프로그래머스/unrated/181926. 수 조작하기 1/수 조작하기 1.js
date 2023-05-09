function solution(n, control) {
    let answer = n;
    control.split("").forEach((str) => {
        if (str === "w") answer += 1;
        if (str === "s") answer -= 1;
        if (str === "d") answer += 10;
        if (str === "a") answer -= 10;
    })
    return answer;
}