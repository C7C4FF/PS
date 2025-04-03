# https://leetcode.com/problems/maximum-value-of-an-ordered-triplet-i/?envType=daily-question&envId=2025-04-02
# ans = (nums[0] - nums[1]) * nums[2]
# 결국 답이 되는 가장 큰 곱셈의 결과는 가장 뒤의 인덱스로 결졍되기 떄문에 for 문에서 가장 먼저 업데이트를 해줌.

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        largest_value = 0
        diff = 0
        ans = 0

        for i in range(len(nums)):
            ans = max(ans, diff * nums[i])
            largest_value = max(largest_value, nums[i])
            diff = max(diff, largest_value - nums[i])
            
        return ans if ans >= 0 else 0

'''
# bruteforce 로도 풀기

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        ans = 0

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    print(i,j,k)
                    ans = max(ans, (nums[i] - nums[j]) * nums[k])
        
        return ans if ans >= 0 else 0
'''
