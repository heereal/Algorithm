import sys
input = sys.stdin.readline

n = int(input())
b1, b2 = map(int, input().split())
answer = False

for _ in range(n):
    lx, ly, hx, hy = map(int, input().split())
    if lx <= b1 <= hx and ly <= b2 <= hy:
        answer = True
        print('Yes')
        break
else:
    print('No')

