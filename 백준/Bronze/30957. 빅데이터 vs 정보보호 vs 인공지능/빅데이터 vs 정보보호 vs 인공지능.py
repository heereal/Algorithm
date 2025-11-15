from collections import Counter

n = int(input())
interested = input()

count = Counter(interested)
max_count = max(count.values())

res = ""

for c in ['B', 'S', 'A']:
    if count[c] == max_count:
        res += c

if len(res) == 3:
    print('SCU')
else:
    print(res)