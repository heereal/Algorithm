import sys
input = sys.stdin.readline

N = int(input())

names = set()
cnt = 0

for i in range(N):
    name = input().strip()

    if name == 'ENTER':
        cnt += len(names)
        names = set()
    else:
        names.add(name)

cnt += len(names)
print(cnt)