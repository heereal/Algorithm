a, b, c = map(int, input().split())
length_max = max((a, b, c))
length_sum = sum((a, b, c))

if length_max >= length_sum - length_max:
    print((length_sum - length_max) * 2 - 1)
else:
    print(length_sum)