function solution(my_string) {
    let arr = my_string.match(/\d+/g);
    return arr ? arr.reduce((acc, cur) => acc + Number(cur), 0) : 0;
}