# https://school.programmers.co.kr/learn/courses/30/lessons/340212

# 처음 레벨은 1임

# 난이도가 레벨 이하라면 time[cur] 만큼 시간을 써서 품
# 난이도가 레벨보다 높다면, 퍼즐을 총 '난이도-레벨' 만큼 틀림
# 추가로 time[cur-1] 만큼 시간을 써서 이전 퍼즐을 풀고 와야 함
# 이전 문제를 풀고 + 이번 문제를 풀면 레벨업. 그걸 time[cur-1] * (diffs[i] - level) 번 해야 함
# 그래서 한계 안으로 들어오면서, 가장 높은 레벨은 얼마인가..

# 최소 레벨 1, 최대 레벨 100,000 (가장 어려운 난이도)으로 이분 탐색 진행

def solution(diffs, times, limit):
    answer = 0
    left, right = 1, max(diffs)
    
    while left <= right:
        level = (left + right) // 2
        duration = 0
        
        for i in range(len(diffs)):
            if diffs[i] > level:
                duration += (times[i-1] + times[i]) * (diffs[i] - level) + times[i]
            else:
                duration += times[i]
        
        if duration > limit:
            left = level + 1
        else:
            right = level - 1
    
    return right + 1

'''
# 문제 중 가장 높은 난이도로 시작해서 하나씩 낮추기

시간 초과

def solution(diffs, times, limit):
    level = max(diffs)
    time = 0
    
    while time <= limit:
        temp = 0
        
        for i in range(len(diffs)):
            if diffs[i] > level:
                temp += (times[i-1] + times[i]) * (diffs[i] - level) + times[i]
            else:
                temp += times[i]
        
        if temp > time:
            time = temp
        
        level -= 1
    
    return level + 2
'''
