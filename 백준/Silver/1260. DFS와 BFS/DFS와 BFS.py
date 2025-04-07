import sys
from collections import deque
input = sys.stdin.readline

N, M, V = map(int, input().split())
graph = [[0] * (N + 1) for _ in range(N+1)]

visited1 = [False] * (N + 1)
visited2 = [False] * (N + 1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1

def DFS(V):
    print(V, end=" ")
    visited1[V] = True
    
    for i in range(1, N+1):
        if not visited1[i] and graph[V][i]:
            visited1[i] = True
            DFS(i)

def BFS(V):
    visited2[V] = True
    queue = deque([V])

    while queue:
        V = queue.popleft()
        print(V, end=" ")

        for i in range(1, N+1):
            if not visited2[i] and graph[V][i]:
                queue.append(i)
                visited2[i] = 1

DFS(V)
print()
BFS(V)
