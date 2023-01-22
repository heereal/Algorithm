function solution(my_string) {
    return my_string.split("").filter((str) => !"aeiou".split("").includes(str)).join("")
}