def solution(n):
    before, now = 0, 1
    
    for i in range(2, n):
        before, now = now, before + now
        
    return (before + now) % 1234567