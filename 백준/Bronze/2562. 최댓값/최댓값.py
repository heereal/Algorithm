int_list = []
for _ in range(9):
    int_list.append(int(input()))

max = max(int_list)
print(max)
print(int_list.index(max)+1)