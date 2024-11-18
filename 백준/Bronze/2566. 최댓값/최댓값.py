table = []
max_num = 0
max_row = 0

for i in range(9):
	temp = list(map(int, input().split()))
	table.append(temp)
	temp_max = max(temp)

	if temp_max > max_num:
		max_num = temp_max
		max_row = i

max_col = table[max_row].index(max_num)
print(max_num)
print(max_row + 1, max_col + 1)