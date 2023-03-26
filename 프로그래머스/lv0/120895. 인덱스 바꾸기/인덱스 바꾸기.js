function solution(my_string, num1, num2) {
    return my_string.split("").map((str, i) => i === num1 ? str = my_string[num2] : i === num2 ? str = my_string[num1] : str).join("");
}