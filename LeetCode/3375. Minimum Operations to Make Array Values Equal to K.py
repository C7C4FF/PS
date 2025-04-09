# https://leetcode.com/problems/minimum-operations-to-make-array-values-equal-to-k/?envType=daily-question&envId=2025-04-09
# k로 만들기... k 보다 작은 수가 있다면, 무조건 실패
# k 보다 큰 수의 종류가 횟수가 됨.

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        lst = Counter(nums).keys()

        ans = 0
        for n in lst:
            if n < k:
                return -1
            elif n > k:
                ans += 1
            else:
                pass

        return ans
