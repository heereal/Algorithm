function solution(numbers, num1, num2) {
    let array = [];
    for (i=num1; i <= num2; i++) {
        array.push(numbers[i])
    }
    return array
}