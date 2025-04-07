N = int(input())

def dp(N):
    a, b = 1, 1 # F(1), F(2)

    for i in range(3, N + 1):
        a, b = b, a + b # F(b) = F(i)
    
    return b

print(dp(N), N-2)