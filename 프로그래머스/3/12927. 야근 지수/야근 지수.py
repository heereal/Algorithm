import heapq

def solution(n, works):
    if sum(works) <= n:
        return 0
    
    works = [-w for w in works]
    heapq.heapify(works)
    
    for _ in range(n):
        max_val = heapq.heappop(works)
        heapq.heappush(works, max_val + 1)
    
    return sum([w**2 for w in works])