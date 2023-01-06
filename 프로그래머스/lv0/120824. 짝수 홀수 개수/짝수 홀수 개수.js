function solution(num_list) {
    let a = num_list.filter(num => num % 2 === 0).length
    return [a, num_list.length-a];
}