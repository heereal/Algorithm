function solution(binomial) {
    const [a, op, b] = binomial.split(" ");
    switch (op) {
        case "+":
            return parseInt(a) + parseInt(b);
        case "-":
            return parseInt(a) - parseInt(b);
        case "*":
            return parseInt(a) * parseInt(b);
    }
}