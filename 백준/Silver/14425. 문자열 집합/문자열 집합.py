import sys
input = sys.stdin.readline

N, M = map(int, input().split())
S = {input().strip() : 0 for i in range(N)}
cnt = 0

for i in range(M):
    if input().strip() in S:
        cnt += 1

print(cnt)
