# https://school.programmers.co.kr/learn/courses/30/lessons/68936

'''
    00 01 02 03  04 05 06 07
    10 11 12 13  14 15 16 17
    20 21 22 23  24 25 26 27
    30 31 32 33  34 35 36 37
    
    40 41 42 43  44 45 46 47
    50 51 52 53  54 55 56 57
    60 61 62 63  64 65 66 67
    70 71 72 73  74 75 76 77
'''

def check_quadrant(arr, length):
'''
반환 조건: 모두 0 or 모두 1 or 2x2 행렬이 됐을 때
그 외의 경우는 사분원을 쪼개가며 재귀호출
'''
    is_zero = all(all(x == 0 for x in row) for row in arr)
    is_one = all(all(x == 1 for x in row) for row in arr)
    
    mid = length // 2
    
    if is_zero:
        return [1, 0]
    elif is_one:
        return [0, 1]
    
    quadrant_i = []
    quadrant_ii = []
    quadrant_iii = []
    quadrant_iv = []
        
    for i in range(mid):
        quadrant_i.append(arr[i][mid:])
        quadrant_ii.append(arr[i][:mid])
        quadrant_iii.append(arr[mid+i][:mid])
        quadrant_iv.append(arr[mid+i][mid:])
        
    else:
        result_i = check_quadrant(quadrant_i, mid)
        result_ii = check_quadrant(quadrant_ii, mid)
        result_iii = check_quadrant(quadrant_iii, mid)
        result_iv = check_quadrant(quadrant_iv, mid)
        
        return [result_i[0] + result_ii[0] + result_iii[0] + result_iv[0],
               result_i[1] + result_ii[1] + result_iii[1] + result_iv[1]]

def solution(arr):
    length = len(arr)
    answer = check_quadrant(arr, length)
    
    return answer
