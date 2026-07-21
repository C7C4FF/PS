# https://leetcode.com/problems/maximize-active-section-with-trade-i/description/?envType=daily-question&envId=2026-07-21
# 1이면 +1, 0이면 -1로 연속된 범위를 구하기
# 그 이후에 음수 인덱스 2개씩 찾아서 전체 1의 갯수에 그 절대값을 더해서 가장 큰 값을 찾기

class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        nums = []
        ans = float('-inf')

        start, continuous = s[0], 1 if s[0] == '1' else -1
        for n in range(1, len(s)):
            this = s[n]
            
            if start == this:
                if s[n] == '1':
                    continuous += 1
                else:
                    continuous -= 1
            else:
                nums.append(continuous)
                start, continuous = s[n], 1 if s[n] == '1' else -1
        
        nums.append(continuous)

        total_ones = sum(v for v in nums if v > 0)
        neg = [idx for idx, v in enumerate(nums) if v < 0]

        ans = total_ones

        for i in range(len(neg) - 1):
            left, right = neg[i], neg[i + 1]

            added = abs(nums[left]) + abs(nums[right])
            ans = max(ans, total_ones + added)

        return ans
        


            
                    

        
