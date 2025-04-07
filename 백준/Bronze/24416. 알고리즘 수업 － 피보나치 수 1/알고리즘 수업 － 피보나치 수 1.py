N = int(input())

def dp(N):
    memo = [0] * (N + 1)
    memo[1] = 1

    for i in range(2, N + 1):
        memo[i] = memo[i-1] + memo[i-2]
    
    return memo[N]

print(dp(N), end=" ")
print(N-2)