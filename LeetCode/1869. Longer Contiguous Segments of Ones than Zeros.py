# https://leetcode.com/problems/longer-contiguous-segments-of-ones-than-zeros/description/

class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        zeros, length_zero = 0, 0
        ones, length_one = 0, 0

        for n in s:
            if n == "0":
                zeros += 1
                ones = 0
                length_zero = max(zeros, length_zero)
            else:
                ones += 1
                zeros = 0
                length_one = max(ones, length_one)

        return length_one > length_zero
