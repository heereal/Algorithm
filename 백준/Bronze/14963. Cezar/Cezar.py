n = int(input())
cards = [int(input()) for _ in range(n)]
x = 21 - sum(cards)
go, stop = (x - 1) * 4, (14 - x) * 4

for num in cards:
    if num <= x:
        go -= 1
    else:
        stop -= 1

if stop >= go:
    print('DOSTA')
else:
    print('VUCI')