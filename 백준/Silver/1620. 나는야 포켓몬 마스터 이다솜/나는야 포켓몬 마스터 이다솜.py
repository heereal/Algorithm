import sys
input = sys.stdin.readline

N, M = map(int, input().split())
pokemons = {}

for i in range(1, N+1):
    name = input().strip()
    pokemons[i] = name
    pokemons[name] = i

for _ in range(M):
    q = input().strip()
    if q.isalpha():
        print(pokemons[q])
    else:
        print(pokemons[int(q)])