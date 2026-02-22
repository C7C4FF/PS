# https://leetcode.com/problems/binary-gap/?envType=daily-question&envId=2026-02-22
# (?=(패턴)) 으로 이미 찾았던 부분까지 계속 참조해서 찾기

class Solution:
    def binaryGap(self, n: int) -> int:
        ans = 0
        pattern = r"(?=(10*1))"
        n = bin(n)[2:]

        result = re.finditer(pattern, n)
        
        for i in result:
            start, end = i.span(1)
            ans = max(end - start - 1, ans)

        return ans
