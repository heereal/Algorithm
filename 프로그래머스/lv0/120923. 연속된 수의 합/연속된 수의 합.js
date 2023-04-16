function solution(num, total) {
    let array = Array(total + num*2).fill(0).map((v, i) => i - num);
    console.log(array)
    for (let i = 0; i < array.length; i++) {
        if (array.slice(i, i + num).reduce((acc, cur) => acc + cur, 0) === total) return array.slice(i, i + num);
    }
}