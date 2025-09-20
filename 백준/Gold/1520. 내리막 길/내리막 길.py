import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

m, n = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(m)]

dp = [[-1] * n for _ in range(m)]
moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def dfs(x, y):
    # 도착점인 경우
    if x == (m - 1) and y == (n - 1):
        return 1
    
    # 이미 방문한 적이 있을 경우
    if dp[x][y] != -1:
        return dp[x][y]
    
    dp[x][y] = 0   # 방문 표시 + 초기화

    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < m and 0 <= ny < n:
            if map[x][y] > map[nx][ny]:
                dp[x][y] += dfs(nx, ny)
    
    return dp[x][y]

print(dfs(0, 0))