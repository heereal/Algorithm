import sys
input = sys.stdin.readline

n = int(input())
a = sorted(list(map(int, input().split())))
b = sorted(list(map(int, input().split())))

for i in range(n):
    if b[i] < a[i]:
        print('NE')
        break
else:
    print('DA')