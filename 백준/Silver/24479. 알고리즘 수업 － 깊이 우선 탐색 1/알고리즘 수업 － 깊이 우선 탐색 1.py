import sys
input = sys.stdin.readline

N, M, R = list(map(int, input().split()))
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    U, V = list(map(int, input().split()))
    graph[U].append(V)
    graph[V].append(U)

def DFS():
    order = [0] * (N+1)
    cnt = 0

    stack = [R]
    visited[R] = True

    while stack:
        node = stack.pop()
        visited[node] = True

        if not order[node]:
            cnt += 1
            order[node] = cnt

        for i in sorted(graph[node], reverse=True):
            if not visited[i]:
                stack.append(i)

    return order

visited = [False] * (N + 1)
order = DFS()

for i in range(1, N+1):
    print(order[i])