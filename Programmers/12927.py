# https://school.programmers.co.kr/learn/courses/30/lessons/12927

import heapq

def solution(n, works):
    works = [-x for x in works]
    heapq.heapify(works)

    while n > 0 and works:
        largest = -heapq.heappop(works)
        
        if largest > 0:
            largest -= 1
            heapq.heappush(works, -largest)
            
        n -= 1

    return sum(x**2 for x in works)
