function solution(left, right) {
    let array = [];
    for (let i = left; i <= right; i++) {
        let count = 0;
        for (let z = 0; z <= i; z++) {
            if (i % z === 0) count += 1;
        }
        array.push(count);
    }
    return array.reduce((acc, cur, index) => acc + (cur % 2 === 0 ? index + left : -(index + left)), 0);
}