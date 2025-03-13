# https://leetcode.com/problems/zero-array-transformation-ii/?envType=daily-question&envId=2025-03-13
# 차이 배열을 이용해서, 제로 어레이가 되는 최소 K를 찾기.

class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        def check(mid):
            diff = [0 for _ in range(len(nums)+1)]

            for i in range(mid):
                l, r, v = queries[i]
                diff[l] -= v
                diff[r+1] += v
            
            temp = 0
            for i in range(len(nums)):
                temp += diff[i]
                # 0 보다 크다면 더 검사하지 않고 중지
                if nums[i] + temp > 0:
                    return False
            return True

        # nums 리스트가 처음부터 zero-array 인지 확인
        if all(n <= 0 for n in nums):
            return 0

        # 이진 탐색 수행
        left, right = 0, len(queries)
        ans = -1
        while left <= right:
            mid = (left + right) // 2

            # True => zero-array 라면 최소 k 찾기.
            if check(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
            
        return ans


'''
# MLE ..
class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        diff = [0 for _ in range(len(nums)+1)]
        cnt = []

        if all(n <= 0 for n in nums):
            return 0

        for l, r, v in queries:
            diff[l] -= v
            diff[r+1] += v
            cnt.append(diff[::])

        for i in range(len(cnt)):
            temp = nums[::]
            for j in range(1, len(cnt[i])):
                cnt[i][j] += cnt[i][j-1]
            
            valid = True
            for j in range(len(nums)):
                temp[j] += cnt[i][j]
            
                if temp[j] > 0:
                    valid = False
                    break

            if valid:
                return i+1

        return -1
-----
#TLE ,,
#O(n.length * queries.length) 를 줄이기...

class Solution:
    def check(self, diff_temp, nums_temp):
        for i in range(1, len(diff_temp)):
            diff_temp[i] += diff_temp[i-1]
        
        for i in range(len(nums_temp)):
            nums_temp[i] += diff_temp[i]
            
            if all(n <= 0 for n in nums_temp):
                return True
        
        return False

    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        diff = [0 for _ in range(len(nums)+1)]
        cnt = 0

        if all(n <= 0 for n in nums):
            return cnt

        for l, r, v in queries:
            diff[l] -= v
            diff[r+1] += v
            cnt += 1

            diff_temp = diff[::]
            nums_temp = nums[::]
            
            if self.check(diff_temp, nums_temp):
                return cnt

        return -1
'''
