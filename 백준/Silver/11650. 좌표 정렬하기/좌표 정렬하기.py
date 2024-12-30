import sys
input = sys.stdin.readline

N = int(input())
li = []

for _ in range(N):
    temp = list(map(int, input().split()))
    li.append(temp)
    
li.sort()

for i in li:
    print(*i)
