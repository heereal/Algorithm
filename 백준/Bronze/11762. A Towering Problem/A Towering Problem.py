from itertools import combinations

arr = list(map(int, input().split()))
total = arr[:6]
h1, h2 = arr[6], arr[7]

for combi in combinations(total, 3):
    if sum(combi) == h1:
        tower2 = [x for x in total if x not in combi]

        if sum(tower2) == h2:
            tower1 = sorted(combi, reverse=True)
            tower2 = sorted(tower2, reverse=True)
            print(*(tower1 + tower2))
            break