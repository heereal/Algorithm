function solution(numer1, denom1, numer2, denom2) {
    let numer = (numer1 * denom2) + (numer2 * denom1);
    let denom = denom1 * denom2;
    let first = numer;
    let second = denom;
    for ( let i = Math.min(numer, denom); i >= 2; i--) {
        if (first % i === 0 && second % i === 0) {
            first = numer / i;
            second = denom / i;
        }
    }
    return [first, second];
}