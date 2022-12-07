function solution(num_list, n) {
    let result = [];
    for(i=0; i<num_list.length; i+=n) {
        result.push(num_list.slice(i, n+i))
    }
    return result;
}