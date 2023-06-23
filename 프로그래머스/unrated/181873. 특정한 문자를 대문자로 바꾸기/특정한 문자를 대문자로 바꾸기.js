function solution(my_string, alp) {
    return [...my_string].map((str) => str === alp ? str.toUpperCase() : str).join("");
}