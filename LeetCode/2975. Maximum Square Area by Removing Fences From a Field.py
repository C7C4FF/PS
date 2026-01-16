# https://leetcode.com/problems/maximum-square-area-by-removing-fences-from-a-field/?envType=daily-question&envId=2026-01-16

class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        x = sorted(set([1, m] + hFences))
        y = sorted(set([1, n] + vFences))

        all_x = set()
        for i in range(len(x)):
            for j in range(i+1, len(x)):
                all_x.add(x[j] - x[i])
        
        side = 0
        for i in range(len(y)):
            for j in range(i+1, len(y)):
                if y[j] - y[i] in all_x:
                    side = max(side, y[j] - y[i])
            
        if side == 0:
            return -1
        else:
            return (side * side) % (10**9 + 7)
