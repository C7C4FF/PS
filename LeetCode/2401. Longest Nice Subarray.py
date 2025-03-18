# https://leetcode.com/problems/longest-nice-subarray/?envType=daily-question&envId=2025-03-18
# [a, b, c] 가 있다면 (a, b), (b, c), (a, c) 전부 bitwise AND 결과가 0이어야 함.
# 모든 수의 비트가 1이 겹치면 안 되니 지나온 수에 대해 계속해서 OR 연산을 더해주고, 
# OR == 0 이라면 +1, 아니라면 겹치는 게 있다는 뜻이므로 반복문 중단

class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        lst = []
        n = len(nums)

        for i in range(n):
            cnt = 1
            curr_or = nums[i]
            for j in range(i+1, n):
                # 현재까지 모든 비트와 겹치는 것이 없는지 확인
                if curr_or & nums[j] == 0:
                    curr_or |= nums[j] # or 업데이트
                    cnt += 1
                else:
                    break

            lst.append(cnt)
        
        return max(lst)
