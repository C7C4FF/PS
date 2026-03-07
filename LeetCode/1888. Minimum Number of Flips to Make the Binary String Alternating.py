# https://leetcode.com/problems/minimum-number-of-flips-to-make-the-binary-string-alternating/?envType=daily-question&envId=2026-03-07
# TLE ..

class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)

        cycle_s = s + s
        n_cycle = len(cycle_s)

        zero = "0"
        one = "1"

        for i in range(1, n_cycle):
            if zero[-1] == "0":
                zero += "1"
                one += "0"
            else:
                zero += "0"
                one += "1"
        
        if s == one or s == zero:
            return 0

        binary_s = int(cycle_s, 2)
        binary_0, binary_1 = int(zero, 2), int(one, 2)
        mask = (1 << n) - 1

        diff_0 = binary_s ^ binary_0
        diff_1 = binary_s ^ binary_1
        min_dist = n

        for _ in range(n):
            dist_0 = (diff_0 & mask).bit_count()
            dist_1 = (diff_1 & mask).bit_count()

            min_dist = min(min_dist, dist_0, dist_1)

            diff_0 >>= 1
            diff_1 >>= 1
            
            if min_dist == 0:
                return 0
        
        return min_dist
        
        
        
