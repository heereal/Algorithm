function solution(n) {
    for ( i = 1; i > 0; i++) {
        if (i*6 % n === 0) return i
    }
}