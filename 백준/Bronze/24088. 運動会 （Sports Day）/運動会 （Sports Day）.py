n = int(input())
k = int(input())
s = input()

red = s.count('R')
print('W' if k == red else 'R')