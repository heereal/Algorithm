n = int(input())
res = [1, 1] + [0] * 44

for i in range(2, 46):
    res[i] = res[i - 1] + res[i - 2]

for _ in range(n):
    x = int(input())
    print(res[x])