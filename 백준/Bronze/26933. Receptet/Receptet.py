n = int(input())
answer = 0

for _ in range(n):
    h, b, k = map(int, input().split())
    if b - h > 0:
        answer += (b - h) * k   

print(answer)