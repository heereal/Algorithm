import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))

li = [0]
sum = 0

for num in nums:
    sum += num
    li.append(sum)

for _ in range(M):
    i, j = map(int, input().split())
    print(li[j] - li[i-1])