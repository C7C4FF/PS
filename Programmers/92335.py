# https://school.programmers.co.kr/learn/courses/30/lessons/92335

def is_prime(n):
    if n < 2:
        return False

    # 2부터 sqrt(n) 까지 검사
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    
    return True

def convert_k_base(n, k):
    digits = []
    
    while n > 0:
        digits.append(str(n % k))
        n //= k
        
    return "".join(reversed(digits))

def solution(n, k):
    answer = 0
    
    base = convert_k_base(n, k)
    base = base.split("0")
    
    for number in base:
        if not number:
            continue
        if '0' in number:
            continue
        
        number = int(number)
        
        if is_prime(number):
            answer += 1
    
    return answer
