# https://school.programmers.co.kr/learn/courses/30/lessons/17679

# 오른쪽 아래를 기준으로 4개가 같은 항목을 찾고, 해당 좌표 (i, j)를 저장. 그 후 "." 으로 바꾸기
# 애니팡 이후에 . 으로 바꾼 것을 내리는 방법... -> 세로 줄끼리 스택으로 저장. 앞을 "." 으로 채우고 스택을 뒤에 붙이기

'''
# board를 그대로 사용할 때 4개가 모인 것들을 . 으로 바꾸던 함수.
# anipang(board, i-1, j), anipang(board, i, j) 2번씩 쓰기..

def anipang(board, i, j):
    # (i-1, j-1) (i-1, j)
    # (i, j-1), (i, j)
    row = board[i]
    
    row[j-1] = "."
    row[j] = "."
    
    board[i] = "".join(row)
    
    return board
'''

def drop_element(board):
    rows = len(board)
    cols = len(board[0])
    
    for col in range(cols):
        stack = [board[row][col] for row in range(rows)]
        string = [x for x in stack if x.isalpha()]
        dots = rows - len(string)
        dropped = ["."] * dots + string
        
        for row in range(rows):
            board[row][col] = dropped[row]
            
    return board
        
def solution(m, n, board):
    answer = 0
    new_board = [list(row) for row in board]
    
    while True:
        temp = []
        
        for i in range(m):
            for j in range(n):
                if new_board[i][j].isalpha():
                    if i == 0 or j == 0:
                        pass
                    else:
                        if new_board[i][j] == new_board[i-1][j] == new_board[i][j-1] == new_board[i-1][j-1]:
                            temp.append((i, j))
        
        # 삭제
        if temp:
            while temp:
                i, j = temp.pop()
                new_board[i][j] = "."
                new_board[i-1][j] = "."
                new_board[i][j-1] = "."
                new_board[i-1][j-1] = "."
        else:
            break    
        
        # 내리기
        new_board = drop_element(new_board)
        
    
    for row in new_board:
        answer += row.count(".")
    
    return answer
