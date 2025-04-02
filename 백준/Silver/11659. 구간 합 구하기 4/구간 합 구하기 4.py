import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))

li = [0]

for i in range(N):
    li.append(li[i] + nums[i])

for _ in range(M):
    i, j = map(int, input().split())
    print(li[j] - li[i-1])