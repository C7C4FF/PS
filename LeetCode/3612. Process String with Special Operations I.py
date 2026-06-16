# https://leetcode.com/problems/process-string-with-special-operations-i/description/?envType=daily-question&envId=2026-06-16
# * 마지막 글자 제거, % 뒤집기, # 복제하기

class Solution:
    def processStr(self, s: str) -> str:
        ans = ""
        for ch in s:
            if ch.isalpha():
                ans += ch
            elif ch == "*":
                ans = ans[:len(ans)-1]
            elif ch == "%":
                ans = ans[::-1]
            elif ch == "#":
                ans = ans + ans

        return ans
