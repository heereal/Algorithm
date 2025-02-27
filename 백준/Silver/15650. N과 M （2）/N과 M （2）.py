N, M = map(int, input().split())
S = []

def backtraking(start):
    if len(S) == M:
        print(*S)
        return
    
    for i in range(start, N+1):
        if i not in S:
            S.append(i)
            backtraking(i+1)
            S.pop()

backtraking(1)