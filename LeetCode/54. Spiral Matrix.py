# https://leetcode.com/problems/spiral-matrix/description/

# 상하좌우의 경계값을 만들고, 한번 돌 때마다 경계 좁힘

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        m, n = len(matrix), len(matrix[0])
        total = m * n
        
        top, bottom = 0, m-1
        left, right = 0, n-1

        while left <= right and top <= bottom:
            # 오른쪽으로
            for i in range(left, right+1):
                ans.append(matrix[top][i])
            top += 1

            if len(ans) == total: break

            # 아래쪽으로
            for j in range(top, bottom+1):
                ans.append(matrix[j][right])
            right -= 1

            if len(ans) == total: break

            # 왼쪽으로
            for k in range(right, left-1, -1):
                ans.append(matrix[bottom][k])
            bottom -= 1

            if len(ans) == total: break

            # 위로
            for l in range(bottom, top-1, -1):
                ans.append(matrix[l][left])
            left += 1
        
        return ans

# -----------------------------
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

