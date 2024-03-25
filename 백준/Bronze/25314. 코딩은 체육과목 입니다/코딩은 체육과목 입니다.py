n = int(input())

byte = n // 4
how_long = ""

for i in range(1, byte + 1):
    if i == byte: 
        how_long += "long"
        break
    how_long += "long "

print(how_long, "int")
