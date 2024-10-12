total_price = int(input())
total_number = int(input())
sum = 0

for _ in range(total_number):
    price, number = map(int, input().split())
    sum += price * number

if total_price == sum:
    print("Yes")
else:
    print("No")
