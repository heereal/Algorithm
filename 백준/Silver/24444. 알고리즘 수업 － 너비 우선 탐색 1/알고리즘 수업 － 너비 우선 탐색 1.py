from collections import deque
import sys
input = sys.stdin.readline

n, m, r = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def bfs(start):
    global cnt

    visited = [False] * (n + 1)
    visited[start] = True
    queue = deque([start])

    while queue:
        node = queue.popleft()
        cnt += 1
        answer[node] = cnt

        for next in sorted(graph[node]):
            if not visited[next]:
                queue.append(next)
                visited[next] = True

answer = [0] * (n + 1)
cnt = 0

bfs(r)

for i in answer[1:]:
    print(i)