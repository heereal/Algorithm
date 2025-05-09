def solution(c):
    c.sort()
    answer = 0
    i = 0
    
    for v in range(max(c)):
        if v > c[i]:
            i += 1
            
        if len(c[i:]) >= v and len(c[:i]) <= v:
            answer = v
        elif len(c[i:]) < v:
            break

    return answer