# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one/?envType=daily-question&envId=2026-02-26

class Solution:
    def numSteps(self, s: str) -> int:
        ans = 0
        n = int(s, 2)

        while n != 1:
            if n % 2 == 0:
                n //= 2
            else:
                n += 1
            
            ans += 1

        return ans
