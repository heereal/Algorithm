function solution(price, money, count) {
    let fee = Array(count).fill().reduce((acc, cur, i) => acc + price * ( i + 1 ), 0)
    return money > fee ? 0 : Math.abs(money - fee);
}