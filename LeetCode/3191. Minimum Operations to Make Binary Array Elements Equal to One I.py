# https://leetcode.com/problems/minimum-operations-to-make-binary-array-elements-equal-to-one-i/?envType=daily-question&envId=2025-03-19
# 힌트 1번이 아주 큰 도움 -> greedy 하게 생각하기
# If nums[0] is 0, then the only way to change it to 1 is by doing an operation on the first 3 elements of the array.
# 오른쪽을 다 바꿔도, 결국 왼쪽을 뒤집으려면 그 해당 인덱스를 시작점으로 뒤집어야 함.

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        cnt = 0
        for i in range(n-2):
            # 1이라면 1 - 1 로 0이 되고, 0이라면 1 - 0 으로 1이 됨
            if nums[i] == 0:
                nums[i] = 1 - nums[i]
                nums[i+1] = 1 - nums[i+1]
                nums[i+2] = 1 - nums[i+2]
                cnt += 1
            else:
                # 1이면 건너뛰기
                continue
        
        # 전부 1이라면
        if sum(nums) == n:
            return cnt
        else:
            return -1
