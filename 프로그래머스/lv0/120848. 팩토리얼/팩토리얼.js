function solution(n) {
    let answer = 1;
    for ( i = 2; i <= Number.MAX_SAFE_INTEGER; i++ ) {
        answer *= i
        if ( n === answer ) {
            return i
        } else if ( answer > n ) {
            return i - 1
        }
        
    }
}