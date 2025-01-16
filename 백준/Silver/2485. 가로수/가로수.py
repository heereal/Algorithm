import sys
input = sys.stdin.readline

def f_gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

N = int(input())
trees = [int(input()) for _ in range(N)]

gaps = [trees[i+1] - trees[i] for i in range(N-1)]

gcd = gaps[0]
for i in range(1, len(gaps)):
    gcd = f_gcd(gcd, gaps[i])

cnt = 0
for gap in gaps:
    cnt += gap // gcd - 1

print(cnt)