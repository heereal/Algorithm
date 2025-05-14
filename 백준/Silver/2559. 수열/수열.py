n, k = map(int, input().split())
nums = list(map(int, input().split()))

answer = [sum(nums[:k])]

for i in range(1, n-k+1):
    new = answer[-1] - nums[i-1] + nums[i+k-1]
    answer.append(new)

print(max(answer))