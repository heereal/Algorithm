function solution(my_string) {
    let array = [];
    for (const i in my_string) {
        array.push(my_string.slice(-i))
    };
    return array.sort();
}