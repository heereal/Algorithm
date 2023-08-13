function solution(arr, flag) {
    let array = [];
    for (const i in arr) {
        if (flag[i]) array.push(...Array(arr[i] * 2).fill(arr[i]));
        if (!flag[i]) array.splice(-arr[i]);
    }
    return array;
}