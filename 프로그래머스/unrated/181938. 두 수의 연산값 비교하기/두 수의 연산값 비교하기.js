function solution(a, b) {
    let result = parseInt(a.toString() + b.toString());
    return result > 2*a*b ? result : 2*a*b;
}