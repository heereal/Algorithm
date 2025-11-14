import sys
sys.setrecursionlimit(10**6)

def solution(maps):
    maps = [list(m) for m in maps]
    n, m = len(maps), len(maps[0])
    
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    answer = []
    
    def check(x, y):
        maps[x][y] = 'X'

        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                if maps[nx][ny] != 'X':
                    answer[-1] += int(maps[nx][ny])
                    check(nx, ny)
        
    for x in range(n):
        for y in range(m):
            if 0 <= x < n and 0 <= y < m:
                if maps[x][y] != 'X':
                    answer.append(int(maps[x][y]))
                    check(x, y)

    if answer:
        return sorted(answer)
    else:
        return [-1]