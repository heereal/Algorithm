N = int(input())

nums = [0, 1]

for i in range(N-1):
    num = nums[-1] + nums[-2]
    nums.append(num)

print(nums[N])