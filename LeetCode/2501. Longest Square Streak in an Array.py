# https://leetcode.com/problems/longest-square-streak-in-an-array/description/

class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        ans = -1
        
        unique_nums = sorted(set(nums))

        for i in range(len(unique_nums)):
            n = unique_nums[i]
            length = 1
            
            for j in range(i, len(unique_nums)):
                target = n**2
                if target >= 10**5: # 최대 가능한 수가 10**5 까지 되므로 그 이상이면 더 이상 계산 x
                    break

                if unique_nums[j] == target:
                    length += 1
                    n = unique_nums[j]
                    if length == 5: # 가능한 최대 길이는 5까지만 되니 5라면 그만 계산하기
                        return 5
            
            if length != 1: # 초기값과 다르다면 갱신하기
                ans = max(ans, length)
        
        return ans
