# https://leetcode.com/problems/count-total-number-of-colored-cells/?envType=daily-question&envId=2025-03-05

# 처음에는 1 그 다음부터는 이전에 더해졌던 것 +4 씩..
# An = 1 + 4 + 8 + 12 + 16 + ... + 4(n-1)
#    = 1 + 4(1 + 2 + 3 + ... + n-1)
#    = 1 + 4(n(n-1)/2) = 1 + 2n(n-1)

class Solution:
    def coloredCells(self, n: int) -> int:
        return 1 + 2*n*(n-1)
