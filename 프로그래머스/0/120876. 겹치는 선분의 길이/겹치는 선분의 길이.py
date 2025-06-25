def solution(lines):
    base = [0] * 200
    
    for line in lines:
        start, end = line
        
        for i in range(start, end):
            if i <= 0:
                base[abs(i)] += 1
            else:
                base[100+i] += 1

    stacked = list(filter(lambda x: x >= 2, base))

    return len(stacked)