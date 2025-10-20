import sys
input = sys.stdin.readline
from collections import Counter

n = int(input())

for i in range(1, n + 1):   
    x = Counter(input().strip())
    y = Counter(input().strip())

    union = x & y
    x = sum((x - union).values())
    y = sum((y - union).values())
    
    print(f'Case #{i}: {x + y}')