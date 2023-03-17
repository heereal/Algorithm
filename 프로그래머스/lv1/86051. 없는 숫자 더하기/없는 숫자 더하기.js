function solution(numbers) {
    return "123456789".split("").reduce((acc, cur) => acc + (numbers.includes(+cur) ? 0 : +cur), 0)
}