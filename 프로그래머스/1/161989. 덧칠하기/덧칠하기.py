from collections import deque

def solution(n, m, section):
    answer = 1
    prev = section[0]
    
    for sec in section:
        if prev + m <= sec:
            answer += 1
            prev = sec
            
    return answer