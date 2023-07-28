function solution(arr, queries) {
    let answer = arr;
    for (const query of queries) {
        let [i, j] = query;
        let tempArray = [...answer];
        tempArray[i] = answer[j];
        tempArray[j] = answer[i];
        answer = tempArray;
    }
    return answer;
}