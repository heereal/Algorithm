import heapq

def solution(S, K):
    cnt = 0
    heap = []
    
    for i in S:
        heapq.heappush(heap, i)
    
    while heap[0] < K:
        if len(heap) >= 2:
            cnt += 1
            a = heapq.heappop(heap)
            b = heapq.heappop(heap)
            heapq.heappush(heap, a + (b * 2))
        else:
            cnt = -1
            break
   
    return cnt