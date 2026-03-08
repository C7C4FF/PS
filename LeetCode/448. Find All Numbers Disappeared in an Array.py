# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
# [1, ... , n] 인 리스트 생성 후 차집합으로 빠진 것들 계산

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        unique = set(nums)
        lst = set([i for i in range(1, n+1)])

        return list(lst - unique)
