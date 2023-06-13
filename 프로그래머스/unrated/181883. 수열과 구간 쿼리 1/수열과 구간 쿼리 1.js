function solution(arr, queries) {
    let answer = arr;
    for (const query of queries) {
        const [s, e] = query;
        for (const i in arr) {
            if (s <= i && e >= i) {
                arr[i] += 1;
            };
        };
    };
    return answer;
}