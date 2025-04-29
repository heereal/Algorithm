N = int(input())
nums = list(map(int, input().split()))

dp = [1] * N

for i in range(1, N):
    for j in range(i):
        if nums[i] > nums[j]:
            dp[i] = max(dp[j]+1, dp[i])

print(max(dp))
