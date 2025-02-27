# https://school.programmers.co.kr/learn/courses/30/lessons/389479

# 서버 1개는 m명을 감당 가능
# nm <= 사용자 <= (n+1)m
# k 시간만큼만..

import heapq

def solution(players, m, k):
    answer = 0
    server = []
    
    for i in range(len(players)):
        while server and server[0] <= i:
            heapq.heappop(server)
        
        std = players[i] // m if players[i] >= m else 0
        
        if len(server) < std:
            gap = std - len(server)
            for _ in range(gap):
                heapq.heappush(server, i+k)
                answer += 1
        
    return answer
