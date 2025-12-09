# 처음에 전부 오른쪽으로 두고.. 한번 지나갈 때마다 왼쪽으로 옮겨주기

class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        freqPrev, freqNext = Counter(), Counter(nums)
        cnt = 0

        for num in nums:
            freqNext[num] -= 1
            cnt += freqPrev[num * 2] * freqNext[num * 2]
            freqPrev[num] += 1
        
        return cnt % (10**9 + 7)
