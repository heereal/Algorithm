function solution(my_str, n) {
    let count = 0;
    let answer = [];
    while ( count < Math.ceil(my_str.length/n)) {
        answer.push(my_str.slice(count*n,(count*n)+n));
        count++;
    }
    return answer;
}