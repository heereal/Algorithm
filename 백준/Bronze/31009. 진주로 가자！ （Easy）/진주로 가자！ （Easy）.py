n = int(input())
j = 0
prices = []

for _ in range(n):
    d, c = input().split()
    if d == 'jinju':
        j = int(c)
    else:
        prices.append(int(c))

print(j)
print(len([p for p in prices if p > j]))