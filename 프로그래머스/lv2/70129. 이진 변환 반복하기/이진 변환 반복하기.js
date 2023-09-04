function solution(s) {
    let answer = [0, 0];
    while (s !== '1') {
        const arr = [...s].filter((num) => num !== '0');
        answer[0] += 1;
        answer[1] += s.length - arr.length;
        s = arr.length.toString(2);
    }
    return answer;
}