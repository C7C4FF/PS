# https://school.programmers.co.kr/learn/courses/30/lessons/12980

def solution(n):
    ans = 0
    
    if n == 1:
        return 1
    
    while n:
        if n % 2 == 0:
            n = n // 2
        
        else:
            n -= 1
            ans += 1

    return ans
