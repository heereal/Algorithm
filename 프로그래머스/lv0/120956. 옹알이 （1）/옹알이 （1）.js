function solution(babbling) {
    let array = ["aya", "ye", "woo", "ma"];
    let answer = 0;
    for (const babble of babbling) {
        let dd = babble;
        for (const say of array) {
            dd = dd.replaceAll(say, 1)
            console.log(typeof dd)
        }
        if (/^1*$/.test(dd)) answer++;
    }
    return answer;
}