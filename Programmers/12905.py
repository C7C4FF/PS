# https://school.programmers.co.kr/learn/courses/30/lessons/12905

# for문 만으로 돌리는 건 조금...
# dp[i][j] 는 해당 좌표에서 끝나는 정사각형의 가장 긴 변이 됨

# [0, 1, 1, 1]     [0, 1, 1, 1]    [0, 1, 1, 1]    [0, 1, 1, 1]    [0, 1, 1, 1]
# [1, 1, 1, 1]  =  [1, 0, 0, 0] -> [1, 2, 2, 2] -> [1, 2, 2, 2] -> [1, 2, 2, 2]
# [1, 1, 1, 1]     [1, 0, 0, 0]    [1, 0, 0, 0]    [1, 2, 3, 3]    [1, 2, 3, 3] 
# [0, 0, 1, 0]     [0, 0, 0, 0]    [0, 0, 0, 0]    [0, 0, 0, 0]    [0, 0, 1, 0]

# dp[2][2] = 2가 되어야 할 것 같아서 유효성 검사를 넣었는데 시간 초과...

def solution(board):
    n = len(board)
    m = len(board[0])
    max_side = 0
    
    dp = [[0] * m for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            if board[i][j] == 1:
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
            
                max_side = max(max_side, dp[i][j])
    '''
                # 정사각형의 모든 셀이 1인지 확인
                # 유효성 검사를 하면 시간 초과...... 
                side = dp[i][j]
                valid = True
                for k in range(side):
                    if not all(board[i-k][j-side+1:j+1]):
                        valid = False
                        break
                
                if valid:
                    max_side = max(max_side, side)
                else:
                    dp[i][j] = 0
    '''
    
    return max_side * max_side
