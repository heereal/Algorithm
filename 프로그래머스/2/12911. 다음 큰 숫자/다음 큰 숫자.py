def solution(n):
    now = bin(n).count("1")
    
    while True:
        n += 1
        next = bin(n).count("1")
        
        if now == next:
            break
        
    return n