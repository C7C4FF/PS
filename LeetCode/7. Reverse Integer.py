# https://leetcode.com/problems/reverse-integer/
# [::-1] 문자열 뒤집기

class Solution:
    def reverse(self, x: int) -> int:
        target = int(str(abs(x))[::-1])
        
        if target < -(2**31) or target > 2**31 - 1:
            return 0

        if x < 0:
            return -target
        else:
            return target

'''
class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            neg = -1
        else:
            neg = 1

        ans = 0

        x = abs(x)
        while x != 0:
            d = x % 10
            x //= 10

            ans = ans * 10 + d
        
        if ans < -(2**31) or ans > 2**31 - 1:
            return 0
        else:
            return ans * neg
'''
