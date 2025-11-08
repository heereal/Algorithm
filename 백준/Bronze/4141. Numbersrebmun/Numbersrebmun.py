t = int(input())
keypad = ["", "", "ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
dic = {}

for i, s in enumerate(keypad):
    for a in s:
        dic[a] = str(i)

for _ in range(t):
    word = input().upper()
    p_num = ""

    for s in word:
        p_num += dic[s]

    if p_num == p_num[::-1]:
        print('YES')
    else:
        print('NO')