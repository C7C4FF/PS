# https://leetcode.com/problems/game-of-life/
# 얕은 복사 조심하기

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]]

        prefix = copy.deepcopy(board)
        
        for i in range(m):
            for j in range(n):
                neighbors = 0

                for dx, dy in directions:
                    next_x, next_y = i + dx, j + dy

                    if 0 <= next_x < m and 0 <= next_y < n:
                        if board[next_x][next_y] == 1:
                            neighbors += 1
                    
                
                if board[i][j] == 1:
                    if neighbors < 2 or neighbors > 3: # 2 미만, 3 초과면 죽음
                        prefix[i][j] = 0
                    else: # 2~3 이어야만 다음 세대로 생존
                        prefix[i][j] = 1
                else:
                    if neighbors == 3: # 죽은 셀은 주위에 정확히 3개의 산 셀이 있으면 살아남
                        prefix[i][j] = 1

            
        board[:] = prefix
        
