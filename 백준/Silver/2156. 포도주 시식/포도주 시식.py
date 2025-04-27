import sys
input = sys.stdin.readline

N = int(input())
w = [0]

for _ in range(N):
    w.append(int(input()))

dp = [0] * (N+1)

if N <= 2:
    print(sum(w))
else:
    dp[1] = w[1]
    dp[2] = w[1] + w[2]

    for i in range(3, N+1):
        dp[i] = max(dp[i-2] + w[i], dp[i-3] + w[i-1] + w[i], dp[i-1])
    
    print(dp[N])