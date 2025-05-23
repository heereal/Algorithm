import sys
input = sys.stdin.readline

k, n = map(int, input().split())
lines = [int(input()) for _ in range(k)]

left, right = 1, max(lines)

while left <= right:
    mid = (left + right) // 2
    cnt = 0

    for line in lines:
        cnt += line // mid
    
    if cnt >= n:
        left = mid + 1
    else:
        right = mid - 1

print(right)