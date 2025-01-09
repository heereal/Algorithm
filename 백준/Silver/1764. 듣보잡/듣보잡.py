import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dic = {input().strip() : False for _ in range(N)}
dic = dict(sorted(dic.items()))
cnt = 0

for _ in range(M):
    name = input().strip()
    if name in dic:
        dic[name] = True
        cnt += 1

print(cnt)

for name in dic:
    if dic[name]:
        print(name)