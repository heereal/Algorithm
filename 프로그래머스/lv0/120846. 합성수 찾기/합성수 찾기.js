function solution(n) {
    let count = 0;
    for (let i = 4; i <= n; i++) {
        let divisorsCount = 0;
        for (let z = 1; z <= i; z++) {
            if (i % z === 0) {
                divisorsCount++
            }
            if (divisorsCount >= 3) {
                count++;
                break;
            }
        }
    }  
    return count;
}