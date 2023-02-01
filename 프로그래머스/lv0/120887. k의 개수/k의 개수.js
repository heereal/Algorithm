function solution(i, j, k) {
    let array = [];
    for (i = i; i <= j; i++) {
        array.push(...i.toString().split(""))
    }
    return array.filter((num) => num === k.toString()).length
}