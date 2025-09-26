from collections import Counter
import sys
input = sys.stdin.readline

n = int(input())
A = [input().strip() for _ in range(n)]
B = [input().strip() for _ in range(n)]

intersection = Counter(A) & Counter(B)
print(sum(intersection.values()))