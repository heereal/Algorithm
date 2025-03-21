from collections import deque
  
def solution(maps):
    n = len(maps)
    m = len(maps[0])
    
    queue = deque([(0, 0)])
    next = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    
    while queue:
        x, y = queue.popleft()
        
        for dx, dy in next:
            nx = x + dx
            ny = y + dy
            
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1:
                queue.append((nx, ny))
                maps[nx][ny] = maps[x][y] + 1
    
    if maps[n-1][m-1] == 1:
        return -1
    else:
        return maps[n-1][m-1]