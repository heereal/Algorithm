n = int(input())
k = int(input())

cards = []
visited = [False] * n
answer = set()

for _ in range(n):
    cards.append(input())

def DFS(num, cnt):
    if cnt == k:
        answer.add(num)
        return

    for i in range(n):
        if not visited[i]:
            visited[i] = True
            DFS(num + cards[i], cnt + 1)
            visited[i] = False

DFS("", 0)
print(len(answer))