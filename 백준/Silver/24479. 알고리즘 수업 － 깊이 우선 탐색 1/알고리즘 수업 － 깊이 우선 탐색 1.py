import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

N, M, R = list(map(int, input().split()))
graph = [[] for _ in range(N+1)]

for _ in range(M):
    U, V = list(map(int, input().split()))
    graph[U].append(V)
    graph[V].append(U)

def DFS(node):
    global cnt
    cnt += 1

    visited[node] = True
    order[node] = cnt

    for i in sorted(graph[node]):
        if not visited[i]:
            DFS(i)

visited = [False] * (N+1)
order = [0] * (N+1)
cnt = 0

DFS(R)
print(*order[1:], sep="\n")