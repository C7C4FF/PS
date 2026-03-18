# https://leetcode.com/problems/spiral-matrix/description/

# 오른쪽 > 아래쪽 > 왼쪽 > 위쪽 으로 반복해가면서 ans에 입력하기. 방문한 곳은 "." 으로 처리
# 경계값과 i,j 를 헷갈리지 않도록 주의하기

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        m, n = len(matrix), len(matrix[0])
        total = m * n

        def right(i: int, j: int) -> tuple[int, int]:
            while j < n and matrix[i][j] != ".":
                ans.append(matrix[i][j])
                matrix[i][j] = "."
                j += 1
            
            return i+1, j-1 # 아래쪽으로 가야하니 i+1, j는 경계를 넘었으니 -1

        def down(i: int, j: int) -> tuple[int, int]:
            while i < m and matrix[i][j] != ".":
                ans.append(matrix[i][j])
                matrix[i][j] = "."
                i += 1
            
            return i-1, j-1 # 왼쪽으로 가야하니 j-1, i는 경계를 넘었으니 -1
            
        def left(i: int, j: int) -> tuple[int, int]:
            while j >= 0 and matrix[i][j] != ".":
                ans.append(matrix[i][j])
                matrix[i][j] = "."
                j -= 1
            
            return i-1, j+1 # 위로 가야하니 i-1, j는 경계를 넘었으니 +1
        
        def up(i: int, j: int) -> tuple[int, int]:
            while i >= 0 and matrix[i][j] != ".":
                ans.append(matrix[i][j])
                matrix[i][j] = "."
                i -= 1
            
            return i+1, j+1 # 오른쪽으로 가야하니 j+1, i는 경계를 넘었으니 +1

        x, y = 0, 0
        while len(ans) < total:
            x, y = right(x, y)
            if len(ans) == total: break
            x, y = down(x, y)
            if len(ans) == total: break
            x, y = left(x, y)
            if len(ans) == total: break
            x, y = up(x, y)
            if len(ans) == total: break
        
        
        return ans

