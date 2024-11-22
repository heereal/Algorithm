n = int(input())
change_list = [25, 10, 5, 1]

for i in range(n):
    change = int(input())
    for j in change_list:
        if change:
            print(change // j, end=" ")
            change = change % j
        else:
            print(0, end=" ")
    print()