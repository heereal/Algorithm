function solution(numbers, k) {
    let answer = (2*k-1) % numbers.length;
    return answer === 0 ? numbers.length : answer;
}