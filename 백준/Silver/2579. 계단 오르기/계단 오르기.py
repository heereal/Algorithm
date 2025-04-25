N = int(input())
stairs = [0] * (N+1)

for i in range(1, N+1):
    stairs[i] = (int(input()))

dp = [0] * (N+1)

if N <= 2:
    print(sum(stairs))
else:
    dp[1] = stairs[1]
    dp[2] = stairs[1] + stairs[2]

    for i in range(3, N+1):
        one_step = dp[i-3] + stairs[i-1] + stairs[i]
        two_step = dp[i-2] + stairs[i]
        dp[i] = max(one_step, two_step)

    print(dp[N])