import sys
input = sys.stdin.readline

s = input().rstrip()
q = int(input())

pre = [[0] * 26]

for i, str in enumerate(s):
    next = pre[i][:]
    next[ord(str)-97] += 1
    pre.append(next)

for _ in range(q):
    a, l, r = input().split()
    i = ord(a) - 97
    print(pre[int(r)+1][i] - pre[int(l)][i])
