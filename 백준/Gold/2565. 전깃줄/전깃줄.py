N = int(input())
wires = []
dp = [1] * N

for _ in range(N):
    wire = list(map(int, input().split()))
    wires.append(wire)

wires.sort()

for i in range(1, N):
    for j in range(i):
        if wires[i][1] > wires[j][1]:
            dp[i] = max(dp[i], dp[j] + 1)

print(N - max(dp))