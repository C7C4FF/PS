# https://school.programmers.co.kr/learn/courses/30/lessons/154539

def solution(numbers):
    answer = [-1] * len(numbers)
    index = []
    
    for i in range(len(numbers)):
        value = numbers[i]
        
        while index:
            # 큰 수를 발견하면, index.pop을 통해 최신화
            if numbers[index[-1]] < value:
                answer[index.pop()] = value
            else:
                break
                
        # 가장 가까운 인덱스를 리스트에 저장
        index.append(i)
            
    return answer

'''
# 시간초과
# 역순으로 이중 for 문을 사용한 풀이는 통과한 것을 보면
# [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ... , 1, 9] 이런 식의 테스트 케이스에서 시간 소요가 났던 것 같음

def solution(numbers):
    answer = []
    
    for i in range(len(numbers)):
        chk = []
        for j in numbers[i+1:]:
            if numbers[i] < j:
                chk.append(j)
                break
        
        if chk:
            answer.append(chk.pop())
        else:
            answer.append(-1)
            
    return answer


'''
