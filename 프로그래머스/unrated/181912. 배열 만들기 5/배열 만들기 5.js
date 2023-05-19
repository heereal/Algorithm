function solution(intStrs, k, s, l) {
    let array = [];
    for (const int of intStrs) {
        let slice = parseInt(int.slice(s, s + l))
        if (slice > k ) array.push(slice)
        
    }
    return array;
}