# https://leetcode.com/problems/clear-digits/?envType=daily-question&envId=2025-02-10
# re.search로 문자-숫자 쌍이 존재할 동안 반복하기

class Solution:
    def clearDigits(self, s: str) -> str:
        pattern = r'[a-z][0-9]'
        condition = re.search(pattern, s)

        while condition:
            start, end = condition.span()
            s = s[:start]+s[end:]
            condition = re.search(pattern, s)
            
        return s
