function solution(my_string, overwrite_string, s) {
    let array = [];
    for (let i = 0; i <= my_string.length; i++) {
        if (i >= s && i <= (s + overwrite_string.length - 1)) array.push(overwrite_string[i - s]);
        else array.push(my_string[i]);
    }
    return array.join("");
}