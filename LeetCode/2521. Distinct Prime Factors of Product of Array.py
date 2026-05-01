# https://leetcode.com/problems/distinct-prime-factors-of-product-of-array/description/

# 1000 이하의 소수를 모두 판별하기? > sqrt(n) 까지만 구하기...

class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        prime = set()

        for n in nums:
            d = 2
            while d * d <= n:
                if n % d == 0:
                    prime.add(d)
                    n //= d
                else:
                    d += 1
            
            if n > 1:
                prime.add(n)

        return len(prime)

'''

class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        prime = set()

        for n in nums:
            if n == 2 or n == 3:
                prime.add(n)
            
            else:
                d = 2
                while d <= n:
                    if n % d == 0:
                        prime.add(d)
                        n //= d
                    else:
                        d += 1

        return len(prime)
                
'''
