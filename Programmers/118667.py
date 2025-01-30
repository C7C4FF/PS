# https://school.programmers.co.kr/learn/courses/30/lessons/118667
# 그냥 하면 시간 초과가 발생해서 최대 큐 길이보다 더 많이 반복된다면 안 된다고 생각하고 반환하기

from collections import deque

def solution(queue1, queue2):
    q1 = deque(queue1)
    q2 = deque(queue2)
    
    sum_q1 = sum(q1)
    sum_q2 = sum(q2)
    
    total = sum_q1 + sum_q2
    
    # 홀수거나 원소 하나가 절반보다 크면 불가능
    if total % 2 != 0:
        return -1
    
    half = total // 2
    
    if max(queue1 + queue2) > half:
        return -1
    
    
    count = 0
    
    while sum_q1 != sum_q2:
        if sum_q1 > sum_q2:
            val = q1.popleft()
            sum_q1 -= val
            q2.append(val)
            sum_q2 += val
        else:
            val = q2.popleft()
            sum_q2 -= val
            q1.append(val)
            sum_q1 += val
        
        count += 1
        
        if count >= 300000:
            return -1
    
    return count
