# https://school.programmers.co.kr/learn/courses/30/lessons/140107

# x^2 + y^2 <= d^2. 찍는 점은 반지름 d인 원 위, 원 안에 있어야 함
# y만 남기고 이항하면 y^2 <= d^2 - x^2
# y <= sqrt(d^2 - x^2) 인데 이제 y는 b*k 이기 때문에...
# b <= sqrt(d^2 - x^2) / k 가 됨

def solution(k, d):
    answer = 0
    
    for i in range(d // k + 1):
        x = i * k
        y = int((d**2 - x**2)**0.5) // k
        answer += y + 1
    
    return answer
