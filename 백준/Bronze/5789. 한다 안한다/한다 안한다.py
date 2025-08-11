n = int(input())

for _ in range(n):
    s = input()
    half = len(s) // 2

    if s[half-1] == s[half]:
        print('Do-it')
    else:
        print('Do-it-Not')