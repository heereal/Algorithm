n = int(input())

for _ in range(n):
    s = input().split()
    new = s[2:] + s[:2]
    print(*new)