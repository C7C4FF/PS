# https://leetcode.com/problems/sqrtx/description

class Solution:
    def mySqrt(self, x: int) -> int:
        return int(math.sqrt(x))

'''
class Solution:
    def mySqrt(self, x: int) -> int:
        ans = 0

        if x == 1:
            return x

        lo, hi = 1, x // 2 + 1

        while lo <= hi:
            mid = (lo + hi) // 2
            sqrt = mid ** 2
            
            if sqrt <= x:
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1

        return ans
'''
