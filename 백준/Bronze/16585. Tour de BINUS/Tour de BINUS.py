n = int(input())
rooms = list(map(int, input().split()))
ax, ad = input().split()
bx, bd = input().split()

answer = []

if ad == 'right':
    answer.append(sum(rooms[int(ax) - 1:]))
elif ad == 'left':
    answer.append(sum(rooms[:int(ax)]))

if bd == 'right':
    answer.append(rooms[int(bx) - 1:].count(0))
elif bd == 'left':
    answer.append(rooms[:int(bx)].count(0))

print(answer[0], answer[1])
