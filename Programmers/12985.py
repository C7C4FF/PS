# https://school.programmers.co.kr/learn/courses/30/lessons/12985

def solution(n,a,b):
    answer = 1
    a, b = min(a, b), max(a, b)

    while n:
        if a+1 == b and a % 2 == 1 and b % 2 == 0:
            break
        a = a // 2 + a % 2
        b = b // 2 + b % 2
        n //= 2

        answer += 1
        
    return answer

# a가 작은 수, b가 큰 수로 정의
# 둘이 만나려면 한 라운드에서 만나려면 a+1 == b 뿐만 아니라, a가 홀수이고 b가 짝수여야 함
# 한 라운드가 끝나면 인원이 절반으로 줄어들기에 2로 나누고, 나머지를 더해주면 다음 라운드의 번호가 됨
