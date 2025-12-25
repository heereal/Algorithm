import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    a, b = input().split()
    if Counter(a) == Counter(b):
        print('Possible')
    else:
        print('Impossible')