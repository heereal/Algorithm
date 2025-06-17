from collections import deque

def solution(n, m, section):
    answer = 0
    queue = deque(section)
    
    while queue:
        last = queue.popleft() + m - 1
        answer += 1
        
        for wall in range(len(queue)):
            if queue[0] <= last:
                queue.popleft()
            else:
                break
            
    return answer