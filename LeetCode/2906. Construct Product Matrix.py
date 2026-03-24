# https://leetcode.com/problems/construct-product-matrix/description/?envType=daily-question&envId=2026-03-24
# 나보다 뒤에 있는 모든 수의 곱을 구하고, 역으로 나보다 앞에 있는 모든 수의 곱을 구해서 곱함
# 수가 점점 커질수록 걸리는 부담이 많아짐 > 매 루프마다 MOD 연산 수행해서 값을 줄이기

class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n, m = len(grid), len(grid[0])
        MOD = 12345

        lst = []

        
        p = 1
        # 나보다 뒤에 있는 모든 수의 곱, prefix
        for i in range(n):
            row = []
            for j in range(m):
                row.append(p)
                p = (p * grid[i][j]) % MOD
            lst.append(row)
        
        p = 1
        # 나보다 뒤에 있는 모든 수의 곱, suffix
        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                lst[i][j] = (lst[i][j] * p) % MOD
                p = (p * grid[i][j]) % MOD

        return lst
