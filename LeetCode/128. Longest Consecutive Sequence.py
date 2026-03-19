# https://leetcode.com/problems/longest-consecutive-sequence/description/
# 수열의 처음인 경우에만 확인

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        ans = 0
        nums = set(nums)
        for num in nums:
            if num - 1 not in nums:
                current = num
                continued = 1

                while current + 1 in nums:
                    current += 1
                    continued += 1
                
                ans = max(ans, continued)

        return ans


# ------
# heap으로 풀면 O(nlogn) 이라서 통과는 하지만 문제 요구사항에 부합 x

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        heapq.heapify(nums)
        continued = 1
        ans = 1
        prev = heapq.heappop(nums)

        while nums:
            this = heapq.heappop(nums)
            if prev == this:
                continue
            elif prev + 1 == this:
                continued += 1
                ans = max(ans, continued)                
            else:
                continued = 1

            prev = this

        return ans
