def solution(cap, n, deliveries, pickups):
    dist = 0
    delivery = 0
    pickup = 0
    
    for i in range(n - 1, -1, -1):
        delivery += deliveries[i]
        pickup += pickups[i]
        
        while delivery > 0 or pickup > 0:
            delivery -= cap
            pickup -= cap
            dist += i + 1
    
    return dist * 2
    