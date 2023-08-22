function solution(num_list) {
    let count = 0;
    for (const num of num_list) {
        let currentNum = num
        while (currentNum !== 1) {
            if (currentNum % 2 === 0) {
                currentNum /= 2;
                count++
            } else {
                currentNum = (currentNum - 1) / 2;
                count++;
            }
        }
    }
    return count;
}