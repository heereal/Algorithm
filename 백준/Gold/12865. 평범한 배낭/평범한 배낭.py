N, K = map(int, input().split())
items = [[0, 0]]
dp = [[0] * (K+1) for _ in range(N+1)]

for _ in range(N):
    item = list(map(int, input().split()))
    items.append(item)

for i in range(1, N+1):
    for j in range(1, K+1):
        w, v = items[i]
        
        if j < w:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w]+v)

print(dp[N][K])