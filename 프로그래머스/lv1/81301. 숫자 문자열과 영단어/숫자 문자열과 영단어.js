function solution(s) {
    let num = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"];
    let answer = s;
    for ( let i = 0; i < 10; i++ ) {
        let answer2 = answer.replaceAll(num[i], i);
        answer = answer2
    }
    return parseInt(answer);
}