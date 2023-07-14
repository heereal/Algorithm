function solution(myString) {
    let array = [..."abcdefghijk"];
    return [...myString].map((str) => array.includes(str) ? "l" : str).join("");
}