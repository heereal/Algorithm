L = input()

for i in range(7):
    G = input()

    if L == G:
        print('WINNER')
        break
    elif i == 6:
        print('LOSER')
        break
    else:
        res = ''
        for j in range(5):
            if L[j] == G[j]:
                res += 'G'
            elif G[j] in L:
                res += 'Y'
            else:
                res += 'X'
        print(res)