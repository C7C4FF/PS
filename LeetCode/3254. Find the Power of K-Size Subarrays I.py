# https://leetcode.com/problems/find-the-power-of-k-size-subarrays-i/description/

class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        ans = []

        for i in range(n-k+1):
            flag = True     # 연속적이고 오름차순으로 정렬되어 있는지 확인

            for j in range(i, i+k-1):
                if nums[j] + 1 != nums[j+1]:
                    flag = False
                    break

            if flag:
                ans.append(nums[i+k-1])
            else:
                ans.append(-1)

        return ans
