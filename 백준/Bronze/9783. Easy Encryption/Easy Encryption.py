message = input()
answer = ""

for s in message:
    if s.isdigit():
        answer += f'#{s}'
    elif s.isupper():
        answer += str(ord(s)-38)
    elif s.islower():
        i = ord(s)-96
        if i < 10:
            answer += f'0{i}'
        else:
            answer += str(ord(s)-96)
    else:
        answer += s
    
print(answer)