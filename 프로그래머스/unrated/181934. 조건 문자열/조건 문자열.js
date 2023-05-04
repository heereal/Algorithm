function solution(ineq, eq, n, m) {
    let result = true;
    if (ineq === "<" && eq === "=") result = n <= m;
    if (ineq === ">" && eq === "=") result = n >= m;
    if (ineq === "<" && eq === "!") result = n < m;
    if (ineq === ">" && eq === "!") result = n > m;
    return result ? 1 : 0;
}