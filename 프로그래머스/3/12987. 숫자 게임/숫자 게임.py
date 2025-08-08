from collections import deque

def solution(A, B):
    A.sort()
    B.sort()
    B = deque(B)
    answer = 0
    
    for a in A:
        while B:
            if B[0] > a:
                answer += 1
                B.popleft()
                break
            else:
                B.popleft()
    
    return answer