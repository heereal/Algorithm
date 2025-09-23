from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
tree = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    p,c, d = map(int, input().split())
    tree[p].append((c, d))
    tree[c].append((p, d))

def bfs(start):
    visited = [-1] * (n + 1)
    visited[start] = 0
    queue = deque([start])

    while queue:
        cur = queue.popleft()
        for next, dist in tree[cur]:
            if visited[next] == -1:
                queue.append(next)
                visited[next] = visited[cur] + dist
    
    max_dist = max(visited)
    max_node = visited.index(max_dist)

    return [max_node, max_dist]

start_node, start_dist = bfs(1)
end_node, max_dist = bfs(start_node)
print(max_dist)