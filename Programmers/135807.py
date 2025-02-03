# https://school.programmers.co.kr/learn/courses/30/lessons/135807
# 3.9 이하에서는 math.gcd() 가 인자를 두 개만 받음.
# functools 의 reduce 를 사용하거나.. 원소 하나를 받아서 gcd 함수에 사용하기
# 3.9 이상에서는 math.gcd(*array) 등으로 지정하면 리스트를 바로 인자로 사용할 수 있음

import math

def get_gcd(array):
    gcd = array[0]
    
    for i in range(len(array)):
        gcd = math.gcd(gcd, array[i])
    
    return gcd

def solution(arrayA, arrayB):
    a = get_gcd(arrayA)
    b = get_gcd(arrayB)
    
    if a == 1:
        a = 0
    else:
        if all(e % a != 0 for e in arrayB):
            pass
        else:
            a = 0
    
    if b == 1:
        b = 0
    else:
        if all(e % b != 0 for e in arrayA):
            pass
        else:
            b = 0
        
    return max(a, b)
