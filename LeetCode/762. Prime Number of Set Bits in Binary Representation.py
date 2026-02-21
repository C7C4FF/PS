# https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation/?envType=daily-question&envId=2026-02-21

class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        ans = 0
        lst = [bin(i)[2:] for i in range(left, right+1)]

        
        def is_prime(number: int) -> bool:
        '''
        1, 특정 수로 나누어지는 수는 소수가 아님
        '''
            if number == 1:
                return False
                
            for i in range(2, int(math.sqrt(number)) + 1):
                if number % i == 0:
                    return False
            return True
        
        for n in lst:
            x = n.count('1')
            if is_prime(x):
                ans += 1

        return ans
            
