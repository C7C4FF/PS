# https://leetcode.com/problems/equal-sum-grid-partition-i/?envType=daily-question&envId=2026-03-25
# 리스트 안의 리스트들을 하나로 합칠 때 sum(List[List[int]], []) > sum(sum(List[List[int]], [])) 로 바로 구할 수 있지만 시간 + 메모리를 많이 잡아먹음.

# 두 영역이 나와야 하니까 마지막은 안 해도 됨

class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        
        # 총 합이 홀수라면 애초에 불가능
        total = sum(sum(row) for row in grid)
        if total % 2 != 0:
            return False

        row_sum = 0
        for i in range(m-1):
            row_sum += sum(grid[i])
            if row_sum == (total // 2):
                return True
        
        # 세로 누적합 계산
        col = [sum(grid[i][j] for i in range(m)) for j in range(n)]

        col_sum = 0
        for i in range(n-1):
            col_sum += col[i]
            if col_sum == (total // 2):
                return True

        return False
            



