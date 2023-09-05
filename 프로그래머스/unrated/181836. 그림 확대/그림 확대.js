function solution(picture, k) {
    let answer = [];
    for (const line of picture) {
        const expanded = line.split('').map((pixel) => pixel.repeat(k)).join('');
        answer.push(...Array(k).fill(expanded));   
    }
    return answer;
}