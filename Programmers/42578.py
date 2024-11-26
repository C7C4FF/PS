# https://school.programmers.co.kr/learn/courses/30/lessons/42578

import collections

def solution(clothes):
    answer = 1
    wardrobe = collections.defaultdict(int)
    
    for cloth, group in clothes:
        wardrobe[group] += 1
    
    for key in wardrobe:
        answer *= wardrobe[key] + 1
        
    return answer - 1

# 하나 있으면 n개,
# 종류가 다른 옷이 n개, m개 있으면 조합의 수는 n + m + n*m 개
# n, m, k라면 n + m + k + nm + nk + mk + nmk ...
# n + m + nm = (n+1)(m+1) - 1 = nm + n + m + 1 - 1
# n + m + k + nm + nk + mk + nmk = (n+1)(m+1)(k+1) - 1 = n + m + k + nm + nk + mk + 1 - 1 
