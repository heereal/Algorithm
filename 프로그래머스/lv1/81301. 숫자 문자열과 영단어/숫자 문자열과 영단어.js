function solution(s) {
    let num = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"];
    let answer = s;
    for ( let i = 0; i < 10; i++ ) {
        let arr = answer.split(num[i]);
        answer = arr.join(i);
    }
    return parseInt(answer);
}