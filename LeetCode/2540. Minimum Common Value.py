# https://leetcode.com/problems/minimum-common-value/?envType=daily-question&envId=2026-05-19
# 교집합 중에 가장 작은 수 찾기

class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        common_set = set(nums1) & set(nums2)

        if common_set:
            return min(common_set)

        return -1
