function solution(my_string) {
    let array = [...my_string].filter((str) => "123456789".split("").includes(str))
    return array.reduce((acc,cur) => acc + parseInt(cur), 0)
}