dad = input().split()
mom = input().split()

colors = set([dad[0], dad[1], mom[0], mom[1]])
sorted_colors = sorted(list(colors))

for c1 in sorted_colors:
    for c2 in sorted_colors:
        print(c1, c2)