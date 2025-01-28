N, K = map(int, input().split())

circle = [i for i in range(1, N+1)]
result = []

idx = 0

for i in range(N):
    idx += K-1
    idx = idx % len(circle)
    
    x = circle.pop(idx)
    result.append(str(x))

print("<" + ", ".join(result) + ">")