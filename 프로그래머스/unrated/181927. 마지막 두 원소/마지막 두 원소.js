function solution(num_list) {
    let prev = num_list[num_list.length - 2];
    let next = num_list[num_list.length - 1];
    next > prev ? num_list.push(next - prev) : num_list.push(next * 2)
    return num_list;
}