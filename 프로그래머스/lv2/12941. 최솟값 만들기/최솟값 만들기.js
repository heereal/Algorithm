function solution(A,B){
    A.sort((a, b) => a - b);
    B.sort((a, b) => b - a);
    return A.reduce((sum, _, i) => sum + (A[i] * B[i]), 0);
}