# https://school.programmers.co.kr/learn/courses/30/lessons/134239

# 짝수라면 / 2, 홀수라면 *3 + 1
# 5 -> 16 -> 8 -> 4 -> 2 -> 1
# 3 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1

# 정적분 구간을 왜 이렇게 나눈지 모르겠지만...
# 뒤에서부터 -1 -2 .. 로 생각하기.

# x의 길이는 1인 사다리꼴의 넓이를 구하는 문제로 바꾸면 해결.
# 단, 주어진 구간의 시작점이 끝점보다 커서 유효하지 않은 구간이 주어질 수 있으며 이때의 정적분 결과는 -1로 정의합니다.

def solution(k, ranges):
    answer = []
    
    f = [k]
    k_val = k
    
    while k_val > 1:
        if k_val % 2 == 0:
            k_val /= 2
        else:
            k_val = k_val * 3 + 1
        f.append(int(k_val))
        
    n = len(f)
    
    for a, b in ranges:
        b += n - 1
        total = 0
        
        if a > b:
            answer.append(-1)
        elif a == b:
            answer.append(0)
        else:
            while a < b:
                area = (f[a] + f[a+1]) / 2
                total += area
                a += 1
            answer.append(total)
    
    return answer
