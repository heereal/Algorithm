function solution(numbers) {
    let answer = 0;
    for (const i in numbers) {
        for (const i2 in numbers) {
            if ( i !== i2 && numbers[i] * numbers[i2] >= answer) {
                answer = numbers[i] * numbers[i2]
            }
        }
    }
    return answer
}