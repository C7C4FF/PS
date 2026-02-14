# https://leetcode.com/problems/champagne-tower/?envType=daily-question&envId=2026-02-14
# row 잔의 수 = n
# 한번씩 부어서 poured 번을 반복하지 않고, 계속 부어진채로 두기 > 가득차도 어차피 1임

class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        glass = [[0] * i for i in range(1, 102)]
        glass[0][0] = poured

        for row in range(query_row + 1):
            for g in range(row + 1):
                liquid = (glass[row][g] - 1) / 2
                if liquid > 0:
                    glass[row+1][g] += liquid
                    glass[row+1][g+1] += liquid
        
        return min(1, glass[query_row][query_glass])
