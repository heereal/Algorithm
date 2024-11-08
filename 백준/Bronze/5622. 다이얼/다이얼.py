word = input()
arr = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
result = 0

for str in word:
    for i in arr:
        if str in i:
            result += arr.index(i) + 3
            break

print(result)