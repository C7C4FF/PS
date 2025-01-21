# https://school.programmers.co.kr/learn/courses/30/lessons/160585

def solution(board):
    first = 0
    second = 0
    
    first_flag = False
    second_flag = False
    
    for line in board:
        first += line.count("O")
        second += line.count("X")

    # 가로, 세로
    for i in range(3):
        if board[i][0]+board[i][1]+board[i][2] == "OOO" or board[0][i]+board[1][i]+board[2][i] == "OOO":
            first_flag = True
        if board[i][0]+board[i][1]+board[i][2] == "XXX" or board[0][i]+board[1][i]+board[2][i] == "XXX":
            second_flag = True

    # 대각선
    if board[0][0]+board[1][1]+board[2][2] == "OOO" or board[0][2]+board[1][1]+board[2][0] == "OOO":
        first_flag = True
    if board[0][0]+board[1][1]+board[2][2] == "XXX" or board[0][2]+board[1][1]+board[2][0] == "XXX":
        second_flag = True
    
    if (
        second > first or # 후공 순서 오류
        first - second >= 2 or # 선공 순서 오류
        (first_flag == True and first <= second) or # 선공이 이겼는데도 게임을 계속
        (first_flag == True and second_flag == True) or # 두 명 다 이기는 경우
        (second_flag == True and first > second) # 후공이 이겼는데도 게임을 계속
    ):
        return 0
    else:
        return 1
