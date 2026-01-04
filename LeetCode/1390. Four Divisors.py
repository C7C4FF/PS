# https://leetcode.com/problems/four-divisors/?envType=daily-question&envId=2026-01-04

class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)

        for num in nums:
            j = 1
            temp = set()
            sqrt_num = math.isqrt(num)

            while j <= sqrt_num:
                if num % j == 0:
                    temp.add(j)
                    temp.add(num // j)
                j += 1

            if len(temp) == 4:
                ans += sum(temp)
        
        return ans
                    
            

