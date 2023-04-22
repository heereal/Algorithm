function solution(d, budget) {
    let sum = 0;
    d.sort((a,b) => a - b);
    // if (d.length === 1) return 1;
    for (const index in d) {
        sum += d[index];
        if (sum === budget) return parseInt(index) + 1;
        if (sum > budget) return parseInt(index);
        if (parseInt(index) === d.length - 1) return parseInt(index) + 1;
    }
}