S = input()
case = set()

for i in range(len(S)):
    for j in range(len(S)-i):
        case.add(S[j:j+i+1])

print(len(case))
