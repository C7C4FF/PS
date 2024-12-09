# https://school.programmers.co.kr/learn/courses/30/lessons/131701

# 원형 수열을 만들기 위해서 두 배로 늘리기
# 다른 방법이 있을 것 같음,,

def solution(elements):
    temp = elements * 2
    s = set()
    
    for i in range(1, len(elements)+1):
        for j in range(len(elements)):
            s.add(sum(temp[j:j+i]))

    return len(s)
