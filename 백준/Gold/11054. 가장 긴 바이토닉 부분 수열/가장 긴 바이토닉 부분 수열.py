N = int(input())
nums = list(map(int, input().split()))

up = [1] * N
down = [1] * N

for i in range(1, N):
    for j in range(i):
        if nums[i] > nums[j]:
            up[i] = max(up[i], up[j]+1)

nums.reverse()

for i in range(1, N):
    for j in range(i):
        if nums[i] > nums[j]:
            down[i] = max(down[i], down[j]+1)

result = [0] * N

for i in range(N):
    result[i] = up[i] + down[N-i-1] - 1

print(max(result))
