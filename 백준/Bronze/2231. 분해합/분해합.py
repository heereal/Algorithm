N = int(input())

for i in range(1, N+1):
    nums = map(int, str(i))
    if i + sum(nums) == N:
        print(i)
        break
    if i == N:
        print(0)
