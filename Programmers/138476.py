# https://school.programmers.co.kr/learn/courses/30/lessons/138476

# dict_value() 로 value만 뽑아서 쓸 수도 있었음...
# value() 로 뽑고 리스트에 누적합으로 만들어서 해결하기...

import collections

def solution(k, tangerine):
    answer = 0
    cnt = 0
    
    mandarin = list(collections.Counter(tangerine).most_common())
    
    for key, value in mandarin:
        cnt += value
        answer += 1
        if cnt >= k:
            break

    return answer
