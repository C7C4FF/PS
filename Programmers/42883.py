# https://school.programmers.co.kr/learn/courses/30/lessons/42883

def solution(number, k):
    '''
    남은 자리수 rest_length 만큼 반복하면서 가장 최대의 값 뽑기
    뽑으면 해당 인덱스를 설정해줘서, 그 뒤부터 탐색하도록 함
    '''
    answer = ''
    
    length = len(number) - k
    index = 0
    
    while len(answer) < length:
        rest_length = length - len(answer)
        max_value = '0'
        
        for i in range(index, len(number) - rest_length + 1):
            if number[i] > max_value:
                max_value = number[i]
                index = i
                
                if max_value == '9':
                    break
        
        answer += max_value
        index += 1
    
    return answer

'''
# 시간 초과
def solution(number, k):
    answer = ''

    length = len(number) - k
    index = 0
    
    while len(answer) < length:
        temp = []
        if len(answer) == 0:
            for i in range(len(number)-length+1):
                temp.append([i, int(number[i])])
    
        else:
            rest_length = length - len(answer)
            
            for i in range(index+1, len(number)-rest_length+1):
                temp.append([i, int(number[i])])
    
            temp.sort(key=lambda x:-x[1])
            index, value = temp.pop(0)
            
        answer += str(value)
    
    return answer
'''    
