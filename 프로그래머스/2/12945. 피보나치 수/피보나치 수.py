def solution(n):
    memo = [0, 1] + [0] * (n-1)
    
    for i in range(2, n+1):
        memo[i] = memo[i-1] + memo[i-2]
        
    return memo[n] % 1234567