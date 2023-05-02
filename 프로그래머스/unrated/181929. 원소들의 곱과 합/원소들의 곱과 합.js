function solution(num_list) {
    let sum = num_list.reduce((acc, cur) => acc + cur, 0);
    let multifly = num_list.reduce((acc, cur) => acc * cur, 1);
    return sum**2 > multifly ? 1 : 0;
}