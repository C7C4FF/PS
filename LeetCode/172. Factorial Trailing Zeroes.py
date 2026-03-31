# https://leetcode.com/problems/factorial-trailing-zeroes/description/
# 뒤에 0이 몇개 있는지 > 2x5 가 몇개 있는지
# 팩토리얼이니 어차피 5가 있다면 2도 있음 > 5만 세기

class Solution:
    def trailingZeroes(self, n: int) -> int:
        cnt_five = 0

        while n > 1:
            cnt_five += n // 5
            n //= 5
        
        return cnt_five
