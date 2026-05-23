# https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/?envType=daily-question&envId=2026-05-23

# 정렬되어 있는 배열은 회전되었어도 감소하는 구간이 딱 한번만 존재해야 함
# 1번인 경우에는 시작과 끝을 비교해주기

class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        
        cnt = 0

        for i in range(1, n):
            if nums[i-1] > nums[i]:
                cnt += 1
        
        if cnt > 1:
            return False
        elif cnt == 1:
            if nums[-1] > nums[0]:
                return False

        return True

'''
# https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/?envType=daily-question&envId=2025-02-02
# 제대로 돌았다면, original[i] = nums[i + x % original.length]
# x를 전부 비교하고, 정렬된 거랑 동일한 게 있는지 확인하기.

class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        original = sorted(nums)
        
        ans = [[] for _ in range(n)]

        for x in range(n):
            for j in range(n):
                ans[j].append(nums[(j+x) % n])
        
        for lst in ans:
            if lst == original:
                return True
        
        return False
'''
