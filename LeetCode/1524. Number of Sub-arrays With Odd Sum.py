# https://leetcode.com/problems/number-of-sub-arrays-with-odd-sum/submissions/1604444057/?envType=daily-question&envId=2025-02-25
# 홀수가 되려면...
# 0+홀수. 짝수 + 홀수

# num 이 짝수라면, 그 전에 만들었던 subarray 들은 변하는 게 없음.
# 반대로 홀수라면, 홀수 subarraay는 짝수가 되고, 짝수 subarray는 홀수가 됨 

class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        odd = 0
        even = 0
        cnt = 0
        
        for num in arr:
            if num % 2 == 0:
                even += 1
            else:
                even, odd = odd, even
                odd_cnt += 1
            cnt += odd_cnt

        return cnt % (10**9 + 7)
