from collections import Counter

arr = input().split()
res = Counter(arr).values()

if len(res) < len(arr):
    print('no')
else:
    print('yes')