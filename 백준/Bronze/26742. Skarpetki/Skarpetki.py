from collections import Counter

str = input()
dic = Counter(str)
answer = 0

for i in dic:
    if dic[i]:
        answer += dic[i] // 2

print(answer)