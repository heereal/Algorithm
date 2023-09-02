function solution(arr) {
    let i = 0;
    let stk = [];
    while (i < arr.length) {
        if (stk.length === 0) {
            stk.push(arr[i]);
        } else if (stk[stk.length - 1] === arr[i]) {
            stk.pop();
        } else if (stk[stk.length - 1] !== arr[i]) {
            stk.push(arr[i]);
        }
        i++;
    }
    return stk.length !== 0 ? stk : [-1];
}