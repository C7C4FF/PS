# https://leetcode.com/problems/flip-square-submatrix-vertically/description/?envType=daily-question&envId=2026-03-21
# grid[x][y] 를 topleft로 하는 kxk 매트릭스 구하기 > x:x+k y:y+k
# row 씩 리스트에 넣고, 뒤집고 다시 바꿔주기

class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        row = []
        
        for i in range(x, x+k):
            row.append(grid[i][y:y+k])
        
        row = row[::-1]
        
        for i in range(k):
            grid[x+i][y:y+k] = row[i]

        return grid
            

        
