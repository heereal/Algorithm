N, K = map(int, input().split())
circle = [i for i in range(1, N+1)]
idx = 0

print("<", end="")

for i in range(N):
    idx += K-1
    idx = idx % len(circle)

    if i == N-1:
        print(circle[idx], end="")
    else:
        print(circle[idx], end=", ")
        
    circle.pop(idx)

print(">")