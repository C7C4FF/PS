# https://school.programmers.co.kr/learn/courses/30/lessons/42627
# 소요 시간 짧음 -> 요청 시각 빠름 순으로 하기 위해, 힙에 넣어줄 때 순서를 변경해줌

import heapq

def solution(jobs):
    answer = 0
    i = 0
    time = -1
    n = len(jobs)
    waits = []
    
    # 정렬 해주기
    jobs.sort(key=lambda x: x[0])
    
    while jobs or waits or time > 0:
        while jobs and jobs[0][0] == i:
            r, t = jobs.pop(0)
            # 요청시각과 소요시간의 순서 변경
            heapq.heappush(waits, [t, r])
        
        if time <= 0:
            # 대기 큐에 있을 때만 task를 수행하기
            if waits:
                time, request = heapq.heappop(waits)
                
        else:
            time -= 1
            if time == 0:
                answer += (i - request)
                if waits:
                    time, request = heapq.heappop(waits)
                    
        i += 1
        
    return answer // n
