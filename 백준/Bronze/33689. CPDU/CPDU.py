n = int(input())
answer = 0

for _ in range(n):
    word = input()
    if word[0] == 'C':
        answer += 1

print(answer)