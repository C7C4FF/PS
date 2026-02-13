# https://leetcode.com/problems/3sum-closest/

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        cloest = nums[0] + nums[1] + nums[2]
        nums.sort()

        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1

            while left < right:
                sum_of_three = nums[i] + nums[left] + nums[right]

                if abs(target - sum_of_three) < abs(target - cloest):
                    cloest = sum_of_three
                
                if sum_of_three < target:
                    left += 1
                elif sum_of_three > target:
                    right -= 1
                else:
                    return sum_of_three

        return cloest
