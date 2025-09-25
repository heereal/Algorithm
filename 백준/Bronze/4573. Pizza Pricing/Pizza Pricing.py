import sys
input = sys.stdin.readline

menu_number = 0

while True:
    n = int(input())
    menu_number += 1

    if n == 0:
        break
    
    arr = []
    for _ in range(n):
        d, p = map(int, input().split())
        arr.append((p / d ** 2, d))
    
    print(f'Menu {menu_number}: {min(arr)[1]}')