function solution(numbers) {
    let answer = Number.MIN_SAFE_INTEGER;
    for ( i = 0; i < numbers.length; i++ ) {
        for ( j = 0; j < numbers.length; j++ ) {
            if ( i !== j && numbers[i] * numbers[j] >= answer ) {
                answer = numbers[i] * numbers[j]
            }
        }
    }
    return answer;
}