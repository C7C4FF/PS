# https://leetcode.com/problems/minimum-deletions-to-make-string-balanced/description/?envType=daily-question&envId=2026-02-07
# (b, a) 쌍이 없으면 균형잡힘 -> 스택에 저장하면서 ba 쌍을 없애주기

class Solution:
    def minimumDeletions(self, s: str) -> int:
        stack = []
        ans = 0

        for ch in s:
            if ch == 'a' and stack and stack[-1] == 'b':
                stack.pop()
                ans += 1
            else:
                stack.append(ch)
        
        return ans
