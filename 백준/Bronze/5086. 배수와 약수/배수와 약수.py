while True:
    x, y = map(int, input().split())
    if x == 0 and y == 0:
        break

    factor = y % x
    multiple = x %y

    if factor == 0:
        print("factor")
    elif multiple == 0:
        print("multiple")
    else:
        print("neither")