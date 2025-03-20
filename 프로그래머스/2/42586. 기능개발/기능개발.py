from collections import deque

def solution(P, S):
    P = deque(P)
    S = deque(S)
    
    days = 1
    cnt = 0
    result = []
    
    while P:
        if P[0] + (S[0] * days) >= 100:
            P.popleft()
            S.popleft()
            cnt += 1
        else:
            if cnt != 0: 
                result.append(cnt)
                cnt = 0
            days += 1
    
    result.append(cnt)
    
    return result
