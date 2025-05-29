from collections import deque

def solution(priorities, location):
    queue = deque([i for i in range(len(priorities))])
    cnt = 0
    
    while True:
        i = queue.popleft()
        
        if max(priorities) == priorities[i]:
            priorities[i] = 0
            cnt += 1   
            if i == location:
                return cnt   
        else:
            queue.append(i)
