n = int(input())
frame = [input() for _ in range(n)]
answer = ""

def compress(x, y, n):
    global answer
    color = frame[x][y]

    for i in range(x, x + n):
        for j in range(y, y + n):
            if frame[i][j] != color:
                answer += "("
                m = n // 2
                compress(x, y, m)
                compress(x, y + m, m)
                compress(x + m, y, m)
                compress(x + m, y + m, m)
                answer += ")"
                return
                
    if color == "0":
        answer += "0"
    else:
        answer += "1"

compress(0, 0, n)
print(answer)