while True:
    n = int(input())

    if n == 0:
        break

    letter = input()
    msg_arr = []

    for i in range(len(letter) // n):
        if i % 2 == 0:
            msg_arr.append(letter[n*i:(n*i)+n])
        else:
            msg_arr.append(letter[n*i:(n*i)+n][::-1])

    answer = ""
    
    for i in range(n):
        for j in range(len(letter) // n):
            answer += msg_arr[j][i]
    
    print(answer)
