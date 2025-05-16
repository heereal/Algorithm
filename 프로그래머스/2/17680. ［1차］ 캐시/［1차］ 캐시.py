from collections import deque

def solution(cacheSize, cities):
    cache = deque()
    answer = 0
    
    if cacheSize == 0:
        return 5 * len(cities) 
    
    for i in range(len(cities)):
        city = cities[i].lower()
        
        if len(cache) < cacheSize:
            if city not in cache:
                answer += 5
                cache.append(city)
            else:
                answer += 1
                cache.remove(city)
                cache.append(city)
        elif city in cache:
            answer += 1
            cache.remove(city)
            cache.append(city)
        else:
            answer += 5
            cache.popleft()
            cache.append(city)
    
    return answer