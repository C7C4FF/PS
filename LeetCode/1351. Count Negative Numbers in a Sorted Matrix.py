# https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/description/

# non-increasing order > 음수가 나온다면 그 뒤와 그 밑은 전부 음수

# 오른쪽 끝에서부터 순회
# 맨 오른쪽이 0보다 크다면 왼쪽도 전부 0보다 큼. > 아래로 이동
# 0보다 작은 값이 나온다면 음수가 아닐 때까지 왼쪽으로 이동하면서 column의 음수를 다 셈

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        ans = 0

        m, n = len(grid), len(grid[0])
        row, col = 0, n-1
        
        while row < m and col >= 0:
            if grid[row][col] < 0:
                ans += m-row
                col -= 1 # 왼쪽으로
            else:
                row += 1 # 아래로

        return ans



        
        
