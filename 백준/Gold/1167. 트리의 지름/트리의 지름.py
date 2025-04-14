import sys
from collections import deque
input = sys.stdin.readline

V = int(input())
tree = [[] for _ in range(V+1)]

for _ in range(V):
    info = list(map(int, input().split()))
    node = info[0]

    for i in range(1, len(info)-1, 2):
        tree[node].append([info[i], info[i+1]])

def BFS(start):
    visited = [-1] * (V+1)
    visited[start] = 0
    queue = deque([start])

    while queue:
        now = queue.popleft()

        for next_node, next_distance in tree[now]:
            if visited[next_node] == -1:
                queue.append(next_node)
                visited[next_node] = visited[now] + next_distance

    farthest_distance = max(visited)
    farthest_node = visited.index(farthest_distance)
    return farthest_node, visited

farthest_node, _ = BFS(1)
_, visited = BFS(farthest_node)

print(max(visited))