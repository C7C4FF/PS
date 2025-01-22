# https://school.programmers.co.kr/learn/courses/30/lessons/154538

from collections import deque

def solution(x, y, n):
    if x == y:
        return 0
    
    queue = deque([(x, 0)])
    visited = set([x])
    
    while queue:
        value, steps = queue.popleft()
        
        for result in (value + n, value * 2, value * 3):
            if result == y:
                return steps + 1
            
            if result < y + 1 and result not in visited:
                visited.add(result)
                queue.append((result, steps + 1))
        
    return -1
