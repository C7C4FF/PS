# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/?envType=daily-question&envId=2026-05-15

# O(logN) 의 시간복잡도 > binary search
# 결국 가장 작은 수를 찾기
# 중간 값이 오른쪽 값보다 크면, 최솟값은 무조건 오른쪽에 있음
# 중간값이 오른쪽보다 작거나 같으면 최소값은 왼쪽에 있음

class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)

        l, r = 0, n-1

        while l < r:
            mid = (l + r) // 2

            if nums[mid] > nums[r]:
                l = mid+1    
            else:
                r = mid

        return nums[l]
        
'''
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
# 결국 가장 낮은 수를 찾는 것

class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]
        
        l = 0
        r = n - 1

        while l < r:
            mid = (l + r) // 2

            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        
        return nums[l]
'''
