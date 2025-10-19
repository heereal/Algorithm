word = input()
n = len(word)

index_u = word.index('U')
index_f = n- word[::-1].index('F') - 1

answer = ('-' * index_u) + 'U' + ('C' * (index_f - index_u - 1)) + 'F' + ('-' * (n - index_f -  1))
print(answer)