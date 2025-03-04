# https://leetcode.com/problems/check-if-number-is-a-sum-of-powers-of-three/?envType=daily-question&envId=2025-03-04
# 3진수의 수로 표현하고, distinct 체크는 각 수가 1 이하인지 체크하기

class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        a = ''
        while n:
            q = n // 3
            r = n % 3
            a = str(r) + a
            n = q
        
        if a.count('2'):
            return False
        else:
            return True
