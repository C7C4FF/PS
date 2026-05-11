# https://leetcode.com/problems/minimum-cost-to-split-into-ones/description/

# n = 1 > 1, 0, cost 1
# n = 2 > 1, 1, cost 1
# n = 3 > 1, 2, cost 2
# n = 4 > 1, 3, cost 3

# n을 항상 n-1, 1 로 나누는 게 제일 최적화 됨

class Solution:
    def minCost(self, n: int) -> int:
        def devide(n):
            if n <= 0:
                return n
            else:
                return (n-1) + devide(n-1)

        return devide(n)
