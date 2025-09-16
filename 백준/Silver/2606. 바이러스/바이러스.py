n = int(input())
k = int(input())
graph = [[] for _ in range(n + 1)]

for _ in range(k):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0] * (n + 1)
visited[1] = 1
stack = [1]

while stack:
    v = stack.pop()
    for i in graph[v]:
        if not visited[i]:
            stack.append(i)
            visited[i] = 1

print(sum(visited) - 1)