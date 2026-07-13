# https://leetcode.com/problems/sequential-digits/description/?envType=daily-question&envId=2026-07-13
# 슬라이딩 윈도우로 생각하기...


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        ans = []
        digit = "123456789"
        
        for length in range(len(str(low)), len(str(high)) + 1):
            for i in range(10 - length): 
                num = int(digit[i:i + length])
                if low <= num <= high:
                    ans.append(num)
                    
        return ans

'''
class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        ans = []
        digit = "123456789"

        n = len(str(low))

        for i in range(len(digit)-n+1):
            for j in range(i+n, len(digit)+1):
                num = int(digit[i:j])
                if num > high:
                    break
                elif num < low:
                    continue
                else:
                    ans.append(num)

        ans.sort()
        return ans
'''
