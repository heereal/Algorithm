import sys
input = sys.stdin.readline

n = int(input())
name_list = set()

for _ in range(n):
    name, record = input().split()
    if record == 'enter':
        name_list.add(name)
    elif record == 'leave':
        name_list.remove(name)

for name in sorted(name_list, reverse=True):
    print(name)