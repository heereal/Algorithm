import sys
sys.setrecursionlimit(10**6)

dirs = [(1, 0, "d"), (0, -1, "l"), (0, 1, "r"), (-1, 0, "u")]

def solution(n, m, x, y, r, c, k):
    dist = abs(x - r) + abs(y - c)
    if dist > k:
        return 'impossible'
    if dist % 2 != k % 2:
        return 'impossible'
    
    def dfs(a, b, cnt, path):
        if cnt == k:
            if a == r and b == c:
                return path
        else:
            for dx, dy, dir in dirs:
                nx, ny = a + dx, b + dy
                if 1 <= nx <= n and 1 <= ny <= m:
                    dist = abs(nx - r) + abs(ny - c)
                    if dist > k - (cnt + 1):
                        continue
                        
                    result = dfs(nx, ny, cnt + 1, path + dir)
                    if result is not None:
                        return result
    
    answer = dfs(x, y, 0, "")

    return answer