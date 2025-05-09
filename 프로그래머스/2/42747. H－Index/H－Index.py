def solution(c):
    c.sort(reverse=True)
    answer = 0
    
    for v in range(1, len(c) + 1):
        if c[v-1] >= v:
            answer = v
        else:
            break

    return answer