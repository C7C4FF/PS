# https://leetcode.com/problems/contiguous-array/
# 누적합이 0이라면 0과 1의 갯수가 같은.. 확정인 케이스
# 누적합이 같으면 그 안에 나오는 0과 1의 갯수가 같음

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        ans = 0
        current_sum = 0

        sub = {0: -1}

        for i, bit in enumerate(nums):
            current_sum += 1 if bit == 1 else -1

            if current_sum in sub:
                prev = sub[current_sum]
                ans = max(ans, i - prev)
            else:
                sub[current_sum] = i

        return ans

'''
# TLE

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)

        sub = []
        i = 0

        for bit in nums:
            i += 1 if bit == 1 else -1
            sub.append(i)

        try:
            ans = n - sub[::-1].index(0)
        except:
            pass

        for i in range(n):
            for j in range(i+1, n):
                if sub[i] == sub[j]:
                    ans = max(ans, j-i)

        return ans
'''
