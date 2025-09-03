def solution(routes):
    routes.sort(key=lambda x: x[1])
    camera = routes[0][1]
    answer = 1
    
    for start, end in routes:
        if start > camera:
            answer += 1
            camera = end
        
    return answer