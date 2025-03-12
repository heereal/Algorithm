import sys
input = sys.stdin.readline

N = int(input())
S = sorted(list(map(int, input().split())))
X = int(input())

left, right = 0, N-1
cnt = 0

while left < right:
    sum = S[left] + S[right]

    if sum == X:
        cnt += 1
        left += 1
        right -= 1
    elif sum > X:
        right -= 1
    elif sum < X:
        left += 1

print(cnt)