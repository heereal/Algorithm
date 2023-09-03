function solution(A,B){
    const sortedA = A.sort((a, b) => a - b);
    const sortedB = B.sort((a, b) => b - a);
    return A.reduce((sum, _, i) => sum + (sortedA[i] * sortedB[i]), 0);
}