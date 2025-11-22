def solution(park, routes):
    m, n = len(park), len(park[0])
    
    cur = [0, 0]
    for i in range(n):
        if 'S' in park[i]:
            cur = [i, park[i].index('S')]
            break
    
    def check_is_possible(x, y, dx, dy):
        is_dx_movable = True
        
        if y != dy:
            is_dx_movable = False
       
        if is_dx_movable:
            for i in range(x, dx + 1):
                if park[i][y] == 'X':
                    return False
        else:
            for i in range(y, dy + 1):
                if park[x][i] == 'X':
                    return False    

        return True

    for s in routes:
        op, d = s.split()
        d = int(d)
        x, y = cur[0], cur[1]
        
        if op == 'N':
            nx, ny = x - d, y
        elif op == 'S':
            nx, ny = x + d, y
        elif op == 'W':
            nx, ny = x, y - d
        elif op == 'E':
            nx, ny = x, y + d
        
        if 0 <= nx < m and 0 <= ny < n:
            if check_is_possible(min(x, nx), min(y, ny), max(x, nx), max(y, ny)):
                cur = [nx, ny]
     
    return cur