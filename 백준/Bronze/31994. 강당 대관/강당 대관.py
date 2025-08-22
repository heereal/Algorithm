name = []
number = []

for _ in range(7):
    nam, num = input().split()
    name.append(nam)
    number.append(int(num))


print(name[number.index(max(number))])