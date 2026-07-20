# https://leetcode.com/problems/shift-2d-grid/?envType=daily-question&envId=2026-07-20
# 1차원 리스트로 만들고 나머지 연산

class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        ans = []
        m, n = len(grid), len(grid[0])

        flatten = [i for sublist in grid for i in sublist]
        steps = k % (m * n)

        if steps == 0:
            return grid

        new_list = flatten[-steps:] + flatten[:-steps]

        for i in range(0, m*n, n):
            row = new_list[i:i+n]
            ans.append(row)

        return ans
        
