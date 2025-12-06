m = int(input())
answer = 25 + (m * 0.01)

if answer < 100:
    print("%0.2f"%100)
elif answer > 2000:
    print("%0.2f"%2000)
else:
    print("%0.2f"%answer)