function solution(n) {
    return [...n.toString()].reduce((acc, cur)=> acc + parseInt(cur), 0)
}