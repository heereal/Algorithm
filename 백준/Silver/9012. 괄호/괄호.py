T = int(input())

for i in range(T):
    str = input()

    while True:
        if str == '':
            print('YES')
            break
        elif '()' not in str:
            print('NO')
            break
        else:
            str = str.replace('()', '')