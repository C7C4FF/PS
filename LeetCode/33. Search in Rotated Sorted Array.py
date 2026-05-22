# https://leetcode.com/problems/search-in-rotated-sorted-array/description/?envType=daily-question&envId=2026-05-22
# O(logN) -> 이진탐색..~ 

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l, r = 0, n-1

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:
                return mid
            
            # 왼쪽 절반이 바르게 정렬되어 있는 경우 -> 타깃이 왼쪽 안에 존재
            if nums[l] <= nums[mid]:
                if nums[l] <= target and target <= nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1

            # 오른쪽이 바르게 정렬되어 있는 경우 -> 타깃이 오른쪽 안에 존재
            else:
                if nums[mid] <= target and target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1

        return -1
