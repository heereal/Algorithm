N = int(input())

visited = [-1] * N
cnt = 0

def check(now_row):
    for row in range(now_row):
        if visited[now_row] == visited[row] or now_row - row == abs(visited[now_row] - visited[row]):
            return False
    return True
    
def dfs(row):
    if row == N:
        global cnt
        cnt += 1
        return

    for col in range(N):
        visited[row] = col
        if check(row):
            dfs(row + 1)

dfs(0)
print(cnt)