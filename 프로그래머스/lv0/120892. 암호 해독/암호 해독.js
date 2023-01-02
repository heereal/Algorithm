function solution(cipher, code) {
    let array = [...cipher];
    let answer = ''
    for (i=code-1; i<array.length; i+=code) {
        answer += array[i]
    }
    return answer  
}