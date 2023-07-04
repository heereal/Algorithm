function solution(arr) {
    let answer = [];
    for (const num of arr) {
        answer = [...answer, ...Array(num).fill(num)]
    }
    return answer;
}