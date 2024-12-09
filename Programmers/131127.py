# https://school.programmers.co.kr/learn/courses/30/lessons/131127

import collections

def solution(want, number, discount):
    answer = 0
    i = 0
    want_dict = dict(zip(want, number))
    
    while i+10 <= len(discount):
        days = dict(collections.Counter(discount[i:i+10]))
        
        if days == want_dict:
            answer += 1
        
        i += 1
    
    return answer
