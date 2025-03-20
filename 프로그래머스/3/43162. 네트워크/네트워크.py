from collections import deque

def solution(n, computers):
    def bfs(i):
        queue = deque([i])
        
        while queue:
            node = queue.popleft()
            visited[node] = True
            
            for j in range(n):
                if not visited[j] and computers[j][node]:
                    queue.append(j)
            
    visited = [False] * n
    cnt = 0
            
    for i in range(n):
        if not visited[i]:
            bfs(i)
            cnt += 1
        
    return cnt