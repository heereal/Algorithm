month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

while True:
    d, m, y = map(int, input().split())

    if y == 0: 
        break

    answer = sum(month[:m - 1]) + d
    
    if m > 2:
        if y % 400 == 0:
            answer += 1
        elif y % 100 == 0:
            print(answer)
            continue
        elif y % 4 == 0:
            answer += 1 
    
    print(answer)