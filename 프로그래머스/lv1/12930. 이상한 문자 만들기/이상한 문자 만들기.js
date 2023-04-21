function solution(s) {
    let array = s.split(" ");
    console.log(array)
    let answer = [];
    for (const word of array) {
        let temp = "";
        if (word === "") answer.push("");
        for (const i in word) {
            temp += i % 2 !== 0 ? word[i].toLowerCase() : word[i].toUpperCase();
            if (parseInt(i) === word.length-1) answer.push(temp);
        }
    }
    return answer.join(" ");
}