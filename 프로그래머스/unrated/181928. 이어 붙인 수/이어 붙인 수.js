function solution(num_list) {
    let answer = num_list.reduce((acc, cur) => {
        if (cur % 2 === 0) acc[0] += cur
        if (cur % 2 !== 0) acc[1] += cur
        return acc
    }, ["", ""])
    return parseInt(answer[0]) + parseInt(answer[1]);
}