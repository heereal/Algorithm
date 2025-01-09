import sys
input = sys.stdin.readline

N, M = map(int, input().split())
a = set(input().strip() for _ in range(N))
b = set(input().strip() for _ in range(M))

result = sorted(a & b)

print(len(result))

for name in result:
    print(name)