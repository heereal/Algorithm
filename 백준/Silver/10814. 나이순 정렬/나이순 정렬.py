import sys
input = sys.stdin.readline

N = int(input())
li = []

for _ in range(N):
    member = input().split()
    li.append(member)

li.sort(key=lambda x: int(x[0]))

for member in li:
    print(*member)