function solution(code) {
    let mode = true;
    let answer = code.split("").reduce((acc, cur, idx) => {
        if (cur === "1") mode = !mode 
        else if (mode && idx % 2 === 0) acc += cur
        else if (!mode && idx % 2 !== 0) acc += cur
        return acc
    }, "");
    return answer ? answer : "EMPTY"
}