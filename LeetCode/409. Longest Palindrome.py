# https://leetcode.com/problems/longest-palindrome/description/

class Solution:
    def longestPalindrome(self, s: str) -> int:
        cnt = Counter(s)
        ans = 0
        odd = 0

        for k, v in cnt.items():
            q, r = divmod(v, 2)
            ans += q * 2
            odd = max(odd, r)

        return ans + odd 
