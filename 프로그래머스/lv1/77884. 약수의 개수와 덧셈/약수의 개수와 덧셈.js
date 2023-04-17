function solution(left, right) {
    let answer = 0;
    for (let i = left; i <= right; i++) {
        let count = 0;
        for (let z = 0; z <= i; z++) {
            if (i % z === 0) count += 1;
        }
        if (count % 2 === 0) answer += i;
        if (count % 2 !== 0) answer -= i;
    }
    return answer;
}