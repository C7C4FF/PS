# https://leetcode.com/problems/minimum-swaps-to-arrange-a-binary-grid/?envType=daily-question&envId=2026-03-02

class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)
        pos = [-1] * n
        ans = 0

        # 가장 오른쪽에 있는 1의 위치 저장
        for i in range(n):
            for j in range(n-1, -1, -1):
                if grid[i][j] == 1:
                    pos[i] = j
                    break
        
        # j번째 행의 오른쪽 1의 위치가 i 이하라면, i번째 자리에 들어갈 수 있음
        for i in range(n):
            k = -1
            for j in range(i, n):
                if pos[j] <= i:
                    ans += j - i
                    k = j
                    break
            
            if k != -1:
                for j in range(k, i, -1):
                    pos[j], pos[j-1] = pos[j-1], pos[j]
            else:
                return -1
        
        return ans
