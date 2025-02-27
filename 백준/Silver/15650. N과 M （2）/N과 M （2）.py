N, M = map(int, input().split())
S = []

def backtraking():
    if len(S) == M:
        print(*S)
        return
    
    for i in range(1, N+1):
        if i not in S:
            if S and S[-1] > i:
                continue
            S.append(i)
            backtraking()
            S.pop()

backtraking()