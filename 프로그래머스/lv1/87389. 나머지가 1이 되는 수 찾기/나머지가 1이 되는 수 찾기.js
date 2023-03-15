function solution(n) {
    for ( i = 1; i < n; i++ ) {
        if ( n % i === 1 ) {
            return i;
        }
    }
}