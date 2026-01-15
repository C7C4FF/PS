# https://leetcode.com/problems/zigzag-conversion/description/?envType=study-plan-v2&envId=top-interview-150
# t < numRows 내려가는 중, t >= numRows 올라오는 중

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        rows = [[] for _ in range(numRows)]
        period = 2 * (numRows - 1)

        if numRows == 1:
            return s
        
        for i in range(len(s)):
            t = i % period
            index = t if t < numRows else period - t
            rows[index].append(s[i])
        
        ans = ''.join(''.join(row) for row in rows)

        return ans
