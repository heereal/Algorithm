def solution(n, s):
    if s < n:
        return [-1]
    
    answer = []
    
    for i in range(n):
        cur = s // (n - i)
        s -= cur
        answer.append(cur)
    
    return answer