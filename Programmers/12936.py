# https://school.programmers.co.kr/learn/courses/30/lessons/12936

import math

def solution(n, k):
    line = [i+1 for i in range(n)]
    factorial = [math.factorial(i) for i in range(0, n)]
    answer = []
    
    for i in range(n, 0, -1):
        quotient = (k-1) // factorial[i-1]
        k = k % factorial[i-1]
        
        index = line.pop(quotient)
        answer.append(index)
    
    return answer

# 1 2, 2 1 -> 1개 (1)
# 1 2 3, 1 3 2 -> 2개 (2x1)
# 1 2 3 4, 1 2 4 3, 1 3 2 4, 1 3 4 2, 1 4 2 3, 1 4 3 2 -> 6개 (3x2x1)
# 2 1 3 4, 2 1 4 3, 2 3 1 4, 2 3 4 1, 2 4 1 3, 2 4 3 1 ...

# 앞에서부터 (n-1)! (n-2)! ... 의 가짓수를 가짐
# n=4 일 때를 예로 들면 맨 앞이 1인 경우는 6가지, 2인 경우는 6가지, ...
# 맨 앞이 정해지고 나면 그 다음은 (4-2)! -> 2가지를 가짐


'''
시간 초과

import itertools

def solution(n, k):
    line = [i+1 for i in range(n)]
    target = list(itertools.permutations(line))
    
    answer = target.pop(k-1)
    
    return answer
'''
