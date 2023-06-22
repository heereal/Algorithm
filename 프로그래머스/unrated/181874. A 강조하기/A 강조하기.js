function solution(myString) {
    return [...myString].map((str) => str.toLowerCase() === 'a' ? 'A' : str.toLowerCase()).join('');
}