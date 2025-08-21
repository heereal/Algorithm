x = int(input())
n = int(input())
total = x * (n + 1)

for _ in range(n):
    total -= int(input())

print(total)