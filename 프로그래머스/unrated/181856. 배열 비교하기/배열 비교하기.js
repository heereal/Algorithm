function solution(arr1, arr2) {
    if (arr1.length === arr2.length) {
        const sum1 = arr1.reduce((acc, cur) => acc + cur, 0);
        const sum2 = arr2.reduce((acc, cur) => acc + cur, 0);
        return sum1 === sum2 ? 0 : sum1 > sum2 ? 1 : -1;
    }
    else return arr1.length > arr2.length ? 1 : -1;
}