import sys
input = sys.stdin.readline

N, M, R = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)

for _ in range(M):
    U, V = map(int, input().split())
    graph[U].append(V)
    graph[V].append(U)

def DFS():
    cnt = 0
    stack = [R]
    
    while stack:
        node = stack.pop()

        if not visited[node]:
            cnt += 1
            visited[node] = cnt

            for next_node in sorted(graph[node]):
                if not visited[next_node]:
                    stack.append(next_node)
    
DFS()

for v in visited[1:]:
    print(v)
