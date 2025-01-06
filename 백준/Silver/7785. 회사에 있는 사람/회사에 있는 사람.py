import sys
input = sys.stdin.readline

n = int(input())
dic = {}

for _ in range(n):
    name, record = input().split()
    if record == 'enter':
        dic[name] = True
    elif record == 'leave':
        del dic[name]

for name in sorted(dic.keys(), reverse=True):
    print(name)