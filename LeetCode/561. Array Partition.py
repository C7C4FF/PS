class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        sum = 0
        nums.sort()

        for i, n in enumerate(nums):
            # 0부터 짝수들이 가장 작은 수가 됨. (0, 1) (2, 3) ...
            if i % 2 == 0:
                sum += n

        return sum


'''
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        return sum(sorted(nums)[::2])
'''
