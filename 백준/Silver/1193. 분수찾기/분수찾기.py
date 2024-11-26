n = int(input())
line = 1

while n > line:
    n -= line
    line += 1

if line%2 == 0:
    print(f"{n}/{line-n+1}")
else:
    print(f"{line-n+1}/{n}")