import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

N, M, R = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)

for _ in range(M):
    U, V = map(int, input().split())
    graph[U].append(V)
    graph[V].append(U)

def DFS(node):
    global cnt
    visited[node] = cnt

    for next_node in sorted(graph[node], reverse=True):
        if not visited[next_node]:
            cnt += 1
            DFS(next_node)

cnt = 1
DFS(R)

for i in range(1, N+1):
    print(visited[i])