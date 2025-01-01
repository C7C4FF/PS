# https://school.programmers.co.kr/learn/courses/30/lessons/147354

def solution(data, col, row_begin, row_end):
    answer = 0
    
    # col을 기준으로 오름차순, 동일하면 첫번째 컬럼 기준으로 내림차순
    data.sort(key=lambda x:(x[col-1], -x[0]))
    
    while row_begin <= row_end:
        total = 0
        for element in data[row_begin-1]:
            total += element % row_begin
        
        row_begin += 1

        # bitwise
        answer ^= total
            
    return answer
