function solution(myStr) {
    let arr = ["a", "b", "c"];
    for (const alpha of arr) {
        myStr = myStr.replaceAll(alpha, " ")
    }
    let answer = myStr.split(" ").filter((str) => str)
    return answer.length === 0 ? ["EMPTY"] : answer;
}