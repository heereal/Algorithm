function solution(cipher, code) {
    let answer = ''
    for (i=code-1; i<cipher.length; i+=code) {
        answer += cipher[i]
    }
    return answer  
}