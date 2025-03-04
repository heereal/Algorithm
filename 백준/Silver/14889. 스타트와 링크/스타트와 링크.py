import sys
input = sys.stdin.readline

N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]

A = []
min = 1000

def calculate_score(A, B):
    score_a = 0
    score_b = 0

    for i in range(0, N//2):
        for j in range(i+1, N//2):
            score_a += S[A[i]-1][A[j]-1] + S[A[j]-1][A[i]-1]
            score_b += S[B[i]-1][B[j]-1] + S[B[j]-1][B[i]-1]

    return [score_a, score_b]

def backtracking(start):
    if len(A) == N//2:
        B = [i for i in range(1, N+1) if i not in A]
        score_a, score_b = calculate_score(A, B)

        global min
        if abs(score_a-score_b) < min:
            min = abs(score_a-score_b)
            
        return
    
    for i in range(start, N+1):
        if i not in A:
            A.append(i)
            backtracking(i+1)
            A.pop()

backtracking(1)
print(min)