import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dic = {}

for _ in range(N):
    word = input().strip()

    if len(word) >= M:
        if word in dic:
            dic[word] += 1
        else:
            dic[word] = 1

result = sorted(dic.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))

for key, value in result:
    print(key)