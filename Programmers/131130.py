# https://school.programmers.co.kr/learn/courses/30/lessons/131130
# 번호 하나마다 쭉 반복하다보면 1 -> 4 -> 7 -> 8 -> 1 -> 4 ... 처럼 사이클이 생기게 됨

import heapq

def solution(cards):
    answer = 0
    
    visited = [0] * len(cards)
    cycles = []
    
    for i in range(len(cards)):
        if not visited[i]:
            cycle = []
            current = i
            
            while not visited[current]:
                visited[current] = 1
                cycle.append(current)
                current = cards[current] - 1
            
            cycles.append(cycle)
    
    if len(cycles) > 1:
        result = heapq.nlargest(2, cycles, key=len)
        return len(result[0]) * len(result[1])
    else:
        return 0
        
    
    

