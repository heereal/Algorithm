N, M = map(int, input().split())
s = []

def backtracking(start):
    if len(s) == M:
        print(*s)
        return
    
    for i in range(start, N+1):
        s.append(i)
        backtracking(i)
        s.pop()

backtracking(1)