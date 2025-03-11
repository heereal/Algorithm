import heapq
import sys
input = sys.stdin.readline

N = int(input())
heap = []

for _ in range(N):
    num = int(input())

    if num > 0:
        heapq.heappush(heap, num)
    else:
        if heap:
            print(heapq.heappop(heap))
        else:
            print(0)