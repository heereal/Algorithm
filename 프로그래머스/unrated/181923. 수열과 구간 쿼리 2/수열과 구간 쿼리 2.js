function solution(arr, queries) {
    let array = [];
    for (const [s, e, k] of queries) {
        let filteredArray = arr.filter((num, i) => i >= s && i <= e && num > k);
        array.push(filteredArray.length ? Math.min(...filteredArray) : -1)
    }
    return array;
}