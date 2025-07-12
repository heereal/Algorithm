n = input()
s = '1' * len(n)

if n == "0":
    print(1)
elif int(n) >= int(s):
    print(len(n))
else:
    print(len(n) - 1)