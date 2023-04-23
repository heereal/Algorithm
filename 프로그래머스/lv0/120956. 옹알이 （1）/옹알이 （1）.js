function solution(babbling) {
    let array = ["aya", "ye", "woo", "ma"];
    let answer = 0;
    for (const babble of babbling) {
        let word = babble;
        for (const say of array) {
            word = word.replaceAll(say, 1)
        }
        if (/^1*$/.test(word)) answer++;
    }
    return answer;
}