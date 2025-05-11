T = int(input())

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

for _ in range(T):
    N, M = map(int, input().split())
    print(factorial(M) // (factorial(M-N) * factorial(N)))