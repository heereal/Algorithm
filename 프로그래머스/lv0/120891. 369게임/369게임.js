function solution(order) {
    let answer = 0
    order.toString().split("").map((num) =>  "369".includes(num) ? answer += 1 : null)
    return answer
}