import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N+1)]

for i in range(N-1):
    A, B = map(int, input().split())
    graph[A].append(B)
    graph[B].append(A)

visited = [0]*(N+1)

def dfs(s):
    for i in graph[s]:
        if visited[i] == 0:
            visited[i] = s
            dfs(i)

dfs(1)

for i in range(2, N+1):
    print(visited[i])