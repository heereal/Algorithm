def solution(sizes):
    long = 0
    short = 0
    
    for a, b in sizes:
        if a < b:
            a, b = b, a
        
        long = max(long, a)
        short = max(short, b)
        
    return long * short