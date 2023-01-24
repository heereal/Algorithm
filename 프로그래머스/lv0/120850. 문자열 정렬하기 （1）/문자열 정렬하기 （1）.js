function solution(my_string) {
    return my_string.split("").filter((str) => "0123456789".includes(str)).sort((a,b) => a - b).map((num) => parseInt(num))
}