function solution(arr) {
    for (const i in arr) {
        for (const j in arr[i]) {
            if (arr[i][j] !== arr[j][i]) return 0;
        }
        return 1;
    }
}