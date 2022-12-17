function solution(numbers) {
    let answer = 0;
    for (const num of numbers) {
        answer += num
    }
    return (answer / numbers.length)
}