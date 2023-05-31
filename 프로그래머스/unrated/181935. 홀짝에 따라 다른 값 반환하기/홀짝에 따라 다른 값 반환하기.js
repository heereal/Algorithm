function solution(n) {
    let array = Array(n).fill(0).map((v, i) => i + 1);
    let answer = array.reduce((acc, cur, index) => {
        if ( n % 2 === 0 && (index + 1) % 2 === 0) acc += cur ** 2
        if ( n % 2 !== 0 && (index + 1) % 2 !== 0) acc += cur
        return acc;
    }, 0)
    return answer;
}