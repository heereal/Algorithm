import sys
input = sys.stdin.readline

N = int(input())
li = []

for _ in range(N):
    li.append(input().strip())

li = sorted(set(li))
li.sort(key=len)

for i in li:
    print(i)