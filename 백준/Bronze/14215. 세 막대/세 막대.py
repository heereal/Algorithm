li = sorted(list(map(int, input().split())))
if li[2] >= li[0] + li[1]:
    print((li[0] + li[1]) * 2 - 1)
else:
    print(sum(li))