s = input()
korea = "KOREA"
i = 0

for str in s:
    if str == korea[i % 5]:
        i += 1

print(i)