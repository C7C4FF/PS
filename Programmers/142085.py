# https://school.programmers.co.kr/learn/courses/30/lessons/142085#

import heapq

def solution(n, k, enemy):
    answer = 0
    saikyou = []
    
    for e in enemy:
        n -= e
        heapq.heappush(saikyou, (-e, e))
        
        if n < 0 and k > 0:
            invinsible = heapq.heappop(saikyou)[1]
            n += invinsible
            k -= 1
        
        if n >= 0:
            answer += 1
        else:
            break
            
            
        
    return answer

'''
81.3

import heapq

def solution(n, k, enemy):
    answer = 0
    saikyou = []
    heap = []
    
    for e in enemy:
        n -= e
        heapq.heappush(heap, (-e, e))
        
        if len(heap) > k and k > 0:
            invinsible = heapq.heappop(heap)[1]
            k -= 1
            n += invinsible
            heapq.heappush(saikyou, invinsible)
        
        if saikyou:
            if e > saikyou[0] and k == 0:
                n -= heapq.heappop(saikyou)
                n += e
                heapq.heappush(saikyou, e)
        
        if n >= 0:
            answer += 1
        elif n < 0 and k > 0:
            answer += 1
        else:
            break
            
        
    return answer
'''
