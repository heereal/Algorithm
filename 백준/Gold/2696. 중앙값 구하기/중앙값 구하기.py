import sys
from heapq import heappush, heappop
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    m = int(input())
    nums = []

    for _ in range((m // 10) + 1):
        nums += list(map(int, input().split()))
    
    left, right, answer = [], [], [nums[0]]
    mid = nums[0]
        
    for i in range(1, len(nums)):
        if nums[i] > mid:
            heappush(right, nums[i])
        else:
            heappush(left, -nums[i])
        
        if i % 2 == 0:
            if len(left) > len(right):
                heappush(right, mid)
                mid = -heappop(left)
            elif len(left) < len(right):
                heappush(left, -mid)
                mid = heappop(right)
            answer.append(mid)

    print(len(answer))
    for i in range(len(answer)):
        if i != 0 and i % 10 == 0:
            print()
        print(answer[i], end=" ")
    print()
