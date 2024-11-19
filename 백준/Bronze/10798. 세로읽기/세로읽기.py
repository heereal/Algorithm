word_list = [input() for _ in range(5)]

for i in range(15):
	for j in range(5):
		if i < len(word_list[j]):
			print(word_list[j][i], end='')