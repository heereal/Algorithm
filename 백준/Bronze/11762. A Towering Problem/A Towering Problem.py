from itertools import combinations
from collections import Counter

arr = list(map(int, input().split()))
total = arr[:6]
h1, h2 = arr[6], arr[7]

for combi in combinations(total, 3):
    if sum(combi) == h1:
        tower2 = (Counter(total) - Counter(combi)).keys()
        
        if sum(tower2) == h2:
            tower1 = sorted(combi, reverse=True)
            tower2 = sorted(tower2, reverse=True)
            print(*(tower1 + tower2))
            break