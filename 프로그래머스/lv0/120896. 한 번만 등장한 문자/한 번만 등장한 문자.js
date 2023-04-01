function solution(s) {
    let array = [...new Set(s.split("").sort())];
    let answer = "";
    for ( i = 0; i <= array.length - 1; i++ ) {
        let array2 = s.split("").filter((v) => v === array[i]);
        if (array2.length === 1) answer += array[i];
    }
    return answer;
}