class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 투포인터로 판별
        def expand(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1 : right]

        # 한글자 or 이미 펠린드롬일 경우
        if len(s) == 1 or s == s[::-1]:
            return s
        
        result = ''
        
        # 홀수인 경우 +2, 짝수인 경우 +1
        for i in range(len(s) - 1):
            result = max(result, expand(i, i+1), expand(i, i+2), key=len)

        return result
