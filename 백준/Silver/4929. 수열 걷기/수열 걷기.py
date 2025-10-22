while True:
    x = list(map(int, input().split()))

    if x[0] == 0:
        break

    x = set(x[1:])
    y = set(list(map(int, input().split()))[1:])
    inter = sorted(x & y)
    
    x = sorted(list(x))
    y = sorted(list(y))

    answer = 0
    x_sum, y_sum = 0, 0

    for n in inter:
        a = sum(x[:x.index(n) + 1]) - x_sum
        b = sum(y[:y.index(n) + 1]) - y_sum

        if a >= b:
            answer += a
        else:
            answer += b
        
        x_sum += a
        y_sum += b
        
    a = sum(x) - x_sum
    b = sum(y) - y_sum

    if a >= b:
        answer += a
    else:
        answer += b
    
    print(answer)