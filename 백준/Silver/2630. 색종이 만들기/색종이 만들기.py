n = int(input())
paper = []
result = [0, 0]

for i in range(n):
    row = list(map(int, input().split()))
    paper.append(row)

def solve(x, y, n):
    color = paper[x][y]

    for i in range(x, x + n):
        for j in range(y, y + n):
            if paper[i][j] != color:
                m = n // 2
                solve(x, y, m)
                solve(x + m, y, m)
                solve(x, y + m, m)
                solve(x + m, y + m, m)
                return
    
    if color == 0:
        result[0] += 1
    else:
        result[1] += 1

solve(0, 0, n)

print(result[0])
print(result[1])
