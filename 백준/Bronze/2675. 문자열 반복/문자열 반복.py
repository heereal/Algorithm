n = int(input())
for _ in range(n):
    r, s = input().split()
    print("".join([i * int(r) for i in s]))