N = int(input())
cnt = min(99, N)

for num in range(100, N+1):
    a = num // 100
    b = (num // 10) % 10
    c = num % 10
    
    if a - b == b - c:
        cnt += 1

print(cnt)