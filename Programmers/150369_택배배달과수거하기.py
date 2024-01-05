def solution(cap, n, deliveries, pickups):
    answer = 0
    deliveries = deliveries[::-1]
    pickups = pickups[::-1]
    
    deli_num = 0
    pickup_num = 0
    
    for i in range(n):
        deli_num += deliveries[i]
        pickup_num += pickups[i]
        
        while deli_num > 0 or pickup_num > 0:
            deli_num -= cap
            pickup_num -= cap
            
            answer += (n-i)*2
        
    return answer