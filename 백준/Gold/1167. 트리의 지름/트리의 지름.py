import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)

V = int(input())
tree = [[] for _ in range(V+1)]

for _ in range(V):
    info = list(map(int, input().split()))
    node = info[0]

    for i in range(1, len(info)-1, 2):
        tree[node].append((info[i], info[i+1]))

def DFS(node, distance):
    for next_node, next_distance in tree[node]:
        if visited[next_node] == -1:
            visited[next_node] = visited[node] + next_distance
            DFS(next_node, distance + next_distance)

visited = [-1] * (V+1)
visited[1] = 0
DFS(1, 0)

farthest_distance = max(visited)
farthest_node = visited.index(farthest_distance)

visited = [-1] * (V+1)
visited[farthest_node] = 0
DFS(farthest_node, 0)

print(max(visited))