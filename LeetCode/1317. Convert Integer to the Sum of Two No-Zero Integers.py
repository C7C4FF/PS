# https://leetcode.com/problems/convert-integer-to-the-sum-of-two-no-zero-integers/description/

class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        i = 1
        while i <= n//2:
            if ('0' in str(i)) or ('0' in str((n-i))):
                pass
            else:
                return i, (n-i)
            i += 1
