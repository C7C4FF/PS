# https://leetcode.com/problems/count-the-number-of-good-subarrays/?envType=daily-question&envId=2025-04-16
# 새로운 수가 한번 더 들어오면, 쌍이 원래 있던 num 갯수 만큼 더 생김
# 2-1, 2-2 : 1쌍 - 2개, 여기서 3번째 2-3 이 들어오면 
# 원래 있던 2들과 쌍을 이루기 때문에 (2-1, 2-2), (2-1, 2-3), (2-2, 2-3) 로 3 쌍이 됨. 

class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        l = pair = ans = 0
        cnt = Counter()

        for r, num in enumerate(nums):
            pair += cnt[num]
            cnt[num] += 1

            # 현재 r 위치에서 k 개 이상의 쌍이 있으면, 
            # 그 이후의 인덱스는 모두 만족함.
            # 왼쪽 포인터를 앞으로 당기며 계속 확인
            while pair >= k:
                ans += len(nums) - r
                cnt[nums[l]] -= 1
                pair -= cnt[nums[l]]
                l += 1

        return ans
