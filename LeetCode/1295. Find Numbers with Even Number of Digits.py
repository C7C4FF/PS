# https://leetcode.com/problems/find-numbers-with-even-number-of-digits/description/

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return sum(len(str(n)) % 2 == 0 for n in nums)
'''
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        def find_even(num: int):
            if len(str(num)) % 2 == 0: return True
            
        return list(map(find_even, nums)).count(True)
'''
