function solution(my_string) {
    return my_string.split("").filter((str) => !isNaN(str)).sort((a,b) => a - b).map((num) => parseInt(num))
}