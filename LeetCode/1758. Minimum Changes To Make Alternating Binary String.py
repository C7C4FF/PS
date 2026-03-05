# https://leetcode.com/problems/minimum-changes-to-make-alternating-binary-string/description/?envType=daily-question&envId=2026-03-05

class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)

        zero = "0"
        one = "1"

        for i in range(1, n):
            if zero[-1] == "0":
                zero += "1"
                one += "0"
            else:
                zero += "0"
                one += "1"

        c0, c1 = 0, 0

        for i in range(n):
            if s[i] != zero[i]:
                c0 += 1
            
            if s[i] != one[i]:
                c1 += 1
            
        return min(c0, c1)
            
