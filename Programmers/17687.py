# https://school.programmers.co.kr/learn/courses/30/lessons/17687

# 전체 부르는 수는 t*m
# 수가 뒤집혀서 나오기 때문에 저장할 때 앞에 붙여주기
# p-1 부터, m번째마다 나오도록 [p-1::m], t개만 출력하도록 [:t]

def solution(n, t, m, p):
    base = "0123456789ABCDEF"
    base_n = base[:n]
    
    answer = '0'
    cnt = 1
    
    while len(answer) < t * m:
        result = ''
        number = cnt
        
        while number != 0:
            remainder = number % n
            number = number // n
            
            result = base_n[remainder] + result
        
        answer += result
        cnt += 1
        
    return answer[p-1::m][:t]
