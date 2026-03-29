from collections import Counter

n = int(input())
for _ in range(n):
    li = input().split()
    first = [x[0] for x in li]
    c = Counter(first)
    sorted_tiems = sorted(c.items(), key=lambda x: (-x[1], x[0]))
    print(sorted_tiems[0][0])