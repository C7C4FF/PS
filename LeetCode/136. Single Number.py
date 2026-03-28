# https://leetcode.com/problems/single-number/description/
# Counter.most_common = (원소, 갯수)

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        cnt = Counter(nums)

        return cnt.most_common()[-1][0]
