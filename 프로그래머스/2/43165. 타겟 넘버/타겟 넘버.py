from collections import deque

def solution(nums, target):
    queue = deque([0])
    cnt = 0
    
    for num in nums:
        size = len(queue)
        for _ in range(size):
            res = queue.popleft()
            queue.append(res + num)
            queue.append(res - num)
    
    for res in queue:
        if res == target:
            cnt += 1     
                
    return cnt