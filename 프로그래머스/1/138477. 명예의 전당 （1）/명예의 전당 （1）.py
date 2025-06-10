import heapq

def solution(k, score):
    answer = []
    heap = []
        
    for s in score:
        if len(heap) < k:
            heapq.heappush(heap, s)
            answer.append(min(heap))
        else:
            if min(heap) <= s:
                heapq.heappushpop(heap, s)
                answer.append(min(heap))
            else:
                answer.append(answer[-1])

    return answer