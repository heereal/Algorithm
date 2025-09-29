from collections import deque
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    time = [-1] + list(map(int, input().split()))

    # 진입 차수 배열 (선행 조건 개수)
    in_dgree = [0] * (n + 1) 
    graph = [[] for _ in range(n + 1)]

    for _ in range(k):
        x, y = map(int, input().split())
        graph[x].append(y)
        in_dgree[y] += 1
    
    w = int(input())

    queue = deque([])
    dp = [-1] * (n + 1)

    # 진입 차수가 0인 건물(선행 조건 없는 건물)을 큐에 삽입
    for i in range(1, n + 1):
        if in_dgree[i] == 0:
            queue.append(i)
            dp[i] = time[i]

    while queue:
        cur = queue.popleft()

        for next in graph[cur]:
            dp[next] = max(dp[next], dp[cur] + time[next])
            in_dgree[next] -= 1

            # 모든 선행 조건 해결되면 큐에 추가 (건설 시작 가능)
            if in_dgree[next] == 0:
                queue.append(next)

    print(dp[w])