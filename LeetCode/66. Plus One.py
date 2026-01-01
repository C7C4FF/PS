# https://leetcode.com/problems/plus-one/?envType=daily-question&envId=2026-01-01

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = int(''.join(map(str, digits))) + 1
        ans = []
        
        for n in str(num):
            ans.append(int(n))
        
        return ans
        

