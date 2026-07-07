# https://leetcode.com/problems/concatenate-non-zero-digits-and-multiply-by-sum-i/description/?envType=daily-question&envId=2026-07-07

class Solution:
    def sumAndMultiply(self, n: int) -> int:
        x = 0
        total = 0
        p = 1

        while n > 0:
            d = n % 10
            total += d
            if d > 0:
                x += d * p
                p *= 10
            n //= 10
        
        return x * total
