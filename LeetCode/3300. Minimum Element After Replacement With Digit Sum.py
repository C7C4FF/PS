# https://leetcode.com/problems/minimum-element-after-replacement-with-digit-sum/description/?envType=daily-question&envId=2026-05-29
# str로 한 글자씩 구하기 or 10으로 나눠가며 나머지를 더하기

class Solution:
    def minElement(self, nums: List[int]) -> int:
        digit_sum = []
        
        for num in nums:
            temp_sum = 0
            for digit in str(num):
                temp_sum += int(digit)
            digit_sum.append(temp_sum)

        return min(digit_sum)
