function solution(l, r) {
    let array = [];
    for (let i = l; i <= r; i++) {
        if (/^[05]+$/g.test(i.toString())) array.push(i)
    }
    return array.length === 0 ? [-1] : array;
}