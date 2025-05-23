N = int(input())
nums = list(map(int, input().split()))

dp = [0] * N
dp[0] = nums[0]

for i in range(1, N):
    dp[i] = max(nums[i], dp[i-1] + nums[i])

print(max(dp))