# https://school.programmers.co.kr/learn/courses/30/lessons/152996

import collections

def solution(weights):
    answer = 0
    
    cnt = collections.Counter(weights)
    
    for weight in cnt:
        # 자기 자신과 똑같을 때, 여러 개 중 2개를 뽑는 경우
        answer += cnt[weight] * (cnt[weight] - 1) / 2
        
        answer += cnt[weight] * cnt[weight * 2] # 2m, 4m
        answer += cnt[weight] * cnt[weight * 3 / 2] # 3m 2m
        answer += cnt[weight] * cnt[weight * 4 / 3] # 4m 3m
        
    return answer

# 자신의 무게를 w라고 했을 때 시소에 균형이 맞는 무게는
# w, 2w, 1/2w, 2/3w, 3/2w, 4/3w, 3/4w
# 하지만 한 쪽에서만 세면 되니
# w, 2w, 3/2w, 4/3w 만 계산
