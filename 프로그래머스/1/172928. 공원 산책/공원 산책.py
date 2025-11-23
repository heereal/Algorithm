def solution(park, routes):
    dirs = {'N': (-1, 0), 'S': (1, 0), 'W': (0, -1), 'E': (0, 1)}
    m, n = len(park), len(park[0])
    answer = [0, 0]
    
    for i in range(n):
        if 'S' in park[i]:
            answer = [i, park[i].index('S')]
            break

    for route in routes:
        dir, dist = route.split()
        dist = int(dist)
        x, y = answer[0], answer[1] 
        
        for i in range(1, dist + 1):
            nx, ny = x + (dirs[dir][0] * i), y + (dirs[dir][1] * i)
            
            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                break
            if park[nx][ny] == 'X':
                break
        else:
            answer = [nx, ny]
        
    return answer