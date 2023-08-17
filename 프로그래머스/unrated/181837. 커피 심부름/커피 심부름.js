function solution(order) {
    let price = 0;
    order.forEach((drink) => {
        if (drink.includes("americano") || drink === "anything") price += 4500;
        if (drink.includes("latte")) price += 5000;
    })
    return price;
}