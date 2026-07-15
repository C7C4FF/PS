# https://leetcode.com/problems/gcd-of-odd-and-even-sums/?envType=daily-question&envId=2026-07-15
# 이렇게 하면 항상 n이 gcd가 된다.. return n 만 해도 정답

import math

class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        odd, even = 0, 0
        cnt = 1
        i = 1
        while cnt <= n:
            odd += i
            even += i + 1
            cnt += 1
            i += 2
        
        return math.gcd(odd, even)
