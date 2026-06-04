# https://leetcode.com/problems/total-waviness-of-numbers-in-range-i/description/?envType=daily-question&envId=2026-06-04
# 브루트 포스..~ 

class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        wave = 0

        for number in range(num1, num2+1):
            num = str(number)
            n = len(num)
            if n < 3:
                continue

            for i in range(2, n):
                # case 1 peak
                if num[i-1] > num[i] and num[i-1] > num[i-2]:
                    wave += 1

                # case 2 valley
                if num[i-1] < num[i] and num[i-1] < num[i-2]:
                    wave += 1
            
        return wave
                
