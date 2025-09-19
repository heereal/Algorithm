import sys
input = sys.stdin.readline

n = int(input())
time = []

for _ in range(n):
    m, o = map(int, input().split())
    if o == 0:
        time.append(m)

if time:
    print(min(time))
else:
    print(-1)