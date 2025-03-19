def solution(sizes):
    long = []
    short = []
    
    for x, y in sizes:
        if x > y:
            long.append(x)
            short.append(y)
        else:
            long.append(y)
            short.append(x)
        
    return max(long) * max(short)