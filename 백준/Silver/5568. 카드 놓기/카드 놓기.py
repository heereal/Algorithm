from itertools import permutations

n = int(input())
k = int(input())

cards = [input() for _ in range(n)]
answer = set()

for case in permutations(cards, k):
    answer.add("".join(case))

print(len(answer))