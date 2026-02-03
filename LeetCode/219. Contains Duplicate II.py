# https://leetcode.com/problems/contains-duplicate-ii/description/
# 딕셔너리로 마지막에 본 인덱스 저장

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        seen = {}

        for i in range(n):
            if nums[i] not in seen:
                seen[nums[i]] = i
            else:
                if abs(i - seen[nums[i]]) <= k:
                    return True
                else:
                    seen[nums[i]] = i
        
        return False
