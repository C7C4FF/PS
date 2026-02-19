# https://leetcode.com/problems/count-binary-substrings/?envType=daily-question&envId=2026-02-19
# ... 그룹 별로 나눠서 최솟값을 더하기

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        ans = 0
        stack = [1]

        for i in range(1, len(s)):
            if s[i-1] == s[i]:
                stack[-1] += 1
            else:
                stack.append(1)
        
        for i in range(1, len(stack)):
            ans += min(stack[i-1], stack[i])
        
        return ans
