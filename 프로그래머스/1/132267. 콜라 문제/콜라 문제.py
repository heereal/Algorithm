def solution(a, b, n):
    answer = 0
    
    while n >= a:
        pair = n // a
        n = n - (pair * a) + (pair * b)
        answer += (pair * b)
        
    return answer