# https://leetcode.com/problems/keep-multiplying-found-values-by-two/description/

# try except 를 안 쓰고.. 문제에 주어진 대로 하면 됨

class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        while original in nums:
            original *= 2
        
        return original

'''
class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        try:
            idx = nums.index(original)
        except:
            return original
        
        while idx >= 0:
            original *= 2
            try:
                idx = nums.index(original)
            except:
                return original

        return original
'''
                
