# https://school.programmers.co.kr/learn/courses/30/lessons/12938

def solution(n, s):
    answer = []

    # n으로 나눌 수 없다면 -1 반환
    if n > s:
        return [-1]
    
    q, r = divmod(s, n)
    
    answer = [q] * (n-r) + [q+1] * r       
    # 0으로 나누어 떨어질 때를 고려할 필요 없음
    # 곱셈 특성상 한 수가 특출나게 크기보다, 고루 큰 게 더 숫자가 큼
  
    return answer
