n = int(input())
money = {136: 1000, 142: 5000, 148: 10000, 154: 50000}
answer = 0

for _ in range(n):
    m, _ = map(int, input().split())
    answer += money[m]

print(answer)
        
