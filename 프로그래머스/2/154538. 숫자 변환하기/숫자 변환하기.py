from collections import deque

def solution(x, y, n): 
    queue = deque()
    queue.append((x, 0)) # 현재 값과 연산 횟수
    visited = set() # 방문한 값들 기록
    
    while queue:
        num, cnt = queue.popleft() 
        if num > y or num in visited: 
            continue
            
        visited.add(num)
        if num == y:
            return cnt
        for k in (num*3, num*2, num+n):
            if k <= y and k not in visited:
                queue.append((k, cnt+1))
    
    return -1
