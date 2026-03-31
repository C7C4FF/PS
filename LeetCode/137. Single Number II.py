# https://leetcode.com/problems/single-number-ii/description/

# 모든 원소는 정확히 세번 등장. (찾아야 하는 원소 1개 제외)
# 각 비트 자리수마다 등장한 횟수 세기, 3번 등장하면 다시 0으로 초기화

# [2,2,3,2] > 2: 010, 3: 011
# ones = (000 ^ 010) & ~(000) = 010 & 111 = 010 
# twos = (000 ^ 010) & ~(010) = 010 & 101 = 000

# ones = (010 ^ 010) & ~(000) = 000 & 111 = 000
# twos = (000 ^ 010) & ~(000) = 010 & 111 = 010



class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ones = 0
        twos = 0
        
        for num in nums:
            ones = (ones ^ num) & ~twos
            twos = (twos ^ num) & ~ones

        return ones
