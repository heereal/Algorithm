word = input()
answer = []
i = 0

while i < len(word):
    ch = word[i]
    count = 0
    while i < len(word) and word[i] == ch:
        i += 1
        count += 1
    answer.append(ch * (count - 1))

print("".join(answer))