def solution(n):
    answer = set()
    x = 2
    
    while n != 1:
        if n % x == 0:
            answer.add(x)
            n //= x
        else:
            x += 1
            
    return sorted(list(answer))