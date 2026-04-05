n = int(input())

for _ in range(n):
    word = input()
    answer = [word[0].lower()]

    for i in range(1, len(word)):
        if ord(word[i]) < 96:
            answer.append(f'_{word[i].lower()}')
        else:
            answer.append(word[i])
    
    print("".join(answer))