import sys
input = sys.stdin.readline

N = int(input())
li = []

for _ in range(N):
    temp = list(map(int, input().split()))
    li.append(temp)

li.sort(key=lambda x: (x[1], x[0]))

for i in li:
    print(*i)