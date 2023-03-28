function solution(numbers, direction) {
    if ( direction === "right" ) {
        let right = numbers[numbers.length - 1]
        numbers.splice(numbers.length - 1, 1);
        numbers.unshift(right)
    } else {
        let left = numbers[0]
        numbers.splice(0, 1);
        numbers.push(left)
    }
    return numbers;
}