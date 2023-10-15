function solution(n, words) {
    for (let i = 0; i < words.length; i++) {
        if (i === 0) continue; // 첫 번째 단어인 경우 바로 다음 인덱스 순회
        
        const prevWord = words[i - 1]; // 이전 단어
        const nextWord = words[i]; // 현재 단어
        
        const wrongWord = prevWord[prevWord.length - 1] !== nextWord[0]; // 끝말잇기에 실패했을 경우
        const sameWord = words.indexOf(nextWord) !== i; // 동일한 단어를 말했을 경우
        
        if (wrongWord || sameWord) {
            return [i % n + 1, Math.floor(i / n) + 1];
        }
    }
    
    return [0,0] // 끝말잇기에 성공했을 경우
}