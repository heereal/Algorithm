import sys
import heapq
input = sys.stdin.readline

N = int(input())
heap = []

for i in range(N):
    nums = list(map(int, input().split()))
    for j in range(N):
        heapq.heappush(heap, nums[j])
    heap = heapq.nlargest(N, heap)

print(heap[-1])