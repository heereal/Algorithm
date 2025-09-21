from collections import deque

n, m = map(int, input().split())
graph = [[int(i) for i in input()] for _ in range(n)]

moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
queue = deque([(0, 0)])

def bfs():
    while queue:
        x, y = queue.popleft()

        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1:
                    graph[nx][ny] = graph[x][y] + 1
                    queue.append((nx, ny))
    
    print(graph[n-1][m-1])

bfs()