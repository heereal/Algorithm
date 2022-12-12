function solution(numbers) {
    
    let array = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    
    for (const i in array) {
        numbers = numbers.replaceAll(array[i], i)
    }
    
    return parseInt(numbers)
}
