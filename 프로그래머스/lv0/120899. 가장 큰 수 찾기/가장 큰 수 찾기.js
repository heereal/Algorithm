function solution(array) {
    let max_num = Math.max(...array);
    return [max_num, array.indexOf(max_num)]
}