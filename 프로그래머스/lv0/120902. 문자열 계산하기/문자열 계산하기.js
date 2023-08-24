function solution(my_string) {
    let arr = my_string.split(" ");
    let answer = Number(arr[0]);
    for (let i = 0; i <= my_string.length; i++) {
        if (i % 2 !== 0 && arr[i] === '+') answer += Number(arr[i + 1]);
        if (i % 2 !== 0 && arr[i] === '-') answer -= Number(arr[i + 1]);
    }
    return answer;
}