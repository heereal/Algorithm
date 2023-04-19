function solution(n, m) {
    let max = Math.max(n,m);
    let min = Math.min(n,m);
    let first = 0;
    
    // 최대공약수
    for (let i = min; i >= 1; i--) {
        if (max % i === 0 && min % i === 0 ) {
            first = i;
            break;
        };
    };
    
    // 최대공배수
    let second = max;
    while (second % min !== 0) {
        second += max;
    };
    
    return [first, second];
}