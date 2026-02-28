# https://leetcode.com/problems/concatenation-of-consecutive-binary-numbers/?envType=daily-question&envId=2026-02-28

class Solution:
    def concatenatedBinary(self, n: int) -> int:
        ans = 0
        bit = ""
        mod = 10**9 + 7

        for i in range(1, n+1):
            bit += bin(i)[2:]

        return int(bit, 2) % mod
