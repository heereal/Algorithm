n = int(input())
days = [0] * 5

for _ in range(n):
    d = int(input())
    days[d - 1] += 1

if 0 in days:
    print('YES')
else:
    print('NO')