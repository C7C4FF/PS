# https://school.programmers.co.kr/learn/courses/30/lessons/12946

answer = []

def hanoi(x, now_pos, aux, move_pos):
    if x == 1:
        answer.append([now_pos, move_pos])
    else:
        # x-1 개를 가운데 기둥으로 옮기기
        hanoi(x-1, now_pos, move_pos, aux)
        answer.append([now_pos, move_pos])
        # 가운데 기둥의 것들을 끝으로 옮기기
        hanoi(x-1, aux, now_pos, move_pos)
        
def solution(n):
    hanoi(n, 1, 2, 3)
        
    return answer

# 11 / 12 13 23 / 33
# 111 / 113 123 122 322 321 331 / 333
# n번째 판을 끝 기둥으로 옮기기 위해선 n-1개의 판들이 전부 가운데 기둥에 있어야 함
# 마지막으로 옮길 판만 남았을 때 재귀호출 종료
