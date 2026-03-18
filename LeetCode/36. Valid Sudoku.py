# https://leetcode.com/problems/valid-sudoku/description/
# 3x3 박스에 중복되는 게 있는지, row, column에 중복되는 값이 있는지 확인

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # row 에 중복되는 값이 있는지
        for i in range(9):
            row = board[i]
            numbers = [x for x in row if x != "."]

            if len(numbers) != len(set(numbers)):
                return False

      
        # 행렬 전치 후 > column에 중복되는 값이 있는지
        board = list(zip(*board))
        for j in range(9):
            col = board[j]
            numbers = [x for x in col if x != "."]

            if len(numbers) != len(set(numbers)):
                return False

        # 3x3 박스에 중복되는 값이 있는지
        for k in range(0, 9, 3):
            for l in range(0, 9, 3):
                box = [board[r][c] for r in range(k, k+3) for c in range(l, l+3)]
                numbers = [x for x in box if x != "."]

                if len(numbers) != len(set(numbers)):
                    return False


        return True
