# https://leetcode.com/problems/check-if-binary-string-has-at-most-one-segment-of-ones/?envType=daily-question&envId=2026-03-06
# 모든 1이 이어져 있는지 확인하기... > 시작이 0 이니 01 조합이 나온다면 False

class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        n = len(s)
        
        for i in range(1, n):
            if s[i-1] + s[i] == "01":
                return False

        return True
