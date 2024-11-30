# https://school.programmers.co.kr/learn/courses/30/lessons/12978
# 다익스트라 알고리즘으로 체크하기
# 도시 간 최대 거리는 500,000으로 제한 되었으니 최댓값으로 설정
# road의 한 원소를 양방향으로 넣어주기

import heapq

def dijkstra(start, graph, distance):
    heap = []
    distance[start] = 0
    heapq.heappush(heap, (0, start))
    
    while heap:
        weight, visit = heapq.heappop(heap)
        
        if distance[visit] < weight:
            continue
        
        for next_visit, next_weight in graph[visit]:
            total_weight = weight + next_weight
            if total_weight < distance[next_visit]:
                distance[next_visit] = total_weight
                heapq.heappush(heap, (total_weight, next_visit))
                
    return distance

def solution(N, road, K):
    graph = [[] for _ in range(N+1)]
    distance = [500000] * (N+1)
    
    for r in road:
        graph[r[0]].append((r[1], r[2]))
        graph[r[1]].append((r[0], r[2]))
    
    result = dijkstra(1, graph, distance)
    
    answer = sum(1 for d in result if d <= K)
    
    return answer
