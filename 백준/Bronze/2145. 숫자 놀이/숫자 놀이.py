while True:
    n = input()
    if n == "0":
        break

    while True:
        new = sum(int(n[i]) for i in range(len(n)))
        n = str(new)

        if (new // 10) == 0:
            print(new)
            break
