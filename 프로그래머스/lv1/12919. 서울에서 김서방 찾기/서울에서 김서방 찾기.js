function solution(seoul) {
    const array = [];
    seoul.map((string, index) => string === 'Kim' && array.push(index))
    return `김서방은 ${array[0]}에 있다`;
}