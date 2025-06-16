import sys
input = sys.stdin.readline

def DFS(node, cnt):
    visited[node] = True
    for n in graph[node]:
        if not visited[n]:
            cnt = DFS(n, cnt + 1)
    return cnt

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    graph = [[] for _ in range(N + 1)]

    for _ in range(M):
        A, B = map(int, input().split())
        graph[A].append(B)
        graph[B].append(A)

    visited = [False] * (N + 1)
    print(DFS(1, 0))