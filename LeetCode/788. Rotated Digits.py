# https://leetcode.com/problems/rotated-digits/?envType=daily-question&envId=2026-05-02

# 0-0, 1-1, 8-8, 2-5, 5-2, 6-9, 9-6, 347은 로테이션 불가능
# 018 은 계산할 필요 x

class Solution:
    def rotatedDigits(self, n: int) -> int:
        valid = '2569'
        invalid = '347'

        ans = 0
        for num in map(str, range(1, n+1)):
            if any(ch in valid for ch in num) and not any(ch in invalid for ch in num):
                ans += 1
            
        return ans
