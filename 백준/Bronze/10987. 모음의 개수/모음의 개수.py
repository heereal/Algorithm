word = list(input())
answer = 0

for v in ['a', 'e', 'i', 'o', 'u']:
    answer += word.count(v)

print(answer)
