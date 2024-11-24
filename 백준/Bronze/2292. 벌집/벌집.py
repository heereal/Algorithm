n = int(input())
rooms = 1
result = 1

while n > rooms:
    rooms += result*6
    result += 1

print(result)