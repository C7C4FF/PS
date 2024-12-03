# https://school.programmers.co.kr/learn/courses/30/lessons/42577

def solution(phone_book):
    '''
    특정 전화번호가 다른 전화번호의 접두-맨 앞에 존재하는지 확인
    사전 순으로 정렬하면 자신의 뒤의 것만 확인하면 됨
    '''
    answer = True
    
    phone_book.sort()
    
    for i in range(len(phone_book)-1):
        if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
            return False
    
    return answer


'''
# 효율성 실패
def solution(phone_book):
    answer = True
    
    phone_book.sort()
    
    for i in range(len(phone_book)):
        phone = phone_book[i]
        rest = phone_book[i+1:]
        
        length = len(phone)
        
        for rest_phone in rest:
            if rest_phone[:length] == phone:
                return False
        

    return answer
'''
