# https://school.programmers.co.kr/learn/courses/30/lessons/17684

from string import ascii_uppercase

def solution(msg):
    '''
    LZW 알고리즘으로 문자열 압축하기.
    한 글자씩 더해보며 lzw 딕셔너리 안에 문자열이 없다면, 딕셔너리에 해당 문자열을 추가
    마지막으로 추가한 문자를 제외한 index를 answer에 등록 및 초기화
    '''
    answer = []
    lzw = {char: idx + 1 for idx, char in enumerate(ascii_uppercase)}
    
    cnt = 27
    current_word = ""
    
    for char in msg:
        current_word += char
        if current_word not in lzw:
            lzw[current_word] = cnt
            cnt += 1

            answer.append(lzw[current_word[:-1]])
            current_word = char
            
    if current_word:
        answer.append(lzw[current_word])
            
    return answer
