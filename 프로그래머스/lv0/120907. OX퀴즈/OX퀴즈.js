function solution(quiz) {
    let answer = [];
    for (const x of quiz) { 
        let array = x.split(" ");
        if (array[1] === "+") {
            parseFloat(array[0]) + parseFloat(array[2]) === parseFloat(array[4]) 
            ? answer.push("O") 
            : answer.push("X")
        } 
        if (array[1] === "-") {
            parseFloat(array[0]) - parseFloat(array[2]) === parseFloat(array[4]) 
            ? answer.push("O") 
            : answer.push("X")
        }
    }
    return answer
}