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
    
    n = len(word)
    front = p_num[:n//2]
    rear = ''

    if n % 2 == 0:
        rear = p_num[:(n//2)-1:-1]
    else:
        rear = p_num[:n//2:-1]

    if front == rear:
        print('YES')
    else:
        print('NO')