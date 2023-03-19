function solution(arr) {
    let copy = [...arr];
    let sort_array = copy.sort((a,b) => a - b)
    return arr.length === 1 ? [-1] : arr.filter((num) => num !== sort_array[0]);
}