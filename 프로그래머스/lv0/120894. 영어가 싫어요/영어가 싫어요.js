function solution(numbers) {
    
//     let array = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    
//     for (const i in array) {
//         numbers = numbers.replaceAll(array[i], i)
//         console.log(numbers)
//     }
    
//     return parseInt(numbers)
    
    // let answer = ''
    // let answer2 = ''
    
    numbers = numbers.replaceAll('one', '1')
    numbers = numbers.replaceAll('two', '2')
    numbers = numbers.replaceAll('three', '3')
    numbers = numbers.replaceAll('four', '4')
    numbers = numbers.replaceAll('five', '5')
    numbers = numbers.replaceAll('six', '6')
    numbers = numbers.replaceAll('seven', '7')
    numbers = numbers.replaceAll('eight', '8')
    numbers = numbers.replaceAll('nine', '9')
    numbers = numbers.replaceAll('zero', '0')
    
    return parseInt(numbers)
}