# https://leetcode.com/problems/a-number-after-a-double-reversal/description/

class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        reversal = str(num)[::-1]
        double_reversal = str(int(reversal))[::-1]

        if int(double_reversal) == num:
            return True
        else:
            return False
