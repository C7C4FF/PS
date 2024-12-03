# https://school.programmers.co.kr/learn/courses/30/lessons/17686

import re

def solution(files):
'''
정규표현식으로 숫자가 1회부터 5번 반복하는 처음 경우를 찾음.
span()으로 해당 인덱스들을 받아주고, 슬라이싱으로 HEAD, NUMBER 분리, 비교를 위해 원래 파일 이름과 인덱스를 저장.
HEAD, NUMBER, index 순으로 정렬하고 answer에는 원래 file 이름만 넣어서 반환
'''
    answer = []
    temp = []
    i = 0
    
    for file in files:
        findnum = re.compile(r'[0-9]{1,5}')
        this = findnum.search(file)
        
        start, end = this.span()
        
        head = file[0:start].lower()
        number = file[start:end]
        
        temp.append([head, int(number), file, i])
        i += 1
        
    temp.sort(key=lambda x:(x[0], x[1], x[3]))
    
    answer = [file[2] for file in temp]
        
    return answer
