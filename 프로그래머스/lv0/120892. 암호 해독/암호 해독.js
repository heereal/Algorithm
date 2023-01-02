function solution(cipher, code) {
    let array = [...cipher];
    let array2 = [];
    let answer = ''
    for (i=code-1; i<array.length; i+=code) {
        array2.push(array[i])
    }
    for (let char of array2) {
        answer += char
    }
    return answer  
}