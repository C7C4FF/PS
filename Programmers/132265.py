# https://school.programmers.co.kr/learn/courses/30/lessons/132265
# 앞, 뒤에서부터 차례대로 새로운 토핑이 생길 때마다 1씩 더해서 해당 구간에서 몇개의 토핑이 있는지 확인함
# [0, 1, 2, 2, 3, 3, 4, 4, 4]  |  [0, 1, 2, 3, 3, 4]
# [4, 4, 4, 4, 3, 3, 2, 1, 0]  |  [4, 4, 3, 2, 1, 0]
# 둘이 동일한 토핑 개수를 공유하고 있으면 answer에 1 추가..

from collections import defaultdict

def solution(topping):
    answer = 0
    
    n = len(topping)
    
    prefix_dist = [0] * (n+1)
    suffix_dist = [0] * (n+1)
    
    left = defaultdict(int)
    right = defaultdict(int)
    
    for i in range(1, n+1):
        t = topping[i-1]
        prefix_dist[i] = prefix_dist[i-1]
        if left[t] == 0:
            prefix_dist[i] += 1
        left[t] += 1
    
    for i in range(n-1, -1, -1):
        t = topping[i]
        suffix_dist[i] = suffix_dist[i+1]
        if right[t] == 0:
            suffix_dist[i] += 1
        right[t] += 1

  
    for i in range(1, n):
        if prefix_dist[i] == suffix_dist[i]:
            answer += 1
    
    return answer
