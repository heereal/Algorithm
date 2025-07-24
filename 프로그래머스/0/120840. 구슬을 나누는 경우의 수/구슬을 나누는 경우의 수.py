def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

def solution(balls, share):
    return factorial(balls) / (factorial(balls-share) * factorial(share))